# Commission v28-L — Diff-Only Lower-Bound Promotion Re-Audit

The six-gate blind v27 audit found **zero kills**. L3 was unconditional PASS; L1/L2/L4/L5/L6/INTEGRITY were PASS-WITH-CONDITIONS. v28 contains only the requested existing receipts/writing repairs. **Do not re-open verified mathematics except where needed to check that the inserted receipt says exactly what the condition required.**

Target:
\[
S-S_d\ge c(1+d)^{-K}e^{-Cd},
\qquad
D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).
\]

## L1 diff gate

PASS iff Docs 01/02 contain and correctly connect:

- the bilinear+separable \(\phi_S\) cross-difference and \(\mathcal I\le2\langle R_0\rangle\le2\varepsilon\);
- the strict mixed-closure grid-transfer lemma;
- the corrected edge display \(2m_X+2m_U-k_{\rm par}\le4d-1\), with the guard rejecting the old \(-4\) formula in sparse parity cases.

## L2 diff gate

PASS iff Doc 02 contains:

- the imported G1 endpoint positivity/compact-interior collar, with named \(\delta_0,b_0,A_{\max},C_{\rm end}\), all independent of \(\varepsilon,d\), and a reflection-symmetric corridor;
- explicit \(\xi_I\), destination-indexed \(D_I,c_I\), and odd-cell sink service;
- the side-tagged walk-state definition proving \(L\le2d\), \(\sum D_k<8d\), and therefore the unchanged \(\Gamma_d\);
- the central reflection-fixed cell case;
- the no-dilation local-dimension statement.

## L3 diff gate

The actual-Z minimum squeeze is already blind-PASS. Check only that Doc 03 now explicitly derives (3.4)/(3.5) with Bob/Alice provenance and states bipartiteness/evenness. Do not rerun the 19.3M squeeze campaign unless a textual inconsistency is found.

## L4 diff gate

PASS iff Doc 04 explicitly provides:

1. \(K_A=Wb_{\rm amp}(X)^{-1}\), \(K_B=W_Bb_{\rm amp}(U)^{-1}\), with normalized gains \(\alpha,\beta\) identified as the \(F(q)\) variables;
2. multiplier-law parallelism onto one destination fibre, not isometry-only parallelism;
3. involutivity and both exact component equations with \(Q=S\) before invoking \(F(1)=1/4\);
4. the rescaled-limit paragraph: naive atom failure, \(m_C\)-rescaling, norm-boundedness fix, \(O(\mathcal E)\) residual budget, positivity, \(\omega_{P^{-1}}\), Pythagorean marginal/joint collapse, and explicit statement that R2 is not on path.

## L5 diff gate

PASS iff the R1 dependency copy is symbol-clean, its optional TOP_D provenance is correctly classified in the receipt index, and no withdrawn separate fitted-residual estimate is reintroduced.

## L6 diff gate

PASS iff Doc 05 substitutes \(z_0^2\ge1/(2d)\) explicitly in Alternative A and the live chain uses the side-tagged walk/degree ledger from Doc 02. The previously verified horn threshold and compactness logic are not otherwise on trial.

## INTEGRITY / HYGIENE diff gate

PASS iff:

- the v26 ledger entries for partial/a.e.-\(\tau\) and the \(1/2000\) floor are restored, with a stated v27\(\to\)v28 ledger diff;
- `guard_return_hygiene.py` executes a real two-fibre normalized multiplier test at multiplicities 1,2,4,8;
- `guard_live_authority_hygiene.py` enforces symbol typing and killed-item absence in Docs 01–06;
- `UPPER_SCOPE_NOTE.md`, `RHO_Q_IDENTIFICATION.md`, and the receipt index have the v28 commission/symbol/scope corrections;
- archive/member hashes and exact endpoint/G1 guards pass.

## Promotion rule

Return PASS/FAIL/CONDITIONAL for L1–L6 and INTEGRITY. **Six L-gate PASS plus INTEGRITY PASS promotes only the lower theorem.** \(D_{\rm upper}\) and \(\Theta(\log)\) remain excluded.
