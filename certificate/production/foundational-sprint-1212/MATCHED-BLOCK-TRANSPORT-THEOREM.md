# Hilbert-space debt induces packetwise transport

Status: **exact abstract bridge theorem; common weighted I3322 partition still
open**

## Theorem

Let

```text
I=sum_i E_i
```

be a finite orthogonal projection decomposition of a Hilbert space. Let
`G_i<=E_i` be projections, put `G=sum_i G_i`, and let `K` be unitary. Suppose
`alpha` is a permutation of the indices such that

```text
K E_i K*=E_{alpha(i)}.                                (1)
```

For every vector `w`, define

```text
delta=||Kw-w||,
gamma=||(I-G)w||,
D^2=sum_i ||K G_iw-G_{alpha(i)}w||^2.                (2)
```

Then

```text
D<=delta+2 gamma,                                     (3)
D^2<=3 delta^2+6 gamma^2.                             (4)
```

If `m_i=||G_iw||^2`, then

```text
sum_i |m_i-m_{alpha(i)}|
 <=2 ||Gw|| D
 <=2 ||Gw|| (delta+2 gamma).                         (5)
```

No rank, number of blocks, atomicity, or multiplicity factor appears.

## Proof

For each index, insert its coarse block:

```text
K G_iw-G_{alpha(i)}w
 =K(G_i-E_i)w
  +(K E_iw-E_{alpha(i)}w)
  +(E_{alpha(i)}-G_{alpha(i)})w.                     (6)
```

Across `i`, each of the three displayed families occupies mutually
orthogonal coarse target blocks. Their direct-sum norms are respectively

```text
gamma, delta, gamma.                                  (7)
```

For the middle family, (1) gives

```text
K E_iw-E_{alpha(i)}w=E_{alpha(i)}(Kw-w),              (8)
```

and permutation of the complete block family makes its squared norms sum to
`delta^2`. Minkowski's inequality in the direct sum proves (3).
The elementary inequality

```text
||a+b+c||^2<=3(||a||^2+||b||^2+||c||^2)
```

proves (4).

For (5), set `a_i=||G_iw||` and
`b_i=||G_{alpha(i)}w||`. The reverse triangle inequality gives

```text
|a_i-b_i|<=||K G_iw-G_{alpha(i)}w||.                 (9)
```

Therefore Cauchy--Schwarz yields

```text
sum_i |a_i^2-b_i^2|
 <=[sum_i(a_i+b_i)^2]^(1/2) D
 <=2||Gw||D.                                         (10)
```

This completes the proof.

## Application to the response remainders

For Alice, choose a finite sign-symmetric spectral partition `{I_i}` of the
`X` spectrum and set `E_i=1_{I_i}(X)`. The sign relation gives exactly

```text
K_A E_i K_A=1_{-I_i}(X).                             (11)
```

The analogous statement holds for Bob's `U` bins. Refine each coarse bin by
the unique thin contact cell meeting the increasing double-contact graph and
call the resulting joint projection `G_i`. Applied to

```text
w_A=E_A(eta)L_A psi,
w_B=E_B(eta)L_B psi,                                 (12)
```

the theorem turns the response debts into packetwise transport errors.
Sprint 1208 controls `delta`; its contact-tube estimate controls the discarded
mass `gamma` after allowing the oscillation of the bounded Bellman weights on
each cell.

This is stronger than the marginal statement of Sprint 1209. The objects
transported are Hilbert-space packets, not only scalar spectral mass, so
noncommutative multiplicity cannot create cross-bin cancellation.

## What remains

Alice transports `L_A psi`; Bob transports `L_B psi`. Their cell weights
differ by the Bellman cocycle. The remaining theorem must therefore:

1. build one finite adaptive partition closed to a chosen depth under the two
   contact reflections;
2. translate both packet systems to one cocycle-weighted flow;
3. decompose that flow into finite chains and approximate cycles; and
4. combine endpoint leakage with Sprint 1211's cycle margin.

The first two steps are now geometric and scalar-weighted. They are no longer
an unresolved multiplicity or interference problem.
