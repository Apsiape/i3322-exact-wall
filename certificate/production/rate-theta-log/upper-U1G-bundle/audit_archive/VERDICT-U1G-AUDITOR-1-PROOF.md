# VERDICT — U1G round-4 gate, PROOF surface

PROVENANCE: delivered in-session by the round-4 proof-surface auditor
(background agent "U1G round-4 gate: proof") on 2026-08-07 and written
to disk the same day by the adjudicating track, verbatim. HTML entity
escapes from the delivery wrapper (&lt; &gt;) restored to < >.

---

# VERDICT — U1G ROUND-4 PROMOTION GATE, PROOF SURFACE

**Auditor:** independence layer, refutation-first, default FAIL.
**Method:** every load-bearing step re-derived from the `[P]` certificate and the Lean kernel without using the bundle's reasoning; every hash recomputed, never read from a manifest; the Lean kernel built and axiom-checked; 10 fault injections of my own design run against the two guards.

**AUDIT FREEZE.** I audit **STATE M** — the bundle state that verified 38/38 against `MANIFEST_U1E_SHA256.json`, confirmed by my own recomputation at ~10:26 PDT on 2026-08-07. The bundle has since drifted three times (see F-01). All line/hash citations below are to STATE M unless marked "current".

---

## VERDICTS

| Surface | Verdict |
|---|---|
| **R1** The mathematics, re-derived from scratch | **FAIL** — one false displayed inequality at (3.11); everything else verified sound |
| **R2** Round-3 blocker discharge, on disk | **FAIL** — B7 not discharged; B2, B3, B5-provenance carry defects |
| **R3** Scope and fencing | **PASS** |
| **R0** Custody of the artifact under audit (arose during the audit) | **FAIL** |

## **GATE VERDICT: DENIED.**

**The separation the rules demand, stated plainly and first.** I could not break the mathematics. I reconstructed the entire chain — single-map monotonicity, the ratio-limit existence, the eigen-row limit equation, the band algebra, root selection at both ends, truncation exactness, the flux identity, the three-row accounting, the allocation, the limsup — independently from the certificate and the Lean kernel, and **every step is valid**. The theorem `D_upper(eps) = O(log(1/eps))` and the constant `1/kappa_eff <= 23.9010650` are **both true**, and I verified the constant at 80 digits from the certified window. The denial rests on (a) one arithmetically false inequality in the written derivation of that constant, (b) an anchoring/provenance residue, and (c) the fact that the document on trial was edited while I was auditing it. **None of my findings is a mathematical kill. This is the fourth consecutive round in which that is true.**

---

# FINDINGS

## F-01 [BLOCKER — CUSTODY] The bundle under gate is not frozen; it changed three times during this audit, and is currently internally broken.

Timeline, from filesystem mtimes and my own recomputed hashes:

| time (PDT) | event |
|---|---|
| 10:24:07 | `MANIFEST_U1E_SHA256.json` written (38 entries) |
| ~10:26 | I verify **38/38 exact**, nothing unmanifested but the manifest itself. `proof/…U1G.md` = `da721efa7503b758…` (manifest value) |
| 10:37:10 | `dependencies/ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md` created (sha `d486e3e3…`) — a **sixth** dependency copy, unmanifested |
| 10:37:44 | `guards/guard_second_engine_projectors.py` rewritten: `ea1d9f12…` → `ca624543…` |
| 10:38:12 | `proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md` rewritten → `19c7f519…` |
| 10:39:32 | proof rewritten **again** → `05e6a7ab…`; `guard_live_upper_authority_hygiene.py` now also off-manifest |

Current on-disk state (10:39:32), verified by recomputation:

```
manifest mismatches: ['guards/guard_live_upper_authority_hygiene.py',
                      'guards/guard_second_engine_projectors.py',
                      'proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md']
unmanifested:        ['dependencies/ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md']

$ python guards/guard_live_upper_authority_hygiene.py
FAIL provenance model expects exactly 5 dependency copies, found 6      EXIT=1

$ python guards/guard_selftest_injection.py
SELFTEST FAIL: I0 unmutated copy - guard fired, expected PASS           EXIT=1
```

The edits are visibly *responsive* — the new guard docstring cites "round-4 integrity finding 1", and proof §1b (current, lines 137–145) now anchors the Jacobi-quotient-to-Bell-value bridge to `certificate/production/foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md` (sha `514242545b32040e34f0d879dfe8bd745b8a0d24341b071ff93e901763351195`, which I recomputed and confirm). That is a *good repair* — it closes the exact gap I raise in F-04. **But it is being made mid-round, to the artifact the independence layer is reading.** A gate whose subject mutates in response to in-flight audit findings has no independence layer at all; it has a negotiation. This is the round-2 failure mode ("a claim certified by a scope drawn by the claimant") in its purest form, now at the level of the artifact itself.

The banner's own gate rule ("self-audits and worker stage reports are claims, not verdicts") presupposes a frozen subject. It was not frozen. **Note also** that the new §1b anchor will break `H5` on its own terms: the parser at `guard_live_upper_authority_hygiene.py:192–197` requires **exactly 5** certificate pairs and a bare filename, and the new sixth pair's "name" spans a line break (`certificate/production/` + newline + `RIGOROUS-DIMENSION-255-LOWER.md`). The repair is not yet self-consistent.

---

## F-02 [BLOCKER — MATHEMATICS AS WRITTEN] §3.7's (3.11) contains a **false inequality**. The rounding-direction repair that round 3 blockered (B7/F5) was applied in the wrong place, and the guard cannot see it.

Present identically in STATE M and in the current state (lines 354–361):

```
Hence with kappa_± >= K := 0.0836782:

    kappa_eff := (1/kappa_- + 1/kappa_+)^{-1} >= (2/K)^{-1} = K/2
              >= 0.0418391,
    1/kappa_eff <= 2/K <= 23.9010650.                             (3.11)
```

`K` is defined in that sentence as the literal decimal `0.0836782`. Recomputed at 80 digits (mpmath, `mp.dps = 80`):

```
kappa_true = -2·log x_max = 0.0836782798573730113017425762840736563412505687401738264673535
2/K        = 2/0.0836782  = 23.90108773850297927058660439636607862024
2/K <= 23.9010650                                                    ->  FALSE
1/0.0418391 = 23.90108773850297927058660439636607862024
1/0.0418391 <= 23.9010650                                            ->  FALSE
2/kappa_true = 23.90106492878363318980672316398598879823             ->  <= 23.9010650  TRUE
```

**Both** displayed routes through §3.6's down-rounded surrogate overshoot the headline bound by `2.28e-5`. The error is structural, not typographical: `kappa >= 0.0836782` is correctly rounded **DOWN** (§3.10 says so explicitly and is right), but §3.7 then places that surrogate in a **denominator**, where DOWN-rounding is **UNSAFE**. The claimed final bound is true only against the *unrounded* `kappa`, which §3.7's own explanatory sentence concedes ("The exact value of 2/(−2 log x_max) is 23.90106492878…").

This is precisely the defect class of round-3 F5/B7 ("an upper bound must be rounded up in the text of a claim whose only number this is"), applied to the wrong quantity and therefore not discharged.

**The guard cannot catch it, and its G5 claim to the contrary is false.** `guard_a8_strictness.py:81` computes `inv_keff = 2 / kappa` from the *unrounded* `kappa`, not from the proof's displayed `K`. G5 (lines 91–110) is a **substring-presence** check on six literals plus two blacklisted strings — not a chain check. The docstring's claim that G5 ends "guard-enforcing-one-number-while-the-proof-displays-another" (round-3 finding 8) is not implemented. My injection **S-I4** substitutes the proof's own written chain into the guard:

```
S-I4  edit: inv_keff = 2 / mpf("0.0836782")   # the PROOF's written chain 2/K
      -> AssertionError: 1/kappa_eff upper bound fails: 23.9010877385
```

The guard's own headline assert fires on the proof's own written derivation.

**Severity and repair.** The theorem is unaffected; the constant is unaffected (`1/kappa_eff = 1/kappa_- + 1/kappa_+ <= 2/kappa_true = 23.901064928783… <= 23.9010650`, which I verified independently). The repair is one line: display `K := 0.08367827985` (still a safe DOWN-round; `2/0.08367827985 = 23.901064928804… <= 23.9010650`), or perform the division before rounding. **But an inequality that is false as printed, in the numbered display that produces the single explicit constant of the claim on trial, at a fourth gate round that was specifically commissioned to fix rounding directions, cannot pass a refutation-first proof surface.**

---

## F-03 [MAJOR — ANCHORING] The Lean anchor for `I3322Kernel.lean` verifies against the working tree, not against public commit `6e6adb5`. (B2 partially discharged.)

Proof §1b: *"Public repository path lean/I3322Kernel/, public commit 6e6adb5 (pushed 2026-08-07) … Source hashes:"* followed by six digests. I recomputed all six against the **commit blob**:

```
$ git cat-file blob 6e6adb5:lean/I3322Kernel/I3322Kernel.lean | sha256sum
029575287691d33f72a6c513b53eef15f64fc9cfea5c19f567bbd66043d9c9b4
proof §1b anchors:
144289260aa1edfe321bdc5d5dcb32158036356c0ee7ce4b2a9936dae49be978   MISMATCH
```

The other five match the commit exactly. Cause: the working-tree file ends `…RateCores\r\n` while the committed blob ends `…RateCores\n` (verified by `od -c` and `diff`; `git status` masks it via autocrlf). **Anyone who clones the public repo and checks the anchor on Linux, or with `autocrlf=false`, gets a FAILED anchor on one of the six files.** `guard_live_upper_authority_hygiene.py:205–211` hashes the local working tree, so it cannot detect this.

The content in question is a four-line import list with zero mathematical weight, and I confirm the commit is genuinely public (`git ls-remote origin HEAD` → `6e6adb5cad1d3a106…`; `git branch -r --contains 6e6adb5` → `origin/main`). But an anchor that does not verify at its stated anchor point is not an anchor. This is the F10/B2 defect class recurring in reduced form.

**Everything else about B2 is fully discharged and I verify it positively.** I built and ran the kernel myself:

```
$ lake env lean AxiomCheck.lean
27 lines, each 'depends on axioms: [propext, Classical.choice, Quot.sound]'
(staircase_sum_injOn: [propext, Quot.sound] — a subset, as §1b states)   EXIT=0
```

27 theorem declarations across the four modules, 27 `#print axioms` lines, **zero** `sorry`/`axiom`/`native_decide`. All five consumed statements exist **verbatim as quoted** in proof §1b (`RateCores.lean:97, 102–104, 111–112, 117–118`; `QuarterCeiling.lean:95–96`).

---

## F-04 [MODERATE — PROVENANCE] The "exactly five FULL copies, zero extracts" model terminates in an uncarried, unhashed document at a load-bearing point.

Proof §1c: *"G1's endpoint-reserve inputs are provenance-anchored by `dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md`."* That document (line 9) sources its family-A reserves to:

```
**Source:** dependencies/REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md,
            Theorem 4.1 and its exact rational verifier.
```

That file is **not in this bundle** and is **not hash-anchored in proof §1** (a second dangling pointer at line 75 → `THEOREM_N_ROUND3_BLIND_AUDIT_SOURCE.md`). Both resolve only in the sealed v28.1 bundle. The chain is load-bearing: G1 §2's reserves ⇒ `g(1) > 0, g(-1) > 0` ⇒ `Z ⋐ (−1,1)²` (G1 §3:117–123) ⇒ `b >= b_0 > 0` on `K` ⇒ §3.3 may divide by `b(t_±)` and §2's `R_max` is finite. Without compact interiority the whole strictness argument collapses.

`H6`'s dangling-pointer check does not fire because it scans **authored** files only (`guard_live_upper_authority_hygiene.py:223`), not dependency copies. I ran the scan H6 omits and it finds exactly these two.

Mitigating and stated honestly: G1's own status line ("PROVED CANDIDATE; promotion audit may attack provenance/typing") is quoted verbatim and **not upgraded**, and the dependency graph declares G1 upstream-shared with (S). This is a real residue, not a concealment.

---

## F-05 [MODERATE — ANCHORING] PART B's promotion to load-bearing imported an unanchored bridge (STATE M). Repaired mid-round, which is F-01.

In STATE M, §1b promoted `guard_second_engine_projectors.py` PART B to load-bearing for `S > 1/4`, describing its outputs as *"Bell values"*. PART B does not construct projectors or evaluate `<psi|B|psi>`; it computes the top eigenvalue of a Jacobi matrix assembled from `d(x_i,x_{i+1})` and `b(x_{i+1})` (lines 130–137). The identification "Jacobi eigenvalue = Bell value of a legal finite strategy" was carried **only in the guard's docstring** as *"the repository's certified sprint-1292 pattern"* — a prose-named authority at the foot of the single fact all strictness rests on, i.e. the exact F10/round-2-F-6(d) class. The current state anchors it by hash (I confirm the target file and digest); that repair is sound but arrived after freeze.

Two residual points that survive the repair: (i) `mp.eigsy` at 110 dps is a **numerical** eigenvalue, not a certified enclosure — a Rayleigh quotient `<v,Jv>/<v,v>` with the explicit `v` would give a rigorous lower bound in one line and is not done; (ii) PART A verifies 12 block-structured operators at `m = 3..8`, not the six named I3322 operators, so §4's *"All six operators remain exact projections"* is covered by structural argument, not by the cited second engine. Both LOW; neither touches the exhibited values.

---

## F-06 [MODERATE — INSTRUMENTS] Guard coverage. 6 of my 10 injections passed green through the guards; the shipped self-test exercises only one of the two guards.

`guard_selftest_injection.py:55` invokes **only** `guard_live_upper_authority_hygiene.py`. The strictness guard ships with **no** injection self-test. My results (STATE M copy, guards unmodified except where noted):

| # | injection | expected | fired | |
|---|---|---|---|---|
| S-I1 | add a false tighter display `1/kappa_eff <= 23.9010000`, keep required tokens | fire | **no** | GAP |
| S-I2 | display a false down-rounded `y² <= 0.9197270`, keep `0.9197272` elsewhere | fire | **no** | GAP |
| S-I3 | factor-of-two: `kappa = -2*mlog(rho)` | fire | yes | GOOD (F6/B6 repair works) |
| S-I4 | guard computes `2/K` from the proof's displayed `K` | pass | **fired** | **F-02** |
| S-I5 | flip a window digit in the guard's `S_LO` | fire | yes | GOOD |
| H-I1 | mutate a sealed dependency copy on disk | fire | yes | GOOD (H5) |
| H-I2 | insert an **unconditional** `Theta(log)` claim in §7, leave §8's fence intact | fire | **no** | GAP |
| H-I3 | change `1/kappa_eff <= 23.9010650` to `= 23.9010650 exactly — a sharp equality` | fire | **no** | GAP |
| H-I4 | invert §1b's honest-scope disclaimer into "establishes S > S_LO by machine-checked proof" | fire | **no** | GAP |
| H-I5 | replace "DISCLOSED RESIDUAL RISK…" with "NO RESIDUAL RISK REMAINS" | fire | **no** | GAP |

**Diagnosis:** `H3` and `G5` are substring-presence checks. They verify that certain *tokens* appear; they cannot detect a *contradicting sentence added next to them*, nor a false inequality routed around them. The entire R3 fencing surface — conditionality of Θ(log), non-sharpness, honest Lean scope, residual-risk inheritance — is **unguarded**, and the four fencing properties that pass today pass by authorship, not by instrument. This is the round-3 integrity diagnosis ("every claim certified by an instrument whose scope is narrower than the claim") surviving in a new place.

---

# R1 — WHAT I VERIFIED POSITIVELY (re-derived, not accepted)

**Certificate quotes: all verbatim, all at the stated lines.** `CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md:446` *"is Borel and is the graph of a strictly increasing one-to-one Borel map"*, with `Z={(P(u),u):u∈Y}` at 449–451; `:792–795` boxed `P(c_{j+1})=c_j \quad\text{for every }j`; `:798` *"Every adjacent pair \((c_j,c_{j+1})\) is a full-zero source-target pair."*; `:73` the §1 relation form; `:929–932` the transport law; `:916` `H_{jj}=d(c_{j-1},c_j)`, `:920` `H_{j-1,j}=H_{j,j-1}=b(c_{j-1})`, `:967–969` boxed `H\lambda=S\lambda`; `:229` `b(t)=\sqrt{1-t^2}/2`. `d(x,u)=xu+(x-u)/2-1` is **not** defined in the certificate document — I located it at `paper/MANUSCRIPT.md:215` and `certificate/production/foundational-sprint-1197/EXACT-I3322-QUANTUM-SUPREMUM.md:66`, so `D(t)=d(t,t)=t²−1` is correct but its receipt is off-document (LOW; add the line cite). Five certificate hashes and the window at `THEOREM_S_SIGNED_PUBLIC_STATEMENT.md:7–12` all recomputed and match §1a.

**§3.1 is now genuinely written and the induction is valid.** `c_j = P(c_{j+1})` for every `j` with `P` strictly increasing gives `c_{j+1} = P^{-1}(c_j)`; `c_j ∈ ran(P)` for every `j` (witness `c_{j+1}`), so `P^{-1}` applies and preserves order. The `c_1 ≠ c_0` argument is correct: `c_1 = c_0` ⇒ `c_0 = P(c_0)` ⇒ constant **both** directions, ⇒ `lambda` geometric on all of `Z`, ⇒ not in `l²` for any `r(c) > 0` including `r = 1`. Forward induction via `P^{-1}` and backward via `P` are both correct and both written. B4 fully discharged.

**§3.3's eigen-row is the certificate's own row.** `b(c_{j-1})·(lambda_{j-1}/lambda_j) = b(c_{j-1})²/g(c_{j-1})` and `b(c_j)·(lambda_{j+1}/lambda_j) = g(c_j)` reproduce `:943–962` character for character. The `-infinity` end's reciprocal orientation is now spelled out (round-3 F4 discharged); `lambda_{j-1}/lambda_j → 1/y_+` matches `:935–937` exactly. Limit passage licensed by continuity of `b, d, r` on compact `K` and `c_j → t_±`.

**§3.4 by hand:** `D(t)+2b(t) = t²−1+s = −s²+s = s(1−s) ≤ 1/4` with `s=√(1−t²)`, equality iff `s=1/2`. `mu−2 = (S−D−2b)/b ≥ (S−1/4)/b ≥ 2(S−1/4)` needs `b ≤ 1/2` and `S−1/4 ≥ 0`; both held. `mu_min = 2+2(S_LO−1/4) = 2.001750769003037` is an **exact** terminating decimal (`= 2001750769003037/10^15`), verified in exact rationals.

**§3.5 root selection at both ends.** `y+1/y=mu`, `mu>2` ⇒ roots `x_dec = (mu−√(mu²−4))/2 = 2/(mu+√(mu²−4))` and its reciprocal; `l²` excludes the growing root at `+infinity` directly and at `−infinity` through the outward orientation `y_- := 1/r(t_-)`. `x_dec` strictly decreasing in `mu` because `mu+√(mu²−4)` is strictly increasing. Correct.

**All displayed constants at 60+ digits, from scratch, with rounding directions:**

```
x_max  = 0.959024036840272287835284575905452272636739745544819578542828  <= 0.9590241  UP  OK
x_max² = 0.919727103237411938343554152090733717300416301849204693921580  <= 0.9197272  UP  OK
kappa  = 0.083678279857373011301742576284073656341250568740173826467353  >= 0.0836782  DOWN OK
K/2    = 0.0418391 exactly                                               >= 0.0418391  OK
1/kappa_eff <= 2/kappa = 23.90106492878363318980672316398598879823       <= 23.9010650 UP  OK (fact)
                                                                          via 2/K       FALSE (F-02)
```

**§§4–7.** Flux identity re-derived: `Σ_{j∈I} lambda_j (H lambda)_j = S·M_I = <lambda_I, H_I lambda_I> + b(c_{a−1})lambda_{a−1}lambda_a + b(c_b)lambda_b lambda_{b+1}` — character-identical to Cesàro `§2:85–94` (boxed, verified at those exact lines). Three-row accounting is exhaustive: within `I×I` the §4 strategy's matrix differs from `H_I` by a **diagonal** supported at `{a,b}` only, so `V_I = v_I + (lambda_a²Δ_a + lambda_b²Δ_b)/M_I`. `C_diag ≤ 4·1 + 8·2 = 20` recounted from the §0 display (marginals `−A2−B1−2B2`, absolute sum 4; eight joint terms of modulus 1) — safe over-count, harmless since constants are existential. `lambda_a² ≤ R_max|lambda_{a−1}lambda_a|` uses `r`, `lambda_b² ≤ R_max|lambda_b lambda_{b+1}|` uses `1/r` — both covered by `(2.1)`'s `sup_K max{r, 1/r}`. `|I| = L_d+R_d+1 = d` identically; `kappa_∓ L_d, kappa_± R_d = kappa_eff(d−1)+O(1)` with `kappa_eff = kappa_-kappa_+/(kappa_-+kappa_+)`; §7's quantifier order is clean and `S_d` is monotone so `D_upper` is well-defined. **All correct.**

**§1b's S > 1/4 structure is honest.** The disclaimer at lines 124–130 correctly refuses to attach "Lean-checked" to the composite; `quarter_lt_window_lower` is exactly `(1:ℚ)/4 < 2508753845015185/10^16`. I ran PART B myself: `d=24 → 0.2500643651906240706950548`, `d=33 → 0.2505605862827521248927743`, both `> 1/4`, matching §1b's quoted digits. B3 discharged in structure (see F-05 for the bridge).

---

# R2 — BLOCKER DISCHARGE, AGAINST DISK

| | round-3 blocker | verdict |
|---|---|---|
| **B1** | round-2 proof verdict on disk | **DISCHARGED — and I verified the custody myself.** I extracted transcript line 50417 (`…5e738f3c….jsonl`), unescaped XML entities, and diffed against `audit_archive/VERDICT-U1E-AUDITOR-1-PROOF.md` below its header: **117 lines vs 117 lines, ZERO diff hunks.** The header's claims are all accurate — line 50417 is the delivery, 50419 the duplicate task-notification. The ledger's sha256 `9ec4fa7037037d281bfa4f45f989dd18b8dcde9c44a6fce6f11f1510e9f536e5` matches by recomputation. **Provenance verdict: acceptable.** The reconstruction is byte-verbatim against a primary source the adjudicating track did not author, and I confirmed it as an independent party. One residue: `tasks/a707afe53dcd9120f.output` is 0 bytes, so the transcript is the *only* surviving primary — a future external party without transcript access must take my confirmation, not the header's. **Ledger entries 10–15 are consistent** with the reconstructed A1–A22 and residual blockers 1–6; entry 16's "A1–A22 and residual blockers 1–6" is exactly what the document contains, resolving round-3 F21's open count (that verdict inferred "A1–A19" from the paraphrase). |
| **B2** | Lean kernel anchored | **PARTIAL — F-03.** Built, axiom-checked, statements verbatim, commit public; one of six file hashes anchors the working tree, not the commit. |
| **B3** | `S > 1/4` double anchor | **DISCHARGED in structure — F-05 on the bridge.** |
| **B4** | write §3.1 | **DISCHARGED.** Verified valid line by line. |
| **B5** | full G1 source | **DISCHARGED.** Byte-compared against `I3322_V28_1_…/dependencies/`: `G1` `6dbb19c7…`, Cesàro `1ed80a06…`, truncation `908874ee…` — **all three byte-identical**. G1's status line 3 quoted verbatim, not upgraded. Provenance *model* residue: F-04. |
| **B6** | guard repairs | **DISCHARGED on the named item, incomplete overall.** The two-sided `1/kappa_eff` assert is real and fail-capable — my S-I3 mutation fires it. H2 widened, H0 generated, RB content-validated, H6 added — all confirmed by running. But see F-06. |
| **B7** | text corrections, rounding directions | **NOT DISCHARGED — F-02.** The `ENDPOint_` typo survives only in the now-historical U1F proof (`:116`) — acceptable. All three historical proofs carry in-file SUPERSEDED stamps. All other B7 items done. |

**Round-2 A-findings round 3 could not check:** **A3** (routes not independent) — **MOOT**: U1G has one route; the h=r^{−2}/hyperbolicity object is retired and absent. **A6** (three `[P]` nodes with no document) — **MOOT**: equality-module, sextic, wall-comparison selection are on the banner's RETIRED list and appear nowhere in the U1G proof or graph (I grepped). **A9** (bundle disclaims its best receipted input) — **DISCHARGED**: `S > 1/4` is now the strictness source. **A11** ((5.1) mis-cited) — **DISCHARGED**: §5.1 cites Cesàro §2:85–94, which I verified is where it lives. **A12, A14, A15** were the round-2 auditor's *positive verifications*, not blockers; I independently re-derived all three and concur.

---

# R3 — SCOPE AND FENCING: **PASS**

`Theta(log)` occurs **four** times in the live chain, every one conditional: proof `:456` (§8, "IF AND ONLY IF this U1G gate promotes"), banner `:14`, `PROMOTED_LOWER_RATE_RECEIPT.md:14`, `U1E_DEPENDENCY_GRAPH.md:70`. `STATUS_U1E.json` `theta_log_status` likewise. The word "unconditional" never touches the safe bound — its only live occurrences are the banner's own prohibition (`:14`) and the *killed* endpoint product (`:112`, inside a validated retraction block). The bound is stated as "derived inequality … claiming no sharpness" at §7.2 and §9, "anchored uniform bound" in the banner, consistently.

The `[P]` root's §§6–9 residual risk is inherited **at its point of consumption** (§1a, lines 85–94), and correctly located: items (i) `§6` and (ii) `§10` (which consumes §§6–9) both sit inside the range. `STATUS.json` in the public tree confirms the scope verbatim. It is repeated in the banner, `STATUS_U1E.json`'s `claim_on_trial`, the dependency graph, and §9. **This fencing is exemplary.** It is also, per F-06, entirely unguarded — H-I2/I3/I4/I5 all pass green.

---

# MINIMAL BLOCKER LIST

1. **Re-freeze the bundle.** Stop editing the artifact under gate. Re-seal, regenerate `MANIFEST_U1E_SHA256.json`, get all four guards to EXIT=0 including the self-test's I0 baseline, and re-commission round 5 against a stated frozen hash. Fold the mid-round repairs in — they are good — but as *round-5 content*, not as in-flight amendments. Adopt a standing rule alongside ledger entry 16's: **no write to the bundle between commissioning and verdict.** *(F-01)*
2. **Repair (3.11).** Either display `K := 0.08367827985` (safe DOWN-round; `2/K = 23.901064928804… ≤ 23.9010650`) or divide before rounding. Then make **G5 a chain check, not a token check**: have the guard parse the proof's displayed `K` and assert `2/K ≤` the displayed bound. Fix the same overshoot wherever the chain is restated. *(F-02)*
3. **Fix the Lean anchor.** Normalize `I3322Kernel.lean`'s line ending and re-commit, or state §1b's hashes as working-tree hashes and add the commit-blob digests alongside. Have H5 verify against `git cat-file blob 6e6adb5:<path>`, not the working tree. Fix the new §1b anchor's line-broken path so H5's parser can read it. *(F-03, F-01)*
4. **Close the provenance chain or restate it.** Carry and hash-anchor `REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md`, or say plainly in §1c that G1's endpoint reserves terminate in the sealed v28.1 bundle and are inherited at that bundle's status. Extend H6 to scan dependency copies. *(F-04)*

**Recommended, not blocking:** add a Rayleigh-quotient rigorous lower bound to PART B's exhibition; add an injection self-test for the strictness guard; add fencing asserts (no unconditional `Theta`, no equality form of the bound, honest-scope and residual-risk sentences present *and* uncontradicted) so R3 is instrument-backed rather than authorship-backed; cite the `d(x,u)` definition by file and line.

---

# CLOSING

I am the fourth auditor to deny this gate and the second to say the mathematics is sound. I re-derived it independently and I concur with the round-3 assessment without deferring to it: **the chain holds.** The `[P]` quotes are verbatim at the lines claimed, §3.1 is now correctly written, the Lean backbone builds clean on standard axioms only, the constants reproduce to 60 digits, the accounting and allocation are right, the fencing is careful and honest, B1's custody hole is genuinely closed and I verified it against the primary record myself.

What denies it this round is two things, and they should be named separately because they are different kinds of failure. **One is a documentation defect that has now survived four rounds in mutated form:** a rounding direction applied to the right quantity in §3.6 and then reused where its direction is wrong in §3.7, producing a printed inequality that is false by `2.28e-5` in the derivation of the claim's only number — and a guard that verifies a *different* chain than the proof displays while asserting it verifies the same one. That is a few minutes of work to fix.

**The other is structural and more serious:** the artifact was edited three times while I was auditing it, leaving the bundle currently failing its own manifest and two of its own guards. The repairs being made are the right repairs — one of them closes a gap I independently found — but a promotion gate cannot certify a moving target, and an independence layer that reads a document being rewritten in response to it is not independent. **Freeze it, then send it back.** On the mathematics I have nothing left to attack.
