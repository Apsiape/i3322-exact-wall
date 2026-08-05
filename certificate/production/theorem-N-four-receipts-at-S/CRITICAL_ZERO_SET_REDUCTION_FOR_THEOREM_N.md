# Critical zero-set reduction for Theorem (N)

**Date:** 2026-08-05  
**Status:** **PROMOTED component of Theorem (N).**

The critical path uses concavity, reflection-gluing, zero-set localization, and
strict Monge. The exact fixed-point identity `g_q=T_qg_q` is retained below as
an auxiliary theorem but is **not** a dependency of Theorem (N).

## 1. Auxiliary fixed-point identity — not on the critical path

For `q>S`, let `g_q(j)` be the infimum of terminal Schur pivots over finite
histories ending at `j`, and define

\[
(T_qh)(j)=\inf_i\left[q-d(i,j)-\frac{b(i)^2}{h(i)}\right].
\]

History extension gives `g_q<=T_qg_q`. Conversely, a one-edge pivot dominates
the corresponding Bellman expression, and for longer histories the Riccati
update is increasing in the preceding pivot. Therefore

\[
\boxed{g_q=T_qg_q.}
\]

This identity is valid but unused downstream.

## 2. Concavity

For I3322,

\[
d(i,j)=ij+\frac{i-j}{2}-1
\]

is affine in `j`. Every terminal pivot is affine in its terminal label; an
infimum of affine functions is concave. Uniform limits preserve concavity, so

\[
\boxed{g\text{ is concave}.}
\]

## 3. Downward corners

Put

\[
p(x)=\frac{b(x)^2}{g(x)},\qquad C(x)=S+1-\frac x2-p(x).
\]

At every interior point, concavity gives `g'_-(x)>=g'_+(x)`, hence

\[
C'_+(x)-C'_-(x)
=\frac{b(x)^2}{g(x)^2}\bigl(g'_+(x)-g'_-(x)\bigr)\le0.
\]

Every nonsmooth corner of `C` points downward.

## 4. Reflection-gluing

For `q>S`, set `delta=q-S`. Reflecting and reversing a history ending at `-t`
and gluing it to a history ending at `t` leaves the Schur complement

\[
\begin{pmatrix}p&-b(t)\\-b(t)&r\end{pmatrix}\succeq\delta I.
\]

Taking independent infima gives

\[
\bigl(g_q(t)-\delta\bigr)\bigl(g_q(-t)-\delta\bigr)\ge b(t)^2.
\]

Passing to the promoted subsequential limit,

\[
\boxed{K(t):=\frac{g(t)g(-t)}{b(t)^2}\ge1\quad(t\in(-1,1)).}
\]

## 5. Full transport remainder and zero-set localization

Define

\[
A(x)=\sqrt{p(x)g(-x)},\qquad B(u)=\sqrt{g(u)p(-u)}=A(-u),
\]

\[
h(x,u)=S-d(x,u),\qquad R_0(x,u)=h(x,u)-A(x)-B(u).
\]

The two Bellman inequalities and Cauchy–Schwarz give `R_0>=0`.
If `R_0(x,u)=0`, then both Bellman inequalities and Cauchy are equalities and

\[
K(x)K(u)=1.
\]

Since `K>=1`,

\[
\boxed{K(x)=K(u)=1,}
\]

and in particular

\[
p(x)=g(-x),\qquad p(-u)=g(u).
\]

Every raw Bellman tie with `K>1` is outside the equality module.

## 6. Strict Monge

For two full-zero pairs `(x_1,u_1)` and `(x_2,u_2)`, own equalities and cross
Bellman inequalities imply

\[
(x_1-x_2)(u_1-u_2)\ge0.
\]

The convex-envelope theorem excludes equal sources with distinct zero-targets;
the dual-tie involution excludes equal zero-targets with distinct sources.
Thus distinct full-zero pairs are strictly ordered.

## 7. Asymmetry hygiene

The active Bellman envelope may be asymmetric; floating reconnaissance places
its source range near `[-0.8936,+0.8981]`. The involution

\[
R_0(-u,-x)=R_0(x,u)
\]

is not a symmetry assumption on `g`; it follows from `B(u)=A(-u)` and the exact
identity `d(-u,-x)=d(x,u)`.

The symmetry forced on a hypothetical occupied finite equality orbit and the
asymmetry of the full envelope are properties of different objects.
