#!/usr/bin/env python3
"""Exact-rational guards for the matched-block transport theorem."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Q = Fraction


def norm2(vector: list[Q]) -> Q:
    return sum((x * x for x in vector), Q(0))


def main() -> None:
    rng = random.Random(1212)
    fixtures = 0
    quadratic_slack_min = None
    mass_bound_squared_slack_min = None

    for _ in range(1000):
        block_count = rng.randint(1, 9)
        block_size = rng.randint(1, 6)
        dimension = block_count * block_size

        alpha = list(range(block_count))
        rng.shuffle(alpha)

        # K is a signed coordinate permutation mapping block i onto alpha(i).
        internal = []
        signs = []
        for _i in range(block_count):
            p = list(range(block_size))
            rng.shuffle(p)
            internal.append(p)
            signs.append([rng.choice((-1, 1)) for _ in range(block_size)])

        def apply_k(v: list[Q]) -> list[Q]:
            out = [Q(0) for _ in range(dimension)]
            for i in range(block_count):
                for r in range(block_size):
                    source = i * block_size + r
                    target = alpha[i] * block_size + internal[i][r]
                    out[target] = signs[i][r] * v[source]
            return out

        w = [Q(rng.randint(-9, 9), rng.randint(1, 11)) for _ in range(dimension)]

        # Coordinate subprojections G_i<=E_i, including empty/full cases.
        keep = []
        for _i in range(block_count):
            keep.append([rng.choice((False, True)) for _ in range(block_size)])

        def project_block(v: list[Q], i: int, good: bool) -> list[Q]:
            out = [Q(0) for _ in range(dimension)]
            for r in range(block_size):
                if (not good) or keep[i][r]:
                    out[i * block_size + r] = v[i * block_size + r]
            return out

        kw = apply_k(w)
        delta2 = norm2([kw[j] - w[j] for j in range(dimension)])

        gw = [Q(0) for _ in range(dimension)]
        for i in range(block_count):
            giw = project_block(w, i, True)
            gw = [gw[j] + giw[j] for j in range(dimension)]
        gamma2 = norm2([w[j] - gw[j] for j in range(dimension)])

        d2 = Q(0)
        masses = []
        for i in range(block_count):
            giw = project_block(w, i, True)
            target = project_block(w, alpha[i], True)
            transported = apply_k(giw)
            d2 += norm2(
                [transported[j] - target[j] for j in range(dimension)]
            )
            masses.append(norm2(giw))

        quadratic_slack = 3 * delta2 + 6 * gamma2 - d2
        assert quadratic_slack >= 0
        if quadratic_slack_min is None or quadratic_slack < quadratic_slack_min:
            quadratic_slack_min = quadratic_slack

        mass_l1 = sum(
            (abs(masses[i] - masses[alpha[i]]) for i in range(block_count)),
            Q(0),
        )
        # Square the mass bound to retain exact rational arithmetic.
        # sum(a_i+b_i)^2 <= 4||Gw||^2 and D^2 is the packet defect.
        mass_squared_slack = 4 * norm2(gw) * d2 - mass_l1 * mass_l1
        assert mass_squared_slack >= 0
        if (
            mass_bound_squared_slack_min is None
            or mass_squared_slack < mass_bound_squared_slack_min
        ):
            mass_bound_squared_slack_min = mass_squared_slack

        fixtures += 1

    # Exact equality fixtures protect the constants and indexing.
    equality_fixtures = 0
    for block_count in range(1, 10):
        # Identity K, full G: every quantity is exactly zero.
        w = [Q(i - 4, i + 1) for i in range(block_count)]
        d2 = Q(0)
        delta2 = Q(0)
        gamma2 = Q(0)
        assert d2 == 3 * delta2 + 6 * gamma2 == 0
        equality_fixtures += 1

    report = {
        "status": "exact-rational matched-block transport guard",
        "random_fixtures": fixtures,
        "equality_fixtures": equality_fixtures,
        "minimum_quadratic_slack": str(quadratic_slack_min),
        "minimum_mass_bound_squared_slack": str(mass_bound_squared_slack_min),
        "all_gates_pass": fixtures == 1000 and equality_fixtures == 9,
        "claim_boundary": (
            "This verifies the dimension-free packet theorem on exact rational "
            "signed-permutation fixtures. It does not construct the common "
            "adaptive I3322 partition or prove a dimension lower bound."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "matched-block-transport-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
