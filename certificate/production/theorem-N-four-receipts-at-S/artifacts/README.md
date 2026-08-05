# Artifact scope

These artifacts are **guards, not theorem verifiers**.

## Exact-arithmetic guards

- `four_receipts_at_S_endpoint_exact.py` verifies the two rational endpoint
  identities and margins.

## Symbolic algebra guards

- `convex_envelope_algebraic_guards.py` verifies derivative-jump, reflection,
  Monge, contact-parameter, and `C>=g(0)` algebraic identities.
- `critical_zero_set_algebraic_guards.py` verifies reflection, the 2x2
  determinant, the `K_xK_u` identity, Monge, and kink-sign formulas.

## Package integrity

- `package_v5_integrity_verify.py` checks that all W1–W10 textual/package
  controls are present and that obsolete statuses and claims are absent from
  operative documents.

## Not verified by these scripts

The scripts do **not** verify:

- Arzelà–Ascoli or the limiting-weld passage;
- positivity or maximality of the convex minorant;
- the no-kink lifting argument;
- envelope binding on the full source domain;
- joint spectral support or unitary transport;
- the Sprint-1198 closure argument;
- Theorem (N) as a whole.

Those steps were audited analytically in the three blind rounds.
