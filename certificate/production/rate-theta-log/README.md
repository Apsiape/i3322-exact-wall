# Rate certificates — D(ε) = Θ(log(1/ε)) at local-dimension scope

**Result** (2026-08-07): the dimension complexity of the I3322
quantum value satisfies D(ε) = Θ(log(1/ε)) — reaching S to accuracy
ε requires local Hilbert-space dimension of order log(1/ε), and an
explicit truncation of the attaining carrier achieves it. Existential
constants; the upper half carries the derived safe bound
1/κ_eff ≤ 23.9010650 (no sharpness claimed). The companion note in
`paper/` states and proves the result; this directory is its
certificate root. (Pointer update 2026-08-25: the note has been folded
into the main paper — the result is now Section 5 of
`paper/resolution.tex`; the standalone note is preserved in the frozen
v3.3.0 release. This directory is unchanged.)

## Contents

- `upper-U1G-bundle/` — the upper-bound bundle at its gate-closing
  state. Start at its `PROMOTION_RECORD.md` and `README.md`. It
  contains the fully self-contained proof
  (`proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md`), seven full
  byte-identical dependency copies, four verification guard scripts
  with a 40-case injection self-test, the complete fourteen-verdict
  audit record of its seven-round promotion gate (including every
  denial and the repairs each forced), and frozen-commit custody
  records.
- `lower-v28_1-bundle/` — the sealed lower-bound closeout: the
  five-document certificate chain (`new_docs/00–05`), its dependency
  receipts, guards, and the blind-audit verdicts of its own campaign.

## How to verify

1. Lean cores: `lake env lean AxiomCheck.lean` in
   `lean/I3322Kernel/` — 27 theorems, standard axioms only,
   including the band algebra consumed by the upper proof §3–§4 and
   the three combinatorial cores consumed by the lower chain.
2. Constants: run `upper-U1G-bundle/guards/guard_a8_strictness.py` —
   every displayed decimal is re-derived from its stated inputs in
   exact rational arithmetic and the script fails on any mismatch.
3. Integrity: run
   `upper-U1G-bundle/guards/guard_live_upper_authority_hygiene.py`
   and `guard_selftest_injection.py`. NOTE (disclosed): the bundle's
   manifest pins working-tree digests from the machine of record
   (git line-ending normalization applies; see the bundle README's
   reproducibility note), and the hygiene guard's external-source
   checks reference that machine's repository layout — on a clone,
   verify against `git ls-tree` blob identities instead.

## Provenance notes

- These are faithful copies of the program bundles at their sealed
  states (upper: gate-closing commit recorded in
  `upper-U1G-bundle/PROMOTION_RECORD.md`; lower: the v28.1 closeout
  whose archive hash is quoted in
  `upper-U1G-bundle/authority/PROMOTED_LOWER_RATE_RECEIPT.md`).
- Three audit verdicts in `upper-U1G-bundle/audit_archive/` carry
  disclosed transcription provenance headers (their delivery records
  were session transcripts); each was authenticity-tested by a later
  independent auditor, as recorded in the round-7 verdicts.
- The audit protocol, including its computational disclosure, is
  described in `paper/resolution.tex` (Methods) and summarized in
  the companion note's Section 6.
