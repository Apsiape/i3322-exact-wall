#!/usr/bin/env python3
"""Exact-rational guard for output-cell sign coherence."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def main() -> None:
    p_prime_min = Q(1, 10)
    p_prime_max = Q(2)
    inverse_lipschitz = p_prime_max / p_prime_min
    lip_p = Q(28)
    lip_q = Q(14)
    oscillation = lip_p * inverse_lipschitz + lip_q

    assert inverse_lipschitz == 20
    assert oscillation == 574

    m0 = Q(7, 8000)
    g = Q(25, 169) * m0
    delta = Q(25, 97006) * m0
    assert oscillation * delta == g

    rng = random.Random(1264)
    fixtures = 100_000
    minimum_oscillation_slack = None
    opposite_sign_rejections = 0

    for _ in range(fixtures):
        width = delta * Q(rng.randint(1, 100), 100)
        dy = inverse_lipschitz * width * Q(rng.randint(-100, 100), 100)
        du = width * Q(rng.randint(-100, 100), 100)
        dp = lip_p * dy
        dq = lip_q * du
        actual = abs(dp - dq)
        bound = oscillation * width
        slack = bound - actual
        assert slack >= 0
        if minimum_oscillation_slack is None or slack < minimum_oscillation_slack:
            minimum_oscillation_slack = slack

        first = g + Q(rng.randint(0, 1000), 1000) * g
        # An opposite-sign candidate differs by at least 2g and therefore
        # cannot fit inside the certified oscillation diameter <=g.
        second = -(g + Q(rng.randint(0, 1000), 1000) * g)
        if abs(first - second) > oscillation * width:
            opposite_sign_rejections += 1

    gates = {
        "inverse_lipschitz": inverse_lipschitz == 20,
        "shift_oscillation_constant": oscillation == 574,
        "registered_output_width": oscillation * delta == g,
        "hostile_oscillation_fixtures": (
            minimum_oscillation_slack is not None and minimum_oscillation_slack >= 0
        ),
        "opposite_sign_rejected": opposite_sign_rejections == fixtures,
    }
    report = {
        "status": "exact-rational output-cell sign-coherence guard",
        "fixtures": fixtures,
        "inverse_lipschitz_constant": str(inverse_lipschitz),
        "shift_oscillation_coefficient": str(oscillation),
        "safe_margin_m0": str(m0),
        "vertical_gap": str(g),
        "output_cell_width": str(delta),
        "minimum_oscillation_slack": str(minimum_oscillation_slack),
        "opposite_sign_rejections": opposite_sign_rejections,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Common output cells preserve vertical orientation. The final "
            "operator-error integral and universal lower bound remain open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "output-cell-sign-coherence-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
