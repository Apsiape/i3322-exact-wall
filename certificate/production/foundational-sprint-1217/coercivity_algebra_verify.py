#!/usr/bin/env python3
"""Exact algebra guards for Bellman-gap assembly and coercivity constants."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Q = Fraction


def main() -> None:
    rng = random.Random(1217)
    cauchy_checks = 0
    bregman_checks = 0

    # Q-sqrt((Q-d1)(Q-d2)) >= (d1+d2)/2.
    for _ in range(5000):
        q = Q(rng.randint(1, 100), rng.randint(1, 30))
        d1 = q * Q(rng.randint(0, 100), 100)
        d2 = q * Q(rng.randint(0, 100), 100)
        # Square the equivalent nonnegative comparison to stay rational.
        arithmetic_mean = q - (d1 + d2) / 2
        product = (q - d1) * (q - d2)
        assert arithmetic_mean >= 0
        assert arithmetic_mean * arithmetic_mean - product == (d1 - d2) ** 2 / 4
        cauchy_checks += 1

    # Quadratic strongly concave fixtures attain the Bregman coefficient.
    for _ in range(1000):
        curvature = Q(rng.randint(1, 20), 10)  # >=1/10
        y = Q(rng.randint(-20, 20), 20)
        u = Q(rng.randint(-20, 20), 20)
        # F(t)=linear-curvature*t^2/2; linear part cancels.
        f_y = -curvature * y * y / 2
        fp_y = -curvature * y
        f_u = -curvature * u * u / 2
        gap = f_y + fp_y * (u - y) - f_u
        assert gap == curvature * (u - y) ** 2 / 2
        assert gap >= (u - y) ** 2 / 20
        bregman_checks += 1

    m = Q(1, 10)
    lipschitz = Q(2)
    one_gap_contact_constant = m / (2 * lipschitz * lipschitz)
    r0_contact_constant = one_gap_contact_constant / 2
    assert one_gap_contact_constant == Q(1, 80)
    assert r0_contact_constant == Q(1, 160)

    report = {
        "status": "exact-rational Bellman coercivity algebra guard",
        "cauchy_gap_checks": cauchy_checks,
        "strong_concavity_checks": bregman_checks,
        "one_gap_contact_constant": str(one_gap_contact_constant),
        "r0_two_contact_constant": str(r0_contact_constant),
        "all_gates_pass": cauchy_checks == 5000 and bregman_checks == 1000,
        "claim_boundary": (
            "This verifies the algebra and constants. The derivative bounds are "
            "owned separately by predecessor_derivative_interval.py."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "coercivity-algebra-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
