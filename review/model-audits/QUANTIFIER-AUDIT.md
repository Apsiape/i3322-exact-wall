# Lane Q — quantifiers and asymptotics

**Reviewer verdict:** `CORRECTABLE`  
**Repository state audited:** prospective v1.3 branch before review repairs  
**Edits by reviewer:** none

## Principal finding

The reviewer found no refutation of the quantitative theorem, but identified a
proof-presentation gap in the constructive exponent.  The manuscript states
only

```text
lambda_(j+1)/lambda_j -> R^-1
```

and then concludes

```text
q_* - v_L = exp[-(2L+1) log R + O(1)].
```

A ratio limit alone gives only an `o(L)` correction.  For example,
`lambda_n=R^-n exp(sqrt(n))` has the advertised ratio limit but an
`O(sqrt(n))`, rather than `O(1)`, logarithmic correction.  The reviewer found
the stronger input in the analytic unstable-manifold construction: exponential
convergence to the plateau yields summable ratio errors and therefore

```text
lambda_j  = C_+ R^-j (1+O(rho^j)),
lambda_-j = C_- R^-j (1+O(rho^j)),
```

for positive `C_+`, `C_-` and `0<rho<1`.  That stronger estimate must be
stated before the bounded-prefactor conclusion is used.

## Additional corrections

- Replace “the upper estimate is attained by explicit truncations” by
  “witnessed by explicit truncations.”  The truncations are not proved to
  attain `Q_d`.
- Define `Q_d` in the main manuscript as allowing arbitrary mixed states, not
  only by conventional implication.
- State explicitly that the `O(1)` in the all-dimension theorem is independent
  of `d`.

## Obligations checked and accepted

The reviewer independently checked the following points and found them sound:

- compact attainment of `Q_d`, including padding smaller dimensions;
- same-dimension reduction to a pure state and projective effects without a
  Naimark dilation;
- transfer of the projective-optimizer lower bound to mixed/POVM strategies;
- validity of compressed projections as binary effects;
- the exact two-edge boundary-flux identity;
- odd-dimensional truncations and even-dimensional padding;
- the lower-bound case split, `Gamma=312^4`, and the displayed `kappa`;
- inversion to the logarithmic dimension law once the constructive bound is
  available; and
- the projector/dichotomic normalization conversion.

The report classifies the needed repair as public proof clarification, not a
counterexample to the theorem.
