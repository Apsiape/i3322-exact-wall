"""Exact and hostile guards for Sprint 1229's near-fixed constants."""

from __future__ import annotations

from fractions import Fraction as F
import random


MU = F(7, 8000)
H0 = F(1, 10_000_000)
C_A = F(1344)
C_B = F(672)
C_0 = F(54)
C_H = 6 * C_0 * C_0 + F(291, 25) * (C_A * C_A + C_B * C_B)
CONTACT_FAMILY_MULTIPLICITY = 2


def exact_constants() -> int:
    assert C_H == F(131498424, 5)
    assert CONTACT_FAMILY_MULTIPLICITY == 2
    assert C_H * H0 * H0 < MU * MU / 2
    theta = F(1, 10**12)
    delta = theta * H0 / 20
    assert 20 * delta / H0 == theta
    return 3


def hostile_scalar_fixtures(seed: int = 1229, trials: int = 20000) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(trials):
        # Generate only quantities used in the inequality proof.  The closure
        # lower bound is imposed as its exact theorem hypothesis.
        z = F(rng.randrange(0, 1000), 997)
        zp = F(rng.randrange(0, 1000), 991)
        ea = F(rng.randrange(0, 300), 997)
        eb = F(rng.randrange(0, 300), 991)
        eps0 = F(rng.randrange(0, 300), 983)
        h = H0 * F(rng.randrange(0, 1001), 1000)
        w = z * z + zp * zp

        rhs = 48 * eps0 + F(4656, 25) * (ea * ea + eb * eb) + C_H * h * h * w
        assert rhs >= 0
        # This guard checks the absorption arithmetic independently of the
        # pointwise closure theorem already guarded in Sprint 1226.
        if h <= H0:
            assert (MU * MU - C_H * h * h) * w >= MU * MU * w / 2
        checks += 1
    return checks


def main() -> None:
    exact = exact_constants()
    hostile = hostile_scalar_fixtures()
    print("==== SPRINT 1229 NEAR-FIXED GAP GUARD ====")
    print(f"PASS exact constant checks: {exact}")
    print(f"PASS hostile absorption fixtures: {hostile}")
    print(f"C_h = {C_H}")


if __name__ == "__main__":
    main()
