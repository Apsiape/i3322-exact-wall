# Pre-registration: independent endpoint-clustered upper reconstruction

## Independence contract

Write a standard-library-only exact verifier that imports neither the Sprint
1294 theorem engine nor any earlier threshold engine.  It may read the shared
committed nonuniform witness and the published adjacent endpoints.

It must independently:

1. verify the exact reflected nonuniform grid and candidate hash;
2. reconstruct the affine support-line hull;
3. intersect hull cells with mesh cells by ordered two-pointer traversal,
   rather than the production breakpoint/bisection construction;
4. minimize every resulting quadratic numerator at both endpoints;
5. reproduce the production hull count, cell count, exact minima, and worst
   receipts; and
6. preserve the distinction between certificate closure and failure of the
   preregistered performance targets.

## Expected outcome

- `0.250875388108398` passes exactly;
- `0.250875388108397` fails exactly;
- the certificate closes while the two quantitative predictions remain
  recorded as failed.

## Claim boundary

This is an independent arithmetic reconstruction for a shared searched
witness.  It is not an independent witness search, an exact optimum theorem,
or evidence that the registered mesh is optimal.
