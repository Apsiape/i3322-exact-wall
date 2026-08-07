# P4 Receipts and Symbol Hygiene — v27

## P4(a) finite near-maximizer R0 receipt

For every finite-dimensional strategy of value \(S-\varepsilon\),
\[
\boxed{\langle\psi,R_{0,S}(X,U)\psi\rangle\le\varepsilon.}
\]
Derivation: use the generic positive weld at every \(q>S\), take expectation, then let \(q\downarrow S\) using the canonical uniform storage convergence and the positive G1 storage floor.

Because
\[
R_{0,S}=\phi_S(X,U)
\]
is functional calculus of the **commuting pair** \((X,U)\), every joint spectral projection
\[
Q=F(U)E(X)
\]
commutes with \(R_{0,S}\). No such statement is asserted for an arbitrary positive operator.

## P4(b) residual symbols

Use the following names in the v27 layer:

- \(r_A^{\rm step},r_B^{\rm step}\): live one-step response residual vectors;
- \(r_A^{\rm ret},r_B^{\rm ret}\): fitted common-return residuals appearing only in R1;
- \(e_k\): scalar amplitude error in the selected cell recurrence;
- \(e_{\rm ret}=\|r_A^{\rm ret}-q r_B^{\rm ret}\|\): R1 distorted-return error;
- \(m_C\): minimum **selected bridge-block amplitude** on a repeated cycle;
- \(b_{\rm amp}(t)=\sqrt{1-t^2}/2\): response amplitude function;
- \(\iota(t)=-t\): scalar reflection map;
- \(\Gamma_j\): prefix gain product; \(\Gamma_d\): uniform exponential lower prefix bound.

The withdrawn estimate on separate individual fitted-return norms is not consumed.

## P4(c) anchor

For sufficiently small deficit, retained joint mass is at least \(1/2\). A local dimension-\(d\) X operator has at most \(d\) occupied X marginal cells. Pigeonhole therefore gives
\[
\boxed{z_0^2\ge\frac1{2d}.}
\]
No component-rank ledger is used.

## P4(d) reflection/grid symbols

The live cell partition is the reflection-equivariant Borel partition of `02_CELL_RESPONSE_AND_BRIDGE_RECURRENCE_V27.md`. It is not the ordinary all-left-closed/right-open partition used in v26.
