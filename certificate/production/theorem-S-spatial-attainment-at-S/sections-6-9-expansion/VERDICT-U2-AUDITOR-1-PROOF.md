# VERDICT — U2 gate, PROOF surface — DENIED (citations; no mathematical obstruction)

PROVENANCE: delivered in-session by the U2 proof-surface auditor on
2026-08-07 against frozen commit c628e20e (md5
e1460defe308e3886bfa4be7f7ffb261) and written to disk the same day by
the adjudicating track, verbatim (task output file empty; delivery
record is the session transcript).

---

## VERDICT BLOCK

| surface | verdict |
|---|---|
| R1 — lemma-by-lemma verification | PASS WITH CONDITIONS |
| R2 — quantifier audit | PASS WITH CONDITIONS |
| R3 — source fidelity | FAIL |
| R4 — interface (OX.2 / §10 / §11) | PASS |
| Countermodel duty (6.2, 6.3, 8.3, 8.5, 9.3) | all attempts failed; statements hold as written |

### GATE VERDICT: DENIED

Denied on R3, with two supporting must-fix defects on R1/R2. **No
mathematical obstruction was found.** Every headline claim of the
document is true; the centerpiece elimination (L7.6) is correct and
correctly machine-anchored; L9.1(5) genuinely retires the CERT:705
black box; the §8 transversal is correct including the load-bearing
non-strict ≤. The denial is that the document's single most
consequential finding (F1) names the wrong operative anchor, and its
recommended public action would degrade the certificate's citation
chain.

## FINDINGS

**M1 — [MAJOR/BLOCKING] F1's operative anchor is wrong; the actual
proof document is never cited.** CZS:115-126 is textually unqualified
(verified verbatim) but CZS §6 supplies only strict Monge (CZS:121);
CZS:124-125 are one-line pointer sentences naming results nowhere
proved in CZS. The full-locus graph is proved and BOXED in
CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md
(theorem-N package): box at line 224, "R_0^{-1}(0) ∩ D² is a
one-to-one strictly increasing relation", D := (−1,1) (line 15); §7
(lines 177-194) proves the horizontal exclusion via u = H'(x) on the
full source domain; §8 (196-210) the dual-tie/vertical exclusion; §9
(212-225) assembles with strict Monge. Corroborated by the package
README (lines 26-30) and the S1 referee dependency list (lines
509-513). U2 never cites the document. Consequences: SCOPE FLAG
6.1.A's "CZS:124-125 are theorems" is false (they are appeals); F1's
recommended re-anchoring of CERT:73/CERT:1073 to CZS:115-126 would
point a public referee at a summary containing two unproved appeals
instead of the boxed theorem; OX.1 incomplete; OX.4's "exactly the
rows of OX.1" false; F1's inference from FR:172's word "weaker" is
authorial-intent reasoning where CEPE:208-210 settles it cleanly.
Second half of gate question (a) VERIFIED CLEAN: the qualified FR
receipt is genuinely not consumed downstream.

**M2 — [MODERATE/BLOCKING] The (RN-X)/(RN-U) quantifier upgrade is
asserted with a non-sequitur, and it is load-bearing.** U2:348-358
upgrades CERT:417's a.e.-on-the-support statement to every Borel
E ⊆ (−1,1) justified only by endpoint-nullity — which addresses ±1,
not the support extension. Consumed at Y^c, (−Y)^c, D_0^c — sets
possibly off the support. The upgrade is TRUE by a three-line route
inside CERT:376-390: for all bounded Borel f,
∫ b(x)²f(x) d((−id)_*μ_X) = ∫ A(x)²f(x) dμ_X, so
b² d((−id)_*μ_X) = A² dμ_X as measures, and b² > 0 pointwise on
(−1,1) gives the identity for every Borel E with no a.e. at all
(what CERT:392-393's "scalar division" describes). Must be written:
L6.5's "no exceptional set" and the OX.3 null budget rest on it.

**M3 — [MODERATE] Claim 6.3.2's load-bearingness over-attributed.**
Both directions of quasi-invariance follow from the (⟹) direction
alone via the involutions (applied at −N); positivity is NOT needed
for 6.3.3/6.3.5′ or the 6.3.6 induction. U2:412-414 ("without
pointwise positivity ... the induction of Claim 6.3.6 would fail")
is FALSE. Claim 6.3.2 IS load-bearing at exactly: ρ ∈ (0,∞) in
L7.5/L7.6, atom propagation in L9.5(2), and the single-conull-set
count in L7.7 — all correctly executed. Trace: if 6.3.2 were only
a.e., §6 survives; L7.6/L7.7/L9.5 break. As it stands the claim is
pointwise from g(x) > 0 for every x (FR:63, CERT:70); nothing breaks.

**m4 — [MINOR] Four wrong line anchors in the §1 input block** (one
cited five times): concave CERT:69 (cited 66); g > 0 CERT:70 (cited
68); Bellman-feasible CERT:71 (cited 69); endpoint gaps CERT:72
(cited 71). Also d(i,j) at CZS:34 (cited 35, twice); A25's ranges
133-135/137-138; CORRECTION 0.A's CERT:526 spans 522-528. Content
correct throughout; numbers slip.

**m5 — [MINOR] The Remark on I9 contradicts I9 and is wrong**: the
product laws hold identically on (−1,1) (A(t)B(t) = b(t)²), no K = 1
needed; corroborated at the S1 verdict line 150. Delete the clause.

**m6 — [MINOR] Lemma 9.1(5) omits a finiteness hypothesis its proof
uses** (λ(Y_1) < ∞); falsifiable by an infinite-mass family in
isolation; harmless in both applications.

**m7 — [MINOR] L6.5's header lists a §6 output (CERT:514-527) as an
input**, contradicting OX.4; the proof itself is fine.

**m8 — [MINOR] Two typographic defects in load-bearing prose**
(U2:463's complement expression; U2:899's unfinished sentence).

## SURFACE DETAIL (compressed)

R1: every lemma and claim read line-by-line; L7.6 recomputed from
scratch and matched term-for-term against QuarterCeiling.lean:77-90
(hypotheses discharged; file sorry-free; axiom infrastructure
verified). L9.1's by-hand disintegration sound including the
duplicate-atom case; L9.3's Fubini correct; L9.1(5) a genuine,
non-circular uniqueness proof retiring CERT:705. All [standard]
citations genuinely standard and correctly invoked; no Rokhlin or
measurable selection smuggled. Conditions: M2, M3.

R2: every quantifier label verified; NO proof consumes pointwise
where only a.e. was proved — the program's known failure mode is
absent. Defects are the reverse direction: M2, M3.

R3: FAIL per M1/m4/m5; every other anchor in the document verified
verbatim (full list checked).

R4: PASS — all 22 OX.2 rows verified against CERT:746-880 + §11
draws; both sharpenings correct and consistent (sum exactly 1 or 2
matching the two cases; pointwise atoms-on-Z strictly stronger with
no downstream consequence); F8's binding caution correct.

Countermodels: L6.2 (blocked — σ(Y) ⊆ Y forced), L6.3 (blocked;
exposed M3), L8.3 (blocked; the orbit-point case survives
SPECIFICALLY by the non-strict ≤), L8.5 (blocked; CORRECTION 8.5.A/F2
confirmed with the explicit model; strict < genuinely breaks the
degenerate case), L9.3 (blocked; infinite-mass attack succeeds
against 9.1(5) in isolation → m6).

## MINIMAL BLOCKER LIST

B1 (M1): re-anchor A6/F1 to CONVEX_ENVELOPE...COMPLETION §§7-9 (box
:224); add as OX.1 row and OX.4 inventory; delete "are theorems";
change F1's recommended public action; keep CZS:115-126 as the
strict-Monge anchor only.
B2 (M2): replace U2:348-351 with the b²-division derivation from
CERT:376-393.
B3 (M3): delete U2:412-414 and the strict-positivity clause of
U2:456-466; restate 6.3.2's genuine consumers; fix OX.3/OX.4.
B4 (m4-m8): line-number sweep; I9 remark; 9.1(5) hypothesis; L6.5
header; two typographic fixes.

None requires new mathematics. On re-submission with B1-B4 executed,
I expect this document to gate CLEAN.
