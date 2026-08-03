# Finite-dimensional nonattainment of the I3322 supremum

Status: **finite-dimensional tensor-product theorem, conditional on the
validated Bellman fixed point of Sprint 1195**

## Theorem

In the normalization of Sprints 1114--1198, the I3322 tensor-product quantum
supremum is

```text
q_* = 0.250875384513976536... +/- 4.9e-19,
```

and no finite-dimensional tensor-product strategy attains it.

Together with Sprint 1197, this proves the two claims isolated in the frozen
external target of Sprint 1114: the exact validated supremum and genuinely
unbounded finite-dimensional approach.

## 1. Equality must annihilate all three remainders

Sprint 1197 proves

```text
q_* I-B = R_0+R_A+R_B,
R_0,R_A,R_B >= 0.                                      (1)
```

If a unit vector `psi` attained `q_*`, positivity would give

```text
R_0 psi=R_A psi=R_B psi=0.                              (2)
```

Binary effects may be projectivized in a finite dilation, so it is enough to
consider projective measurements. Equivalently, at a finite attaining point,
hold the state and the other effects fixed and replace each binary effect by
an extreme maximizer of its linear objective; extreme binary effects are
projections, and the global upper bound prevents the value from increasing
beyond `q_*`. Put

```text
X=A1+A2-I,  Y=A2-A1,  U=B1+B2-I,  V=B2-B1,
S_A=2A3-I,  S_B=2B3-I.
```

On every interior CS fiber,

```text
Y=2b(X)J_A,  V=2b(U)J_B,
b(t)=sqrt(1-t^2)/2,                                    (3)
```

where `J_A,J_B` are self-adjoint involutions that reverse the signs of the
corresponding CS coordinates.

## 2. The transport kernel is a reversible contact graph

The scalar value of `R_0` at a joint spectral pair `(x,u)` is

```text
q_*-d(x,u)-A(x)-B(u),
d(x,u)=xu+(x-u)/2-1.                                   (4)
```

The proof of (4) uses two Bellman inequalities:

```text
p(x)+F(u)       <= q_*-d(x,u),
F(-x)+p(-u)     <= q_*-d(x,u),                         (5)
p(t)=b(t)^2/F(t).
```

If (4) vanishes, both inequalities in (5) and the intervening Cauchy
inequality are equalities.  The first Bellman contact has the unique
predecessor

```text
x=P(u),                                                   (6)
```

and the reflected contact gives

```text
-u=P(-x).                                                 (7)
```

Here `P` is the strictly increasing predecessor map certified in Sprints
1192--1195.  Thus the zero set of `R_0` is a one-to-one increasing graph and
its reflected contact.  Equations (6)--(7) also keep every zero pair in the
interior; no endpoint division is needed below.

Let `Sigma` be the finite set of `u`-coordinates for which the joint spectral
component of `psi` is nonzero.  Because (6) is one-to-one, a member of
`Sigma` identifies the complete occupied pair `(P(u),u)`.

## 3. The two response kernels are the same finite reversal

Writing the local remainders from Sprint 1197 with (3), equation (2) gives

```text
A(X) psi = b(X)(J_A tensor S_B) psi,
B(U) psi = b(U)(S_A tensor J_B) psi.                    (8)
```

All coefficients are positive on the transport zero set.  The first unitary
in (8) flips `x`; uniqueness of the transport graph therefore maps the scalar
support by

```text
a(u)=P^{-1}(-P(u)).                                     (9)
```

The second flips `u` directly and maps it by

```text
b_map(u)=-u.                                            (10)
```

Both maps are decreasing bijections of the same finite ordered set `Sigma`.
A direct component equation makes the support claim explicit. Define

```text
K_A=J_A tensor S_B,  K_B=S_A tensor J_B,
r_A(x)=A(x)/b(x),    r_B(u)=B(u)/b(u).
```

Then (8) is `K_A psi=r_A(X)psi` and
`K_B psi=r_B(U)psi`. If
`psi_u=(E_{P(u)} tensor F_u)psi`, joint spectral projection gives

```text
K_A psi_u = r_A(-P(u)) psi_{a(u)},
K_B psi_u = r_B(-u)    psi_{b_map(u)}.                 (10a)
```

No cancellation between different source components is possible: `P` is
injective, so after the sign flip distinct sources occupy distinct `X` (or
`U`) eigenspaces. Unitarity and positivity make both maps preserve nonzero
support in both directions.

A finite totally ordered set has exactly one decreasing bijection: its first
element must map to the last, its second to the penultimate, and so on.
Consequently

```text
a=b_map on Sigma.                                       (11)
```

For every occupied `(x,u)`, its common partner is therefore `(-x,-u)`, and

```text
x=P(u),  -x=P(-u).                                      (12)
```

This is the finite-closure step.  No Schmidt alignment or Jacobi normal form
has been assumed.

## 4. Amplitude holonomy forces the quarter ceiling

Let `psi_+` and `psi_-` be the nonzero components at `(x,u)` and `(-x,-u)`.
Taking norms in the two equations (8) gives the same component ratio in two
ways:

```text
rho = ||psi_-||/||psi_+||
    = sqrt(F(-x)/F(x))
    = sqrt(F(u)/F(-u)).                                 (13)
```

Equality in both Bellman inequalities (5) and in Cauchy now fixes the four
values of `F`:

```text
F(x)=b_x/rho,   F(-x)=rho b_x,
F(u)=rho b_u,   F(-u)=b_u/rho,                          (14)
```

where `b_x=b(x)` and `b_u=b(u)`.  Hence, at the two reflected components,

```text
q_*-d(x,u)     = rho(b_x+b_u),
q_*-d(-x,-u)  = (b_x+b_u)/rho.                         (15)
```

Subtracting (15) gives

```text
x-u=(b_x+b_u)(1/rho-rho).                              (16)
```

Using (16) in the first equation of (15) yields

```text
q_* = xu-1+sqrt((b_x+b_u)^2+(x-u)^2/4).                (17)
```

Put `s_x=sqrt(1-x^2)`, `s_u=sqrt(1-u^2)`, and
`t=1-xu>=0`.  The radical in (17) satisfies

```text
(b_x+b_u)^2+(x-u)^2/4
  = (1-xu+s_x s_u)/2
  <= t,                                                 (18)
```

because

```text
(1-xu)^2-s_x^2 s_u^2=(x-u)^2>=0.                       (19)
```

Therefore

```text
q_* <= -t+sqrt(t) <= 1/4,                              (20)
```

the last inequality being

```text
1/4-[-t+sqrt(t)]=(sqrt(t)-1/2)^2>=0.
```

But the validated connection interval has `q_*>1/4`.  This contradiction
proves finite-dimensional nonattainment.

## 5. Scope

The proof is dimension-independent but uses finite spectral support exactly
once: two decreasing bijections of a finite ordered set must coincide.  That
step is false for an infinite order type; the domain-wall strategy escapes by
carrying a non-closing ordered support with asymmetric tail amplitudes.

The theorem concerns finite-dimensional tensor-product quantum strategies.
It does not identify the commuting-operator value, claim experimental access
to the supremum, or support any foundational interpretation.  The important
mathematical mechanism is narrower: **finite closure converts the two local
kernel transports into the same reversal, and their amplitude holonomy then
forces the ordinary `1/4` ceiling.**
