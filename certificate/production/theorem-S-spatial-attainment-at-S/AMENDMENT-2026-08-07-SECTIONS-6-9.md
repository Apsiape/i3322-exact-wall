# Certificate amendment (2026-08-07) — the §§6–9 residual risk is DISCHARGED

**Scope.** This amendment records the discharge of the residual proof
risk that this certificate's status materials have disclosed for its
Sections 6–9 (strict graph and conull response action; fixed-point
nullity; Borel transversal; scalar disintegration and normalization)
— the disclosure carried in `STATUS.json`, the proof document's
header, and inherited by every downstream consumer including the rate
note.

**The discharge.** The full expanded write-up is published at
`sections-6-9-expansion/U2-SECTIONS-6-9-EXPANDED.md`: 25 numbered
lemmas and 14 displayed claims covering every step of §§6–9, each
with complete proof, input anchors (file and line), and an explicit
pointwise/a.e. quantifier label; an inputs table, an interface-out
table checked row-by-row against §10's consumption, a quantifier
audit, and an axiom inventory (nothing beyond standard Borel-space
facts, the certificate's promoted inputs, and the Lean kernel — no
Rokhlin, no abstract disintegration-uniqueness theorem, no
measurable-selection theorem).

It was gated blind before this amendment, and the complete verdicts
ship alongside it: round 1, a hostile proof surface (verdict: no
mathematical obstruction; denial on citation anchors only) and an
independent countermodel-hunting adversary (verdict: NO
COUNTEREXAMPLE across 22 constructed attacks, with independent
numerical confirmation that the §7 elimination margin is strictly
positive at the certified window value: +8.75e-4, vanishing exactly
at S = 1/4); round 2, a diff-scoped re-gate of the repaired document
(verdict: CLEAN — every repair verified item-by-item, every new
quotation checked verbatim against the live files, the two
mathematically substantive repairs re-derived independently).

**Two corrections of record for THIS certificate, effective by this
amendment (the underlying files are hash-frozen — see below — so the
corrections live here):**

1. **Re-anchoring of the §1 certified input (line 73) and its §14
   pointer (line 1073).** The strict one-to-one increasing property
   of the FULL interior zero locus is proved and boxed in
   `../theorem-N-four-receipts-at-S/CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md`
   (box at line 224; §7 horizontal exclusion on the full source
   domain, §8 dual-tie/vertical exclusion, §9 assembly; the raw
   first-contact vs `R_0^{-1}(0)` distinction at its lines 208–210).
   The summary at `CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md`
   :115–126 remains the anchor for strict Monge only; its lines
   124–125 are pointers to the boxed theorem, not standalone proofs.
   Both blind rounds independently converged on this re-anchoring.

2. **Binding of the §10 interface.** §10's "Choose one conditional
   orbit measure having all these properties" (line 742) is bound to
   the enumerated interface of the expansion's Lemma 9.6: a single
   orbit measure carrying properties I1–I9 (single countable orbit;
   purely atomic probability; every atom on the full-zero locus,
   pointwise; the fibre transport laws for both involutions; strict
   positivity of every atom; and the product laws, which hold
   identically on (−1,1)). §10 consumes exactly this interface and
   nothing more (expansion table OX.2, verified against §10's text
   in both gate rounds).

**Hash-freeze note (why the underlying files are unchanged).** The
proof document (`CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md`) and
`STATUS.json` are content-hash-pinned by the promoted rate bundle
(`certificate/production/rate-theta-log/upper-U1G-bundle/`, proof
§1a) and must remain byte-identical for that bundle's guards to
verify. Their residual-risk sentences therefore remain in place as
historical text; this amendment is the dated record that the risk
they describe is discharged. This follows the repository's standing
amend-never-replace practice.

**Effect on downstream disclosures.** The rate note's §4.1/§5
inheritance statements referred to this risk "pending expanded
write-up"; the write-up now exists and is gated. The note's TeX
carries a dated pointer to this amendment (added in the same commit).
The frozen rate bundles are unchanged; their inheritance disclosures
were accurate when sealed and are superseded in effect by this
record.
