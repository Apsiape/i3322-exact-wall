# Commission v27-L — Lower-Bound-Only Promotion Audit

Audit refutation-first. The qualitative Theorem (N) is already promoted and is not on trial. The upper constructive rate is out of promotion scope.

Target claim:
\[
\boxed{S-S_d\ge c(1+d)^{-K}e^{-Cd}}
\]
for finite constants, hence \(D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon))\).

## Gate L1 — raw-cell deletion and parity edge budget

Verify the \(O(\varepsilon^{1/8})\) far-inversion cover and the proof that no-far-inversion support decomposes into four monotone parity subgraphs with
\[
|E_{\rm cell}|\le4d.
\]
Attack exact scalar ties. No component merge is permitted because no components are used.

## Gate L2 — reflection-equivariant cell typing, response/bridge typing, ownership

Attack atoms exactly on every grid boundary. Verify the odd-cell Borel partition satisfies
\[
-I_j=I_{N-1-j}
\]
as sets and hence at spectral-projector level. Verify response localization is same-marginal and the X/U switch occurs only through an actual joint spectral block. Check
\[
\sum e_k^2\le C\mathcal E,
\quad L\le2d,
\quad \sum D_k\le8d.
\]
Reject any hidden cross-marginal substitution inside a response intertwiner.

## Gate L3 — repeated-cell scalar exactification on the actual zero-graph domain

Under \(\mathcal E_n/m_{C,n}^2\to0\), verify the finite near-maximizer \(R_0\) receipt, joint-block commutation, sublevel trimming, and the existence of actual zero-graph projections \(t_k,s_k\in\operatorname{dom}P\) satisfying
\[
|s_k+t_k|\le\delta_n,
\qquad
|P(t_{k+1})+P(s_k)|\le\delta_n.
\]
At a minimum \(t_j\), verify
\[
|P(t_j)+P(s_j)|\le\delta_n+\omega_P(2\delta_n).
\]
No evaluation of \(P\) on an undeclared reflected finite label is allowed. No a.e. `Y_0`, finite-n \(a\), or finite-n \(\tau\) may be used.

## Gate L4 — state-carrying common return / v22B repair

Verify the trimmed bridge vectors give nonzero complete-fibre source and destination components over
\[
(x_*,u_*),\quad(-x_*,-u_*),
\]
and that both exact normalized response transports act on that same state pair. Confirm arbitrary multiplicity is harmless after norms. Then verify
\[
\alpha=\beta
\]
comes from the two state equations—not scalar fixed return alone—and that the neutral quarter ceiling applies.

## Gate L5 — dimension-independent repeat payment and R1 scope

Verify the compact-contradiction inference
\[
m_C^2\le C_C\mathcal E
\]
with \(C_C\) independent of dimension and cycle length. Separately verify R1 only in distorted-return scope and confirm no withdrawn individual fitted-return estimate is consumed.

## Gate L6 — exponential assembly

Verify the anchor \(z_0^2\ge1/(2d)\), prefix product \(\Gamma_d=2^{-4d}\bar\sigma^{2d}\), Green factor \(e^{O(d)}\), the explicit local-error horn before asserting a bridge-amplitude floor, sink/repeat service, \(\mathcal E\le C_0\varepsilon^{1/8}\), and final eighth-power inversion. Confirm every marginal-cell count bound comes from local dimension, not a retracted component rank ledger.

## Required verdict

For each gate return exactly one of:

- **PASS** — with the critical inequality/receipt;
- **FAIL** — with the first false implication and preferably a countermodel;
- **CONDITIONAL** — only with one precise missing finite receipt.

**Promotion rule:** six PASS verdicts promote only the lower theorem. Anything else blocks. Do not adjudicate \(D_{\rm upper}\) or \(\Theta(\log)\) in this commission.
