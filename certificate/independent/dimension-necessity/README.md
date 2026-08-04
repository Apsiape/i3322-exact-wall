# Independent reconstruction of dimension necessity

This directory records a separately written reconstruction and the hostile
audit that ultimately retracted its quantitative finite-dimensional lower
bound. The
original packet contained 19 theorem sources; pre-release review found two
omitted owners and repaired the public packet to the 21 sources under
`source-snapshots/`. The intended information boundary excluded production
Sprints 1231, 1233, 1234, and 1235, but the chronology was not externally
time-sealed and is not claimed as cryptographic evidence of blindness.

The manifest paths are logical production identities. The verifier resolves
them to the immutable snapshot tree, so later editorial changes to a production
theorem cannot retroactively alter the blind packet.

The reconstruction conditionally produced

```text
q_* - Q_d >= c d^-4 Gamma^-d,
Gamma = 312^4 = 9,475,854,336,
c = 4.294654614327144182412697296233929416...e-52.
```

but the implication is not presently a theorem. The displayed decimal for `c`
is descriptive. Both checkers construct it from the exact rational/surd
ledger; arithmetic agreement did not detect the missing localization premise.

Run from the repository root:

```powershell
python certificate/independent/dimension-necessity/verify_source_manifest.py
python certificate/independent/dimension-necessity/verify_constants.py
python certificate/independent/dimension-necessity/post_blind_exact_verify.py
```

`BLIND-DIMENSION-RECONSTRUCTION.md` preserves the conditional debt ledger and
marks the failed implication. `POST-BLIND-ACCEPTANCE.md` now records the
withdrawal of the former acceptance.
