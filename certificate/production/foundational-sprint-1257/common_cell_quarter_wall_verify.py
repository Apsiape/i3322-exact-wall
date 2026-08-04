#!/usr/bin/env python3
"""Exact-rational guard for the common-cell quarter wall."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def main() -> None:
    order = Q(182, 5)
    logarithmic = Q(169, 50)
    vertical = logarithmic / 2
    lip_a = Q(20)
    lip_log_alpha = Q(14)
    lip_log_beta = Q(7)

    order_tax = order * (lip_a + 1)
    resolution_tax = logarithmic * (lip_log_alpha + lip_log_beta)
    cell_tax = order_tax + resolution_tax
    cutoff = Q(1, 2) / cell_tax

    assert vertical == Q(169, 100)
    assert cell_tax == Q(41769, 50)
    assert cutoff == Q(25, 41769)

    # Hostile exact fixtures check the two triangle/Lipschitz substitutions.
    # Synthetic values saturate independently signed Lipschitz envelopes; no
    # numerical evaluation of the already-certified wall is being smuggled in.
    rng = random.Random(1257)
    fixtures = 100_000
    minimum_order_slack = None
    minimum_resolution_slack = None
    for _ in range(fixtures):
        h = Q(rng.randint(1, 100), 100)
        dy = Q(rng.randint(-100, 100), 100) * h
        du = Q(rng.randint(-100, 100), 100) * h
        assert abs(dy) <= h and abs(du) <= h

        # Base event debts are arbitrary; representative perturbations take
        # every allowed sign to attack the triangle estimate.
        horizontal = Q(rng.randint(-1000, 1000), 100)
        vertical_log = Q(rng.randint(-1000, 1000), 100)
        da = Q(rng.randint(-2000, 2000), 100) * abs(dy) / 20
        dla = Q(rng.randint(-1400, 1400), 100) * abs(dy) / 14
        dlb = Q(rng.randint(-700, 700), 100) * abs(du) / 7
        assert abs(da) <= lip_a * abs(dy)
        assert abs(dla) <= lip_log_alpha * abs(dy)
        assert abs(dlb) <= lip_log_beta * abs(du)

        representative_order = horizontal + da - du
        representative_log = vertical_log + dla - dlb
        order_slack = abs(horizontal) + (lip_a + 1) * h - abs(representative_order)
        resolution_slack = (
            abs(vertical_log)
            + (lip_log_alpha + lip_log_beta) * h
            - abs(representative_log)
        )
        assert order_slack >= 0
        assert resolution_slack >= 0
        if minimum_order_slack is None or order_slack < minimum_order_slack:
            minimum_order_slack = order_slack
        if minimum_resolution_slack is None or resolution_slack < minimum_resolution_slack:
            minimum_resolution_slack = resolution_slack

    gates = {
        "vertical_coefficient": vertical == Q(169, 100),
        "cell_diameter_tax": cell_tax == Q(41769, 50),
        "half_gap_cutoff": cutoff == Q(25, 41769),
        "order_substitution": minimum_order_slack is not None and minimum_order_slack >= 0,
        "resolution_substitution": (
            minimum_resolution_slack is not None and minimum_resolution_slack >= 0
        ),
    }
    report = {
        "status": "exact-rational common-cell quarter-wall guard",
        "fixtures": fixtures,
        "order_coefficient": str(order),
        "vertical_coefficient": str(vertical),
        "cell_diameter_tax": str(cell_tax),
        "half_gap_width_coefficient": str(cutoff),
        "minimum_order_substitution_slack": str(minimum_order_slack),
        "minimum_resolution_substitution_slack": str(minimum_resolution_slack),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The pointwise wall survives a common cell. Response-flow total "
            "variation and the universal dimension lower bound remain open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "common-cell-quarter-wall-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
