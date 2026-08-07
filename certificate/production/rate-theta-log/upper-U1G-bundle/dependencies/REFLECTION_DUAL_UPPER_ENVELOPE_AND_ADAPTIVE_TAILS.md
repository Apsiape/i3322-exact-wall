# Reflection-Dual Upper Envelopes and Adaptive Tail Unfolding

**Date:** 2026-08-05  
**Status:** exact analytic theorem plus one exact rational current-\(S\) endpoint-line certificate.  
**Scope:** canonical critical storage \(g_S\), finite-history upper envelopes,
and orbit-adapted interval tilings.

---

# 1. Reflection converts one upper wall into a two-sided bracket

Let \(g_S\) be the canonical critical terminal-pivot storage. The
reflection-gluing theorem gives

\[
g_S(x)g_S(-x)\ge b(x)^2
\qquad(-1<x<1).
\]

Let \(H\) be any pointwise upper bound:

\[
H\ge g_S.
\]

Define

\[
\boxed{
L_H(x)=\frac{b(x)^2}{H(-x)}.
}
\]

Then

\[
\boxed{
L_H(x)\le g_S(x)\le H(x).
}
\]

Indeed,

\[
g_S(x)
\ge
\frac{b(x)^2}{g_S(-x)}
\ge
\frac{b(x)^2}{H(-x)}.
\]

This lower bound does not require a lower Bellman iteration or a feasibility
cone.

---

# 2. Direct bracket for the Bellman line intercept

Put

\[
p_S(x)=\frac{b(x)^2}{g_S(x)}
\]

and

\[
C_S(x)
=
S+1-\frac x2-p_S(x).
\]

From the reflection bracket,

\[
\boxed{
\frac{b(x)^2}{H(x)}
\le
p_S(x)
\le
H(-x).
}
\]

Suppose

\[
S_-\le S\le S_+.
\]

Then

\[
\boxed{
S_-+1-\frac x2-H(-x)
\le
C_S(x)
\le
S_++1-\frac x2-\frac{b(x)^2}{H(x)}.
}
\]

Consequently every Bellman source line

\[
\Lambda_x(u)
=
C_S(x)+\left(\frac12-x\right)u
\]

has a rigorous interval enclosure derived from an upper wall alone.

This is stronger than the failed zero-seed lower iteration: it brackets the
quantity consumed by contact localization directly.

---

# 3. Finite-history upper envelopes

Fix \(q_0>S\). For every finite history \(\mathfrak h\), its terminal pivot is
an affine function of the last target:

\[
\ell_{\mathfrak h}(u)=A_{\mathfrak h}+m_{\mathfrak h}u.
\]

For any finite family \(\mathcal H\), define

\[
\boxed{
H_{\mathcal H}(u)
=
\min_{\mathfrak h\in\mathcal H}\ell_{\mathfrak h}(u).
}
\]

Because \(g_{q_0}\) is the infimum over all finite histories,

\[
g_S\le g_{q_0}\le H_{\mathcal H}.
\]

Thus every finite family of positive-pivot histories produces a valid current
upper wall.

If \(q_0\) and every history label are rational, all pivots, affine lines,
breakpoints and endpoint-line margins are rational.

The histories may be selected numerically. The selection has no authority:
only the subsequent exact positivity and inequality checks are used.

---

# 4. Exact current-\(S\) endpoint-line certificate

Use the certified interval

\[
S_-
=
0.2508753845015185,
\]

\[
S_+
=
0.250875388108398.
\]

Set

\[
q_0=S_++10^{-7}.
\]

The accompanying exact verifier:

1. runs a 2001-point floating grid scout only to select predecessor histories;
2. takes 2001 histories of depth 100 on the rational grid
   \[
   -1,-0.999,\ldots,1;
   \]
3. recomputes every pivot exactly over \(\mathbb Q\);
4. verifies every pivot is positive;
5. constructs the exact rational lower envelope \(H\);
6. minimizes the two explicit endpoint-line differences exactly over every
   affine envelope segment.

The endpoint predecessor lines at the lower certified value are

\[
E_+(u)
=
S_-+\frac12-\frac u2,
\]

\[
E_-(u)
=
S_-+\frac32+\frac{3u}{2}.
\]

The exact rational output proves

\[
\boxed{
E_+(u)-H(u)>\frac{4039}{100000}
}
\]

for every \(u\in[-1,1]\), and

\[
\boxed{
E_-(u)-H(u)>\frac{9893}{50000}
}
\]

for every \(u\in[-1,1]\).

Numerically, the exact minima are approximately

\[
0.0403971747999968
\]

and

\[
0.197860622685758.
\]

Since

\[
g_S\le H
\]

and the true endpoint lines at \(S\) lie above the lines at \(S_-\), we obtain:

## Theorem 4.1 — Current Endpoint-Line Inactivity

\[
\boxed{
g_S(u)
<
S+\frac12-\frac u2-\frac{4039}{100000}
}
\]

and

\[
\boxed{
g_S(u)
<
S+\frac32+\frac{3u}{2}-\frac{9893}{50000}
}
\]

for every \(u\in[-1,1]\).

Thus neither endpoint predecessor \(x=+1\) nor \(x=-1\) can be an exact
Bellman contact at the current wall.

This is a global exact finite-history certificate. It is independent of the
historical reflected-wing construction.

---

# 5. Why a uniform grid produces a false return cycle

Suppose one branch of the exact predecessor graph is a strictly increasing
homeomorphism \(P\) with an accumulation fixed point \(\alpha\), and let

\[
P(c_{n+1})=c_n,
\qquad
c_n\to\alpha.
\]

A uniform grid eventually places many consecutive \(c_n\) in the same cell.
The induced cell graph then contains a self-loop, even though the underlying
orbit is open and has no finite return.

Therefore a grid self-cycle near an accumulation point is not evidence of a
finite scalar cycle.

This explains the 1201-point reconnaissance self-cycle near
\(x\approx0.8783\): it is consistent with an unresolved compressed tail.

---

# 6. Orbit-adapted interval cells

Define the characteristic cells

\[
I_n
=
[\min(c_n,c_{n+1}),\max(c_n,c_{n+1})].
\]

Monotonicity gives

\[
\boxed{
P(I_{n+1})=I_n.
}
\]

For one response step

\[
\tau=P^{-2},
\]

the parity cells satisfy

\[
\boxed{
\tau(I_{n+2})=I_n.
}
\]

Thus the active cell graph is a shift, not a cycle.

On every finite truncation it is acyclic. A Bellman feasibility-cone error
system on these cells is solved by finite back-substitution; no spectral-radius
condition is required.

---

# 7. Tail error recursion

Let an orbit-adapted Bellman enclosure have cell errors \(e_n\) obeying

\[
e_{n+1}
\ge
r_{n+1}+k_ne_n.
\]

On a finite open chain,

\[
e_N
\]

is set by the terminal or boundary-flux receipt, and the remaining errors are
obtained recursively.

If the chain is bi-infinite with a positive square-summable mode, the Riccati
boundary-flux theorem supplies the vanishing terminal condition:

\[
b(c_{-N})\lambda_{-N}\lambda_{-N+1}\to0.
\]

Hence the open-tail feasibility certificate is compatible with the exact
spatial carrier without converting its accumulation point into a false fixed
packet.

---

# 8. Reflection-envelope contact localization criterion

Let \(J\) be a target interval and \(I_\ast\) a proposed source interval.
Choose one rational candidate source \(x_\ast\in I_\ast\).

Using the intercept bracket, compute an upper bound

\[
U_\ast(J)
\ge
\sup_{u\in J}\Lambda_{x_\ast}(u).
\]

For every other source interval \(I\), compute a lower bound

\[
L_I(J)
\le
\inf_{\substack{x\in I\\u\in J}}\Lambda_x(u).
\]

If

\[
\boxed{
L_I(J)>U_\ast(J)
\qquad
(I\ne I_\ast),
}
\]

then every exact predecessor for every \(u\in J\) lies in \(I_\ast\).

For a rational finite-history envelope, these bounds reduce to extrema of
affine or bilinear rational expressions on rectangles.

Nested target refinement with

\[
\operatorname{diam}I_\ast(J)\to0
\]

certifies the current predecessor graph.

---

# 9. Revised executable path

The rigorous current-\(S\) computation should now use:

1. exact rational finite-history upper envelopes;
2. reflection-derived intercept brackets;
3. the exact endpoint-line margins above;
4. orbit-adapted tail cells rather than a uniform endpoint grid;
5. a feasibility cone only where the reflection bracket is not sufficiently
   sharp.

The lower wall need not be generated globally before contact localization
begins.

---

# 10. Claim boundary

Proved:

- reflection-derived storage lower bound from any upper wall;
- direct Bellman-intercept bracket;
- exact rational finite-history upper-envelope construction;
- exact current endpoint-line inactivity margins;
- adaptive-tail unfolding theorem;
- interval contact-localization criterion.

Reconnaissance only:

- interpretation of the previous uniform-grid self-cycle as compressed tail
  behavior.

Open:

- a full nested current contact tiling;
- certified tail coordinates and gain products;
- the universal finite-dimensional lower exponent.
