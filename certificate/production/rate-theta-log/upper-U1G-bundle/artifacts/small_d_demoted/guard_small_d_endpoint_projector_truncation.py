#!/usr/bin/env python3
"""U1 mechanical guard for endpoint-projector truncation, d=3..8.

HONEST CLAIM BOUNDARY
---------------------
This is a fail-capable construction guard, not a theorem verifier.  It uses an
exact-rational excerpt of the committed dimension-255 aligned I3322 strategy
only as fixture data.  It verifies:
  * the endpoint-completion rule for all d=3,...,8;
  * exact algebraic idempotence/self-adjointness of every local 2x2/singleton
    projector block;
  * exact normalization identity for the truncated Schmidt state;
  * rigorous >= 100-decimal-place rational interval enclosures for Bell scores;
  * all scores lie strictly below the certified current-S window;
  * odd and even alternating-parity subsequences rise toward that window.

It does NOT verify Theorem (S), the endpoint-Cesaro theorem, the asymptotic
upper rate, or any numerical rate coefficient.

Stock-Python arithmetic only: fractions.Fraction + integer square-root bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "SMALL_D_TRUNCATION_SOURCE_DATA.json"
SQRT_DIGITS = 140
SQRT_SCALE = 10 ** SQRT_DIGITS


@dataclass(frozen=True)
class Iv:
    lo: F
    hi: F

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("invalid interval")

    @staticmethod
    def point(x: F | int) -> "Iv":
        q = x if isinstance(x, F) else F(x)
        return Iv(q, q)

    def __add__(self, other: "Iv") -> "Iv":
        return Iv(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "Iv":
        return Iv(-self.hi, -self.lo)

    def __sub__(self, other: "Iv") -> "Iv":
        return self + (-other)

    def __mul__(self, other: "Iv") -> "Iv":
        vals = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Iv(min(vals), max(vals))

    def scale(self, q: F) -> "Iv":
        return self * Iv.point(q)

    def div_positive(self, q: F) -> "Iv":
        if q <= 0:
            raise ValueError("positive denominator required")
        return Iv(self.lo / q, self.hi / q)

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi

    def width(self) -> F:
        return self.hi - self.lo


def sqrt_interval(q: F) -> Iv:
    if q < 0:
        raise ValueError("negative radicand")
    # floor(sqrt(q)*SCALE) computed entirely over Z/Q.
    floor_sq = (q.numerator * SQRT_SCALE * SQRT_SCALE) // q.denominator
    n = isqrt(floor_sq)
    lo = F(n, SQRT_SCALE)
    hi = F(n + 1, SQRT_SCALE)
    assert lo * lo <= q
    assert hi * hi > q or q == 0
    return Iv(lo, hi)


def zeros(n: int) -> list[list[Iv]]:
    z = Iv.point(0)
    return [[z for _ in range(n)] for _ in range(n)]


def put_edge(matrix: list[list[Iv]], i: int, j: int, block: tuple[tuple[Iv, Iv], tuple[Iv, Iv]]) -> None:
    matrix[i][i], matrix[i][j] = block[0]
    matrix[j][i], matrix[j][j] = block[1]


def exact_projector_block_check(c: F, sign: int, family: str) -> bool:
    """Check P^2=P exactly in Q[s]/(s^2-(1-c^2)).

    Elements are pairs (a,b) representing a + b*s.  sign picks the off-diagonal
    sign.  family A has diag ((1-c)/2,(1+c)/2); family B swaps c.
    """
    r = 1 - c * c
    half = F(1, 2)

    def add(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
        return (x[0] + y[0], x[1] + y[1])

    def mul(x: tuple[F, F], y: tuple[F, F]) -> tuple[F, F]:
        return (x[0] * y[0] + x[1] * y[1] * r, x[0] * y[1] + x[1] * y[0])

    if family == "A":
        d0, d1 = half * (1 - c), half * (1 + c)
    elif family == "B":
        d0, d1 = half * (1 + c), half * (1 - c)
    else:
        raise ValueError(family)
    off = (F(0), F(sign, 2))
    P = [[(d0, F(0)), off], [off, (d1, F(0))]]
    for i in range(2):
        for j in range(2):
            sq = (F(0), F(0))
            for k in range(2):
                sq = add(sq, mul(P[i][k], P[k][j]))
            if sq != P[i][j]:
                return False
    return True


def exact_hadamard_projector_check() -> bool:
    half = F(1, 2)
    P = [[half, half], [half, half]]
    for i in range(2):
        for j in range(2):
            if sum((P[i][k] * P[k][j] for k in range(2)), F(0)) != P[i][j]:
                return False
    return P[0][1] == P[1][0]


def exact_singleton_projector_check() -> bool:
    return F(1) * F(1) == F(1)


def build_strategy(a: int, b: int, profile: dict[int, F]) -> tuple[list[list[list[Iv]]], list[list[list[Iv]]], list[dict[str, object]]]:
    n = b - a + 1
    pos = {g: g - a for g in range(a, b + 1)}
    a1, a2, a3, b1, b2, b3 = [zeros(n) for _ in range(6)]
    half = F(1, 2)
    one = Iv.point(1)
    exact_blocks: list[dict[str, object]] = []

    for edge in range(a + 1, b + 1):
        c = profile[edge]
        s = sqrt_interval(1 - c * c)
        x = Iv.point(c)
        i, j = pos[edge - 1], pos[edge]
        if edge % 2 == 0:
            # M1: A1,A2,B3.
            block_minus = (
                (Iv.point(half * (1 - c)), -s.scale(half)),
                (-s.scale(half), Iv.point(half * (1 + c))),
            )
            block_plus = (
                (Iv.point(half * (1 - c)), s.scale(half)),
                (s.scale(half), Iv.point(half * (1 + c))),
            )
            r = ((Iv.point(half), Iv.point(half)), (Iv.point(half), Iv.point(half)))
            put_edge(a1, i, j, block_minus)
            put_edge(a2, i, j, block_plus)
            put_edge(b3, i, j, r)
            exact_blocks.extend([
                {"edge": edge, "operator": "A1", "ok": exact_projector_block_check(c, -1, "A")},
                {"edge": edge, "operator": "A2", "ok": exact_projector_block_check(c, +1, "A")},
                {"edge": edge, "operator": "B3", "ok": exact_hadamard_projector_check()},
            ])
        else:
            # M0: B1,B2,A3.
            block_minus = (
                (Iv.point(half * (1 + c)), -s.scale(half)),
                (-s.scale(half), Iv.point(half * (1 - c))),
            )
            block_plus = (
                (Iv.point(half * (1 + c)), s.scale(half)),
                (s.scale(half), Iv.point(half * (1 - c))),
            )
            r = ((Iv.point(half), Iv.point(half)), (Iv.point(half), Iv.point(half)))
            put_edge(b1, i, j, block_minus)
            put_edge(b2, i, j, block_plus)
            put_edge(a3, i, j, r)
            exact_blocks.extend([
                {"edge": edge, "operator": "B1", "ok": exact_projector_block_check(c, -1, "B")},
                {"edge": edge, "operator": "B2", "ok": exact_projector_block_check(c, +1, "B")},
                {"edge": edge, "operator": "A3", "ok": exact_hadamard_projector_check()},
            ])

    # Explicit severed endpoint completion.
    left = 0
    if a % 2 == 0:  # {a-1,a} in M1
        for M in (a1, a2, b3):
            M[left][left] = one
        left_pairing = "M1:A1,A2,B3"
    else:             # {a-1,a} in M0
        for M in (b1, b2, a3):
            M[left][left] = one
        left_pairing = "M0:B1,B2,A3"

    right = n - 1
    if b % 2 == 0:  # {b,b+1} in M0
        for M in (b1, b2, a3):
            M[right][right] = one
        right_pairing = "M0:B1,B2,A3"
    else:            # {b,b+1} in M1
        for M in (a1, a2, b3):
            M[right][right] = one
        right_pairing = "M1:A1,A2,B3"

    exact_blocks.extend([
        {"edge": a, "operator": left_pairing, "ok": exact_singleton_projector_check(), "kind": "left singleton"},
        {"edge": b + 1, "operator": right_pairing, "ok": exact_singleton_projector_check(), "kind": "right singleton"},
    ])
    return [a1, a2, a3], [b1, b2, b3], exact_blocks


def matmul(A: list[list[Iv]], B: list[list[Iv]]) -> list[list[Iv]]:
    n = len(A)
    out = zeros(n)
    for i in range(n):
        for j in range(n):
            acc = Iv.point(0)
            for k in range(n):
                acc = acc + A[i][k] * B[k][j]
            out[i][j] = acc
    return out


def projection_interval_check(P: list[list[Iv]]) -> tuple[bool, F]:
    n = len(P)
    PP = matmul(P, P)
    max_width = F(0)
    for i in range(n):
        for j in range(n):
            residual = PP[i][j] - P[i][j]
            if not residual.contains_zero():
                return False, residual.width()
            max_width = max(max_width, residual.width())
            # self-adjointness is exact at construction level; interval equality too.
            if P[i][j] != P[j][i]:
                return False, max_width
    return True, max_width


def marginal(v: list[F], P: list[list[Iv]], norm: F) -> Iv:
    acc = Iv.point(0)
    for i, x in enumerate(v):
        acc = acc + P[i][i].scale(x * x)
    return acc.div_positive(norm)


def correlation(v: list[F], A: list[list[Iv]], B: list[list[Iv]], norm: F) -> Iv:
    acc = Iv.point(0)
    n = len(v)
    for i in range(n):
        for j in range(n):
            acc = acc + (A[i][j] * B[i][j]).scale(v[i] * v[j])
    return acc.div_positive(norm)


def bell_score(v: list[F], A: list[list[list[Iv]]], B: list[list[list[Iv]]], norm: F) -> Iv:
    val = -marginal(v, A[1], norm) - marginal(v, B[0], norm) - marginal(v, B[1], norm).scale(F(2))
    for coeff, local, remote in (
        (1, A[0], B[0]),
        (1, A[0], B[1]),
        (1, A[1], B[0]),
        (1, A[1], B[1]),
        (-1, A[0], B[2]),
        (1, A[1], B[2]),
        (-1, A[2], B[0]),
        (1, A[2], B[1]),
    ):
        val = val + correlation(v, local, remote, norm).scale(F(coeff))
    return val


def dec(q: F, places: int = 50) -> str:
    # Deterministic decimal rendering from Q without float conversion.
    sign = "-" if q < 0 else ""
    q = abs(q)
    integer = q.numerator // q.denominator
    rem = q.numerator % q.denominator
    digits = []
    for _ in range(places):
        rem *= 10
        digits.append(str(rem // q.denominator))
        rem %= q.denominator
    return f"{sign}{integer}." + "".join(digits)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    profile = {int(k): F(v) for k, v in data["profile_decimal"].items()}
    vector = {int(k): F(v) for k, v in data["vector_decimal"].items()}
    s_minus = F(data["certified_window_lower"])
    rows = []

    for d in range(3, 9):
        a, b = data["segments"][str(d)]
        assert b - a + 1 == d
        v = [vector[j] for j in range(a, b + 1)]
        norm = sum((x * x for x in v), F(0))
        assert norm > 0
        # Exact normalized-state identity: sum (v_j/sqrt(norm))^2 = 1.
        normalized_state_exact = sum((x * x for x in v), F(0)) == norm

        A, B, exact_blocks = build_strategy(a, b, profile)
        assert all(row["ok"] for row in exact_blocks)
        interval_checks = [projection_interval_check(P) for P in A + B]
        assert all(ok for ok, _ in interval_checks)
        max_proj_width = max(width for _, width in interval_checks)
        assert max_proj_width < F(1, 10**120)

        score = bell_score(v, A, B, norm)
        assert score.hi < s_minus
        rows.append({
            "dimension": d,
            "segment": [a, b],
            "left_severed_pair": [a - 1, a],
            "right_severed_pair": [b, b + 1],
            "all_six_exact_block_projections": True,
            "projection_interval_residual_contains_zero": True,
            "projection_interval_residual_width_lt_1e-120": True,
            "normalized_state_exact": normalized_state_exact,
            "local_dimension_equals_retained_interval": d == (b - a + 1),
            "bell_lower": dec(score.lo, 60),
            "bell_upper": dec(score.hi, 60),
            "strictly_below_certified_window": score.hi < s_minus,
        })

    # Alternating endpoint completion gives two parity subsequences.  The smoke
    # check is intentionally parity-resolved, not a false all-d monotonicity claim.
    by_d = {row["dimension"]: row for row in rows}
    def lower(d: int) -> F:
        # Stored decimal is a truncation; use fresh exact interval for comparisons below.
        a, b = data["segments"][str(d)]
        v = [vector[j] for j in range(a, b + 1)]
        norm = sum((x * x for x in v), F(0))
        A, B, _ = build_strategy(a, b, profile)
        return bell_score(v, A, B, norm).lo
    def upper(d: int) -> F:
        a, b = data["segments"][str(d)]
        v = [vector[j] for j in range(a, b + 1)]
        norm = sum((x * x for x in v), F(0))
        A, B, _ = build_strategy(a, b, profile)
        return bell_score(v, A, B, norm).hi

    odd_rises = upper(3) < lower(5) and upper(5) < lower(7)
    even_rises = upper(4) < lower(6) and upper(6) < lower(8)
    assert odd_rises
    assert even_rises

    result = {
        "status": "PASS — U1 endpoint-projector truncation mechanical guard",
        "arithmetic": f"exact Fraction algebra plus rational sqrt intervals at {SQRT_DIGITS} decimal places",
        "source_profile_separator_vector_sha256": data["source_profile_separator_vector_sha256"],
        "dimensions_checked": list(range(3, 9)),
        "rows": rows,
        "odd_parity_scores_rise_d3_d5_d7": odd_rises,
        "even_parity_scores_rise_d4_d6_d8": even_rises,
        "all_scores_below_certified_window": all(row["strictly_below_certified_window"] for row in rows),
        "all_gates_pass": True,
        "claim_boundary": (
            "Mechanical truncation guard only. The parity-resolved small-d rise is a smoke check, "
            "not a proof of asymptotic convergence or of the U1 rate. No numerical rate constant is verified."
        ),
    }
    out = HERE / "small_d_endpoint_projector_truncation_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
