#!/usr/bin/env python3
"""Symbolic no-endpoint verification of the infinite I3322 carrier.

This is independent of ``spatial_realization_verify.py``.  It constructs a
four-site periodic alternating carrier over a polynomial ring, expands the
Bell functional directly, and reduces only by the four unit-circle relations
``s_j**2 + c_j**2 = 1``.  Four sites are the smallest endpoint-free fixture
containing both matching parities and every local term of the bi-infinite
construction.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
N = 4


def zero() -> sp.Matrix:
    return sp.zeros(N, N)


def install(matrix: sp.Matrix, i: int, j: int, block: sp.Matrix) -> None:
    matrix[i, i] = block[0, 0]
    matrix[i, j] = block[0, 1]
    matrix[j, i] = block[1, 0]
    matrix[j, j] = block[1, 1]


def marginal(lam: tuple[sp.Symbol, ...], matrix: sp.Matrix) -> sp.Expr:
    return sp.expand(sum(lam[i] ** 2 * matrix[i, i] for i in range(N)))


def correlation(
    lam: tuple[sp.Symbol, ...], left: sp.Matrix, right: sp.Matrix
) -> sp.Expr:
    return sp.expand(
        sum(
            lam[i] * lam[j] * left[i, j] * right[i, j]
            for i in range(N)
            for j in range(N)
        )
    )


def reduce_unit_circles(
    expression: sp.Expr,
    cosines: tuple[sp.Symbol, ...],
    sines: tuple[sp.Symbol, ...],
) -> sp.Expr:
    """Take the exact multivariate remainder modulo s_j^2+c_j^2-1."""
    variables = (*sines, *cosines)
    generators = [sines[j] ** 2 + cosines[j] ** 2 - 1 for j in range(N)]
    basis = sp.groebner(generators, *variables, order="lex", domain=sp.QQ)
    remainder = sp.Integer(0)
    # Groebner reduction treats Schmidt symbols as coefficients only after we
    # split the expression into their monomials.
    lam_symbols = sorted(expression.free_symbols - set(variables), key=str)
    if not lam_symbols:
        _, reduced = basis.reduce(sp.expand(expression))
        return sp.expand(reduced)
    poly_in_lam = sp.Poly(expression, *lam_symbols)
    for exponent, coefficient in poly_in_lam.terms():
        _, reduced = basis.reduce(sp.expand(coefficient))
        monomial = sp.prod(symbol ** power for symbol, power in zip(lam_symbols, exponent))
        remainder += reduced * monomial
    return sp.expand(remainder)


def main() -> None:
    c = sp.symbols("c0:4", real=True)
    s = sp.symbols("s0:4", real=True)
    lam = sp.symbols("l0:4", real=True)
    half = sp.Rational(1, 2)
    a = [zero(), zero(), zero()]
    b = [zero(), zero(), zero()]
    receiver = sp.Matrix([[half, half], [half, half]])

    for edge in range(N):
        first, second = (edge - 1) % N, edge
        if edge % 2 == 0:
            install(
                a[0], first, second,
                sp.Matrix([[half * (1 - c[edge]), -half * s[edge]],
                           [-half * s[edge], half * (1 + c[edge])]]),
            )
            install(
                a[1], first, second,
                sp.Matrix([[half * (1 - c[edge]), half * s[edge]],
                           [half * s[edge], half * (1 + c[edge])]]),
            )
            install(b[2], first, second, receiver)
        else:
            install(
                b[0], first, second,
                sp.Matrix([[half * (1 + c[edge]), -half * s[edge]],
                           [-half * s[edge], half * (1 - c[edge])]]),
            )
            install(
                b[1], first, second,
                sp.Matrix([[half * (1 + c[edge]), half * s[edge]],
                           [half * s[edge], half * (1 - c[edge])]]),
            )
            install(a[2], first, second, receiver)

    bell = -marginal(lam, a[1]) - marginal(lam, b[0]) - 2 * marginal(lam, b[1])
    for coefficient, left, right in (
        (1, a[0], b[0]), (1, a[0], b[1]),
        (1, a[1], b[0]), (1, a[1], b[1]),
        (-1, a[0], b[2]), (1, a[1], b[2]),
        (-1, a[2], b[0]), (1, a[2], b[1]),
    ):
        bell += coefficient * correlation(lam, left, right)

    jacobi = sum(
        (
            c[j] * c[(j + 1) % N]
            + (c[j] - c[(j + 1) % N]) / 2
            - 1
        ) * lam[j] ** 2
        + s[j] * lam[(j - 1) % N] * lam[j]
        for j in range(N)
    )
    residual = sp.expand(bell - jacobi)
    reduced = reduce_unit_circles(residual, c, s)

    projection_residuals = []
    for measurement in (*a, *b):
        for entry in measurement * measurement - measurement:
            projection_residuals.append(reduce_unit_circles(sp.expand(entry), c, s))

    result = {
        "status": "symbolic endpoint-free I3322 spatial-carrier guard",
        "carrier_sites": N,
        "contains_both_matching_parities": True,
        "bell_minus_jacobi_remainder": str(reduced),
        "all_six_projection_remainders_zero": all(value == 0 for value in projection_residuals),
        "all_gates_pass": reduced == 0 and all(value == 0 for value in projection_residuals),
        "relations_used": [f"s{j}^2+c{j}^2-1=0" for j in range(N)],
    }
    assert result["all_gates_pass"]
    (HERE / "spatial-symbolic-guard.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
