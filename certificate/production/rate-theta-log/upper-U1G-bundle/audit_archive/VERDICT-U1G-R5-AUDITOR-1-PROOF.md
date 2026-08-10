> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1G round-5 gate, PROOF surface — **PROMOTE**

PROVENANCE: delivered in-session by the round-5 proof-surface auditor
(background agent "U1G round-5 gate: proof") on 2026-08-07, against
frozen commit 5c3e9c8b, and written to disk the same day by the
adjudicating track, verbatim. HTML entity escapes restored.

---

# VERDICT — U1G ROUND-5 PROMOTION GATE, PROOF SURFACE

**Auditor:** independence layer, refutation-first, default FAIL.
**Frozen subject:** `[private-workspace]\U1E\` at commit `5c3e9c8b`.
**Method:** every hash recomputed from primary sources (commit blobs and sealed originals, never from the manifest); every constant re-derived from scratch at 140 digits plus exact rationals, never read from a guard; all four guards run by me; the Lean receipt re-verified against the committed blobs rather than trusted; six fault injections of my own design.

## FREEZE VERIFICATION — the item that killed round 4

The bundle did not move. I snapshotted all 44 files at session start, mid-audit, and at close:

- `git log --oneline -1 -- U1E` → `5c3e9c8b`, identical at open and close; `HEAD` = `5c3e9c8b`; `git status --porcelain -- U1E` empty throughout.
- Manifest recomputed independently: **43/43 entries match, zero mismatches, zero unmanifested files, exact partition** (43 entries + the manifest = 44 files on disk).
- Byte-level diff of the full file set, session start vs. session end: **identical**.

One drift event occurred and it was **mine**: my `importlib` probe of the hygiene guard wrote `.pyc` files into `guards/__pycache__/`. I removed them and confirmed restoration. I then verified that running the guards the normal way (as scripts) creates nothing — so `MANIFEST_U1E_SHA256.json:4`'s claim "live guards write nothing" is **accurate as tested**. I report my own drift because the freeze rule binds me too.

`FREEZE RULE` is in the banner at `authority/00_AUTHORITY_BANNER_U1E.md:34-41`: *"NO WRITE to the bundle between commissioning and verdict... every repair — however small, however directly an auditor requests it — lands as the NEXT round's content."*

## PER-SURFACE VERDICTS

| Surface | Verdict |
|---|---|
| **R1** The four round-4 proof blockers, on disk | **PASS** |
| **R2** The mathematics, spot-hostile | **PASS** — two LOW display/notation findings, no error |
| **R3** Scope and fencing | **PASS WITH CONDITIONS** — content correct; H9 instrument is token-overfit |

## **GATE VERDICT: PROMOTE.**

---

## R1 — THE FOUR ROUND-4 BLOCKERS: ALL DISCHARGED

**F-01 custody — DISCHARGED.** Freeze verified byte-for-byte above. All four guards `EXIT=0` (I initially mis-read exit codes through a `tail` pipe and re-ran them cleanly): `guard_a8_strictness` 5/5 checks, `guard_live_upper_authority_hygiene` 12/12 (H0, RB, H1×2, H2, H3, H4, H5, H9, H7, H6, H8), `guard_second_engine_projectors` PART A + PART B, `guard_selftest_injection` **23/23**. Ledger entry 23 (`authority/U1E_CORRECTION_LEDGER.md:278-315`) is honest, not defensive: *"(F-01, CUSTODY — ACKNOWLEDGED AS A PROCESS VIOLATION) the adjudicating track edited the bundle while the round-4 auditors were reading it; the mid-round edits were correct in content and wrong in procedure"* (`:282-285`).

**F-02 the false printed inequality — DISCHARGED.** §3.7 now reads `K := 0.08367827985` (`proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md:380`). Recomputed independently:

```
kappa = -2 log x_max = 0.08367827985737301130174257628407365634125056874017382646735354554151
K     = 0.08367827985        K <= kappa  TRUE (slack 7.373e-12)  -> valid DOWN-round
2/K   = 23.901064930889589743401017103962373098...   <= 23.9010650  TRUE as printed
K/2   = 0.041839139925                               >= 0.0418391   TRUE as printed
```
Both displayed routes in (3.11) are now **true as printed**. The round-4 defect reproduces exactly on the old value (`2/0.0836782 = 23.9010877385…`, false), confirming the repair is at the right place. The §3.7 parenthetical's stated reason (`:381-387`) is **correct**: `K` appears only in `K/2` (down-rounded → safe for a lower bound) and in the *denominator* of `2/K` (down-rounded `K` → over-estimate → safe for an upper display).

**G5 is now a genuine chain check, verified by mutation** (`guards/guard_a8_strictness.py:111-129`). It parses the proof's own `K` and asserts both the down-round premise (`:119`) and the chain (`:121`, `:124`). My two injections isolate the two asserts independently:

| # | injection | result |
|---|---|---|
| **AI-1** | `K := 0.0836783` — *invalid* down-round (K > κ) but chain inequalities still true | **FIRED**: `G5 displayed K is not a valid DOWN-round of kappa` |
| **AI-2** | `K := 0.083678` — valid down-round, but `2/K = 23.901144…` overshoots | **FIRED**: `G5 the proof's displayed chain 2/K exceeds the displayed bound` |

AI-1 is the sharper test: it passes both chain inequalities and is caught only by the premise assert. G5 is fail-capable on both halves.

**F-03 Lean anchor — DISCHARGED.** All six §1b digests verified against **commit blobs**, not the working tree:

```
$ git cat-file blob 6e6adb5:lean/I3322Kernel/I3322Kernel.lean | sha256sum
029575287691d33f72a6c513b53eef15f64fc9cfea5c19f567bbd66043d9c9b4   = proof :114  MATCH
```
and likewise `AxiomCheck.lean` (`:116`), `QuarterCeiling.lean` (`:118`), `RateCores.lean` (`:120`), `EndpointMargins.lean` (`:122`), `FiniteClosure.lean` (`:124`) — **6/6**. Round-4's mismatched `1442892…` is gone. `6e6adb5` is genuinely public: `git ls-remote origin HEAD` → `6e6adb5cad1d3a106…`, `git branch -r --contains` → `origin/main`. H5 does the same via `git cat-file` (`guard_live_upper_authority_hygiene.py:260-270`), never the working tree.

I did not trust the stored receipt — I re-derived it. From the commit blobs: **27 theorem/lemma declarations**, **27 `#print axioms` lines**, name sets identical **and in the same order** as `audit_archive/AXIOMCHECK_RECEIPT_2026-08-07.txt`; coverage complete in both directions (no declaration unchecked, no check without a declaration); **zero** `sorry`, `axiom`, or `native_decide`. The sole non-standard row, `staircase_sum_injOn: [propext, Quot.sound]`, is a strict **subset** of the standard axioms, exactly as §1b:107 states. All five consumed statements verbatim: `RateCores.lean:97, 102-104, 111-112, 117-118`; `QuarterCeiling.lean:95-96`.

**F-04 provenance termination — DISCHARGED.** `REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md` is carried as the seventh copy, **byte-identical** (`cmp` clean) to the sealed v28.1 source, sha `589bb7d8…`, hash-anchored at `proof:187`. All **7/7** copies verified byte-identical to their external sealed sources independently of H7. The termination statement (`proof:188-196`) is plain and **accurate**: I confirmed the uncarried family-B source is real (`dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md:75` → `THEOREM_N_ROUND3_BLIND_AUDIT_SOURCE.md`) and — the point round 4 could not close — that it is **not load-bearing here**: `08 §C:106` states *"The new G1 endpoint-positivity contradiction uses family **A** only."* Family A is the copy now carried. The load-bearing chain to `Z ⋐ (−1,1)²` (`G1:117-123`, boxed) therefore terminates inside the bundle. G1's status line is quoted unupgraded (`G1:3`).

## R2 — THE MATHEMATICS

I re-derived rather than re-read. **No mathematical error found.** All §3 displays at 140 digits with rounding directions:

```
mu_min  = 2 + 2(S_LO - 1/4) = 2.001750769003037  exact terminating rational, > 2   (3.7)
x_max   = 0.959024036840272287835284575905452272636739745544819578542827  <= 0.9590241  UP   OK  (3.9)
x_max^2 = 0.919727103237411938343554152090733717300416301849204693921580  <= 0.9197272 UP   OK  (3.9)
kappa   = 0.083678279857373011301742576284073656341250568740173826467353  >= 0.0836782 DOWN OK  (3.10)
2/kappa = 23.901064928783633189806723163985988798231738477714215119445    <= 23.9010650     OK
```
Root round-trip `x_max + 1/x_max − mu_min = 0E-139`. Root selection (3.8) correct — `2/(mu+√(mu²−4))` is the smaller root, strictly decreasing in `mu`. The eigen-row limit (§3.3) reproduces the certificate's own row: `:916` `H_jj=d(c_{j-1},c_j)`, `:920` `H_{j-1,j}=H_{j,j-1}=b(c_{j-1})`, `:929-932` transport law, `:935-937` the reciprocal orientation at `−∞`, `:967-969` boxed `Hλ=Sλ`, `:229` `b(t)=√(1−t²)/2` — **all verbatim at the cited lines**, as are `§6:446-451`, `§10:792-795` (boxed), `§10:798`, `§1:73`. The flux identity (5.1) is boxed character-for-character at `dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md:85-94`. Index bookkeeping is consistent (`κ_± = −2 log y_±` against `λ_j² ~ e^{−κ_+ j}`); allocation `|I| = L_d+R_d+1 = d`; balance gives `κ_∓L_d = κ_eff(d−1)+O(1)` with `κ_eff = κ_−κ_+/(κ_−+κ_+)`, consistent with (3.11); §7's limsup and quantifier order are clean. `C_diag ≤ 4·1+8·2 = 20` is a safe over-count. All five §1a certificate hashes and both public-repo anchors (`9a5d34fb…` sprint-1197, `5142425…` sprint-1292) recomputed and match; the window at `THEOREM_S_SIGNED_PUBLIC_STATEMENT.md:7-12` is open at its lower endpoint, licensing `S > S_LO` strictly.

**M-01 [LOW — documentation]** Display-convention inconsistency at `proof:391`, `STATUS_U1E.json:19`, `ledger:294`: `2/K = 23.9010649309...`. The true value is `23.90106493088959…`; every other ellipsis in the document **truncates**, so this one alone **rounds** the last shown digit. **No inequality is false** — the chain in (3.11) is true as printed and G5 verifies it in exact rationals — but in a gate whose last two rounds turned on rounding-direction discipline, the document should not switch convention inside its own headline display. Fix: write `23.90106493088...` as at `:394`.

**M-02 [LOW — notation]** The symbol `K` is overloaded: a **compact set** in §2 and a **decimal surrogate** in §3.7. Harmless to the argument, and G5's regex is unambiguous, but a reader meets `sup_K` and `2/K` in the same proof.

## R3 — SCOPE AND FENCING

**Content: correct.** `Theta(log)` occurs exactly four times in the live chain, every one conditional: `proof:513` (under §8's *"IF AND ONLY IF this U1G gate promotes"*, `:512`), `banner:14`, `PROMOTED_LOWER_RATE_RECEIPT.md:14`, `U1E_DEPENDENCY_GRAPH.md:80`, plus `STATUS_U1E.json:18`. The word "unconditional" never touches the safe bound. Non-sharpness is stated at `proof:507`, `proof:522`, `banner:12`, `STATUS:4`. Lean scope is honestly fenced (`proof:136-142`). Residual risk is inherited at the point of consumption (`proof:92-101`). Round-4's recommended items were adopted: the Rayleigh-quotient **rigorous** lower bound is implemented, and the `d(x,u)` receipt is now cited by file+line and hash-anchored (`proof:80-88`).

**Instrument: partial.** H9 exists — a genuine improvement over round 4's zero backing — but it is a forbidden-token list. My injections escape it:

| # | injection (manifest re-pinned, i.e. determined adversary) | expected | fired |
|---|---|---|---|
| **AI-3** | Sharpness claim evading the token list: *"the constant 23.9010650 is best possible and is attained in the limit; no further improvement is available"* | fire | **no — GAP** |
| **AI-4** | **False** tighter display added beside the true one: `y_±² <= 0.9197270 and 1/kappa_eff <= 23.9010000` | fire | **no — GAP** |
| **AI-5** | Content hidden in `guards/__pycache__/` (H8 excludes it; also gitignored) | fire | **no — GAP** |
| **AI-6b** | §1b repointed to commit `9999999` with a decoy `6e6adb5` token elsewhere | fire | **no — GAP** |

**I-01 [MODERATE — instrument]** AI-3: a sentence asserting exactly what §7.2/§9 disclaim passes H9 green. The fencing is authorship-backed against paraphrase.
**I-02 [MODERATE — instrument]** AI-4: round-4's S-I1/S-I2 gap persists. An *added* false display is invisible.
**I-03 [MODERATE — instrument]** AI-6b: H5 **hardcodes** `6e6adb5` rather than parsing the commit from the proof, so §1b's commit identifier is authorship-backed.
**I-04 [LOW — instrument]** AI-5: `__pycache__` is excluded by H8 *and* gitignored, a triple blind spot. The bundle is currently clean — I verified zero such files.

**All four are coverage gaps against future tampering, not defects in the present artifact.** On every one I checked the actual content and it is correct: no sharpness sentence, no false display, the right commit, no hidden files.

## WHY THIS PROMOTES

I set out to deny this. I could not. The four named blockers are executed and I verified each against primary sources rather than the bundle's own reasoning: the freeze held byte-for-byte through my entire audit, (3.11) is arithmetically true as printed with the guard now checking the printed chain, all six Lean anchors resolve at a genuinely public commit with a receipt I reproduced from the blobs myself, and the provenance chain's load-bearing branch now terminates inside the bundle with the uncarried branch named and shown to be inert.

The residual findings are two LOW documentation nits and four instrument-coverage gaps. **I decline to convert the instrument gaps into blockers.** Round 4 rated R3 PASS with *zero* instrument backing and listed fencing asserts as *"Recommended, not blocking"*; round 5 shipped partial backing. Denying now for incomplete backing of an item that passed with none would be moving the goalposts, and the regress has no natural stopping point — every token check admits a paraphrase. What matters at a promotion gate is whether the claim on trial is true and supported, and it is: `D_upper(eps) = O(log(1/eps))` at local Hilbert-space dimension scope with existential constant, and `1/kappa_eff <= 23.9010650` as a derived, non-sharp, risk-inheriting bound.

I am the fifth auditor and the third on the proof surface to report that the mathematics is sound. Unlike my predecessors I have nothing procedural left to hold against it either.

## RECOMMENDED (non-blocking, for the round-5 record)

1. **M-01** — restore the truncation convention at `proof:391` / `STATUS:19` / `ledger:294`.
2. **M-02** — rename §3.7's decimal surrogate (e.g. `K_0`) to free `K` for §2's compact set.
3. **D-01 [LOW — documentation]** — stale round labels: `proof:3` and `banner:1` both self-declare "round 4" while `MANIFEST:2` and `STATUS:5` correctly say round 5. Under a freeze rule that commissions each round against a stated commit, the artifact should know its own round.
4. **I-01/I-02** — make H9 and G5 *structural*: parse every `<=`-display of the four tracked constants and verify each numerically, rather than blacklisting strings. This closes AI-3 and AI-4 together.
5. **I-03** — have H5 parse the commit id from §1b and use it in `git cat-file`.
6. **I-04** — narrow H8's exclusion from `__pycache__/` to `*.pyc`, and disclose the exclusion in its printed message.
