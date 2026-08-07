# Commission v26-L — Lower-Bound-Only Promotion Audit

Audit refutation-first. The qualitative Theorem (N) is already promoted and is not on trial. The upper constructive rate is out of promotion scope.

Target claim:
\[
\boxed{S-S_d\ge c(1+d)^{-K}e^{-Cd}}
\]
for finite constants, hence \(D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon))\).

## Gate L1 — raw-cell deletion and parity edge budget

Verify the reflection-symmetric grid, the \(O(\varepsilon^{1/8})\) far-inversion cover, and the proof that no-far-inversion support decomposes into four monotone parity subgraphs with
\[
|E_{\rm cell}|\le4d.
\]
Attack spectral ties explicitly. A tie must not create a component merge because no components exist.

## Gate L2 — response/bridge typing and global ownership

Verify that response localization is same-marginal, reflection maps grid cells exactly to grid cells, and the X/U switch is only through an actual joint spectral block. Check
\[
\sum e_k^2\le C\mathcal E,
\quad L\le2d,
\quad \sum D_k\le8d.
\]
Reject any hidden cross-marginal substitution inside \(W\) or \(W_B\).

## Gate L3 — repeated-cell scalar exactification

Under \(\mathcal E_n/m_{C,n}^2\to0\), verify the finite near-maximizer \(R_0\) receipt, joint-block commutation, sublevel trimming, and the minimum-U squeeze
\[
P(u_{\min})+P(-u_{\min})\to0.
\]
The proof must use only monotonicity/closedness of \(Z\); no a.e. `Y_0`, no finite-n \(a\) or \(\tau\), and evenness must come from the marginal-type bipartite cycle.

## Gate L4 — state-carrying common return / v22B repair

Verify that the adjacent trimmed bridge vectors give a nonzero exact source fibre and reflected destination fibre, and that both exact normalized response transports act on the **same state component pair**. Confirm arbitrary multiplicity is harmless after norms. Then verify
\[
\alpha=\beta
\]
comes from the two state equations—not from scalar fixed return alone—and that the neutral quarter ceiling applies.

## Gate L5 — dimension-independent repeat payment and R1 scope

Verify the compact-contradiction inference
\[
m_C^2\le C_C\mathcal E
\]
with \(C_C\) independent of dimension and cycle length. Separately verify R1 only in distorted-return scope and confirm no withdrawn individual fitted-return estimate is consumed.

## Gate L6 — exponential assembly

Verify the anchor \(z_0^2\ge1/(2d)\), prefix product \(\Gamma_d=2^{-4d}\bar\sigma^{2d}\), Green factor \(e^{O(d)}\), sink/repeat dichotomy, \(\mathcal E\le C_0\varepsilon^{1/8}\), and the final eighth-power inversion. Confirm every marginal-cell count bound comes from local dimension, not the retracted component rank ledger.

## Required verdict

For each gate return exactly one of:

- **PASS** — with the critical inequality/receipt;
- **FAIL** — with the first false implication and preferably a countermodel;
- **CONDITIONAL** — only with one precise missing finite receipt.

**Promotion rule:** six PASS verdicts promote only the lower theorem. Anything else blocks. Do not adjudicate \(D_{\rm upper}\) or \(\Theta(\log)\) in this commission.
