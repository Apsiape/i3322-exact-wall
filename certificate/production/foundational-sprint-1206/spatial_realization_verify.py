#!/usr/bin/env python3
"""Exact guards for the Pal--Vertesi block-to-Jacobi realization.

The spatial theorem is analytic. This script independently checks the finite
local identity using only Fraction arithmetic and rational points on the unit
circle. No production I3322 module is imported.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent


def zeros(n: int) -> list[list[F]]:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    n = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(n)), F(0)) for j in range(n)]
        for i in range(n)
    ]


def matsub(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def is_zero(a: list[list[F]]) -> bool:
    return all(x == 0 for row in a for x in row)


def unit_point(t: int) -> tuple[F, F]:
    """Rational (cosine, positive sine) on the unit circle."""
    den = F(1 + t * t)
    return F(1 - t * t, 1 + t * t), F(2 * t, 1 + t * t)


def put_edge(
    matrix: list[list[F]],
    first: int,
    second: int,
    block: tuple[tuple[F, F], tuple[F, F]],
) -> None:
    matrix[first][first], matrix[first][second] = block[0]
    matrix[second][first], matrix[second][second] = block[1]


def put_block(matrix: list[list[F]], i: int, block: tuple[tuple[F, F], tuple[F, F]]) -> None:
    put_edge(matrix, i, i + 1, block)


def blocks(c: list[F], s: list[F]) -> tuple[list[list[list[F]]], list[list[list[F]]]]:
    """Exact finite open Pal--Vertesi blocks, independently reconstructed."""
    n = len(c) - 1
    a1, a2, a3 = zeros(n), zeros(n), zeros(n)
    b1, b2, b3 = zeros(n), zeros(n), zeros(n)
    half = F(1, 2)

    a1[0][0] = a2[0][0] = b3[0][0] = F(1)
    for edge in range(2, n, 2):
        first = edge - 1
        x, y = c[edge], s[edge]
        put_block(a1, first, ((half * (1 - x), -half * y), (-half * y, half * (1 + x))))
        put_block(a2, first, ((half * (1 - x), half * y), (half * y, half * (1 + x))))
        put_block(b3, first, ((half, half), (half, half)))

    for edge in range(1, n - 1, 2):
        first = edge - 1
        x, y = c[edge], s[edge]
        put_block(b1, first, ((half * (1 + x), -half * y), (-half * y, half * (1 - x))))
        put_block(b2, first, ((half * (1 + x), half * y), (half * y, half * (1 - x))))
        put_block(a3, first, ((half, half), (half, half)))

    a3[-1][-1] = F(1)
    # With c_n=-1 the published endpoint has B1=B2=0.
    b2[-1][-1] = 1 + c[-1]
    return [a1, a2, a3], [b1, b2, b3]


def marginal(lam: list[F], matrix: list[list[F]]) -> F:
    return sum((x * x * matrix[i][i] for i, x in enumerate(lam)), F(0))


def correlation(lam: list[F], a: list[list[F]], b: list[list[F]]) -> F:
    n = len(lam)
    return sum(
        (lam[i] * lam[j] * a[i][j] * b[i][j] for i in range(n) for j in range(n)),
        F(0),
    )


def bell_score(lam: list[F], a: list[list[list[F]]], b: list[list[list[F]]]) -> F:
    value = -marginal(lam, a[1]) - marginal(lam, b[0]) - 2 * marginal(lam, b[1])
    for coefficient, local, remote in (
        (1, a[0], b[0]),
        (1, a[0], b[1]),
        (1, a[1], b[0]),
        (1, a[1], b[1]),
        (-1, a[0], b[2]),
        (1, a[1], b[2]),
        (-1, a[2], b[0]),
        (1, a[2], b[1]),
    ):
        value += coefficient * correlation(lam, local, remote)
    return value


def jacobi_score(lam: list[F], c: list[F], s: list[F]) -> F:
    n = len(lam)
    diagonal = sum(
        (
            (c[j] * c[j + 1] + (c[j] - c[j + 1]) / 2 - 1) * lam[j] * lam[j]
            for j in range(n)
        ),
        F(0),
    )
    neighbors = sum((s[j] * lam[j - 1] * lam[j] for j in range(1, n)), F(0))
    return diagonal + neighbors


def cyclic_blocks(c: list[F], s: list[F]) -> tuple[list[list[list[F]]], list[list[list[F]]]]:
    """No-endpoint alternating blocks, the local model used on ell2(Z)."""
    n = len(c)
    if n % 2:
        raise ValueError("Cyclic alternating carrier requires even dimension")
    a1, a2, a3 = zeros(n), zeros(n), zeros(n)
    b1, b2, b3 = zeros(n), zeros(n), zeros(n)
    half = F(1, 2)
    r = ((half, half), (half, half))
    for edge in range(n):
        first, second = (edge - 1) % n, edge
        x, y = c[edge], s[edge]
        if edge % 2 == 0:
            put_edge(a1, first, second, ((half * (1 - x), -half * y), (-half * y, half * (1 + x))))
            put_edge(a2, first, second, ((half * (1 - x), half * y), (half * y, half * (1 + x))))
            put_edge(b3, first, second, r)
        else:
            put_edge(b1, first, second, ((half * (1 + x), -half * y), (-half * y, half * (1 - x))))
            put_edge(b2, first, second, ((half * (1 + x), half * y), (half * y, half * (1 - x))))
            put_edge(a3, first, second, r)
    return [a1, a2, a3], [b1, b2, b3]


def cyclic_jacobi_score(lam: list[F], c: list[F], s: list[F]) -> F:
    n = len(lam)
    diagonal = sum(
        (
            (c[j] * c[(j + 1) % n] + (c[j] - c[(j + 1) % n]) / 2 - 1)
            * lam[j]
            * lam[j]
            for j in range(n)
        ),
        F(0),
    )
    neighbors = sum((s[j] * lam[(j - 1) % n] * lam[j] for j in range(n)), F(0))
    return diagonal + neighbors


def fixture(n: int, offset: int) -> dict[str, object]:
    if n < 5 or n % 2 == 0:
        raise ValueError("Use odd open dimensions at least five")
    c, s = [F(1)], [F(0)]
    for j in range(1, n):
        x, y = unit_point(1 + ((j + offset) % 6))
        c.append(x)
        s.append(y)
    c.append(F(-1))
    s.append(F(0))
    lam = [F((j + 1) * (n - j) + offset, n * n + 3) for j in range(n)]
    a, b = blocks(c, s)

    projection_checks = [is_zero(matsub(matmul(p, p), p)) for p in a + b]
    direct = bell_score(lam, a, b)
    reduced = jacobi_score(lam, c, s)

    # Wrong matching control: remove A3. The identity must notice.
    wrong_a = [a[0], a[1], zeros(n)]
    wrong_residual = bell_score(lam, wrong_a, b) - reduced
    assert all(projection_checks)
    assert direct == reduced
    assert wrong_residual != 0
    return {
        "dimension": n,
        "offset": offset,
        "all_six_exact_projections": all(projection_checks),
        "bell_minus_jacobi": str(direct - reduced),
        "wrong_matching_residual_nonzero": str(wrong_residual),
    }


def cyclic_fixture(n: int, offset: int) -> dict[str, object]:
    if n < 4 or n % 2:
        raise ValueError("Use even cyclic dimensions at least four")
    points = [unit_point(1 + ((j + offset) % 7)) for j in range(n)]
    c, s = [point[0] for point in points], [point[1] for point in points]
    lam = [F((j + 2) * (n + 1 - j) + offset, n * n + 7) for j in range(n)]
    a, b = cyclic_blocks(c, s)
    projection_checks = [is_zero(matsub(matmul(p, p), p)) for p in a + b]
    direct = bell_score(lam, a, b)
    reduced = cyclic_jacobi_score(lam, c, s)
    wrong_b = [b[0], b[1], zeros(n)]
    wrong_residual = bell_score(lam, a, wrong_b) - reduced
    assert all(projection_checks)
    assert direct == reduced
    assert wrong_residual != 0
    return {
        "dimension": n,
        "offset": offset,
        "all_six_exact_projections": all(projection_checks),
        "bell_minus_jacobi": str(direct - reduced),
        "wrong_matching_residual_nonzero": str(wrong_residual),
    }


def main() -> None:
    open_checks = [fixture(n, offset) for n in (5, 7, 9, 11) for offset in (0, 2, 5)]
    cyclic_checks = [cyclic_fixture(n, offset) for n in (4, 6, 8, 10) for offset in (0, 3, 6)]
    checks = open_checks + cyclic_checks
    result = {
        "status": "exact independent block-to-Jacobi spatial-realization guard",
        "arithmetic": "fractions.Fraction only",
        "open_fixtures": open_checks,
        "no_endpoint_cyclic_fixtures": cyclic_checks,
        "fixture_count": len(checks),
        "all_gates_pass": all(
            row["all_six_exact_projections"] and row["bell_minus_jacobi"] == "0"
            for row in checks
        ),
        "claim_boundary": (
            "This guards the local projector and Bell-to-Jacobi identities. "
            "The certified bi-infinite profile, ell2 tail, and eigen-equation "
            "remain analytic inputs from Sprint 1195."
        ),
    }
    assert result["all_gates_pass"]
    (HERE / "spatial-realization-guard.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
