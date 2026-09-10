# Direct weighted-flow lower proof

Working revision, 2026-09-10. The complete analytic proof is included in
`../../../paper/LOWER-BOUND-REVISION.tex`. It proves the lower half of the
logarithmic dimension law under the paper's critical-storage inputs.

The old paired-block common-return route is not a dependency. In particular,
the argument does not identify vectors in different spectral cells, does not
replace a quantum strategy by a same-dimension scalar carrier, and does not
select one branch while ignoring other weights. The finite spectral universe
has at most 4d labels even when the joint measure has quadratically many cells.

## Development controls

- `check_weighted_flow.py`: exact rational potentials on all directed graphs
  through three vertices, selected larger graphs, and failing hypotheses.
- `check_interfaces.py`: product identities with multiplicity mixing,
  response-ratio orientation, reflection-swap balance, weighted endpoint
  flux, and the strict rounding slack in the eventual upper coefficient.
- `../../../lean/I3322Kernel/I3322Kernel/WeightedFlow.lean`: selected finite
  inequalities and summation identities; see the formalization map below.

These controls are not an asymptotic proof or a final release review.
Earlier blind and integration audits predate the new Lean module and final
editorial changes; they are not independent review of the complete revision.
The public correction precedence is in `../../../paper/REVISION-NOTES.md`.

## Exact formalization boundary

| Analytic proof step | Current machine coverage |
| --- | --- |
| Critical storage, positive weld, compact collar | analytic; finite operator controls only |
| Convex-envelope regularity and monotone predictor | analytic; not Lean-formalized |
| Quantum response to scalar balance, n <= 4d | analytic; orientation/algebra controls only |
| Cycle interval, path separation, SCC decomposition | analytic; finite graph controls only |
| Existence and exponential size of signed potential | analytic; executable finite certificate construction, not a Lean existence theorem |
| Low/high/internal and entering-region edge inequalities | Lean: `low_internal`, `high_internal`, `entering_low` |
| All nonnegative edges contribute | Lean: `all_edges` |
| Sum of edge work equals signed marginal residual | Lean: `balance_identity` |
| Bounded potential implies mass <= B times residual L1 | Lean: `signed_work_bound`, `mass_le_residual`; the potential is a hypothesis |
| Three-way final alternative | Lean: `assembly_alternative`; subsequent asymptotic assembly analytic |
| Weighted endpoint sum and strict coefficient slack | Lean: `weighted_endpoint_payment`, `upper_rounding_slack` |

No `sorry`, new axioms, physical recovery assumption, or uncharged dimension
increase is intended. The full analytic theorem is not formalized; public
release requires explicit author approval.
