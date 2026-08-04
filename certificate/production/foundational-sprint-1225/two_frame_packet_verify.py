from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def norm_sq(vector):
    return sum(x * x for x in vector)


def permute(vector, permutation):
    result = [Fraction(0) for _ in vector]
    for source, target in enumerate(permutation):
        result[target] = vector[source]
    return result


def main():
    rng = random.Random(1225)
    fixtures = 10000
    maximum_squared_violation = Fraction(0)

    for _ in range(fixtures):
        dimension = rng.randint(2, 40)
        blocks = rng.randint(1, dimension)
        labels = list(range(blocks))
        labels.extend(rng.randrange(blocks) for _ in range(dimension - blocks))
        rng.shuffle(labels)

        permutation = list(range(dimension))
        rng.shuffle(permutation)
        target_labels = [None] * dimension
        for source, target in enumerate(permutation):
            target_labels[target] = labels[source]

        source_keep = [rng.choice((False, True)) for _ in range(dimension)]
        target_keep = [rng.choice((False, True)) for _ in range(dimension)]
        vector = [Fraction(rng.randint(-20, 20), rng.randint(1, 20)) for _ in range(dimension)]
        transformed = permute(vector, permutation)

        # K is the permutation. Kw-w is evaluated in the common ambient basis.
        delta_sq = norm_sq([transformed[i] - vector[i] for i in range(dimension)])
        gamma_s_sq = norm_sq(
            [vector[i] if not source_keep[i] else Fraction(0) for i in range(dimension)]
        )
        gamma_t_sq = norm_sq(
            [vector[i] if not target_keep[i] else Fraction(0) for i in range(dimension)]
        )

        packet_error_sq = Fraction(0)
        for block in range(blocks):
            source_packet = [
                vector[i] if labels[i] == block and source_keep[i] else Fraction(0)
                for i in range(dimension)
            ]
            moved_source = permute(source_packet, permutation)
            target_packet = [
                vector[i]
                if target_labels[i] == block and target_keep[i]
                else Fraction(0)
                for i in range(dimension)
            ]
            packet_error_sq += norm_sq(
                [moved_source[i] - target_packet[i] for i in range(dimension)]
            )

        bound = 3 * (delta_sq + gamma_s_sq + gamma_t_sq)
        violation = packet_error_sq - bound
        maximum_squared_violation = max(maximum_squared_violation, violation)
        assert violation <= 0

    result = {
        "status": "exact-rational two-frame packet-transport guard",
        "hostile_fixtures": fixtures,
        "maximum_squared_bound_violation": str(maximum_squared_violation),
        "coordinate_step_error_required": False,
        "all_gates_pass": True,
        "claim_boundary": (
            "Exact addresses and packet-energy transport are certified. "
            "Near-fixed charging and final constant assembly remain open."
        ),
    }
    target = Path(__file__).with_name("two-frame-packet-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
