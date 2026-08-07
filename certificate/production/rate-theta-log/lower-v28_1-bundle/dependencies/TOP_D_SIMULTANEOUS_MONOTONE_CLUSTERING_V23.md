# Top-d Simultaneous Monotone Clustering — v23

**Date:** 2026-08-06  
**Status:** repaired theorem; replaces the false rank-cost selection statement in the shifted-grid package.  
**Consumed sources:** `SHIFTED_GRID_RANK_COSTED_CLUSTERING_AND_COARSE_CONVERSE.md` §§1–6 only; Sprint-1221 matched-block theorem in `YM_STAGE2DJ_I3322_FINITE_RANK_EXIT_BRIDGE.md`.

## 1. What is retracted

The statement

\[
\sup_{\sum_{k\in J} r_k\le d}\sum_{k\in J}w_k
\ge \sum_k w_k-\|M-D\|_F^2
\]

is not a consequence of the matched-block theorem and is **retracted**. No v23 argument uses a rank-cost ledger \(\sum r_k\le d\).

The only finite-dimensional cardinality fact used below is the true top-\(d\) matched-block inequality.

## 2. Far-inversion deletion

Let \(M\) be the coefficient matrix of a normalized pure strategy of local dimension at most \(d\). For grid width \(0<\eta\le1\), the state-anchored inversion theorem gives

\[
\mathcal I\le 4\varepsilon.
\]

The shifted-grid weighted vertex-cover construction deletes far-inversion cells of total mass

\[
\beta_{\rm far}
\le 8\sqrt{\mathcal I}\,\eta^{-3}
\le 16\sqrt\varepsilon\,\eta^{-3}.
\tag{2.1}
\]

After this deletion the surviving near-conflict components \(C_1,\ldots,C_N\) are strictly ordered **simultaneously in both scalar coordinates**: after one global orientation,

\[
i<j,\quad (x,u)\in C_i,\ (x',u')\in C_j
\quad\Longrightarrow\quad
x<x',\quad u<u'.
\tag{2.2}
\]

This is the required simultaneous-pairing receipt. The label \(k\) is a joint component label; it is not an independently chosen Alice label later matched to an independently chosen Bob label.

For each component let \(E_k\) be its Alice \(X\)-support projection, \(F_k\) its Bob \(U\)-support projection, and

\[
D_k=F_kME_k^{\mathsf T},\qquad w_k=\|D_k\|_F^2.
\]

The blocks are mutually orthogonal on both sides and

\[
D=\sum_kD_k,\qquad
\|M-D\|_F^2=\beta_{\rm far},\qquad
\sum_k w_k=1-\beta_{\rm far}.
\tag{2.3}
\]

## 3. True top-d recovery

Order the block masses decreasingly:

\[
w_{(1)}\ge w_{(2)}\ge\cdots.
\]

Sprint 1221 gives

\[
\boxed{
\sum_{j>d}w_{(j)}\le \|M-D\|_F^2=\beta_{\rm far}.
}
\tag{3.1}
\]

Retain the \(d\) largest nonzero paired blocks. Call their index set \(J_d\). Then

\[
|J_d|\le d,
\tag{3.2}
\]

and

\[
\sum_{k\in J_d}w_k
=\sum_k w_k-\sum_{j>d}w_{(j)}
\ge 1-2\beta_{\rm far}.
\tag{3.3}
\]

Thus the total state mass discarded by the two operations—far-inversion removal and top-\(d\) paired-block selection—is at most

\[
\boxed{
\beta_{\rm tot}\le 2\beta_{\rm far}.
}
\tag{3.4}
\]

No packet rank is summed.

## 4. Exact exponent bookkeeping

Choose

\[
\eta=\varepsilon^{1/8},\qquad 0<\varepsilon\le1.
\]

Then (2.1) gives

\[
\beta_{\rm far}
\le16\varepsilon^{1/2}\varepsilon^{-3/8}
=16\varepsilon^{1/8},
\tag{4.1}
\]

and therefore

\[
\boxed{
\beta_{\rm tot}\le32\varepsilon^{1/8}.
}
\tag{4.2}
\]

The constant is independent of \(d\). Any later exponential-in-\(d\) inversion may use the elementary implication

\[
32\varepsilon^{1/8}\ge A(1+d)^{-K}e^{-Bd}
\]

\[
\Longrightarrow\quad
\boxed{
\varepsilon
\ge
\left(\frac A{32}\right)^8
(1+d)^{-8K}e^{-8Bd}.
}
\tag{4.3}
\]

This, not the tautology `expand(a**8)==a**8`, is the required root-taking guard.

## 5. Simultaneous pairing survives top-d selection

Because \(J_d\) is a subset of the already jointly ordered components, deleting the other components cannot alter the common ordering. Thus one and the same ordered label set indexes:

- retained Alice \(X\) packet supports \(E_k\);
- retained Bob \(U\) packet supports \(F_k\);
- paired coefficient blocks \(D_k\).

After scalar reflection, an Alice or Bob response support on these labels is antitone. There is no free label permutation between the two sides.

This is the v23 replacement for the false “rank-costed monotone clustering” claim.

## 6. Deleted selected blocks are serviced, not forgotten

When a top-\(d\) deletion removes a destination block, the destination-localized response identity gives

\[
\|P_jW\psi\|
\le
A_{\max}\|P_j\psi\|+\|P_jr_A\|,
\]

and analogously for Bob. Summing over deleted destination blocks charges their response leakage to the once-global deletion mass plus the response residual. Thus top-\(d\) mass deletion creates paid graph sinks; it is not silently erased.

## 7. Claim boundary

**Proved/repaired here:**

1. simultaneous joint ordering of the retained components;
2. true top-\(d\) recovery with \(N\le d\);
3. retained paired mass \(\ge1-2\beta_{\rm far}\);
4. \(\beta_{\rm tot}\le32\varepsilon^{1/8}\);
5. dimension-independent exponent \(1/8\);
6. preservation of one common label order after selection.

**Retracted:** every use of \(\sum r_v\le d\) as a selection theorem.
