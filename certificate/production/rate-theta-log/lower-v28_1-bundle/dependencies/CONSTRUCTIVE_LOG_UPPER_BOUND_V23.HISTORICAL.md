# Constructive Logarithmic Upper Bound — v23

**Date:** 2026-08-06  
**Status:** repaired existence-class upper theorem; the unsupported decimal coefficient `13.2991468418` is retracted.  
**Inputs:** current spatial carrier Theorem (S), current endpoint classification, `ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md`, and `RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md`.

## 1. Retraction

No v23 statement uses

\[
13.2991468418
\]

as a certified coefficient. The old number had no derivation in the audit bundle and is removed from the claim ledger.

## 2. Coarse endpoint receipt E1

The exact current carrier has a bi-infinite full-zero scalar word. Let its target tail limits be \(\alpha,\beta\) and the corresponding predecessor limits \(x_+,x_-\).

The current endpoint classification excludes every boundary closure:

1. a mixed endpoint/interior closure contradicts the endpoint \(R_0\) gap;
2. cross corners are Bellman-infeasible;
3. a same-sign corner would force
   \[
   g(1)+g(-1)=S,
   \qquad g(1)g(-1)=0,
   \]
   hence one endpoint storage value equals \(S\), contradicting the certified endpoint-line margins.

Therefore

\[
\boxed{
\alpha,\beta,x_+,x_-\in K_0\Subset(-1,1)
}
\tag{2.1}
\]

for one compact interval \(K_0\). This is precisely E1 of the endpoint-Cesàro theorem. No TT-030 tail or historical value is used.

## 3. Strict outward multipliers

The current carrier supplies positive endpoint transport-density limits and hence outward two-step multipliers

\[
\rho_+,ho_->0.
\]

Square summability gives \(\rho_\pm\le1\). If \(\rho_+=1\), the endpoint limiting return equations satisfy the multiplicity-uniform neutral-return hypotheses and force \(S\le1/4\), contradicting \(S>1/4\). Likewise on the left. Hence

\[
\boxed{0<\rho_+,\rho_-<1.}
\tag{3.1}
\]

Define

\[
\kappa_+=-\log\rho_+>0,
\qquad
\kappa_-=-\log\rho_->0.
\]

Cesàro logarithmic transport then yields the exact one-sided asymptotic rates for the carrier amplitudes and boundary fluxes.

## 4. Effective two-tail exponent

For a finite retained interval with \(L\) sites on the left and \(R\) sites on the right, balance

\[
\kappa_-L\sim\kappa_+R.
\]

The effective exponent per total carrier dimension is

\[
\boxed{
\kappa_{\rm eff}
=
\left(\frac1{\kappa_-}+\frac1{\kappa_+}\right)^{-1}
>0.
}
\tag{4.1}
\]

The exact boundary-flux identity gives finite sections with

\[
S-v_I
\le
\exp[-\kappa_{\rm eff}|I|+o(|I|)].
\tag{4.2}
\]

## 5. Truncation legitimacy

Let

\[
I=[-L,R]\cap\mathbb Z,
\qquad
|\psi_I\rangle
=
\frac{\sum_{j\in I}\lambda_j|j,j\rangle}
{(\sum_{j\in I}\lambda_j^2)^{1/2}}.
\]

Complete every severed alternating \(2\times2\) measurement block by a one-dimensional endpoint projector. Then:

- all six local measurements remain projections;
- \(|\psi_I\rangle\) is a unit vector;
- local dimension is exactly \(|I|\);
- every retained Schmidt coefficient is positive.

The finite and infinite measurement blocks agree on the interior. The only value loss comes from omitted tail mass, omitted nearest-neighbor terms, and the two severed boundary bonds; normalization contributes the factor \((1-T_I)^{-1}\). Thus there is a fixed Bell constant \(C_B\) with

\[
0\le S-\mathcal B(\psi_I)
\le
C_B\frac{T_I+B_I}{1-T_I}.
\tag{5.1}
\]

Combining (4.2) and (5.1) gives

\[
\boxed{
S-S_{d+O(1)}
\le
\exp[-\kappa_{\rm eff}d+o(d)].
}
\tag{5.2}
\]

Equivalently,

\[
\boxed{
D_{\rm upper}(\varepsilon)
\le
\frac1{\kappa_{\rm eff}}\log\frac1\varepsilon
+o(\log(1/\varepsilon)).
}
\tag{5.3}
\]

## 6. Claim boundary

The theorem proves an existential logarithmic constructive upper bound. It does **not** certify a decimal value of \(1/\kappa_{\rm eff}\), does not prove the lower converse, and does not equate \(S\) with the historical Pál–Vértesi decimal.
