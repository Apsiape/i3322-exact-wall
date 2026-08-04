# Release verifier

`verify_release.py` has two modes:

- default: check manifest coverage, frozen SHA-256 custody, private-path
  exclusion, and theorem receipt semantics;
- `--full`: additionally regenerate every production and independent receipt
  in dependency order, including the independently reconstructed spatial
  truncation theorem, robust dimension-necessity chain, and sealed blind
  reconstruction, then recheck the theorem semantics.

Regenerate the manifest only after an intentional release change:

```powershell
python certificate/release/build_release_manifest.py
```

Do not regenerate the manifest to make a failed custody check disappear.
