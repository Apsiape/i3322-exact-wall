# Pre-registration: Bellman--Hellinger flow duality

## Wager

The globally normalized Bellman problem is not fundamentally a characteristic
orbit problem. It is a convex primal whose dual variable is a positive edge
measure. Local Bellman contact selects the support of that measure; global
amplitude normalization is the separate KKT condition balancing its incoming
and outgoing marginals.

This would explain why the historical local shooting geometry could be exact
while its global amplitude weld failed.

## Finite theorem target

For a finite set `I`, real costs `d_ij`, and `b_i>0`, define

```text
P = inf_(g_i>0) max_(i,j) [d_ij + b_i^2/g_i + g_j].
```

For a probability matrix `pi_ij`, let

```text
r_i = sum_j pi_ij,       s_i = sum_j pi_ji.
```

Prove

```text
P = sup_pi [sum_ij pi_ij d_ij + 2 sum_i b_i sqrt(r_i s_i)].
```

The proof must identify the square

```text
r_i b_i^2/g_i + s_i g_i - 2b_i sqrt(r_i s_i)
 = (b_i sqrt(r_i/g_i)-sqrt(s_i g_i))^2
```

and justify the minimax exchange, including a controlled limit for zero
marginals and the endpoint case `b_i=0` used by I3322.

## Registered consequences to test

1. **KKT balance:** on every positive marginal,
   `s_i = r_i b_i^2/g_i^2`.
2. **Contact support:** positive `pi_ij` occurs only where the primal maximum
   is attained.
3. **Path embedding:** for an open aligned Jacobi path with positive state
   amplitudes, the associated edge measure's dual objective equals its
   normalized Rayleigh quotient exactly; endpoint terms vanish because
   `b(+/-1)=0`.
4. **Failure diagnosis:** contact support alone does not imply KKT balance.
   Construct an exact counterfixture with perfect contact and nonzero marginal
   balance defect.
5. **No overclaim:** do not assert that every Hellinger flow is quantum
   realizable, that the continuum minimax follows automatically, or that the
   historical `q_*` is restored.

## Decision

- If the theorem or path embedding fails, abandon this architecture.
- If both land, the next campaign is the continuum limit and the realizability
  classification of extremal flows.
- If arbitrary extremal flows require branching that the I3322 block family
  cannot realize, record the resulting primal/quantum gap rather than naming
  equality.
