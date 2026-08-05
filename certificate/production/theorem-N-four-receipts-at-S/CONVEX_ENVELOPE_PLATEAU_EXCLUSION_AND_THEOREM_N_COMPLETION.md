# Convex-envelope plateau exclusion and completion of Theorem (N)

**Date:** 2026-08-05  
**Status:** **PROMOTED after round-3 repair W1–W4.**

This is the operative open-interval proof. It does not require any wing or
`range(P)` interiority receipt.

## 1. Storage and bounded intercept on the full source domain

Let `g` be the promoted limiting storage. It is finite and concave on
`[-1,1]`, and

\[
g(x)>0\qquad(x\in D:=(-1,1)).
\]

Define

\[
b(x)^2=\frac{1-x^2}{4},\qquad
p(x)=\frac{b(x)^2}{g(x)},\qquad
C(x)=S+1-\frac x2-p(x).
\]

Bellman feasibility is

\[
g(u)\le C(x)+\left(\frac12-x\right)u.
\]

At `u=0`,

\[
p(x)+g(0)\le S-d(x,0)=C(x)+p(x),
\]

so

\[
\boxed{C(x)\ge g(0)>0\quad(x\in D).}
\]

Because `p>=0` and `x>-1`,

\[
C(x)\le S+\frac32.
\]

Thus `C` is continuous and bounded on `D`, the constant `g(0)` is a convex
minorant, and the greatest convex minorant

\[
H=\operatorname{conv}_{\downarrow,D}C
\]

is finite on all of `D`.

This one-line lower bound makes the endpoint boundary layer harmless. No active
wing exclusion is needed. Moreover, if `g(1)=0` or `g(-1)=0`, concavity gives a
linear chord lower bound for `g` near that endpoint while `b(x)^2` vanishes
linearly. Hence `p=b^2/g` remains bounded; `C` cannot blow down at the boundary.

## 2. Downward-corner lemma

At every interior point,

\[
C'_+(x)-C'_-(x)
=\frac{b(x)^2}{g(x)^2}\bigl(g'_+(x)-g'_-(x)\bigr)\le0.
\]

Every corner of `C` points downward.

## 3. Envelope reduction — W2 repair

For fixed `u`, put

\[
m=\inf_{y\in D}[C(y)-uy].
\]

The affine function `y -> uy+m` is a convex minorant of `C`, so it is at most
`H`. Hence

\[
\inf_{y\in D}[H(y)-uy]\ge m.
\]

Since `H<=C`, the reverse inequality holds. Therefore

\[
\boxed{
\inf_{y\in D}[C(y)-uy]
=
\inf_{y\in D}[H(y)-uy].
}
\]

This proof is valid on the noncompact open interval and uses no chord endpoint.

## 4. No kink below the obstacle — W3 repair

Suppose `H(x_0)<C(x_0)` and `H'_-(x_0)<H'_+(x_0)`. Choose a slope strictly
between the one-sided derivatives and let `ell` be the corresponding affine
supporting line through `(x_0,H(x_0))`. Then `ell<=H`, with equality only at
`x_0`, and `H-ell` grows at least linearly on both sides.

For small `epsilon>0`,

\[
U_\epsilon=\{x:H(x)<\ell(x)+\epsilon\}
\]

is contained in a neighborhood where continuity and `H(x_0)<C(x_0)` give
`ell+epsilon<C`. Outside `U_epsilon`, `H>=ell+epsilon`. Thus

\[
\max(H,\ell+\epsilon)
\]

is a convex minorant of `C` strictly above `H` at `x_0`, contradicting the
maximality of `H`.

Therefore `H` has no kink at any point where `H<C`.

## 5. Contact points and strengthened no-kink theorem — W5

Suppose `H(x_0)=C(x_0)`. Put `F=C-H>=0`. Since `F(x_0)=0`,

\[
F'_-(x_0)\le0\le F'_+(x_0).
\]

Hence

\[
C'_-(x_0)\le H'_-(x_0)\le H'_+(x_0)\le C'_+(x_0).
\]

The downward-corner lemma gives `C'_-(x_0)>=C'_+(x_0)`, so equality holds
throughout:

\[
\boxed{C'_-(x_0)=H'_-(x_0)=H'_+(x_0)=C'_+(x_0).}
\]

Thus `C` is differentiable at every contact point, `H'=C'` there, a strict
downward corner of `C` is never active, and `H` is differentiable everywhere
on `D`.

## 6. Correct activity implication — W4

If `x` minimizes `C(y)-uy` over `D`, then the envelope reduction gives

\[
C(x)-ux=m\le H(x)-ux\le C(x)-ux.
\]

Therefore

\[
H(x)=C(x)
\]

and `x` minimizes `H(y)-uy`, so

\[
\boxed{x\text{ active for }C\quad\Longrightarrow\quad u\in\partial H(x).}
\]

The converse is not asserted and is false where `H<C`.

Since `H` is differentiable, one source cannot be active for two distinct
targets.

## 7. Binding to the full zero locus — W1 repair

If `(x,u) in R_0^{-1}(0)`, zero-set localization gives the first Bellman
equality as an equality:

\[
g(u)=C(x)+\left(\frac12-x\right)u.
\]

Feasibility gives the corresponding inequality for **every** `y in D`. Thus
`x` is active for the full source domain `D`, not for a restricted interval,
and

\[
u=H'(x).
\]

Consequently one source cannot serve two distinct full-zero targets.

## 8. Dual tie and vertical exclusion

The definitional identity `B(u)=A(-u)` and polynomial identity
`d(-u,-x)=d(x,u)` give

\[
\boxed{R_0(-u,-x)=R_0(x,u).}
\]

If two distinct sources shared one full-zero target, reflection would produce
one source with two distinct full-zero targets, contradicting Section 7.

This theorem concerns `R_0^{-1}(0)`. The raw first-contact correspondence may
have vertical ties at chord endpoints; at most one such source is a full-zero
source.

## 9. Strict graph and completion

Strict Monge gives

\[
(x_1-x_2)(u_1-u_2)\ge0
\]

for full-zero pairs. Horizontal and vertical equality are excluded unless the
pairs coincide. Therefore

\[
\boxed{R_0^{-1}(0)\cap D^2\text{ is a one-to-one strictly increasing relation}.}
\]

On a hypothetical finite maximizer this is precisely the weaker graph property
consumed by Sprint 1198. The unitary response maps are total decreasing
bijections of the same finite ordered support, hence coincide; the audited
amplitude elimination gives `S<=1/4`, contradicting Sprint 1292.

Theorem (N) follows.
