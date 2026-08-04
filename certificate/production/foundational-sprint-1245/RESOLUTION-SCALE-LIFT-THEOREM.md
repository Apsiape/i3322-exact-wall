# The response cocycle translates Schmidt resolution

Status: **exact operator lift of the amplitude cocycle**

Sprint 1246 subsequently removes the commutation hypothesis by replacing
scalar resolution `tI` with the exact operator-valued metric `tC^(-2)`.

## 1. Contact makes the Schmidt density decomposable

At exact Bellman contact, the coefficient operator has block support only on
the one-to-one graph `x=P(u)`:

```text
E_x D F_u^T=0 unless x=P(u).                         (1)
```

Consequently `rho_A=DD^*` commutes with `X`, and `rho_B=D^*D` commutes with
`U`. Every response multiplier `C_A=c_A(X)` or `C_B=c_B(U)` therefore
commutes with the corresponding Schmidt density.

## 2. Multipliers act by changing resolution

For

```text
W_A,t(D)=DD^*(tI+DD^*)^(-1),                         (2)
```

let `C>0` commute with `rho_A=DD^*`. Then

```text
W_A,t(CD)
 =C^2 rho_A(tI+C^2 rho_A)^(-1)
 =rho_A(t C^(-2)+rho_A)^(-1).                       (3)
```

On the spectral block where `C=c`,

```text
W_A,t(CD)=W_A,t/c^2(D).                              (4)
```

Thus, if `zeta=log t`, the response multiplier translates the resolution
coordinate by

```text
zeta -> zeta-2 log c.                               (5)
```

The analogous identity holds for right multiplication `DC_B^T` and the Bob
soft support.

## 3. Response covariance

If a two-sided response correspondence is exact,

```text
U D V=C D,                                          (6)
```

with `U,V` unitary, then the right unitary cancels from the left density:

```text
W_A,t(CD)=U W_A,t(D)U^*.                            (7)
```

Equations (4) and (7) say that the response transports the ordered Schmidt
flag while translating its resolution scale. This statement retains all
multiplicity spaces and requires no Schmidt-basis choice.

## 4. I3322 cocycle

The balanced response weights give

```text
c_A(x)^2=F(-x)/F(x),
c_B(u)^2=F(u)/F(-u).                                (8)
```

Along the two response maps, the composed scale multiplier is

```text
C(u)=F(u)F(-P(u))/[F(-u)F(P(u))],                   (9)
```

the mass cocycle already certified in Sprints 1210 and 1214. The previous
skew product is therefore not an artifact of packet amplitudes. It is the
action of the exact response correspondence on the canonical resolution
filtration `(W_t)_(t>0)`.

## 5. New finite-closure picture

At `t=0`, every nonzero Schmidt direction has soft weight one. Finite exact
closure then reduces to the unique reversal of the support flag, recovering
Sprint 1198. At `t>0`, a near-optimal finite strategy can evade closure only
by moving the mismatch into directions with `s_j^2<<t`. Repeated cocycle
translation drives those directions through logarithmic resolution layers.

This identifies the intended quantitative theorem:

```text
nontrivial order-and-scale drift for q_*>1/4
 + at most d Schmidt directions
 -> a boundary direction with weight at least exp(-O(d)).                (10)
```

Equation (10) is not proved here. The advance is that its scale coordinate,
transport law, and cocycle are now exact and representation-free at equality.
