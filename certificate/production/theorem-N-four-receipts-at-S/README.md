# Theorem (N) — promoted package v5

**Status:** **PROMOTED.**  
**Promotion record:** three rounds of independent adversarial review (record: `review/ROUND3-VERDICT.md`);
four receipts of four; signed 2026-08-05.

This directory contains the operative proof package for finite-dimensional
nonattainment of the I3322 quantum supremum at the current common value `S`.

## Public theorem

In the Collins–Gisin normalization used by the repository:

- the classical bound is `0`;
- the qubit and qutrit maximum is exactly `1/4`;
- `S = omega_tensor = omega_commuting` lies in
  `(0.2508753845015185, 0.250875388108398]`;
- no finite-dimensional quantum strategy attains `S`;
- consequently `C_q(3,3;2,2)` is not closed.

The exact signed wording is in `THEOREM_N_SIGNED_PUBLIC_STATEMENT.md`.

## Operative proof spine

1. `FOUR_RECEIPTS_AT_S_ASSEMBLY.md` — limiting-weld substitute and exact
   endpoint exclusion, including the round-3 spectral-cutoff paragraph.
2. `CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md` — concavity,
   reflection-gluing `K >= 1`, zero-set localization, and strict Monge.
3. `CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` — the
   repaired open-interval convex-minorant proof and strict full-zero graph.
4. `THEOREM_N_SIGNED_PUBLIC_STATEMENT.md` — promoted theorem, dependency list,
   and binding claim boundary.
5. `W1_W10_EXECUTION_LEDGER.md` — exact disposition of every round-3 finding.

## Artifact scope

The scripts in `artifacts/` are **algebraic-identity and exact-arithmetic
guards only**. They do not verify the limiting weld, convex-minorant maximality,
no-kink logic, envelope binding, operator transport, or the complete theorem.
See `artifacts/README.md`.

## Retired material

The v4 tiling specifications, fail-closed Receipt-(ii) schemas, validators,
branch verdicts, supersession notes, and contradictory OPEN-status documents
are not shipped as operative files. `SUPERSEDED_FILES_LEDGER.md` records their
retirement.

## Explicit nonclaims

This package does **not** claim:

- that `S` equals the historical Pál–Vértesi decimal;
- that the historical infinite-dimensional construction is optimal;
- current spatial attainment of `S`;
- `C_qs(3,3;2,2) \\ C_q(3,3;2,2)` is nonempty;
- the retracted conditional dimension-necessity theorem;
- global uniqueness of the raw first Bellman contact.
