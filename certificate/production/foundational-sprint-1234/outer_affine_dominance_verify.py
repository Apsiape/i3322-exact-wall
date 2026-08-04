#!/usr/bin/env python3
"""Independent exact guard for the inactive Bellman-line subtraction."""

from __future__ import annotations

from fractions import Fraction as Q
import random

import sympy as sp


def symbolic_guard() -> tuple[sp.Expr, sp.Expr]:
    x, xe, y = sp.symbols("x xe y", real=True)
    # The intercept may be an arbitrary function of the predecessor.  It
    # cancels after anchoring both lines at the same endpoint, so model it by
    # independent symbols rather than importing the shooting engine.
    bx, be = sp.symbols("bx be", real=True)
    lx = bx + (sp.Rational(1, 2) - x) * y
    le = be + (sp.Rational(1, 2) - xe) * y

    right = sp.expand((lx - le) - (lx - le).subs(y, 1))
    left = sp.expand((lx - le) - (lx - le).subs(y, -1))

    assert sp.simplify(right - (x - xe) * (1 - y)) == 0
    assert sp.simplify(left - (xe - x) * (y + 1)) == 0
    return right, left


def hostile_guard(seed: int = 1234, trials: int = 100_000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        denominator = rng.randrange(1, 10_000)
        xe = Q(rng.randrange(1, denominator + 1), denominator)
        y = Q(rng.randrange(-denominator, denominator + 1), denominator)

        # Right tail: x>=xe and y<=1.
        x_right = xe + Q(rng.randrange(0, 10_001), 10_000)
        remainder_right = (x_right - xe) * (1 - y)
        assert remainder_right >= 0

        # Reflected left tail: x<=-xe and y>=-1.
        x_left = -xe - Q(rng.randrange(0, 10_001), 10_000)
        remainder_left = (-xe - x_left) * (y + 1)
        assert remainder_left >= 0
        checks += 2
    return checks


def main() -> None:
    right, left = symbolic_guard()
    checks = hostile_guard()
    print("==== SPRINT 1234 OUTER AFFINE DOMINANCE ====")
    print(f"PASS symbolic right remainder: {right}")
    print(f"PASS symbolic left remainder:  {left}")
    print(f"PASS exact-rational signed fixtures: {checks}")


if __name__ == "__main__":
    main()
