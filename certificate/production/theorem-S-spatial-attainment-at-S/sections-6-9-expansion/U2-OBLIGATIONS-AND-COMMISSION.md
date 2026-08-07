# U2 — Expanded write-up of certificate §§6–9: obligations map + commission

Adjudicating track, 2026-08-07. Target: discharge the disclosed
residual risk of CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md §§6–9
(conull invariant set, Borel transversal, uniqueness of
disintegration) with a full expanded write-up, gated blind before it
amends the public certificate. Consumers of these sections: §10 (the
carrier construction), hence Theorem (S), hence the C_qs\C_q
separation AND the entire rate theorem's upper half.

## Complete obligations ledger (every thin step, numbered)

### §6 — strict graph and the conull response action
- **O6.1** Z Borel + graph of strictly increasing one-to-one Borel P:
  derive single-valuedness/graph-ness from the certified §1 input
  ("the full interior zero locus is a one-to-one strictly increasing
  relation", line 73) + Borel-graph ⟹ Borel-map (standard: a Borel
  graph of a function on a standard Borel space has Borel projections
  and the map is Borel — cite or prove via injective Borel image).
- **O6.2** Dual-zero involution P(−P(u)) = −u: from the certificate's
  φ symmetry (locate and quote the exact symmetry identity used —
  expected: (x,u) full-zero ⟺ (−u,−x) full-zero).
- **O6.3** THE CONULL INVARIANT SET (named risk #1). Prove: (i) each
  RN transport law forces its reflected coordinate to exist a.e.
  (if the domain of a failed on a positive-measure set, the law's
  two sides disagree — write the actual argument, not the gesture);
  (ii) KEY LEMMA: the transport densities r_A(P(·))², r_B(·)² are
  positive and finite a.e., hence a_*, b_* preserve μ_U-null sets in
  both directions (quasi-invariance) — this is what licenses the
  countable intersection; (iii) the intersection over all finite
  words w in the infinite-dihedral group D_∞ = ⟨a,b | a²=b²=1⟩ of
  the pullbacks of the good domain is Borel, conull (countably many
  words × null-set preservation), and invariant under a and b by
  construction; (iv) a is a decreasing involution on Y₀
  (a = P^{-1}∘(−)∘P, P increasing ⟹ decreasing; a² = id from O6.2),
  b(u) = −u likewise.
- **O6.4** τ = a∘b increasing (two decreasing maps); an increasing
  injective map has no non-fixed periodic point (τⁿu = u, τu > u ⟹
  τⁿu > u by induction — write both directions).
- **O6.5** Restatement of the §5 RN laws on Y₀ (verbatim carryover;
  state the measurable-set quantifier precisely).

### §7 — fixed points carry no mass
- **O7.1** F Borel, a,b-invariant (τ commutes appropriately; write).
- **O7.2** On F: a(u) = b(u) = −u (from τu = u and the involutions).
- **O7.3** Equal integrals over every Borel E ⊆ F of the two
  densities ⟹ densities equal a.e. on F (standard; write). NOTE
  aE = bE on F must be justified pointwise (both equal −E).
- **O7.4** (x,u) and (−x,−u) both full-zero pairs (from O6.2 + τu=u).
- **O7.5** The four zero-set-localization identities
  g(−x) = ρb(x), g(x) = b(x)/ρ, g(u) = ρb(u), g(−u) = b(u)/ρ:
  state the localization receipt PRECISELY (which promoted document,
  which display) and derive all four.
- **O7.6** THE ELIMINATION, now Lean-anchored (this is the
  expansion's centerpiece — the prose "audited Sprint-1198
  elimination" becomes a two-line computation ending in a
  machine-checked theorem): from
     S − d(x,u) = ρ(b(x)+b(u)),  S − d(−x,−u) = (b(x)+b(u))/ρ,
  with d(x,u) = xu + (x−u)/2 − 1, so d(x,u)+d(−x,−u) = 2xu−2 and
  d(x,u)−d(−x,−u) = x−u. Set A := S − xu + 1 and δ := (x−u)/2; the
  two equalities read A − δ = ρB and A + δ = B/ρ with B := b(x)+b(u).
  MULTIPLYING eliminates ρ: A² − δ² = B², and A = S + (1−xu) > 0
  forces A = √(B² + δ²). Hence
     S = xu − 1 + √( (b(x)+b(u))² + (x−u)²/4 ),
  which is ≤ 1/4 by the Lean kernel's `quarter_ceiling` theorem
  (QuarterCeiling.lean:77-90, hypotheses x² ≤ 1, u² ≤ 1 — satisfied,
  labels interior). Contradiction with certified S > 1/4
  (window + `quarter_lt_window_lower`, honest scope as in the rate
  note). CHECK ALSO: ρ > 0 needed for the multiplication direction
  and for A−δ, A+δ > 0 — derive ρ > 0 from positivity of the
  densities (O6.3(ii)); and note b(x), b(u) > 0 interior.
- **O7.7** μ_U(F) = 0 by contradiction (a.e.-to-existence quantifier
  step written explicitly: if μ_U(F) > 0 then a point satisfying ALL
  a.e. identities exists — intersect the finitely many conull sets).

### §8 — Borel transversal (named risk #2)
- **O8.1** Y± Borel, invariant unions of orbits (τ increasing).
- **O8.2** α, β orbit-constant Borel; strict monotonicity of n ↦ τⁿu
  on Y₊; α(u) < u < β(u); q(u) Borel (first-rational selection —
  write the measurability).
- **O8.3** D₊ meets each increasing orbit EXACTLY once (existence +
  uniqueness of the crossing index n; both directions).
- **O8.4** Mirror on Y₋ via τ^{-1}.
- **O8.5** bτb = τ^{-1} (one line from involutions); b maps orbits to
  orbits exchanging Y₊/Y₋ ORBIT-WISE (careful casework: can a
  Z-orbit be b-invariant? handle both cases); the induced involution
  on the Z-transversal is Borel; lesser-representative choice gives a
  Borel transversal of the full dihedral relation (write the
  well-definedness: "lesser of its two representatives" needs the
  pair measurable and the choice Borel).
- **O8.6** Transversal ⟹ smooth ⟹ standard Borel quotient
  π: Y₀∖F → T with T Borel-isomorphic to the transversal (prove
  directly by defining π as the map to the orbit's transversal
  point — then T IS the transversal, no abstract quotient theory
  needed; verify π Borel: π(u) = the unique transversal point in the
  orbit — expressible via countably many words w: π(u) = w(u) where
  w = first word with w(u) ∈ transversal).
- **O8.7** QUANTIFIER AUDIT: everything modulo F and the null
  complement of Y₀; state the final domain precisely.

### §9 — disintegration and normalization (named risk #3)
- **O9.1** Disintegration existence: since T is the transversal
  (Borel subset of Y₀) and π is Borel with countable fibres (orbits),
  disintegration of μ_U over ν := π_*μ_U exists with probability
  fibre measures μ_t on the orbit of t — AVOID abstract Rokhlin if
  possible: for countable-fibre Borel π this is elementary (write it:
  the orbit is countable, define μ_t pointwise via conditional atoms
  — the measure of each atom in the fibre — via the RN derivative of
  μ_U restricted to graphs of the countably many words w against
  π_*μ_U; verify measurability in t and the integration identity).
- **O9.2** π∘a = π∘b = π (orbit maps), hence b_*μ_U and a_*μ_U also
  fibre over ν.
- **O9.3** THE NORMALIZATION, simplified (centerpiece #2 — replaces
  the bare "uniqueness of probability disintegration" appeal):
  push forward the transport law b_*μ_U = r_B²μ_U by π. LHS:
  π_*(b_*μ_U) = (π∘b)_*μ_U = π_*μ_U = ν. RHS: π_*(r_B²μ_U) has
  density c_B(t) = ∫ r_B² dμ_t against ν (write the Fubini step).
  Hence c_B = 1 ν-a.e. — no uniqueness theorem consumed for this
  half. THEN fibre equality b_*μ_t = r_B²μ_t ν-a.e.: both are
  disintegrations of THE SAME measure b_*μ_U = r_B²μ_U over the same
  π and same base ν; state and prove the a.e.-uniqueness of
  countable-fibre disintegration directly (elementary here: fibres
  are countable, compare atom weights via the same RN argument as
  O9.1 — again no abstract theorem needed). Mirror for a.
- **O9.4** Atomicity (countable fibres) + a.e. fibre supported in
  the full-zero locus (disintegrate the null set {φ≠0}; write the
  null-fibre argument).
- **O9.5** Positive atom propagates along its whole orbit (densities
  in (0,∞) on Y₀ + the fibre transport laws; induction over words).
- **O9.6** Existence of one good t (finitely/countably many conull
  conditions on t; intersection conull; ν ≠ 0). State EXACTLY the
  properties the chosen orbit measure carries into §10 (the
  interface: single orbit, purely atomic probability, atoms on Z,
  fibre transport laws for a and b, all-atoms-positive).

### Cross-cutting
- **OX.1** Inputs table: every consumed display with file+line
  (§1:73 relation; §5 RN laws — quote them; the zero-set
  localization receipt; Lean quarter_ceiling + window; φ symmetry).
- **OX.2** Interface-out table: exactly what §10 consumes (so the
  gate can check §10 needs nothing more than what is proved).
- **OX.3** a.e.-vs-pointwise audit on EVERY lemma (the program's
  standing quantifier-audit rule) — each statement labeled
  [pointwise on Y₀] / [μ_U-a.e.] / [ν-a.e. t].
- **OX.4** No new axioms beyond: standard Borel space facts
  (countable selection, Borel graphs), the certificate's promoted
  inputs, and the Lean kernel. Anything else = flag loudly.

## Commission

Draft U2-SECTIONS-6-9-EXPANDED.md executing every obligation above
as numbered lemmas with complete proofs (Lemma 6.1 ↔ O6.1, etc.),
each lemma carrying its input anchors and its quantifier label.
Blind gate follows (proof surface + countermodel-hunter,
refutation-first, frozen artifact) before any public amendment.
