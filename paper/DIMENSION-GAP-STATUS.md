# Quantitative convergence and the open dimension lower bound

> **Superseded 2026-08-07.** The open lower bound named below has been
> discharged: `D(epsilon) = Theta(log(1/epsilon))` is proved, with the
> lower half unconditional. See the companion rate note in `paper/` and
> `certificate/production/rate-theta-log/`. This document remains the
> historical record of the one-sided constructive rate (its
> family-specific exponent `log R` is sharper than, and consistent with,
> the rate note's uniform safe constant) and of the gap as it was named.
>
> **Pointer update 2026-08-25.** The standalone rate note has been folded
> into the main paper: the result now appears as Section 5 of
> `paper/resolution.tex` / `resolution.pdf`. The certificates are
> unchanged at `certificate/production/rate-theta-log/`; the standalone
> note is preserved in the frozen v3.3.0 release.

## Definition

Let `Q_d` be the optimum of the normalized I3322 functional over
tensor-product strategies whose two local Hilbert spaces have dimensions at
most `d`. Mixed states and arbitrary binary POVMs are allowed. Let `q_*` be the
certified infinite-dimensional wall value.

Compactness and multilinear extremality imply that `Q_d` has a pure-state,
projective-measurement representative on the same local spaces. No Naimark
dilation or increase in dimension is used.

## Constructive upper bound on the deficit

For the certified positive wall, let `v_L` be the value obtained by compressing
all local effects and the state to indices `{-L,...,L}` and normalizing. With
`d=2L+1`, the exact principal-section identity is

```text
q_*-v_L = [h_-L lambda_-L-1 lambda_-L
            + h_(L+1) lambda_L lambda_(L+1)] / S_L.
```

The analytic wall tails give

```text
lim -log(q_*-v_L)/d = log R,
R = 1.07809205080209208...,
log R = 0.07519285919570202....
```

Since `Q_d>=v_L`, this proves

```text
0 < q_*-Q_d <= exp[-d log R+O(1)].
```

Thus `log(1/epsilon)/log R+O(1)` local dimension is sufficient.

## Conditional lower-bound campaign

The attempted robust equality-certificate argument produces the conditional
constants

```text
Gamma = (20*78/5)^4 = 312^4 = 9,475,854,336,
kappa = 4.294654614327144182412697296233929416...e-52
```

and would imply, for every `d>=1`,

```text
q_*-Q_d >= kappa d^-4 Gamma^-d.
```

The finite-rank, recurrence, inactive-tail, and scalar-closure pieces are
explicit. The missing implication is the localization of the global response
defect to the common near-fixed packets. The two-frame estimate contains full
complement terms, whereas the shifted pullback estimate controls only
unpaired mass after restriction. No existing certificate bounds the resulting
commutator/interface term.

The written ledger was separately reconstructed from a theorem packet and
then audited in exact arithmetic. A subsequent hostile reconstruction found
the missing localization premise. The corrected `48 epsilon_0` coefficient
and `kappa` remain meaningful only conditional on a future localization
theorem. The original chronology was not externally time-sealed.

## Present complexity consequence

Let `D(epsilon)` be the least `d` for which some allowed strategy has deficit
at most `epsilon`. The proved construction implies only

```text
D(epsilon) <= log(1/epsilon)/log R+O(1).
```

The matching lower order remains open. In particular, neither
`D(epsilon)=Theta(log(1/epsilon))` nor an optimal necessity exponent is
currently claimed.

## Post-review structural result

Keeping the four coarse omissions rather than deleting their complementary
parts yields a valid coupled-sector estimate

```text
m_near<=C_D(m_drift+m_out)+C_N sqrt(epsilon).
```

It follows that either the deficit exceeds an explicit fixed threshold or a
dimension-independent amount of active drift mass is present. This removes
the possibility that an almost-optimal finite strategy hides all of its mass
in the near-fixed sector for free.

It does not restore the dimension lower bound. An exact terminal-fork
countermodel shows that the two response-specific images of one localized
packet may occupy orthogonal multiplicity fibres under the same coarse
spectral label, even when the response involutions have the shared I3322
factor types and exact sign relations. Scalar packet norms therefore lose the
branch provenance needed to charge entry into the near-fixed sector.

Any future necessity proof must use a stronger contact-dependent rigidity
theorem or an operator/PSD/Gram-valued transport. The former scalar
common-packet completion is closed as a route under the current hypotheses.

## Operator-valued restart

Sprints 1240--1245 replace scalar packets by the coefficient operator `D` of
the bipartite state. The two response remainders control the complete matrix
correspondences

```text
J_A D S_B^T ~= C_A D,
S_A D J_B^T ~= D C_B^T.
```

This controls every singular value. The regularized support

```text
W_A,t=D(tI+D^*D)^(-1)D^*,
W_B,t=D^*(tI+DD^*)^(-1)D
```

interpolates between state mass and Schmidt rank. For cumulative contact
flags `E_s=1_{Y(X)<=s}` and `F_s=1_{U<=s}`, the global contact coercivity gives
the grid-free theorem

```text
integral ||E_sD-D F_s^T||_HS^2 ds <= sqrt(40 epsilon_0).
```

Marginal singular/volume balances do not close the proof: an exact finite
doppelganger preserves all of them while using two different target
involutions. The relative invariant is the mixed cumulative-flag distance,
which is a weighted permutation footrule and extends to rowwise
Wasserstein-1 distance for branch-mixing kernels.

At exact contact, the response multiplier `C=c(X)` acts on regularized support
by

```text
W_t(CD)=W_(t/c^2)(D)
```

on each contact block. Thus the known amplitude cocycle is canonically a
translation of `log t`, not an artifact of the discarded packet model.

Sprints 1246--1259 sharpen this further. Logarithmic differentiation turns the
soft flag into a positive order--resolution measure of total mass equal to
Schmidt rank, and the state coefficient operator supplies a canonical positive
coupling of the Alice and Bob measures. A shifted grid buys a common coarse
source with every rejected event charged to contact debt, and the pointwise
quarter wall survives the cell diameter.

The output topology is now part of the theorem rather than a bookkeeping
choice. Total variation on rounded atoms is discontinuous, and ordinary joint
Wasserstein transport can erase a fixed resolution mismatch by swapping
nearby fibres. The complete ordered flag instead defines monotone-fibre
transport. Its vertical cost is recovered exactly from synchronized prefix
tails with only a linear rank factor. The remaining gate is to prove that the
two I3322 operator response receipts control those synchronized prefixes on
the canonical carrier. No universal deficit lower bound is claimed until that
common-carrier receipt is proved and independently reconstructed.

Sprints 1260--1265 subsequently close the geometric part of that receipt.
The contact coupling is integrable on the complete upper tail needed by the
flow, the event measure has a rank-independent exponential upper cap, and one
shared shifted grid supplies identical original-order and response-output
prefixes. The I3322 derivative box also makes the vertical translation sign
coherent inside each retained output cell. Thus the remaining gate is no
longer a choice of carrier or fibre: it is the explicit integration of the
Sprint-1249 response errors and the charged source/output/band complements.
No universal deficit lower bound is claimed before that ledger is completed
and independently audited.

## Numerical illustration of the constructive sequence

| local dimension | value | gap to `q_*` |
|---:|---:|---:|
| 31 | 0.250492717483438 | 3.82667e-4 |
| 63 | 0.250850779989507 | 2.46045e-5 |
| 127 | 0.250875195790122 | 1.88724e-7 |
| 191 | 0.250875382981378 | 1.53260e-9 |
| 255 | 0.250875384501519 | 1.24575e-11 |

The table illustrates the upper construction only; no fit from these values
enters either theorem.

## Scope and release status

The constructive estimate is valid for the unrestricted tensor-product
optimum because the explicit truncations are admissible strategies. It does
not prove that those truncations attain `Q_d`. The proposed device-independent
necessity theorem is on hold pending the missing localization lemma; no v1.3
tag or DOI should be created from the conditional argument.
