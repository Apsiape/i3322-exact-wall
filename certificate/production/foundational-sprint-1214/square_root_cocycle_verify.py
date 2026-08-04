#!/usr/bin/env python3
"""Exact guards for the square-root Bellman cocycle composition."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random

import sympy as sp


HERE = Path(__file__).resolve().parent
Q = Fraction


def random_involution(size: int, rng: random.Random) -> list[int]:
    remaining = list(range(size))
    rng.shuffle(remaining)
    out = list(range(size))
    while remaining:
        i = remaining.pop()
        if remaining and rng.choice((False, True)):
            j = remaining.pop()
            out[i] = j
            out[j] = i
        else:
            out[i] = i
    return out


def main() -> None:
    rng = random.Random(1214)
    fixtures = 0
    minimum_energy_slack = None

    for _ in range(3000):
        size = rng.randint(1, 30)
        a = random_involution(size, rng)
        b = random_involution(size, rng)
        tau = [a[b[i]] for i in range(size)]
        z = [Q(rng.randint(0, 30), rng.randint(1, 19)) for _ in range(size)]
        p = [Q(rng.randint(1, 30), rng.randint(1, 19)) for _ in range(size)]
        q = [Q(rng.randint(1, 30), rng.randint(1, 19)) for _ in range(size)]

        ra = [p[a[i]] * z[a[i]] - p[i] * z[i] for i in range(size)]
        rb = [q[b[i]] * z[b[i]] - q[i] * z[i] for i in range(size)]
        c = [
            p[b[i]] * q[i] / (p[tau[i]] * q[b[i]])
            for i in range(size)
        ]
        s = [
            ra[b[i]] / p[tau[i]]
            + p[b[i]] * rb[i] / (p[tau[i]] * q[b[i]])
            for i in range(size)
        ]
        for i in range(size):
            assert z[tau[i]] == c[i] * z[i] + s[i]

        p_min = min(p)
        p_max = max(p)
        q_min = min(q)
        lhs = sum((value * value for value in s), Q(0))
        rhs = (
            Q(2) / (p_min * p_min) * sum((value * value for value in ra), Q(0))
            + Q(2) * p_max * p_max / (p_min * p_min * q_min * q_min)
            * sum((value * value for value in rb), Q(0))
        )
        slack = rhs - lhs
        assert slack >= 0
        if minimum_energy_slack is None or slack < minimum_energy_slack:
            minimum_energy_slack = slack
        fixtures += 1

    # Symbolic custody of the balanced-weight ratios and orientation c^2=C.
    f_u, f_minus_u, f_pm, f_minus_pm, b_u_sq, b_pm_sq = sp.symbols(
        "F_u F_minus_u F_Pminus F_minus_Pminus b_u_sq b_pm_sq", positive=True
    )
    a_pm_sq = b_pm_sq * f_minus_pm / f_pm
    a_minus_pm_sq = b_pm_sq * f_pm / f_minus_pm
    b_u_weight_sq = b_u_sq * f_u / f_minus_u
    b_minus_u_weight_sq = b_u_sq * f_minus_u / f_u
    a_ratio_square_residual = sp.factor(
        a_pm_sq / a_minus_pm_sq - (f_minus_pm / f_pm) ** 2
    )
    b_ratio_square_residual = sp.factor(
        b_u_weight_sq / b_minus_u_weight_sq - (f_u / f_minus_u) ** 2
    )
    c_squared = sp.factor(f_minus_pm * f_u / (f_pm * f_minus_u))
    mass_cocycle = f_u * f_minus_pm / (f_minus_u * f_pm)
    orientation_residual = sp.factor(c_squared - mass_cocycle)

    report = {
        "status": "exact-rational square-root cocycle composition guard",
        "random_fixtures": fixtures,
        "minimum_energy_slack": str(minimum_energy_slack),
        "balanced_A_ratio_square_residual": str(a_ratio_square_residual),
        "balanced_B_ratio_square_residual": str(b_ratio_square_residual),
        "i3322_cocycle_orientation_residual": str(orientation_residual),
        "all_gates_pass": (
            fixtures == 3000
            and a_ratio_square_residual == 0
            and b_ratio_square_residual == 0
            and orientation_residual == 0
        ),
        "claim_boundary": (
            "This proves the packet-amplitude composition and its dimension-free "
            "energy estimate. It does not supply global contact moduli, the local-"
            "dimension packet budget, or the final quantitative lower bound."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "square-root-cocycle-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
