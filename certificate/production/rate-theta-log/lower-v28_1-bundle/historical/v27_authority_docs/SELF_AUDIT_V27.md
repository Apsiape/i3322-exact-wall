# Independent Self-Audit — v27 Lower Bound

**Date:** 2026-08-06  
**Scope:** lower theorem only.  
**Method:** refutation-first replay after the v26 conditional findings were repaired.

## L1 — PASS

Far-inversion deletion remains \(O(\varepsilon^{1/8})\). After deletion, splitting raw joint-cell support by row/column parity produces four monotone supports, hence
\[
|E_{\rm cell}|\le4d.
\]
No component merging or component rank ledger is used.

## L2 — PASS

The v27 odd-cell Borel partition is exactly reflection-equivariant, including boundary atoms:
\[
-I_j=I_{N-1-j}.
\]
The dedicated guard checks 62,500 exact rational points, including 2,650 exact cell-boundary atoms. Same-marginal response typing is therefore literal at projector level. The X/U switch remains only through an actual joint state block. Global ownership gives
\[
\sum e_k^2\le C\mathcal E,
\quad L\le2d,
\quad \sum D_k\le8d.
\]

## L3 — PASS

Every finite-n scalar evaluation is at an actual zero-graph projection in \(D=\operatorname{dom}P\). The cycle supplies
\[
|s_k+t_k|\le\delta_n,
\qquad
|P(t_{k+1})+P(s_k)|\le\delta_n.
\]
At a minimum \(t_j\), monotonicity and the compact-domain modulus \(\omega_P\) give
\[
|P(t_j)+P(s_j)|\le\delta_n+\omega_P(2\delta_n).
\]
Thus the limit satisfies
\[
s_*=-t_*,
\qquad
P(s_*)=-P(t_*).
\]
The finite guard checks 598 admissible cyclic configurations on non-reflection-closed partial domains; all 598 have \(-t_{\min}\notin\operatorname{dom}P\), so the guard explicitly exercises the former failure mode.

## L4 — PASS

Sublevel trimming loses \(o(m_C)\) norm; shrinking cells plus the strict graph identify one nonzero source complete fibre over \((x_*,u_*)\) and one destination complete fibre over \((-x_*,-u_*)\). The exact response equations act on the same state pair:
\[
K_Av_+=\alpha v_-,
\qquad
K_Bv_+=\beta v_-.
\]
Isometry gives
\[
\alpha=\beta.
\]
This uses the state-carrying common pair, not scalar fixed return alone. Multiplicity is harmless because the response coefficient is scalar functional calculus on a complete fibre. Neutral gain invokes the promoted quarter ceiling.

## L5 — PASS

If no dimension-independent \(C_C\) existed, one could choose a sequence with
\[
\mathcal E_n/m_{C,n}^2\to0.
\]
The L3--L4 compact contradiction uses only fixed scalar compacta, normalized local vectors, and exact response equations, so growing dimension or cycle length cannot evade it. Hence
\[
m_C^2\le C_C\mathcal E
\]
with fixed \(C_C\). R1 remains live only for already-typed distorted returns and no withdrawn individual fitted-residual estimate is consumed.

## L6 — PASS

The walk has
\[
z_0^2\ge1/(2d),
\quad L\le2d,
\quad \sum D_k\le8d,
\]
with prefix floor
\[
\Gamma_d=2^{-4d}\bar\sigma^{2d}.
\]
The explicit Green factor satisfies
\[
\mathcal H_d\le\sqrt{2d}\max(1,\sigma)^{2d}.
\]
If accumulated error is large it pays directly. Otherwise all marginal amplitudes retain the \(\Gamma_d\) floor. Before asserting a bridge floor, v27 now splits again: either a local \(e_k\) is large and pays directly, or
\[
m_k\ge \frac{\sigma}{4\sqrt d}\Gamma_dz_0.
\]
Sink or repeat service then gives
\[
\mathcal E\ge c(1+d)^{-K}e^{-Cd}.
\]
Since the v27 far deletion is below \(128\varepsilon^{1/8}\) and endpoint deletion is \(O(\varepsilon)\), eighth-power inversion gives
\[
S-S_d\ge c_0(1+d)^{-K_0}e^{-C_0d}.
\]

# Verdict

\[
\boxed{
L1=L2=L3=L4=L5=L6=\mathrm{PASS}.
}
\]

**Self-audit verdict:** the v27 lower theorem is **promotion-eligible under this six-gate audit**. It remains prudent to obtain an independent external replay before public promotion. The constructive upper rate and full \(\Theta(\log)\) statement remain outside this audit.
