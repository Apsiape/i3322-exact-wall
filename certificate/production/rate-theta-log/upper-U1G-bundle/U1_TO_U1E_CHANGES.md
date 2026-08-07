# U1 → U1E complete change list

Both trees are committed to the program repository (U1 at ingest
commit ed23e196; U1E at its own commit), so the exact unified diff of
every file is available via `git diff <U1-commit> <U1E-commit> -- U1
U1E` and is not duplicated here. File-level enumeration:

ADDED
- proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1E.md   (the live proof; R1A-R4)
- proof/CESARO_MULTIPLIER_IDENTIFICATION_TWO_ROUTES.md (R1A both
  routes + retrodiction, retraction-blocked numerics)
- authority/00_AUTHORITY_BANNER_U1E.md        (replaces U1 banner)
- authority/U1E_CORRECTION_LEDGER.md          (replaces U1 ledger;
  kills #2/#12 carried; G1-extract entry; R1-R5 entries)
- authority/U1E_DEPENDENCY_GRAPH.md           (replaces U1 graph;
  spurious S→G1 edge removed; S>1/4 non-consumption stated)
- STATUS_U1E.json                             (replaces STATUS_U1;
  gate rule stated; no sealed regenerating outputs)
- guards/guard_kappa_bracket_retrodiction.py  (new)
- guards/guard_second_engine_projectors.py    (adopted external
  second engine, unchanged from its committed source)
- guards/guard_live_upper_authority_hygiene.py (REWRITTEN: live-chain
  scope, retraction-block exemption, fail-capable, real predecessor
  check when the public tree is present)
- artifacts/small_d_demoted/DISCLOSURE.md     (new)
- U1_TO_U1E_CHANGES.md                        (this file)

MOVED (demotion, contents unchanged)
- guards/guard_small_d_endpoint_projector_truncation.py,
  small_d_endpoint_projector_truncation_results.json,
  SMALL_D_TRUNCATION_SOURCE_DATA.json, GUARD_SMALL_D_STDOUT.txt
  → artifacts/small_d_demoted/

MODIFIED
- dependencies/G1_PROMOTED_UPPER_RECEIPT.md   (retraction notice
  RESTORED in a marked block; no other change)

RETAINED UNCHANGED
- proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md    (historical, superseded)
- dependencies/{DISTORTED_RETURN_QUARTER_CEILING_CURRENT_V22,
  ENDPOINT_CESARO_UPPER_RECEIPT, TRUNCATION_UPPER_RECEIPT,
  THEOREM_S_SIGNED_PUBLIC_STATEMENT, PROMOTED_LOWER_RATE_RECEIPT (in
  authority/)}.md
- audit_archive/SOURCE_HASH_ANCHORS.json, audit_diff/*,
  artifacts/GUARD_DATA_PROVENANCE.md, guards/U1_GUARD_RESULTS.txt
  (historical records of the U1 round)
- README.md (U1-era; superseded by the banner for authority purposes)

DELETED
- proof/U1B_HYGIENE.txt        (unbacked banner file; gate F19)
- I3322_U1_UPPER_GATE_MANIFEST_SHA256.json (superseded by the U1E
  manifest, which excludes regenerating outputs)

# U1E → U1F change list (2026-08-07, post-U1E-gate)

ADDED: proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1F.md (live proof, A8
route); guards/guard_a8_strictness.py;
dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md (FULL source,
faithful copy from the sealed v28.1 bundle);
artifacts/commission_history/ (relocated two-routes note);
audit_archive/SELF_AUDIT_U1.SUPERSEDED.md and
U1_GUARD_RESULTS.HISTORICAL.txt (relocated with stamps).
MODIFIED: proof/...U1E.md (supersession header; §§4-7 live by
incorporation); banner (live-chain definition, provenance model,
strictness route); ledger (entries 10-15); dependency graph (U1F
correction section); STATUS (gate history, strictness route);
hygiene guard (scope-coincidence LIVE list, two-tier scan, U1F
tokens, new proof-doc hash 090aeceb..., whitespace-normalized
matching); README (rewritten).
REMOVED: dependencies/ENDPOINT_CESARO_UPPER_RECEIPT.md (lossy
extract, replaced by full source); guards/__pycache__/ (orphan);
SELF_AUDIT_U1.md and guards/U1_GUARD_RESULTS.txt from their old
locations (relocated, above).
PUBLIC REPO: certificate proof-doc header reconciled to PROMOTED
v3.1.0 with the §§6-9 residual-risk note (commit e50bfec); manifest
refreshed; new hash 090aecebe7d5c1502bbe93961e40821179cc9a4c592de841316a33a4871a4141.

# U1F → U1G change list (2026-08-07, post-round-3 gate, both DENIED)

ADDED
- proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md   (the live proof, fully
  self-contained; ledger entry 17)
- audit_archive/VERDICT-U1E-AUDITOR-1-PROOF.md (round-2 proof verdict
  RECONSTRUCTED from the session transcript, provenance header inside;
  ledger entry 16)
- audit_archive/VERDICT-U1F-AUDITOR-1-PROOF.md and
  VERDICT-U1F-AUDITOR-2-INTEGRITY.md          (round-3 verdicts,
  written to disk the day delivered)
- dependencies/G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md
  (FULL sealed v28.1 copy, byte-identical, cmp-verified)
- dependencies/RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md
  (FULL sealed v28.1 copy, byte-identical, cmp-verified)
- dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md (consolidated-bundle
  copy; G1 endpoint-reserve provenance, round-3 finding 11)
- guards/guard_selftest_injection.py          (injection self-test,
  round-3 integrity blocker 1)

MOVED (each with an in-file stamp; ledger entries 19, 21)
- dependencies/G1_PROMOTED_UPPER_RECEIPT.md
  -> audit_archive/G1_PROMOTED_UPPER_RECEIPT.EXTRACT.SUPERSEDED.md
- dependencies/TRUNCATION_UPPER_RECEIPT.md
  -> audit_archive/TRUNCATION_UPPER_RECEIPT.EXTRACT.SUPERSEDED.md
- dependencies/DISTORTED_RETURN_QUARTER_CEILING_CURRENT_V22.md
  -> audit_archive/DISTORTED_RETURN_QUARTER_CEILING_CURRENT_V22
     .KILL_PROVENANCE.md   (dependencies/ = consumed sources only)
- guards/guard_kappa_bracket_retrodiction.py
  -> artifacts/commission_history/guard_kappa_bracket_retrodiction
     .RETIRED.py           (consumes a retired authority; F20)

MODIFIED
- proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md, ...U1E.md, ...U1F.md:
  in-file SUPERSEDED/gate-DENIED stamps (round-3 finding 10); U1E's
  §§4-7 are no longer live-by-incorporation (fully historical)
- audit_archive/SELF_AUDIT_U1.SUPERSEDED.md and
  U1_GUARD_RESULTS.HISTORICAL.txt: in-file stamps added
- authority/00_AUTHORITY_BANNER_U1E.md: rewritten for U1G (parseable
  LIVE CHAIN list; five-full-copy provenance model; verdict index)
- authority/U1E_CORRECTION_LEDGER.md: kill-declaration entries 2/10
  wrapped in retraction blocks; entries 16-21 appended
- authority/U1E_DEPENDENCY_GRAPH.md: rewritten clean (S-§14
  correction; Lean + PART B nodes; retired list)
- authority/PROMOTED_LOWER_RATE_RECEIPT.md: stale "if U1 promotes"
  wording made gate-neutral (round-3 integrity finding 1, staleness)
- STATUS_U1E.json: U1G round; verdict index; corrected
  regenerating-outputs sentence (finding 12); Lean anchor field
- guards/guard_a8_strictness.py: two-sided 1/kappa_eff bracket (F6);
  x bracket; display-concordance check G5 (finding 8)
- guards/guard_live_upper_authority_hygiene.py: REWRITTEN — H0
  generated-scan-set coincidence check, content-validated retraction
  blocks, H2 over all authored files, H5 parsed anchors + hard-fail,
  H6 dangling pointers
- audit_archive/SOURCE_HASH_ANCHORS.json: note reconciled with the
  full-copy provenance model (finding 14)
- README.md: rewritten (four guards + self-test; verdict shelf)
- U1_TO_U1E_CHANGES.md: this section

PUBLIC REPO (commit 6e6adb5, pushed): lean/I3322Kernel — RateCores
module committed (was untracked); band algebra added (band_identity,
s_mul_one_sub_s_le_quarter, band_quarter_ceiling, amplitude_b_le_half);
AxiomCheck extended to all 27 theorems; root module import committed.

# U1G round-4 -> round-5 change list (2026-08-07)

ADDED: dependencies/ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md
(SIXTH full copy, byte-identical to sealed v28.1 upper_artifacts,
matches U1-round anchor d486e3e3...);
audit_archive/VERDICT-U1G-AUDITOR-2-INTEGRITY.md and
VERDICT-U1G-AUDITOR-1-PROOF.md (round-4 verdicts);
audit_archive/AXIOMCHECK_RECEIPT_2026-08-07.txt.
MODIFIED: proof section 1b (PART B assert + sprint-1292 bridge anchor
by path+hash), 1d (Cesaro section-3 range 101-132), 1e (sixth copy);
guard_second_engine_projectors.py (load-bearing exhibition assert at
d=24/33; docstring corrected); hygiene guard (H7 external
byte-identity registry, H8 manifest partition, RB registry by file
and count incl. zero-in-copies); selftest (manifest-aware copies,
per-mutation rehash, injections I9-I13 = the round-4 auditor's
J1/J2/J10/J3/J4); banner (six copies, RB registry, partition rule);
graph (legend conditional-typing, sixth copy node); ledger (round-4
section + entry 22); STATUS (round 5); this file; and
MANIFEST_U1E_SHA256.json (regenerated — round-4 finding 8: the
manifest is itself a tracked modification in every round).

# Round-4 PROOF-verdict execution (2026-08-07, same round-5 seal)

ADDED: dependencies/REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS
.md (SEVENTH full copy, sealed v28.1, sha 589bb7d8...; F-04);
audit_archive/VERDICT-U1G-AUDITOR-1-PROOF.md (round-4 proof verdict).
MODIFIED: proof 3.7 (K := 0.08367827985 repairing the F-02 false
inequality, rounding-direction logic stated), 1b (COMMIT-BLOB hashes,
git cat-file verification command; F-03), 1a(iv) (d(x,u) receipt
cited by file+line and hash-anchored, sprint-1197), 1c (seventh copy
+ termination statement; F-04); a8 guard (G5 chain check parsing the
displayed K); hygiene guard (H5 Lean via git cat-file at 6e6adb5;
pub-repo anchors 2; copies 7; H9 fencing phrases); second-engine
guard (Rayleigh-quotient rigorous lower bound in the exhibition
assert; F-05(i)); selftest (I14/I14b strictness chain, I15 fencing);
banner (FREEZE RULE standing; seven copies; round-4 verdict paths);
ledger (entry 23); STATUS; this file; manifest regenerated at seal.

# Round-5 -> round-6 change list (2026-08-07)

ADDED: audit_archive/VERDICT-U1G-R5-AUDITOR-{1-PROOF,2-INTEGRITY}.md
(round-5 verdicts, PROOF = PROMOTE); audit_archive/VERDICT-U1-AUDITOR-
{1-PROOF,2-INTEGRITY}.md and VERDICT-U1E-AUDITOR-2-INTEGRITY.md
(faithful copies of the blind-batch-v19 originals, which are
git-committed in this seal; round-5 finding 8).
MODIFIED: proof (M-01 display convention; M-02 K -> K_0; D-01 round
label; no mathematical content change); DISCLOSURE.md (finding-6
contradiction resolved); hygiene guard (H7 digest registry, RB
content digests, H8 full filename allowlist + *.pyc-only disclosed
exclusion, H9 bundle-wide + AI-3 phrases, H5 commit-id parsing); a8
guard (G5 every-occurrence + structural range check); selftest
(I16-I24; rehash filter aligned; 32 cases); banner (round 6; H7/RB/
partition wording matched to implementation; verdict shelf); ledger
(round-5 section + entry 24); STATUS; this file; manifest regenerated
at seal.

# Round-6 -> round-7 change list (2026-08-07)

ADDED: audit_archive/VERDICT-U1G-R6-AUDITOR-1-PROOF-DELTA.md and
VERDICT-U1G-R6-AUDITOR-2-INTEGRITY.md (round-6 verdicts).
MODIFIED: proof (section 3.7 prose rename completion ONLY - two bare
K -> K_0 in one sentence; no display, no inequality, no chain link
changed); ledger (entry-23 M-01 fourth-site fix; entry-24 count
correction; entry 25); banner (RB sentence scoped; unscanned-by-
design disclosure); a8 guard (G5 identifier + comparison-syntax +
mu_min branch); hygiene guard (scoped *.pyc exclusion; H9x extended
token scan; H10 custody cmp); selftest (I25-I31; rehash filter
aligned; 40 cases); STATUS; this file; manifest regenerated at seal.

# Round-7 PROMOTION commit (2026-08-07)

ADDED: PROMOTION_RECORD.md; audit_archive/VERDICT-U1G-R7-AUDITOR-
{1-PROOF-DELTA,2-INTEGRITY}.md (round-7 verdicts; PROMOTE both).
MODIFIED: README.md (F1 accuracy rewrite + F9/F10 disclosures);
banner (F2 header, F3 verdict shelf); STATUS (PROMOTED; theta fired);
ledger (round-7 section + entry 26); this file; manifest regenerated.
The PROOF is UNTOUCHED in this commit — the promoted document is
byte-identical to the round-7 gated blob.
