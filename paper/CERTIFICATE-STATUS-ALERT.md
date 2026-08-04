# Certificate status alert — 2026-08-04

The theorem package in the frozen `v1.0.0`, `v1.1.0`, and `v1.2.0` archives
should currently be read as a **historical claim under correction**, not as a
closed computer-assisted proof.

An exact 400-bit Arb audit performed after those releases found a nonzero
global-amplitude mismatch in the Bellman datum on the complete unique-root
bracket:

```text
target amplitude - reflected source amplitude
in [0.00014027592551842303, 0.00017894047518170395].
```

The interval excludes zero.  This exposes a load-bearing normalization gap in
the current Bellman upper-bound assembly.  The audit is reproducible from
`certificate/production/foundational-sprint-1285/` and is incorporated into
the release verifier at repository HEAD.

This finding does **not** establish that the reported numerical constant is
wrong.  It establishes that the present proof of the global Bellman upper
bound is incomplete.  Consequently, until a corrected global normalization or
an independent upper bound is certified, repository HEAD does not certify:

- equality of the tensor-product or commuting-operator supremum with `q_*`;
- finite-dimensional nonattainment at that value;
- the claimed `C_qs \ C_q` witness or nonclosure corollary; or
- a finite-section deficit measured from the true I3322 optimum.

Exact local shooting, spatial-wall, boundary-flux, and algebraic receipts are
retained.  Their valid conditional content is not erased by the failed weld.
No replacement theorem is claimed yet.
