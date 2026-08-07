# Critical Zero-Set Reduction for Theorem (N)

**Date:** 2026-08-05  
**Status:** Analytic reduction. Theorem (N) remains unpromoted.  
**Purpose:** Replace the overstrong requirement “the first Bellman contact is
globally unique” by the smaller equality-kernel requirement actually consumed
by the operator proof.

---

## 1. Terminal-pivot storage is an exact fixed point

Let \(q>S\), put

\[
\delta=q-S>0,
\]

and let \(g_q(j)\) be the infimum of terminal Schur pivots of all finite
histories ending at \(j\), as in Sprint 1295.

Define

\[
(T_qh)(j)
=
\inf_i\left[
q-d(i,j)-\frac{b(i)^2}{h(i)}
\right].
\]

Sprint 1295 proves

\[
g_q\le T_qg_q
\]

by extending histories.

### Theorem 1.1

\[
\boxed{g_q=T_qg_q.}
\]

### Proof

Take a finite history ending at \(j\).

If it has only one edge \(i\to j\), its terminal pivot is

\[
q-d(i,j)
\ge
q-d(i,j)-\frac{b(i)^2}{g_q(i)}
\ge
(T_qg_q)(j).
\]

If it has at least two edges, let \(p\) be the preceding pivot and let \(i\) be
the penultimate label. Since \(p\ge g_q(i)\) and

\[
p\longmapsto q-d(i,j)-\frac{b(i)^2}{p}
\]

is increasing,

\[
p_{\rm terminal}
\ge
q-d(i,j)-\frac{b(i)^2}{g_q(i)}
\ge
(T_qg_q)(j).
\]

Every terminal pivot ending at \(j\) is therefore at least
\((T_qg_q)(j)\). Taking the infimum gives

\[
g_q\ge T_qg_q.
\]

Together with the extension inequality, equality follows.

---

## 2. Concavity of the storage

For I3322,

\[
d(i,j)=ij+\frac{i-j}{2}-1
\]

is affine in \(j\).

Every terminal pivot ending at \(j\) has the form

\[
A_{\mathfrak h,i}(q)-d(i,j),
\]

and is therefore affine in \(j\). Hence

\[
\boxed{g_q\text{ is concave and continuous}.}
\]

This does not imply differentiability.

---

## 3. Sign of a storage kink

Let

\[
p_q(x)=\frac{b(x)^2}{g_q(x)}
\]

and define the first-contact intercept

\[
C_q(x)=q+1-\frac{x}{2}-p_q(x).
\]

Suppose \(g_q\) has one-sided derivatives at \(x_0\). Concavity gives

\[
g'_{q,+}(x_0)-g'_{q,-}(x_0)\le0.
\]

Since \(b^2\) is smooth,

\[
p'_{q,+}(x_0)-p'_{q,-}(x_0)
=
-\frac{b(x_0)^2}{g_q(x_0)^2}
\left(
g'_{q,+}(x_0)-g'_{q,-}(x_0)
\right)
\ge0.
\]

Therefore

\[
\boxed{
C'_{q,+}(x_0)-C'_{q,-}(x_0)\le0.
}
\]

A genuine storage kink produces a downward kink in the minimized intercept.
Such a point cannot be a local minimizer of

\[
C_q(x)+\left(\frac12-x\right)u
\]

for any \(u\).

Consequently an active seam is either smooth or inactive. The earlier claim
that every piecewise-linear storage knot automatically creates a predecessor
plateau had the sign reversed.

This fact does not by itself prove global contact uniqueness: separated smooth
pieces can still be joined by a lower convex-envelope chord.

---

## 4. Reflection-gluing defect theorem

Let a finite history ending at \(t\) have terminal pivot \(p\), and let a
second history ending at \(-t\) have terminal pivot \(r\).

Reflect and reverse the second history. The I3322 identities

\[
d(-y,-x)=d(x,y),
\qquad
b(-x)=b(x)
\]

make its Jacobi matrix the reversed original matrix.

Concatenate the first history with this reflected-reversed history. After
Schur-complementing every noncentral coordinate, the remaining two-dimensional
matrix is

\[
\begin{pmatrix}
p&-b(t)\\
-b(t)&r
\end{pmatrix}.
\]

Every finite path satisfies

\[
qI-J\ge\delta I.
\]

By the variational characterization of a Schur complement, the effective
matrix also satisfies

\[
\begin{pmatrix}
p&-b(t)\\
-b(t)&r
\end{pmatrix}
\ge
\delta I.
\]

Therefore

\[
(p-\delta)(r-\delta)\ge b(t)^2.
\]

Taking independent infima over histories ending at \(t\) and \(-t\) gives:

### Theorem 4.1

\[
\boxed{
\bigl(g_q(t)-\delta\bigr)
\bigl(g_q(-t)-\delta\bigr)
\ge
b(t)^2.
}
\]

In particular,

\[
g_q(t)g_q(-t)>b(t)^2
\]

at every interior point for \(q>S\).

For any uniform limiting storage \(g\) along \(q\downarrow S\),

\[
\boxed{
g(t)g(-t)\ge b(t)^2.
}
\]

Define

\[
K(t)=\frac{g(t)g(-t)}{b(t)^2}
\]

on the interior. Then

\[
\boxed{K(t)\ge1.}
\]

This proves analytically the inequality previously seen only in the critical
scouts.

---

## 5. Full transport remainder

Set

\[
p(x)=\frac{b(x)^2}{g(x)},
\]

\[
A(x)=\sqrt{p(x)g(-x)},
\]

\[
B(u)=\sqrt{g(u)p(-u)}=A(-u),
\]

and

\[
h(x,u)=S-d(x,u).
\]

Bellman feasibility gives

\[
p(x)+g(u)\le h(x,u),
\]

and reflection gives

\[
g(-x)+p(-u)\le h(x,u).
\]

Cauchy--Schwarz gives

\[
A(x)+B(u)
\le
\sqrt{
\bigl(p(x)+g(u)\bigr)
\bigl(g(-x)+p(-u)\bigr)
}
\le h(x,u).
\]

Thus

\[
R_0(x,u)
=
h(x,u)-A(x)-B(u)
\ge0.
\]

### Theorem 5.1 — Zero-set localization

If

\[
R_0(x,u)=0,
\]

then:

1. both Bellman inequalities are equalities;
2. Cauchy--Schwarz is an equality;
3.
   \[
   K(x)K(u)=1.
   \]

Since \(K\ge1\),

\[
\boxed{
R_0(x,u)=0
\Longrightarrow
K(x)=K(u)=1.
}
\]

Moreover,

\[
p(x)=g(-x),
\qquad
p(-u)=g(u),
\]

and the zero relation reduces to

\[
\boxed{
S-d(x,u)=g(-x)+g(u).
}
\]

Hence every first-contact tie with either \(K(x)>1\) or \(K(u)>1\) is
irrelevant to the equality module.

---

## 6. Strict Monge ordering of the actual zero relation

Let \((x_1,u_1)\) and \((x_2,u_2)\) be two \(R_0\)-zero pairs.

The own-contact equalities and the two cross Bellman inequalities give

\[
h(x_1,u_1)+h(x_2,u_2)
\le
h(x_1,u_2)+h(x_2,u_1).
\]

For I3322 this is exactly

\[
\boxed{
(x_1-x_2)(u_1-u_2)\ge0.
}
\]

Therefore the full \(R_0=0\) relation is monotone.

If both coordinates differ, their order is strict and consistent. The only
remaining possible failure of graph injectivity is:

- two distinct targets sharing one source; or
- two distinct sources sharing one target.

By reflection these are the same plateau obstruction.

---

## 7. Exact remaining gate

The globally unique first Bellman predecessor demanded in the round-2
interface is stronger than the operator proof needs and may be false.

The exact remaining statement is only:

> **Plateau exclusion on the full \(R_0=0\) locus.**  
> No interior source \(x\) can satisfy \(R_0(x,u_1)=R_0(x,u_2)=0\) for
> \(u_1\ne u_2\).

Once this is proved, strict Monge ordering makes the \(R_0=0\) locus a
one-to-one strictly increasing graph on every finite occupied support. The
already-audited Sprint-1198 mechanism then applies.

This is a one-dimensional zero-defect certificate, not a full contact tiling.

---

## 8. Why the new lemmas do not alone prove plateau exclusion

If one source \(x\) has two zero targets \(u_1<u_2\), concavity and the common
Bellman line force

\[
g(u)
=
S-d(x,u)-p(x)
\qquad
(u_1\le u\le u_2).
\]

Thus \(g\) is affine on that target interval, and

\[
K(u_1)=K(u_2)=1.
\]

The inequalities \(g(u)g(-u)\ge b(u)^2\) do not, by themselves, prohibit two
such endpoint equalities. An additional strictness receipt for the
reflection-gluing defect is required.

A valid final receipt may take either form:

1. an analytic theorem that \(K=1\) cannot occur twice on one Bellman affine
   face; or
2. an interval certificate covering only the candidate plateau faces and
   proving \(K>1\) at one endpoint of every nontrivial face.

This is substantially smaller than certifying unique first contact for every
target.

---

## 9. Promotion status

Closed:

- limiting equality module at \(S\);
- exact endpoint exclusion;
- \(S>1/4\);
- fixed-point identity for terminal-pivot storage;
- reflection-gluing defect \(K\ge1\);
- localization and monotonicity of the true \(R_0=0\) relation.

Open:

\[
\boxed{
\text{plateau exclusion on }R_0^{-1}(0).
}
\]

Theorem (N) remains unpromoted until that final statement is certified and
blindly audited.
