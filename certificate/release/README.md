# Release verifier

`verify_release.py` has two modes:

At repository HEAD, a successful custody run reports
`CUSTODY_PASS_THEOREM_GAP`, not `PASS`: the files and registered negative
receipt are internally reproducible, while Sprint 1285 leaves the headline
Bellman theorem certificate open. A zero process exit code means the audit
completed and agreed with that disclosed status; it does not mean the
historical theorem has been repaired.

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
