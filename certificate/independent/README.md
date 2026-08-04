# Independent I3322 interval reconstruction

This directory reconstructs the complete computer-assisted Bellman input
without Arb or any production Python module. It uses `mpmath.iv` real
intervals and a local rectangular-complex layer.

Run from this directory's repository root:

```powershell
python certificate/independent/arithmetic_selftest.py
python certificate/independent/plateau_series_mpmath.py
python certificate/independent/analytic_tail_mpmath.py
python certificate/independent/shooting_miranda_mpmath.py
python certificate/independent/global_graph_mpmath.py
python certificate/independent/verify_independent_reconstruction.py
python certificate/independent/spatial_symbolic_verify.py
python certificate/independent/truncation_flux_mpmath.py
```

The global graph pass takes roughly three minutes on the reference machine.
The assembler checks the source AST for forbidden `flint` imports before it
loads a production receipt for post-verdict numerical comparison.

The final two commands separately reconstruct the spatial Bell-to-Jacobi
identity and the finite-section boundary-flux law. The truncation engine also
derives and interval-encloses the plateau exponent without importing a
production module.

The subdirectory `dimension-necessity/` is a separate blind reconstruction of
the quantitative lower bound. It freezes the literal 19-source packet seen by
the reconstructing agent, its preregistration and full proof, and a subsequent
exact-arithmetic hostile audit. It neither imports nor paraphrases the
production dimension-bound assembly.
