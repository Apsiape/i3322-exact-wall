---
RECONSTRUCTED RECORD (2026-08-07). This verdict was delivered in-session
by the round-2 (U1E gate) proof-surface auditor on 2026-08-07 and was
not written to disk at the time -- a custody failure identified by the
round-3 proof auditor (finding F21/B1). This file is a verbatim
extraction from the session transcript
(5e738f3c-f46b-4ebc-9d44-8215213f7a82.jsonl, line 50417; duplicate
delivery of the same task-notification at line 50419), reconstructed by
the adjudicating track. XML entity escapes (&lt; &gt; &amp;) introduced
by the transcript's task-notification wrapper have been unescaped; the
body is otherwise byte-verbatim. The verbatim body begins below the
rule.
---

## AUDIT REPORT — U1E upper gate, mathematics surface

Independence note taken seriously: I re-derived every load-bearing identity and ran my own second-engine numerics rather than accepting any receipt's self-description.

---

### VERDICTS BY SURFACE

| Surface | Verdict |
|---|---|
| **Q1** identification ρ± = q*, both routes, bracket authority, kill-#12 bypass, countermodel | **FAIL** |
| **Q2** index bookkeeping (3.4)/(5.6)/(6.2)-(6.3); retrodiction guard | **PASS-WITH-CONDITIONS** |
| **Q3** error accounting §5 | **PASS-WITH-CONDITIONS** |
| **Q4** allocation, limsup, definitions | **PASS-WITH-CONDITIONS** |
| **Q5** U1-blocker discharge (B1-B6, F1-F17) | **FAIL** (one blocker migrated, not discharged) |

---

### FINDINGS

**A1 — KILL. The certified bracket (3.2) has no receipt anywhere in the working set.**
Location: `U1E/proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1E.md` (3.2); `authority/U1E_DEPENDENCY_GRAPH.md` node "[P] certified q* bracket".
I grepped every file (all types) in `U1E/`, `U1/`, and the V28.1 bundle for `860375`/`860376`/`0.8603`. The digits `0.860375661183927` / `0.860376162879071` occur **only** in U1E's own proof, its own two-routes document, and its own guard, where they are hard-coded string constants. There is no source file, no SHA anchor, no derivation, no replay. The claimed scope statement — "retained as live by the hostile correction audit for the EXACT carrier … the kill in that audit concerned only transfer to near-maximizers" (lines 119-121) — cites an audit that does not exist in the working set; grep for "correction audit"/"near-maximizer" returns only U1E's own two self-assertions. **Q1(c) answer: the scope claim is unverifiable and there is no bracket receipt at all.** This is the sole source of strictness in the bundle as written, and it is exactly the defect class the U1 gate killed (load-bearing strictness resting on unanchored predecessor material), re-instantiated in a new costume.

**A2 — KILL (as written). The λ_j = c/|j|, ρ = 1 countermodel is excluded by A1's unanchored constant and by nothing else.**
Q1(e): walking the chain for a ρ = 1 profile — §3.1 (tails converge), §3.2 (pair asymptotically (−t*,−t*)), §3.3 (multiplier continuity), §3.5, §5, §6, §7 all survive verbatim; the *only* step that fails is (3.3)'s `q* < 8604/10000`, which is (3.2). The bundle also explicitly renounces the one receipted alternative: `U1E_DEPENDENCY_GRAPH.md` states "strictness comes from the q* bracket, **not** from S vs 1/4" and "U1E does NOT consume S > 1/4 anywhere". Having bypassed kill #12 by discarding the quarter-ceiling route, the proof stranded strictness on an unreceipted numeral.

**A3 — MAJOR. The "two independent routes" are not independent.**
Route (a) §3.2 and route (b) §3.3 share the *same* premise (§3.1: the whole label tail converges to a single label) and terminate at the *same* unanchored object (q*). Route (b) additionally introduces a new unreceipted object: "the h = r^{−2} eigenvalue of the current characteristic map" (a linearization/derivative), equated without warrant to the amplitude transport multiplier (a function value), and cited to a "hyperbolicity package" that (i) is not in the working set and (ii) the governing source explicitly *retired* (`ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md` §11: "endpoint hyperbolicity … unnecessary"; §4: "No derivative of P, τ, or r_B is required"). A confirmation route may not be scored as independent when it consumes the primary route's load-bearing premise.

**A4 — MAJOR. §3.2 silently assumes the exact identity its own source refuses to assume, and the live-chain extract deletes the warning.**
The sealed source (`I3322_V28_1.../dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md`) defines ρ₊ = r_B(α)·r_B(x₊) with **two distinct** endpoint labels α = lim u_n and x₊ = lim P(u_n), and §9 states verbatim: *"valid only after an additional endpoint-pairing identity identifies r_A(x₊) = r_B(β). That identity was not yet certified and is no longer silently assumed."* U1E's (3.1) `ρ+ = r_B(−t*)²` **is** that identity (r_B(x₊) = r_B(α)). U1E's dependency extract `ENDPOINT_CESARO_UPPER_RECEIPT.md` carries neither §5's product form, nor §2's flux identity, nor §9's warning — so the live chain cannot see the limitation it violates. This is the F5/F23 pattern (extract deletes the source's claim-limiting notice) recurring at the new proof's center, one entry after the ledger claimed to have fixed that pattern.

**A5 — MAJOR (repairable in one line). §3.1's monotonicity is a strengthening of the cited receipt.**
The receipts give only that the *response* orbit (u_n) is monotone. The label sequence interleaves c_{2n} = u_n with c_{2n+1} = −P(−u_n) (public certificate §10), so its convergence to a single value is a genuinely stronger claim — and it is precisely the claim A4 needs. **The warrant does exist and U1E never cites it:** the certificate's §1 certified inputs state "the full interior zero locus is a one-to-one **strictly increasing** relation". With P increasing and c_j = P(c_{j+1}), monotonicity of (c_j) follows by induction, hence single-valued tail limits and α = P(α) = x₊. Without that citation the alternative closure P(α) = −α is not excluded — and under it the proof's own §3.3 reciprocity r(t)r(−t) = 1 forces ρ = 1 **exactly**. Two adjacent sentences in §3.2 ("alternating between the labels" vs "asymptotically (−t*,−t*)"; "carrier orientation (+t* → −t*)") read as supporting opposite conclusions.

**A6 — MAJOR. Three `[P]` nodes of the dependency graph have no document in the working set.**
"equality-module: nonfixed ordered response orbit", "sextic tail-closure", "wall-comparison selection". Zero grep hits outside U1E's own prose. The proof's banner claims "Every consumed receipt is named with file"; these are named with adjectives.

**A7 — VERIFICATION (positive, and decisive on the mathematics). ρ± = q* is TRUE; I confirmed it independently to ~10 digits by a route the bundle never uses.**
At a constant tail label t the Jacobi data are D = d(t,t) = t²−1, b(t) = √(1−t²)/2, and Hλ = Sλ forces x + 1/x = (S−D)/b for x = lim λ_{j+1}/λ_j. Evaluating at the plateau label t* = 0.8782729451808125 with S = S_LO:
```
mu = 2.00565663046839      x = 0.927564580039505      x^2 = 0.860376050143863
```
`x² = 0.860376050143863` lies **inside** the asserted bracket, and matches the blind round's quoted `q* = 0.860376050505…` to 9 significant figures. Independently, running U1E's own second engine (`guard_second_engine_projectors.optimize_profile`, d = 120) I get a converged profile with a genuine plateau at |c| = 0.87823 and Perron-vector outward ratios → 0.9276 = √q*. So the identification's *conclusion* is sound; what fails the gate is its *warrant* (A1-A6).

**A8 — CONSTRUCTIVE REPAIR (verified). Strictness is elementary and needs no bracket, no selection theorem, no quarter-ceiling mechanism.**
From the Bellman equality at the limit pair, S − (D + 2b) = (g(α) − b(α))²/g(α) ≥ 0, while D + 2b = t²−1+√(1−t²) = s(1−s) ≤ **1/4** (s = √(1−t²)) for every label. Certified S > 1/4 therefore gives strict inequality, hence g(α) ≠ b(α), hence μ > 2, hence (λ ∈ ℓ², λ > 0 selects the decaying root) ρ± = x² < 1. Uniformly, with b ≤ 1/2:
```
mu >= 2 + 2(S - 1/4) = 2.00175077  =>  rho <= 0.91972710
kappa >= 0.08367828 per index, kappa_eff >= 0.04183914,  1/kappa_eff <= 23.9010649
```
This is an unconditional, receipt-light, explicit constant. It consumes only: the certified S > 1/4 (Theorem-S signed statement), the Bellman/Jacobi structure (public certificate §11), and the Sprint-1295 word-matrix forms of d and b. Recommended as the replacement for §3.2-§3.4. (Only outstanding citation need: a one-line in-corpus receipt for d(t,t) = t²−1; I took it from U1E's own second engine, corroborated by max_t[d+2b] = 1/4 being *exactly* the certified qubit/qutrit maximum and by the guard's ladder reproducing I3322 values.)

**A9 — MAJOR. The bundle disclaims its own best receipted input.** See A8 vs `U1E_DEPENDENCY_GRAPH.md`'s "S > 1/4 … is NOT used by U1E". Optimizing for "kill #12 untouched" cost the proof its only anchored strictness mechanism.

**A10 — MINOR. §2's collar parenthetical is imported and incoherent here.** "b ≥ b₀ > 0 away from the endpoint collar, whose state mass is paid at O(eps) by the collar receipt": all carrier labels lie in Z ⋐ (−1,1) so there is no collar mass to pay; and an additive O(ε) payment would be fatal at the theorem's own scale. b ≥ b₀ follows directly from compactness of K. The collar receipt exists (G1 source §4) but is not in U1E's G1 extract.

**A11 — MINOR (provenance). (5.1) is mis-cited.** Attributed to "the endpoint-Cesàro receipt"; U1E's extract of that receipt contains no flux identity. The identity is in the sealed source §2.
**A12 — VERIFIED. (5.1) is exact.** I re-derived it: Σ_{j∈I} λ_j(Hλ)_j = S·M_I and equals ⟨λ_I,H_Iλ_I⟩ + b(c_{a−1})λ_{a−1}λ_a + b(c_b)λ_bλ_{b+1}. Only the two cut edges are unpaid. b ≤ 1/2 ✓.

**A13 — MINOR. C_diag = 12 recount.** The I3322 CG functional's coefficient ℓ¹ norm is 4 (marginals, |−1|+|−1|+|−2|) + 8 (joint, modulus 1) = 12 ✓, consistent with the standard form and with classical bound 0 / qubit max 1/4. But the per-term bound is loose in the wrong direction: a *joint* term's diagonal is a product of two projector diagonals, so |a′b′ − ab| ≤ 2, giving 4 + 16 = 20, not 12. Immaterial (C_B is existential), but the "= 12" is presented as derived.

**A14 — VERIFIED. (5.5) is correct and strictly tighter than the truncation receipt.** The receipt's bound carries C_B(T_I + B_I)/(1−T_I); U1E's derivation via the normalized Rayleigh quotient legitimately drops the T_I numerator term (omitted diagonal mass is already absorbed by M_I). Three-row table (5.2) is exhaustive: interior blocks are copied verbatim (truncation receipt), the cut off-diagonals coincide with the compression's zeros, and only the diagonals at the two severed retained indices a, b change. (5.3) is valid with R_max ≥ actual ratio, consistent with (1.1).

**A15 — VERIFIED. §3.5, §5.5, §6, §7 all check.** (3.4): ρ is a two-index ratio ⇒ λ_j ∼ ρ^{j/2} ⇒ λ_j² ∼ e^{−κj}, so κ acts per index in mass estimates — consistent with (5.6), with the source's per-characteristic-site κ, and with (6.2). (5.7) needs no separate receipt: λ_bλ_{b+1} ≍ λ_b² gives the same exponent. (6.1)-(6.2): L_d + R_d + 1 = d exactly ✓; κ_−L_d = κ_+R_d = κ_eff·d + O(1) ✓; O(1) absorbed by o(d) ✓. §7 is quantifier-clean (η fixed → eventual bound → ratio limsup ≤ 1/(κ_eff−η) → η↓0), and S − S_d ≤ S − V_{I_d} has the correct direction.

**A16 — MINOR. §3.6 misstates its own magnitude.** Independent computation: 2/(−log q_hi) = 13.2991468417991093, so |scout − endpoint| = **8.9e-13**, not the stated "≈ 9e−11". Guard runs and passes (tolerance 5e-11); its interval [13.2990952753131, 13.2991468417991] reproduces mine exactly.

**A17 — MINOR/MAJOR. The "independent" two-routes document's numerics do not reproduce.** It states κ ∈ [0.150385586528, 0.150386169994] and 1/κ_eff ∈ [13.2990952564, 13.2991468542] and "within 1.2e-8"; correct values are [0.150385586668914, 0.150386169780479], [13.2990952753131, 13.2991468417991], 8.9e-13. Every quoted endpoint is wrong at the 11th-12th digit. A document offered as an independent derivation should not disagree with the bundle's own guard.

**A18 — MAJOR (evidential inversion). The retrodiction argues against the bundle, not for it.**
That the retracted scout 13.2991468418 equals 2/(−log q_hi) to 9e-13 shows the historical scout and the "certified" bracket's **upper endpoint** are the *same computation* — i.e. the bracket is not independent of the retracted numeric it is said to explain. The two-routes document escalates this to "strong independent evidence the identification types"; on a hostile reading it is evidence of provenance entanglement between a retracted constant and an unreceipted one (A1). Downgrade to: "consistency note, no evidential weight".

**A19 — MINOR. §0 definitions.** S_d says "six projection-valued binary measurements acting on H_A, H_B respectively" — it is three per party; and the eight joint terms of "the fixed I3322 Bell operator" are never displayed, although §5.3 recounts their coefficients. Well-formed enough to survive B5/F14, but the object §5 counts is not fully written down.

**A20 — NOTE (positive, integrity spillover).** All three U1E guards run clean for me. `guard_live_upper_authority_hygiene.py` is genuinely fail-capable and the retraction-block exemption works: I injected `13.299` outside a retraction block into a scratchpad copy of the live proof and H1 fired (`AssertionError: killed literal '13.299'`). H5's five Theorem-S hashes verify: I independently re-hashed `CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md` (`15e44422…d66b0`) against both the external certificate directory and a byte-identical in-repo copy. PART A of the second engine (symbolic projectors, arbitrary angles, m = 3..8, both matchings, complements) passes.

**A21 — NOTE. Ledger entry 5's "the scalar-orbit document is NOT consumed" is equivocal.** The anchored public certificate *is* the scalar-orbit theorem (revised/retitled); §§10-12 supply exactly the diagonal Schmidt form, positive λ, labels, Jacobi recurrence, (1.1) and the alternating blocks. I verified U1E §1's §12 quotation is verbatim-accurate, and that (1.1) λ_{j+1}/λ_j = g(c_j)/b(c_j) is certificate §11 verbatim (reconciled with the Cesàro receipt's r_B = √(g(t)/g(−t)) by K(c_j) = 1 on the full-zero locus — a step U1E should state, since it also underwrites §3.3's reciprocity).

**A22 — NOTE. No independent large-d confirmation of the exponential rate exists.** Running the second engine's optimizer myself (d = 20…260) the deficit decays with observed rate/step 0.110, 0.091, 0.080, 0.070, 0.052 over d = 30…80 — bracketing the (retracted) κ_eff = 0.0752 — then saturates at ≈ 6e-6 for d ≥ 100 (float64 fixed-point iteration, not the true S_d). Consistent with the claim; decisive of nothing.

---

### Q5 — U1-BLOCKER DISCHARGE TABLE

| Blocker | Status |
|---|---|
| **B1 (KILL)** exhibit (1.1)-(1.2) at endpoint datum, Q = S, gains identified | **NOT DISCHARGED — migrated.** Bypass is a legitimate strategy, but the replacement's strictness input is unreceipted (A1) and excludes the countermodel only by assertion (A2). |
| **Auditor-2 blocker 1 (KILL)** discharge F7(a)/(b) or restore Sprint-1198 with receipt | **NOT DISCHARGED.** (a) is genuinely bypassed (F(q)/q_ret/RHO_Q absent — Q1(d) is clean; guard H2 confirms; I re-grepped). (b) is replaced by a new undischarged object, not closed. |
| **B2 / F2 / F3** carrier structure into live chain with real anchor | **DISCHARGED.** Public certificate v3.1.0 + DOI; five hashes independently re-verified by me; §§10-12 do license the consumed structure. Self-referential anchor eliminated. |
| **B3 / F9 / F10** charge retained endpoint diagonal, derive C_B | **DISCHARGED** (§5.2-5.4), modulo A13. |
| **B4 / F11** receipt or derive T_I | **DISCHARGED** (§5.5, derived; mis-citation deleted; bound is tighter than the receipt). |
| **B5 / F13 / F14** define S_d, D_upper; resolve trichotomy | **DISCHARGED** with A19; the false "trichotomy" is retracted honestly and ledgered as a stage-report error. |
| **B6** two-tail algebra, every-d, limsup | **DISCHARGED** (A15). |
| **B7 / F20 / F21 / F22** guard disclosures or demotion | **DISCHARGED.** Small-d fixture demoted to `[V]` with a full, candid disclosure (argmax window rule, non-nested chains, unrecomputed payload hash, newline defect). |
| **F6 / E1** endpoint-limit receipt | **PARTIAL.** The substance is now right (Z closed and compactly interior ⇒ limits ∈ Z, with the exact labels ±t*), but the monotonicity warrant is uncited (A5) and K(limit) = 1 is used unstated (A21). |
| **F5 / F23** retraction notice, guard scoping | **DISCHARGED** for G1 (restored in a marked block; guard rescoped and injection-verified, A20) — but **the same pattern recurs undetected** in the Cesàro extract (A4). |
| **F15 / F16 / F17 / F19** banner, gate rule, STATUS, unbacked file | **DISCHARGED.** |

---

### GATE VERDICT

**DOES NOT PROMOTE.** D_upper(ε) = O(log(1/ε)) does not pass on the mathematics surface as written.

Sharp statement of where I land, since it is unusual: **the theorem is true and I verified its central constant independently (A7); the bundle does not prove it.** The chain's strictness — the sole source of κ_eff > 0, hence of the entire claim — rests on a numerical bracket with no receipt anywhere in the working set, defended by an audit-scope claim that also has no receipt, confirmed by a "second route" that is not independent, and supported by a retrodiction whose actual content is that the bracket and a retracted numeral are the same computation. That is the U1 kill relocated, not discharged.

**Residual blockers (all repairable; two are one-liners):**
1. **(KILL)** Produce a real receipt for the q* bracket — file, hash, exact-arithmetic replay — **or** delete §3.4 and adopt the elementary route of **A8** (S > 1/4 ≥ band top ⇒ ρ ≤ 0.919727, 1/κ_eff ≤ 23.9011), which is anchored, unconditional, and yields an explicit constant. I recommend the latter; it also retires A3, A6 and A18 at a stroke.
2. **(KILL/MAJOR)** Cite the certificate §1 "one-to-one strictly increasing" fact and write the two-line induction giving monotonicity of (c_j), single-valued tail limits and α = x₊ (A5) — this is what actually discharges A4's pairing identity, and it must be stated *as* the discharge of the source's §9 warning.
3. **(MAJOR)** Restore §9 of the Cesàro source (and §4-§5's two-label structure, and §2's flux identity) into `dependencies/ENDPOINT_CESARO_UPPER_RECEIPT.md`; an extract that omits the source's own limitation on the step the proof takes is the F23 failure mode, not a hygiene success.
4. **(MAJOR)** Ship the sextic tail-closure, wall-comparison selection and equality-module documents, or remove those `[P]` nodes.
5. **(MAJOR)** Withdraw the "two independent routes" framing; withdraw or re-scope the h = r^{−2} eigenvalue claim (no receipt; the governing source retired hyperbolicity).
6. **(MINOR)** Fix §3.6's "9e−11" → 8.9e−13; correct the two-routes document's κ and 1/κ_eff intervals and its "1.2e-8"; re-label the retrodiction as a consistency note with no evidential weight; state K(c_j) = 1 where reciprocity and (1.1)↔r_B are reconciled; strike or rewrite §2's collar/O(eps) parenthetical; fix §0's "six … respectively" and display the eight joint coefficients; note C_diag ≤ 20 by the two-sided product bound.

Θ(log) remains correctly fenced as a conditional corollary and does **not** promote.
