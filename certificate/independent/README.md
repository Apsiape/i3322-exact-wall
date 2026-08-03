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
```

The global graph pass takes roughly three minutes on the reference machine.
The assembler checks the source AST for forbidden `flint` imports before it
loads a production receipt for post-verdict numerical comparison.
