# Pre-registration: independent dimension-255 witness reconstruction

## Independence contract

Write a separate `mpmath.iv` evaluator that imports no production verifier and
does not reuse its rational square-root floor routine. It may read only the
committed decimal candidate and the production report for a final concordance
comparison performed after the direct interval is assembled.

## Targets

1. Reconstruct the normalized Jacobi quotient directly with actual interval
   square roots at 160 decimal digits.
2. Verify the candidate payload hash independently.
3. Enclose the value in an interval of width below `1e-100`.
4. Prove the direct interval lies above the production rational floor.
5. Confirm the direct interval lies below the Sprint 1290 upper endpoint.

## Claim boundary

This is independent arithmetic evaluation of one shared witness, not an
independent witness search and not a proof of optimality.
