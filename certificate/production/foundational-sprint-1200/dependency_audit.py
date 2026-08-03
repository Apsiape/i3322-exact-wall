"""Machine-readable custody and strict-contact audit for Sprints 1195--1199."""

from __future__ import annotations

from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent


def load(sprint: int, name: str) -> dict:
    path = FRONTIER / f"foundational-sprint-{sprint}" / name
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    payload = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    getcontext().prec = 80
    graph = load(1192, "exact-invariant-graph-projection.json")
    wing = load(1193, "exact-boundary-wing.json")
    outer = load(1194, "inactive-outer-guard.json")
    aligned = load(1195, "theorem-assembly.json")
    tensor = load(1197, "theorem-assembly.json")
    finite = load(1198, "theorem-assembly.json")
    commuting = load(1199, "theorem-assembly.json")

    central_rows = [graph["local_plateau_piece"], *graph["pieces"]]
    strict_central = all(
        row["largest_dx_upper"] < 0 and row["largest_dy_upper"] < 0
        for row in central_rows
    )
    strict_wing = all(
        row["largest_dx_upper"] < 0 and row["largest_dy_upper"] < 0
        for row in wing["pieces"]
    )

    q_text = tensor["q_interval"]
    match = re.fullmatch(r"\[([0-9.]+) \+/- ([0-9.eE+-]+)\]", q_text)
    if match is None:
        raise ValueError(q_text)
    lower = Decimal(match.group(1)) - Decimal(match.group(2))

    gates = {
        "strict_central_contact_graph": strict_central and graph["all_tiles_certified"],
        "strict_boundary_wing_graph": strict_wing and wing["complete_right_wing_graph"],
        "inactive_contacts_excluded": (
            outer["right_outer_contacts_excluded"]
            and outer["left_outer_contacts_excluded_by_reflection"]
        ),
        "aligned_bellman_dependency": aligned["all_gates_pass"],
        "tensor_operator_certificate": tensor["all_gates_pass"],
        "finite_nonattainment_certificate": finite["all_gates_pass"],
        "commuting_extension_certificate": commuting["all_gates_pass"],
        "wall_strictly_above_quarter": lower > Decimal("0.25"),
    }

    sources = [
        FRONTIER / "foundational-sprint-1195" / "EXACT-ALIGNED-WALL-THEOREM.md",
        FRONTIER / "foundational-sprint-1197" / "EXACT-I3322-QUANTUM-SUPREMUM.md",
        FRONTIER / "foundational-sprint-1198" / "FINITE-DIMENSIONAL-NONATTAINMENT.md",
        FRONTIER / "foundational-sprint-1199" / "COMMUTING-I3322-THEOREM.md",
    ]
    report = {
        "status": "adversarial dependency and strict-contact audit",
        "gates": gates,
        "q_interval": q_text,
        "q_lower_minus_quarter": str(lower - Decimal("0.25")),
        "source_sha256": {
            path.relative_to(FRONTIER.parent.parent).as_posix(): digest(path)
            for path in sources
        },
        "all_gates_pass": all(gates.values()),
        "scope_repair": (
            "State the commuting theorem for its standard PVM presentation; "
            "do not make a separate general POVM-dilation claim load-bearing."
        ),
    }
    output = HERE / "dependency-audit.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
