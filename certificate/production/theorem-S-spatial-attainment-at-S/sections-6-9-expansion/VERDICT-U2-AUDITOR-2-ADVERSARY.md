# VERDICT — U2 gate, ADVERSARY surface — NO COUNTEREXAMPLE FOUND

PROVENANCE: delivered in-session by the U2 countermodel-hunting
adversary on 2026-08-07 against frozen commit c628e20e (re-verified
at close: c628e20ecca7dcfe03d1a95e5a31eb93ac31f667, diff empty) and
written to disk the same day by the adjudicating track, verbatim
(task output file empty; delivery record is the session transcript).

---

## VERDICT: NO COUNTEREXAMPLE FOUND

Twenty-two attacks run (A1 i-v, A2 i-iii, A3 ×3, A4 ×2, plus 6
source-collation attacks). Zero produced a countermodel. Every
hypothesis stripped turned out load-bearing and correctly stated.
Both sharpenings survive, including against the degenerate
b-invariant orbit built explicitly for the purpose.

Registered: ONE substantive defect (S1), ONE load-bearing
non-sequitur (S2), six wording/anchor repairs. S1/S2 do not break the
mathematics but falsify two of the document's own completeness
claims; both must be fixed before the public amendment.

INDEPENDENT NUMERIC CONFIRMATION of the §7 centerpiece (own engine):
E = (b(x)+b(u))² + (x−u)²/4 = (1 + √((1−x²)(1−u²)) − xu)/2 exact to
1e-12 over 4×10⁵ random points; E ≤ 1−xu everywhere;
sup(xu−1+√E) = 1/4 attained only at x = u = −√3/2. At the certified
S = 0.2508753845015185, min(Σ²−δ²−Λ²) = +8.75e-4 > 0 on a 3000²
grid; at S = 1/4 it touches 0. Lemma 7.6's contradiction is genuine
with strictly positive margin; the extremiser −0.866 lies inside
CZS:130-131's active source range, so no range-based evasion.

## S1 — SUBSTANTIVE: Claim 0.1 consumes an operator identity
displayed nowhere in the cited corpus. The scalarisation step needs
the generic weld 𝓑 = d(X,U) + W + W_B (equivalently
𝓑 = XU + (X−U)/2 − I + Y(B₃−I/2) + (A₃−I/2)V, Sprint-1197/1287),
displayed in neither CERT, CZS, FR nor QC — CERT only names it at
1078-1079. Verified TRUE by direct expansion to the I3322
Collins-Gisin form. Consequences: OX.1 lacks the row; OX.4's
"exactly the rows of OX.1"/"no new axioms" false as written; F4's
"supplied missing step" is itself unanchored. This is the one place
the document should have carried a GAP block and did not. Repair:
add OX.1 row A7′ anchored to the Sprint-1287 source; display or GAP.

## S2 — LOAD-BEARING NON-SEQUITUR: the CERT:417 upgrade. Endpoint
nullity does not license extension off the support (explicit
countermodel to the INFERENCE given: μ_X carried by [0,0.5], law
asserted on supp only, fails at E = [−0.5,−0.4]). Needed:
(−id)_*μ_X ≪ μ_X. TRUE via CERT:376-390 (pre-division identity for
every bounded Borel f) + b > 0 pointwise + b even → the law for
every Borel E ⊆ (−1,1), no support caveat; CERT:433 same content,
also uncited. OX.1 A14/A15 cite only the post-division boxed laws.
Secondary: U2:456-466 derives D_a-conullity via (⇐) + positivity,
redundantly — the boxed derivation above it needs only (⇒);
U2:412-414's parenthetical is right about 6.3.6 but placed where it
reads as about 6.3.5.

## ATTACK LOG (numbered, all outcomes)

1. (A1-i) RN law holding while dom(a) misses positive measure:
NO COUNTERMODEL — D_a = P^{-1}(Y), μ_U(D_a) = μ_X(Y), mass carried
on −Y moves by the (⟹) half; Claim 6.3.1's pushforward step
independently verified. Yield: S2.
2. (A1-ii) D₊ missing/double-hitting an orbit; boundary α = −1/β = 1;
q(u) an orbit point: NO COUNTERMODEL. Latent hazard unflagged: q(u)
CAN equal an orbit point; the non-strict ≤ is then load-bearing
(strict < would MISS that orbit entirely). Amendment should say why.
3. (A1-iii) Explicit b-invariant dihedral orbit: NO COUNTERMODEL —
both cases built end-to-end (case (b): Y₀ = {n±1/3}; case (a):
Y₀ = {n+1/2}, k odd). Sub-case k EVEN (self-paired point b(v) = v,
v = 0) PASSES nontrivially: I4 forces r_B(0) = 1, and indeed
B(0) = b(0) identically — a consistency check that could have failed
and does not; record as a positive receipt.
4. (A1-iv) By-hand disintegration vs everywhere-discontinuous
first-representation map: NO COUNTERMODEL — structurally impossible;
nothing uses continuity; (9.1.1), covering, Σν_i = ν, and the
change-of-variables chain re-verified line-by-line. Unflagged
subtlety: on small orbits w_i(t) = w_j(t) possible; f_i is the atom
weight only ν-a.e.; (9.1.1)'s "each exactly once" invites the false
inference μ_t({w_i(t)}) = f_i(t). One sentence to add.
5. (A1-v) Two distinct fibre systems for b_*μ_U = r_B²μ_U:
NO COUNTERMODEL under stated hypotheses; hypothesis set verified
MINIMAL (dropping carried-by-fibre admits an immediate two-point
countermodel; 9.1(5) states exactly the killing condition).
6. (A2-i) Localisation identities at both pairs: NO FAILURE — and
the receipt is needed only at (x,u): p(−x) = g(x) and p(u) = g(−u)
follow from K(x) = K(u) = 1 alone; (7.5.2) is redundant; the
document's "p-halves are genuinely new" parenthetical is FALSE
(missed simplification, not error). L7.4 still needed for
R_0(−x,−u) = 0 in (7.6.2).
7. (A2-ii) Same-ρ derived or imported: DERIVED (L7.3, exceptional
set named, domain restricted before use); Steps 1-5 re-verified.
8. (A2-iii) Boundary/edge behavior: NO FAILURE — Z ⊆ (−1,1)²
strictly; every division and root guarded; Lean hypothesis discharge
correct; all QC anchors exact.
9. (A3) Claim 6.3.6 word induction: HOLDS — the compressed sentence
reconstructed in full; domain-containment handled by the ∩D_0 at
each stage via G_w.
10. (A3) L7.7 a.e.→existence: HOLDS — exactly one conull condition;
the cleaner F* = ∅ route present.
11. (A3) L9.6 single-t selection: HOLDS, but OX.3's "absorbed by the
δ_t redefinition" is true only for 9.1(3),(4); for L9.3/L9.5/L9.6
the δ_t fibres are inadmissible and are excluded by N_2 by
definition. State it.
12. (A4) Sum exactly 1 or exactly 2: HOLDS — recomputed via
b𝒪_ℤ(u₀) = 𝒪_ℤ(b(u₀)); attacked with the coinciding-representative
orbit and the sharpening is exactly what that model produces.
Implicit consequence to state: in case (a) λ̃ enumerates each atom
exactly TWICE, j ↦ c_j need not be injective, and the √2
normalisation at CERT:857-864 is substantive.
13. (A4) Atoms-on-Z pointwise: HOLDS; near-tautological by
construction; the a.e. content of φ = 0 spent once. Inherits S1 via
Claim 0.1.
14. F1/SCOPE FLAG attack: FAILS, and the finding is STRONGER than
the document knows — the dedicated boxed theorem is
CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md:224
(PROMOTED after round-3 repair W1-W4; §7 full-locus horizontal
exclusion via u = H'(x); §8 vertical exclusion from
R_0(−u,−x) = R_0(x,u); FR:191-192 independently confirms). Repair:
primary anchor there; CZS:115-126 secondary; downgrade F1 from
"closest call" to "resolved by a boxed theorem".
15. Anchor audit: ALL citations checked against live files; all
correct except ONE slip — L6.1(1)'s "uniform limit of the continuous
g_n, CERT:64": CERT:64 asserts only g_n → g; correct anchors FR:49
(g continuous and concave) or CERT:66 (concavity ⟹ interior
continuity).
16. I9 remark self-contradiction: the remark's "valid where K=1" is
WRONG — A(t)B(t) = b(t)² identically on (−1,1); r_A r_B = 1
unconditionally; matches CERT:261/CERT:419-431. Delete the clause.
17. CORRECTION 0.A incomplete — three further live collisions in
CERT: Y (operator A₂−A₁ at 203 vs the subset at 449 — the most
serious, §6 is built on the second), q (q_n ↓ S at 59 vs the
rational enumeration at 644 — U2 reproduces this collision itself),
π (GNS at 98 vs orbit quotient at 678; U2 adds π_u/π_x and π_ℤ).

## WORDING REPAIRS R1-R12 (mathematics held in every case)

R1 Claim 0.1/OX.1/OX.4: add the generic weld as input row; retract
"exactly"/"no new axioms" or display the weld. (S1)
R2 U2:348-358 + OX.1 A14/A15: replace with the CERT:376-390
derivation; add 376-390 and 433 to OX.1. (S2)
R3 U2:456-466 vs 412-414: D_a needs only (⟹); positivity for
6.3.6/7.3-Step-5/9.5, not 6.3.5.
R4 L8.3/8.4: state q(u)-on-orbit possibility and why ≤ is
load-bearing.
R5 L7.5: delete "p-halves genuinely new"; receipt needed only at
(x,u).
R6 §0.0/OX.1-A6/SCOPE FLAG/F1: primary anchor
CONVEX_ENVELOPE...:224; downgrade F1.
R7 L9.1: the small-orbit duplicate-representative sentence.
R8 I9 remark: delete the K=1 clause.
R9 CORRECTION 0.A/F3: add Y, q, π collisions; fix U2's own q reuse.
R10 L6.1(1): re-anchor g-continuity to FR:49/CERT:66.
R11 OX.2 CERT:849-855 row: each atom twice in case (a); √2
substantive.
R12 OX.3 row: δ_t absorption is (3),(4)-only.

## BOTTOM LINE

The engine survives every countermodel attempt. The three named
residual risks are genuinely retired: the conull invariant set is
correct including the compressed backward-trajectory induction; the
Borel transversal is correct including the degenerate b-invariant
case, built and checked; disintegration uniqueness is correct with a
hypothesis set verified minimal. The §7 elimination is correct and
independently reconfirmed numerically with a positive margin. The
document is not, however, self-contained in the way OX.4 claims: S1
and S2 are where a hostile referee would stop, both one-paragraph
repairs from material in the public repo. Fix R1 and R2 before the
amendment; R6 is a free strengthening of the document's own
self-declared weakest point.
