# Schmidt correspondence and regularized-volume boundary law

Status: **proved operator-valued stability theorem; the final contact-to-rank
inequality remains open**

## 1. The branch-resolved response equations

Let a pure bipartite state be represented by its coefficient operator
`D : conjugate(H_B) -> H_A`, so that

```text
(M tensor N) psi  <->  M D N^T.                       (1)
```

Use the notation of Sprint 1208:

```text
K_A=J_A tensor S_B,       L_A=sqrt(A(X)),
K_B=S_A tensor J_B,       L_B=sqrt(B(U)).              (2)
```

The exact response defects become

```text
||(I-K_A)L_A psi||
 = ||L_A D-J_A L_A D S_B^T||_HS,

||(I-K_B)L_B psi||
 = ||D L_B^T-S_A D L_B^T J_B^T||_HS.                 (3)
```

Because `J_A f(X)=f(-X)J_A` and
`J_B f(U)=f(-U)J_B`, put

```text
C_A=L_A(-X)^(-1)L_A(X),
C_B=L_B(-U)^(-1)L_B(U).                               (4)
```

On a sign-symmetric response region where
`L_A(-X),L_B(-U)>=sqrt(eta)`, equation (3) gives

```text
||C_A D-J_A D S_B^T||_HS <= sqrt(2 epsilon_A/eta),
||D C_B^T-S_A D J_B^T||_HS <= sqrt(2 epsilon_B/eta).  (5)
```

At equality these are not scalar mass relations. They are two-sided
equivalences of the complete Schmidt operator. They retain spectral
multiplicity and the relative placement of every branch.

## 2. Complete singular-spectrum control

Left and right multiplication by a unitary preserves all singular values.
Mirsky's inequality applied to (5) therefore yields

```text
||s(C_A D)-s(D)||_2 <= sqrt(2 epsilon_A/eta),
||s(D C_B^T)-s(D)||_2 <= sqrt(2 epsilon_B/eta),        (6)
```

where `s(M)` is the decreasing singular-value vector, padded with zeros.
This strictly refines a Frobenius-norm or packet-mass balance: equal total
mass does not imply equal singular spectra.

For an exact finite full-rank correspondence, taking the top exterior power
recovers the ordinary volume balance

```text
|det C_A|=|det C_B|=1.                                (7)
```

The ordinary determinant is not robust when the smallest Schmidt coefficient
is tiny. That is the expected regime of the wall truncations, so (7) is an
exact classifier but not yet a quantitative theorem.

## 3. Soft volume

For an `m x n` matrix `M`, let `r=min(m,n)` and define

```text
Phi_t(M)=sum_(j=1)^r log(t+s_j(M)^2),        t>0.      (8)
```

Along a differentiable matrix path, the Hilbert--Schmidt norm of the gradient
is at most `sqrt(r/t)`, because

```text
2s/(t+s^2) <= 1/sqrt(t).                              (9)
```

Integrating on the line segment from `M` to `N` proves

```text
|Phi_t(M)-Phi_t(N)| <= sqrt(r/t) ||M-N||_HS.          (10)
```

Combining (5) and (10) gives the two regularized modular balances

```text
|Phi_t(C_A D)-Phi_t(D)| <= sqrt(2r epsilon_A/(t eta)),
|Phi_t(D C_B^T)-Phi_t(D)| <= sqrt(2r epsilon_B/(t eta)). (11)
```

These estimates tolerate arbitrarily small Schmidt coefficients. Their only
dimension dependence is the explicit `sqrt(r)` volume factor.

## 4. Exact boundary telescope

Let

```text
D=diag(lambda_0,...,lambda_(r-1)),
T(D)=diag(lambda_1,...,lambda_(r-1),0).               (12)
```

Every interior singular value cancels in (8), leaving

```text
Phi_t(T(D))-Phi_t(D)
 = log(t)-log(t+lambda_0^2).                          (13)
```

Thus regularized volume reads a finite translation as a boundary defect. It
does not need a spectral grid, a packet ancestry relation, or a choice of
near-fixed sector. On a cyclic finite translation the same expression is
zero because the missing endpoint is reinserted. This is the correct algebraic
dichotomy behind the exact proof: an infinite nonclosing translation may
carry a nontrivial amplitude cocycle, whereas every finite closure must pay
for the return.

## 5. What changed

The failed packet campaign tried to convert the two response equations into
scalar flows before proving that their targets were the same. Equations
(3)--(11) avoid that conversion. The object transported is the Schmidt
operator itself; unitary branch mixing is part of the correspondence rather
than an unpriced error.

This does not yet prove a universal lower bound on `q_*-Q_d`. The remaining
gate is now sharply typed:

```text
Bellman contact + two soft-volume balances
    => a finite-rank boundary term bounded below.      (14)
```

If (14) is false, the operator-rigidity route dies. If it is true, it supplies
the missing converse without reconstructing a scalar orbit.
