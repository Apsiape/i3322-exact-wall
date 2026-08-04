# Sprint 1240 pre-registration -- Schmidt correspondence and soft volume

Date: 2026-08-04

## Target

Re-enter the quantitative-dimension problem before scalar packetization.
Represent a pure bipartite state by its Schmidt coefficient operator `D` and
translate the two response remainders into two-sided matrix correspondences.

The registered candidate invariant is the regularized volume

```text
Phi_t(D)=log det(t I + D^* D),       t>0.
```

Unlike the ordinary determinant, `Phi_t` remains stable when `D` has very
small singular values. Unlike total packet mass, it retains the complete
singular-value multiset and hence the multiplicity data erased by the failed
scalar route.

## Registered predictions

1. Under the coefficient-matrix identification
   `(A tensor B) psi <-> A D B^T`, each response defect is exactly a weighted
   Hilbert--Schmidt matrix defect.
2. Removing the nondegenerate response weight gives approximate
   correspondences

   ```text
   J_A D S_B^T ~= C_A D,
   S_A D J_B^T ~= D C_B^T,
   ```

   where `C_A=L_A(-X)^(-1)L_A(X)` and
   `C_B=L_B(-U)^(-1)L_B(U)`.
3. Mirsky's inequality then controls the complete singular-value displacement
   with no block-count factor.
4. For `r=min(dim H_A,dim H_B)`,

   ```text
   |Phi_t(M)-Phi_t(N)| <= sqrt(r/t) ||M-N||_HS.
   ```

5. On a finite one-step shift, the difference of `Phi_t` values telescopes
   exactly to the omitted endpoint. Thus the invariant sees boundary
   nonclosure rather than an arbitrarily chosen packet partition.

## Failure conditions

- either coefficient-matrix identity has the wrong operator order;
- the response weight cannot be removed without an unowned inverse;
- the singular-value estimate needs a dimension-dependent block count beyond
  the explicit rank factor in the soft-volume bound;
- the soft-volume Lipschitz constant is false;
- or the finite shift retains an interior term.

## Claim boundary

This sprint is an operator-valued bridge, not a dimension lower bound. A
future theorem must still combine the two soft-volume balances with Bellman
contact and show that finite rank must pay a nonzero boundary charge.
