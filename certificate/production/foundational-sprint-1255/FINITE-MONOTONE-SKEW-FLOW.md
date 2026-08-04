# Finite monotone skew flows pay a path endpoint or a fixed-point translation

Status: **proved abstract theorem; I3322 coarse coupling remains to be
assembled**

## 1. Setup

Let `S={1,...,n}`, `n<=d`, carry its natural order.  Let `A_i` and `B_i` be
two strictly decreasing lists of real output coordinates.  At source `i`,
let `mu_i` be a finite positive measure on log resolution, with tail

```text
f_i(L)=mu_i({zeta:zeta>=-L}),                        (1)
```

and let `p_i,q_i in [-B,B]`.  Define the signed horizontal tail measure

```text
sigma_L
 =sum_i f_i(L+p_i) delta_(A_i)
  -sum_i f_i(L+q_i) delta_(B_i).                    (2)
```

Put

```text
M_core=sum_i mu_i([-H,0]),
R=2Bd+B,
V=sup_{-R<=L<=H+R} ||sigma_L||_TV.                  (3)
```

Whenever `A_i=B_j`, draw a directed edge `i->j`.  Assume every fixed edge
`i->i` obeys

```text
|p_i-q_i|>=g>0.                                     (4)
```

Then

```text
boxed:
M_core <=[3d^3+(H+2B)/g] V.                         (5)
```

## 2. The graph has only paths and fixed points

Both output lists are strictly decreasing.  Hence if

```text
A_i=B_j,       A_k=B_l,       i<k,
```

then `A_i>A_k`, so `B_j>B_l`, and therefore `j<l`.  The partial map
`i->j` is increasing and injective.  Every component is a directed path or
a directed cycle.  An increasing map of a finite ordered set has no
nontrivial cycle, so every cycle is a fixed point.

This is the finite-order mechanism from the exact nonattainment proof, now
applied to complete vertical tail functions rather than packet vectors.

## 3. Path components

At a matched output `A_i=B_j`, the coefficient of `sigma_L` is

```text
r_ij(L)=f_i(L+p_i)-f_j(L+q_j).                      (6)
```

At an unmatched path endpoint, the coefficient is one nonnegative shifted
tail.  Every such coefficient has absolute value at most `V`.

Solving (6) forward along a path expresses `f_i(x)` as the terminal tail at
an argument shifted by at most `2Bd`, plus at most `d-1` residuals.  Apply
this once at `x=H` and once at `x=0`.  All required cuts lie in the interval
in (3), and

```text
mu_i([-H,0])=f_i(H)-f_i(0)<=3dV.                    (7)
```

A path has at most `d` nodes and there are at most `d` path components.
Thus all non-fixed components contribute at most

```text
3d^3 V.                                             (8)
```

The cubic factor is deliberately loose; it avoids any assumption about how
many paths share a cut at which their individual maxima occur.

## 4. Fixed components

For a fixed node, the coefficient is

```text
f_i(L+p_i)-f_i(L+q_i).                              (9)
```

The tail is monotone, so (9) has a constant sign.  For every event with
`zeta in [-H,0]`, the interval of cuts on which its two shifted indicators
differ lies inside `[-B,H+B]` and has length `|p_i-q_i|`.  Therefore

```text
g mu_i([-H,0])
 <=integral_(-B)^(H+B)|f_i(L+p_i)-f_i(L+q_i)| dL.  (10)
```

Fixed outputs are distinct.  Summing (10), using total variation in (2),
and then `||sigma_L||_TV<=V` gives

```text
sum_(fixed i) mu_i([-H,0]) <=(H+2B)V/g.             (11)
```

Equations (8) and (11) prove (5).

## 5. The event-measure core is never empty

If the `mu_i` decompose the order-resolution event measure of a normalized
Schmidt density `rho`, put `t=exp(-H)`.  Summing over the order atoms gives

```text
M_core=Tr[W_t(rho)-W_1(rho)].                       (12)
```

For every eigenvalue `0<lambda<=1`,

```text
lambda/(t+lambda)-lambda/(1+lambda)
 >=lambda(1-t)/[2(1+t)].                            (13)
```

Since `Tr rho=1`,

```text
M_core >=(1-exp(-H))/[2(1+exp(-H))].                (14)
```

Thus a normalized finite-rank event measure cannot make both pushed skew
flows uniformly close unless it pays a path endpoint or a fixed-point
vertical translation.

## 6. Remaining typed gate

Sprint 1253 supplies the fixed-point gap, and Sprint 1254 supplies a
canonical common carrier.  To obtain the Bell deficit bound, the joint
carrier must now be coarsened in the two order coordinates so that:

1. off-diagonal contact mass is charged by (13) of Sprint 1254;
2. both response actions descend to decreasing injections on the same finite
   coarse support; and
3. `V` is bounded above by the response debts with the regularized
   `t^(-1/2)` stability cost.

No fibre-local response estimate is needed in (5), but this final coarse
descent has not yet been proved.

