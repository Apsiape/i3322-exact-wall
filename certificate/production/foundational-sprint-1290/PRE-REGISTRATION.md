# Pre-registration: exact fixed-witness Bellman threshold

## Observation already known

The Sprint 1287 rational certificate deliberately raised the historical source
value to

```text
q_hat = 0.250876384514
```

and certified a global residual greater than `8.89e-7`. The rigorous
upper/lower window is about `1.189e-6`, so most of that window may be certificate
padding rather than a structural separation.

## Wager

Keep the committed 6,401 rational knots fixed. Search, in exact `Fraction`
arithmetic, for the smallest multiple of `10^-15` for which the same global
piecewise-linear Bellman proof passes.

The search must use the complete exact partition and exact quadratic minima;
floating point may not decide pass or fail.

## Registered predictions

1. The fixed witness certifies an upper endpoint below `0.2508756`.
2. It does not certify the historical source value near
   `0.2508753845139765`; interpolation and rationalization leave a real
   positive tax.
3. The resulting rigorous upper/lower window is below `4e-7`.
4. Rechecking the returned predecessor grid point fails, while the returned
   grid point passes.
5. The generic Bellman-to-I3322 operator weld remains unchanged.

## Claim boundary

This is an optimization of one already committed witness, not a proof of the
exact optimum. A smaller upper endpoint cannot by itself establish equality,
nonattainment, nonclosure, or a tensor/commuting separation.

## Decision

- If the window remains above `4e-7`, the safety-padding diagnosis fails.
- If it falls below `4e-7`, use the Bellman--Hellinger gap identity to split
  the residual window between contact slack and marginal-balance slack before
  attempting any new characteristic construction.
