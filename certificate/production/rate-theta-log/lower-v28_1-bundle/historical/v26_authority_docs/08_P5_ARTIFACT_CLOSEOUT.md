# P5 Artifact Closeout

## P5(a) endpoint-envelope verifier

`guards/exact_rational_endpoint_line_certificate.py` is the original exact verifier. Floating arithmetic selects predecessor histories only. Every pivot, affine line, hull breakpoint and final margin is recomputed over \(\mathbb Q\). The captured replay output is `guards/endpoint_line_certificate_result.json`.

It certifies
\[
E_+(u)-H(u)>4039/100000,
\qquad
E_-(u)-H(u)>9893/50000
\]
for all \(u\in[-1,1]\).

## P5(b) endpoint-projector truncation

Written explicitly in `upper_artifacts/ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md`.

## P5(c) promotion scope

The v26 promotion rule is **lower-bound only**. The constructive upper is supplementary and cannot promote or block the lower theorem except by exposing a contradiction in a shared promoted dependency.

## P5(d) rho/q identification

Written explicitly in `upper_artifacts/RHO_Q_IDENTIFICATION.md`.

## P5(e) integrity

- the v23 original archive hash is asserted, not merely printed, by `guards/guard_v23_archive_integrity_assert.py`;
- an outer detached SHA-256 manifest is generated after sealing the v26 archive;
- the prior consolidated bundle is included under `historical/` with its known hash recorded in the manifest.

## P5(f) supersession header

The copied `ANTITONE_EDGE_BUDGET_AND_EXPONENTIAL_BRANCH_SELECTION_V22.md` begins with an explicit v26 supersession header. The v26 proof does not consume its historical component `N<=d` line.

## P5(g) hygiene

The collar payment, \(g\ge0\) ordering, \(\phi_S\) continuity ordering, \(\lambda_j\to0\) route to \(\rho_\pm\le1\), symbol collision repair, and prefix-gain rename are all frozen in `06_P4_RECEIPTS_AND_SYMBOL_HYGIENE.md`.
