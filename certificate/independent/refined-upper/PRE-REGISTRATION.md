# Pre-registration: independent refined-upper reconstruction

## Independence contract

Write a separate standard-library-only verifier that imports no production
engine. It may read the committed 25,601 rational knots and the published
passing/failing endpoints, but it must independently:

1. reconstruct the exact support-line hull;
2. rebuild the common partition with the piecewise-linear witness;
3. minimize every exact quadratic numerator at the passing endpoint;
4. exhibit a negative exact numerator at the preceding endpoint;
5. reproduce the global worst interval and certify strict knot positivity.

## Targets

- exactly 25,601 knots and complete domain coverage;
- a nonnegative global minimum at `0.250875391558130`;
- a negative global minimum at `0.250875391558129`;
- exact agreement with the production endpoint and worst-interval receipt;
- no import of the production threshold engine.

## Claim boundary

This independently reconstructs the arithmetic proof for one shared witness.
It is not an independent witness search and does not identify the exact I3322
optimum.
