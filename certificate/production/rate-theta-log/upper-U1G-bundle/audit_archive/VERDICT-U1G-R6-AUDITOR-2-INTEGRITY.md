> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1G round-6 gate, INTEGRITY surface — DENIED (narrowest)

PROVENANCE: delivered in-session by the round-6 integrity-surface
auditor on 2026-08-07 against frozen commit a52d24aa and written to
disk the same day by the adjudicating track, verbatim (the task
output file was empty — the delivery record is the session
transcript). HTML entity escapes restored.

---

# VERDICT — U1G round-6 gate, INTEGRITY surface

**Auditor:** independence layer, refutation-first, default FAIL.
**Subject:** `[private-workspace]\U1E\` at frozen commit `a52d24aa02ecb502d0b4a714860a88f8c3243c34`, U1E tree `f2d0b06ed2e95a47861bdea46cbb91634ef64d02`.
**Method:** full 48-file manifest recomputation at open and close; all four live guards and the shipped selftest executed; all four RB block digests recomputed independently from source text; the six round-5 blockers attacked by injection in a sandbox copy (real bundle and real sealed external bundles never written); **19 injections of my own construction** beyond the shipped set.

## FREEZE: **HELD.** Second clean round in a row. HEAD, U1E tree hash, git status identical at open and close; manifest 48/48 exact at both times; no __pycache__ anywhere, so the disclosed *.pyc exclusion is vacuous on the frozen content.

## Surface verdicts

| Surface | Verdict |
|---|---|
| **S1** Six round-5 blockers, by injection | **FAIL** — blockers 1, 2, 5, 6 fully discharged and robust under novel variants; blocker 3 has one attached injection neither shipped nor closed; blocker 4 not executed as written and partially regressed by this round's own rename |
| **S2** Guards + selftest | **PASS-WITH-CONDITIONS** — 4/4 guards exit 0; 33/33 selftest cases; 4/4 RB digests independently reproduced |
| **S3** Manifest + change list | **PASS** |
| **S4** Scope and fencing | **PASS** |

# GATE VERDICT: **DENIED** — the narrowest denial this gate has received; every blocker is a one-line edit, and nothing found touches the claim on trial.

## Genuinely discharged (verified against source and by injection)

**Blocker 1 (H7 digest registry): FULLY DISCHARGED, stronger than asked** — EXPECTED_DIGESTS pins all 7 copies including the two previously unanchored; copy AND source checked. My T1 (tamper copy + re-pin proof digest + manifest + THE GUARD'S OWN REGISTRY) still FIRED via the independent external root; T2 (new authority file + ALLOWED_FILES edited to admit it) fired on H0. Banner wording now accurate.

**Blocker 2 (RB content pinning): FULLY DISCHARGED** — all four normalized-content sha256 recomputed independently, 4/4 MATCH; I17 fires; five of my own variants all fire (cross-file swap, in-file reorder, in-block append, stray unmatched BEGIN marker engineered to swallow live text, block planted in STATUS). I could not launder anything through this.

**Blocker 5: DISCHARGED** — DISCLOSURE.md now agrees precisely with the PART B promotion; H9 bundle-wide (6/6 files fire on the N5 text); round labels correct.

**Blocker 6: FULLY DISCHARGED** — ten verdicts inside, manifested; three early copies cmp-clean vs originals (git hash-object agrees on original/working/copy); originals git-tracked at a52d24aa; reconstructed round-2 verdict blob unchanged across 260e2ffd, 5c3e9c8b, a52d24aa.

**Blocker 3 (stated repair): fully executed** — ALLOWED_FILES pins all 48; I18/I19/I20 fire; my case-variation rename and shadow-directory escapes fire; the new-file/relocation family is closed.

## NUMBERED FINDINGS

**1. [MAJOR] Blocker 4 not executed as written; the same seal's rename re-opened the hole.** The blocker said findall on `K :=`; the implementation reads `K_0 :=` — narrowed to the renamed identifier in the same seal. V1 (the round-5 N4 text VERBATIM, `K :=` form, displaying `2/K <= 23.9010650` with 2/0.0836782 = 23.9010877...) → PASSED SILENTLY on both guards. Not present in the frozen document (no `K :=` exists in the proof) — a missing tripwire, not a live falsity — but it is the one thing this surface exists to check, on the one blocker that names it.

**2. [MODERATE] Blocker 3's attached injection N2c neither shipped nor closed nor disclosed.** A filename allowlist cannot close an append to an already-allowed file: E1 (README.md), E2 (U1_TO_U1E_CHANGES.md), E7 (historical U1F proof) all PASSED SILENTLY with killed literals, kill-route tokens, and unfencing text. Mitigating: all are HISTORICAL/non-live by the banner's definition. The repair was executed and the injection dropped silently instead of disclosed.

**3. [MODERATE] An archived verdict can be rewritten silently — compensating control exists and I exercised it.** E3 (rewrite an archived verdict DENIED→PROMOTE, re-pin manifest) PASSED SILENTLY; no guard cross-checks archived verdicts against originals. LOW in practice only because blocker 6 landed: the originals are git-tracked and byte-comparable, which is the check I ran. Worth one cmp in the guard.

**4. [MODERATE] The structural range check is defeated by one character.** V2: strict `<` instead of `<=` with false values → PASSED SILENTLY. Latent only.

**5. [MODERATE] Same check, defeated by Unicode.** V3: `≤` → PASSED SILENTLY. The proof already carries Unicode; not exotic. Latent only.

**6. [MODERATE] A tracked constant sits in an untracked range.** No mu_min branch: V4 (`mu >= 2.0017508`, false) → PASSED SILENTLY. Controls V5/V6 inside tracked windows fired, so the mechanism is sound where wired.

**7. [LOW] The *.pyc exclusion is global, not __pycache__-scoped, and the guard's own comment says otherwise.** E4 (`authority/LIVE_CLAIM.pyc` with killed literals) → PASSED SILENTLY, invisible to manifest and allowlist. Disclosed at policy level; the banner's "any new file anywhere" overstates. I20 tests only the __pycache__ case.

**8. [LOW] H9 is a phrase blacklist; paraphrases pass** ("no hypotheses whatsoever... independent of the outcome of any gate; the constant cannot be improved") → PASSED SILENTLY. Inherent ceiling, never asked for by any blocker; recorded, not a defect.

**9. [MINOR] Four documentation residuals.** (a) ledger:294 still `2/K = 23.9010649309 <= 23.9010650` — a fourth M-01 site (round-UP, not truncation; bare equality wrong in its last digit) and un-renamed K, in an authored live file, while entry 24 claims "fixed at all three sites". (b) proof:382 M-02 rename incomplete (bare K/K/2 in the safety sentence). (c) ledger:358 says "32 cases"; the selftest executes 33. (d) banner "placed anywhere else ... all fail" overreaches — four blocks exist in historical files outside the registry; the governing "in the live chain" clause makes it defensible but the sentence overreaches.

## Calibration — what the residuals touch

**Nothing above touches the claim on trial. Tested directly:** I scanned all six authored live files for every numeric display under all six comparison symbols (<=, <, ≤, >=, >, ≥) against 60-digit true values of mu, x, rho, kappa, kappa_eff, 1/kappa_eff, including the four channels G5 is blind to:

> **FALSE DISPLAYS IN THE FROZEN LIVE CHAIN: 0**

Findings 1 and 4–6 are missing tripwires against future edits, not live falsities. Findings 2, 3, 7 live in files the banner declares non-live, or behind a disclosed exclusion. The perimeter has holes; **the core is clean and I could not move it.**

## S4 — PASS. Theta(log) at exactly four live sites + STATUS, every one conditional. "unconditional" three times, never on the bound (the prohibition itself + two registered kill blocks). "sharp" only as denials. G1 typing not upgraded. **The proof diff 5c3e9c8b→a52d24aa contains no mathematical content change — confirmed exhaustively** (18 lines: D-01, M-02, M-01; M-01 verified a pure convention fix). **The round-5 PROOF-surface PROMOTE transfers intact.**

## S3 — PASS. Manifest 48/48 at open and close; change list exact against git diff (5 ADDED, 10 MODIFIED, all 15 paths accounted).

## MINIMAL BLOCKER LIST FOR ROUND 7 (all mechanical)

1. G5: `re.findall(r"\bK(?:_0)? := ...")` — ship V1.
2. G5: accept `(?:<=|<|≤)` and `(?:>=|>|≥)` — ship V2, V3.
3. G5: add the mu_min range branch — ship V4.
4. Close or disclose N2c — extend the token scan to the scannable allowed files or state the design; ship E1 either way.
5. Scope the *.pyc exclusion to `__pycache__/` — ship E4.
6. Add a custody cmp for the three archived early-round verdicts — ship E3.
7. Documentation: ledger:294, proof:382, "32→33 cases", RB sentence scope.

## CLOSING

I am the sixth auditor to deny this gate and the fourth in a row to report that the mathematics is not what fails. I re-derived the constant chain at 60 digits, recomputed all 48 manifest digests twice, reproduced all four RB content digests from raw text, verified all ten verdicts' custody in git and by byte comparison, and confirmed the only changes since the round-5 PROMOTE are a display convention, a rename, and a label.

What denies this round: blocker 4 was executed against a renamed identifier introduced in the same seal, so the exact injection it was written to close still passes; and blocker 3's attached injection N2c was dropped rather than shipped or disclosed. Everything else is discharged, several items more robustly than requested — I attacked H7 and the RB registry with nine variants of my own design and could not break either.

The gap between this bundle and promotion is now three regex edits, two scan-set decisions, and a cmp. Ship items 1–7 with V1, V2, V3, V4, E1, E3, E4 attached as selftest cases, freeze it again, and I expect this to promote — and unlike my predecessor I will add: **do not change any identifier in the same seal that hardens a guard against it.** That is the specific mechanism that cost this round.
