"""Audit the historical local prerequisites and current global-gap status."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent


def read(sprint: int, filename: str) -> dict:
    return json.loads((FRONTIER / f"foundational-sprint-{sprint}" / filename).read_text(encoding="utf-8"))


def main() -> None:
    contact = read(1195, "contact-covariance.json")
    connection = read(1116, "validated-exact-shooting-degree.json")
    graph = read(1192, "exact-invariant-graph-projection.json")
    wing = read(1193, "exact-boundary-wing.json")
    outer = read(1194, "inactive-outer-guard.json")
    hyperbolic = read(1115, "plateau-hyperbolicity-certificate.json")
    amplitude_gap = read(1285, "wide-bracket-amplitude-exclusion.json")

    gates = {
        "exact_contact_covariance": contact["all_exact_checks_zero"],
        "exact_connection_miranda_faces": connection["miranda_conditions"] and all(
            face["opposite_sign_certified"] for face in connection["face_checks"]
        ),
        "one_unstable_plateau_direction": hyperbolic["root_count"]["above_one"] == 1,
        "central_graph_certified": graph["all_tiles_certified"] and graph["corrected_plateau_to_section_plus_reflection"],
        "boundary_wing_exists_unique": wing["existence_by_IVT"] and wing["uniqueness_in_bracket"],
        "boundary_wing_graph_certified": wing["complete_right_wing_graph"] and wing["failure_count"] == 0,
        "inactive_outer_guard": outer["successor_monotonicity_repair"] and outer["right_outer_contacts_excluded"] and outer["left_outer_contacts_excluded_by_reflection"],
        "positive_pivots_central": all(piece["minimum_pivot_lower"] > 0 for piece in graph["pieces"]),
        "positive_pivots_wing": all(piece["minimum_pivot_lower"] > 0 for piece in wing["pieces"]),
    }
    local_pass = all(gates.values())
    report = {
        "status": "historical local aligned-wall gates with global amplitude gap",
        "gates": gates,
        "all_gates_pass": local_pass,
        "historical_local_gates_pass": local_pass,
        "global_amplitude_compatibility": False,
        "headline_assembly_closed": False,
        "gap_receipt_passes": amplitude_gap["all_gates_pass"],
        "q_interval_from_validated_connection": connection["rectangle"]["Q"],
        "claim_boundary": (
            "These historical gates certify local chart geometry only. Sprint "
            "1285 proves that their global amplitude compatibility equation "
            "fails, so they do not presently assemble a continuous Bellman "
            "fixed point or certify the unrestricted quantum value."
        ),
    }
    output = HERE / "theorem-assembly.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not (report["historical_local_gates_pass"] and report["gap_receipt_passes"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
