# Rigorous dimension-255 I3322 lower strategy

Status: **exact finite tensor-product lower bound**

## Theorem

The committed 255-dimensional aligned strategy has value strictly above

```text
0.2508753845015185.
```

More precisely, `exact-dimension-255-lower-bound.json` records the exact
rational lower bound obtained by replacing every square root in the direct
Jacobi quotient with a certified 60-place rational floor.

Combined with the exact Sprint 1293 commuting upper bound,

```text
0.2508753845015185 < omega_tensor
                     <= omega_commuting <= 0.250875391558130.
```

The resulting unconditional window is

```text
7.056611488552207e-9.
```

## Search receipt

The floating builder reached the registered 1,000-iteration cap with final
profile update `3.58046925441613e-13`, above its borrowed `2e-14` search
tolerance. This miss is recorded and was not repaired by changing the search
after the fact.

Optimizer convergence is not a premise of this theorem. The committed profile
and state are simply an explicit legal finite strategy, and the theorem-stage
calculation evaluates that fixed strategy directly using exact rationals. All
255 committed state amplitudes are strictly positive; the smallest is about
`5.6662e-6`.

## Exact certificate

The verifier checks:

- the SHA-256 hash of the complete profile/state payload;
- exact endpoints and all 254 strict interior coordinates;
- strict positivity of every committed amplitude;
- every rational square-root lower enclosure;
- the exact normalized diagonal and neighbor numerators;
- the lower endpoint against the then-current Sprint 1290 exact fraction.

The lower certificate itself remains current. Sprint 1293 subsequently
supersedes only the upper endpoint and window reported by the original JSON.

## Claim boundary

This is achievability by one finite tensor-product strategy. It does not prove
optimality in dimension 255, identify the unrestricted exact optimum, prove
nonattainment, separate tensor from commuting models, or imply nonclosure.
