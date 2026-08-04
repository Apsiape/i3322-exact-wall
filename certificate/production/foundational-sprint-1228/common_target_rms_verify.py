"""Independent guards for Sprint 1228's common-target RMS theorem."""

from __future__ import annotations

from fractions import Fraction
import math
import random


def exact_ratio_guards() -> int:
    checks = 0
    for m in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        for M in (Fraction(2), Fraction(3), Fraction(5)):
            for omega in (Fraction(1, 100), Fraction(1, 20)):
                ell_s = M - omega
                ell_t = m + omega
                p = ell_s - omega
                pp = ell_t + omega
                assert pp >= m and ell_t >= m
                lhs = abs(p / pp - ell_s / ell_t)
                rhs = omega * (1 / m + M / (m * m))
                assert lhs <= rhs
                checks += 1
    return checks


def random_packet_guards(seed: int = 1228, trials: int = 10000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        n = rng.randrange(1, 12)
        lv = [rng.uniform(-2, 2) for _ in range(n)]
        lw = [rng.uniform(-2, 2) for _ in range(n)]
        # Orthogonal/unitary transport is irrelevant to reverse triangle;
        # lv and lw are the two transported weighted packet vectors.
        a = math.sqrt(sum(x * x for x in lv))
        b = math.sqrt(sum(x * x for x in lw))
        e = math.sqrt(sum((x - y) ** 2 for x, y in zip(lv, lw)))
        assert abs(a - b) <= e + 1e-14

        z = rng.uniform(0.05, 3)
        zp = rng.uniform(0.05, 3)
        p = a / z if a else 0.0
        pp = b / zp if b else 0.0
        if pp > 0:
            lhs = abs(zp - (p / pp) * z)
            assert lhs <= e / pp + 1e-12
        checks += 1
    return checks


def many_chain_guard(seed: int = 2281, trials: int = 10000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        d = rng.randrange(1, 30)
        n = rng.randrange(1, d + 1)
        M = Fraction(rng.randrange(1, 8), 1)
        assert n * n * M ** (2 * (n - 1)) <= d * d * M ** (2 * (d - 1))
        checks += 1
    return checks


def main() -> None:
    exact = exact_ratio_guards()
    packets = random_packet_guards()
    chains = many_chain_guard()
    print("==== SPRINT 1228 COMMON-TARGET RMS GUARD ====")
    print(f"PASS exact ratio fixtures: {exact}")
    print(f"PASS Euclidean packet fixtures: {packets}")
    print(f"PASS many-chain monotonicity fixtures: {chains}")


if __name__ == "__main__":
    main()

