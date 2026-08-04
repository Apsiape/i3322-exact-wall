# Certificate map

This file separates analytic claims from computer-assisted inputs.

## Main analytic chain

| Claim | Owner | Verification |
|---|---|---|
| Bell-operator reparameterization (4.3) | Sprint 1197 | `bellman_quantum_dual_verify.py` |
| Geometric Cauchy inequality (3.4) | Sprint 1197 | exact SymPy residual plus paper proof |
| Product laws (3.5) | Sprint 1197 | exact SymPy residual plus direct multiplication |
| Commutant local factorization (4.9)–(4.10) | Sprint 1199 | exact block factor plus hidden direct-sum guards |
| Finite support reversal | Sprints 1198/1200 | exhaustive and rank-formula independent engines |
| Amplitude elimination (6.1)–(6.5) | Sprints 1198/1200 | two independent symbolic scripts |
| Quarter ceiling (6.6)–(6.8) | Sprints 1198/1200 | exact polynomial identities and paper proof |

| Infinite alternating projections | Sprint 1206 | direct-sum proof plus two exact guards |
| Spatial Bell-to-Jacobi identity | Sprint 1206 | exact-rational fixtures and independent symbolic reconstruction |
| Normal vector-state attainment | Sprint 1206 | `ell^2` wall input plus absolute-convergence proof |

## Spatial-separation and nonclosure chain

| Claim | Owner | Verification |
|---|---|---|
| `C_q(3,3;2,2)` nonclosure | Corollary to main theorem | compact subsequence plus continuity |
| `C_qs(3,3;2,2) \ C_q(3,3;2,2)` witness | Sprint 1206 | explicit normal vector state at `q_*` plus nonattainment |
| Binary input-count minimality | Jordan/Schmidt argument | self-contained analytic proof in manuscript |

Neither row adds a computer-assisted dependency beyond the main theorem.

## Computer-assisted Bellman input

| Input | Receipt or engine |
|---|---|
| Hyperbolic algebraic plateau | `certificate/production/foundational-sprint-1115/plateau-hyperbolicity-certificate.json` |
| Validated shooting zero and `q_*` interval | `certificate/production/foundational-sprint-1116/validated-exact-shooting-degree.json` |
| Analytic local unstable manifold | `certificate/production/foundational-sprint-1116/analytic-tail-graph-transform.json` |
| Exact envelope covariance | `certificate/production/foundational-sprint-1195/contact_covariance_verify.py` |
| Strict central graph | `certificate/production/foundational-sprint-1192/exact_invariant_graph_projection.py` |
| Strict endpoint wings | `certificate/production/foundational-sprint-1193/exact_boundary_wing.py` |
| Inactive predecessor exclusion | `certificate/production/foundational-sprint-1194/inactive_outer_guard.py` |
| Bellman theorem assembly | `certificate/production/foundational-sprint-1195/theorem_assembly_verify.py` |

### Independent interval reconstruction

The directory `certificate/independent/` reconstructs all of
the preceding computer-assisted inputs using `mpmath.iv`, a locally written
rectangular complex-interval class, and no imports from production Arb/FLINT
modules. `independent-reconstruction.json` records eight passing gates and an
exact directed-overlap check against the production `q_*` receipt performed
only after the independent verdict was assembled.

## End-to-end theorem receipts

- `certificate/production/foundational-sprint-1197/theorem-assembly.json`
- `certificate/production/foundational-sprint-1198/theorem-assembly.json`
- `certificate/production/foundational-sprint-1199/theorem-assembly.json`
- `certificate/production/foundational-sprint-1200/dependency-audit.json`
- `certificate/production/foundational-sprint-1200/independent-nonattainment.json`
- `certificate/production/foundational-sprint-1206/spatial-realization-guard.json`
- `certificate/independent/spatial-symbolic-guard.json`

## Reproduction commands

The release-level entry points are:

```powershell
python certificate/release/verify_release.py
python certificate/release/verify_release.py --full
```

Quick mode checks frozen SHA-256 custody and semantic receipt gates. Text is
hashed after canonical LF normalization and PDFs as raw bytes, so checkout
line-ending policy cannot create a false custody failure. Full mode
also runs the individual commands below, including the independent interval
reconstruction. The production half is deterministic replay; the independent
half is a separately implemented certificate path.

From the repository root:

```powershell
python certificate/production/foundational-sprint-1192/exact_invariant_graph_projection.py
python certificate/production/foundational-sprint-1193/exact_boundary_wing.py
python certificate/production/foundational-sprint-1194/inactive_outer_guard.py
python certificate/production/foundational-sprint-1195/contact_covariance_verify.py
python certificate/production/foundational-sprint-1195/theorem_assembly_verify.py
python certificate/production/foundational-sprint-1196/cyclic_sos_verify.py
python certificate/production/foundational-sprint-1197/bellman_quantum_dual_verify.py
python certificate/production/foundational-sprint-1197/symmetrized_dual_guard.py
python certificate/production/foundational-sprint-1197/operator_remainder_random_guard.py
python certificate/production/foundational-sprint-1197/theorem_assembly_verify.py
python certificate/production/foundational-sprint-1198/equality_kernel_verify.py
python certificate/production/foundational-sprint-1198/theorem_assembly_verify.py
python certificate/production/foundational-sprint-1199/commuting_certificate_verify.py
python certificate/production/foundational-sprint-1199/theorem_assembly_verify.py
python certificate/production/foundational-sprint-1200/independent_nonattainment_verify.py
python certificate/production/foundational-sprint-1200/dependency_audit.py
python certificate/production/foundational-sprint-1206/spatial_realization_verify.py
python certificate/release/normalization_concordance_verify.py
python certificate/release/dimension_gap_audit.py
python certificate/independent/arithmetic_selftest.py
python certificate/independent/plateau_series_mpmath.py
python certificate/independent/analytic_tail_mpmath.py
python certificate/independent/shooting_miranda_mpmath.py
python certificate/independent/global_graph_mpmath.py
python certificate/independent/verify_independent_reconstruction.py
python certificate/independent/spatial_symbolic_verify.py
```

The production graph covers take approximately one minute in total and the
independent graph reconstruction approximately three minutes on the reference
workstation. The remaining commands complete in seconds.

`certificate/release/release-manifest.json` freezes every standalone source,
dependency, and receipt hash. `paper/TECHNICAL-SUPPLEMENT.md` explains every numerical margin and also
records two rejected instruments: the six-forward-piece graph convention and
the endpoint line-derivative guard.
