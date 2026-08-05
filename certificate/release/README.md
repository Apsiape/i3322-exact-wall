# Release verifier

`verify_release.py` has two modes:

At repository HEAD, a successful custody run reports
`CUSTODY_PASS_COMMON_VALUE_HISTORICAL_HEADLINE_GAP`, not `PASS`: the files,
registered negative receipt, exact rational window, and Sprint 1295
tensor/commuting value-equality theorem are internally reproducible, while
Sprint 1285 leaves the historical exact-optimum headline open. A zero process
exit code means the audit completed and agreed with that disclosed status; it
does not mean the historical decimal, nonattainment, or nonclosure has been
repaired.

Sprint 1292 adds the strongest exact finite-strategy lower bound, and Sprint
1294 adds the strongest exact Bellman upper bound. The verifier therefore also
checks the unconditional interval
`0.2508753845015185 < omega_tensor <= omega_commuting <= 0.250875388108398`.
The 255-dimensional strategy is separately reconstructed with `mpmath.iv` at
160 decimal digits. The endpoint-clustered upper certificate is separately reconstructed
with exact `Fraction` arithmetic and a different nonuniform partition traversal; neither
independent engine imports its production counterpart.

Sprint 1295 proves that the tensor and commuting suprema are the same common
Bellman/path variational value. A separately written exact-rational engine
checks the index orientation, Schur-pivot floor, weld typing, and 24 genuine
Pal--Vertesi carrier embeddings across both parity branches. The theorem does
not identify the common value with the historical decimal.

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
