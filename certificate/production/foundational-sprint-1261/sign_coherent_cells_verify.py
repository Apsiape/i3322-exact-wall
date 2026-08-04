#!/usr/bin/env python3
"""Exact-rational guard for the sign-coherent cell theorem."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def main() -> None:
    K = Q(182, 5)
    G = Q(169, 100)
    m0 = Q(7, 8000)  # safe rational below the certified wall margin
    theta = m0 / (4 * K)
    g = m0 / (4 * G)
    h = Q(25) * m0 / Q(41769)

    assert theta == Q(5, 728) * m0
    assert g == Q(25, 169) * m0
    assert 42 * h < g

    rng = random.Random(1261)
    fixtures = 50_000
    minimum_wall_slack = None
    minimum_cancellation_slack = None

    for _ in range(fixtures):
        B = Q(rng.randint(1, 30), 7)
        # A synthetic cell contains small events of one vertical orientation
        # and arbitrarily oriented large events.  Masses and debts are exact.
        small_count = rng.randint(0, 12)
        large_count = rng.randint(0, 12)
        small_sign = -1 if rng.randrange(2) else 1
        M_s = Q(0)
        M_l = Q(0)
        D_h = Q(0)
        vertical_small = Q(0)
        vertical_large = Q(0)

        for _j in range(small_count):
            mass = Q(rng.randint(1, 50), 31)
            horizontal = theta * Q(rng.randint(0, 99), 100)
            vertical_min = (m0 / 2 - K * horizontal) / G
            vertical = vertical_min + Q(rng.randint(0, 100), 100) * max(B, g)
            vertical = min(vertical, 2 * B)
            # If the randomly chosen B is too small to host the certified gap,
            # enlarge it; this is a theorem guard, not an I3322 box sampler.
            if vertical < vertical_min:
                B = vertical_min
                vertical = vertical_min
            wall_slack = K * horizontal + G * vertical - m0 / 2
            assert wall_slack >= 0
            M_s += mass
            D_h += mass * horizontal
            vertical_small += mass * small_sign * vertical
            if minimum_wall_slack is None or wall_slack < minimum_wall_slack:
                minimum_wall_slack = wall_slack

        for _j in range(large_count):
            mass = Q(rng.randint(1, 50), 31)
            horizontal = theta * Q(rng.randint(100, 500), 100)
            vertical = Q(rng.randint(-200, 200), 100) * B
            M_l += mass
            D_h += mass * horizontal
            vertical_large += mass * vertical

        assert M_l <= D_h / theta
        observed_area_lower = abs(vertical_small + vertical_large)
        theorem_prebound = g * M_s - 2 * B * M_l
        cancellation_slack = observed_area_lower - theorem_prebound
        assert cancellation_slack >= 0
        if (
            minimum_cancellation_slack is None
            or cancellation_slack < minimum_cancellation_slack
        ):
            minimum_cancellation_slack = cancellation_slack

    gates = {
        "horizontal_threshold": theta == Q(5, 728) * m0,
        "vertical_gap": g == Q(25, 169) * m0,
        "cell_oscillation_below_gap": 42 * h < g,
        "hostile_wall_split": minimum_wall_slack is not None and minimum_wall_slack >= 0,
        "large_event_cancellation_billed": (
            minimum_cancellation_slack is not None and minimum_cancellation_slack >= 0
        ),
    }
    report = {
        "status": "exact-rational sign-coherent vertical-cell guard",
        "fixtures": fixtures,
        "safe_margin_m0": str(m0),
        "horizontal_threshold": str(theta),
        "vertical_gap": str(g),
        "certified_cell_width": str(h),
        "cell_oscillation": str(42 * h),
        "minimum_wall_split_slack": str(minimum_wall_slack),
        "minimum_cancellation_slack": str(minimum_cancellation_slack),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Cellwise vertical cancellation is blocked after billing large "
            "horizontal events. Common output-prefix control remains open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "sign-coherent-cells-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
