#!/usr/bin/env python3
"""Exact symbolic certificate for the positive I3322 plateau branch.

The proof uses SymPy only to verify polynomial identities and rational signs.
It does not treat numerical eigensolver output as a certificate.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def sign_at(expr: sp.Expr, symbol: sp.Symbol, value: sp.Rational) -> int:
    evaluated = sp.factor(expr.subs(symbol, value))
    if evaluated > 0:
        return 1
    if evaluated < 0:
        return -1
    return 0


def main() -> None:
    c, r, q, t = sp.symbols("c r q t", real=True)
    s = sp.sqrt(1 - c**2)

    plateau_1 = q - (c**2 - 1 + s * (r + 1 / r) / 2)
    plateau_2 = (1 + 2 * c) * r**2 - (1 - 2 * c) - 2 * c * r / s

    r_low = s / (c + 1)
    r_high = s * (2 * c - 1) / ((1 - c) * (2 * c + 1))
    q_high = (4 * c**4 - 5 * c**2 + 2) / (4 * c**2 - 1)

    # Both roots of the ratio equation are obtained algebraically. The first
    # gives q=c^2; the second gives the branch used by the domain wall.
    assert sp.simplify(plateau_2.subs(r, r_low)) == 0
    assert sp.simplify(plateau_1.subs({r: r_low, q: c**2})) == 0
    assert sp.simplify(plateau_2.subs(r, r_high)) == 0
    assert sp.simplify(plateau_1.subs({r: r_high, q: q_high})) == 0

    derivative = sp.factor(sp.diff(q_high, c))
    expected_derivative = (
        2 * c * (4 * c**2 - 3) * (4 * c**2 + 1)
        / ((2 * c - 1) ** 2 * (2 * c + 1) ** 2)
    )
    assert sp.simplify(derivative - expected_derivative) == 0

    # Rebuild the exact map and its Jacobian, then restrict it to the high
    # plateau branch.
    x, y, u = sp.symbols("x y u", real=True)
    sx = sp.sqrt(1 - x**2)
    sy = sp.sqrt(1 - y**2)
    diagonal = x * y + (x - y) / 2 - 1
    v = 2 * (q - diagonal - sx / (2 * u)) / sy
    z = (((1 - 2 * x) + 2 * y * v / sy) / v**2 - 1) / 2
    jacobian = sp.Matrix([y, z, v]).jacobian([x, y, u])
    jacobian_fixed = sp.simplify(
        jacobian.subs({x: c, y: c, u: r_high, q: q_high})
    )
    charpoly = jacobian_fixed.charpoly()
    characteristic = sp.factor(charpoly.as_expr().subs(charpoly.gen, t))

    linear = (4 * c**3 - 3 * c + 1) * t + (4 * c**3 - 3 * c - 1)
    quadratic = (
        (4 * c**3 - 3 * c + 1) * t**2
        + 4 * c**2 * (1 - 4 * c**2) * t
        + (-4 * c**3 + 3 * c + 1)
    )
    denominator = (c + 1) ** 2 * (2 * c - 1) ** 4
    assert sp.simplify(characteristic - linear * quadratic / denominator) == 0

    a = sp.factor(4 * c**3 - 3 * c + 1)
    d = sp.factor(-4 * c**3 + 3 * c + 1)
    quadratic_at_one = sp.factor(quadratic.subs(t, 1))
    assert sp.simplify(a - (c + 1) * (2 * c - 1) ** 2) == 0
    assert sp.simplify(d - (1 - c) * (2 * c + 1) ** 2) == 0
    assert sp.simplify(
        quadratic_at_one + 2 * (2 * c**2 - 1) * (4 * c**2 + 1)
    ) == 0

    # Exact rational enclosure corresponding to a deliberately wider Q window
    # than the final sprint-1114 decimal. Monotonicity on c>sqrt(3)/2 turns
    # endpoint signs into a root enclosure.
    q_lo = sp.Rational(250875384513, 10**12)
    q_hi = sp.Rational(250875384515, 10**12)
    c_lo = sp.Rational(878272945173, 10**12)
    c_hi = sp.Rational(878272945189, 10**12)
    numerator = sp.together(q_high - q).as_numer_denom()[0]
    assert sign_at(numerator.subs(q, q_lo), c, c_lo) < 0
    assert sign_at(numerator.subs(q, q_lo), c, c_hi) > 0
    assert sign_at(numerator.subs(q, q_hi), c, c_lo) < 0
    assert sign_at(numerator.subs(q, q_hi), c, c_hi) > 0
    assert c_lo > sp.sqrt(3) / 2 and c_hi < 1

    # On the complete high branch sqrt(3)/2<c<1:
    # - the linear root d/a lies strictly in (0,1), because a,d>0 and a-d>0;
    # - the quadratic has positive value at 0 and negative value at 1;
    # - its positive leading coefficient then forces one root in (0,1) and
    #   one root in (1,infinity).
    assert sp.simplify((a - d) - 2 * c * (4 * c**2 - 3)) == 0

    c_mid = sp.N((c_lo + c_hi) / 2, 50)
    numeric_roots = [
        complex(root)
        for root in sp.nroots(sp.Poly(linear * quadratic, t).subs(c, c_mid), n=40)
    ]
    numeric_roots.sort(key=abs, reverse=True)

    result = {
        "status": "exact algebraic plateau and exact branch-wide hyperbolicity",
        "q_interval": [str(q_lo), str(q_hi)],
        "c_interval": [str(c_lo), str(c_hi)],
        "ratio_branches": {
            "low": str(r_low),
            "domain_wall": str(r_high),
        },
        "q_domain_wall": str(q_high),
        "q_derivative": str(derivative),
        "characteristic_numerator_factorization": str(linear * quadratic),
        "branch": "sqrt(3)/2 < c < 1",
        "root_count": {
            "inside_unit_interval": 2,
            "above_one": 1,
            "argument": "exact endpoint signs of one linear and one quadratic factor",
        },
        "reference_multipliers": [
            {"real": root.real, "imag": root.imag, "abs": abs(root)}
            for root in numeric_roots
        ],
        "claims_not_made": [
            "the connection Q lies in the displayed Q interval",
            "the unstable manifold reaches the reflection section",
            "global I3322 optimality",
        ],
    }
    (HERE / "plateau-hyperbolicity-certificate.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
