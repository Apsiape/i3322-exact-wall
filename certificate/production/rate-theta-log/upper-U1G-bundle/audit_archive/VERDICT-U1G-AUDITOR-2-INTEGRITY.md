> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1G round-4 gate, INTEGRITY surface

PROVENANCE: delivered in-session by the round-4 integrity-surface
auditor (background agent "U1G round-4 gate: integrity") on 2026-08-07
and written to disk the same day by the adjudicating track, verbatim.
HTML entity escapes from the delivery wrapper (&lt; &gt;) restored to < >.

---

# VERDICT — U1G round-4 gate, INTEGRITY surface

**Auditor:** independent refutation-first integrity surface, round 4.
**Bundle:** `[private-workspace]\U1E\` at git commit `260e2ffd`.
**Method:** every property re-derived from the filesystem, git, and the public trees; every hash recomputed; the Lean `AxiomCheck` replayed; 13 injections of my own design executed. The ledger's narrative was used only as a list of claims to attack.

# GATE VERDICT: **DENIED**

Default FAIL sustained — but the shape of the failure has changed, and that is the finding that matters.

The round-3 structural diagnosis — *"every claim about the bundle is still certified by an instrument whose scope is narrower than the claim"* (`audit_archive/VERDICT-U1F-AUDITOR-2-INTEGRITY.md:82`) — is **no longer universal, and is no longer true of the core**. Provenance, anchors, digits, stamps, custody, and the proof's authority quotations are now genuinely instrumented or independently verifiable, and I verified them. The pattern survives in exactly three places: the dependency-copy content channel, the retraction-block exemption, and — newly introduced this round — the PART B promotion that was built to close a round-3 blocker. Six of my twelve hygiene-guard injections passed silently, plus a seventh against the second-engine guard.

## Surface verdicts

| Surface | Verdict |
|---|---|
| **S1** Round-3 discharge (findings 1–15, blockers 1–9) | **FAIL** — 14/15 findings discharged; finding 5 and blocker 2 broken by injection |
| **S2** Guards and self-test | **FAIL** — 7 injections pass silently; the load-bearing PART B fact carries no assert |
| **S3** Manifest + custody | **PASS-WITH-CONDITIONS** |
| **S4** Scope | **PASS-WITH-CONDITIONS** |

## What is genuinely discharged (verified on disk, against source, not against the ledger)

**Finding 2/3 — full byte-identical sources. DISCHARGED, verified by `cmp`.** All five copies byte-identical to their sealed sources. G1's status line survives intact and is quoted verbatim, un-upgraded, in proof §1c; the graph types it "[source: PROVED CANDIDATE, verified within the promoted v28.1 lower closeout]", not [P]. Finding 11 also discharged (08_ENDPOINT carried and hash-pinned).

**Finding 4 — Cesàro disclaimers by section number. DISCHARGED, and the section numbers are accurate** (§6 at :226 with Sprint-1198 at :261; §9's warning exactly r_A(x_+)=r_B(β) at :507-509; §3's +3 padding at :101; §10 scouts at :513; §13 E1 at :633; consumed §2 flux identity at :84-94). No disclaimer misdescribes its target.

**Finding 7 — H5 parsed and hard-failing. DISCHARGED, broken-tested** (simulated absent tree fires; hash-digit flip fires; no SKIP path in the code).

**Finding 8 — digit agreement. DISCHARGED** across proof/banner/STATUS/guard, with G5 additionally forbidding the down-rounded displays.

**Finding 9 — Theorem-S §14. DISCHARGED** ("G1 is UPSTREAM-SHARED with (S), not independent of it").

**Finding 10 — in-file stamps. DISCHARGED on all six historical documents.**

**Findings 12/13/14/15 — DISCHARGED** (STATUS regenerating-outputs wording; DISCLOSURE.md named by path in README and graph; "four live guards plus the injection self-test"; SOURCE_HASH_ANCHORS note reconciled; |I|+3 conflict flagged).

**Blocker 1 — implemented and fail-capable** (H0 generates the scan set and parses the banner list; the round-3 deletions and additions now fire; selftest 13/13).

**Blocker 8 / B2 — the Lean anchor is real, and I replayed it** (27 theorems, exit 0, standard axioms only; five cited statements match character-for-character; zero sorry/axiom).

**Blocker 4 / B4 — the certificate quotations are verbatim** (all five §1a hashes and the window reproduce).

**Custody (B1) — discharged.** All six gate verdicts on disk; the reconstructed round-2 proof verdict contains A1–A22 and residual blockers 1–6, consistent with the ledger's paraphrase.

## Numbered findings

**1. [MAJOR] The load-bearing PART B exhibition asserts nothing about the fact it was promoted to certify — and its key step is a prose-named, unreceipted supplier.** (a) No assert ties any value to 1/4 — demonstrated: truncating the ladder to d ≤ 6, where every value is below 1/4, still prints ALL PASS, exit 0. (b) The docstring's "exceed the closure ceiling 1/4 from d >= 6" is false on both halves, in a guard whose own rule is "no banner exceeds its code". (c) The Jacobi→Bell bridge is asserted in prose ("the repository's certified sprint-1292 pattern") with no file, no hash — verbatim the defect the bundle disclaims at Cesàro §6. The bridge DOES exist publicly (certificate/production/foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md:15) — an anchoring failure, not a falsehood. Consequence: S > 1/4 is single-anchored (which is sound and alone discharges B3); the "INDEPENDENT SECOND ANCHOR" is claimed in three live documents and established by nothing.

**2. [MAJOR] The dependency-copy content channel is uninstrumented.** "FULL byte-identical" is claimed everywhere and checked only against the proof's own quoted digest (a closed loop). Injection J1 (append a live assertion to the Cesàro copy + re-pin the proof digest) → guard PASSES, all green. Nothing compares any copy to the sealed v28.1 sources. True today by my cmp; no instrument verifies it tomorrow.

**3. [MAJOR] Round-3 blocker 2 not discharged: the retraction-block content validator is evadable in one attempt, and is not applied to dependency copies at all.** Injection J2 ("Historical note. Lemma 4 (established...): the endpoint coefficient is exactly 13.299 and the endpoint product g(1)g(-1)=0 holds...") → guard PASSES ("Historical" satisfies the required regex; "Lemma 4" is not "THEOREM:"). Injection J10 (the self-test's own I3 string, placed in a dependency copy with digest re-pinned) → guard PASSES (blocks in copies are never validated).

**4. [MODERATE] H0's generated scan set is still a hard-coded enumeration of three location patterns, cross-checked only against a list the audited party writes.** Three escapes: J3 (authority/EXTRA_AUTHORITY.txt with killed tokens — the glob is *.md) → PASSES; J4 (supplement/EXTRA_LIVE_LEMMA.md cited by the proof) → PASSES; J5 (delete the graph from the banner list and relocate it) → PASSES. All three are caught by manifest re-verification (which I ran: 38/38, zero unlisted) — but no guard checks the manifest. Tying H0's universe to the manifest closes all three at once.

**5. [MODERATE] PART A's named source is absent from the bundle and unanchored** (ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md survives only as a hash inside two historical files). The verification itself is genuine; the independence claim cannot be checked from the bundle.

**6. [MINOR] Graph legend typing exceeds two sources' own status lines** ([R] applied to the Cesàro source, whose own status is "conditional only on a coarse interior endpoint receipt", and to the truncation source, "Abstract theorem package with a conditional... corollary").

**7. [MINOR] The Lean axiom claim has no receipt in the bundle.** I replayed it and the claim is true — recorded here so the next round does not have to.

**8. [MINOR] Change-list omission and one line-range slip** (MANIFEST_U1E_SHA256.json omitted from the MODIFIED list; Cesàro §3 cited as lines 101–128, runs 101–132).

## S4 assessment

Θ(log) is conditional at every occurrence (proof §8, banner, STATUS, graph ×2, lower receipt — "never earlier, never independently"). 23.9010650 is never sharp and never unconditional; "unconditional" survives only inside retraction blocks describing the killed endpoint product. G1's PROVED CANDIDATE typing is not upgraded anywhere. PART B's promotion is scoped correctly in words; finding 1 is that the instrument does not deliver what the scoped claim asserts. Conditions: findings 1 and 6.

## Minimal blocker list for round 5

1. **H7 — external byte-identity** for every dependency copy against its hash-anchored external path; ship injections J1 and J10. *(Finding 2)*
2. **Retraction blocks**: content validation on copies too; replace the four-alternative forbidden regex with a file+line whitelist or strict positive grammar; ship J2. *(Finding 3)*
3. **H0 universe from the manifest**: banner AUTHORED ∪ COPIES ∪ HISTORICAL must partition all manifest entries; manifest must match the filesystem; ship J3/J4/J5. *(Finding 4)*
4. **PART B — pick one**: (a) assert the d=24/d=33 values > 1/4, anchor the bridge by path+hash, fix the false docstring; or (b) withdraw "INDEPENDENT SECOND ANCHOR"/"load-bearing" and let S > 1/4 rest on the certified window + quarter_lt_window_lower, which is sound and sufficient. *(Finding 1)*
5. **PART A provenance**: carry or hash-anchor ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md, or strike the claim. *(Finding 5)*
6. **Cosmetic, one pass**: graph legend typing; a stored AxiomCheck receipt; manifest in the change list; Cesàro §3 range. *(Findings 6, 7, 8)*

## Closing

Blockers 1, 3, 4, 5, 6, 7, 8 and 9 of round 3 are discharged; blocker 2 is not, and blocker 1 is discharged only within a universe that is still self-declared. Fourteen of fifteen round-3 findings are closed on disk. The mathematics-facing anchors — certificate line quotations, the Lean kernel, the sealed sources, the digit chain — are the strongest surfaces in the bundle and I could not move any of them.

What denies this round is narrow and mechanical: **two content channels (dependency copies, retraction blocks) are still exempt from every instrument, and the one new load-bearing instrument does not assert its load-bearing fact.** The recurring pattern is no longer "every claim"; it is three claims, each with a named, hours-long fix. If round 5 ships blockers 1–4 with the injections attached, I expect this to promote.
