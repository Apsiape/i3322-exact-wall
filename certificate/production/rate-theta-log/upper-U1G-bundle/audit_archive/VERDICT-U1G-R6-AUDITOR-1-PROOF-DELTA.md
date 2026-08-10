> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1G round-6 gate, PROOF surface (DELTA AUDIT) — **PROMOTE CARRIES**

PROVENANCE: delivered in-session by the round-6 proof-surface delta
auditor on 2026-08-07 against frozen commit a52d24aa and written to
disk the same day by the adjudicating track, verbatim (the task
output file was empty — the delivery record is the session
transcript, as with the reconstructed round-2 verdict). HTML entity
escapes restored.

---

# VERDICT — U1G ROUND-6 PROMOTION GATE, PROOF SURFACE (DELTA AUDIT)

**Auditor:** independence layer, refutation-first, default FAIL.
**Frozen subject:** `[private-workspace]\U1E\` at commit `a52d24aa`.
**Predecessor:** round-5 proof surface, **PROMOTE** at `5c3e9c8b`.
**Method:** every constant re-derived from `S_LO` at 140 dps + exact rationals; all 13 anchors recomputed from primary sources (working tree + `git cat-file` blobs); all four guards run; 19 mutations of my own design executed in a scratchpad sandbox copy; the real bundle never written.

## PER-SURFACE VERDICTS

| Surface | Verdict |
|---|---|
| **D1** The proof diff | **PASS** — exactly the three sanctioned changes, nothing else |
| **D2** Recommendation execution | **PASS WITH FINDINGS** — all six items implemented and fail-capable; two ledger-accuracy defects |
| **D3** Spot re-verification | **PASS** — 13/13 anchors, 4/4 guards, freeze byte-identical, fencing unchanged |

## **GATE VERDICT: PROMOTE CARRIES.**

## D1 — THE PROOF DIFF

`git diff 5c3e9c8b a52d24aa -- U1E/proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md` is **9 insertions, 9 deletions, two hunks**, and contains exactly and only: (1) D-01 — `:3` status line, "round 4" → "round 6" with the round-5 PROMOTE recorded; (2) M-01 — `:391` and `:394`, `23.9010649309...` → `23.90106493088...`; (3) M-02 — `:380–395`, `K` → `K_0` in the surrogate's definition and every display, plus one clause of new prose naming the reason. No other line moved. **No custody-class finding.**

**M-01 verified as truncation, not rounding.** `2/K_0 = 40000000000/1673565597 = 23.9010649308895897434010171039623730984...`; `"23.90106493088"` is a strict prefix — truncation, correct. The superseded `"23.9010649309"` is not a prefix — it was a rounding, matching the M-01 diagnosis exactly. Same test passes at `proof:397`.

**§3.7 chain re-verified from scratch, exact rationals + 140 dps:** mu_min = 2001750769003037/10^15 exact; x_max <= 0.9590241 UP OK; x_max² <= 0.9197272 UP OK; kappa >= 0.0836782 DOWN OK; K_0 premise K_0 <= kappa TRUE, slack 7.3730113e-12; K_0/2 = 0.041839139925 >= 0.0418391 TRUE as printed; 2/K_0 = 23.90106493088958974... <= 23.9010650 TRUE as printed; ordering 2/kappa < 2/K_0 <= 23.9010650 TRUE. Root round-trip 0E-139. F-02 reproduces on the old value. The M-02 rename changed no decimal, no inequality, no chain link.

## D2 — RECOMMENDATION EXECUTION

All items implemented; 19 sandbox mutations with the manifest re-pinned (determined-adversary model): B0/B1 baselines pass; X1 (restated unsafe surrogate K_0 := 0.083678) FIRED; X1b (invalid down-round K_0 := 0.0836783, chain still true) FIRED on the premise assert; X2 (false tighter <= 23.9010000) FIRED; X2b (x, 0.9590200) FIRED; X2c (false >= on kappa, 0.0836790) FIRED; X3 (Lean commit → 9999999) FIRED; X3b (repoint to a REAL earlier commit) FIRED; X4 (non-pyc in __pycache__) FIRED; X4b (genuine .pyc) correctly passed (disclosed exclusion behaves as documented); X5 (AI-3 verbatim in proof) FIRED; X5b (AI-3 in banner, bundle-wide H9) FIRED; X6 (revert K_0 → bare K throughout) FIRED — the rename cannot be silently undone.

**Honesty on the unclosable residue.** Five of my own escape attempts pass green: `<` instead of `<=` (X2d), reversed orientation (X2e), a false display in the banner (X2f — G5 is proof-scoped), and three fresh paraphrases — "cannot be improved" (X5c), "optimal and is achieved in the limit" (X5d), "exactly logarithmic, not merely O(log)" (X5e). This is the regress my predecessor named and declined to convert into a blocker; I decline likewise: the actual content is correct on every one (no sharpness sentence, no false display anywhere in the bundle, Theta(log) fenced at all five live sites). The ledger does not claim I-01/I-02 are closed.

## D3 — SPOT RE-VERIFICATION

13/13 anchors MATCH by recomputation (5 certificate; 6 Lean commit blobs at 6e6adb5, which = git ls-remote origin HEAD, contained in origin/main; 2 public-repo). All four guards EXIT=0; selftest 32/32. Freeze holds byte-for-byte: independent recursive digest of all 49 files identical at open and close (86aa7c0ab7c1adabb23c3b8fb908addfd504907d2c451717ab3b7f904cd0b3ad); git clean throughout; manifest 48/48; no .pyc anywhere; zero drift of my own. Theta(log) fencing unchanged at all five live sites; (7.2) still "claiming no sharpness"; "unconditional" appears nowhere in the proof. Verdict shelf: 10 verdicts; the three new faithful copies byte-identical to the blind-batch-v19 originals, which are now git-tracked.

## FINDINGS

**F-01 [LOW — ledger accuracy, OVERCLAIM].** `ledger:352` states M-01 "fixed at all three sites"; `ledger:294` is byte-identical to its 5c3e9c8b text and still reads `2/K = 23.9010649309 <= 23.9010650` — the sole surviving M-01 instance, in the register whose job is to record what was fixed. Inequality true; the self-report inaccurate. Fix: one line.

**F-02 [LOW — notation, incomplete M-02].** `proof:382` still reads "because K appears below only in K/2" while everything below writes K_0 — read literally under the new convention it asserts something false about a compact set. Intent unambiguous; no inequality touched; G5 unaffected (X6 confirms). Fix: K → K_0 twice.

**F-03 [LOW — instrument scope].** The G5 structural range check is proof-scoped; a false display in the banner passes (X2f). Content correct today in every authored file. Fix: scope the ledger sentence or extend the check.

**F-04 [LOW — residual regress; NOT a blocker].** `<`/`>`/reversed orientation escape the structural check (X2d/X2e); paraphrases escape H9 (X5c/d/e). Coverage gaps against future tampering, not defects in the present artifact.

**Zero findings of severity MODERATE or above. Zero mathematical findings. Zero custody findings.**

## WHY THE PROMOTE CARRIES

The commission asked one question: did anything move in the proof that shouldn't have. Nothing did. The diff is nine lines in, nine out — display convention, symbol rename, round label. I rederived the repaired §3.7 chain from S_LO upward in exact rationals without consulting the guard, and it holds with the same numbers, the same inequalities, and 7.4e-12 of slack on the down-round premise. The predecessor's recommended items were not merely gestured at. Thirteen anchors recomputed, four guards green, the freeze byte-identical with no drift from me.

I am the sixth auditor and the fourth on the proof surface to report that the mathematics is sound. **The round-5 PROMOTE carries forward to `a52d24aa`.**

## RECOMMENDED (non-blocking): fix ledger:294 or amend ledger:352; complete the rename at proof:382; scope or extend the "every <=/>= display" claim; if closing further is ever wanted, accept `<`/`>` and reversed orientation into G5 and treat H9 as advisory. Neither should gate promotion.
