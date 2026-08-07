#!/usr/bin/env python3
"""U1c guard: endpoint-projector truncation legitimacy + value approach.

SECOND-ENGINE STATUS: built from the repository artifacts alone
(ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md matching/completion
rules; the sprint-1292 Jacobi variational construction), independently
of the U1b proof text.

PART A (symbolic, sympy): for interval sizes m = 3..8 and BOTH
alternating matchings, build the truncated measurement operator per
the artifact: full 2x2 rank-one blocks with ARBITRARY symbolic angles
on interior pairs, one-dimensional projector completion at severed
endpoints. Verify P^2 = P and P = P^T EXACTLY (symbolically), for all
angle values simultaneously — stronger than any specific carrier
assignment. Local dimension = |I| by construction (asserted on shape).

PART B (mpmath, 110 digits): for d in an increasing ladder, optimize
the scalar profile (float search per the sprint-1292 iteration — the
search has no proof authority), then evaluate the top Jacobi
eigenvalue at 110-digit precision. Each profile defines an explicit
d-dimensional strategy whose Bell value is that eigenvalue — the
Jacobi-quotient-to-Bell-value bridge is the public certificate
document certificate/production/foundational-sprint-1292/
RIGOROUS-DIMENSION-255-LOWER.md (sha256 514242545b32040e34f0d879
dfe8bd745b8a0d24341b071ff93e901763351195; "the direct Jacobi
quotient" realized by "an explicit legal finite strategy"), anchored
in proof §1b. Assert: values strictly increase with d, remain
strictly below the certified upper endpoint S_HI = 0.250875388108398,
Perron vector normalization to 1e-80, and — THE LOAD-BEARING
EXHIBITION FACT (proof §1b; round-4 integrity finding 1) — the
values at d = 24 and d = 33 STRICTLY EXCEED 1/4. (Values below 1/4
at small d are expected — the PV family is not optimal there — and
claim nothing; the exhibition consumes only d = 24 and d = 33.)

Fail-capable: every assert can fire; no banner exceeds its code.
"""

from __future__ import annotations

import sympy as sp
import numpy as np
from mpmath import mp

S_HI = "0.250875388108398"
S_LO = "0.2508753845015185"


# ---------- PART A: symbolic projector legitimacy ----------

def truncated_measurement(m: int, matching: int):
    """Operator on C^m per the truncation artifact, symbolic angles.

    matching 0 pairs (0,1),(2,3),... ; matching 1 pairs (1,2),(3,4),...
    Severed endpoint indices get one-dimensional projector completion.
    """
    P = sp.zeros(m, m)
    covered = set()
    k = 0
    start = 0 if matching == 0 else 1
    j = start
    while j + 1 < m:
        th = sp.symbols(f"theta_{matching}_{j}", real=True)
        c, s = sp.cos(th), sp.sin(th)
        P[j, j] += c * c
        P[j, j + 1] += c * s
        P[j + 1, j] += c * s
        P[j + 1, j + 1] += s * s
        covered.add(j)
        covered.add(j + 1)
        j += 2
        k += 1
    # Endpoint completion: any index not covered by a full block gets a
    # one-dimensional projector (assigned to this outcome).
    for idx in range(m):
        if idx not in covered:
            P[idx, idx] += 1
    return P


def part_a() -> int:
    checked = 0
    for m in range(3, 9):
        for matching in (0, 1):
            P = truncated_measurement(m, matching)
            assert P.shape == (m, m), "local dimension must equal |I|"
            idem = sp.simplify(P * P - P)
            assert idem == sp.zeros(m, m), (
                f"P^2 != P at m={m}, matching={matching}")
            assert sp.simplify(P - P.T) == sp.zeros(m, m), (
                f"P != P^T at m={m}, matching={matching}")
            # The complementary outcome is then automatically a
            # projection; assert it anyway (fail-capable).
            Q = sp.eye(m) - P
            assert sp.simplify(Q * Q - Q) == sp.zeros(m, m)
            checked += 1
    return checked


# ---------- PART B: value ladder at 110 digits ----------

def jacobi_np(profile: np.ndarray) -> np.ndarray:
    diagonal = (profile[:-1] * profile[1:]
                + (profile[:-1] - profile[1:]) / 2.0 - 1.0)
    matrix = np.diag(diagonal)
    off = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - profile[1:-1] ** 2))
    matrix += np.diag(off, 1) + np.diag(off, -1)
    return matrix


def optimize_profile(dim: int, iters: int = 4000, damping: float = 0.65):
    plateau = 0.8782729451808125
    coord = np.arange(dim + 1, dtype=float) - dim / 2.0
    profile = -plateau * np.tanh(coord / 3.0)
    profile[0], profile[-1] = 1.0, -1.0
    for _ in range(iters):
        _, vecs = np.linalg.eigh(jacobi_np(profile))
        v = np.abs(vecs[:, -1])
        prop = profile.copy()
        left, right = v[:-1], v[1:]
        lin = ((profile[:-2] - 0.5) * left * left
               + (profile[2:] + 0.5) * right * right)
        cur = left * right
        prop[1:-1] = lin / np.sqrt(lin * lin + cur * cur)
        upd = damping * prop + (1.0 - damping) * profile
        upd[0], upd[-1] = 1.0, -1.0
        if float(np.max(np.abs(upd - profile))) < 1e-15:
            profile = upd
            break
        profile = upd
    return profile


def precise_value(profile: np.ndarray):
    """Top eigenvalue + Perron vector of the Jacobi matrix, 110 digits."""
    mp.dps = 110
    n = len(profile) - 1
    x = [mp.mpf(repr(float(t))) for t in profile]
    J = mp.zeros(n, n)
    for i in range(n):
        J[i, i] = x[i] * x[i + 1] + (x[i] - x[i + 1]) / 2 - 1
    for i in range(n - 1):
        J[i, i + 1] = J[i + 1, i] = mp.sqrt(1 - x[i + 1] ** 2) / 2
    evals, evecs = mp.eigsy(J)
    top = max(range(n), key=lambda i: evals[i])
    lam = evals[top]
    v = [evecs[i, top] for i in range(n)]
    norm = mp.sqrt(mp.fsum(t * t for t in v))
    # Rayleigh quotient of the explicit vector v: a RIGOROUS lower
    # bound on the top eigenvalue regardless of eigsy's numerics
    # (round-4 proof finding F-05(i)).
    Jv = [mp.fsum(J[i, j] * v[j] for j in range(n)) for i in range(n)]
    rq = mp.fsum(v[i] * Jv[i] for i in range(n)) / mp.fsum(
        t * t for t in v)
    return lam, norm, rq


def part_b():
    dims = [3, 4, 6, 8, 12, 16, 24, 33]
    s_hi = mp.mpf(S_HI)
    s_lo = mp.mpf(S_LO)
    values = []
    rayleigh = {}
    for d in dims:
        profile = optimize_profile(d)
        lam, norm, rq = precise_value(profile)
        # eigsy returns orthonormal eigenvectors; this is a REAL check
        # of the normalization at working precision.
        assert abs(norm - 1) < mp.mpf("1e-80"), (
            f"Perron vector not normalized at d={d}")
        assert lam < s_hi, f"value at d={d} not below certified window"
        assert abs(rq - lam) < mp.mpf("1e-60"), (
            f"Rayleigh quotient disagrees with eigsy at d={d}")
        values.append((d, lam))
        rayleigh[d] = rq
    # Strict increase (the family value ladder climbs with dimension).
    for (d1, v1), (d2, v2) in zip(values, values[1:]):
        assert v2 > v1, f"values not strictly increasing at d={d2}"
    # Genuine approach: the deficit to the certified lower endpoint is
    # strictly decreasing along the ladder.
    deficits = [(d, s_lo - v) for d, v in values]
    for (d1, e1), (d2, e2) in zip(deficits, deficits[1:]):
        assert e2 < e1, f"deficit not decreasing at d={d2}"
    # THE LOAD-BEARING EXHIBITION ASSERT (round-4 integrity finding 1):
    # the promoted fact S > 1/4 by exhibition requires the d=24 and
    # d=33 values to strictly exceed 1/4. This assert IS the
    # instrument for that fact — it must be able to fail.
    quarter = mp.mpf(1) / 4
    exhibited = {d: lam for d, lam in values}
    for d_req in (24, 33):
        assert d_req in exhibited, (
            f"exhibition dimension d={d_req} missing from the ladder — "
            f"the promoted S > 1/4 fact has no witness")
        assert exhibited[d_req] > quarter, (
            f"EXHIBITION FAILS: value at d={d_req} does not exceed 1/4")
        # The Rayleigh quotient of the EXPLICIT vector is a rigorous
        # lower bound on the top eigenvalue — the exhibition holds
        # even if eigsy's eigenvalue were distrusted (round-4 proof
        # finding F-05(i)).
        assert rayleigh[d_req] > quarter, (
            f"EXHIBITION FAILS (Rayleigh): quotient at d={d_req} does "
            f"not exceed 1/4")
    return values


def main() -> None:
    na = part_a()
    print(f"PART A PASS: {na} truncated measurements verified as exact "
          f"projections (symbolic, arbitrary block angles, m=3..8, "
          f"both matchings, complements included)")
    values = part_b()
    print("PART B PASS: value ladder (110-digit top eigenvalues)")
    quarter = mp.mpf(1) / 4
    for d, lam in values:
        marker = " (> 1/4)" if lam > quarter else ""
        print(f"  d={d:3d}  value={mp.nstr(lam, 25)}{marker}")
    print(f"  strictly increasing; all < S_HI={S_HI}; "
          f"deficit to S_LO strictly decreasing; "
          f"deficit at d=33: {mp.nstr(mp.mpf(S_LO) - values[-1][1], 8)}")
    print("NOTE: the ladder is the PV-family value, a LOWER bound on "
          "S_d; the family is not optimal at small d, so values below "
          "1/4 at small d are expected and claim nothing.")
    print("U1C GUARD: ALL PASS")


if __name__ == "__main__":
    main()
