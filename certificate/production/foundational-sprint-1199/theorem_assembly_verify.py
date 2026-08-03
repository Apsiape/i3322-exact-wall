"""Custody gate for the commuting-operator I3322 extension."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    supremum = load(
        ROOT / "certificate" / "production" / "foundational-sprint-1197" / "theorem-assembly.json"
    )
    nonattainment = load(
        ROOT / "certificate" / "production" / "foundational-sprint-1198" / "theorem-assembly.json"
    )
    commuting = load(HERE / "commuting-certificate-audit.json")
    gates = {
        "tensor_product_supremum_dependency": bool(supremum["all_gates_pass"]),
        "finite_equality_kernel_dependency": bool(nonattainment["all_gates_pass"]),
        "commutant_factorization_and_matrix_guards": bool(commuting["all_gates_pass"]),
        "theorem_document_present": (HERE / "COMMUTING-I3322-THEOREM.md").is_file(),
        "preregistration_present": (HERE / "PRE-REGISTRATION.md").is_file(),
    }
    report = {
        "status": "machine-readable custody gate for commuting-operator I3322",
        "gates": gates,
        "q_interval": supremum["q_interval"],
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Commuting-operator supremum and finite-dimensional nonattainment; "
            "no Connes-embedding, experimental, or foundational claim."
        ),
    }
    output = HERE / "theorem-assembly.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
