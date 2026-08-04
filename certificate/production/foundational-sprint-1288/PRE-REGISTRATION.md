# Pre-registration: independent finite-strategy lower bound

## Question

Can one certify a strong lower bound for the true I3322 quantum value using a
single explicit finite-dimensional strategy, without using the failed global
wall normalization, a Bellman fixed point, or an infinite gluing argument?

## Candidate family

Use only the finite aligned Pal--Vertesi/Jacobi family.  For a finite list

```text
c_0=1, c_n=-1,  -1<c_j<1,
```

let the `n x n` real symmetric matrix have

```text
H_jj       = d(c_j,c_(j+1)),
H_(j-1),j  = sqrt(1-c_j^2)/2.
```

The already exact local block identity shows that every normalized vector
`lambda` yields an admissible finite tensor-product I3322 strategy with value
`lambda^T H lambda`.  No claim about the global optimum is used in this
direction.

## Construction and exact proof boundary

1. Numerically optimize a moderate finite profile and positive vector.
2. Quantize every internal `c_j` and every vector coordinate to committed
   rational decimal data.
3. In the theorem verifier, bound each `sqrt(1-c_j^2)` from below by an exact
   rational square-root floor and evaluate the resulting Rayleigh quotient
   entirely with `Fraction` arithmetic.
4. The floating optimizer is a witness search only and has no proof authority.

## Registered gates

1. the candidate has matching dimensions, exact endpoints, and all internal
   coordinates strictly inside `(-1,1)`;
2. the committed vector is nonzero and strictly positive;
3. every rational square-root floor is positive and its square is no greater
   than `1-c_j^2`;
4. the exact denominator `sum lambda_j^2` is positive;
5. the exact certified Bell value exceeds `0.250875`;
6. the rigorous interval width obtained with Sprint 1287's exact upper bound
   is below `1.4e-6`.

The target `0.250875` is intentionally weaker than the historical wall value.
If it fails, the new upper bound remains valid and the failure localizes the
remaining issue to finite lower-strategy reconstruction.  If it passes, the
repository will certify a nontrivial two-sided window for the true value while
leaving exact equality, nonattainment, separation, and nonclosure open.
