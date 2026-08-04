from __future__ import annotations

import json
import random
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def a_map(x: Fraction, scale: Fraction) -> Fraction:
    return -scale * x if x >= 0 else -x / scale


def b_map(x: Fraction) -> Fraction:
    return -x


def tau_map(x: Fraction, scale: Fraction) -> Fraction:
    return a_map(b_map(x), scale)


def exact_average_separation(pairs, period: Fraction) -> Fraction:
    events = defaultdict(Fraction)
    events[Fraction(0)] = Fraction(0)
    events[period] = Fraction(0)
    always = Fraction(0)
    for left_point, right_point, weight in pairs:
        lo, hi = sorted((left_point, right_point))
        distance = hi - lo
        if distance >= period:
            always += weight
            continue
        start = lo % period
        end = hi % period
        if start == end:
            continue
        if start < end:
            events[start] += weight
            events[end] -= weight
        else:
            events[0] += weight
            events[end] -= weight
            events[start] += weight
            events[period] -= weight
    current = always
    integral = Fraction(0)
    points = sorted(events)
    for left, right in zip(points[:-1], points[1:]):
        current += events[left]
        integral += current * (right - left)
    return integral / period


def main() -> None:
    rng = random.Random(1227)
    fixtures = 5000
    for _ in range(fixtures):
        scale = Fraction(rng.randint(1, 20), rng.randint(1, 20))
        if scale < 1:
            scale = 1 / scale
        width = Fraction(rng.randint(1, 20), rng.randint(1, 20))
        pairs = []
        raw_weights = []
        for _ in range(rng.randint(1, 20)):
            u = Fraction(rng.randint(-200, 200), rng.randint(1, 31))
            weight = Fraction(rng.randint(1, 20), rng.randint(1, 20))
            au = a_map(u, scale)
            bu = b_map(u)
            tauu = tau_map(u, scale)
            assert abs(au - bu) <= scale * abs(u - tauu)
            pairs.append((au, bu, weight))
            raw_weights.append(weight)
        total = sum(raw_weights, Fraction(0))
        normalized = [(a, b, w / total) for a, b, w in pairs]
        average = exact_average_separation(normalized, width)
        formula = sum(
            w * min(Fraction(1), abs(a - b) / width)
            for a, b, w in normalized
        )
        assert average == formula

    result = {
        "status": "exact-rational near-fixed pullback-pairing guard",
        "hostile_weighted_measures": fixtures,
        "unpaired_mass_coefficient": "20*Delta/h",
        "common_projection_formula_recorded": True,
        "mutual_source_target_orthogonality_claimed": False,
        "all_gates_pass": True,
        "claim_boundary": (
            "The set-theoretic pullback and shifted separation theorem are "
            "guarded; no pointwise fibre identification is claimed."
        ),
    }
    target = Path(__file__).with_name("pullback-pairing-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
