#!/usr/bin/env python3
"""Exact rational endpoint-line certificate.

The floating grid is used only to select finite histories.
All pivots, affine lines, envelope intersections, and final margin checks are
then recomputed exactly over Q.
"""

from fractions import Fraction
import json
import math
import numpy as np

S_LO = Fraction(2508753845015185, 10**16)
S_HI = Fraction(250875388108398, 10**15)
Q0 = S_HI + Fraction(1, 10**7)

N = 2001
DEPTH = 100
grid_float = np.linspace(-1.0, 1.0, N)
grid_rat = [Fraction(-1) + Fraction(j, 1000) for j in range(N)]

def b2_float(x):
    return (1.0 - x*x) / 4.0

def d_float(x, u):
    return x*u + (x-u)/2.0 - 1.0

q0_float = float(Q0)
D = (
    grid_float[:, None] * grid_float[None, :]
    + (grid_float[:, None] - grid_float[None, :]) / 2.0
    - 1.0
)
U = np.min(q0_float - D, axis=0)
for _ in range(1000):
    new = np.minimum(
        U,
        np.min(
            q0_float
            - D
            - b2_float(grid_float)[:, None] / U[:, None],
            axis=0,
        ),
    )
    if np.max(np.abs(new-U)) < 1e-13:
        U = new
        break
    U = new

Pidx = np.argmin(
    q0_float
    - D
    - b2_float(grid_float)[:, None] / U[:, None],
    axis=0,
)

def b2(x):
    return (1-x*x) / 4

def d(x, u):
    return x*u + (x-u)/2 - 1

def exact_history_line(target_index):
    indices = [target_index]
    cur = target_index
    for _ in range(DEPTH):
        cur = int(Pidx[cur])
        indices.append(cur)
    indices.reverse()

    fixed = [grid_rat[k] for k in indices[:-1]]
    p = Q0 - d(fixed[0], fixed[1])
    assert p > 0

    for k in range(1, len(fixed)-1):
        p = Q0 - d(fixed[k], fixed[k+1]) - b2(fixed[k]) / p
        assert p > 0

    source = fixed[-1]
    intercept = Q0 + 1 - source/2 - b2(source)/p
    slope = Fraction(1, 2) - source
    return intercept, slope

# One minimum intercept for each repeated slope.
by_slope = {}
for j in range(N):
    a, m = exact_history_line(j)
    if m not in by_slope or a < by_slope[m]:
        by_slope[m] = a

lines = [(by_slope[m], m) for m in sorted(by_slope, reverse=True)]

# Exact lower envelope. As target increases, active slopes decrease.
hull = []
for a, m in lines:
    intersection = None
    while hull:
        a0, m0, start0 = hull[-1]
        intersection = (a-a0)/(m0-m)
        if start0 is not None and intersection <= start0:
            hull.pop()
        else:
            break
    start = None if not hull else intersection
    hull.append((a, m, start))

segments = []
for k, (a, m, start) in enumerate(hull):
    end = hull[k+1][2] if k+1 < len(hull) else None
    left = Fraction(-1) if start is None or start < -1 else start
    right = Fraction(1) if end is None or end > 1 else end
    if left < right:
        segments.append((left, right, a, m))

def minimum_affine_difference(Ea, Em):
    best = None
    where = None
    for left, right, a, m in segments:
        for x in (left, right):
            value = (Ea + Em*x) - (a + m*x)
            if best is None or value < best:
                best = value
                where = x
    return best, where

margin_plus, where_plus = minimum_affine_difference(
    S_LO + Fraction(1, 2),
    Fraction(-1, 2),
)
margin_minus, where_minus = minimum_affine_difference(
    S_LO + Fraction(3, 2),
    Fraction(3, 2),
)

floor_plus = Fraction(4039, 100000)
floor_minus = Fraction(9893, 50000)

assert margin_plus > floor_plus
assert margin_minus > floor_minus

result = {
    "scope": "exact rational certificate after heuristic history selection",
    "q0": str(Q0),
    "grid_points": N,
    "history_depth": DEPTH,
    "selected_unique_slopes": len(lines),
    "active_envelope_segments": len(segments),
    "all_exact_pivots_positive": True,
    "margin_plus_exact": str(margin_plus),
    "margin_plus_decimal": float(margin_plus),
    "margin_plus_location": float(where_plus),
    "certified_floor_plus": str(floor_plus),
    "margin_minus_exact": str(margin_minus),
    "margin_minus_decimal": float(margin_minus),
    "margin_minus_location": float(where_minus),
    "certified_floor_minus": str(floor_minus),
}
print(json.dumps(result, indent=2))
