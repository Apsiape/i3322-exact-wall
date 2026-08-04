#!/usr/bin/env python3
"""Custody and exact-rational guards for the certified response-weight box."""

from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent
Q = Fraction


def read(sprint: int, name: str) -> dict:
    path = FRONTIER / f"foundational-sprint-{sprint}" / name
    return json.loads(path.read_text(encoding="utf-8"))


def interval_upper(text: str) -> Decimal:
    # Saved intervals use '[center +/- radius]'. Margins here exceed 1e-3.
    match = re.fullmatch(r"\[([^ ]+) \+/- ([^\]]+)\]", text)
    assert match is not None
    return Decimal(match.group(1)) + Decimal(match.group(2))


def main() -> None:
    central = read(1192, "exact-invariant-graph-projection.json")
    wing = read(1193, "exact-boundary-wing.json")
    outer = read(1194, "inactive-outer-guard.json")
    assembly = read(1195, "theorem-assembly.json")

    central_pivots = [
        Decimal(str(central["local_plateau_piece"]["minimum_pivot_lower"])),
        *[
            Decimal(str(piece["minimum_pivot_lower"]))
            for piece in central["pieces"]
        ],
    ]
    wing_pivots = [
        Decimal(str(piece["minimum_pivot_lower"])) for piece in wing["pieces"]
    ]
    outer_f_lower = Decimal(str(outer["minimum_F_target_lower"]))
    q_upper = interval_upper(assembly["q_interval_from_validated_connection"])
    terminal_upper = interval_upper(wing["terminal_predecessor_interval"])
    # The old tile engines serialized Arb endpoints through binary64. Charge a
    # deliberately excessive tax before using those summaries as rational
    # threshold custody. At these magnitudes binary64 conversion error is
    # below 1e-15; 1e-12 leaves three extra decimal orders.
    serialization_tax = Decimal("1e-12")

    ancestry_gates = {
        "central_complete": bool(central["corrected_plateau_to_section_plus_reflection"]),
        "wing_complete": bool(wing["complete_right_wing_graph"]),
        "outer_complete": bool(
            outer["right_outer_contacts_excluded"]
            and outer["left_outer_contacts_excluded_by_reflection"]
        ),
        "theorem_assembly": bool(assembly["all_gates_pass"]),
        "active_F_above_one_fifth": (
            min(central_pivots + wing_pivots) - serialization_tax
            > Decimal("0.2")
        ),
        "outer_F_above_one_fifth": (
            outer_f_lower - serialization_tax > Decimal("0.2")
        ),
        "q_below_0_251": q_upper < Decimal("0.251"),
        "predecessor_inside_0_9": (
            terminal_upper + serialization_tax < Decimal("0.9")
        ),
    }

    f_min = Q(1, 5)
    f_max = Q(13, 10)
    cutoff = Q(9, 10)
    b_min_sq = (1 - cutoff * cutoff) / 4
    response_min_sq = b_min_sq * f_min / f_max
    response_max_sq = Q(1, 4) * f_max / f_min
    response_min = Q(1, 12)
    response_max = Q(13, 10)
    assert response_min_sq > response_min * response_min
    assert response_max_sq < response_max * response_max

    alice_energy_constant = Q(2) / response_min
    bob_energy_constant = (
        Q(2) * response_max / (response_min * response_min)
    )
    cocycle_amplitude_max = f_max / f_min
    assert alice_energy_constant == 24
    assert bob_energy_constant == Q(1872, 5)
    assert cocycle_amplitude_max == Q(13, 2)

    report = {
        "status": "certificate-derived global Bellman/response-weight box",
        "ancestry_gates": ancestry_gates,
        "minimum_saved_active_pivot_lower": str(min(central_pivots + wing_pivots)),
        "minimum_saved_outer_F_lower": str(outer_f_lower),
        "validated_q_upper": str(q_upper),
        "terminal_predecessor_upper": str(terminal_upper),
        "legacy_float_serialization_tax": str(serialization_tax),
        "global_F_box": [str(f_min), str(f_max)],
        "contact_coordinate_cutoff": str(cutoff),
        "b_min_squared": str(b_min_sq),
        "response_min_squared_raw": str(response_min_sq),
        "response_max_squared_raw": str(response_max_sq),
        "safe_response_weight_box": [str(response_min), str(response_max)],
        "recurrence_energy_constants_A_B": [
            str(alice_energy_constant), str(bob_energy_constant)
        ],
        "cocycle_amplitude_max": str(cocycle_amplitude_max),
        "all_gates_pass": all(ancestry_gates.values()),
        "claim_boundary": (
            "This reuses the validated Bellman ancestry to certify conservative "
            "global weight and cocycle constants. It does not certify the "
            "off-contact r0 coercivity or final dimension inequality."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "certified-weight-box-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
