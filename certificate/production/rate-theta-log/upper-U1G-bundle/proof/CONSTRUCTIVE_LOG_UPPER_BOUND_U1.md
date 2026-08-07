SUPERSEDED STAMP (2026-08-07): the U1 gate DENIED this document and
its strictness route is KILLED (round-1 verdicts on disk; ledger
entries 4-9). Retained as history only; nothing here is live. The
in-file status line below is the HISTORICAL claim of the superseded
round, not a current status.

# Constructive logarithmic upper bound at local-dimension scope — U1

**Status:** **UPPER-ONLY PROMOTION CANDIDATE.**  
**Claim under audit:**
\[
\boxed{D_{\rm upper}(\varepsilon)=O(\log(1/\varepsilon))}
\]
at **local Hilbert-space dimension** scope, with existential positive rate constant `1/kappa_eff`.  
**No numerical rate coefficient is asserted or consumed.**

The lower theorem
\[
D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon))
\]
is already promoted and is not reproved here. Consequently
\[
D(\varepsilon)=\Theta(\log(1/\varepsilon))
\]
may be stated only as the conditional corollary obtained if this U1 upper gate promotes.

---

## 1. Exact carrier and lawful endpoint corridor

By promoted Theorem (S), the exact value `S` is attained by a normal spatial rank-one carrier on two copies of `ell^2(Z)`. In the scalar/Jacobi representation used by the endpoint-Cesàro theorem there are labels
\[
c_j\in(-1,1)
\]
and positive amplitudes
\[
\lambda_j>0,\qquad \sum_j\lambda_j^2=1,
\]
with the exact current Bellman/Jacobi recurrence and Bell value `S`.

Promoted G1 supplies the endpoint receipt needed by the rate theorem. If a full-zero carrier sequence attempted to accumulate at either scalar endpoint, zero-set localization along that sequence would give
\[
g(t_n)g(-t_n)=b(t_n)^2\longrightarrow0,
\qquad
b(t)=\frac{\sqrt{1-t^2}}2,
\]
which contradicts continuity together with the promoted positive endpoint values. Therefore
\[
\boxed{Z=R_0^{-1}(0)\Subset(-1,1)^2.}
\tag{1.1}
\]
All four limiting source/target labels of the selected two tails therefore lie in one compact interior corridor. The scalar response multipliers used below are consequently finite, continuous, and strictly positive there.

No stronger endpoint statement is used.

---

## 2. Outward multipliers and the bound `rho_pm <= 1`

Use the source/destination convention of the endpoint-Cesàro receipt. At the forward end set
\[
a_+=r_{B,{\rm mult}}(\alpha_{\rm end}),
\qquad
b_+=r_{A,{\rm mult}}(x_{+,\rm end}),
\]
so that the outward two-step amplitude ratio tends to
\[
\boxed{\rho_+=\frac{a_+}{b_+}>0.}
\tag{2.1}
\]
At the negative end the outward characteristic orientation is reversed. Set
\[
a_-=r_{A,{\rm mult}}(x_{-,\rm end}),
\qquad
b_-=r_{B,{\rm mult}}(\beta_{\rm end}),
\]
so that
\[
\boxed{\rho_-=\frac{a_-}{b_-}>0.}
\tag{2.2}
\]

The promoted spatial carrier is an `ell^2` vector, hence
\[
\boxed{\lambda_j\to0\quad(j\to\pm\infty).}
\tag{2.3}
\]
The load-bearing input to strict ratio control is the limit (2.3). If, for example, `rho_+>1`, choose `delta>0` with `rho_+>1+2 delta`. Convergence of the outward two-step ratios then gives, for all sufficiently far forward indices,
\[
\frac{\lambda_{2n+2}}{\lambda_{2n}}>1+\delta,
\]
so that the positive subsequence is eventually geometrically increasing and cannot tend to zero. Contradiction. Thus `rho_+<=1`. The negative tail is identical after the outward orientation in (2.2). Therefore
\[
\boxed{0<\rho_\pm\le1.}
\tag{2.4}
\]

---

## 3. The endpoint `rho <=> q_ret` identification and strictness

This step is written here because it is load-bearing.

The distorted-return quarter theorem orients the ratio of its two **normalized response gains** into `(0,1]`:
\[
q_{\rm ret}=\min\left\{\frac{a}{b},\frac{b}{a}\right\}.
\tag{3.1}
\]
At the forward endpoint the normalized gain convention is precisely `(a,b)=(a_+,b_+)`. Since (2.4) gives `a_+/b_+=rho_+<=1`,
\[
\boxed{q_{{\rm ret},+}=\rho_+.}
\tag{3.2}
\]
At the negative endpoint we already chose the reversed outward convention `(a,b)=(a_-,b_-)`, and (2.4) again gives
\[
\boxed{q_{{\rm ret},-}=\rho_-.}
\tag{3.3}
\]
Hence at either end
\[
\rho_\pm=1
\quad\Longleftrightarrow\quad
q_{{\rm ret},\pm}=1.
\tag{3.4}
\]

The exact distorted-return theorem gives
\[
F(q)=\frac{(1+q)^2}{16q}
=\frac14+\frac{(1-q)^2}{16q}
\tag{3.5}
\]
for the current component equations. In the neutral case `q=1`,
\[
F(1)=\frac14.
\tag{3.6}
\]
The endpoint full-zero limiting sector at level `Q=S`, together with (3.2) or (3.3), would therefore force
\[
S\le\frac14
\]
if either `rho_+` or `rho_-` equalled one. This contradicts the promoted certified fact `S>1/4`. Consequently
\[
\boxed{0<\rho_+<1,\qquad0<\rho_-<1.}
\tag{3.7}
\]

Define, existentially,
\[
\boxed{
\kappa_+=-\log\rho_+>0,
\qquad
\kappa_-=-\log\rho_->0.
}
\tag{3.8}
\]
No numerical evaluation of these constants is part of U1.

---

## 4. Endpoint-Cesàro decay

On the forward even subsequence let `u_n=lambda_{2n}`. The exact carrier recurrence gives
\[
\frac{u_{n+1}}{u_n}\longrightarrow\rho_+.
\]
Therefore
\[
\log u_n
=\log u_0+
\sum_{k=0}^{n-1}\log\frac{u_{k+1}}{u_k},
\]
and ordinary Cesàro convergence yields
\[
\lim_{n\to\infty}-\frac1n\log\lambda_{2n}=\kappa_+.
\tag{4.1}
\]
The intervening odd ratio tends to a finite positive interior multiplier, so the odd subsequence has the same logarithmic tail rate in the characteristic indexing of the endpoint-Cesàro theorem. At the negative end,
\[
\lim_{n\to\infty}-\frac1n\log\lambda_{-2n}=\kappa_-.
\tag{4.2}
\]
Equivalently, the two severed boundary-bond costs and the corresponding omitted tail masses satisfy the upper asymptotic estimate
\[
T_I+B_I
\le
\exp(-\kappa_-L+o(L))+
\exp(-\kappa_+R+o(R))
\tag{4.3}
\]
for the two-sided intervals used below. This is exactly the endpoint-Cesàro carrier-rate receipt; no summability of ratio errors is required.

---

## 5. Explicit endpoint-projector truncation

Let
\[
I=[a,b]\cap\mathbb Z,
\qquad d=|I|=b-a+1.
\]
Retain the normalized state
\[
\boxed{
|\psi_I\rangle
=
\frac{\sum_{j=a}^{b}\lambda_j|j,j\rangle}
{M_I^{1/2}},
\qquad
M_I=\sum_{j=a}^{b}\lambda_j^2.
}
\tag{5.1}
\]
Thus `||psi_I||=1`, and both local Hilbert spaces are exactly `C^d`.

The infinite strategy uses the alternating nearest-neighbour matchings
\[
\mathcal M_0=\{\{2k,2k+1\}:k\in\mathbb Z\},
\qquad
\mathcal M_1=\{\{2k-1,2k\}:k\in\mathbb Z\}.
\tag{5.2}
\]
Every full `2x2` alternating block contained in `I` is assigned the same matrix entries as its infinite-carrier block by the truncation construction.

There are exactly two severed endpoint pairings to service:

- **Left endpoint:** the severed pairing is `\{a-1,a\}`. For whichever alternating measurement matching contains this pair, replace the cut `2x2` block on the retained coordinate by the one-dimensional projector `|a><a|`.
- **Right endpoint:** the severed pairing is `\{b,b+1\}`. For whichever alternating measurement matching contains this pair, replace the cut `2x2` block on the retained coordinate by the one-dimensional projector `|b><b|`.

Measurements whose endpoint block is not severed retain the matrix entries already assigned by the truncation construction.

For the complementary binary outcome use the complementary one-dimensional projector on the severed block. Hence each of the six displayed measurement projectors is a direct sum of mutually orthogonal rank-one `2x2` blocks and zero or more one-dimensional endpoint projectors. Therefore, exactly,
\[
\boxed{P^2=P=P^*}
\tag{5.3}
\]
for all six local operators.

The local dimension is not a padded path parameter:
\[
\boxed{\dim\mathcal H_A=\dim\mathcal H_B=d=|I|.}
\tag{5.4}
\]

Define omitted state mass and the two specifically named severed-bond masses by
\[
T_I=\sum_{j\notin I}\lambda_j^2,
\tag{5.5}
\]
\[
B_I=|\lambda_{a-1}\lambda_a|+|\lambda_b\lambda_{b+1}|.
\tag{5.6}
\]
The finite and infinite strategies agree on every interior alternating block. The only changed contributions are omitted diagonal tail terms, omitted nearest-neighbour tail terms, the left severed pairing `\{a-1,a\}`, the right severed pairing `\{b,b+1\}`, and normalization. The promoted truncation receipt therefore gives a constant `C_B<infinity`, depending only on the fixed Bell functional, such that
\[
\boxed{
0\le S-\mathcal B(\psi_I)
\le
C_B\frac{T_I+B_I}{1-T_I}.
}
\tag{5.7}
\]
Since `T_I -> 0` on the intervals below, `(1-T_I)^{-1}=1+o(1)`.

---

## 6. Balance the two tails

Choose `L,R -> infinity` so that
\[
\kappa_-L=\kappa_+R+o(L+R).
\tag{6.1}
\]
With
\[
d=L+R+1,
\]
(4.3) and (5.7) give
\[
S-\mathcal B(\psi_I)
\le
\exp(-\kappa_-L+o(L))
+
\exp(-\kappa_+R+o(R)).
\tag{6.2}
\]
The balanced common exponent per total retained local dimension is
\[
\boxed{
\kappa_{\rm eff}
=
\left(
\frac1{\kappa_-}+\frac1{\kappa_+}
\right)^{-1}>0.
}
\tag{6.3}
\]
Thus there is a sequence of explicit finite local-dimensional strategies with
\[
\boxed{
S-S_d
\le
\exp[-\kappa_{\rm eff}d+o(d)].
}
\tag{6.4}
\]
Here `d` is exactly the retained local Hilbert-space dimension of (5.4); there is no Schmidt-rank reinterpretation in the claim.

---

## 7. Invert the rate

Let `eta>0`. From (6.4), for all sufficiently large `d` in the balanced construction,
\[
S-S_d\le\exp[-(\kappa_{\rm eff}-\eta)d].
\]
Hence any sufficiently small `varepsilon` is achieved once
\[
d\ge\frac{1}{\kappa_{\rm eff}-\eta}\log\frac1\varepsilon+O(1).
\]
Letting `eta downarrow 0` yields
\[
\boxed{
D_{\rm upper}(\varepsilon)
\le
\frac1{\kappa_{\rm eff}}
\log\frac1\varepsilon
+o(\log(1/\varepsilon)).
}
\tag{7.1}
\]
In particular,
\[
\boxed{D_{\rm upper}(\varepsilon)=O(\log(1/\varepsilon)).}
\tag{7.2}
\]
The coefficient is existential. U1 certifies no decimal value for it.

---

## 8. Conditional combined corollary

The lower theorem is already promoted:
\[
D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).
\]
Therefore **if and only if the present U1 upper gate is promoted**, the two results combine at the same local-dimension scope to give
\[
\boxed{D(\varepsilon)=\Theta(\log(1/\varepsilon)).}
\tag{8.1}
\]
This line is a conditional corollary, not an independently promoted claim in this bundle.

---

## 9. Exact dependency boundary

Live analytic dependencies are only:

1. promoted Theorem (S), for existence of the exact positive spatial carrier;
2. promoted G1, only for compact interiority of the full-zero endpoint limits;
3. the endpoint-Cesàro carrier-rate receipt;
4. the exact distorted-return quarter ceiling;
5. the explicit endpoint-projector alternating-block truncation receipt;
6. the promoted lower theorem only for the conditional statement (8.1).

No numerical rate coefficient, no historical optimality identification, no retracted upper coefficient, no hyperbolicity assumption, and no new lower-bound argument is used.
