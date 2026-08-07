#!/usr/bin/env python3
"""Exact-rational guard for G1 endpoint contradiction arithmetic and provenance separation."""
from fractions import Fraction as F

Splus = F(250875388108398, 10**15)
rplus = F(4039, 100000)
rminus = F(9893, 50000)
third = F(1, 3)

ub_g1 = Splus - rplus
ub_gm1 = Splus - rminus
reserve_plus = third - ub_g1
reserve_minus = third - ub_gm1

assert ub_g1 == F(105242694054199, 500000000000000)
assert ub_gm1 == F(26507694054199, 500000000000000)
assert reserve_plus == F(184271917837403, 1500000000000000)
assert reserve_minus == F(420476917837403, 1500000000000000)
assert reserve_plus > 0 and reserve_minus > 0

# Exact Theorem-(N) endpoint margins are a DIFFERENT receipt family.
m_plus = F(23686917837403, 3008753881083980)
m_minus = F(274562305945801, 4008753881083980)
assert rplus != m_plus and rminus != m_minus

print("PASS G1 endpoint arithmetic")
print("  coarse endpoint-line reserve +: 4039/100000")
print("  coarse endpoint-line reserve -: 9893/50000")
print(f"  1/3 - [Splus-4039/100000] = {reserve_plus}")
print(f"  1/3 - [Splus-9893/50000] = {reserve_minus}")
print("  provenance guard: coarse rationals are not exact Theorem-(N) m_+,m_-")
