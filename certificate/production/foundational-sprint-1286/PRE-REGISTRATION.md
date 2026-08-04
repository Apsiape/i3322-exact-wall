# Pre-registration: global Bellman criticality scout

## Motivation and disclosed pilot

After Sprint 1285 invalidated the local-chart normalization, an unregistered
`N=3201` pilot iterated the Bellman operator directly from its affine boundary
cap without a positivity floor.  Every tested value below the shooting
constant collapsed to a nonpositive iterate, while the shooting constant and
one value above it converged to positive fixed points.

This pilot is not evidence graded as registered.  The following fixed
resolution/offset experiment is registered before its engine is written.

## Operator and instrument

For a grid on `[-1,1]`, start from

```text
B_q(y)=q+(1-y)/2
```

and iterate

```text
F_{n+1}(y)=min(B_q(y), min_x [q+1-x/2-(x-1/2)y-(1-x^2)/(4F_n(x))]).
```

Use the exact ordered lower hull of the grid lines, not an `N x N` matrix.
Do not clip or replace nonpositive values.  Classify a run as:

- `collapsed` at the first iterate with `min F<=0`;
- `fixed` when the sup difference falls below `1e-11` while `F>0`;
- `unresolved` after 5,000 iterations.

Run resolutions

```text
N = 801, 1601, 3201, 6401
```

at offsets from the displayed shooting center

```text
-1e-4, -1e-5, -1e-6, 0, +1e-6, +1e-5, +1e-4.
```

## Registered gates

1. every negative-offset run collapses at every resolution;
2. the zero-offset run converges positively at every resolution;
3. every positive-offset run converges positively at every resolution;
4. the zero-offset fixed profiles retain `min F>0.04`;
5. the zero-offset minimum values agree between `N=3201` and `N=6401` within
   `5e-5`;
6. no run is unresolved.

Passing classifies the shooting constant as a **resolution-robust numerical
critical point** of the global Bellman positivity problem, furnishing a repair
route independent of local reversible normalization.  It is not an interval
proof of criticality, a proof that the exact shooting root equals the Bellman
threshold, or a restored I3322 theorem.
