"""Custody gate for the finite-dimensional nonattainment theorem."""

from __future__ import annotations

from decimal import Decimal, getcontext
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    getcontext().prec = 80
    equality = load(HERE / "equality-kernel-audit.json")
    supremum = load(
        ROOT / "certificate" / "production" / "foundational-sprint-1197" / "theorem-assembly.json"
    )
    shooting = load(
        ROOT
        / "certificate"
        / "production"
        / "foundational-sprint-1116"
        / "validated-exact-shooting-degree.json"
    )
    q_text = shooting["rectangle"]["Q"]
    match = re.fullmatch(r"\[([0-9.]+) \+/- ([0-9.eE+-]+)\]", q_text)
    if match is None:
        raise ValueError(f"unexpected Q interval: {q_text}")
    midpoint, radius = Decimal(match.group(1)), Decimal(match.group(2))
    lower = midpoint - radius

    gates = {
        "tensor_product_supremum_certificate": bool(supremum["all_gates_pass"]),
        "equality_kernel_scalar_audit": bool(equality["all_gates_pass"]),
        "validated_wall_strictly_above_one_quarter": lower > Decimal("0.25"),
        "theorem_document_present": (HERE / "FINITE-DIMENSIONAL-NONATTAINMENT.md").is_file(),
        "registration_present": (HERE / "PRE-REGISTRATION.md").is_file(),
    }
    report = {
        "status": "machine-readable custody gate for finite-dimensional nonattainment",
        "gates": gates,
        "q_interval": q_text,
        "q_lower_minus_one_quarter": str(lower - Decimal("0.25")),
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Finite-dimensional tensor-product nonattainment only; no claim "
            "about commuting-operator attainment or physical realization."
        ),
    }
    output = HERE / "theorem-assembly.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
