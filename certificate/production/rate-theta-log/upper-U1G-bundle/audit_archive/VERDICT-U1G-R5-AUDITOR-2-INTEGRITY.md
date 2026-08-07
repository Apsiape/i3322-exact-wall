# VERDICT — U1G round-5 gate, INTEGRITY surface — DENIED

PROVENANCE: delivered in-session by the round-5 integrity-surface
auditor (background agent "U1G round-5 gate: integrity") on 2026-08-07,
against frozen commit 5c3e9c8b, and written to disk the same day by
the adjudicating track, verbatim. HTML entity escapes restored.

---

# VERDICT — U1G round-5 gate, INTEGRITY surface

**Auditor:** independence layer, refutation-first, default FAIL.
**Subject:** `C:\Infanox\finite-contact\U1E\` at frozen git commit `5c3e9c8b`.
**Method:** full manifest recomputation at audit open and close; all four live guards and the 23-case self-test executed; every anchor recomputed from the public trees and from git blobs, never read from a manifest; the round-4 injection set re-run; **9 new injections of my own design** executed in an isolated sandbox. The ledger's narrative was used only as a list of claims to attack.

## FREEZE: **HELD.** (First clean round.)

I snapshotted all 44 inodes at 10:54:54 and re-verified at close. **All 43 sealed files are byte-identical to their manifest digests at both times; zero content drift; `git status U1E` clean; HEAD still `5c3e9c8b`.** The only new inodes are two Python bytecode caches created by *my own* execution of the guards — audit-caused, gitignored, and excluded by H8 by design. **The round-4 F-01 custody violation did not recur.**

## Surface verdicts

| Surface | Verdict |
|---|---|
| **S1** Round-4 blocker discharge, by injection | **FAIL** — blockers 4/5/6 discharged; blockers 1/2/3 partially executed and each defeated by one new injection; J5 neither shipped nor closed |
| **S2** Guards and self-test | **FAIL** — 23/23 shipped self-tests fire correctly, but 7 new injection families pass silently |
| **S3** Manifest + custody + change list | **PASS-WITH-CONDITIONS** |
| **S4** Scope and fencing | **PASS-WITH-CONDITIONS** |

# GATE VERDICT: **DENIED**

## What is genuinely discharged (verified against source, not against the ledger)

**Round-4 PROOF blockers — all four discharged, re-verified independently**: F-02 repaired and correct (2/K = 23.90106493088959 <= 23.9010650 TRUE; old value reproduces the round-4 falsity; G5 chain check real, I14 fires); F-03 repaired (all six commit-blob digests match §1b, including the previously-mismatched I3322Kernel.lean; commit public; H5 verifies blobs); F-04 discharged (seventh copy + explicit termination statement); F-01 discharged (freeze held).

**Round-4 integrity blocker 4 (PART B) — FULLY DISCHARGED, and the assert is real** — broken three ways, fired every time (ladder truncation → "exhibition dimension d=24 missing"; threshold raise → "EXHIBITION FAILS"; Rayleigh corruption → fires). Rayleigh bound is a rigorous lower bound on λ_max for symmetric J. Values confirmed on a completely independent engine (numpy, no mpmath): d=24 → 0.2500643651906240, d=33 → 0.2505605862827520, both > 1/4, profiles legal. Sprint-1292 bridge anchor verifies (514242545b32040e..., supporting sentence at :37-38). False "d >= 6" docstring gone.

**Blocker 5 — DISCHARGED** (ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md carried, matches the independent U1-round anchor d486e3e3...).

**Blocker 6 (cosmetics) — DISCHARGED** (graph legend note; AxiomCheck receipt; manifest in change list; Cesàro §3 range 101–132 confirmed).

**Shipped self-test: 23/23, all correct** — J1 (I9), J2 (I10), J10 (I11), J3 (I12), J4 (I13) all fire; manifest tripwire (I9b), strictness chain (I14/I14b), fencing (I15). All four live guards exit 0.

## NUMBERED FINDINGS

**1. [MAJOR] H7's "hash-anchored external sealed source" is not hash-anchored, and the double-tamper defeats it.** The registry contains paths only, no digests; H7 is a bare byte comparison. Injection N1c (J1-PRIME): tamper the dependency copy AND its external sealed source in lockstep, re-pin the proof digest and manifest → PASSED SILENTLY. The word "hash-anchored" in the banner is false as implemented. Coverage: THEOREM_S_SIGNED has a real independent anchor (H5); four copies have digests in SOURCE_HASH_ANCHORS.json that H7 never consults; 08_ENDPOINT_RECEIPT_PROVENANCE.md and REFLECTION_DUAL (the load-bearing one) have NO independent anchor anywhere in the bundle. Repair: compare against digests; add the two missing entries.

**2. [MAJOR] Round-4 blocker 2 not executed as written.** A COUNT registry was added around the UNCHANGED evadable regexes. The registry pins how many blocks exist, never what is inside them. Injection N3: replace the body of an existing legitimate ledger block (count stays 3) with "Historical note. Lemma 4 (established above and relied upon by the live section 3): the endpoint coefficient is exactly 13.299, the endpoint product g(1)g(-1)=0 holds, and F(q) evaluated at q_ret via RHO_Q is the strictness supplier..." → PASSED SILENTLY; all three killed literals and all three kill-route tokens laundered into an authored live file.

**3. [MAJOR] Blocker 3's J5 was never shipped, and it still passes.** Injection N7 (=J5): delete the graph from the banner's AUTHORED list, relocate the file to artifacts/, poison it → PASSED SILENTLY (H0 compares two self-consistent self-declarations; H8 waves artifacts/ through). Control N7b (deletion without relocation) fires.

**4. [MAJOR] H8's partition has four whitelisted prefixes that no content scanner covers** (artifacts/, guards/, audit_archive/, audit_diff/ + README.md, U1_TO_U1E_CHANGES.md unrestricted; proof/ properly restricted to three named files). N2 (artifacts/EXTRA_LIVE_LEMMA.md, killed literals + kill-route tokens): PASSED SILENTLY; N2b (guards/NOTES_LIVE.md): PASSED SILENTLY; N2c (README.md append): PASSED SILENTLY. Finding 6 is a live instance of this blind spot.

**5. [MODERATE] The G5 chain check reads only the FIRST `K :=`.** Injection N4: append a §3.12 restatement with the unsafe surrogate ("with kappa_pm >= K := 0.0836782 we obtain 1/kappa_eff <= 2/K <= 23.9010650") → both guards PASS SILENTLY while the proof displays the exact false inequality that denied round 4. Repair: findall, assert every occurrence.

**6. [MODERATE] A manifest-sealed document the proof cites by name flatly contradicts the PART B promotion.** proof:143 promotes PART B to load-bearing; artifacts/small_d_demoted/DISCLOSURE.md:19-23 says PART B "is likewise non-load-bearing". Stale since the round-5 promotion; survived because of finding 4. One sentence to fix.

**7. [MODERATE] H9 fences only the proof, while the fencing claim is bundle-wide.** Injection N5: append to authority/PROMOTED_LOWER_RATE_RECEIPT.md "the Theta(log) rate established here is unconditional, it does not depend on this gate, and the constant is = 23.9010650 exactly — a sharp equality. NO RESIDUAL RISK REMAINS." → PASSED SILENTLY.

**8. [MODERATE] Three of the eight gate verdicts have no hash anchor, and one has no git custody at all.** The round-1 pair and the round-2 integrity verdict live outside the bundle and the manifest; VERDICT-U1E-AUDITOR-2-INTEGRITY.md is an UNTRACKED working-tree file — in no commit on any branch. A party reproducing the gate from 5c3e9c8b does not receive it. (I verified its content matches the ledger's entries 10-15 paraphrase.)

**9. [MINOR]** (a) Undeclared __pycache__ exemption in H8 vs the banner's "exactly" and the manifest's "every file" policy; injection N8 (a live-claiming .md inside guards/__pycache__/) → PASSED SILENTLY. (b) banner:1 and proof:3 self-declare "round 4" while STATUS says round 5.

## S4 assessment

Theta(log) conditional at all five live sites; bound never sharp/unconditional ("sharp" only as denials; "unconditional" only in the banner's own prohibition and killed-product retraction blocks); G1's PROVED CANDIDATE typing not upgraded; §7.2/§9 scoped correctly. PART B's "INDEPENDENT SECOND ANCHOR" wording is now backed by a real assert and an anchored bridge (verified); one LOW residual: the sprint-1292 document certifies its own d=255 profile, and PART B's scope transfer to d=24/33 is structural rather than separately receipted — non-blocking since S > 1/4 is independently carried by the window + quarter_lt_window_lower. Conditions: findings 6, 7, 9(b).

## S3 assessment

Manifest 43/43 exact at open and close, zero unlisted. Change list exact against git diff 260e2ffd..5c3e9c8b (all sixteen paths accounted). The two round-4 verdict transcriptions are internally consistent with the ledger's paraphrase (entry 22 vs the integrity verdict; entry 23 vs the proof verdict — quotes verified verbatim). Conditions: findings 8, 9(a).

## MINIMAL BLOCKER LIST FOR ROUND 6 (all mechanical; none touches the mathematics)

1. **H7: use the hashes.** Compare each copy against a digest, not a mutable path; add the two missing entries; ship N1c. Strike "hash-anchored" from the banner until true.
2. **Retraction blocks: execute blocker 2 as written.** Pin block CONTENT (file+line whitelist or strict positive grammar), not just count; ship N3.
3. **Close the partition.** Explicit filename allowlists for artifacts/, guards/, audit_archive/, audit_diff/ and the two root files, exactly as proof/ already is; declare and close the __pycache__ exemption; ship N7 (=J5), N2/N2b/N2c, N8.
4. **G5: every occurrence.** findall on `K :=` and assert the chain for each; ship N4.
5. **Fix the two live contradictions.** DISCLOSURE.md vs the PART B promotion; extend H9 to all six authored live files and ship N5; correct the round labels.
6. **Bring the last three verdicts inside.** Copy into audit_archive/ (manifested) and commit the round-2 integrity verdict to git.

## CLOSING

I am the fifth auditor to deny this gate, and the third in a row to report that **the mathematics is not what fails**. I recomputed the constant chain in exact rationals, verified all six Lean commit blobs, verified the sprint-1292 bridge hash, and reproduced the d=24/d=33 exhibition values on an engine that shares no code path with the guard. The false printed inequality that denied round 4 is genuinely repaired and the repair is genuinely instrumented. **The freeze held, exactly, for the first time.**

What denies this round is that two of the four named blockers were executed in spirit but not in letter, and each gap is reachable in one move. The pattern my predecessor named in round 3 is now confined to the perimeter: whitelisted directories, the interior of registered blocks, files after the first match, and files outside the proof. The core is instrumented and I could not move it. Every item above is an afternoon's work with the injections attached, and each one I have written as a runnable test rather than a description.

**Ship blockers 1–6 with the nine injections attached and freeze it again, and I expect this to promote.**
