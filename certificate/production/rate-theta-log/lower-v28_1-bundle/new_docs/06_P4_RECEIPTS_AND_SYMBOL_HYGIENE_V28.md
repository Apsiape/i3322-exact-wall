# P4 Receipts and Symbol Hygiene — v28

## 1. Finite near-maximizer \(R_0\) receipt

For every finite-dimensional strategy of Bell value \(S-\varepsilon\),
\[
\boxed{\langle\psi,R_{0,S}(X,U)\psi\rangle\le\varepsilon.}
\]
It is obtained from the generic positive weld at \(q>S\) and the canonical uniform storage convergence as \(q\downarrow S\). Since \(R_{0,S}=\phi_S(X,U)\) is functional calculus of the commuting pair, every joint spectral bridge projection \(Q=F(U)E(X)\) commutes with \(R_{0,S}\). No such commutation is asserted for arbitrary positive operators.

## 2. Frozen symbol table

- \(b_{\rm amp}(t)=\sqrt{1-t^2}/2\): response amplitude function.
- \(b_0=\min_{t\in K}b_{\rm amp}(t)>0\): uniform G1 corridor amplitude floor.
- \(A_{\max}\): fixed upper bound for the positive response coefficient functions on \(K\).
- \(\sigma=b_0/A_{\max}>0\): normalized same-marginal response floor.
- \(\delta_0>0\): fixed reflection-symmetric G1 corridor inset, \(K=[-1+\delta_0,1-\delta_0]\).
- \(C_{\rm end}\): fixed endpoint-collar payment constant with \(\beta_{\rm end}\le C_{\rm end}\varepsilon\).
- \(\iota(t)=-t\): scalar reflection map.
- \(W,W_B\): raw Alice/Bob response operators before \(b_{\rm amp}\)-normalization.
- \(K_A=Wb_{\rm amp}(X)^{-1}\), \(K_B=W_Bb_{\rm amp}(U)^{-1}\): **normalized** response transports on the G1 corridor.
- \(\phi_S(x,u)=R_{0,S}(x,u)\): critical scalar \(R_0\) weld; \(Z=\phi_S^{-1}(0)\).
- \(Q\): common scalar left side in the two exact return component equations; on the critical zero pair, \(Q=S\).
- \(\mathcal I\): ordered inversion energy of the joint spectral measure.
- \(\alpha,\beta>0\): **source-evaluated** normalized multiplier gains consumed by \(F(q)\), \(q=\alpha/\beta\); the source-to-reflected-destination vector coefficients are \(1/\alpha,1/\beta\). Endpoint labels never use bare \(\alpha\) or \(\beta\) in the v28 layer.
- \(\beta_{\rm far}\): far-inversion deletion mass.
- \(\beta_{\rm end}\): endpoint/collar deletion mass.
- \(\beta_{\rm del}:=\beta_{\rm far}+\beta_{\rm end}\): total deletion mass in the Pythagorean marginal-to-joint receipt.
- \(\mathcal E:=\varepsilon+\beta_{\rm far}+\beta_{\rm end}\): global quantitative error/deletion budget, so \(\beta_{\rm del}\le\mathcal E\).
- \(r_A^{\rm step},r_B^{\rm step}\): live one-step response residual vectors.
- \(r_A^{\rm ret},r_B^{\rm ret}\): fitted R1 common-return residual vectors.
- \(r_{A,{\rm mult}},r_{B,{\rm mult}}\): exact scalar multiplier functions in the equality module.
- \(\xi_I\): normalized same-marginal localized response error from Doc 02 (3.3).
- \(c_I\): deleted joint mass in the **destination** row/column corresponding to source walk state \(I\).
- \(D_I\): retained bridge degree in that same destination row/column.
- \(e_I\): scalar recurrence error after combining \(\xi_I\) and \(\sqrt{c_I}\).
- \(e_{\rm ret}=\|r_A^{\rm ret}-q r_B^{\rm ret}\|\): R1 combined mismatch.
- \(m_C\): minimum selected bridge-block amplitude on a repeated cycle.
- \(\Gamma_j\): actual prefix gain; \(\Gamma_d\): uniform exponential prefix floor.

The withdrawn estimate on separate fitted-return residual norms is not consumed.

## 3. Anchor and dimension convention

The quantitative proof uses the original local factors of dimension at most \(d\), not a Naimark dilation. Retained X-marginal mass is at least \(1/2\) in the small-deficit regime, so
\[
\boxed{z_0^2\ge1/(2d).}
\]
No component-rank ledger is used.
