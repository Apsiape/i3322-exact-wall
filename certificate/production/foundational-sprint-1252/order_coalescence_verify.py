#!/usr/bin/env python3
"""Exact guards for decreasing-map Wasserstein coalescence."""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cdf_distance(first, second, support) -> Fraction:
    total = Fraction(0)
    ordered = sorted(set(support))
    for left, right in zip(ordered, ordered[1:]):
        cdf_first = sum(weight for point, weight in first if point <= left)
        cdf_second = sum(weight for point, weight in second if point <= left)
        total += abs(cdf_first - cdf_second) * (right - left)
    return total


def push(measure, mapping):
    return [(mapping(point), weight) for point, weight in measure]


def main() -> None:
    rng = random.Random(1252)
    fixtures = 0
    minimum_identity_slack = None
    wrong_monotonicity_detections = 0

    for _ in range(20000):
        size = rng.randrange(2, 25)
        points = sorted(set(Fraction(rng.randrange(-200, 201), 100) for _ in range(size * 3)))[:size]
        if len(points) < 2:
            continue
        weights = [Fraction(rng.randrange(1, 30), rng.randrange(1, 30)) for _ in points]
        measure = list(zip(points, weights))

        # Affine decreasing maps suffice as exact hostile fixtures; their
        # images are generally off the original support.
        alpha = Fraction(rng.randrange(1, 20), rng.randrange(1, 20))
        beta = Fraction(rng.randrange(1, 20), rng.randrange(1, 20))
        shift_a = Fraction(rng.randrange(-30, 31), 10)
        shift_b = Fraction(rng.randrange(-30, 31), 10)
        a = lambda x, aa=alpha, ss=shift_a: ss - aa * x
        b = lambda x, bb=beta, ss=shift_b: ss - bb * x

        pushed_a = push(measure, a)
        pushed_b = push(measure, b)
        support = [point for point, _ in pushed_a + pushed_b]
        transport = cdf_distance(pushed_a, pushed_b, support)
        common_source = sum(weight * abs(a(point) - b(point)) for point, weight in measure)
        slack = transport - common_source
        assert slack == 0
        if minimum_identity_slack is None or slack < minimum_identity_slack:
            minimum_identity_slack = slack

        # Reversing one map to increasing generically destroys the identity.
        b_wrong = lambda x, bb=beta, ss=shift_b: ss + bb * x
        pushed_wrong = push(measure, b_wrong)
        wrong_support = [point for point, _ in pushed_a + pushed_wrong]
        wrong_transport = cdf_distance(pushed_a, pushed_wrong, wrong_support)
        wrong_source = sum(weight * abs(a(point) - b_wrong(point)) for point, weight in measure)
        if wrong_transport != wrong_source:
            wrong_monotonicity_detections += 1
        fixtures += 1

    gates = {
        "decreasing_common_source_is_optimal": fixtures >= 19000 and minimum_identity_slack == 0,
        "mixed_monotonicity_control_rejected": wrong_monotonicity_detections > 0,
    }
    report = {
        "status": "quantitative order-coalescence guard",
        "exact_rational_fixtures": fixtures,
        "minimum_wasserstein_identity_slack": str(minimum_identity_slack),
        "wrong_monotonicity_detections": wrong_monotonicity_detections,
        "i3322_lipschitz_constant": 20,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The decreasing-map transport identity and coalescence algebra are guarded. "
            "The amplitude/quarter-margin closure remains open."
        ),
    }
    (HERE / "order-coalescence-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

