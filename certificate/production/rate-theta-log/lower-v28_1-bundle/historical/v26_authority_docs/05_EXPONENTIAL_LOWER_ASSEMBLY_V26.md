# Exponential Lower Assembly — v26

Let
\[
\mathcal E=\varepsilon+\beta_{\rm far}+\beta_{\rm end}.
\]
For sufficiently small \(\varepsilon\), retained joint mass is at least \(1/2\). Since there are at most \(d\) occupied X marginal cells, one anchor obeys
\[
\boxed{z_0^2\ge\frac1{2d}.}
\]

The simple marginal-cell walk satisfies
\[
L\le2d,
\qquad
\sum D_k\le8d,
\qquad
\sum e_k^2\le C_R\mathcal E,
\]
and every deterministic prefix product is at least
\[
\Gamma_d=2^{-4d}\bar\sigma^{2d},\qquad \bar\sigma=\min(1,\sigma).
\]

The standard Green dichotomy gives either direct payment
\[
\mathcal E\ge \operatorname{poly}(d)^{-1}\Gamma_d^2 z_0^2,
\]
or every visited marginal packet stays above a fixed exponential fraction of \(z_0\). In the latter branch, each selected bridge block is also at least \(\operatorname{poly}(d)^{-1/2}\Gamma_dz_0\).

At a sink, response/deletion service pays that amplitude. At a repeat, the dimension-free repeated-cell theorem gives \(m_C^2\le C_C\mathcal E\). Hence in all cases
\[
\boxed{
\mathcal E\ge c(1+d)^{-K}e^{-Cd}.
}
\]

For the reflection-symmetric grid, \(\beta_{\rm far}\le54\varepsilon^{1/8}\). G1 endpoint-collar deletion is \(O(\varepsilon)\), so for one fixed \(C_0\),
\[
\mathcal E\le C_0\varepsilon^{1/8}
\]
for \(0<\varepsilon\le1\). Therefore
\[
\boxed{
S-S_d=\varepsilon
\ge c_0(1+d)^{-K_0}e^{-C_0'd}.
}
\]
Equivalently,
\[
\boxed{D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).}
\]

**Status:** theorem candidate pending the six-gate hostile re-audit.
