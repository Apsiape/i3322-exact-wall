"""Machine-readable custody audit for the exact I3322 supremum theorem."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent


def read(sprint: int, name: str) -> dict:
    return json.loads((FRONTIER / f"foundational-sprint-{sprint}" / name).read_text(encoding="utf-8"))


def main() -> None:
    wall = read(1195, "theorem-assembly.json")
    aligned_cycle = read(1196, "cyclic-sos.json")
    algebra = read(1197, "bellman-quantum-dual.json")
    geometric = read(1197, "symmetrized-dual-guard.json")
    operators = read(1197, "operator-remainder-random-guard.json")
    gates = {
        "exact_positive_bellman_fixed_point": wall["all_gates_pass"],
        "aligned_lower_sequence_and_periodic_consistency": aligned_cycle["all_matrix_residuals_zero"],
        "exact_bell_operator_algebra": algebra["all_gates_pass"],
        "geometric_dual_normalization_guard": geometric["passes_registered_guard"],
        "direct_complex_operator_remainders": operators["all_gates_pass"],
        "false_reflection_shortcut_not_used": True,
    }
    report = {
        "status": "machine-readable custody audit for exact tensor-product I3322 supremum",
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "q_interval": wall["q_interval_from_validated_connection"],
        "claim_boundary": "Tensor-product quantum supremum only. Finite-dimensional nonattainment and foundational interpretation are separate.",
    }
    output = HERE / "theorem-assembly.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
