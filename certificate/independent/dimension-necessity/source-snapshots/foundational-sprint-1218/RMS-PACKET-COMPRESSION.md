# Exact RMS weights remove the cell-oscillation modulus

Status: **exact grouped-packet theorem; common packet construction and final
assembly remain open**

## 1. RMS compression theorem

Let `G_i` be mutually orthogonal packet projections, let `v_i=G_i psi`, and
let `L>=0` commute with every `G_i`. For `v_i!=0`, define

```text
z_i=||v_i||,
p_i=||L v_i||/z_i.                                    (1)
```

If the spectrum of `L^2` on `G_i H` lies in `[ell,u]`, then

```text
ell<=p_i^2=<v_i,L^2v_i>/<v_i,v_i><=u.                (2)
```

Suppose `K` is unitary and a proposed packet transport has error

```text
e_i=||K L v_i-L v_(alpha i)||.                       (3)
```

Unitary invariance of norm and the reverse triangle inequality give

```text
|p_i z_i-p_(alpha i)z_(alpha i)|
 =|||L v_i||-||L v_(alpha i)|||
 <=e_i.                                               (4)
```

Thus the exact scalar amplitude residuals required by Sprint 1214 follow
without replacing `L` by a cell representative. There is no oscillation,
mesh, number-of-cells, dimension, or multiplicity factor.

## 2. I3322 constants

Sprint 1216 certifies on the good contact square

```text
1/12<A(X),B(U)<13/10.                                (5)
```

Since `L_A^2=A(X)` and `L_B^2=B(U)`, every nonzero grouped packet has

```text
1/12<p_i^2,q_i^2<13/10.                              (6)
```

The recurrence-energy constants from Sprint 1216 therefore remain

```text
K_A=24,
K_B=1872/5.                                          (7)
```

For point packets exactly on the contact graph, the reflection-ratio identity
gives the sharper amplitude cocycle bound `13/2`. A grouped packet need not
retain that pointwise correlation. From (6), the safe effective bound is

```text
c_i
 <=(p_max/p_min)(q_max/q_min)
 <=(sqrt((13/10)/(1/12)))^2
 =78/5.                                               (8)
```

This distinction is mandatory. `13/2` belongs to pointwise contact ancestry;
`78/5` belongs to the robust grouped-packet theorem.

## 3. Consequence

Sprint 1215 now yields, for total good packet mass `W` on a local
`d`-dimensional carrier,

```text
endpoint energy+recurrence energy
 >=W/[d^2(78/5)^(2(d-1))].                           (9)
```

This constant is intentionally crude but completely explicit and does not
depend on a partition mesh. The next proof obligation is only to construct
the common matched packets from the two contact residual bounds while
recombining repeated local blocks. The inactive strip must also be discarded
by its positive compact gap.

## Scope

The theorem removes one analytic modulus; it does not itself prove that the
Alice and Bob packet families can be chosen identically with at most `d`
nonzero sites. That common-packet/recombination step is the remaining
structural assembly gate.
