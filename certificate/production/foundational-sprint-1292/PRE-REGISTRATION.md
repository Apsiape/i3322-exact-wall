# Pre-registration: exact dimension-255 tensor lower strategy

## Prior numerical information

The repository's non-certifying dimension audit reports a dimension-255
aligned value near `0.250875384501519`. This sprint does not claim blind
discovery. It asks whether an independently committed decimal witness can be
turned into a rigorous finite-dimensional tensor lower bound.

## Wager

1. Re-run the direct profile/eigenvector optimization at dimension 255.
2. Commit the resulting decimal profile and positive state vector.
3. Hash the complete payload.
4. In a separate standard-library verifier, interpret every decimal as an
   exact rational, replace every `sqrt(1-c_j^2)` by a certified 60-place
   rational floor, and evaluate the normalized Jacobi quotient exactly.

## Registered targets

- all 255 state amplitudes remain strictly positive after decimal commitment;
- all 254 interior profile coordinates lie strictly in `(-1,1)`;
- every rational square-root floor is valid;
- the certified value exceeds `0.2508753844`;
- combined with Sprint 1290, the unconditional rigorous window is below
  `1.2e-7`.

## Claim boundary

The witness is one explicit finite tensor-product strategy. It cannot prove
the exact optimum, nonattainment, tensor/commuting separation, nonclosure, or
optimality among dimension-255 strategies.

## Decision

- If decimal tail truncation creates a zero amplitude or destroys the target,
  increase witness precision rather than silently altering the test.
- If the exact floor certificate lands, reconstruct the same committed witness
  with an independent interval engine before promoting the new public window.
