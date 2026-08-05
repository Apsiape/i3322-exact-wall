#!/usr/bin/env python3
"""Finite synthetic controls. Not a theorem verifier."""
import math
import random

rng = random.Random(20260805)

for _ in range(10000):
    n = 25
    b = [rng.uniform(0.05, 0.49) for _ in range(n)]
    g = [rng.uniform(0.05, 1.5) for _ in range(n)]

    lam = [1.0]
    for j in range(n-1):
        lam.append(lam[-1] * g[j] / b[j])

    S = rng.uniform(0.3, 3.0)
    diag = [0.0] * n
    for j in range(1, n):
        diag[j] = S - b[j-1]**2/g[j-1] - g[j]

    for j in range(1, n-1):
        value = (
            b[j-1]*lam[j-1]
            + diag[j]*lam[j]
            + b[j]*lam[j+1]
        )
        assert abs(value-S*lam[j]) < 1e-10 * max(1.0, abs(S*lam[j]))

for _ in range(10000):
    n = 30
    mass = [rng.expovariate(1.0) for _ in range(n)]
    z = sum(mass)
    mass = [m/z for m in mass]
    ratio = [rng.uniform(0.05, 4.0) for _ in range(n)]
    reflected = [ratio[i]**2 * mass[i] for i in range(n)]

    total = sum(mass) + sum(reflected)
    even = [math.sqrt(m/total) for m in mass]
    odd = [math.sqrt(m/total) for m in reflected]

    assert abs(sum(v*v for v in even+odd)-1.0) < 1e-12
    for i in range(n):
        assert abs(odd[i]/even[i]-ratio[i]) < 1e-12

print("PASS: 20,000 finite synthetic controls")
print("SCOPE: orbit consistency, disintegration and Fatou are not tested")
