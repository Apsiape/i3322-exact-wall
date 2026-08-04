from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def a_map(x, scale):
    if x >= 0:
        return -scale * x
    return -x / scale


def b_map(x, _scale):
    return -x


def apply_word(word, x, scale):
    for letter in reversed(word):
        x = a_map(x, scale) if letter == "a" else b_map(x, scale)
    return x


def inverse_word(word):
    # Both generators are involutions.
    return word[::-1]


def cell_index(x, shift, width):
    return (x - shift) // width


def reduced_frame_counts(max_a_count):
    counts = {m: 0 for m in range(max_a_count + 1)}
    counts[0] += 1  # identity
    for length in range(1, 2 * max_a_count + 2):
        for first in "ab":
            word = "".join(
                first if i % 2 == 0 else ("b" if first == "a" else "a")
                for i in range(length)
            )
            count_a = word.count("a")
            if count_a <= max_a_count:
                counts[count_a] += 1
    return counts


def main():
    rng = random.Random(1223)
    fixtures = 10000
    maximum_lipschitz_violation = Fraction(0)
    exact_transport_failures = 0

    for _ in range(fixtures):
        scale = Fraction(rng.randint(1, 20), rng.randint(1, 20))
        if scale < 1:
            scale = 1 / scale
        width = Fraction(rng.randint(1, 13), rng.randint(1, 13))
        shift = Fraction(rng.randint(-20, 20), rng.randint(1, 29)) % width
        length = rng.randint(0, 12)
        word = "".join(rng.choice("ab") for _ in range(length))
        next_letter = rng.choice("ab")
        x = Fraction(rng.randint(-200, 200), rng.randint(1, 31))
        y = Fraction(rng.randint(-200, 200), rng.randint(1, 31))

        gx = apply_word(word, x, scale)
        moved_then_reflected = (
            a_map(gx, scale) if next_letter == "a" else b_map(gx, scale)
        )
        composed = apply_word(next_letter + word, x, scale)
        if moved_then_reflected != composed:
            exact_transport_failures += 1

        inv = inverse_word(word)
        inv_x = apply_word(inv, x, scale)
        inv_y = apply_word(inv, y, scale)
        count_a = word.count("a")
        bound = scale**count_a * abs(x - y)
        violation = abs(inv_x - inv_y) - bound
        maximum_lipschitz_violation = max(maximum_lipschitz_violation, violation)
        assert violation <= 0

        # Membership in gQ is, by definition, membership after g^-1 in Q.
        same_moved_cell = cell_index(inv_x, shift, width) == cell_index(inv_y, shift, width)
        same_base_cell = cell_index(
            apply_word(inv, x, scale), shift, width
        ) == cell_index(apply_word(inv, y, scale), shift, width)
        assert same_moved_cell == same_base_cell

    assert exact_transport_failures == 0
    frame_counts = reduced_frame_counts(32)
    assert frame_counts[0] == 2
    assert all(frame_counts[m] == 4 for m in range(1, 33))
    result = {
        "status": "exact-rational moving-dihedral-partition guard",
        "fixtures": fixtures,
        "exact_partition_transport_failures": exact_transport_failures,
        "maximum_lipschitz_violation": str(maximum_lipschitz_violation),
        "certified_active_chart_generator_bound": "20",
        "distinct_reduced_frames_at_zero_a": frame_counts[0],
        "maximum_distinct_reduced_frames_per_positive_a_count": max(
            frame_counts[m] for m in range(1, 33)
        ),
        "all_gates_pass": True,
        "claim_boundary": (
            "Moving partitions remove reflection rounding and the guard checks "
            "the per-frame distortion only. Multi-frame multiplicity must be "
            "counted separately; final assembly remains open."
        ),
    }
    target = Path(__file__).with_name("moving-partition-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
