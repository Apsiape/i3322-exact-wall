#!/usr/bin/env python3
"""Exact guard for finite sequential maximization of a multilinear objective."""

from __future__ import annotations

import itertools
import random


DENOMINATOR = 17
VARIABLES = 6


def value_scaled(coefficients: list[int], numerators: list[int]) -> int:
    """Return DENOMINATOR**VARIABLES times the exact polynomial value."""
    total = 0
    for mask, coefficient in enumerate(coefficients):
        term = coefficient
        degree = 0
        for index, numerator in enumerate(numerators):
            if mask & (1 << index):
                term *= numerator
                degree += 1
        total += term * DENOMINATOR ** (VARIABLES - degree)
    return total


def sequential_vertex(coefficients: list[int], start: list[int]) -> list[int]:
    point = list(start)  # coordinates are exact numerators over DENOMINATOR
    for index in range(len(point)):
        at_zero = list(point)
        at_one = list(point)
        at_zero[index] = 0
        at_one[index] = DENOMINATOR
        point = at_one if value_scaled(coefficients, at_one) >= value_scaled(coefficients, at_zero) else at_zero
    return point


def hostile(seed: int = 1237, trials: int = 50_000) -> int:
    rng = random.Random(seed)
    checks = 0
    for trial in range(trials):
        coefficients = [rng.randrange(-20, 21) for _ in range(1 << VARIABLES)]
        start = [rng.randrange(0, DENOMINATOR + 1) for _ in range(VARIABLES)]
        endpoint = sequential_vertex(coefficients, start)
        assert value_scaled(coefficients, endpoint) >= value_scaled(coefficients, start)
        assert all(coordinate in (0, DENOMINATOR) for coordinate in endpoint)

        # On a held-out 1/100 subset, independently enumerate the whole cube.
        if trial % 100 == 0:
            maximum = max(
                value_scaled(coefficients, [DENOMINATOR * bit for bit in vertex])
                for vertex in itertools.product((0, 1), repeat=VARIABLES)
            )
            assert maximum >= value_scaled(coefficients, endpoint)
        checks += 1
    return checks


def main() -> None:
    checks = hostile()
    print("==== SPRINT 1237 SAME-DIMENSION EXTREME REDUCTION ====")
    print(f"PASS exact-rational multilinear fixtures: {checks}")
    print("PASS sequential replacement never lowers the objective")


if __name__ == "__main__":
    main()
