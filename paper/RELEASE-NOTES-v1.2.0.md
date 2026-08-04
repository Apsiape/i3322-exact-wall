# v1.2.0 -- explicit spatial attainment

Version 1.2.0 strengthens the exact I3322 wall theorem by making an omitted
consequence explicit.

## New theorem

The bi-infinite wall certified in Sprint 1195 has a positive geometrically
decaying eigenvector `lambda in ell^2(Z)`. Installing its cosine profile in the
alternating Pal--Vertesi rank-one projector blocks and using

```text
psi = sum_j lambda_j e_j tensor e_j
```

gives a normal spatial strategy with I3322 value exactly `q_*`. Combined with
the finite-dimensional nonattainment theorem,

```text
C_q(3,3;2,2) != C_qs(3,3;2,2).
```

Together with the v1.1 compactness theorem, `(3,3;2,2)` is coordinatewise
minimal by bipartite binary input counts for this separation and for
nonclosure of `C_q`.

## Verification added

- a production engine checks 24 exact-rational open and endpoint-free
  alternating carriers;
- every correct Bell-to-Jacobi residual is zero;
- deleting one alternating receiver gives a nonzero residual in all 24
  controls;
- a separate symbolic engine reconstructs the smallest endpoint-free carrier
  containing both parities and reduces the Bell residual to zero modulo only
  the unit-circle relations;
- the infinite passage is analytic, using direct-sum projections and absolute
  convergence from `lambda in ell^2`.

## Priority boundary

The alternating construction and its infinite-dimensional interpretation are
due to Pal and Vertesi (2010). General `C_q != C_qs` separation was already
proved by Coladangelo and Stark (2018). The new content is the exact I3322
upper and nonattainment theorem applied to the certified spatial wall, closing
the conjectured I3322 instance in the minimal binary input scenario.

## Correction

Earlier versions said that spatial attainment of `q_*` remained open. That
was an assembly error: the certified wall theorem already contained the
required normalizable two-sided eigenvector, but the manuscript used it only
to construct finite Rayleigh quotients. Version 1.2 corrects that omission
openly.
