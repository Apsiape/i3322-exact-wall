# Adjudication of the prospective v1.3 model review

**Date:** 2026-08-04  
**Decision:** **HOLD -- do not tag, publish, or mint v1.3**

## Review posture

Human referee access is unavailable.  The project therefore uses isolated
frontier-model reconstructions as its accepted adversarial review mechanism.
The three lanes were separated by packet and attack surface, but they share a
broad model lineage.  Their reports are evidence only to the extent that the
underlying arguments can be reproduced.

## Reproduced findings

### Quantifiers and asymptotics -- repaired

- `Q_d` now explicitly ranges over arbitrary mixed states and binary POVMs.
- Same-dimension pure/projective reduction is stated without Naimark dilation.
- The constructive bound is *witnessed* by truncations, not said to be
  attained by them.
- The tail argument now uses the analytic unstable-manifold asymptotic
  `lambda_j=C_+R^{-j}(1+O(rho^j))`; a ratio limit alone was insufficient for a
  dimension-independent prefactor.

### Packet and constant audit -- partly repaired, one blocker remains

- The omitted scalar closure and pullback-address sources are now included as
  Sprints 1226 and 1227.
- The canonical packet uses the saturated preimage `Y^{-1}(gI)`, not the
  unsaturated `P(gI)` expression.
- Source and target contact families are each orthogonal but are not jointly
  orthogonal.  Conditional on a valid localization lemma, the safe coefficient
  is therefore `48 epsilon_0`, not `24 epsilon_0`.  This changes the conditional
  prefactor but not `Gamma=312^4`.
- **Unresolved load-bearing gap:** the common near-fixed projections do not by
  themselves localize the global response defect.  The two-frame theorem
  includes complement terms

  ```text
  ||(I-sum G_j)L_sigma psi||,
  ||(I-sum G'_j)L_sigma psi||,
  ```

  while the pullback estimate controls only the unpaired part of a restricted
  near-fixed measure.  It does not control all mass omitted by those sums.
  A localized-response/commutator estimate or a genuine packet-completion
  intertwiner is still required.

The finite-dimensional countermodel

```text
H=C^2,  w=(e1+e2)/sqrt(2),  K e1=e2,  K e2=e1,
G=G'=|e1><e1|
```

has zero global response defect but unit fine-packet error.  It does not
refute a future I3322-specific localization theorem; it refutes the inference
currently used to obtain one.

### Custody and replay -- repairable after the theorem boundary is settled

- The original reconstruction chronology is not externally time-sealed.
- The release verifier now rechecks hashes after full replay and no longer
  claims complete dependency closure or cryptographically sealed blindness.
- The release manifest is intentionally left stale while the mathematical
  claim boundary is under adjudication.  It must be regenerated only after
  the theorem is either repaired or narrowed, and it must include this review
  directory if the review is shipped as part of the release.

## Maximal presently supported statement

The prospective v1.3 package presently supports the constructive upper bound

```text
q_* - Q_d <= exp[-d log R + O(1)]
```

with a dimension-independent `O(1)` term and the documented truncation
witnesses.  The matching universal lower bound and hence
`D(epsilon)=Theta(log(1/epsilon))` remain conditional on the unresolved
near-fixed localization lemma.

## Exit rule

There are only two honest exits:

1. prove the missing localized-response theorem, subject it to a fresh
   isolated reconstruction, and then restore the two-sided claim; or
2. narrow v1.3 to the constructive upper bound and publish the failed
   lower-bound route as an explicit open problem.

Until one exit is completed, v1.3 remains prospective.

## Post-adjudication update

Sprints 1238--1239 tested the first exit rather than assuming it.

- Sprint 1238 proves a weaker coupled-sector theorem: near-fixed mass forces
  either Bell deficit or a fixed amount of complementary drift mass. It keeps
  all four coarse omissions and uses no localized response vector.
- Sprint 1239 kills the proposed terminal shortcut. Even with the I3322
  shared-factor forms and exact coarse sign relations, two zero-error
  response branches can occupy orthogonal multiplicity fibres inside one
  coarse target block.

Consequently the scalar packet architecture is not a path to the missing
theorem under the current hypotheses. A future attempt must retain
operator/Gram provenance or establish a stronger contact-dependent rigidity
theorem. The release decision remains **HOLD**.

## Operator-valued replacement update

Sprints 1240--1259 implement the first option without restoring the claim.
They retain the full Schmidt coefficient operator, replace arbitrary cells by
the complete nested contact flag, and identify the response cocycle with an
exact translation of regularization scale. An exact doppelganger kills
marginal determinant/singular-spectrum closure, while a mixed
flag/Wasserstein distance records the relative response gluing that the scalar
route lost. The filtration now lifts to a positive order-resolution event
measure whose total mass is Schmidt rank; every soft flag is one of its
rectangles. Individual response pushforwards obey a dimension-free
`1/sqrt(t)` stability law.

The response composition, logarithmic boundary bill, and pointwise
order-or-resolution wall are now explicit.  More importantly, the two event
measures are marginals of a canonical positive joint coupling built from the
coefficient operator, so the terminal-fork multiplicity provenance is no
longer selected by hand.  An abstract finite monotone-flow theorem also
closes the rank-only combinatorial gate: paths pay endpoints and fixed points
pay resolution translations.

The charged source descent and coarse quarter wall are now proved. Two hostile
controls reject a direct total-variation or ordinary-Wasserstein completion:
the former is discontinuous on moving atoms and the latter can swap nearby
multiplicity fibres. The complete ordered flag supplies the correctly typed
replacement, and synchronized prefixes recover the entire vertical
translation bill with a linear rank factor. The remaining theorem must show
that the I3322 operator response receipts control those synchronized prefixes
on the canonical joint carrier; it may not infer that fact from marginal
rectangle data or reinstate the retracted localized-response premise.
Until it is proved and independently reconstructed, the release decision and
the maximal public statement are unchanged.
