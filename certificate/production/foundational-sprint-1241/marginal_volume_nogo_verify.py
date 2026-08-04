#!/usr/bin/env python3
"""Exact-rational counterexample to marginal-volume closure."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
Q = Fraction


def permute(values: list[Q], permutation: list[int]) -> list[Q]:
    return [values[permutation[i]] for i in range(len(values))]


def main() -> None:
    lam = [Q(1), Q(2), Q(5), Q(11)]
    p = [3, 2, 1, 0]
    q = [1, 0, 3, 2]
    cp = [lam[p[i]] / lam[i] for i in range(4)]
    cq = [lam[q[i]] / lam[i] for i in range(4)]
    target_p = [cp[i] * lam[i] for i in range(4)]
    target_q = [cq[i] * lam[i] for i in range(4)]

    reciprocal_p = [cp[i] * cp[p[i]] for i in range(4)]
    reciprocal_q = [cq[i] * cq[q[i]] for i in range(4)]
    determinant_p = sp.prod(sp.Rational(v.numerator, v.denominator) for v in cp)
    determinant_q = sp.prod(sp.Rational(v.numerator, v.denominator) for v in cq)

    z = sp.symbols("z")
    characteristic_d = sp.expand(
        sp.prod(z + sp.Rational(v.numerator, v.denominator) ** 2 for v in lam)
    )
    characteristic_p = sp.expand(
        sp.prod(z + sp.Rational(v.numerator, v.denominator) ** 2 for v in target_p)
    )
    characteristic_q = sp.expand(
        sp.prod(z + sp.Rational(v.numerator, v.denominator) ** 2 for v in target_q)
    )
    mismatch_squared = sum((target_p[i] - target_q[i]) ** 2 for i in range(4))

    report = {
        "status": "exact marginal-volume doppelganger",
        "schmidt_diagonal": [str(v) for v in lam],
        "first_involution": p,
        "second_involution": q,
        "first_multiplier": [str(v) for v in cp],
        "second_multiplier": [str(v) for v in cq],
        "first_reciprocal_products": [str(v) for v in reciprocal_p],
        "second_reciprocal_products": [str(v) for v in reciprocal_q],
        "first_determinant": str(determinant_p),
        "second_determinant": str(determinant_q),
        "characteristic_residual_first": str(sp.expand(characteristic_p - characteristic_d)),
        "characteristic_residual_second": str(sp.expand(characteristic_q - characteristic_d)),
        "target_mismatch_squared": str(mismatch_squared),
        "all_gates_pass": bool(
            all(value == 1 for value in reciprocal_p)
            and all(value == 1 for value in reciprocal_q)
            and determinant_p == 1
            and determinant_q == 1
            and characteristic_p == characteristic_d
            and characteristic_q == characteristic_d
            and mismatch_squared > 0
        ),
        "claim_boundary": (
            "This disproves closure from marginal singular/volume data alone. "
            "The second permutation is not globally decreasing, so the result "
            "motivates rather than disproves an ordered-flag theorem."
        ),
    }
    (HERE / "marginal-volume-nogo.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
