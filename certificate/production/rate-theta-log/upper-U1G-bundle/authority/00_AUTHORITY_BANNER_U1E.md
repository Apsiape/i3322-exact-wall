# Authority Banner — U1G — PROMOTED (gate closed at round 7, frozen commit bf47d0b8)

Date: 2026-08-07. Supersedes the U1F banner after the round-3 gate
(DENIED on both surfaces; verdicts ON DISK in audit_archive/, including
the reconstructed round-2 proof verdict). The round-3 proof auditor's
assessment is the commission this bundle executes: "the mathematics is
sound and I could not break it" — every remaining defect was
anchoring, exposition, or audit trail.

CLAIM ON TRIAL: D_upper(eps) = O(log(1/eps)) at local-Hilbert-space-
dimension scope, existential constant 1/kappa_eff, with the derived
safe bound 1/kappa_eff <= 23.9010650 (no sharpness claimed; inherits
the [P] root's disclosed residual risk — see proof §1a; "anchored
uniform bound", never "unconditional"). Theta(log) appears ONLY as the
conditional corollary of proof §8 and promotes only if this gate
passes; nothing in this bundle promotes it independently.

GATE RULE: promotion requires clean PASS verdicts from at least two
independent refutation-first external auditors (proof surface and
integrity surface), adjudicated by the program's audit track under
the frozen blind-before-promotion protocol. Self-audits and worker
stage reports are claims, not verdicts. ALL prior verdicts of this
gate are on disk (index also in STATUS verdicts_on_disk): round 1 —
VERDICT-U1-AUDITOR-1-PROOF.md and VERDICT-U1-AUDITOR-2-INTEGRITY.md
in fsd/papers/i3322-exact-wall/blind-batch-v19/; round 2 —
audit_archive/VERDICT-U1E-AUDITOR-1-PROOF.md (reconstructed from the
session transcript with a disclosed provenance header) and
VERDICT-U1E-AUDITOR-2-INTEGRITY.md in blind-batch-v19; round 3 —
audit_archive/VERDICT-U1F-AUDITOR-1-PROOF.md and
audit_archive/VERDICT-U1F-AUDITOR-2-INTEGRITY.md; round 4 —
audit_archive/VERDICT-U1G-AUDITOR-1-PROOF.md and
audit_archive/VERDICT-U1G-AUDITOR-2-INTEGRITY.md; round 5 —
audit_archive/VERDICT-U1G-R5-AUDITOR-1-PROOF.md (**PROMOTE**, the
first passing surface of this gate, at frozen commit 5c3e9c8b) and
audit_archive/VERDICT-U1G-R5-AUDITOR-2-INTEGRITY.md (DENIED, six
mechanical blockers, executed in this round). The round-1 pair and
the round-2 integrity verdict are now ALSO carried inside the bundle
(round-5 finding 8): audit_archive/VERDICT-U1-AUDITOR-1-PROOF.md,
VERDICT-U1-AUDITOR-2-INTEGRITY.md, VERDICT-U1E-AUDITOR-2-INTEGRITY.md
(faithful copies of the blind-batch-v19 originals, which are
committed to git in the same seal); round 6 —
audit_archive/VERDICT-U1G-R6-AUDITOR-1-PROOF-DELTA.md (PROMOTE
CARRIES) and VERDICT-U1G-R6-AUDITOR-2-INTEGRITY.md; round 7 —
audit_archive/VERDICT-U1G-R7-AUDITOR-1-PROOF-DELTA.md (PROMOTE
CARRIES) and VERDICT-U1G-R7-AUDITOR-2-INTEGRITY.md (**PROMOTE** —
the gate-closing verdict).

FREEZE RULE (standing, adopted per round-4 proof finding F-01, which
correctly identified mid-round edits to the bundle as a gate-integrity
violation): NO WRITE to the bundle between commissioning and verdict.
Each round is commissioned against a stated frozen git commit; every
repair — however small, however directly an auditor requests it —
lands as the NEXT round's content. The round-4 mid-audit edits are
acknowledged in ledger entry 23 as a process violation; their content
was folded into round 5 under this rule.

PROVENANCE MODEL (final, per round-3 findings 2/3/B5 and round-4
findings 2/5; round-4 proof finding F-04): dependencies/ carries
EXACTLY seven FULL byte-identical faithful predecessor copies — zero
extracts, zero additions, zero retraction-block appendices:

  ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md      (sealed v28.1 copy)
  G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md
                                               (sealed v28.1 copy)
  RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md
                                               (sealed v28.1 copy)
  ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md
                                               (sealed v28.1 copy,
                                               upper_artifacts; PART
                                               A's source, round-4
                                               finding 5)
  THEOREM_S_SIGNED_PUBLIC_STATEMENT.md         (public certificate copy)
  08_ENDPOINT_RECEIPT_PROVENANCE.md            (consolidated-bundle copy)
  REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md
                                               (sealed v28.1 copy; the
                                               08 document's family-A
                                               source, round-4 proof
                                               finding F-04; deeper
                                               receipts terminate in
                                               the sealed v28.1
                                               archive at PROMOTED
                                               status — proof §1c)

Each is hash-pinned in the manifest and in proof §1, and each is
verified by the hygiene guard's H7 against a DIGEST REGISTRY pinned in
the guard's own code — copy hash AND external-source hash must both
match the pinned digest, so a lockstep tamper of copy plus source
(round-5 finding 1, injection N1c) fails; changing a digest requires a
guard edit visible to manifest, git, and the gate. Their internal
status-limiting language is PRESERVED IN FULL (that is the point of
full copies); which sections are consumed vs explicitly not consumed
is declared in proof §1c–1e by section number. The superseded U1-era
extracts are stamped and archived in audit_archive/. Public anchors:
repository path + release + DOI + public commits with current content
hashes (proof §1a); the Lean kernel is anchored by public commit +
per-file hashes (proof §1b).

LIVE CHAIN (definitive; the hygiene guard GENERATES its scan set from
this section and cross-checks this exact list — scope-coincidence
rule, ledger entries 15 and 20):

AUTHORED (full killed-literal scan, retraction blocks exempt only
after content validation):
- proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md
- authority/00_AUTHORITY_BANNER_U1E.md
- authority/PROMOTED_LOWER_RATE_RECEIPT.md
- authority/U1E_CORRECTION_LEDGER.md
- authority/U1E_DEPENDENCY_GRAPH.md
- STATUS_U1E.json

COPIES (faithful predecessor content; scanned for killed-IDENTITY
assertions only — historical numeric scouts inside sealed sources are
provenance content, not live assertions; ZERO retraction blocks
permitted in any copy):
- dependencies/*.md (the seven files above)

RETRACTION-BLOCK REGISTRY (round-4 finding 3; round-5 finding 2):
the ONLY legitimate retraction blocks in the live chain are — this
banner: exactly 1; the correction ledger: exactly 3 — and each block's
CONTENT is pinned by the sha256 of its normalized text in the guard's
RB_CONTENT_DIGESTS. Editing the interior of a registered block
(round-5 injection N3), adding a block, or placing one anywhere else
IN THE LIVE CHAIN (authored files and dependency copies), all fail.
Blocks inside HISTORICAL files are outside this registry by design —
they are records of past rounds. Changing a registered block requires
updating the registry in the same commit.

UNSCANNED-BY-DESIGN DISCLOSURE (round-6 finding 2 / blocker 4): the
HISTORICAL files (the three superseded proofs, artifacts/, and the
audit trees) are NOT token-scanned, because they are records that
legitimately QUOTE killed content — every verdict quotes the very
literals it killed. Their bytes are pinned by the manifest and the
filename allowlist, and every modification to them must be accounted
against git diff in the change list at each seal. README.md and
U1_TO_U1E_CHANGES.md, which have no legitimate killed content, ARE
token-scanned (guard H9x). The round-6 E1 injection ships as selftest
I29; the corresponding append-to-historical-file channel is disclosed
here rather than closed, with the change-list-vs-git-diff check as
its control.

PARTITION RULE (round-4 finding 4; round-5 findings 3/4): the
manifest must match the filesystem exactly (sole disclosed exclusion:
*.pyc bytecode), and the COMPLETE bundle file set is pinned as an
explicit filename allowlist in the guard's ALLOWED_FILES — any new,
missing, or relocated file anywhere (including artifacts/, guards/,
the audit trees, or a new directory) fails the gate. Adding a file
requires editing the allowlist in the same commit. H8 re-verifies all
of this on every run.

KILL-ROUTE TOKEN RULE (scope-coincident with the guard's H2): the
kill-#12 route tokens are banned from every AUTHORED live file outside
validated retraction blocks; the proof document must not contain them
at all, in or out of blocks.

HISTORICAL (not live, stamped in-file): proof/
CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md, .../U1E.md, .../U1F.md;
audit_archive/ and audit_diff/ (verdicts, hash anchors, superseded
extracts and self-audits); artifacts/ ([V] non-load-bearing: the
demoted small-d fixture — its PV-padding caveat is in
artifacts/small_d_demoted/DISCLOSURE.md — the commission-history
notes, and the retired retrodiction guard).

STRICTNESS ROUTE (U1G §3, self-contained): single-map label
monotonicity (certificate §10:792 boxed, §6:446 strictly increasing P)
gives both tail limits in the compact interior corridor (G1); the
Jacobi eigen-row limit gives y + 1/y = mu(t_±); the band algebra
D(t) + 2b(t) = s(1-s) <= 1/4 (Lean: band_identity,
s_mul_one_sub_s_le_quarter, band_quarter_ceiling, amplitude_b_le_half,
public commit 6e6adb5) with the certified window S > S_LO > 1/4
(window hash-anchored; the literal comparison Lean:
quarter_lt_window_lower; independent second anchor by PART B
exhibition) forces mu >= 2.001750769003037, so both outward ratios
obey y_± <= 0.9590241 and y_±² <= 0.9197272 < 1; kappa_± >= 0.0836782
per index, kappa_eff >= 0.0418391, 1/kappa_eff <= 23.9010650
(two-sided guard bracket).

RETIRED FROM THE LIVE CHAIN (ledger entries 10, 17): the selected-tail
bracket and its identification, sextic tail-closure, wall-comparison
selection, equality-module, hyperbolicity. Their retirement record and
all quoted retired numerics live in the ledger's marked retraction
blocks and the on-disk verdicts — the U1G proof contains NO retired
numeric and NO retraction block.

RETRACTION-BLOCK-BEGIN — kill declarations (retraction record, not
assertions; carried per ledger entries 1–3): kill #2 — scalar fixed
return does not force neutral gain (not consumed; no neutral-gain step
exists in the live chain). kill #12 — raw-gain substitution into F(q)
is forbidden; this bundle BYPASSES the route entirely (no F(q), no
q_ret, no RHO_Q, no return-sector mechanism anywhere in the U1G
proof); the strictness algebra is the Lean-checked scalar band
ceiling. The unconditional endpoint product g(1)g(-1)=0 remains
KILLED; it appears in authored live files only inside marked
retraction blocks like this one, and in the G1 full source only inside
that source's own §3 kill statement. RETRACTION-BLOCK-END
