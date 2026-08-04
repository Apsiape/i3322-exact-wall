# The two event measures are marginals of one canonical positive coupling

Status: **proved operator theorem; I3322 coarse descent remains open**

## 1. The coupling density

Represent the normalized bipartite state by its coefficient operator
`D : conjugate(H_B) -> H_A`, and put

```text
rho_A=DD*,                 rho_B=D*D,
K_t(rho)=t rho(tI+rho)^(-2),
Z_t=sqrt(t) D(tI+rho_B)^(-1).                        (1)
```

Let `E` and `F` be the spectral PVMs of the saturated Alice contact
coordinate `Y(X)` and the Bob coordinate `U`.  For measurable order sets
`A,B`, define

```text
pi_t(A,B)=||E(A) Z_t F(B)||_HS^2.                    (2)
```

This is a positive finite measure.  Orthogonality of either PVM gives its
two marginals.  The singular-functional-calculus identity

```text
D f(D*D)=f(DD*)D
```

implies

```text
Z_t Z_t*=K_t(rho_A),       Z_t*Z_t=K_t(rho_B).       (3)
```

Consequently

```text
pi_t(A,all)=Tr[E(A)K_t(rho_A)],
pi_t(all,B)=Tr[F(B)K_t(rho_B)].                      (4)
```

Integrating (2) against `d zeta`, `t=exp(zeta)`, defines a positive measure
`Pi` on

```text
Alice order x Bob order x log resolution.            (5)
```

Its two order-resolution marginals are exactly the Alice and Bob event
measures of Sprint 1247.  Its total mass is the Schmidt rank.  Thus the two
flags never needed an inferred or selected coupling: the state supplies one
canonically.

## 2. Exact contact is diagonal support

Write

```text
C=Y(X)D-DU.                                          (6)
```

If `C=0`, then `rho_B` commutes with `U`, and (1) gives

```text
Y(X)Z_t=Z_tU.                                        (7)
```

Therefore

```text
integral |y-u|^2 d pi_t(y,u)=0,                      (8)
```

so every `pi_t` and the full measure `Pi` are supported on the diagonal
`y=u`.  This recovers the common event measure without a monotone-class
identification and retains the multiplicity provenance discarded by scalar
packets.

## 3. Near contact has an explicit commutator bill

Let `R_t=(tI+rho_B)^(-1)`.  Direct algebra gives

```text
[rho_B,U]=C*D-D*C,
[U,R_t]=R_t[rho_B,U]R_t,                             (9)

Y Z_t-Z_t U
 =sqrt(t){C R_t+D[U,R_t]}.                           (10)
```

For a normalized state, `||D||<=1`.  Hence

```text
||[rho_B,U]||_HS<=2||C||_HS,

||Y Z_t-Z_t U||_HS
 <=||C||_HS(t^(-1/2)+2t^(-3/2)).                    (11)
```

For `0<t<=1`,

```text
integral |y-u|^2 d pi_t
 =||Y Z_t-Z_t U||_HS^2
 <=9 ||C||_HS^2/t^3.                                (12)
```

Sprint 1232 gives `||C||_HS^2<=40 epsilon_0`, so

```text
integral |y-u|^2 d pi_t <=360 epsilon_0/t^3.         (13)
```

The power `t^-3` is conservative.  Its significance is structural, not
numerical: contact now controls an actual coupling of the two complete soft
flags, rather than only separate cumulative traces.

## 4. What this repairs

The terminal-fork countermodel defeats attempts to identify two orthogonal
response target vectors.  It does not defeat (2): orthogonal multiplicity
fibres remain distinct matrix blocks inside the same positive coupling and
are summed only after their Hilbert--Schmidt energy has been recorded.

The remaining architecture is a finite-flow statement on `Pi`:

```text
two approximately invariant decreasing response actions
+ contact coupling cost
+ at most d units of total event mass
+ the pointwise order-or-resolution gap of Sprint 1253
=> a nonzero response/contact bill.                  (14)
```

Sprint 1255 proves the abstract finite-flow part of (14).  No dimension lower
bound is claimed until the continuous joint coupling is descended to that
flow with every contact and rounding interface charged.  The advance here is
that the flow has a canonical carrier and no uncharged common-fibre choice.
