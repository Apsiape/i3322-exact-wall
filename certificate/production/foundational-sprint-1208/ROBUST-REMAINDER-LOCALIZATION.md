# Robust localization from the three I3322 certificate remainders

Status: **representation-free first stability theorem; orbit rounding and
dimension necessity remain open**

## Theorem

Let a projective tensor-product or commuting strategy have unit vector `psi`
and Bell deficit

```text
epsilon = q_* - <psi,B psi>.
```

For the three positive remainders of Sprint 1197,

```text
epsilon = epsilon_0+epsilon_A+epsilon_B,
epsilon_i=<psi,R_i psi> >= 0.                         (1)
```

Put

```text
K_A=J_A S_B,      L_A=sqrt(A(X)),
K_B=S_A J_B,      L_B=sqrt(B(U)).                     (2)
```

Cross-party commutation makes `K_A,K_B` self-adjoint involutions. The sign
relations and the exact product laws give

```text
R_A=L_A(I-K_A)L_A,
R_B=L_B(I-K_B)L_B.                                   (3)
```

Consequently

```text
||(I-K_A)L_A psi||^2 = 2 epsilon_A,
||(I-K_B)L_B psi||^2 = 2 epsilon_B.                  (4)
```

This is an exact quantitative statement for every representation; it uses no
Schmidt alignment, discrete spectrum, or wall coordinates.

For `eta>0`, define the sign-symmetric good projections

```text
E_A(eta)=1_{min(A(X),A(-X)) >= eta},
E_B(eta)=1_{min(B(U),B(-U)) >= eta}.                 (5)
```

They commute with the corresponding sign flip and Bellman weight. On their
ranges define

```text
T_A=L_A^{-1}K_A L_A,
T_B=L_B^{-1}K_B L_B.                                 (6)
```

Then

```text
||E_A(eta)(I-T_A)psi|| <= sqrt(2 epsilon_A/eta),
||E_B(eta)(I-T_B)psi|| <= sqrt(2 epsilon_B/eta).      (7)
```

Thus the two exact equality transports are quantitatively stable wherever
their weights are not degenerate.

## Transport localization

Because `X` and `U` commute, `R_0=r_0(X,U)` has a joint spectral measure
`mu_psi`, where

```text
r_0(x,u)=q_*-d(x,u)-A(x)-B(u) >= 0.                  (8)
```

Let `Z={r_0=0}` be the certified double-contact set. For any closed
`D subset [-1,1]^2` disjoint from `Z`, compactness and strict contact give

```text
kappa(D)=min_D r_0 > 0,
mu_psi(D) <= epsilon_0/kappa(D).                      (9)
```

In particular, the equality proof shows that `Z` is compactly contained in
the nondegenerate response region. Hence some `eta>0` makes the bad-weight
set

```text
D_eta={min(A(x),A(-x),B(u),B(-u)) < eta}
```

disjoint from `Z`, and

```text
mu_psi(D_eta) <= epsilon_0/kappa_eta.                (10)
```

Equations (7) and (10) are the promised first implication:

```text
small Bell deficit
  => most state mass lies near the double-contact graph
  => both weighted response reflections have small norm defect there.      (11)
```

## Proof of the local identities

The sign flip satisfies `K_A f(X)=f(-X)K_A`. Therefore

```text
L_A K_A L_A
 = sqrt(A(X)A(-X)) K_A
 = b(X)K_A,
```

which is the off-diagonal response term in `R_A`; this proves (3). Since
`K_A^2=I`, one has `(I-K_A)^2=2(I-K_A)`, proving (4). On the symmetric good
projection, `L_A^{-1}` has norm at most `eta^{-1/2}` and the projection
commutes with `K_A`; applying `L_A^{-1}` to (4) gives (7). The Bob proof is
identical. Equation (9) is Markov's inequality applied to the nonnegative
joint spectral function (8).

## Exact remaining wall

This theorem does **not** prove that the two approximate reflections act on
one finite ordered set. Continuous spectral mass, multiplicity, and
noncommuting third responses can still disperse the error. The next theorem
must extract, from (11), either:

1. a finite approximate orbit whose two reflections compose to an oriented
   translation, or
2. a direct finite-rank trace/index inequality that charges the mismatch
   without discretizing the orbit.

Only then can the sharp weighted-path endpoint lemma convert rank `d` into a
lower bound on `q_*-Q_d`.
