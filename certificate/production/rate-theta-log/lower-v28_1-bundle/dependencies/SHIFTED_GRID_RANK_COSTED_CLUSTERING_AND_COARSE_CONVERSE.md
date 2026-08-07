# Shifted-Grid Rank-Costed Clustering and the Coarse Converse

**Date:** 2026-08-05  
**Status:** exact rank-costed clustering theorem and exact abstract branching
converse; current I3322 converse conditional on one robust return-payment
receipt and the current-\(S\) rigidity rebind.

---

# Part I — Shifted-grid clustering

## 1. Input

Let \(M\) be the coefficient matrix of a normalized pure state with

\[
\operatorname{rank}M\le d,
\qquad
\|M\|_F=1.
\]

Let \(X\) and \(U\) have finite spectra in \([-1,1]\). Write the orthogonal
spectral block decomposition

\[
M=\sum_{x,u}M_{u,x}.
\]

Put

\[
m_{u,x}=\|M_{u,x}\|_F^2.
\]

The total scalar mass is

\[
\sum_{x,u}m_{u,x}=1.
\]

Define the inversion energy

\[
\mathcal I
=
\sum_{(x,u),(x',u')}
m_{u,x}m_{u',x'}
\bigl[(x-x')(u-u')\bigr]_-.
\]

For an I3322 strategy with Bell deficit \(\varepsilon\), the
state-anchored Monge theorem gives

\[
\boxed{\mathcal I\le4\varepsilon.}
\]

---

## 2. Grid cells

Fix

\[
0<\eta\le1.
\]

Choose arbitrary shifts \(s_x,s_u\in[0,\eta)\) and partition each coordinate
axis into half-open intervals of width \(\eta\). There are at most

\[
K\le\frac4\eta
\]

intervals in either coordinate and therefore at most

\[
n\le\frac{16}{\eta^2}
\]

occupied grid cells.

Let \(m_v\) be the total state mass in cell \(v=(p,q)\).

---

## 3. Far inversion graph

Two occupied cells

\[
v=(p,q),
\qquad
w=(p',q')
\]

form a far inversion if

\[
(p-p')(q-q')<0,
\]

\[
|p-p'|\ge2,
\qquad
|q-q'|\ge2.
\]

Every pair of spectral points in those two cells is inverted with

\[
|x-x'|\ge\eta,
\qquad
|u-u'|\ge\eta.
\]

Hence

\[
\eta^2m_vm_w
\]

is paid by the inversion energy, and summing unordered far edges gives

\[
\boxed{
\sum_{\{v,w\}\in E_{\rm far}}m_vm_w
\le
\frac{\mathcal I}{2\eta^2}.
}
\]

---

## 4. Weighted vertex-cover lemma

### Lemma 4.1

For any finite graph with vertex weights \(m_v\ge0\), there is a vertex cover
\(B\) such that

\[
\boxed{
\sum_{v\in B}m_v
\le
\sqrt{
|E|
\sum_{\{v,w\}\in E}m_vm_w
}.
}
\]

### Proof

For every edge, choose an endpoint of smaller weight. The union of the chosen
endpoints is a vertex cover and has weight at most

\[
\sum_{\{v,w\}\in E}\min(m_v,m_w)
\le
\sum_{\{v,w\}\in E}\sqrt{m_vm_w}.
\]

Cauchy--Schwarz gives the claim.

Applying the lemma to the far inversion graph and using

\[
|E_{\rm far}|
\le
\frac{n^2}{2}
\le
\frac{128}{\eta^4}
\]

gives a cover of mass

\[
\boxed{
\beta
\le
8\sqrt{\mathcal I}\,\eta^{-3}.
}
\]

Delete those cells.

---

## 5. Near-conflict components

On the remaining cells, connect two cells whenever:

1. some pair of their points is order-inverted; or
2. they contain a common exact \(X\)-spectral value; or
3. they contain a common exact \(U\)-spectral value.

No remaining inversion can be far, because the far inversion graph has been
covered. Thus every inversion edge is local at the grid scale.

Let

\[
C_1,\ldots,C_N
\]

be the connected components of this near-conflict graph.

### Theorem 5.1 — Ordered-component theorem

After relabeling,

\[
\boxed{
C_1<C_2<\cdots<C_N
}
\]

strictly in both scalar coordinates: for \(i<j\), every point
\((x,u)\in C_i\) and \((x',u')\in C_j\) satisfies

\[
x<x',
\qquad
u<u'.
\]

### Proof

If two distinct components contained an inverted pair, the two cells would be
joined by a near-conflict edge. If they shared an exact \(x\) or \(u\) label,
they would also be joined.

Thus every cross-component pair is strictly comparable.

The orientation is constant across a connected component. Indeed, two
incomparable vertices cannot lie on opposite strict sides of a fixed
comparable point: if

\[
a<z<b
\]

coordinatewise, then \(a<b\), contradicting incomparability. Propagating along
a conflict path fixes the same side for the whole component. Repeating for
both components yields one consistent total order.

---

## 6. Paired matrix blocks

For each component \(C_k\), let \(E_k\) be the sum of all Alice \(X\)-spectral
projections whose labels occur in \(C_k\), and \(F_k\) the corresponding Bob
\(U\)-projection sum. Put

\[
D_k=F_kME_k^{\mathsf T}.
\]

Distinct components have disjoint left and right spectral supports. Moreover,
every retained nonzero block belongs to exactly one \(D_k\). Therefore

\[
D:=\sum_kD_k
\]

is precisely the coefficient matrix obtained by deleting the vertex-cover
cells, and

\[
\boxed{
\|M-D\|_F^2=\beta,
}
\]

\[
\boxed{
\sum_k\|D_k\|_F^2=1-\beta.
}
\]

The blocks \(D_k\) are mutually orthogonal on both sides.

---

## 7. Rank-cost recovery

Let

\[
r_k=\operatorname{rank}D_k,
\qquad
w_k=\|D_k\|_F^2.
\]

The matched-block rank theorem gives

\[
\boxed{
\sup_{\sum_{k\in J}r_k\le d}
\sum_{k\in J}w_k
\ge
\sum_kw_k-\|M-D\|_F^2.
}
\]

Hence there is a selected ordered family \(J\) with

\[
\sum_{k\in J}r_k\le d
\]

and retained mass

\[
\boxed{
\sum_{k\in J}w_k
\ge
1-2\beta.
}
\]

Combining with the cover estimate:

### Theorem 7.1 — Rank-Costed Monotone Clustering

For every \(\eta\in(0,1]\), there exists a strictly ordered family of paired
blocks with total rank cost at most \(d\) and mass at least

\[
\boxed{
1-16\sqrt{\mathcal I}\,\eta^{-3}.
}
\]

For I3322,

\[
\boxed{
\text{retained mass}
\ge
1-32\sqrt\varepsilon\,\eta^{-3}.
}
\]

Choosing

\[
\eta=\varepsilon^{1/8}
\]

gives

\[
\boxed{
\text{retained mass}
\ge
1-32\varepsilon^{1/8}.
}
\]

Thus the rank-costed clustering gate is closed.

The choice \(\eta=\varepsilon^{1/8}\) balances scalar clustering resolution
against removed mass. It is not claimed sharp.

---

# Part II — Response order after clustering

## 8. Antitone response support

Let \(K_A\) be any bounded operator satisfying

\[
K_AXK_A^{-1}=-X
\]

on the selected compact corridor. If the block from ordered component \(i\)
to ordered component \(j\) is nonzero, then some source label \(x\in C_i\)
is sent to \(-x\in C_j\).

Therefore:

### Lemma 8.1

The Alice response block relation is antitone:

\[
i<i',
\quad
i\stackrel A\longrightarrow j,
\quad
i'\stackrel A\longrightarrow j'
\quad\Longrightarrow\quad
j>j'.
\]

The Bob response relation is antitone for the same reason.

Consequently, every composition of one Alice and one Bob response is
order-preserving.

This support statement is exact and independent of the response error.

---

## 9. Transport-error scale

The response partition identities give total squared error \(O(\varepsilon)\)
on the full state.

Projecting away clustering mass \(\beta=O(\varepsilon^{1/8})\) changes every
bounded response vector by at most

\[
O(\sqrt\beta)
=
O(\varepsilon^{1/16}).
\]

Therefore the selected ordered packet family inherits normalized response
transport with total vector error

\[
\boxed{
\Delta
=
O(\varepsilon^{1/16}),
}
\]

provided the exact maximizing orbit is confined to a compact coefficient
corridor so the normalizing coefficients are bounded above and below.

That compact-corridor step is conditional on a current-\(S\) rebind of the
exact scalar-orbit rigidity theorem.

---

# Part III — A coarse branching converse

## 10. Abstract branching hypotheses

Let

\[
z_1,\ldots,z_N>0,
\qquad
N\le d,
\]

be amplitudes of ordered packets carrying

\[
\sum_{i=1}^Nz_i^2\ge m_0.
\]

Assume two decreasing partial response choices \(a,b\). They are obtained by
choosing, from each response flow, a destination with largest norm.

If the normalized total outgoing response has lower bound \(\sigma z_i\),
there are at most \(N\) destinations, so the chosen branch obeys

\[
z_{a(i)}
\ge
\frac{\sigma}{\sqrt N}z_i-e_i^A,
\]

\[
z_{b(i)}
\ge
\frac{\sigma}{\sqrt N}z_i-e_i^B.
\]

Assume

\[
\sum_i\left((e_i^A)^2+(e_i^B)^2\right)
\le
\Delta^2.
\]

The composition

\[
\tau=a\circ b
\]

is increasing wherever defined.

Assume also a terminal/return payment:

- if \(\tau\) becomes undefined at \(i\), then \(z_i\le H\Delta\);
- if \(\tau(i)=i\), then \(z_i\le H\Delta\).

The second line is the robust near-common-return payment still open for
current I3322.

---

## 11. Largest-branch path theorem

Choose \(i_0\) with

\[
z_{i_0}
\ge
\sqrt{\frac{m_0}{N}}.
\]

Iterate \(\tau\).

Because \(\tau\) is increasing on a finite ordered set, every periodic orbit is
fixed. Hence within at most \(N\) iterates, the path reaches either:

1. an undefined endpoint; or
2. a fixed point.

For one two-response step, put

\[
r=\frac{\sigma^2}{N}.
\]

The recurrence has the form

\[
z_{i_{k+1}}
\ge
rz_{i_k}-f_k,
\]

with

\[
\sum_kf_k^2
\le
C_\sigma\Delta^2.
\]

At the terminal point,

\[
z_{i_n}\le H\Delta.
\]

Iteration and Cauchy--Schwarz give

\[
r^n z_{i_0}
\le
C\Delta.
\]

Since \(n\le N\),

\[
\boxed{
\Delta
\ge
c
\left(\frac{\sigma^2}{N}\right)^N
\sqrt{\frac{m_0}{N}}.
}
\]

---

## 12. Conditional I3322 coarse converse

For the clustered I3322 packets,

\[
\Delta\le C_0\varepsilon^{1/16}.
\]

Therefore, under the compact-corridor and robust-return hypotheses,

\[
\varepsilon^{1/16}
\ge
c
\left(\frac{\sigma^2}{d}\right)^d
d^{-1/2}.
\]

Equivalently:

\[
\boxed{
S-S_d
\ge
c_1
\sigma^{32d}
d^{-16d-8}.
}
\]

The constants are not optimized.

This gives the first coarse dimension law:

\[
\boxed{
d
=
\Omega\left(
\frac{\log(1/\varepsilon)}
{\log\log(1/\varepsilon)}
\right).
}
\]

It is weaker than the desired logarithmic law, because largest-branch
selection pays a factor \(d^{-1/2}\) at every reflection.

A true shifted-matching or rank-one flow decomposition would remove that loss
and restore an exponential lower profile.

---

# Part IV — Exact remaining receipts

## 13. What is now closed

- restriction-free scalar inversion budget;
- shifted-grid far-inversion removal;
- exact ordered conflict-component clustering;
- matched-block restoration of the rank budget;
- mass retention \(1-O(\varepsilon^{1/8})\);
- antitone response support;
- the abstract largest-branch converse.

---

## 14. What remains for the coarse I3322 bound

### R1 — Current-\(S\) compact rigidity rebind

Rebind TT-030's exact scalar-orbit support and mass rigidity to the repaired
current-\(S\) certificate. This supplies:

\[
m_0>0,
\qquad
\sigma>0,
\]

and a compact symmetric coefficient corridor.

### R2 — Normalized response-flow inequality

Write the projected response partition identities in the clustered matrix
language and verify the branch inequalities with total error

\[
\Delta=O(\varepsilon^{1/16}).
\]

The support and error accounting are already established; this is an operator
typing audit.

### R3 — Robust fixed-cluster payment

Prove that an approximately closed selected response channel satisfies

\[
z_i\le H\Delta.
\]

This is the stable version of the Sprint-1198 common-return quarter ceiling.

R3 is the only new analytic payment principle. R1 is a dependency rebind and
R2 is a typing/normalization assembly.

---

## 15. Sharp converse boundary

Even after the coarse converse lands, the matching exponential profile remains
stronger.

To remove the factor \(d^{-d}\), one must replace largest-branch selection by
a rank-preserving decomposition of the antitone response flows into shifted
partial matchings or paths with a dimension-independent transport floor.

Thus:

\[
\boxed{
\begin{array}{c|c}
\text{largest branch}
&
e^{-O(d\log d)}
\\
\text{rank-preserving shifted flow}
&
e^{-O(d)}.
\end{array}
}
\]

---

## 16. Claim boundary

Proved here:

- Rank-Costed Monotone Clustering Theorem;
- exact antitone response-support theorem;
- abstract largest-branch path theorem;
- conditional \(e^{-O(d\log d)}\) converse formula.

Not yet proved:

- current I3322 R1–R3;
- an unconditional quantitative lower bound;
- the matching exponential exponent.
