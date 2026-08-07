# Commission v28 Closeout Checklist

This index maps every requested condition to the exact v28 receipt. No item below claims new mathematics.

| condition | landed receipt | guard / note |
|---|---|---|
| A1 normalized `K_A,K_B`; normalized gains are `F(q)` variables | Doc 04 §§1,6; Doc 06 symbol table | `guard_return_hygiene.py` raw-vs-normalized negative control |
| A2 multiplier-law parallelism | Doc 04 §2, using SHIFTED_GRID (2.1)–(2.3) provenance + exact multiplier dependency | multiplicity 1,2,4,8 guard; isometry-only negative control |
| A3 involutivity; both component equations; `Q=S` | Doc 04 §§1,5 | exact `F(1)=1/4` guard retained |
| A4 rescaled nonzero fibres / ultraproduct hygiene | Doc 04 §3 | live-hygiene symbol/route scan |
| B1 explicit Bob/Alice derivation of (3.4)/(3.5) | Doc 03 §3 | existing actual-Z squeeze guard retained |
| B2 bipartite/even cycle | Doc 03 §1 | side-tagged walk in Doc 02 |
| C1 `I <= 2 <R0> <= 2 eps` from bilinear+separable `phi_S` | Doc 01 §1 | `guard_monge_cross_difference.py` |
| C2 G1 endpoint positivity/collar with named constants | imported G1 dependency + Doc 02 §1 | `guard_g1_endpoint_arithmetic.py` |
| C3 strict grid-transfer lemma | Doc 01 §3 | `guard_grid_transfer_strict.py` |
| C4 corrected parity display | Doc 01 §4 | sparse 1x1 negative control in edge guard |
| C5 side-tagged walk state and unchanged `Gamma_d` | Doc 02 §6 | live-chain consistency scan |
| C6 reflection-fixed central cell | Doc 02 §7 | neutral case explicitly typed |
| C7 reflection-symmetric G1 corridor | Doc 02 §1 | named `K=-K` |
| C8 odd-cell sink subsection | Doc 02 §8 | `xi_I,c_I,D_I` ownership in §§3–4 |
| C9 `xi_I`; source/destination indexing; no dilation; Alt-A anchor substitution | Doc 02 §§3,4,9; Doc 05 §2 | live hygiene + L6 guard |
| D1 restore v26 ledger entries + predecessor diff | Doc 07 | live-hygiene guard |
| D2 real return guard | `guards/guard_return_hygiene.py` | multiplicities 1,2,4,8 + negatives |
| D3 enforce live authority hygiene | `guards/guard_live_authority_hygiene.py` | symbol typing + killed-item absence |
| D4 upper/R1/RHO/index hygiene | upper scope/RHO files + R1 dependency + receipt index | live-hygiene guard |

**Promotion state:** withheld pending the diff-only Commission v28-L replay.
