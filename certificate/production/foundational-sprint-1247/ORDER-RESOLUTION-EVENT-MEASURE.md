# Schmidt rank is the total mass of an order-resolution event measure

Status: **exact canonical lift; quantitative I3322 escape theorem remains open**

## 1. Definition

Let `rho>=0` be a finite-dimensional density operator and let `E` be the
spectral projection-valued measure of an ordered coordinate.  For `t>0`, put

```text
W_t(rho)=rho(tI+rho)^(-1),
K_t(rho)=t rho(tI+rho)^(-2).                         (1)
```

Since

```text
K_t(rho)=-d W_t(rho)/d log(t),                      (2)
```

define a measure on `order x log-resolution` by

```text
mu_rho(A x I)
 =integral_I Tr[E(A) K_(exp(zeta))(rho)] d zeta.    (3)
```

This is positive even when `E(A)` and `rho` do not commute, because for a
projection `P` and a positive operator `K`,

```text
Tr(PK)=Tr(K^(1/2) P K^(1/2))>=0.                    (4)
```

## 2. Rank is mass, exactly

For every nonzero eigenvalue `lambda`,

```text
integral_(-infinity)^infinity
 exp(zeta) lambda/[exp(zeta)+lambda]^2 d zeta
 =integral_0^infinity lambda/(t+lambda)^2 dt
 =1.                                                (5)
```

Zero eigenvalues contribute nothing.  Therefore

```text
mu_rho(all order x R)=rank(rho).                    (6)
```

More precisely, the vertical integral is the support projection:

```text
integral_R K_(exp(zeta))(rho) d zeta=P_supp(rho).  (7)
```

Thus each Schmidt direction contributes exactly one unit of event mass.  Its
log-resolution profile is a logistic derivative centred at `log(lambda)`.
The normalization `Tr(rho)=1` anchors those centres through
`sum exp(log(lambda_j))=1`; an arbitrary common vertical translation is not
available.

There is a second exact moment identity.  The scalar density in (5) is a
translated logistic derivative: after `zeta=log(lambda)+r` it is
`exp(r)/(1+exp(r))^2`, an even probability density in `r`.  Its mean is zero.
Writing `log^+(rho)` for the logarithm on the support of `rho` and zero on its
kernel gives

```text
integral_R zeta K_(exp(zeta))(rho) d zeta=log^+(rho). (8)
```

Consequently

```text
integral_(A x R) zeta d mu_rho
 =Tr[E(A) log^+(rho)].                                (9)
```

The zeroth moment of the same measure is rank; its first moment is the
flag-localized log-determinant potential.  The flag and volume campaigns are
therefore two marginals of one object, not competing constructions.

## 3. Exact response action

If `rho` commutes with an ordered multiplier `C=c(X)>0`, then on a joint
spectral block

```text
K_t(C rho C)=K_(t/c^2)(rho).                       (10)
```

Consequently the event measure is pushed forward by

```text
(x,zeta) -> (x,zeta+2 log c(x)).                  (11)
```

Sprint 1245 described the dual action on the *query* `t`: evaluating the new
operator at `t` evaluates the old one at `t/c^2`.  Equation (11) records the
same fact as motion of the event centre and fixes the apparent sign ambiguity.

If `U` is unitary, replacing `(rho,E)` by
`(U rho U^*, U E U^*)` leaves (3) unchanged.  Hence an exact response
correspondence acts on the measure by the order reversal supplied by the
response involution together with the vertical translation (11).

For exact I3322 contact, Sprint 1245 proves the commutation needed here.  The
two responses therefore act on one canonical finite measure by the two order
reversals and the certified amplitude cocycle.  Their composition is not
merely a scalar packet recursion; it is a skew action on

```text
ordered contact coordinate x logarithmic Schmidt resolution.             (14)
```

When `C` and `rho` do not commute, the first-moment response is instead

```text
Tr E[log^+(C rho C)-log^+(rho)].                    (12)
```

For full support its total at `E=I` is still `2 log det(C)`, but a proper
ordered flag need not receive `2 Tr(E log C)`.  The difference

```text
A_E(C,rho)
 =Tr E[log(C rho C)-log(rho)-2 log(C)]              (13)
```

is a noncommutative allocation term.  It vanishes in the exact contact
regime, where `rho` and the response multiplier are jointly decomposable,
but it must be charged in a near-contact proof rather than silently treated
as scalar scale transport.

## 4. Why this changes the finite-rank problem

The earlier packet arguments assigned mass to an arbitrary grid and then
lost branch provenance.  The measure (3) has no grid and loses no Schmidt
direction:

- the horizontal coordinate is the full cumulative spectral flag;
- the vertical coordinate is the full regularization filtration;
- its total mass is exactly the Schmidt rank;
- response multipliers act as translations rather than changing the
  bookkeeping convention.

The desired dimension theorem can now be phrased as a finite-measure escape
statement.  On a region where the composed I3322 skew action has a directed
vertical drift, an exactly invariant finite measure cannot carry positive
mass.  A near-invariant measure can do so only by placing event mass near a
vertical boundary.  Because `Tr(rho)=1` anchors the upper boundary and only
`d` unit-mass profiles are available, that boundary payment is expected to be
exponential in `d`.

That last quantitative statement is not proved here.  Equations (3)--(14)
identify a canonical object on which it can be proved without packet cells,
deleted complements, or a chosen Schmidt basis.
