# Release notes — v3.1.0 (2026-08-05)

## Headline

**Theorem (S): the common I3322 value `S` is attained by a normal spatial
strategy on `ell^2(Z) tensor ell^2(Z)`.** Combined with v3.0.0's Theorem
(N) (no finite-dimensional strategy attains `S`):

- **`C_qs(3,3;2,2) \ C_q(3,3;2,2)` is nonempty.**

## What is new relative to the decertified historical route

The 2026 historical release claimed spatial attainment via a bi-infinite
wall whose global amplitude-compatibility equation was later exactly
refuted (Sprint 1285). The new route does not repair that equation — it
dissolves it. The proof starts from a maximizing commuting state
(weak-* compactness), derives exact kernel equations with the transport
blocks `W = Y(B_3 - I/2)` and `W_B = (A_3 - I/2)V` (no global CS
involution is assumed to exist — it need not), disintegrates only the
scalar spectral measure over countable response orbits, and reads the
amplitudes off the conditional probability measure. Consistency,
normalization, and `l^2` summability are therefore inherited, and the
amplitude cocycle and the Jacobi eigenvalue equation `H lambda = S
lambda` are derived, not imposed. The finite (no-endpoint) Pal--Vertesi
block identity then installs the eigenpair as a normal spatial strategy.

## Review record

The candidate was audited by the same independent refutation-first
referee lineage that signed Theorem (N). The audit found two genuine
holes (a circular fixed-point exclusion whose unqualified form was
false, and a globally nonexistent CS involution), supplied and verified
both repairs, and signed conditionally; the executed repairs (V1-V9)
ship with the certificate together with the full verdict and the
retired first candidate. All Sprint-1195 objects appear on the signed
dependency list's explicit not-used list.

## Claim boundary (binding)

- `S` is identified ONLY by the certified window
  `(0.2508753845015185, 0.250875388108398]`.
- The historical spatial construction remains decertified; it is
  superseded, not restored.
- Open and not claimed: the exact optimum beyond the window; the
  dimension-necessity lower bound.
- Package scripts are algebraic smoke tests and finite synthetic
  controls only; the analytic proof and the review record are
  load-bearing.

## Changes

- New certificate directory
  `certificate/production/theorem-S-spatial-attainment-at-S/`.
- README, certificate status alert, certificate map, manuscript banner
  (Markdown and rebuilt PDF), technical-supplement banner updated.
- Metadata to v3.1.0 with extended title.
