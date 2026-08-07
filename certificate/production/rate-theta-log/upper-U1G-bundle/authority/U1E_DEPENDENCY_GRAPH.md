# U1G Dependency Graph (round 4; supersedes all earlier graphs —
# the U1/U1E/U1F graphs are HISTORICAL in their entirety and live only
# in git history and the on-disk verdicts)

Legend: [P] promoted; [R] receipt consumed within promoted scope —
where the source's own status line is CONDITIONAL, the [R] typing
covers only the consumed sections and the condition is stated at the
node (round-4 finding 6); [V] machine-verified, load-bearing where
stated; [C] candidate on trial in THIS gate.

```text
[P] Theorem (S) — public certificate v3.1.0 (DOI 10.5281/zenodo.21782008;
    five content hashes in proof §1a; §§6-9 residual risk DISCLOSED
    and inherited at the point of consumption)
      +--> §6:446 strictly increasing one-to-one Borel map P
      +--> §10:792 boxed P(c_{j+1}) = c_j (every j); §10:798 full-zero
      |    adjacent pairs
      +--> §11 transport law (1.1) and Jacobi eigen-equation
      +--> certified window (0.1): S > S_LO   [signed statement copy,
           hash-pinned in dependencies/]

[V] Lean kernel — public commit 6e6adb5, per-file hashes in proof §1b,
    AxiomCheck all 27 theorems, standard axioms only
      +--> band_identity; s_mul_one_sub_s_le_quarter;
      |    band_quarter_ceiling; amplitude_b_le_half   (proof 3.4-3.6)
      +--> quarter_lt_window_lower — LITERAL comparison 1/4 < S_LO
           ONLY (honest scope; the window itself is the [P] anchor)

[V] PART B exhibition (guards/guard_second_engine_projectors.py) —
    load-bearing ONLY for S > 1/4 (values 0.25006..., 0.25056... at
    d = 24, 33; construction caveat: PV open-endpoint padding, NOT the
    §4 completion — disclosed in artifacts/small_d_demoted/DISCLOSURE.md;
    the caveat does not touch the exhibited values)

[source: PROVED CANDIDATE, verified within the promoted v28.1 lower
 closeout] G1 — full byte-identical source in dependencies/
      +--> Z = R0^{-1}(0) compactly interior (§3:117-123 boxed)
      +--> m_g > 0 (§4:129-133); b_0 > 0 (§4:172-179)
      +--> corridor K, R_max finite                     (proof §2, 5.3)
      NOTE (Theorem-S §14): G1's inputs (storage, reflection gluing,
      zero-set localization, endpoint reserves) are among the promoted
      receipts that Theorem (S) itself also consumes — G1 is
      UPSTREAM-SHARED with (S), not independent of it. No (S) -> G1
      edge exists; both root in the lower program's promoted receipts;
      the graph is acyclic. G1's endpoint reserves are provenance-
      anchored by dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md.

[R] endpoint-Cesàro FULL source (dependencies/; own status:
    "conditional only on a coarse interior endpoint receipt" — the
    consumed §2 flux identity is exact algebra from H lambda = S
    lambda and does not depend on that condition, which §3.1 also
    discharges)
      +--> §2:85-94 boxed flux identity ONLY             (proof 5.1)
      NOT CONSUMED, by section number (proof §1d): §6 rival
      strictness (prose-named supplier), §9 symmetry warning
      (dependency removed — ends bounded separately), §3 |I|+3
      padding (superseded by proof §4's exact d = |I|), §10 scouts.

[R] truncation FULL sources (dependencies/, two files; the rank-costed
    source's own status is an abstract package with a CONDITIONAL
    corollary — nothing conditional is consumed) — provenance for §4's
    block anatomy and PART A's matching/completion rules
    (ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md, round-4 finding
    5); §4 is self-contained and PART A second-engine verified
    (symbolic, arbitrary angles)

        |
        v
[C] U1G proof: monotone labels + eigen-row limits (§3.1-3.3)
    --> band strictness (§3.4-3.5) --> kappa_eff >= 0.0418391 (§3.7)
    --> truncation d = |I| (§4) --> accounting (§5)
    --> allocation, every d (§6) --> limsup (§7)
        |
        v
[C] D_upper(eps) = O(log(1/eps)); 1/kappa_eff <= 23.9010650 (§7.2)
        |
        +--[P] D_lower = Omega(log) (authority/PROMOTED_LOWER_RATE_
        |      RECEIPT.md; consumed at corollary level ONLY)
        v
    Theta(log(1/eps)) — CONDITIONAL COROLLARY (§8), promotes only
    with this gate

[V, non-load-bearing] artifacts/small_d_demoted/ (disclosed:
    DISCLOSURE.md); artifacts/commission_history/ (superseded notes
    and the retired retrodiction guard)
```

RETIRED authorities (ledger entries 10, 17): selected-tail bracket +
identification, sextic tail-closure, wall-comparison selection,
equality-module, hyperbolicity — none appears in the U1G proof; the
retirement record is the ledger and the on-disk verdicts.
