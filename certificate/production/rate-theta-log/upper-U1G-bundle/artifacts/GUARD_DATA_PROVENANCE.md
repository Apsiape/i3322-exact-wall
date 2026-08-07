# Small-d guard data provenance

The mechanical guard uses a small exact-decimal excerpt from the public repository fixture

`certificate/production/foundational-sprint-1292/dimension-255-candidate.json`

whose committed profile/vector payload hash is

`e43171241e1e1c464d2b1c1aec888d50407aa9f87f57adcf4eee39954127e093`.

The companion public verifier

`certificate/production/foundational-sprint-1292/exact_dimension_255_lower_bound.py`

reads those committed decimal strings as `fractions.Fraction`, verifies the payload hash, and rigorously certifies the committed 255-dimensional strategy. U1 copies only the entries needed for its `d=3..8` construction guard.

**Claim boundary:** this fixture does not supply the current infinite carrier and is not an input to the analytic rate proof. It is used only to test the finite endpoint-projector construction and parity-resolved small-d behavior.
