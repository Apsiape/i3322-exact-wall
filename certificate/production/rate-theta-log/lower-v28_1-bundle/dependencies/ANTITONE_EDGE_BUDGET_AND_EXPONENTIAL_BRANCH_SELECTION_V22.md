# V27 SUPERSESSION HEADER — HISTORICAL DEPENDENCY ONLY

**Not load-bearing for the v27 raw-cell converse.** Any occurrence below of `N <= d` derived from a component/rank-cost ledger belongs to the historical v22 route. The v27 proof does **not** use that inference. It uses instead the elementary local-dimension facts `m_X <= d` and `m_U <= d` for occupied marginal spectral cells, the raw-cell four-parity edge budget, and the v27 reflection-equivariant Borel cell convention. `TOP_D_SIMULTANEOUS_MONOTONE_CLUSTERING_V23.md` remains supplied only for provenance of the earlier correction history.

---
# Antitone Edge Budget and Exponential Branch Selection — v22

**Date:** 2026-08-06  
**Status:** exact abstract theorem.  
**Purpose:** replace the old repeated `largest branch` loss `d^{-O(d)}` by a single exponential loss using the global edge budget of ordered antitone response supports.

---

## 1. Ordered antitone response supports

Let

\[
L=\{1,\dots,m\},\qquad R=\{1,\dots,n\}
\]

with their natural orders. A bipartite support

\[
E\subseteq L\times R
\]

is **antitone** when for any two edges \((i,j),(i',j')\in E\),

\[
i<i'\quad\Longrightarrow\quad j\ge j'.
\tag{1.1}
\]

No degree-one or matching hypothesis is imposed.

### Theorem 1.1 — Antitone edge budget

Every antitone support satisfies

\[
\boxed{|E|\le m+n-1.}
\tag{1.2}
\]

### Proof

Order the distinct edges lexicographically by increasing left coordinate and,
within one left coordinate, by decreasing right coordinate:

\[
(i_1,j_1),\ldots,(i_M,j_M).
\]

Antitonicity implies

\[
i_1\le i_2\le\cdots\le i_M,
\qquad
j_1\ge j_2\ge\cdots\ge j_M.
\]

Because the edges are distinct, from one edge to the next at least one of the
integer coordinates changes strictly. Across the entire list the left
coordinate can increase at most \(m-1\) times in total integer variation and
the right coordinate can decrease at most \(n-1\) times in total integer
variation. Hence

\[
M-1\le(m-1)+(n-1),
\]

which is (1.2). ∎

The bound is sharp, e.g. one complete first row together with one fixed column
through the remaining rows gives \(m+n-1\) edges.

---

## 2. Two alternating response relations

Let the retained rank-costed cluster set contain \(N\) ordered vertices, with
positive integer rank costs \(r_v\) satisfying

\[
\sum_v r_v\le d.
\]

Therefore

\[
\boxed{N\le d.}
\tag{2.1}
\]

Let \(E_0,E_1\) be the two alternating response supports. Treat each as a
bipartite relation between two ordered copies of the retained cluster set and
assume each is antitone. Then Theorem 1.1 gives

\[
|E_p|\le2N-1,
\qquad p=0,1,
\]

and hence

\[
\boxed{|E_0|+|E_1|\le4N-2\le4d-2.}
\tag{2.2}
\]

This is the global branch budget.

---

## 3. Degree product on a simple alternating walk

Consider an alternating walk in the parity-expanded graph,

\[
(v_0,p_0),(v_1,p_1),\ldots,(v_L,p_L),
\qquad p_{k+1}=1-p_k,
\]

stopped at the first sink or immediately before the first repeated
parity-state. Let

\[
D_k\ge1
\]

be the outgoing degree of \((v_k,p_k)\) in the active relation \(E_{p_k}\).
Before stopping, the parity-states are distinct. Therefore their outgoing edge
sets are disjoint as sets of edges, and

\[
\boxed{
\sum_{k=0}^{L-1}D_k
\le |E_0|+|E_1|
\le4d-2.
}
\tag{3.1}
\]

Also

\[
L\le2N\le2d.
\tag{3.2}
\]

For every integer \(D\ge1\),

\[
D\le2^D.
\]

Thus

\[
\prod_{k=0}^{L-1}D_k
\le
2^{\sum_kD_k}
\le
2^{4d-2},
\]

so the repeated largest-branch square-root loss obeys

\[
\boxed{
\prod_{k=0}^{L-1}D_k^{-1/2}
\ge2^{-2d+1}.
}
\tag{3.3}
\]

The important point is qualitative but exact:

\[
\boxed{
\text{branch selection costs }e^{-O(d)},\text{ not }d^{-O(d)}.
}
\]

---

## 4. Largest-amplitude branch recurrence

At a parity-state \((v,p)\), suppose the localized response vector has
orthogonal destination components \(\{\zeta_{v\to w}\}_{w\in N_p(v)}\) and
satisfies

\[
\left(\sum_{w\in N_p(v)}\zeta_{v\to w}^2\right)^{1/2}
\ge a_v z_v-e_v,
\tag{4.1}
\]

with \(a_v>0\), \(e_v\ge0\). Choose a destination with largest component.
Then

\[
\boxed{
 z_{v_{k+1}}
\ge
\frac{a_{v_k}}{\sqrt{D_k}}z_{v_k}-e_{v_k}.
}
\tag{4.2}
\]

Indeed the largest component is at least the \(\ell^2\)-norm divided by
\(\sqrt{D_k}\), and replacing \(e_v/\sqrt{D_k}\) by the larger \(e_v\) only
weakens the inequality.

Assume on the retained response corridor

\[
0<\sigma\le a_v\le A<\infty.
\tag{4.3}
\]

The selected edge gains are

\[
g_k=\frac{a_{v_k}}{\sqrt{D_k}}.
\]

Using (3.2)--(3.3), for \(0<\sigma\le1\),

\[
\boxed{
G_L:=\prod_{k=0}^{L-1}g_k
\ge
\sigma^{2d}2^{-2d+1}.
}
\tag{4.4}
\]

If \(\sigma>1\), replace it by \(1\) in this lower bound.
The corresponding Green norm is at most exponential because

\[
g_k\le A,
\qquad L\le2d.
\tag{4.5}
\]

Thus both signal attenuation and error amplification are at worst exponential
in \(d\).

---

## 5. Branch-Selected Forest Theorem

Let \(\eta\ge0\) be a global paid-error parameter. Assume:

1. **rank-costed retained graph:** \(N\le d\);
2. **mass anchor:** some retained parity-state has
   \[
   z_0^2\ge c_a/d;
   \tag{5.1}
   \]
3. **antitone support:** both alternating response supports obey (1.1);
4. **response budget:**
   \[
   \sum_v e_v^2\le C_R\eta;
   \tag{5.2}
   \]
5. **gain bounds:** (4.3);
6. **sink service:** at every genuine sink reached by the selected walk,
   \[
   \delta z_{\rm sink}^2\le C_E\eta,
   \qquad\delta>0;
   \tag{5.3}
   \]
7. **cycle service:** if the selected walk first repeats a parity-state, the
   resulting cycle anchor obeys
   \[
   z_{\rm cyc}^2\le C_C\eta.
   \tag{5.4}
   \]

Then there are constants \(c,C,K>0\), depending only on the fixed response
corridor and the service constants, such that

\[
\boxed{
\eta\ge c(1+d)^{-K}e^{-Cd}.
}
\tag{5.5}
\]

### Proof

Follow the largest-amplitude outgoing branch until a sink or first repeated
parity-state. The walk has length at most \(2d\). Iterating (4.2) gives

\[
z_L\ge G_Lz_0-\mathcal G_L\sqrt{C_R\eta},
\tag{5.6}
\]

where \(\mathcal G_L\le \sqrt{2d}\max(1,A)^{2d}\) is an admissible exponential
Green bound.

If

\[
\mathcal G_L\sqrt{C_R\eta}\ge\frac12G_Lz_0,
\]

then (4.4), (5.1), and the exponential Green bound already give (5.5).
Otherwise

\[
z_L\ge\frac12G_Lz_0,
\]

so

\[
z_L^2\ge
\frac{c_a}{4d}
\sigma^{4d}2^{-4d+2}.
\tag{5.7}
\]

If the walk ends at a sink, (5.3) and (5.7) give (5.5).
If it closes a cycle, the repeated parity-state has an amplitude bounded below
by the same iteration up to another fixed exponential factor; (5.4) gives
(5.5). ∎

---

## 6. Consequence for a fractional paid budget

The shifted-grid clustering route naturally produces paid deletions and bridge
errors of size

\[
\eta\le C_\alpha\varepsilon^\alpha
\]

for some fixed \(\alpha>0\); in the existing coarse I3322 theorem one may take
\(\alpha=1/8\).

If (5.5) holds, then

\[
C_\alpha\varepsilon^\alpha
\ge c(1+d)^{-K}e^{-Cd},
\]

and therefore

\[
\boxed{
\varepsilon
\ge
c'(1+d)^{-K'}e^{-C'd}.
}
\tag{6.1}
\]

Thus an \(O(\varepsilon^{1/8})\) clustering tax does **not** obstruct the
logarithmic complexity class. The only thing that did was the old
\(d^{-O(d)}\) repeated-branch loss, and Theorem 1.1 removes it.

---

## 7. I3322 interface

The already-established shifted-grid rank-costed clustering supplies:

- ordered paired blocks;
- total rank cost at most \(d\);
- retained mass \(1-O(\varepsilon^{1/8})\);
- exact antitone support for each response relation;
- response partition energy;
- endpoint service;
- large-scalar-cycle payment by the inversion budget.

Therefore the old structural demand for a **rank-preserving degree-two partial
matching decomposition** is stronger than necessary.

The only remaining load-bearing I3322 receipt for this route is the
**scalar-small cycle service** (5.4), with the current operator typing of its
return mismatch and robust quarter-ceiling Bell gap.

### New first failed line

\[
\boxed{
\text{scalar-small rounded response cycle}
\Longrightarrow
z_{\rm cyc}^2\le C\,\varepsilon^\alpha
}
\]

for one fixed \(\alpha>0\), using only current promoted response/quarter-ceiling
receipts.

Once that local cycle receipt is closed, (6.1) yields the exponential
finite-dimensional converse without C034 and without the v18 cross-marginal
packet-typing error.
