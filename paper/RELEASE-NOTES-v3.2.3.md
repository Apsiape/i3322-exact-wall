# Release notes — v3.2.3 (2026-08-06)

Verification-audit release: a fresh adversarial audit of the corrected
v3.2.2 paper (checking the correction pass itself and all newly added
content against primary sources) found 9 items; all are fixed here.
The theorems, certificates, and constants are unchanged and all verified.

Paper (resolution.tex, rebuilt PDF):
- Mghirbi citation corrected: N. (Nidhal) Mghirbi, actual record titles
  ("Proof-carrying exact quantum bounds for the I3322 Bell inequality";
  software record titled separately); acknowledgments initial fixed.
  All claims ABOUT the work were verified correct (dates, widths,
  priority) — only the entry itself was wrong.
- Dykema-Paulsen-Prakash 2018 attribution weakened to what "The Delta
  game" actually contains (compactness remark + explicit I3322
  attainment question; the implication is immediate but unstated
  there); full bibliographic data added.
- Orphaned references wired: Araujo et al. now cited (2026 work with
  Vertesi as coauthor still treating the optimum as unresolved); NPA
  cited at the hierarchy caution.
- Lupini et al. cited under its published title; dangling
  "abstract's phrase" reference repaired; Coladangelo-Stark
  "amenable" suggestion re-characterized per their actual text;
  Pakhunov level-10 figure re-sourced to Gigena et al.; MNY gloss
  attributes the Pi_1 half to Slofstra; Bell operator attributed to
  PV Eq. (3); C_qs definition corrected (includes finite dimensions);
  smallest-scenario list reordered (Beigi first); the three
  reviewer-supplied repairs named (W1, V1, V2); PV-quote bracket
  tightened; minor title hyphenation.
- Verified and untouched: the PV verbatim conjecture quote, both
  Coladangelo-Stark quotes with version attribution, the displayed
  Bell operator (exact match to PV Eq. (3) and the concordance), the
  m+- decimals (exact division), all window constants, the AI
  disclosure, and all mandated-removal residue checks.

Repository:
- README and CITATION.cff no longer carry the retracted
  exact-identification and construction-optimality claims (residues
  from the historical release that contradicted the paper under the
  same DOI).
