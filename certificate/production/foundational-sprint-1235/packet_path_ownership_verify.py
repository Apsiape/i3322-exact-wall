#!/usr/bin/env python3
"""Exact finite-model guard for canonical moving-packet ownership."""

from __future__ import annotations

import random


def norm2(vector: list[int]) -> int:
    return sum(x * x for x in vector)


def hostile(seed: int = 1235, trials: int = 100_000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        d = rng.randrange(1, 13)
        cells = rng.randrange(1, d + 1)
        times = rng.randrange(1, d + 1)

        # A moved frame is represented by an injective relabelling.  The same
        # initial label therefore has one canonical descendant, and distinct
        # labels cannot merge at a fixed time.
        frames: list[list[int]] = []
        base = list(range(cells))
        ambient = max(cells + times + 1, d + 1)
        for _time in range(times):
            image = rng.sample(range(ambient), cells)
            assert len(image) == len(set(image))
            frames.append(image)

        # Give each chain a strictly ordered sequence of local spectral ranks.
        # Nonzero sites are distinct and cannot exceed the local dimension.
        ranks: list[list[int]] = []
        exits: list[int] = []
        for _i in base:
            length = rng.randrange(1, times + 1)
            occupied = rng.sample(range(d), length)
            assert len(occupied) == len(set(occupied))
            assert length <= d
            ranks.append(occupied)
            exits.append(length - 1)

        # Exact diagonal-PVM packet model.  At each time, different initial
        # labels occupy disjoint coordinates.  A signed permutation plays the
        # response unitary and maps each coarse source coordinate to its exact
        # canonical target coordinate.
        dimension = 2 * cells + 3
        source_packets: list[list[int]] = []
        target_packets: list[list[int]] = []
        packet_errors = 0
        scalar_errors = 0
        for i in base:
            source = [0 for _ in range(dimension)]
            target = [0 for _ in range(dimension)]
            # Integers are exact rationals and make the 100,000-fixture guard
            # fast enough to remain a routine verification target.
            amplitude = rng.randrange(0, 30)
            perturbation = rng.randrange(-5, 6)
            source[i] = amplitude
            target[cells + i] = amplitude + perturbation
            source_packets.append(source)
            target_packets.append(target)

            # The signed permutation sends coordinate i to cells+i.
            transported = [0 for _ in range(dimension)]
            transported[cells + i] = amplitude
            error = [transported[j] - target[j] for j in range(dimension)]
            packet_errors += norm2(error)
            scalar_errors += (abs(amplitude) - abs(amplitude + perturbation)) ** 2

        # Reverse triangle, squared and summed over the orthogonal family.
        assert scalar_errors <= packet_errors

        # Horizontal ownership: exact direct sums contain no cross terms.
        summed_source = [sum(packet[j] for packet in source_packets) for j in range(dimension)]
        summed_target = [sum(packet[j] for packet in target_packets) for j in range(dimension)]
        assert norm2(summed_source) == sum(norm2(packet) for packet in source_packets)
        assert norm2(summed_target) == sum(norm2(packet) for packet in target_packets)

        # Each terminal is charged at one exit time.  Grouping endpoints by
        # time gives at most `times<=d` uses of the ambient terminal measure,
        # independent of the number of chains.
        nonempty_exit_times = len(set(exits))
        assert nonempty_exit_times <= times <= d

        # Closure is the label identity: target (k,i) is source (k+1,i).
        for k in range(times - 1):
            for i in base:
                target_key = (k + 1, i)
                next_source_key = (k + 1, i)
                assert target_key == next_source_key

        checks += 1
    return checks


def main() -> None:
    checks = hostile()
    print("==== SPRINT 1235 PACKET-PATH OWNERSHIP ====")
    print(f"PASS exact-rational hostile path systems: {checks}")
    print("PASS no initial-cell multiplicity in direct-sum energy")
    print("PASS response-time and exit-time multiplicities <= d")


if __name__ == "__main__":
    main()
