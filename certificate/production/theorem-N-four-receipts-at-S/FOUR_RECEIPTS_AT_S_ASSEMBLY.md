# Four Receipts at `S` — promoted critical-weld assembly

**Date:** 2026-08-05  
**Status:** **PROMOTED as part of Theorem (N).**

## 1. Inputs

The proof uses:

1. Sprint 1295's common value `S` and terminal-pivot storage `g_q` for every
   `q>S`;
2. Sprint 1287's generic operator weld;
3. the certified window
   \[
   0.2508753845015185<S\le0.250875388108398;
   \]
4. Sprint 1292's exact dimension-255 lower strategy, so `S>1/4`;
5. the audited Sprint-1198 equality-kernel mechanism.

No Sprint-1195 fixed point or reflected left wing is imported.

---

# Receipt (i): limiting-weld substitute

Assume, for contradiction, that a fixed finite-dimensional strategy `rho`
attains `S`. Choose `q_n downarrow S`, with `q_n <= S_+`, and let `g_n` be the
Sprint-1295 storage. Then

\[
g_n\ge q_n-S>0
\]

and Bellman feasibility holds.

Every terminal-pivot function ending at `j` is affine in `j`, and

\[
|\partial_jd(i,j)|=|i-1/2|\le3/2.
\]

One-edge histories give a common upper bound. Thus a subsequence converges
uniformly:

\[
g_n\to g,
\]

where `g` is continuous and concave.

## Interior positivity

If `x in (-1,1)` and `g(x)=0`, then `b(x)>0` and feasibility gives, for fixed
`j`,

\[
g_n(j)\le q_n-d(x,j)-\frac{b(x)^2}{g_n(x)}\to-\infty,
\]

contradicting `g_n(j)>=q_n-S`. Hence

\[
\boxed{g(x)>0\quad(-1<x<1).}
\]

No endpoint positivity is asserted or needed.

## Passage of the weld — explicit spectral cutoff (W6)

For every `n`,

\[
q_nI-\mathcal B=R_{0,n}+R_{A,n}+R_{B,n},\qquad R_{\nu,n}\succeq0.
\]

Since `rho` attains `S`,

\[
\sum_\nu\operatorname{Tr}(\rho R_{\nu,n})=q_n-S\to0.
\]

Receipt (iii) excludes endpoint spectral mass. Because `rho` is
finite-dimensional, choose `c<1` so its occupied `X`- and `U`-spectra lie in
`[-c,c]`. Put

\[
\Pi=1_{[-c,c]}(X)\,1_{[-c,c]}(U).
\]

By the audited commutation and anticommutation relations, the symmetry of
`[-c,c]` makes `Pi` commute with the scalar operators and the response factors
appearing in all three remainders; `Pi rho=rho`. Uniform convergence of `g_n`
and interior positivity give uniform convergence of every scalar coefficient
on `[-c,c]`, hence

\[
\Pi R_{\nu,n}\Pi\to\Pi R_{\nu,\infty}\Pi
\]

in operator norm. Positivity and zero trace against `rho` pass to the limit:

\[
R_{\nu,\infty}\succeq0,\qquad
\operatorname{Tr}(\rho R_{\nu,\infty})=0,
\]

so

\[
\boxed{R_{\nu,\infty}\rho=0.}
\]

Thus a hypothetical finite maximizer carries the exact current equality module,
even if `g(1)` or `g(-1)` vanishes. The endpoint boundary layer is bypassed,
not solved.

---

# Receipt (iii): exact endpoint exclusion

Set `r=1/10`.

For the right endpoint line

\[
L_+^q(u)=q+\frac12-\frac u2,
\]

the history `1 -> 1-r -> u` gives

\[
L_+^q(u)-p_1
=r\left[\frac{2-r}{4q+2r}-\left(u+\frac12\right)\right].
\]

Uniformly for `q<=S_+` and `u in [-1,1]`,

\[
\boxed{
m_+=\frac{23686917837403}{3008753881083980}>0.
}
\]

For the left endpoint line

\[
L_-^q(u)=q+\frac32+\frac{3u}{2},
\]

the history `-1 -> -1+r -> u` gives

\[
\boxed{
m_-=\frac{274562305945801}{4008753881083980}>0.
}
\]

At an endpoint predecessor, one Bellman sum is at most `h-m_±` and the other at
most `h`. Hence

\[
h-\sqrt{h(h-m_\pm)}\ge\frac{m_\pm}{2}.
\]

The reflected identities give the same exclusion for endpoint target
coordinates. Therefore no occupied scalar atom has `x=±1` or `u=±1`.

**No interiority statement about the full active range is claimed or used.**

---

# Receipt (ii): weaker sufficient zero-locus graph

The proof does not require global uniqueness of the raw first-contact
predecessor. The operative statement is:

\[
\boxed{R_0^{-1}(0)\text{ on the occupied interior support is a one-to-one,
strictly increasing relation}.}
\]

It follows from:

1. concavity and the reflection-gluing inequality `K>=1`;
2. zero-set localization;
3. the repaired open-interval convex-minorant theorem;
4. horizontal exclusion;
5. the exact dual-tie involution and vertical exclusion;
6. strict Monge ordering.

Raw first-contact vertical ties may exist on chord regions. At most one member
of such a tie can lie on `R_0^{-1}(0)`.

---

# Receipt (iv): above the quarter ceiling

Sprint 1292 gives an exact dimension-255 strategy with value strictly above

\[
0.2508753845015185>\frac14.
\]

Together with Sprints 1287/1295,

\[
\boxed{S>1/4.}
\]

The classical bound is `0`; `1/4` is the qubit/qutrit and finite-common-return
ceiling.
