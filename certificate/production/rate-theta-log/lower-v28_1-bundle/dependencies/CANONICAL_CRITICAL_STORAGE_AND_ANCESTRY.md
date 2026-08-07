# Canonical Critical Storage and the Finite-History Ancestry Criterion

**Date:** 2026-08-05  
**Status:** exact analytic theorem candidate.  
**Scope:** Sprint-1295 terminal-pivot storages and the repaired current-\(S\)
Bellman grammar.

# 1. Finite-history pivots

For a finite label history

\[
\mathfrak h=(c_0,c_1,\ldots,c_m),
\]

define its Schur pivots at level \(q>S\) by

\[
p_1(q)=q-d(c_0,c_1),
\]

\[
p_{k+1}(q)
=
q-d(c_k,c_{k+1})
-
\frac{b(c_k)^2}{p_k(q)}.
\]

All pivots are positive for \(q>S\). The terminal-pivot storage is

\[
g_q(t)
=
\inf\{p_m(q):\mathfrak h\text{ finite and }c_m=t\}.
\]

It satisfies

\[
g_q=T_qg_q,
\]

where

\[
(T_qh)(t)
=
\inf_x
\left[
q-d(x,t)-\frac{b(x)^2}{h(x)}
\right].
\]

# 2. Parameter comparison

## Lemma 2.1 — Finite-history redshift

If \(q_2=q_1+\eta\), \(\eta>0\), then for every fixed finite history,

\[
\boxed{p_k(q_2)\ge p_k(q_1)+\eta}
\]

at every pivot.

The first pivot is immediate. If the claim holds at \(k\), then

\[
p_{k+1}(q_2)-p_{k+1}(q_1)
=
\eta
+
b(c_k)^2
\left(
\frac1{p_k(q_1)}
-
\frac1{p_k(q_2)}
\right)
\ge\eta.
\]

## Theorem 2.2 — Storage comparison

For \(S<q_1<q_2\),

\[
\boxed{
g_{q_2}(t)
\ge
g_{q_1}(t)+(q_2-q_1).
}
\]

Thus both \(g_q(t)\) and \(g_q(t)-q\) are increasing in \(q\).

# 3. Canonical critical limit

Define

\[
\boxed{
g_S(t)=\inf_{q>S}g_q(t).
}
\]

Then

\[
g_q(t)\downarrow g_S(t)
\qquad(q\downarrow S).
\]

The common spatial modulus of continuity and one-edge upper bounds imply
uniform convergence:

\[
\boxed{
g_q\to g_S
\quad\text{uniformly on }[-1,1].
}
\]

Consequently every sequence \(q_n\downarrow S\) yields the same critical
storage. Moreover,

\[
\boxed{
g_q(t)\ge g_S(t)+(q-S).
}
\]

# 4. Greatest-feasible characterization

Call \(h\) Bellman-feasible at level \(q\) when \(h>0\) on the interior and

\[
h(t)
\le
q-d(x,t)-\frac{b(x)^2}{h(x)}
\]

for all \(x,t\), with the natural endpoint convention.

## Theorem 4.1 — Maximality above the wall

\[
\boxed{
h\le T_qh
\quad\Longrightarrow\quad
h\le g_q.
}
\]

Indeed, feasibility shows every one-edge terminal pivot dominates \(h\).
If a preceding pivot dominates \(h(c_k)\), monotonicity of
\(-b(c_k)^2/p\) in \(p\) propagates the domination to the next pivot. Taking
the infimum over all histories proves the result.

## Theorem 4.2 — Greatest critical storage

\[
\boxed{
h\le T_Sh
\quad\Longrightarrow\quad
h\le g_S.
}
\]

Critical feasibility implies feasibility at every \(q>S\); apply Theorem 4.1
and let \(q\downarrow S\).

# 5. Exact critical fixed point

The limiting Bellman inequalities give

\[
g_S\le T_Sg_S.
\]

Since \(T_S\) is order preserving,

\[
T_Sg_S\le T_S^2g_S.
\]

Thus \(T_Sg_S\) is feasible. Greatest-feasible maximality gives

\[
T_Sg_S\le g_S.
\]

Therefore

\[
\boxed{g_S=T_Sg_S.}
\]

The current storage is the greatest positive critical fixed point.

# 6. Storage trace on an exact equality orbit

For a current full-zero characteristic orbit

\[
P(c_{j+1})=c_j,
\]

zero-set localization gives

\[
g_S(c_j)g_S(-c_j)=b(c_j)^2
\]

and the Riccati recurrence

\[
g_S(c_{j+1})
=
S-d(c_j,c_{j+1})
-
\frac{b(c_j)^2}{g_S(c_j)}.
\]

For the positive scalar mode \(\lambda\),

\[
\frac{\lambda_{j+1}}{\lambda_j}
=
\sqrt{\frac{g_S(c_j)}{g_S(-c_j)}}.
\]

Hence

\[
\boxed{
g_S(c_j)
=
b(c_j)\frac{\lambda_{j+1}}{\lambda_j},
}
\]

\[
\boxed{
g_S(-c_j)
=
b(c_j)\frac{\lambda_j}{\lambda_{j+1}}.
}
\]

# 7. Why another fixed point is not automatically current

If \(F=T_SF\), maximality yields only

\[
F\le g_S.
\]

A fixed point need not be the greatest fixed point. Matching the value,
fixed-point equation, dual-zero identity, or one normalizable orbit does not
alone prove \(F=g_S\).

# 8. Finite-history saturation

A critical storage \(F\) is **finite-history saturated** when, for every
target \(t\) and every \(\varepsilon>0\), there is a finite history ending at
\(t\) whose level-\(S\) pivots are positive and whose terminal pivot obeys

\[
p_{\mathfrak h}(S)\le F(t)+\varepsilon.
\]

## Theorem 8.1 — Analytic ancestry criterion

Let \(F\) be continuous, positive on the interior, and Bellman-feasible at
\(S\). Then

\[
\boxed{F=g_S}
\]

if and only if \(F\) is finite-history saturated.

Maximality gives \(F\le g_S\). Saturation gives the reverse inequality because
for a fixed positive-pivot history,

\[
g_q(t)\le p_{\mathfrak h}(q),
\]

and the finite pivot is continuous in \(q\) at \(S\). Let \(q\downarrow S\)
and then \(\varepsilon\downarrow0\).

# 9. Equivalent ancestry receipts

Any of the following identifies a proposed analytic wall \(F_{\rm an}\) with
\(g_S\):

1. finite analytic predecessor histories whose terminal pivots converge to
   \(F_{\rm an}(t)\) for every target;
2. uniform collapse of finite-history upper brackets
   \[
   U_N^S\downarrow F_{\rm an};
   \]
3. proof that every critical feasible \(h\) satisfies \(h\le F_{\rm an}\);
4. orbit saturation plus global exhaustion of the Bellman lower envelope.

# 10. Exact remaining gate

The current storage is now canonical. Historical/current identification is
exactly the question:

\[
\boxed{
\textbf{Does the proposed analytic wall satisfy finite-history saturation?}
}
\]

Once this is proved, its predecessor graph, shooting coordinate, cocycle and
interval estimates become current-\(S\) data.

# 11. Claim boundary

Proved:

- finite-history parameter comparison;
- canonical subsequence-independent critical limit;
- greatest-feasible characterization;
- exact critical fixed point;
- storage trace on equality orbits;
- finite-history saturation iff analytic identification.

Open:

- saturation of the proposed TT-030/released analytic wall at current \(S\);
- historical/current graph identification;
- the universal lower exponent.
