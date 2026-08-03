# Exact tensor-product quantum supremum of I3322

Status: **operator theorem, conditional on the validated Bellman fixed-point
construction of Sprint 1195**

## Theorem

In the normalization used by Pal--Vertesi and throughout Sprints 1114--1197,
the tensor-product quantum supremum of the I3322 Bell functional is

```text
q_* = 0.250875384513976536... +/- 4.9e-19,
```

where `q_*` is the exact validated domain-wall connection parameter of Sprint
1116. Every finite-dimensional quantum strategy obeys `I3322<=q_*`, and the
aligned finite-dimensional sequence approaches `q_*`.

This theorem identifies the supremum. It does not yet assert that no finite
dimension attains it; that is a separate equality-kernel classification.

## 1. Exact pair coordinates

It suffices to consider binary projective measurements. Define

```text
X=A1+A2-I,   Y=A2-A1,
U=B1+B2-I,   V=B2-B1.
```

The projector relations give

```text
X^2+Y^2=I,   XY+YX=0,
U^2+V^2=I,   UV+VU=0.                       (1)
```

A direct expansion of the original I3322 functional gives

```text
B = G(X,U)
    + Y tensor (B3-I/2)
    + (A3-I/2) tensor V,                     (2)

G(X,U)=X tensor U + X/2 tensor I
       - I tensor U/2 - I.
```

The symbolic expansion and held-out random complex-matrix reconstruction are
verified by `bellman_quantum_dual_verify.py`.

## 2. Two Bellman inequalities, not a false reflection identity

Let `F>0` be the exact Bellman fixed point from Sprint 1195 and put

```text
b(x)=sqrt(1-x^2)/2,
p(x)=b(x)^2/F(x).
```

The first draft incorrectly asserted `F(x)F(-x)=b(x)^2` globally. The endpoint
wings disprove it. The corrected proof uses the forward Bellman inequality

```text
p(x)+F(u) <= q_*-d(x,u),                     (3)
d(x,u)=xu+(x-u)/2-1,
```

and the same inequality at predecessor `-u`, target `-x`:

```text
F(-x)+p(-u) <= q_*-d(-u,-x)
             = q_*-d(x,u).                   (4)
```

Define the geometrically balanced functions

```text
A(x)=sqrt(p(x)F(-x)),
B(u)=sqrt(F(u)p(-u)).                         (5)
```

Cauchy applied to (3)--(4) gives

```text
A(x)+B(u)
 <= sqrt([p(x)+F(u)][F(-x)+p(-u)])
 <= q_*-d(x,u).                              (6)
```

No symmetry of `F` is used. Direct multiplication in (5) yields the exact
local product laws

```text
A(x)A(-x)=b(x)^2,
B(u)B(-u)=b(u)^2.                            (7)
```

The polynomial identity behind the first inequality in (6) and both products
are checked independently in the verifier. The 32,001-guard hull places the
resulting dual ceiling within `6.9e-14` of `q_*`; that numerical guard is not
used in the proof.

## 3. Dual potentials and the transport remainder

Define

```text
alpha(x)=1/2-A(x),
beta(u)=q_*-1/2-B(u),
t_A=1/2,
t_B=q_*-1/2.
```

Since `X tensor I` and `I tensor U` commute, scalar functional calculus and
(6) give

```text
R_0=alpha(X) tensor I+I tensor beta(U)-G(X,U) >= 0.     (8)
```

Its scalar spectral value is exactly `q_*-d(x,u)-A(x)-B(u)`.

## 4. The two local response remainders

The CS decomposition of two projections reduces (1), away from its
one-dimensional endpoints, to fibers

```text
X = diag(x,-x),
Y = [[0,s],[s,0]],   s=sqrt(1-x^2)=2b(x),
```

up to phase. Since `||B3-I/2||<=1/2`, the Alice remainder

```text
R_A=t_A I-alpha(X) tensor I-Y tensor (B3-I/2)           (9)
```

has, on every response spectral fiber `z in [-1/2,1/2]`, diagonal entries
`A(x),A(-x)` and off-diagonal entry `-2b(x)z`. By (7), its determinant is

```text
A(x)A(-x)-4b(x)^2z^2
 = b(x)^2(1-4z^2) >= 0.                                (10)
```

Hence `R_A>=0`. The identical argument with `B` gives

```text
R_B=t_B I-I tensor beta(U)-(A3-I/2) tensor V >= 0.      (11)
```

The one-dimensional CS summands require no division. At `x=+/-1`, `Y=0` and
`A(x)=A(-x)=0` where needed, giving a zero or positive gap. At
`x=0,Y=+/-1`, (7) forces `A(0)=1/2`, and (9) is
`I/2 +/- (B3-I/2)>=0`. The Bob degeneracies are identical.

## 5. Dimension-independent Bell-operator certificate

Adding (8), (9), and (11), using `t_A+t_B=q_*`, cancels both potentials. By
(2),

```text
q_* I-B = R_0+R_A+R_B >= 0.                           (12)
```

This certificate assumes no Schmidt basis, stationarity, common frame,
path/cycle normal form, or alignment. The weighted KKT obstruction from Sprint
1116 is paid by two local PSD response remainders rather than wished away.

Binary POVMs do not enlarge the value: they may be dilated to projective
measurements, or the linear functional may be optimized at projective extreme
effects. Thus (12) bounds every finite-dimensional tensor-product strategy.

## 6. Sharpness

Sprints 1114--1116 construct the exact domain-wall strategy, and Sprint 1195
proves that its finite aligned open truncations have values converging to
`q_*`. These are legitimate finite-dimensional quantum strategies. Therefore
the quantum supremum is at least `q_*`; (12) gives the reverse inequality.

## What the proof found

The missing global object was not an alignment theorem. It was the geometric
mean of two Bellman inequalities. The scalar domain wall supplies two balanced
potentials that simultaneously:

- price transport between Alice's and Bob's CS spectra;
- absorb Alice's third response by an exact determinant;
- absorb Bob's third response by the reflected determinant.

The outer wings are not a nuisance. Their failure of naive reflection is why
the arithmetic must be geometric rather than a direct identification.

## Boundary

This is an external mathematical theorem about the tensor-product I3322
supremum. It is not evidence for the corpus's metaphysics, does not move a
physics hard-problem grade, and does not address commuting-operator
correlations beyond the tensor-product model. Finite-dimensional
nonattainment remains separate.
