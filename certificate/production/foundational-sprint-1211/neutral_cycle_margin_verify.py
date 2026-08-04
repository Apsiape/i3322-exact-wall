#!/usr/bin/env python3
"""Symbolic identities and high-precision guards for neutral-cycle margin."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random

import mpmath as mp
import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    B, rho, delta, Q, ep, em = sp.symbols(
        "B rho delta Q E_plus E_minus", positive=True
    )
    delta0 = B * (1 / rho - rho)
    S0 = B * (rho + 1 / rho) / 2
    ep_formula = Q - delta / 2 - rho * B
    em_formula = Q + delta / 2 - B / rho

    sum_residual = sp.factor(
        Q - S0 - (ep_formula + em_formula) / 2
    )
    difference_residual = sp.factor(
        delta - delta0 - (em_formula - ep_formula)
    )
    s0_square_residual = sp.factor(S0**2 - (B**2 + delta0**2 / 4))

    x, u, sx, su = sp.symbols("x u s_x s_u", real=True)
    t = 1 - x * u
    bsum = (sx + su) / 2
    scalar_square = bsum**2 + (x - u) ** 2 / 4
    target_square = (t + sx * su) / 2
    unit_relations = [sx**2 - (1 - x**2), su**2 - (1 - u**2)]
    groebner = sp.groebner(unit_relations, sx, su, x, u, domain=sp.QQ)
    scalar_square_residual = sp.factor(groebner.reduce(sp.expand(scalar_square - target_square))[1])
    order_identity_residual = sp.factor(
        sp.expand(t**2 - sx**2 * su**2 - (x - u) ** 2)
    )
    order_identity_residual = sp.factor(groebner.reduce(order_identity_residual)[1])

    q_lower = Fraction("0.250875384513976535514")
    quarter_margin = q_lower - Fraction(1, 4)
    assert quarter_margin > 0

    mp.mp.dps = 80
    rng = random.Random(1211)
    maximum_violation = mp.mpf("0")
    minimum_margin_seen = mp.inf
    checks = 0
    fixtures = [
        (mp.mpf("0"), mp.mpf("0"), mp.mpf("1")),
        (mp.mpf("1"), mp.mpf("-1"), mp.mpf("1e-20")),
        (mp.mpf("-1"), mp.mpf("1"), mp.mpf("1e20")),
        (mp.sqrt(3) / 2, mp.sqrt(3) / 2, mp.mpf("1")),
        (-mp.sqrt(3) / 2, -mp.sqrt(3) / 2, mp.mpf("1")),
    ]
    for _ in range(5000):
        fixtures.append(
            (
                mp.mpf(rng.uniform(-1, 1)),
                mp.mpf(rng.uniform(-1, 1)),
                mp.power(10, mp.mpf(rng.uniform(-12, 12))),
            )
        )

    q_value = mp.mpf("0.250875384513976535514")
    for xv, uv, rhov in fixtures:
        bx = mp.sqrt(max(mp.mpf("0"), 1 - xv * xv)) / 2
        bu = mp.sqrt(max(mp.mpf("0"), 1 - uv * uv)) / 2
        bval = bx + bu
        dval = xv - uv
        qshift = q_value - xv * uv + 1
        eplus = qshift - dval / 2 - rhov * bval
        eminus = qshift + dval / 2 - bval / rhov
        phi = xv * uv - 1 + mp.sqrt(bval * bval + dval * dval / 4)
        closure = q_value - phi
        rhs = max(abs(eplus), abs(eminus))
        violation = max(mp.mpf("0"), closure - rhs)
        maximum_violation = max(maximum_violation, violation)
        minimum_margin_seen = min(minimum_margin_seen, closure)
        checks += 1

    report = {
        "status": "exact neutral-cycle identities plus 80-digit hostile guard",
        "sum_identity_residual": str(sum_residual),
        "difference_identity_residual": str(difference_residual),
        "S0_square_residual": str(s0_square_residual),
        "scalar_square_residual_mod_unit_circles": str(scalar_square_residual),
        "order_identity_residual_mod_unit_circles": str(order_identity_residual),
        "certified_lower_margin": str(quarter_margin),
        "high_precision_checks": checks,
        "maximum_detected_violation": mp.nstr(maximum_violation, 20),
        "minimum_closure_margin_seen": mp.nstr(minimum_margin_seen, 30),
        "all_gates_pass": (
            sum_residual == 0
            and difference_residual == 0
            and s0_square_residual == 0
            and scalar_square_residual == 0
            and order_identity_residual == 0
            and maximum_violation == 0
            and quarter_margin > 0
        ),
        "claim_boundary": (
            "This proves and guards the scalar neutral-cycle margin. It does not "
            "yet transfer arbitrary operator deficit to a cycle decomposition or "
            "prove a dimension lower bound."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "neutral-cycle-margin-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
