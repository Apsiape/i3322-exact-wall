# The two I3322 responses compose to one exact skew action

Status: **exact equality-case theorem; robust flux remains open**

## 1. One common event measure

At exact Bellman contact, let `u=Y(X)` on Alice and use `U` on Bob.  The
coefficient intertwining relation

```text
E_s D=D F_s^T                                             (1)
```

for every cumulative threshold, together with
`W_A,t D=D W_B,t`, identifies the Alice and Bob rectangle masses.  By the
monotone-class theorem their order-resolution event measures are one finite
measure `mu`.

## 2. The two involutions

Write

```text
alpha(u)^2=F(-P(u))/F(P(u)),
beta(u)^2 =F(u)/F(-u),                                  (2)

a(u)=P^(-1)(-P(u)),       b(u)=-u.                      (3)
```

The exact Alice response correspondence gives

```text
C_A rho_A C_A=J_A rho_A J_A.                           (4)
```

The left side translates event resolution by `2 log alpha(u)`; the right
side pushes order through `a`.  Therefore `mu` is invariant under

```text
T_A(u,zeta)=(a(u),zeta+2 log alpha(u)).                (5)
```

The Bob correspondence gives similarly

```text
T_B(u,zeta)=(-u,zeta+2 log beta(u)).                    (6)
```

The identities `alpha(a(u))=1/alpha(u)` and
`beta(-u)=1/beta(u)` make both transformations involutions, as required by
the unitary response operators.

## 3. Composition and cocycle orientation

Apply Bob first and Alice second.  Then

```text
T=T_A o T_B,
T(u,zeta)=(tau(u),zeta+h(u)),

tau(u)=a(-u),
h(u)=2 log beta(u)+2 log alpha(-u).                   (7)
```

Using (2),

```text
exp(h(u))
 =F(u)F(-P(-u))/[F(-u)F(P(-u))]
 =C(u).                                                (8)
```

This is exactly the cocycle orientation certified in Sprint 1214.  Thus

```text
T(u,zeta)=(tau(u),zeta+log C(u)).                     (9)
```

The packet amplitude recursion, the log-resolution translation, and the
response-measure composition are the same skew action in three coordinates.

## 4. Finite-mass closure recovers nonattainment

In finite local dimension, the horizontal coordinate has finite spectral
support.  Both `a` and `b` are decreasing, so `tau=a o b` is increasing.  A
finite orbit of an increasing interval map contains no nontrivial cycle:
every recurrent point is fixed.  Invariance of the horizontal marginal of
`mu` therefore forces every occupied `u` to satisfy

```text
tau(u)=u.                                              (10)
```

Since `a` is an involution, `a(-u)=u` implies `a(u)=-u`; the two response
reversals coincide on occupied support, exactly as in Sprint 1198.

At such a fixed base point, the conditional vertical measure is finite and is
invariant under translation by `log C(u)`.  A nonzero finite measure on the
real line cannot be invariant under a nonzero translation.  Hence

```text
C(u)=1                                                (11)
```

on every occupied point.  Equations (10)--(11) are the order and amplitude
closure conditions used by Sprint 1198 to prove the quarter ceiling.  Since
the certified wall has `q_*>1/4`, no finite-dimensional equality strategy
exists.

This is not a new nonattainment claim.  It is a successful end-to-end sanity
test of the event-measure architecture: it recovers the existing exact theorem
without packets, determinants, or a Schmidt-basis choice.

## 5. The robust target

For a near-optimal finite-dimensional strategy, `mu` is only approximately
common and approximately invariant after a vertical cut.  The remaining
theorem must quantify the dichotomy behind (10)--(11):

```text
order moves by tau(u)-u,
or resolution moves by log C(u),
or event mass crosses the chosen boundary.            (12)
```

The Bellman closure margin says the first two cannot both vanish on a
positive state-mass region when the value exceeds `1/4`.  Sprint 1249 prices
the approximation error by `exp(L/2)sqrt(epsilon)` at depth `L`.  What remains
is to turn (12) into a full-measure flux inequality with no uncharged
restriction.

