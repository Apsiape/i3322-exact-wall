# Every regularized flag is a rectangle of one finite measure

Status: **exact unification theorem; no universal dimension lower bound claimed**

Let `mu_rho` be the order-resolution event measure of Sprint 1247.  Because
`K_t=-dW_t/d log(t)` and `W_t` tends to zero as `t` tends to infinity,

```text
mu_rho(A x [log(t),infinity))
 =Tr[E(A) W_t(rho)].                                 (1)
```

Thus the mixed cumulative quantities used in Sprints 1242--1244 are exactly
the masses of axis-aligned rectangles:

```text
Tr[E_s W_t(rho)]
 =mu_rho((order<=s) x (resolution>=log(t))).         (2)
```

The ordered flag, the soft support, the regularized determinant derivative,
and the amplitude-cocycle scale are four views of the same positive measure.

## Captured mass

If `Tr(rho)=1`, its nonzero eigenvalues obey `0<lambda_j<=1`.  Hence

```text
M_t:=mu_rho(all order x [log(t),infinity))
    =sum_j lambda_j/(t+lambda_j),                    (3)

1/(1+t)<=M_t<=min(rank(rho),1/t).                    (4)
```

The lower bound follows from
`lambda/(t+lambda)>=lambda/(t+1)` and summing.  The two upper bounds follow
from `lambda/(t+lambda)<=1` and `<=lambda/t`.

In particular, at every `t<=1`, at least half a unit of event mass remains
above the cut, independent of Schmidt rank and of the smallest Schmidt
coefficient.  This is the nonvanishing core on which a robust order argument
may act.

## The boundary that cannot be deleted

The complement below the cut has mass

```text
rank(rho)-M_t.                                       (5)
```

It may be large even when its ordinary state mass is tiny: each nonzero
Schmidt direction contributes one total event, but a direction with
`lambda<<t` lies almost entirely below `log(t)`.  Response translation can
move mass across this boundary.  Therefore restricting to a fixed resolution
tail creates an explicit flux term at `log(t)`.

This is the canonical version of the obstruction found by the independent
packet audits: a globally small response defect does not control a restricted
sector unless inbound and outbound boundary flux are charged.  The event
measure does not make that obstruction disappear.  It makes the missing term
typed and measurable.

## Quantitative consequence already available

For coefficient operators `M,N`, Sprint 1242 gives

```text
||W_t(M)-W_t(N)||_HS
 <=(||M||_op+||N||_op) ||M-N||_HS/t.                (6)
```

Consequently every rank-`k` ordered projection `E` obeys

```text
|mu_M(E x [log(t),infinity))
 -mu_N(E x [log(t),infinity))|
 <=sqrt(k)(||M||_op+||N||_op)||M-N||_HS/t.          (7)
```

Sprint 1249 subsequently improves (6)--(7) by self-adjoint dilation to the
dimension-free square-root estimate

```text
||W_t(M)-W_t(N)||_HS
 <=[3 sqrt(6)/(8 sqrt(t))]||M-N||_HS.                (8)
```

Taking `t=exp(-L)` therefore shows the sharper unavoidable tradeoff:

```text
deeper resolution captures more Schmidt directions,
but amplifies a response defect by exp(L/2).          (9)
```

The constructive I3322 wall has Schmidt coefficients separated on an
exponential scale, so an exponential dimension law is the natural outcome of
optimizing (9).  This theorem does not perform that optimization.  The next
gate is a full-measure response-flux inequality on the skew action, followed
by a cut chosen only after every boundary crossing is charged.
