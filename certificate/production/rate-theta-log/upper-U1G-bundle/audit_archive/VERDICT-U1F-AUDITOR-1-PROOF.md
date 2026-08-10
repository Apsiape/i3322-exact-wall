> Redaction note (2026-08-10): absolute private-workspace paths neutralized to [private-workspace]; no other byte changed.

# VERDICT — U1F round-3 gate, PROOF surface

PROVENANCE: delivered in-session by the round-3 proof-surface auditor
(background agent "U1F round-3 gate: proof") on 2026-08-07 and written
to disk the same day by the adjudicating track, verbatim. HTML entity
escapes from the delivery wrapper (&lt; &gt;) restored to < >.

---

# HOSTILE AUDIT — U1F ROUND-3 PROMOTION GATE

Independence layer. Default verdict FAIL. I re-derived every load-bearing step from the [P] root rather than reading the bundle's account of it, and I treated the A8 route as hostile to its author (the round-2 proof auditor).

---

## VERDICTS

| Surface | Verdict |
|---|---|
| **R1** A8 strictness chain | **PASS-WITH-CONDITIONS** (conditions C1–C4) |
| **R2** Accounting incorporation | **PASS-WITH-CONDITIONS** (conditions C5–C6) |
| **R3** Round-2 blocker discharge | **FAIL** (unauditable — primary document absent) |
| **R4** Operator / allocation / bound status | **PASS** (one cosmetic defect, F6) |

**GATE VERDICT: DENIED.** R3 alone forces it.

**But the denial is not a mathematical kill, and that distinction is load-bearing.** Rounds 1 and 2 died on the mathematical centre. Round 3 does not: the A8 chain survived hostile independent re-derivation intact. Every blocker below is an *anchoring, exposition, or audit-trail* defect, and every one is repairable without new mathematics from material I verified is already present. This is a materially better bundle than its predecessors, and I want that on the record alongside the DENIED.

---

## WHAT I VERIFIED INDEPENDENTLY (not taken from the bundle)

- **Certificate §1 certified input, quoted from the file** (`CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md:73`): *"the full interior zero locus is a one-to-one strictly increasing relation."* Present. §6:446–451 strengthens it: *"Z ... is the graph of a strictly increasing one-to-one Borel map P."*
- **Certificate §10:792–796 boxed:** `P(c_{j+1}) = c_j for every j` — a **single** map for **every** link. This is what actually makes §3.1's induction valid.
- **Bellman identity (1.2) exists as claimed.** Certificate §11:943–962: `(Hλ)_j/λ_j = d(c_{j-1},c_j) + p(c_{j-1}) + g(c_j) = S`, `p = b²/g`. Fixed-label specialization gives `S − D = g + b²/g`, hence `S − (D+2b) = (g−b)²/g`. Verified.
- **Transport law (1.1) is verbatim §11:929–932.** Confirmed.
- **Band identity + quarter ceiling, by hand and symbolically:** `D(t)+2b(t) = t²−1+s = −s²+s = s(1−s) ≤ 1/4`, equality iff `s=1/2`. Correct.
- **The whole chain at 60 digits, computed from scratch:** `μ_min = 2.001750769003037`, `x = 0.959024036840272…`, `ρ = 0.919727103237412…`, `κ = 0.083678279857373…`, `1/κ_eff = 23.901064928783633…`. Every displayed constant reproduces exactly.
- **Flux identity (5.1) re-derived from `Hλ = Sλ`:** `⟨λ_I,H_Iλ_I⟩ = S·M_I − [b(c_{a−1})λ_{a−1}λ_a + b(c_b)λ_bλ_{b+1}]`. Character-for-character identical to Cesàro source §2's boxed statement.
- **Operator display:** extracted the CG table under the concordance permutation — const 0, Alice marginals (−1,0,0), Bob (−2,−1,0), joints [[1,1,1],[1,1,−1],[1,−1,0]]. Exactly the repo's `NORMALIZATION-CONCORDANCE.md` table. Deterministic max = **0**; qubit max = **0.2500000000000013**. Matches the certificate's "classical bound 0, qubit and qutrit maximum exactly 1/4".
- **Five Theorem-S content hashes:** all five re-hashed on the public tree, all match §1.
- **Manifest:** 30/30 exact, nothing missing, nothing unmanifested but the manifest.
- **Strong corroboration the bundle does not claim:** certificate **§7:594–610** runs the *same* elimination. I carried it out symbolically — with `x=cos A, u=cos B, σ=(A+B)/2, δ=(A−B)/2` it reduces to `S = sin σ − sin²σ − ½ + ½cos 2δ ≤ 1/4`. **A8 is the audited Sprint-1198 argument, already living inside the promoted [P] root**, and the Cesàro receipt §6 already used it for `ρ± < 1`. The A8 route is not novel machinery on trial; it is the certificate's own argument made quantitative. That materially strengthens the case.

---

## FINDINGS

### R1 — THE A8 STRICTNESS CHAIN

**F1 [MAJOR] — §3.1's monotonicity warrant cites the wrong section; the load-bearing fact is never quoted. (Round-2 A5 not repaired.)**
§3.1 justifies the induction from "the zero-locus relation, which is one-to-one and STRICTLY INCREASING (certificate §1)". §1 alone does **not** license the induction. Certificate §10 defines the labels *interleaved* — `c_{2n}=u_n`, `c_{2n+1}=−P(−u_n)` — which reads as two alternating maps (`t↦−P(−t)` on even→odd, `P^{-1}` on odd→even), and for alternating maps the stated induction ("if `c_{j+1} ≥ c_j` then applying the increasing relation preserves the order at the next link") is **invalid**: `c_1 ≥ c_0` does not give `c_2 = P^{-1}(c_1) ≥ φ(c_0) = c_1`.
The claim is nonetheless **true**, because §10:792 boxes `P(c_{j+1}) = c_j` for *every* `j` — one map, uniform. That single line is what the proof needs and it is **never quoted**, in violation of the program's own quote-with-file-and-line rule (ledger entry 8). The "two-line argument" the round-2 auditor asked for is still not written.
*Repair: quote certificate §10:792–796 and §6:446–451; state `c_{j+1}=P^{-1}(c_j)`, `P^{-1}` strictly increasing, done.*

**F2 [MAJOR] — the pairing discharge is asserted, not argued, and is misattributed to the wrong statement.**
§3.1 claims to discharge "the Cesàro source's §9 pairing warning". Cesàro §9:501–509 warns about a *different* proposition: that `r_A(x_+) = r_B(β)` — a **two-end symmetry** identity — "was not yet certified and is no longer silently assumed". U1F discharges "the u-limit and the x-limit coincide", which is not what §9 warns about. Ledger entry 11 repeats the misattribution.
The proposition U1F actually needs is `α = x_+` (so that Cesàro's `ρ_+ = r_B(α)r_B(x_+)` equals U1F's `x²`), and it **is** true and two lines long: the *full* sequence is monotone under the single increasing `P^{-1}`, so its even and odd subsequences share a limit. Nowhere written.
*Note the good news: U1F does not need §9's identity at all — it bounds κ₊ and κ₋ separately. The exposure is removable entirely by dropping the ρ± framing from §3.2, since §5.5 needs only `lim λ_{j+1}/λ_j < 1`.*

**F3 [MODERATE] — §3.3's "uniformly over all labels" is false as written.**
`μ(t) := (S−D(t))/b(t) ≥ 2.00175` holds for every `t` (pure scalar). But `μ(t) = r(t)+1/r(t)` holds **only where `(t,t)` is a full-zero pair** — i.e. only at the limit label, since along the orbit `c_{j+1} ≠ c_j`. So `x < 1 strictly, uniformly over all labels` conflates two different quantities. Non-fatal (only the limit is used downstream, and §5.5's `o(L)/o(R)` absorbs it), but the sentence is not true.

**F4 [MINOR] — R1(b): no Poincaré argument is needed, and the proof should say why.**
The one-step ratio limit exists trivially: `λ_{j+1}/λ_j = r(c_j)` exactly by (1.1), `c_j → t`, `r` continuous on the corridor. §3.2 instead writes `x = lim λ_{j+1}/λ_j` by fiat. Positivity + ℓ² selection of the decaying root **is** written (lines 120–122) and is correct at the `+∞` end; the `−∞` end's reciprocal orientation is not spelled out. Cheap fix, and it removes any Poincaré-type question.

**F5 [MINOR] — rounding direction on the two explicit UPPER bounds.**
True values: `ρ = 0.91972710323…`, `1/κ_eff = 23.90106492878…`. The proof displays `ρ ≤ 0.9197271…` (3.5) and `1/κ_eff ≤ 23.9010649…` (3.7)/(7.2). Read without honoring the ellipsis, **both are false**. The banner and guard use correctly up-rounded `0.9197272` / `23.9010650`. An upper bound must be rounded up in the text of a claim whose only number this is. (`μ ≥ 2.001750769…` is fine — correct direction.)

**F6 [MODERATE] — the A8 guard's asserts are fail-capable but have a one-sided hole at exactly the contested factor of two.**
Mutation test, 5 injections: `S_LO→1/4` FIRED; `b=s/3` FIRED; growing root selected FIRED; `D(t)` sign flip FIRED. **`inv_keff = 2/kappa → 1/kappa` DID NOT FIRE** — G4's assert is one-sided (`< 23.9010650`), so a factor-of-two error in the index bookkeeping of §3.4 (the very thing §3.4/§3.5 exist to nail down) passes green as long as it makes the bound look *better*. G3 has a two-sided bracket on ρ; G4 has none on `1/κ_eff`. *Repair: add `inv_keff > 23.9010648`.*

**F7 [MINOR] — (3.7)'s harmonic-mean step is unwritten.** `κ_eff = (1/κ₋+1/κ₊)^{-1} ≥ K/2` given `κ± ≥ K` needs monotonicity in each argument. Stated only in the guard's docstring, not the proof.

**F8 [PASS] — R1(f), kill-#12 bypass CONFIRMED on the mathematics.** (3.2) is pure algebra from the certificate's own quoted `d` and `b`. No distorted-return functional, no return-quotient orientation, no return-sector theorem appears anywhere in the live proof — every grep hit is a disclaimer or inside the §3.5 retraction block. This is a genuine bypass, not a repair.

**F9 [PASS with one exception] — R1(g), retired authorities carry no load.** §3.5 is wholly inside a retraction block and is cited nowhere downstream: genuinely non-load-bearing, confirmed. **Exception:** U1E **§6.2's parenthetical** *"(With rho± = q\* the two rates are equal and kappa_eff = kappa/2.)"* sits inside the **live-by-incorporation** §6 and asserts the **retired** q\* identification. It bears no load on (3.7) (F7's monotonicity suffices), but it is a live assertion of a retired authority and must be struck.

### CROSS-CUTTING — THE LEAN ANCHOR

**F10 [MAJOR — recurrence of the round-2 KILL class] — the Lean kernel is a prose-named, unhashed authority.**
§0, §3.3 and the banner assert "the machine-checked kernel carries both backbone inequalities" with **no path, no hash, no commit, no release**. Round-2 integrity F-6(d) killed the previous bundle precisely for prose-named authorities — *"anchored strictly less than the RHO_Q document whose unanchored status was the original KILL."* The pattern has recurred at the new route's foundation.
The kernel does exist and is clean (`C:\Infanox\i3322-exact-wall\lean\I3322Kernel\`, Lean 4.30.0 + mathlib, **zero `sorry`/`axiom`/`native_decide`**) — but it is **outside the declared working set**, `RateCores.lean` is **untracked**, `I3322Kernel.lean` is **modified-uncommitted**, and `AxiomCheck.lean` does not cover `RateCores`. The hygiene guard H3 only string-matches the theorem *name* in markdown; nothing in the bundle checks the kernel at all.

**F11 [MAJOR] — the machine-checking claim is overstated on the single load-bearing input.**
`quarter_lt_window_lower` (`QuarterCeiling.lean:92–97`) is:
```lean
theorem quarter_lt_window_lower : (1 : ℚ) / 4 < 2508753845015185 / 10 ^ 16 := by norm_num
```
That is a **comparison of two rational literals**. It does **not** establish `S ≥ S_LO`. The proof writes *"The certified window gives S >= S_LO > 1/4 (also Lean-checked: quarter_lt_window_lower)"*, attaching "Lean-checked" to the composite. The substantive half rests on un-formalized interval arithmetic, **explicitly disclaimed in the kernel's own README**. Since `S > 1/4` is the *only* certified input the entire strictness route consumes, this is where the route's weight actually rests — and it is the least anchored link.
*In-bundle mitigation exists but is disclaimed away:* `guard_second_engine_projectors` PART B exhibits explicit PV-family strategies with 110-digit values `0.2500643651906…` (d=24) and `0.2505605862827…` (d=33), both `> 1/4` — that would establish `S > 1/4` **by exhibition**, which is stronger than any citation. It is declared **non-load-bearing**. Promote it, or anchor the window certification. (I attempted an independent see-saw at d ≤ 8 and only reached the 1/4 plateau — the excess is genuinely delicate and deserves a real receipt, not a literal comparison.)

**F12 [MODERATE] — `s(1−s) ≤ 1/4` is not the Lean statement.** The kernel has `scalar_quarter_ceiling : 0 ≤ t → -t + √t ≤ 1/4`. The identity chain `D+2b = t²−1+s = s(1−s)` is done on paper, not in Lean. Mitigated: I verified the chain symbolically myself and the A8 guard verifies it in sympy — so it *is* machine-checked, just not where the proof says.

**F13 [DISCLOSED — record it] — A8 did not reduce exposure to the [P] root's disclosed risk; it increased it.** The strictly-increasing single-valued `P` is certificate **§6**, squarely inside the disclosed-risk range §§6–9, and §10's label construction consumes §§6–9. §1 discloses the inheritance honestly, but the gate should record that the *new* route's foundation is the *riskiest* part of the root.

### R2 — ACCOUNTING INCORPORATION

**F14 [PASS] — flux identity citation correction (a) genuinely discharged.** Verified present in the full Cesàro source §2 and identical to (5.1); re-derived independently.

**F15 [PASS] — C_diag ≤ 20 and (5.5')/(5.6') follow.** `20 = 4` (marginal absolute sum, verified from the §0 display) `+ 8×2` (joint diagonals, `|a'b'−ab| ≤ 2`). Arithmetic correct and consistent with §0. (5.5') legitimately omits `T_I` from the numerator — the flux identity is exact, and `T_I` enters only through `M_I = 1−T_I` (this is *sharper* than the truncation receipt's `C_B(T_I+B_I)/(1−T_I)`, correctly so). The collar parenthetical is struck and §2 rewritten to justify it from compact interiority (A10 discharged).

**F16 [MODERATE] — dangling reference in a LIVE authority file (round-2 F-18 not discharged).** `U1E_DEPENDENCY_GRAPH.md:31` cites `dependencies/ENDPOINT_CESARO_UPPER_RECEIPT.md`. **That file does not exist** — it is `ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md`. The banner declares `authority/*.md` live and the hygiene guard scans this file, but has no pointer check. Also U1F §3.2 mis-cases the filename (`ENDPOint_…`).

**F17 [MODERATE] — the corrected provenance model is itself false for two of five dependencies.** The banner (F-4 correction) states dependencies/ carries *"FAITHFUL predecessor copies (full documents)"*. `G1_PROMOTED_UPPER_RECEIPT.md` and `TRUNCATION_UPPER_RECEIPT.md` both self-declare **"This extract carries only the statements consumed by U1"**. The extract→full-source repair (ledger 11) was applied to Cesàro but **not to G1** — and G1 is load-bearing: it supplies the compact interiority without which the limit label could reach `±1`, `b(t_inf) → 0`, and the entire strictness argument collapses. The F23/A4 extract pattern survives in the most load-bearing dependency, and the F-4 correction is inaccurate.

**F18 [MODERATE] — SCOPE-COINCIDENCE only half-adopted (round-2 F-15 not discharged).** H1's `LIVE_AUTHORED` does mirror the banner ✓. But **H2** (the kill-#12 check) hand-scopes to the U1F file alone, while the banner declares U1E §§4–7 and `dependencies/*.md` live. The round-2 process lesson — *"the hygiene guard's LIVE list must coincide with the banner's LIVE CHAIN definition"* — was banked in prose (ledger 15) but not in H2's code. This is the same failure shape as F-6a/F-7/F-8.

**F19 [MINOR] — retraction-block laundering (round-2 F-12) not discharged.** `strip_retraction_blocks` removes anything between the markers with **no check that the block contains retraction language**. §3.5 and the banner both place content inside such blocks.

**F20 [MINOR] — a green "PASS … strictness" line sourced from a retired authority.** `guard_kappa_bracket_retrodiction.py` consumes the **retired** q\* bracket and prints `PASS U1E strictness + retrodiction guard`. `guards/` is outside the banner's LIVE CHAIN, so nothing scans it. Rename or drop. *(Consistency note in the bundle's favour: the retired estimate `1/κ_eff ≈ 13.299` and the live bound `≤ 23.901` are mutually consistent — the live bound is ~1.8× looser, as a bound should be. No contradiction.)*

### R3 — ROUND-2 BLOCKER DISCHARGE

**F21 [BLOCKER] — the round-2 proof verdict does not exist.**
`VERDICT-U1E-AUDITOR-1-PROOF.md` is absent from its stated path, absent from anywhere under `[private-workspace]`, and absent from every git commit (only `VERDICT-U1-AUDITOR-1-PROOF.md` (round 1) and `VERDICT-U1E-AUDITOR-2-INTEGRITY.md` (round 2, integrity) exist).

The **only** surviving record of findings A1–A19 is the **audited party's own paraphrase** in `U1E_CORRECTION_LEDGER.md` entries 10–15. That paraphrase references A1, A2, A4, A5, A7, A8, A10, A13, A16, A17, A18, A19 — **twelve of nineteen**. **A3, A6, A9, A11, A12, A14, A15 have no discharge record anywhere in the repository.** The phrase "residual blockers 1–6" appears **nowhere** in the repo.

I can report on the round-2 **integrity** verdict (I read it): F3/F5/F11/F16/F19/F20/F23/F24 discharged; F-6, F-7, F-8, F-1/2/3, F-10 discharged and independently re-verified by me; **F-4 NOT discharged (F17 above), F-12 NOT discharged (F19), F-15 NOT discharged (F18), F-18 NOT discharged (F16).**

For the **proof** surface I can report nothing verifiable. The independence layer is being asked to certify discharge against a document it is structurally prevented from reading, with the discharge narrative supplied solely by the party being audited. **This is the round-2 failure mode — a claim certified by a scope drawn by the claimant — recurring one level up, at the gate itself.** R3 fails on availability of evidence, not on the merits.

### R4 — OPERATOR, ALLOCATION, BOUND STATUS

**F22 [PASS] — operator display.** Recounted: 3 marginal terms, absolute sum **4** ✓; **8** joint terms of modulus 1 ✓; classical max **0** ✓; qubit max **0.2500000000000013** ✓; CG extraction matches the repo concordance exactly ✓. A19 discharged — §0 now correctly says "three binary projection-valued measurements PER PARTY" (U1E's "six … acting on H_A, H_B respectively" was ambiguous).

**F23 [PASS] — allocation and limsup.** `|I| = L_d+R_d+1 = d` identically; `κ₋L_d = κ_eff(d−1)+O(1)` and `κ₊R_d = κ_eff(d−1)+O(1)`; (6.3) and (7.1) follow. Spot-check clean.

**F24 [PASS] — bound status consistently stated.** §3.3 ("BOUNDS … not rate claims"), §9 ("a derived inequality, guard-checked, and claims no sharpness"), (7.2) ("the anchored uniform bound") are mutually consistent, and §8's Θ(log) fencing is correct and iff-gated. Only wrinkle is F5's rounding, plus banner/STATUS (`23.9010650`) vs proof (`23.9010649…`) disagreeing in the last digit.

---

## RESIDUAL BLOCKERS (explicit — all must clear for promotion)

**B1 (fatal this round).** Produce `VERDICT-U1E-AUDITOR-1-PROOF.md`. Until the round-2 proof verdict is in the working set, no auditor can discharge R3, and A3/A6/A9/A11/A12/A14/A15 plus "residual blockers 1–6" are entirely unaccounted for. *This is the only blocker I cannot work around; everything else below is a few hours of writing.*

**B2.** Anchor the Lean kernel like any other authority: path, commit, content hashes, `AxiomCheck` covering every cited theorem, `RateCores.lean` committed. A guard that re-hashes the kernel, not one that string-matches a theorem name in markdown. (F10)

**B3.** Fix the `S > 1/4` anchor. Either state plainly that `quarter_lt_window_lower` checks only the literal comparison and anchor the window certification separately, **or** promote PART B's exhibited d=24/d=33 strategies to load-bearing — exhibition is the stronger receipt and it is already in the bundle. (F11, F12)

**B4.** Write §3.1. Quote certificate §10:792–796 and §6:446–451; state `c_{j+1} = P^{-1}(c_j)` with `P^{-1}` strictly increasing; conclude full-sequence monotonicity; derive `α = x_+` from it. Correct the §9 attribution (or delete the ρ± framing, which removes the dependency outright). (F1, F2)

**B5.** Carry the **full G1 source** as the Cesàro source is now carried, and correct the banner's provenance sentence — G1 and TRUNCATION are extracts. (F17)

**B6.** Guard/hygiene: extend H2's scan set to the whole banner live chain; add a two-sided assert on `1/κ_eff`; add a dangling-pointer check; make retraction-block exemption conditional on retraction language. (F6, F16, F18, F19)

**B7.** Text corrections: round the two upper bounds **up**; strike U1E §6.2's q\* parenthetical; fix "uniformly over all labels"; write the harmonic-mean step; fix the `ENDPOint_` typo. (F3, F5, F7, F9)

---

## CLOSING ASSESSMENT

Does `D_upper(ε) = O(log(1/ε))` promote **on the mathematics**? My honest answer: **the mathematics is sound and I could not break it.** I reconstructed the entire A8 chain from the [P] certificate without using the bundle's reasoning, and it holds — the band identity, the quarter ceiling, the Bellman identity's genuine presence in §11, the limit passage by continuity (which needs no continuity of `P` or `τ`, a subtlety the proof gets right by accident of construction), the root selection, the flux identity, the allocation, the operator. The route's own foundation turns out to be the elimination already audited at certificate §7 and already used at Cesàro §6, which is corroboration the bundle does not even claim for itself.

What it cannot do is **promote**, because promotion requires that an independent party be *able to check* the chain of custody, and on three counts it presently cannot: the round-2 proof verdict is missing, the Lean anchor is prose-named and its cited theorem proves less than the text says, and the two steps round 2 flagged in §3.1 are still asserted rather than written.

I flag one thing for the adjudicating track specifically. None of my findings are of the form "this doesn't match how it's normally done" — they are availability-of-evidence and internal-rigor failures, which remain binding under the program's own guardrail. But I also note that **F1–F3 and F5–F7 are all defects of *writing down* arguments I verified are true.** If a fourth round produces the same DENIED on the same six items, the correct read is a documentation-discipline problem, not a mathematical one — and the gate should say so rather than let a repeat denial read as mounting evidence against the theorem.
