# Certificate status alert — 2026-08-04

The theorem package in the frozen `v1.0.0`, `v1.1.0`, and `v1.2.0` archives
should currently be read as a **historical claim under correction**, not as a
closed computer-assisted proof.

An exact 400-bit Arb audit performed after those releases found a nonzero
global-amplitude mismatch in the Bellman datum on the complete unique-root
bracket:

```text
target amplitude - reflected source amplitude
in [0.00014027592551842303, 0.00017894047518170395].
```

The interval excludes zero.  This exposes a load-bearing normalization gap in
the current Bellman upper-bound assembly.  The audit is reproducible from
`certificate/production/foundational-sprint-1285/` and is incorporated into
the release verifier at repository HEAD.

A second engine in `certificate/independent/amplitude-gap/` independently
reconstructs the degree-12 chart and map with `mpmath.iv`, proves strict
monotonicity across the complete bracket, and encloses the same gap in

```text
[0.00014027599579792882, 0.00017894040323422364].
```

The two certified intervals overlap.  The negative audit therefore no longer
depends on the production Arb implementation.

This finding does **not** establish that the reported numerical constant is
wrong.  It establishes that the present proof of the global Bellman upper
bound is incomplete.  Consequently, until a corrected global normalization or
an independent upper bound is certified, repository HEAD does not certify:

- equality of the tensor-product or commuting-operator supremum with `q_*`;
- finite-dimensional nonattainment at that value;
- the claimed `C_qs \ C_q` witness or nonclosure corollary; or
- a finite-section deficit measured from the true I3322 optimum.

Exact local shooting, spatial-wall, boundary-flux, and algebraic receipts are
retained.  Their valid conditional content is not erased by the failed weld.
## Rigorous partial repair

Sprint 1287 supplies an independent global normalization route. Its committed
rational piecewise-linear function is checked using standard-library
`Fraction` arithmetic over every common interval of the function and its
exact support-line envelope. Sprint 1294 repeats that construction on a
symmetric endpoint-clustered 25,601-knot grid and exactly locates the
fixed-witness threshold on a `10^-15` grid.

The exact geometric-reflection/operator weld uses no fixed-point identity,
concavity, contact uniqueness, wall orbit, or shooting-chart amplitude. It
therefore proves the unconditional bound

```text
omega_tensor <= omega_commuting <= 0.250875388108398.
```

This is a real theorem repair, but it is deliberately narrower than the frozen
headline. It does not identify the exact optimum and does not restore
nonattainment, `C_qs \ C_q`, or nonclosure. At the Sprint 1294 endpoint the
exact global minimum is positive, while its immediate `10^-15` predecessor
fails. A separately written exact engine reconstructs the hull, all 46,458
common intervals, and both endpoint receipts without importing the production
verifier. Its preregistered performance target failed and is retained in the
receipt. Proximity to the historical wall candidate is not used as an equality
theorem.

Sprint 1292 supplies the strongest current lower side: a committed
255-dimensional finite tensor-product strategy evaluated with exact rational
square-root floors and reconstructed independently with 160-digit interval
arithmetic. Repository HEAD therefore proves the unconditional window

```text
0.2508753845015185 < omega_tensor
                   <= omega_commuting <= 0.250875388108398,
```

whose exact certified width is approximately `3.606879488552207e-9`. This
still does not identify the exact optimum or restore any nonattainment or
correlation-set separation claim.

## Model-value equality repair

Sprint 1295 proves a separate universal Bellman--path equivalence.  Combined
with the arbitrary-positive-storage operator weld from Sprint 1287 and the
exact Pal--Vertesi principal-block carrier, it gives

```text
omega_tensor(I3322) = omega_commuting(I3322)
                    = the common Bellman/path variational value.
```

The proof neither imports nor repairs the failed shooting-amplitude assembly.
It is independently reconstructed by exact source/target, Schur-pivot, weld,
and carrier attacks.  Thus the shrinking numerical window brackets one common
value, not two potentially different values.  The common value is not yet
identified with the historical decimal, so finite-dimensional nonattainment,
spatial attainment at the true value, and nonclosure remain open.

## Repair signal, not yet a repair

Sprint 1286 directly iterates the globally selected Bellman operator without
a positivity floor. Across four resolutions, all tested offsets at or below
`q_*-10^-6` collapse when the offset is negative, while the displayed
shooting value and all tested positive offsets converge to positive profiles.
The two finest zero-offset profile minima agree within `6.53e-7`.

This suggests that the same scalar may be independently characterized as the
global Bellman positivity threshold. It is a numerical, preregistered signal,
not an interval proof and not a restoration of the headline theorem. Sprint
1287 completes the first direct globally normalized subsolution above that
threshold; closing the remaining approximately `1e-6` gap requires a limiting
or adaptive exact certificate, or a separate certified lower strategy.
