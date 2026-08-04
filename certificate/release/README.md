# Release verifier

`verify_release.py` has two modes:

At repository HEAD, a successful custody run reports
`CUSTODY_PASS_RIGOROUS_WINDOW_HEADLINE_GAP`, not `PASS`: the files, registered
negative receipt, and Sprint-1287 exact rational upper bound are internally
reproducible, while Sprint 1285 leaves the historical exact-optimum headline
open. A zero process exit code means the audit completed and agreed with that
disclosed status; it does not mean equality, nonattainment, or nonclosure has
been repaired.

Sprint 1288 adds an exact finite-strategy lower bound. The verifier therefore
also checks the unconditional interval
`0.25087519579012 < omega_tensor <= omega_commuting <= 0.250876384514`.

The full replay is byte-deterministic. Sprint 1279 previously serialized
wall-clock timing into its scientific JSON; that non-mathematical field was
removed after the full replay correctly rejected the changing hash.

- default: check manifest coverage, frozen SHA-256 custody, private-path
  exclusion, and theorem receipt semantics;
- `--full`: additionally regenerate every production and independent receipt
  in dependency order, including the independently reconstructed spatial
  truncation theorem, robust dimension-necessity chain, and separately written
  reconstruction, then recheck the theorem semantics.  The reconstruction's
  original chronology was not externally time-sealed and is not represented
  as cryptographic evidence of blindness.

The prospective v1.3 claim boundary has an additional publication guard:

```powershell
python certificate/release/v13_claim_contract_verify.py
```

It checks that the public theorem still quantifies over same-dimensional
POVM strategies, that both truncation boundaries and both asymptotic rates
have independent receipts, that the literature language is scoped, and that
v1.3 has not been represented as an archival release prematurely.

Regenerate the manifest only after an intentional release change:

```powershell
python certificate/release/build_release_manifest.py
```

Do not regenerate the manifest to make a failed custody check disappear.
