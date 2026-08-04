from __future__ import annotations

import json
import random
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def add_arc(events, start, end, weight, period):
    """Add the positively oriented circle arc [start,end) modulo period."""
    start %= period
    end %= period
    if start == end:
        return
    if start < end:
        events[start] += weight
        events[end] -= weight
    else:
        events[Fraction(0)] += weight
        events[end] -= weight
        events[start] += weight
        events[period] -= weight


def exact_shift_profile(pairs, period):
    always = Fraction(0)
    events = defaultdict(Fraction)
    events[Fraction(0)] = Fraction(0)
    events[period] = Fraction(0)
    for y, u, weight in pairs:
        lo, hi = sorted((y, u))
        distance = hi - lo
        if distance >= period:
            always += weight
            continue
        add_arc(events, lo, hi, weight, period)

    points = sorted(events)
    current = always
    minimum = None
    integral = Fraction(0)
    for left, right in zip(points[:-1], points[1:]):
        current += events[left]
        if right > left:
            minimum = current if minimum is None else min(minimum, current)
            integral += current * (right - left)
    return minimum if minimum is not None else always, integral / period


def main():
    rng = random.Random(1222)
    fixtures = 5000
    max_average_violation = Fraction(0)
    max_existence_violation = Fraction(0)

    for _ in range(fixtures):
        h = Fraction(rng.randint(1, 11), rng.randint(1, 11))
        raw = []
        total_weight = Fraction(0)
        for _ in range(rng.randint(1, 20)):
            y = Fraction(rng.randint(-100, 100), rng.randint(1, 31))
            u = Fraction(rng.randint(-100, 100), rng.randint(1, 31))
            weight = Fraction(rng.randint(1, 20), rng.randint(1, 20))
            raw.append((y, u, weight))
            total_weight += weight
        pairs = [(y, u, w / total_weight) for y, u, w in raw]

        minimum, average = exact_shift_profile(pairs, h)
        formula = sum(w * min(Fraction(1), abs(y - u) / h) for y, u, w in pairs)
        first_moment_bound = sum(w * abs(y - u) / h for y, u, w in pairs)
        max_average_violation = max(max_average_violation, average - formula)
        max_existence_violation = max(max_existence_violation, minimum - average)
        assert average == formula
        assert minimum <= average <= first_moment_bound

        second_moment = sum(w * (y - u) ** 2 for y, u, w in pairs)
        first_moment = sum(w * abs(y - u) for y, u, w in pairs)
        assert first_moment**2 <= second_moment

    result = {
        "status": "exact-rational shifted monotone-rounding guard",
        "hostile_weighted_measures": fixtures,
        "maximum_average_formula_violation": str(max_average_violation),
        "maximum_existence_violation": str(max_existence_violation),
        "certified_i3322_coefficient": "40*sqrt(10)/h",
        "all_gates_pass": True,
        "claim_boundary": (
            "This certifies paired contact rounding. Dihedral reflection closure "
            "and the final dimension inequality remain open."
        ),
    }
    target = Path(__file__).with_name("shifted-rounding-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
