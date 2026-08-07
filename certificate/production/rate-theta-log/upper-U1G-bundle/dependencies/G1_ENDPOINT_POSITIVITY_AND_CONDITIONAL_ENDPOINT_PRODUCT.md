# G1 Repair — Endpoint Positivity, Conditional Endpoint Product, and Uniform Collar

**Status:** **PROVED CANDIDATE; promotion audit may attack provenance/typing but no new frontier input is assumed.**  
**Supersedes:** `UNIFORM_ENDPOINT_COLLAR_OR_REPLACEMENT_GATE_V23.md` as the live G1 record.

## 1. Inputs

Let `g=g_S` be the canonical critical storage. The consumed promoted/current receipts are:

1. `g` is continuous on `[-1,1]` and `3/2`-Lipschitz there;
2. reflection gluing on the interior:
   \[
   g(t)g(-t)\ge b(t)^2=\frac{1-t^2}{4};
   \]
3. the certified upper wall
   \[
   S\le S_+=0.250875388108398;
   \]
4. the finite-history endpoint-line inactivity reserves, with their exact provenance stated separately in `08_ENDPOINT_RECEIPT_PROVENANCE.md`:
   \[
   g(1)<S-\frac{4039}{100000},
   \qquad
   g(-1)<S-\frac{9893}{50000}.
   \]

The last two rationals are **not** Theorem-(N)'s exact `m_+`,`m_-` remainder margins.

## 2. Endpoint positivity

Assume first `g(1)=0`. By the closed-interval `3/2`-Lipschitz modulus,

\[
 g(t)\le\frac32(1-t),\qquad t<1.
\]

Reflection gluing gives

\[
 g(-t)
 \ge
 \frac{(1-t^2)/4}{(3/2)(1-t)}
 =\frac{1+t}{6}.
\]

Letting `t` increase to `1` and using continuity,

\[
 g(-1)\ge\frac13.
\]

But

\[
 g(-1)
 <S_+-\frac{9893}{50000}
 =\frac{26507694054199}{500000000000000}
 <\frac13.
\]

Contradiction.

Similarly, `g(-1)=0` would imply `g(1)>=1/3`, while

\[
 g(1)
 <S_+-\frac{4039}{100000}
 =\frac{105242694054199}{500000000000000}
 <\frac13.
\]

Therefore

\[
\boxed{g(1)>0,\qquad g(-1)>0.}
\]

The exact reserves against `1/3` are

\[
\frac13-\left(S_+-\frac{4039}{100000}\right)
=\frac{184271917837403}{1500000000000000}>0,
\]

\[
\frac13-\left(S_+-\frac{9893}{50000}\right)
=\frac{420476917837403}{1500000000000000}>0.
\]

`guards/guard_g1_endpoint_arithmetic.py` checks these identities over `Q`.

## 3. Correction to the endpoint-product claim

The statement

\[
\boxed{g(1)g(-1)=0}
\]

is **false as an unconditional/global receipt** and is killed.

The valid implication is conditional. If `(x_n,u_n)` is a sequence of full-zero pairs and one coordinate `t_n` tends to `+1` or `-1`, zero-set localization gives

\[
K(t_n)=1,
\qquad
 g(t_n)g(-t_n)=b(t_n)^2.
\]

Since `b(t_n)^2 -> 0`, continuity yields

\[
 g(1)g(-1)=0.
\]

Endpoint positivity contradicts this. Hence no full-zero sequence can approach either endpoint.

Thus the closed full-zero set is compactly interior:

\[
\boxed{
Z:=R_0^{-1}(0)\Subset(-1,1)^2.
}
\]

This is the only lawful use of the endpoint-product implication in the new package.

## 4. Uniform near-critical collar

Because `g` is positive on the entire compact interval,

\[
m_g:=\min_{[-1,1]}g>0.
\]

The canonical storage comparison gives, for every `q>S`,

\[
 g_q(t)\ge g_S(t)+(q-S)\ge m_g.
\]

Hence

\[
p_q(t)=\frac{b(t)^2}{g_q(t)}
\]

has no endpoint singularity. The common Lipschitz modulus and uniform convergence `g_q -> g_S` imply uniform convergence of the scalar weld coefficients and therefore

\[
\phi_q\to\phi_S
\]

uniformly on the closed square.

Since `Z` is compactly interior, choose a fixed boundary collar `C_end` disjoint from `Z`. Continuity gives

\[
 c_0:=\min_{C_{\rm end}}\phi_S>0.
\]

For all sufficiently near-critical `q`, uniform convergence yields

\[
\boxed{
\phi_q\ge c_0/2
\quad\text{on }C_{\rm end}.
}
\]

Therefore boundary-collar mass is paid by the positive scalar remainder and every unpaid response walk lies in one fixed interior corridor. Values of `q` bounded a fixed amount above `S` are already directly paid by that level gap, so only the near-critical regime is load-bearing.

Consequently the v23 coefficient floor and ceiling become lawful existential constants:

\[
0<b_0\le b(t),
\qquad
A_{\max}<\infty,
\qquad
\sigma=b_0/A_{\max}>0.
\]

## 5. Claim boundary

This document proves **existence-class G1**. It does not certify a public decimal corridor width, does not revive the old global endpoint-product identity, and does not authorize the previously floated `1/2000` global storage floor.
