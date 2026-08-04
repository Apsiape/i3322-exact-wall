# Bellman--Hellinger flow duality

## Result

The missing global object in the historical I3322 Bellman construction is not
a preferred characteristic orbit. It is a positive flow on the contact graph.
Bellman equality determines where that flow may live; amplitude normalization
is the independent marginal-balance equation that determines whether it can
live there consistently.

This distinction explains a formerly puzzling conjunction: the local Bellman
geometry could be exact while the proposed global amplitude recursion failed.

## Finite theorem

Let `I` be finite, let `d_ij` be real, and let `b_i > 0`. Define

```text
P = inf_(g_i>0) max_(i,j) (d_ij + b_i^2/g_i + g_j).
```

For a probability matrix `pi=(pi_ij)`, write

```text
r_i = sum_j pi_ij,        s_i = sum_j pi_ji.
```

Then

```text
P = max_pi [sum_ij pi_ij d_ij + 2 sum_i b_i sqrt(r_i s_i)].       (1)
```

The maximum is over all nonnegative matrices of total mass one. The formula
continues to `b_i >= 0` by a monotone limiting argument.

### Proof

Write the primal in epigraph form:

```text
minimize q
subject to d_ij + b_i^2/g_i + g_j <= q       for every i,j,
           g_i > 0.
```

It is a finite convex program. It is strictly feasible: choose any positive
`g`, then choose `q` strictly above all finitely many left-hand sides. Its
Lagrange multipliers are nonnegative numbers `pi_ij`. Infimizing over `q`
forces `sum_ij pi_ij=1`. The remaining Lagrangian is

```text
sum_ij pi_ij d_ij + sum_i (r_i b_i^2/g_i + s_i g_i).
```

For each coordinate,

```text
r_i b_i^2/g_i + s_i g_i - 2b_i sqrt(r_i s_i)
 = (b_i sqrt(r_i/g_i) - sqrt(s_i g_i))^2.                         (2)
```

Its infimum is therefore `2b_i sqrt(r_i s_i)`. This also holds when
one marginal is zero, by taking `g_i` to zero or infinity as appropriate.
Slater strong duality now gives (1). Compactness of the probability simplex
and continuity of its objective give attainment on the dual side.

For `b_i=0`, replace `b_i` by `b_i+epsilon`. The dual values converge
uniformly on the compact simplex. The primal values decrease to the original
value: the lower inequality is monotonicity, while evaluating at any fixed
positive `g` supplies the matching upper limit. Thus (1) survives at the
I3322 endpoints.

## The two independent optimality laws

At a primal-dual optimum, complementary slackness says

```text
pi_ij > 0  =>  d_ij + b_i^2/g_i + g_j = P.                       (3)
```

This is **contact support**. Where both marginals are positive, equality in
(2) separately says

```text
s_i = r_i b_i^2/g_i^2.                                           (4)
```

This is **flow balance**. Equation (3) does not imply (4). The exact verifier
contains a two-state counterexample in which every edge is in perfect contact,
yet a contact-supported unit flow violates both balance equations. A balanced
self-loop on the same contact graph attains the primal value exactly.

The historical shooting argument established local contact information and
then treated a particular amplitude rule as if it followed. The theorem shows
why that inference was invalid: support and balance are different KKT clauses.

## Exact weld to the aligned Jacobi strategies

Take an open profile

```text
c_0=1, c_1, ..., c_(n-1), c_n=-1
```

and positive amplitudes `lambda_0,...,lambda_(n-1)`. Put total squared norm
`S=sum_j lambda_j^2` and place flow

```text
pi_(c_j,c_(j+1)) = lambda_j^2/S
```

on the consecutive directed edges. Its row and column marginals at an
interior point are

```text
r(c_j)=lambda_j^2/S,       s(c_j)=lambda_(j-1)^2/S.
```

For I3322, `2b(c)=sqrt(1-c^2)`. Hence the Hellinger term at `c_j` is

```text
2b(c_j)sqrt(r(c_j)s(c_j))
 = sqrt(1-c_j^2) lambda_(j-1)lambda_j/S,
```

exactly the off-diagonal term of the normalized Jacobi Rayleigh quotient.
The cost integral gives its diagonal term. The unmatched endpoint marginals
contribute zero because `b(1)=b(-1)=0`. Therefore every finite aligned path is
literally a path-supported feasible point of the flow dual, with identical
objective value.

The exact guard reconstructs this identity over `Fraction` on a nontrivial
rational Pythagorean fixture; no floating approximation or square-root oracle
is used.

## What changed

The rigorous window remains

```text
0.25087519579012 < omega_tensor <= omega_commuting <= 0.250876384514.
```

This theorem does **not** close that window. It changes the architecture of the
remaining question:

- the Bellman upper problem is a convex flow problem;
- finite Jacobi lower strategies are path flows inside its dual;
- the equality question is whether an optimal Bellman flow can be represented,
  or approximated without loss, by the quantum-realizable path family;
- branching flow that cannot be unfolded into that family is now a precise
  candidate source of a tensor/commuting or relaxation gap.

## Claim boundary

This result does not establish that every dual flow is quantum realizable. It
does not justify the historical characteristic orbit, recover the retracted
amplitude recursion, prove a continuum minimax theorem, identify the exact
I3322 optimum, prove nonattainment, or separate tensor from commuting models.

The next decisive object is the optimizer's support-and-balance geometry, not
another unconstrained shooting orbit.
