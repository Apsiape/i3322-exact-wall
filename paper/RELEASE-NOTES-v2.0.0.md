# v2.0.0 release notes — correction and certified value window

This is a **correction release**. The major version signals a change in
what the archive asserts, not an extension of it.

## What this release withdraws

A post-release 400-bit exact-arithmetic audit (Sprint 1285) found a
nonzero global-amplitude mismatch in the Bellman upper-bound assembly of
the earlier releases, enclosed in

```text
[0.00014027592551842303, 0.00017894047518170395],
```

excluding zero, and independently reproduced by a separately implemented
`mpmath.iv` engine with an overlapping enclosure. The weld between the
reflected charts fails as previously asserted. Consequently the following
claims of v1.0.0–v1.2.0 are **under correction and not asserted here**:

- identification of the exact I3322 optimum with the historical constant;
- equality of the tensor-product and commuting-operator suprema;
- finite-dimensional nonattainment;
- the spatial C_qs \ C_q witness and nonclosure of C_q(3,3;2,2);
- deficit statements measured from the true optimum.

The numerical candidate is not thereby disproved. The earlier releases
remain archived unchanged as historical records; nothing is deleted.

A structural explanation of the failure is included (Sprint 1289):
Bellman contact determines support, while amplitude normalization is a
separate KKT marginal-balance law; the failed weld conflated the two.

## What this release rigorously certifies

Unconditionally, with exact rational certificates:

```text
0.2508753845015185 < omega_tensor <= omega_commuting <= 0.250875388108398
```

with window width below `3.607e-9`.

- **Lower endpoint:** an explicit 255-dimensional tensor-product strategy
  committed as rational data, evaluated entirely in exact arithmetic with
  rational square-root floors, and independently reconstructed at
  160-digit interval precision (Sprint 1292).
- **Upper endpoint:** an exact rational piecewise-linear Bellman
  subsolution with a symmetric endpoint-clustered 25,601-knot witness,
  exactly optimized, with a separately written standard-library engine
  reproducing the nonuniform hull, all 46,458 common intervals, and both
  endpoint receipts (Sprints 1287, 1293, 1294).
- The compactness half of the earlier minimality theorem (binary
  scenarios with at most two inputs on either side are closed) is
  analytic, independent of the failed certificate, and unaffected.

One registered quantitative prediction (window below `3e-9` for the
Sprint 1294 collider) **failed** and is preserved in the record; the
exact theorem nevertheless improved the previous bound.

## Verification

The complete deterministic replay covers the frozen custody manifest,
the production certificate stack, the independent reconstructions, and
the audit that found the gap — which is retained permanently in the
release verifier:

```powershell
python certificate/release/verify_release.py
python certificate/release/verify_release.py --full
```

The verifier's own output states which certificates are closed and which
historical claims are not.

## Status of the repair programme

Preregistered numerical evidence (Sprint 1286) indicates the historical
candidate as the global Bellman positivity threshold; the certified
window contains it. The open steps are a contact-adaptive rational
witness on the upper side and a continuum Bellman–Hellinger realization
theorem. These are research targets, not assertions.
