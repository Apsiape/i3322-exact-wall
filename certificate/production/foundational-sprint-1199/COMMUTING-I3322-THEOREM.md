# Exact commuting-operator I3322 supremum

Status: **commuting-operator theorem, conditional on the validated Bellman
fixed point of Sprint 1195**

## Theorem

For the standard commuting-operator model of the I3322 Bell scenario,

```text
Q_commuting = q_*
            = 0.250875384513976536... +/- 4.9e-19.
```

No finite-dimensional commuting-operator representation attains this value.

## 1. The certificate is spatially agnostic

Let Alice's three projections and Bob's three projections act on one Hilbert
space, with every Alice projection commuting with every Bob projection. Put

```text
X=A1+A2-I,  Y=A2-A1,
U=B1+B2-I,  V=B2-B1.
```

The same algebra as Sprint 1197 gives

```text
X^2+Y^2=I,  {X,Y}=0,
U^2+V^2=I,  {U,V}=0,                               (1)
```

and

```text
B_I3322 = G(X,U)+Y(B3-I/2)+(A3-I/2)V,              (2)
G(X,U)=XU+X/2-U/2-I.
```

No tensor sign occurs in (1)--(2); cross-party commutation is sufficient.

Because `[X,U]=0`, the scalar Bellman transport inequality applies by joint
continuous functional calculus:

```text
R_0=alpha(X)+beta(U)-G(X,U)>=0.                     (3)
```

## 2. A commutant factorization replaces the fiber determinant

Write

```text
b(t)=sqrt(1-t^2)/2,
S_B=2B3-I,
Y=2b(X)J_A,                                        (4)
```

where `J_A` is the polar sign of `Y` on the interior support. It reverses the
`X` coordinate and commutes with every Bob operator. The endpoint kernel of
`b(X)` has `Y=0` and is handled by continuity.

The geometric potential from Sprint 1197 obeys

```text
A(X)A(-X)=b(X)^2.                                  (5)
```

Let `L_A=sqrt(A(X))`. Since
`J_A f(X)=f(-X)J_A` and `S_B` commutes with the complete Alice algebra,

```text
L_A J_A S_B L_A=b(X)J_A S_B=Y(B3-I/2).             (6)
```

Therefore the local response remainder has the exact factorization

```text
R_A=A(X)-Y(B3-I/2)
   =L_A(I-J_A S_B)L_A>=0.                           (7)
```

On the interior `J_A` and `S_B` are commuting self-adjoint contractions, so
`J_A S_B` is a self-adjoint contraction. The endpoint remainder is simply the
nonnegative diagonal term left when `Y=0`.

The identical construction with

```text
S_A=2A3-I,  V=2b(U)J_B,
B(U)B(-U)=b(U)^2
```

gives

```text
R_B=sqrt(B(U))(I-S_A J_B)sqrt(B(U))>=0.             (8)
```

This factorization proves directly that the tensor fibers in Sprint 1197
were a representation convenience, not a hypothesis of the inequality.

## 3. The commuting supremum

Adding (3), (7), and (8) gives exactly

```text
q_*I-B_I3322=R_0+R_A+R_B>=0.                        (9)
```

Thus the commuting-operator value is at most `q_*`. Tensor-product strategies
are commuting strategies, and the finite aligned tensor-product sequence from
Sprint 1195 approaches `q_*`. Hence the reverse inequality holds and the
commuting supremum is exactly `q_*`.

Binary projective measurements are the standard presentation of the
commuting correlation set used here. No separate general POVM-dilation claim
is needed for this theorem.

## 4. Finite-dimensional nonattainment also survives

The Sprint-1198 equality proof uses only:

1. a finite joint spectrum for the commuting pair `(X,U)`;
2. the one-to-one increasing zero graph of `R_0`;
3. the commuting involutions `J_A S_B` and `S_A J_B`;
4. equality in the two Bellman contacts and the local product laws.

All four are present in a finite-dimensional commuting representation. The
two response kernels again induce decreasing bijections of the same finite
ordered spectral support, hence the same reversal. The identical amplitude
calculation forces the value to be at most `1/4`, contradicting `q_*>1/4`.

Therefore no finite-dimensional commuting-operator strategy attains the
commuting supremum.

## Boundary

This theorem concerns the usual bipartite commuting-operator correlation
model. It does not claim that every commuting correlation is spatial, settle
Connes embedding, identify a laboratory implementation of the limiting wall,
or promote any corpus ontology. It strengthens the scope of one Bell
inequality certificate and its nonattainment theorem.
