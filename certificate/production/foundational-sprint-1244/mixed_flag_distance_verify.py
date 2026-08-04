#!/usr/bin/env python3
"""Exact-rational guards for mixed cumulative-flag distance."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Q = Fraction


def inverse(permutation: list[int]) -> list[int]:
    out = [0] * len(permutation)
    for i, value in enumerate(permutation):
        out[value] = i
    return out


def permutation_flag_distance(p: list[int], q: list[int], weights: list[Q]) -> Q:
    n = len(p)
    total = Q(0)
    for k in range(1, n):
        p_set = set(p[:k])
        q_set = set(q[:k])
        total += sum((weights[j] for j in p_set.symmetric_difference(q_set)), Q(0))
    return total


def cdf_distance(p: list[Q], q: list[Q]) -> Q:
    cumulative = Q(0)
    total = Q(0)
    for i in range(len(p) - 1):
        cumulative += p[i] - q[i]
        total += abs(cumulative)
    return total


def greedy_wasserstein(p: list[Q], q: list[Q]) -> Q:
    """Exact earth mover cost on the integer line."""
    supply = [[i, p[i]] for i in range(len(p)) if p[i] > 0]
    demand = [[i, q[i]] for i in range(len(q)) if q[i] > 0]
    i = j = 0
    cost = Q(0)
    while i < len(supply) and j < len(demand):
        amount = min(supply[i][1], demand[j][1])
        cost += amount * abs(supply[i][0] - demand[j][0])
        supply[i][1] -= amount
        demand[j][1] -= amount
        if supply[i][1] == 0:
            i += 1
        if demand[j][1] == 0:
            j += 1
    return cost


def random_distribution(size: int, rng: random.Random) -> list[Q]:
    raw = [rng.randint(0, 30) for _ in range(size)]
    if sum(raw) == 0:
        raw[0] = 1
    total = sum(raw)
    return [Q(value, total) for value in raw]


def main() -> None:
    rng = random.Random(1244)
    permutation_fixtures = 0
    stochastic_fixtures = 0
    minimum_nonzero_ratio = None

    for _ in range(20000):
        n = rng.randint(2, 12)
        p = list(range(n))
        q = list(range(n))
        rng.shuffle(p)
        rng.shuffle(q)
        weights = [Q(rng.randint(1, 30), rng.randint(1, 30)) for _ in range(n)]
        lhs = permutation_flag_distance(p, q, weights)
        ip = inverse(p)
        iq = inverse(q)
        rhs = sum((weights[j] * abs(ip[j] - iq[j]) for j in range(n)), Q(0))
        assert lhs == rhs
        if p != q:
            assert lhs >= 2 * min(weights)
            ratio = lhs / (2 * min(weights))
            if minimum_nonzero_ratio is None or ratio < minimum_nonzero_ratio:
                minimum_nonzero_ratio = ratio
        permutation_fixtures += 1

    for _ in range(30000):
        n = rng.randint(2, 15)
        p = random_distribution(n, rng)
        q = random_distribution(n, rng)
        assert cdf_distance(p, q) == greedy_wasserstein(p, q)
        stochastic_fixtures += 1

    # The exact Sprint 1241 pair is detected.
    p0 = [3, 2, 1, 0]
    q0 = [1, 0, 3, 2]
    w0 = [Q(1), Q(1), Q(1), Q(1)]
    doppelganger_distance = permutation_flag_distance(p0, q0, w0)

    report = {
        "status": "exact mixed-flag/Wasserstein distance guard",
        "permutation_fixtures": permutation_fixtures,
        "stochastic_fixtures": stochastic_fixtures,
        "minimum_nonzero_over_two_min_weight": str(minimum_nonzero_ratio),
        "marginal_volume_doppelganger_distance": str(doppelganger_distance),
        "all_gates_pass": bool(
            permutation_fixtures == 20000
            and stochastic_fixtures == 30000
            and minimum_nonzero_ratio is not None
            and minimum_nonzero_ratio >= 1
            and doppelganger_distance > 0
        ),
        "claim_boundary": (
            "This proves the finite permutation identity and independently "
            "checks the one-dimensional stochastic Wasserstein formula. It "
            "does not derive response kernels or a Bell-deficit bound."
        ),
    }
    (HERE / "mixed-flag-distance-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
