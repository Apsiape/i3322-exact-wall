# The I3322 wall is spatially attained

Status: analytic consequence of the certified bi-infinite wall plus an
explicit infinite alternating-block realization.

## Theorem

In the standard binary `3 x 3` Bell scenario, there is a normal vector-state
correlation

```text
p_* in C_qs(3,3;2,2)
```

whose canonical I3322 value is `q_*`. No finite-dimensional tensor-product
correlation has this value. Consequently

```text
C_q(3,3;2,2) != C_qs(3,3;2,2).
```

Together with Sprint 1205, this is minimal in the coordinatewise ordering of
bipartite binary input counts: if either party has at most two binary inputs,
`C_q=C_qs` and the common set is compact.

## 1. Certified input

Sprint 1195 constructs one bi-infinite cosine profile

```text
c=(c_j)_(j in Z),       -1 < c_j < 1,
```

and a positive geometrically decaying vector `lambda in ell^2(Z)` satisfying

```text
H(c) lambda = q_* lambda.                         (1)
```

After normalization, `sum_j lambda_j^2=1`. The bounded Jacobi operator is

```text
H_jj       = d(c_j,c_(j+1)),
H_(j-1),j  = sqrt(1-c_j^2)/2,

d(x,y)=xy+(x-y)/2-1.                              (2)
```

The geometric decay and equation (1) are theorem statements in the certified
aligned-wall package, not extrapolations from the finite numerical ladder.

## 2. Infinite measurement operators

For `t in [-1,1]`, put `s=sqrt(1-t^2)` and define

```text
P_A^pm(t) = (1/2) [[1-t,  pm s],
                   [pm s, 1+t]],

P_B^pm(t) = (1/2) [[1+t,  pm s],
                   [pm s, 1-t]],

R         = (1/2) [[1,1],[1,1]].                  (3)
```

Every matrix in (3) is a rank-one orthogonal projection.

Let both local Hilbert spaces be `ell^2(Z)` with basis `(e_j)`. Partition the
integer line into the two alternating perfect matchings

```text
E_A = {(2k-1,2k): k in Z},
E_B = {(2k,2k+1): k in Z}.                         (4)
```

On every edge `(j-1,j)` in `E_A`, install

```text
A_1 = P_A^-(c_j),   A_2 = P_A^+(c_j),   B_3 = R.
```

On every edge `(j-1,j)` in `E_B`, install

```text
B_1 = P_B^-(c_j),   B_2 = P_B^+(c_j),   A_3 = R.
```

Thus each of the six measurements is an orthogonal direct sum of rank-one
projections. They are bounded projections on `ell^2(Z)`.

## 3. Normal spatial state

Define

```text
|psi_*> = sum_(j in Z) lambda_j |e_j,e_j>.         (5)
```

Because `lambda in ell^2` and is normalized, (5) converges in the Hilbert
tensor product and is a unit vector. Its state is normal. No ultraproduct,
singular functional, Banach limit, or commuting-only representation appears.

For the finite-band real matrices `M,N` used below,

```text
<psi_*|M tensor N|psi_*>
  = sum_(r,s) lambda_r lambda_s M_rs N_rs.          (6)
```

Here every measurement is two-banded. All diagonal sums are dominated by
`sum lambda_j^2`, and all neighbor sums are absolutely convergent by
Cauchy--Schwarz. Therefore the finite block identity passes to (5) without a
conditional-series or limit-exchange assumption.

## 4. Bell value

Expanding the canonical I3322 functional with (3)--(6) gives

```text
I3322(psi_*,A,B)
 = sum_j d(c_j,c_(j+1)) lambda_j^2
   + sum_j sqrt(1-c_j^2) lambda_(j-1) lambda_j
 = <lambda,H(c)lambda>.                            (7)
```

The first equality is the infinite version of the exact Pal--Vertesi-to-Jacobi
reduction. The second is (2). By (1) and normalization,

```text
I3322(psi_*,A,B)=q_*.                              (8)
```

This proves spatial attainment.

## 5. Separation and model location

The archived nonattainment theorem proves that no point of `C_q` has I3322
value `q_*`. The correlation constructed above belongs to `C_qs` and has that
value. Hence it lies in

```text
C_qs \ C_q.
```

The standard inclusion `C_qs subset C_qa=closure(C_q)` also places the point in
`C_qa`. Equivalently, the exposed face from Sprint 1205 has nonempty
intersection with `C_qs`.

## 6. What changed

The previous scope statement treated spatial attainment as open because the
lower construction was used only as a sequence of finite Rayleigh quotients.
That discarded a stronger certified input: the limiting carrier already has
an `ell^2` eigenvector. Once the alternating projector blocks are installed on
`ell^2(Z)`, the same object is a normal spatial strategy. No new numerical
constant or physical postulate is needed.

## Boundaries

- This does not prove that the maximizing correlation or exposed face is
  unique.
- It does not separate `C_qa` from `C_qc`.
- It does not give a quantitative dimension lower bound near `q_*`.
- Minimality is only for bipartite binary-output input counts.
- The theorem is standard operator-algebraic quantum information; it makes no
  broader foundational claim.
