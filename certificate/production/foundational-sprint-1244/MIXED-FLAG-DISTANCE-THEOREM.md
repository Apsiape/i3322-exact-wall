# Mixed flag distance is weighted transport distance

Status: **exact finite theorem and stochastic extension**

## 1. Permutation theorem

Let `E_k` project onto the first `k` points of `{0,...,n-1}`. For
permutations `p,q`, put

```text
E_k^p=P E_k P^T,       E_k^q=Q E_k Q^T.              (1)
```

Let `W=diag(w_0,...,w_(n-1))` with every `w_j>0`. Then

```text
D_W(p,q)
 :=sum_(k=1)^(n-1) Tr[W |E_k^p-E_k^q|]
 =sum_j w_j |p^(-1)(j)-q^(-1)(j)|.                  (2)
```

Indeed, for a fixed target point `j`, membership in `E_k^p` turns on exactly
when `k>p^(-1)(j)`. The two step functions disagree at precisely the integer
thresholds between `p^(-1)(j)` and `q^(-1)(j)`.

Consequently `D_W(p,q)=0` iff `p=q`. If `p!=q`, at least two target points
move and

```text
D_W(p,q)>=2 min_j w_j.                              (3)
```

In particular, if both maps are decreasing bijections, they are the same
reversal and (2) vanishes. Equation (2) is the quantitative form of the
finite-order lemma used in Sprint 1198.

## 2. Branch-mixing extension

Let `P,Q` now be row-stochastic kernels. For each target row `j`, let

```text
F_P(j,k)=sum_(i<k) P_(j,i),
F_Q(j,k)=sum_(i<k) Q_(j,i).                          (4)
```

Define

```text
D_W(P,Q)=sum_j w_j sum_(k=1)^(n-1)
                     |F_P(j,k)-F_Q(j,k)|.            (5)
```

On the ordered unit lattice, the inner sum is exactly the
Wasserstein-1 distance between row `j` of `P` and row `j` of `Q`. Thus

```text
D_W(P,Q)=sum_j w_j W_1(P_j,Q_j).                    (6)
```

This remains meaningful when a response unitary mixes multiplicity spaces:
the row gives the distribution of target order positions, and the cumulative
flag records that distribution without selecting a branch.

## 3. Relation to the Schmidt campaign

Choose the weights

```text
w_j(t)=s_j^2/(t+s_j^2),                              (7)
```

the eigenvalues of the regularized support from Sprint 1242. Then the mixed
distance ignores directions far below `sqrt(t)` continuously rather than
deleting them. The family over all `t>0` retains the full singular spectrum,
while the cumulative flags retain relative order.

This repairs both losses exposed so far:

- marginal volume retained multiplicity but forgot gluing;
- scalar packets retained local addresses but deleted complement branches.

The remaining analytic gate is to extract two response kernels from the
matrix correspondences and control (6) by the Bell deficit. No such estimate
is asserted here.
