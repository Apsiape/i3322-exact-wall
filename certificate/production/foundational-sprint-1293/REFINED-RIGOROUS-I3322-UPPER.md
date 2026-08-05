# Refined rigorous I3322 upper certificate

Status: **exact 25,601-knot rational Bellman theorem**

## Theorem

In the repository normalization,

```text
omega_tensor <= omega_commuting <= 0.250875391558130.
```

The upper endpoint is the exact rational number

```text
25087539155813 / 100000000000000.
```

Together with the exact dimension-255 lower strategy,

```text
0.2508753845015185 < omega_tensor
                     <= omega_commuting <= 0.250875391558130,
```

with exact width recorded in `exact-refined-witness-threshold.json` and
decimal width

```text
7.056611488552207e-9.
```

## Certificate

The floating builder applies the same ordered Bellman-envelope iteration as
Sprint 1287 on a uniform 25,601-knot grid. It converges in 180 iterations and
commits every knot as an 18-place decimal rational. The candidate hash is

```text
920bcf40ea1ef92f262180a75aaeb9d7588d692011009ba8736e6d3e1b1612f1.
```

The theorem verifier then uses only exact `Fraction` arithmetic. It rebuilds
20,758 retained support lines and checks 45,465 common linearity intervals per
threshold evaluation. Exact binary search on the `10^-15` grid proves

```text
0.250875391558130  passes,
0.250875391558129  fails.
```

The passing point has a strictly positive exact minimum numerator; the failing
predecessor has a strictly negative one. The abstract Bellman-to-I3322
operator weld is unchanged.

## What this resolves

The former `1.10e-7` window was not stable under mesh refinement. A fourfold
increase in knot count reduced it to `7.06e-9`, close to the factor-sixteen
behavior expected from piecewise-linear interpolation error. This strongly
retypes the previous gap as certificate discretization rather than evidence
of a tensor/commuting separation.

## Claim boundary

This is an exact upper bound, not an exact-value theorem. It is sharp only on
the `10^-15` grid for this fixed piecewise-linear witness. It does not prove
equality at the historical candidate, finite-dimensional nonattainment at the
true optimum, tensor/commuting separation, or nonclosure.
