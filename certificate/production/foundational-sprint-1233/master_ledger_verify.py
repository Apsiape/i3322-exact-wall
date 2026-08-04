"""Exact-rational adversary for Sprint 1233's master discard ledger."""

from __future__ import annotations

from fractions import Fraction as F
import random


A = F(400)
M = F(78, 5)


def hostile(seed: int = 1233, trials: int = 50000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        d = rng.randrange(1, 16)
        alpha = F(rng.randrange(1, 20), rng.randrange(1, 10))
        beta = F(rng.randrange(1, 20), rng.randrange(1, 10))
        lam = F(rng.randrange(1, 20), rng.randrange(1, 10))

        # Registered sufficient lower threshold from the small-loss algebra.
        threshold = 1 / (
            2 * beta * (1 + lam) * d * (d + 1) * (A * M * M) ** d
        )
        t = threshold * F(rng.randrange(1, 1000), 1000)
        loss = lam * A**d * t
        w = 1 - alpha * t - loss
        if w >= F(1, 2):
            lower = w / ((d + 1) * M ** (2 * d))
            upper = beta * (d * t + loss)
            # Below the registered threshold the two bills cannot coexist.
            assert lower > upper

        # Rate identity, guarded independently of the fixture branch.
        assert A * A * M**4 == (20 * M) ** 4
        checks += 1
    return checks


def main() -> None:
    checks = hostile()
    print("==== SPRINT 1233 MASTER LEDGER GUARD ====")
    print(f"PASS exact-rational adversarial fixtures: {checks}")
    print(f"rate base = {(20*M)**4}")


if __name__ == "__main__":
    main()

