# Pre-registration: 25,601-knot exact Bellman refinement

## Wager

The remaining certified upper tax is primarily the interpolation error of the
6,401-knot piecewise-linear Bellman witness, not a stable separation from the
historical numerical candidate.

Hold the construction and source value fixed, replace the uniform mesh by
25,601 knots, commit every knot as an 18-place decimal rational, and search
for the first passing `10^-15` upper endpoint using the full exact support-line
partition and exact quadratic minima.

Floating point may choose the witness. It may not decide any theorem gate.

## Registered targets

1. The floating builder completes before its fixed iteration cap and emits a
   strictly positive 25,601-knot candidate.
2. The exact candidate hash and complete domain partition verify.
3. The exact passing endpoint lies below `0.25087542`.
4. The immediately preceding `10^-15` grid point fails.
5. Paired with the independently reconstructed dimension-255 lower strategy,
   the unconditional window is below `4e-8`.
6. The abstract Bellman-to-I3322 operator weld is unchanged.

## Failure routing

- If target 3 or 5 fails, uniform refinement is demoted and the next witness
  must use contact-adaptive knots or direct convex optimization.
- If the floating iteration fails to settle but the explicit witness passes
  the theorem targets, record the search miss as non-load-bearing, as in
  Sprint 1292.
- No result identifies the exact optimum, proves nonattainment, separates
  tensor from commuting models, or proves nonclosure.
