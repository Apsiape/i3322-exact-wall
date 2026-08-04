# v1.1.0 release notes

This release preserves the archived `v1.0.0` exact-wall theorem and its
certificate stack. It adds consequences and corrects the priority record.

## New theorem

- `C_q(3,3;2,2)` is not closed.
- If either party has at most two binary inputs, the corresponding
  finite-dimensional quantum correlation set is compact.
- Therefore the `3 x 3` binary-output scenario is minimal, in the
  coordinatewise ordering of input counts, for finite-dimensional quantum
  nonclosure.

The compactness proof is independent of the computer-assisted I3322
certificate. It uses a common dilation of two binary POVMs, Jordan's lemma,
Schmidt compression, and Caratheodory's theorem. The nonclosure implication
then uses only the archived maximizing sequence and finite-dimensional
nonattainment theorem.

## Priority correction

The original search missed Nidhal Mghirbi's July 2026 Zenodo release,
`10.5281/zenodo.21477901`, which predates `v1.0.0` and gives a proof-carrying
exact rational enclosure of the I3322 value with width below `10^-9`.

That work does not determine the exact supremum, finite-dimensional
attainment, or tensor--commuting equality. The present theorem therefore
remains distinct, but it is not the first proof-carrying exact I3322 bound.
The manuscript, README, and priority audit now credit this antecedent
explicitly.

Dykema, Paulsen, and Prakash had also explicitly observed in 2018 that the
conjectured I3322 nonattainment would imply nonclosure of `C_q(3,2)`. The new
corollary closes that known conjectural route; it does not claim priority for
the implication itself or for general nonclosure.

## Verification

The complete release verifier checks every frozen file and replays the full
production and independent certificate stacks. The new compactness and
minimality argument is analytic and introduces no additional computational
dependency.
