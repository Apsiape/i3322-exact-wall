# Independent I3322 interval reconstruction

This directory reconstructs the historical local Bellman inputs without Arb
or any production Python module. It uses `mpmath.iv` real intervals and a
local rectangular-complex layer. The reconstruction is **not** a complete
Bellman certificate: `amplitude-gap/` independently proves that the local
charts fail the required global amplitude compatibility equation.

Run from this directory's repository root:

```powershell
python certificate/independent/arithmetic_selftest.py
python certificate/independent/plateau_series_mpmath.py
python certificate/independent/analytic_tail_mpmath.py
python certificate/independent/shooting_miranda_mpmath.py
python certificate/independent/global_graph_mpmath.py
python certificate/independent/amplitude-gap/amplitude_gap_mpmath.py
python certificate/independent/amplitude-gap/amplitude_gap_concordance.py
python certificate/independent/verify_independent_reconstruction.py
python certificate/independent/spatial_symbolic_verify.py
python certificate/independent/truncation_flux_mpmath.py
```

The global graph pass takes roughly three minutes on the reference machine.
The assembler checks the source AST for forbidden `flint` imports before it
loads a production receipt for post-verdict numerical comparison. Its passing
status means that the local receipts and the diagnosed global gap reproduce
consistently; it explicitly reports `headline_certificate_closed: false`.

The final two commands separately reconstruct the spatial Bell-to-Jacobi
identity and the finite-section boundary-flux law. The truncation engine also
derives and interval-encloses the plateau exponent without importing a
production module.

The subdirectory `dimension-necessity/` preserves a separately written but
retracted reconstruction of a quantitative lower bound. Pre-release review
expanded its incomplete 19-source packet to 21 sources and then found a
missing localized-response/commutator premise. The exact arithmetic remains a
conditional ledger. The public history does not externally time-seal the
original chronology.
