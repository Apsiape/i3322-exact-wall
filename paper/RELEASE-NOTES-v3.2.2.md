# Release notes — v3.2.2 (2026-08-05)

Correction release for the resolution paper and repository hygiene,
following three adversarial audits of the paper itself (a simulated
hostile referee, a citation/constants auditor, and the earlier zoo
sweep). The theorems are unchanged; every finding concerns
presentation, attribution, or metadata.

## Paper corrections (paper/resolution.tex, rebuilt PDF)

- RETITLED to "The I3322 quantum value is attained spatially but not in
  finite dimension" — the Pál–Vértesi conjecture is now quoted verbatim
  in the introduction, with an explicit statement of which half is
  proved (finite-dimensional nonattainment) and which remains open
  (optimality of their construction; exact value).
- FIXED two false decimal bounds: the exact margins m± were printed
  with decimals belonging to a different margin family; corrected to
  m+ > 0.00787 and m- > 0.0684, with the note that only positivity is
  consumed.
- CREDITED prior art: Mghirbi's July 2026 exact rational two-sided
  I3322 enclosures (tighter than the window used here) are cited, and
  the window is presented as a certified input, not a contribution.
  Added: Dykema–Paulsen–Prakash's 2018 recorded implication
  (nonattainment => nonclosure), Araújo–Klep–Garner–Vértesi–Navascués
  2026, Fritz and Junge et al. for commuting-model attainment, the
  Lupini et al. correlation-set taxonomy, and Coladangelo–Stark's
  "simplest suspected scenario" observation.
- ADDED the AI disclosure and review-nature section: frontier language
  models (OpenAI GPT/Codex-class, Anthropic Claude-class) used for
  proof discovery, implementation, auditing, and editing; the
  adversarial review described accurately as a preregistered
  refutation-first protocol executed by independently instantiated
  frontier models — procedural, not ontological, independence — with
  reviewer-supplied repairs identified; author contribution and
  responsibility statement included.
- SCOPED the minimality claim to two-outcome bipartite scenarios;
  corrected the comparison list (Beigi's two distinct separations;
  Slofstra's game sizes and output alphabets; Musat–Rørdam credited).
- WEAKENED the storage paragraph to what the public certificates prove
  (subsequential Arzelà–Ascoli limit; concavity, positivity,
  feasibility — the only properties consumed).
- Corrected attributions and wording: qutrit ceiling no longer
  attributed to Pál–Vértesi; "d >= 12" stated as their numerical
  family finding; POVM handling via extreme-effect replacement;
  commuting-model attainment cited to Fritz/Junge et al. with the
  compactness argument; CGLMP minimality claim removed; chained
  inequalities folded into the correlator clause; embezzlement
  correspondence labeled heuristic; the two NPA cautions
  disambiguated (hierarchy-attainment vs strategy-attainment) with
  full author lists; the asymmetry remark rewritten without numeric
  ranges (envelope-vs-orbit distinction retained); C_q/C_qs defined;
  the Bell operator displayed; Theorem 1 stated for arbitrary finite
  local dimensions.
- Bibliography: Fanizza et al. full seven-author list (initial M.);
  Pakhunov added as author of arXiv:2607.13774; van Luijk et al.
  title corrected to the cited paper; Mousavi–Nezhadi–Yuen now cited
  in the discussion (STOC 2022); Ll. Masanes; CHTW page range;
  arXiv-vs-journal title variants noted where they differ.

## Repository hygiene

- The Sprint-1206 spatial-attainment document is now RETIRED-marked
  (a mandatory condition of the Theorem-S review): its claim rested on
  the decertified Sprint-1195 wall; current spatial attainment lives
  in the theorem-S certificate, which uses only the finite block
  identity.
- paper/CERTIFICATE-MAP.md: the separation-witness row now points to
  the theorem-S certificate.
- ROUND1-VERDICT.md and ROUND2-VERDICT.md now ship in the theorem-N
  review directory (previously only round 3 shipped).
- CITATION.cff now carries the concept DOI (was: the stale v1.2.0
  frozen DOI) and version 3.2.2.
- certificate/release/README.md documents the custody status-string
  semantics: the "historical headline gap" refers to exact-value
  identification, not to the promoted theorems.
