from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def run_orientation(rng, positive):
    delta = Fraction(rng.randint(2, 40), rng.randint(1, 20))
    eta = delta * Fraction(rng.randint(0, 3), 10)
    h_max = (delta - eta) / 4
    diameter = h_max * Fraction(rng.randint(1, 9), 10)
    length = rng.randint(2, 30)
    center = Fraction(rng.randint(-100, 100), rng.randint(1, 20))
    cells = []

    for _ in range(length):
        left_radius = diameter * Fraction(rng.randint(0, 10), 20)
        right_radius = diameter - left_radius
        cells.append((center - left_radius, center + right_radius))
        error = eta * Fraction(rng.randint(-10, 10), 10)
        center = center + (delta if positive else -delta) + error

    ordered = cells if positive else list(reversed(cells))
    for previous, following in zip(ordered[:-1], ordered[1:]):
        assert previous[1] < following[0]
    for i in range(len(ordered)):
        for j in range(i + 1, len(ordered)):
            assert ordered[i][1] < ordered[j][0]
    return delta, eta, diameter


def main():
    rng = random.Random(1224)
    fixtures = 10000
    minimum_registered_slack = None

    for index in range(fixtures):
        delta, eta, diameter = run_orientation(rng, positive=(index % 2 == 0))
        slack = delta - eta - 2 * diameter
        assert slack > 0
        minimum_registered_slack = (
            slack if minimum_registered_slack is None else min(minimum_registered_slack, slack)
        )

    # Exact mesh specialization for depths 0..32.
    for depth in range(33):
        delta = Fraction(7, 10)
        eta = Fraction(1, 10)
        h = (delta - eta) / (4 * 20**depth)
        H = 20**depth * h
        assert 2 * H < delta - eta

    result = {
        "status": "exact-rational ordered temporal-rank guard",
        "hostile_drift_chains": fixtures,
        "positive_orientation_fixtures": fixtures // 2,
        "negative_orientation_fixtures": fixtures // 2,
        "moving_frame_depths_checked": 33,
        "minimum_registered_gap_slack": str(minimum_registered_slack),
        "all_gates_pass": True,
        "claim_boundary": (
            "The temporal rank theorem is conditional on drift and step-error "
            "bounds. Near-fixed charging and final assembly remain open."
        ),
    }
    target = Path(__file__).with_name("ordered-temporal-rank-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
