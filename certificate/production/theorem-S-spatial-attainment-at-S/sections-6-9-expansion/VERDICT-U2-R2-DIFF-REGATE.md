# VERDICT — U2 v0.2, diff-scoped re-gate (round 2) — **CLEAN**

PROVENANCE: delivered in-session by the round-2 diff-scoped auditor on
2026-08-07 against frozen commit 5c0aff76 (blob 593ec398, freeze
verified at open and close) and written to disk the same day by the
adjudicating track, verbatim in substance (task output empty; delivery
record is the session transcript).

## GATE VERDICT: CLEAN
Carried with one mandatory pre-publication correction (F-1) — a
single clause, no mathematics, not a re-gate trigger.

| surface | result |
|---|---|
| D1 — repair verification, item by item | PASS (22/22 executed; 3/3 deviations adjudicated; 1 collateral defect → F-1) |
| D2 — diff discipline | CLEAN (856+/165−, every hunk traces to a named verdict item; lemma statements byte-identical apart from the q→θ rename and L9.1(5)'s added hypothesis) |
| D3 — spot re-verification of new material | CLEAN (5/5) |

## Key adjudications
- B1 executed in full; independently confirmed CZS (141 lines) has NO
  convex-envelope theorem and NO dual-tie argument — its 124-125 are
  pointer sentences; the CEPE re-anchoring strictly improves the
  referee path. All CEPE quotes verbatim incl. the box at CEPE:224.
- B2/(6.3.0) — the load-bearing new text — re-derived line by line:
  CERT:372-390/392-393 verbatim; bounded-Borel-f identity → measure
  identity via change of variables with b even → division by
  pointwise-positive b² → every Borel E ⊆ (−1,1), no a.e., no support
  caveat. S2's non-sequitur fully repaired.
- Deviation (i) upheld: Sprint-1287 genuinely lacks the weld display
  (prose only); MAN:498-507 verbatim-exact; the (0.1.W) cancellation
  recomputed and CORRECT (G(X,U) = d(X,U) exactly; W, W_B cancel
  exactly).
- Deviation (ii) upheld: concavity is CERT:69 (CERT:66 is blank-ish
  header text); v0.2 sided with the proof auditor correctly.
- Deviation (iii) upheld and M3's claim verified independently: (⟹)
  is universally quantified over Borel sets and negation is an
  involution on them, so both null-set directions follow from the
  forward direction alone — available precisely because B2 upgraded
  the laws to every Borel set. The two repairs interlock correctly.
- I9 identity recomputed: A(t)B(t) = b(t)² identically on (−1,1).
- Notes 8.3.A/8.4.A logic rechecked: strict < demands n < m and
  m ≤ n — impossible; the orbit would be missed entirely; with ≤ the
  solution set is exactly n = m.
- GR-1/GR-2 recomputed (r_B(0) = 1; the exact identity for E;
  E ≤ 1−xu ⟺ (x−u)² ≥ 0; equality case at x = u = −√3/2 exact).
- Every retracted claim survives ONLY inside its own retraction; no
  killed assertion is live anywhere.

## FINDINGS
- **F-1 [MAJOR/non-blocking/mandatory pre-publication]**: U2:74-75's
  "the ONLY place in the public repository where the generic weld is
  displayed" is FALSE — Sprint-1197's
  EXACT-I3322-QUANTUM-SUPREMUM.md:38-47 displays the same identity in
  bipartite tensor form under machine verification
  (bellman_quantum_dual_verify.py, :49-50) — exactly the source
  CERT:1078 names. The error runs CONSERVATIVE (understates
  corroboration); fix: "the only place" → "a place", and add
  Sprint-1197:38-47 to OX.1 row A7′ as a second, machine-verified
  anchor (a net strengthening). Flagged with a standing note: v0.2
  repaired one exclusivity overclaim and minted another; that reflex
  deserves a standing check.
- **F-2 [MINOR]**: cite CERT:214-224 (W² = b(X)², WX = −XW; W_B
  analogues) in L6.3's inputs so the U-side "same argument" is
  self-anchored.
- **F-3 [MINOR]**: remark that finiteness of A²dμ_X follows from the
  displayed identity at f ≡ 1 (left side ≤ 1/4).
- **F-4 [MINOR/optional]**: Note 8.3.A's ℝ-model could be replaced
  by a bounded in-range witness; nothing wrong as stated.
- **F-5 [TRIVIAL]**: CERT:358-361 → closing bracket at 362.

## STATEMENT FOR THE AMENDMENT RECORD
The U2 expansion gated clean on round 2. All twenty-two round-1
repair items were verified executed against the frozen v0.2 (commit
5c0aff76, freeze confirmed at open and close): proof-surface blockers
B1-B4, adversary defects S1-S2, wording repairs R1-R12, and both gate
receipts GR-1/GR-2. The two repairs that carried mathematical weight
were re-derived independently and are correct — the (RN-X)/(RN-U)
quantifier upgrade now follows from the pre-division identity
CERT:376-390 by change of variables and division by a
pointwise-positive b², yielding every Borel E ⊆ (−1,1) with no a.e.
and no support caveat, and the generic weld 𝓑 = d(X,U)+W+W_B is
displayed, anchored verbatim to MANUSCRIPT.md:498-507, with the two
response blocks shown cancelling exactly. All three of the revision
agent's flagged deviations were independently adjudicated and upheld.
Every new quotation was checked verbatim against the live files and
matched; the line-number sweep is complete with no stale anchors; and
the diff introduced no mathematical change outside the four sites the
verdicts directed. One non-blocking defect is docketed for correction
before publication (F-1, executed in the publication pass).
