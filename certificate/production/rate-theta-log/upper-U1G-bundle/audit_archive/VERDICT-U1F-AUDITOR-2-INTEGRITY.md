# VERDICT — U1F round-3 gate, INTEGRITY surface

> Redaction note (2026-08-10): a private-workspace path fragment neutralized to [private-workspace]; no other byte changed.

PROVENANCE: delivered in-session by the round-3 integrity-surface
auditor (background agent "U1F round-3 gate: integrity") on 2026-08-07
and written to disk the same day by the adjudicating track, verbatim.
HTML entity escapes from the delivery wrapper (&lt; &gt;) restored to < >.

---

# GATE VERDICT: **DENIED** — the integrity surfaces do not promote

Round-3 bundle U1E/U1F. Default FAIL sustained. Substantial real repair happened (the public-certificate surface is now the strongest thing in the bundle), but the two findings the round-2 auditor banked as *process lessons* — the scope-coincidence rule and retraction-block laundering — are **written into the ledger and not implemented on disk**, and I broke both by injection.

## Surface verdicts

| Surface | Verdict |
|---|---|
| **S1** Round-2 discharge (F-1..F-18, KILL F-6) | **FAIL** |
| **S2** Guards | **FAIL** |
| **S3** Manifest + changes | **PASS-WITH-CONDITIONS** |
| **S4** Scope | **PASS-WITH-CONDITIONS** |

## What is genuinely discharged (verified on disk, not from the ledger)

- **F-1/F-2/F-3 — fully discharged, best surface in the bundle.** Public tree `C:\Infanox\i3322-exact-wall\certificate\production\theorem-S-spatial-attainment-at-S\`: header now reads `PROMOTED (release v3.1.0)` with the §§6–9 residual-risk note; `090aecebe7d5c150…` matches proof §1, guard H5, **and** `MANIFEST_SHA256.txt` (all 12 entries re-verify). All five quoted hashes reproduce exactly. U1F §1 names the doc as *the* scalar-orbit document and inherits the risk explicitly; ledger 13 retracts the false claim.
- **F-6 (the KILL) — discharged for the live chain proper.** Grep of the banner's live chain: U1F mentions sextic/selection/hyperbolicity/bracket **only in the negative** ("no selection theorem, no sextic, no hyperbolicity, no numerical bracket"); the four occurrences in `…U1E.md` §3.1/§3.4 sit inside the explicitly-superseded §§0-3. The A8 route's quoted authority is real: certificate §1 line 73 says verbatim *"the full interior zero locus is a one-to-one strictly increasing relation"*, and §11 gives `λ_{j+1}/λ_j = g(c_j)/b(c_j)` as claimed.
- **F-6a byte-check — passes.** `dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md` is **byte-identical** to the sealed v28.1 copy (`1ed80a067d3afcbd…`, 9330 B, `cmp` clean). The line-28 `q_ret` sentence is gone.
- **F-8 — clean.** `guards/` holds four `.py` and nothing else; the phantom `__pycache__` manifest entry (present at seal 3c447f59) is gone; running all four guards creates no `__pycache__` and mutates nothing.
- **F-10/F-11 — discharged.** Guard prints `|diff| = 8.907e-13`; two-routes note relocated to `artifacts/commission_history/` with its 11th-digit errors documented in ledger 12 and README.
- **Manifest:** 30/30 hashes exact, excludes itself, **zero** unlisted files.
- **Change list:** verified against `git diff 3c447f59 4ab222f2 -- U1E` — complete and honest, no undeclared moves.
- **A8 guard is genuinely fail-capable:** 6/6 injections fire (S_LO→1/4 and →0.2499 both kill `mu>2`; ρ threshold tightened to 0.9197271 fails; 1/κ_eff tightened to 23.9010649 fails; band identity broken fails).

## Numbered findings

**1. [MAJOR] The SCOPE-COINCIDENCE RULE (ledger entry 15) is false on disk.** Banner defines the live chain as `authority/*.md`; `guard_live_upper_authority_hygiene.py` `LIVE_AUTHORED` hard-codes 3 of the 4, omitting `authority/PROMOTED_LOWER_RATE_RECEIPT.md`. Injected: **deleting** that file → guard PASSES. Injecting `The coefficient 13.299 is asserted; g(1)g(-1)=0 holds.` into it → guard **PASSES**. This is verbatim the round-2 auditor's banked lesson ("the hygiene guard's LIVE list must coincide with the banner's LIVE CHAIN definition"), adopted in prose and not implemented. The omitted file is also stale ("This U1 bundle… if U1 promotes").

**2. [MAJOR] F-4 NOT discharged — third iteration.** Banner: `dependencies/` carries "FAITHFUL predecessor copies (**full documents**…)". Two of five are self-declared **extracts**: `G1_PROMOTED_UPPER_RECEIPT.md` ("*promoted upper-only receipt extract*", 2055 B vs sealed 4042 B) and `TRUNCATION_UPPER_RECEIPT.md` ("*upper-only receipt extract*", 1571 B, drawn from two sealed sources).

**3. [MAJOR] The G1 extract commits the exact F23/F-6a defect the bundle claims to have closed.** Sealed source status line: `**Status:** **PROVED CANDIDATE; promotion audit may attack provenance/typing…**`. The extract replaces this with `**Authority:** promoted G1`, and the graph types it `[P] G1`. The source's status-limiting line is deleted by an extract — the same pattern ledger 11 says was "closed by carrying the full source" for Cesàro. G1 is load-bearing (U1F §2: corridor, `m_g`, `b_0`, `R_max`).

**4. [MAJOR] The replacement full source carries a rival unreceipted strictness proof inside the live chain, unsuperseded.** Cesàro §6, "*Why 0<ρ±<1 needs no numerical multiplier certificate*", derives strictness from "the **Sprint-1198** amplitude-elimination hypotheses" (prose name, no file, no hash in the bundle) plus "the **quarter-ceiling obstruction**" — the mechanism ledger entry 2 declares BYPASSED. U1F §3.1 explicitly discharges the source's §9 warning; **nothing anywhere names §6**. The round-2 KILL was "the retained Cesàro receipt names an unreceipted strictness supplier inside my declared live chain." That sentence has moved from line 28 to §6. Relocated, not discharged.

**5. [MODERATE] F-12 laundering fully open — demonstrated.** Injected into `…U1F.md`: a `RETRACTION-BLOCK` containing `THEOREM: the coefficient is exactly 13.299 and g(1)g(-1)=0 holds; this is a live assertion.` → **PASS**. Same in a dependency copy → **PASS**. No check that blocks contain retraction language. Contentwise, **U1F §3.5 is not pure history**: it asserts `ρ± = q* = g(−t*)/g(t*)` and an auditor's ~10-digit verification — precisely the object round-2 F-6(b)(c) attacked — inside the exempt region.

**6. [MODERATE] F-15 NOT discharged.** H2 scans only U1F; the banner's live chain is larger. Live-chain grep finds `F(q)`/`RHO_Q` in `…U1E.md:136` and `F(q)` in a dependency. The H3 docstring still describes *U1E* tokens ("the identification rho± = q*; the certified bracket; the three-row table") while the code checks U1F tokens.

**7. [MODERATE] F-14 NOT discharged.** H5's five hashes are a hand-maintained dict, not parsed from proof §1 (they agree today — I verified all five independently — but nothing enforces it). The soft `SKIP` survives: an auditor without the public tree gets an all-green run with the only real predecessor check silently skipped.

**8. [MODERATE] Two displayed upper bounds in the live proof are literally false as written.** (3.5) `rho± <= 0.9197271…` — true value **0.919727103237**. (3.7)/(7.2) `1/kappa_eff <= 23.9010649…` — true value **23.9010649288**. Banner and STATUS carry the correct **0.9197272** / **23.9010650**, and the guard asserts against *those* — while H3 **requires** the truncated tokens `0.9197271` / `23.9010649` to be present in the proof. The guard enforces the false display and separately verifies the true bound. (7.2) is the theorem line.

**9. [MODERATE] F-17 NOT discharged.** `U1E_DEPENDENCY_GRAPH.md`: "G1's inputs are the storage/gluing/reserve receipts, **independent of (S)**." Theorem-S §14 *Exact dependency boundary* lists exactly those Theorem-(N) items (limiting storage, reflection-gluing K≥1, zero-set localization) among what (S) itself consumes. Verbatim uncorrected; the U1F CORRECTION section does not touch it.

**10. [MODERATE] F-7 stamp is path-only.** `git diff` reports **R100** (100% identical content) for both relocations. Zero content change → **no SUPERSEDED stamp, no "gate DENIED" note** in either document. The self-audit still reads as a clean PASS table certifying the killed route: `| rho_pm = 1 excluded | PASS | explicit rho <=> q_ret orientation + neutral quarter ceiling |`. Same defect in `proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md`, whose in-file header still says `**Status:** **UPPER-ONLY PROMOTION CANDIDATE.**`

**11. [MODERATE] Unanchored authority under a [P] root.** Sealed G1 §1 sources its two load-bearing endpoint reserves to `08_ENDPOINT_RECEIPT_PROVENANCE.md` — absent from U1E, absent from the sealed v28.1 bundle, absent from `SOURCE_HASH_ANCHORS.json` (it exists at `[private-workspace]/i3322_consolidated_promotion_bundle/new_docs/`, unanchored). The extract deletes even its name. Original-F-6 class, one level down.

**12. [MINOR] F-13 claim false as worded.** STATUS: "no guard output file is manifest-sealed; guards print to stdout only." `artifacts/small_d_demoted/GUARD_SMALL_D_STDOUT.txt` and `small_d_endpoint_projector_truncation_results.json` are manifest-sealed guard outputs, and the shipped demoted guard writes the JSON (line 386). Substantively harmless — I confirmed the write is now idempotent and breaks no seal.

**13. [MINOR] F-16 pointer still mis-wired.** README/graph say "see its NOTE"; the printed NOTE covers only the PV-family lower-bound caveat. The load-bearing caveat (PART B uses PV open-endpoint padding, **not** the endpoint-projector completion) lives only in `artifacts/small_d_demoted/DISCLOSURE.md`, which neither pointer names.

**14. [MINOR] F-18 residuals.** README says "three guards" then lists four. `SOURCE_HASH_ANCHORS.json`'s note ("Raw predecessor copies are deliberately excluded…") now contradicts the banner and the shipped full Cesàro source (which carries scouts 0.8616013 / 13.4262). Banner cites "retraction-block additions ledgered in entries 6 **and 11**" — entry 11 added no block.

**15. [MINOR] Unflagged conflict introduced by the replacement source.** New Cesàro §3 asserts realization "in local dimension at most `|I|+3`"; U1F §4 asserts "exactly `d = |I|` — no dilation, no padding". Nothing flags it.

## S4 assessment (asked explicitly)

Θ(log) is conditional at **every** occurrence — banner, STATUS, graph (×2), U1F §8, U1E §8, and even the historical U1 doc (§8.1 is fenced "if and only if"). Nothing self-promotes. **The safe-bound / retired-scout distinction is clearly maintained**: §3.3 "The displayed decimals are BOUNDS…, not rate claims"; §9 "a derived inequality, guard-checked, and claims no sharpness"; the 23.90 bound derives from `S_LO` and `b ≤ 1/2` alone and is strictly *weaker* than the retired 13.299, which now appears only inside retraction blocks. Conditions: finding 8, plus "unconditional/unconditionally" (banner, (7.2)) overstates — it is unconditional relative to the *retired bracket*, not relative to the [P] roots' disclosed residual risk (§9 does disclose).

## Residual blockers for round 4

1. Generate the hygiene guard's scan set from the banner's live-chain globs — implement the adopted rule, and ship the injection test.
2. Add a retraction-block **content** check (retraction/kill/history language required, live theorem assertions forbidden), or drop the exemption for a file+line whitelist.
3. Carry G1 and TRUNCATION as full byte-identical sources, or correct the banner to "two extracts, three full copies" and audit what each extract deletes. Restore G1's `PROVED CANDIDATE` line and reconcile the `[P]` typing against a hashed promotion commission.
4. U1F must disclaim Cesàro **§6** (and Sprint-1198) by section number, as it already does for §9; and flag §3's `+3` typing.
5. Make (3.5)/(3.7)/(7.2) agree digit-for-digit with the guard and banner.
6. Stamp the two archived documents **and** `proof/…U1.md` in-document (gate DENIED, route killed).
7. Correct "independent of (S)" against Theorem-S §14; mark the pre-U1F graph block HISTORICAL, not "superseded where they differ".
8. Parse H5's hashes from proof §1; make H5 hard-fail (or non-zero exit) when the public tree is absent; widen H2 to the full live chain.
9. Anchor `08_ENDPOINT_RECEIPT_PROVENANCE.md` by path + hash.

The recurring structural pattern across findings 1, 3, 4, 5, 6 and 10: **every claim about the bundle is still certified by an instrument whose scope is narrower than the claim**, and every "closed" defect has reappeared one level down. That is the same failure the round-2 auditor named, and it is why this round does not promote either.
