"""Exact-rational guard for Sprint 1230's reverse endpoint theorem."""

from __future__ import annotations

from fractions import Fraction as F
import random


def iterate(chain, z0):
    z = z0
    residuals = []
    for c, s in chain:
        residuals.append(s)
        z = c * z + s
    return z, residuals


def hostile(seed: int = 1230, trials: int = 20000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        d = rng.randrange(1, 14)
        M = F(rng.randrange(1, 7), 1)
        total_initial = F(0)
        total_bill = F(0)
        for _chain in range(rng.randrange(1, 20)):
            n = rng.randrange(0, d + 1)
            z0 = F(rng.randrange(0, 30), 11)
            chain = []
            for _ in range(n):
                num = rng.randrange(1, int(M) + 1)
                den = rng.randrange(1, int(M) + 1)
                c = F(num, den)
                assert c <= M and 1 / c <= M
                s = F(rng.randrange(-20, 21), 13)
                chain.append((c, s))
            zn, residuals = iterate(chain, z0)
            total_initial += z0 * z0
            total_bill += zn * zn + sum(s * s for s in residuals)
        assert total_bill >= total_initial / ((d + 1) * M ** (2 * d))
        checks += 1
    return checks


def main() -> None:
    checks = hostile()
    print("==== SPRINT 1230 FINITE-RANK EXIT GUARD ====")
    print(f"PASS exact-rational hostile fixtures: {checks}")


if __name__ == "__main__":
    main()

