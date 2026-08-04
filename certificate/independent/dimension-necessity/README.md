# Independent reconstruction of dimension necessity

This directory records the blind reconstruction and hostile post-verdict audit
of the quantitative finite-dimensional lower bound.  The reconstruction was
given only the 19 theorem sources frozen byte-for-byte under
`source-snapshots/` and identified in `source-manifest.json`, plus the
standard facts listed in `PRE-REGISTRATION.md`.  It did not read the production
assembly in foundational sprints 1231, 1233, 1234, or 1235 before returning its
verdict.

The manifest paths are logical production identities. The verifier resolves
them to the immutable snapshot tree, so later editorial changes to a production
theorem cannot retroactively alter the blind packet.

The accepted theorem is

```text
q_* - Q_d >= c d^-4 Gamma^-d,
Gamma = 312^4 = 9,475,854,336,
c = 4.294654614331445998753374519792940851...e-52.
```

The displayed decimal for `c` is descriptive.  Both checkers construct it
from the exact rational/surd ledger in the proof.

Run from the repository root:

```powershell
python certificate/independent/dimension-necessity/verify_source_manifest.py
python certificate/independent/dimension-necessity/verify_constants.py
python certificate/independent/dimension-necessity/post_blind_exact_verify.py
```

`BLIND-DIMENSION-RECONSTRUCTION.md` contains the complete independent debt
ledger. `POST-BLIND-ACCEPTANCE.md` records the subsequent quantifier,
geometry, ancestry, multiplicity, and exact-arithmetic audit.
