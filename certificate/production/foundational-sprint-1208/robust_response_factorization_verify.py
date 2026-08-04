#!/usr/bin/env python3
"""Exact symbolic guard for the robust local-response identities."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def reduce_sign(expression: sp.Expr, sign: sp.Symbol) -> sp.Expr:
    return sp.rem(sp.Poly(sp.expand(expression), sign), sp.Poly(sign**2 - 1, sign)).as_expr()


def main() -> None:
    lp, lm, sign, p, q = sp.symbols("l_plus l_minus sign p q", real=True)
    identity = sp.eye(2)
    L = sp.diag(lp, lm)
    K = sp.Matrix([[0, sign], [sign, 0]])
    response = sp.Matrix([[lp**2, -sign * lp * lm], [-sign * lp * lm, lm**2]])

    factor_residual = (response - L * (identity - K) * L).applyfunc(sp.expand)
    involution_residual = (K * K - identity).applyfunc(lambda x: reduce_sign(x, sign))

    vector = sp.Matrix([p, q])
    weighted = L * vector
    failed = (identity - K) * weighted
    norm_squared = (failed.T * failed)[0]
    energy_twice = 2 * (vector.T * response * vector)[0]
    norm_residual = reduce_sign(norm_squared - energy_twice, sign)

    wrong_sign_response = sp.Matrix(
        [[lp**2, sign * lp * lm], [sign * lp * lm, lm**2]]
    )
    wrong_sign_residual = (
        wrong_sign_response - L * (identity - K) * L
    ).applyfunc(sp.expand)

    report = {
        "status": "exact symbolic robust response-factorization guard",
        "factorization_residual": [[str(x) for x in row] for row in factor_residual.tolist()],
        "involution_residual_mod_sign_squared": [
            [str(x) for x in row] for row in involution_residual.tolist()
        ],
        "squared_norm_residual_mod_sign_squared": str(sp.factor(norm_residual)),
        "wrong_sign_control": [[str(x) for x in row] for row in wrong_sign_residual.tolist()],
        "wrong_sign_detected": any(x != 0 for x in wrong_sign_residual),
        "all_gates_pass": (
            factor_residual == sp.zeros(2)
            and involution_residual == sp.zeros(2)
            and sp.expand(norm_residual) == 0
            and any(x != 0 for x in wrong_sign_residual)
        ),
        "claim_boundary": (
            "This proves the local algebra and squared-norm identity. The spectral "
            "cutoff, transport localization, orbit rounding, and dimension bound are "
            "analytic statements with separate ownership."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "robust-response-factorization.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
