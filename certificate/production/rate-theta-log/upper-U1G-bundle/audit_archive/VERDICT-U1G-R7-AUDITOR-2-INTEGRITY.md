> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1G round-7 gate, INTEGRITY surface — **PROMOTE**

PROVENANCE: delivered in-session by the round-7 integrity-surface
auditor on 2026-08-07 against frozen commit bf47d0b8 and written to
disk the same day by the adjudicating track, verbatim (task output
file empty; delivery record is the session transcript). HTML entity
escapes restored.

---

# VERDICT — U1G round-7 gate, INTEGRITY surface

**Auditor:** independence layer, refutation-first, default FAIL.
**Subject:** `[private-workspace]\U1E\` at frozen commit `bf47d0b88f7b0172d7173a1c48658e16447328ab`, U1E tree `27c441445eca5d5ef1fd2728eeb0ef9b3c4ae1f7`.
**Method:** full 50-file manifest recomputation at open and close; all four guards and the shipped selftest executed; all four RB content digests recomputed independently from raw text; the constant chain re-derived at 80 digits; the seven round-6 blockers attacked by injection in a sandbox copy (the real bundle and the real sealed external bundles were never written); **30 injections of my own construction**; and the a52d24aa tree reconstructed from git to test the round-6 transcriptions' authenticity.

## FREEZE: **HELD.** Third clean round in a row.
HEAD, U1E tree hash, and git status identical at open and close. Manifest 50/50 exact at both times, zero mismatches, zero unlisted, zero missing. No .pyc and no __pycache__ anywhere. The guards write nothing — confirmed by byte-identity of the bundle after every run.

## Surface verdicts

| Surface | Verdict |
|---|---|
| **S1** Seven round-6 blockers, by injection | **PASS** — all seven executed as written; every named injection ships and fires for the correct reason |
| **S2** Guards + selftest + own injections | **PASS-WITH-CONDITIONS** — 4/4 guards exit 0; 40/40 selftest; 4/4 RB digests reproduced; recommended items F4–F7, F9 |
| **S3** Manifest + change list | **PASS** — 50/50; zero unlisted; change list exact against git diff |
| **S4** Scope and fencing | **PASS** — proof delta prose-only; the round-6 PROMOTE CARRIES transfers intact |

# GATE VERDICT: **PROMOTE**

## S1 — the seven blockers, item by item

1. **G5 identifier — EXECUTED AS WRITTEN.** Regex character-for-character as specified; V1 verbatim FIRES for the correct reason. The identifier lesson honored: the proof diff is two bare K → K_0 in one safety sentence plus rewrap, nothing else; the guard was WIDENED, not re-narrowed.
2. **Comparison syntaxes — EXECUTED AS WRITTEN.** I26/I27 fire; my own variants (<=, <, ≤, incidentally =<) all fire; the line-break-split display is caught (\s* spans newlines).
3. **mu_min branch — EXECUTED AS WRITTEN.** I28 fires on 2.0017508 vs true 2.001750769003037 — 9th-decimal discrimination. Remaining unbranched ranges calibrated: kappa-upper/rho-lower are the direction that cannot help the claim; S_LO is unpinned (F5) but bounded — inflating it alone yields only visible inconsistency, and the lockstep attack fires on the pinned mu_min token.
4. **N2c — EXECUTED AS WRITTEN; the disclosure is honest and the control is real.** H9x scans README + change list; E1/I29 fires. I RAN the disclosed control: round-6→7 change-list section vs git diff --name-status = 2 ADDED, 9 MODIFIED, exact match on all 11 paths.
5. ***.pyc scoping — EXECUTED AS WRITTEN.** I31 fires; I20 still fires; the residual is the disclosed exclusion itself, vacuous on frozen content.
6. **H10 custody cmp — EXECUTED AS WRITTEN, scope principled** (exactly the three verdicts with independent originals). I30 fires. **The round-6 transcriptions were authenticity-tested, not trusted**: I reconstructed the a52d24aa tree from git and re-ran every checkable claim of the round-6 integrity verdict — manifest 48, selftest 33, the narrowed regex, the ASCII-only findall, zero `K :=` in that proof, and V1–V4 all passing silently against the ACTUAL a52d24aa guard. Every falsifiable assertion reproduced exactly. A transcription that denies its own author and whose every technical claim independently reproduces is not a forgery. Ledger entry 25 corresponds one-to-one with the verdict's blocker list.
7. **Documentation — all four items executed.** Ledger site correct truncation; zero bare K/2 or 2/K in any proof file (all seven surviving K tokens are §2's compact set); 40 PASS lines = 40 case ids = both claim sites; RB sentence scoped, and the live chain carries exactly the 4 registered blocks.

## S2 — core verification

4/4 guards exit 0. 40/40 selftest. 4/4 RB digests reproduced from raw text. All seven shipped injections traced to the specific assert each trips. Independent false-display sweep at 80 digits across all six authored live files plus README and the change list, including phrase and LaTeX channels G5 cannot see — 49 decimals in tracked ranges examined:

> ### FALSE DISPLAYS IN THE FROZEN LIVE CHAIN: **0**

## S4 — scope

Proof diff prose-only; round-6 PROMOTE CARRIES transfers intact. Theta(log) at four live sites, all conditional; §8 iff-fenced; "unconditional" never on the bound; "sharp" only as denials; G1 remains PROVED CANDIDATE, not upgraded.

## NUMBERED FINDINGS (all RECOMMENDED; none blocking)

**F1. [MODERATE]** README.md materially stale about the bundle's own structure ("fourth gate round"; "five copies" twice vs seven; "six verdicts, rounds 1–3" vs twelve, rounds 1–6; "four live guards"; "round-3 injection set" vs rounds 3–6). Not a blocker: unmodified this seal, inherited debt unflagged by six prior auditors, every error UNDERSTATES, banner/STATUS/ledger/guard-output are exhaustive and correct, and README defers to the banner. **Fix before anyone outside the program reads the bundle.**
**F2. [MINOR]** Stale round labels: banner line 1 "round 6"; manifest "round-6 gate". STATUS correct.
**F3. [MINOR]** Banner verdict shelf enumerates rounds 1–5, omitting the round-6 pair (on disk, manifested; STATUS indexes all twelve correctly). Enumeration stale only.
**F4. [MODERATE]** G5's identifier regex is whitespace-exact (double space, no space, tab, bold markers, bare = all evade). Brittleness inherited from the blocker's literal specification; the frozen proof contains exactly one K_0 :=, in the safe form.
**F5. [LOW–MODERATE]** The proof's S_LO display is not pinned to the guard's own constant; bounded by the pinned mu_min token (lockstep attack fires; solo attack yields only visible inconsistency).
**F6. [LOW]** Unbranched structural ranges — all in the direction that cannot make the bound look better.
**F7. [LOW]** Comparison-syntax ceiling (LaTeX \le, &le;, U+2A7D, natural language). Inherent to symbol scanning; never named by any blocker.
**F8. [LOW]** Verdict custody beyond H10's three rests on git alone (all twelve git-tracked at bf47d0b8; rounds commissioned against frozen commits; no guard enforces it).
**F9. [LOW–MODERATE, new class]** core.autocrlf=true: the manifest pins CRLF working-tree digests, not git blob digests — an external auditor cloning with autocrlf=false gets 50/50 mismatch and H8 hard-fails. The bundle is not reproducible from git alone and neither the manifest policy nor the banner discloses this. No laundering channel (normalization uniform, cannot carry semantic content); the chain verifies exactly on the machine of record. **Fix before an external party verifies the seal from a clone.**
**F10. [INFORMATIONAL]** Three descriptions say "sole disclosed exclusion: *.pyc bytecode" without the __pycache__ qualifier the code now enforces. Safe direction: code stricter than advertised.

## CALIBRATION — why this promotes

I applied my predecessor's own standard. All seven blockers were executed as written — checked against the literal text, each named injection run, each firing for the right reason. The mechanism that cost round 6 was not repeated. Of my thirty injections, every one either fired, fell inside a disclosed channel whose control I ran and verified exact, or is a latent tripwire gap in a direction that cannot strengthen the claim. The two findings with teeth (F4, F5) are both bounded. Nothing I found touches the claim on trial, and my independent 80-digit sweep through the channels G5 is blind to found zero false displays.

I am the seventh auditor on this gate and the fifth in a row to report that the mathematics is not what fails. Two proof-surface PROMOTEs stand at 5c3e9c8b and a52d24aa, and I confirmed the delta since carries no mathematical content. The perimeter still has holes, all named above and none load-bearing; **the core is clean, and I could not move it.**

**PROMOTE.** F1 is the one item to fix before this bundle is read outside the program; F9 before an external party verifies the seal from a clone.
