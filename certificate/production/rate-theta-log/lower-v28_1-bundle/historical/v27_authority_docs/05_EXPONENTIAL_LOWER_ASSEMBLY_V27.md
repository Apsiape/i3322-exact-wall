# Exponential Lower Assembly — v27

Let
\[
\mathcal E=\varepsilon+\beta_{\rm far}+\beta_{\rm end}.
\tag{1.1}
\]
For sufficiently small \(\varepsilon\), retained joint mass is at least \(1/2\). Since a local dimension-\(d\) scalar operator has at most \(d\) occupied X marginal cells, one retained X-cell anchor obeys
\[
\boxed{z_0^2\ge\frac1{2d}.}
\tag{1.2}
\]

The simple marginal-cell walk satisfies
\[
L\le2d,
\qquad
\sum D_k\le8d,
\qquad
\sum e_k^2\le C_R\mathcal E.
\tag{1.3}
\]
Every deterministic prefix product is at least
\[
\Gamma_d=2^{-4d}\bar\sigma^{2d},
\qquad
\bar\sigma=\min(1,\sigma).
\tag{1.4}
\]

## 2. Green dichotomy

Put
\[
g_k=\frac{\sigma}{\sqrt{D_k}}.
\]
Iterating gives
\[
z_j\ge G_jz_0-\sum_{i<j}G_{i+1,j}e_i,
\]
where \(G_j=\prod_{k<j}g_k\) and \(G_{i+1,j}=\prod_{i<k<j}g_k\). By (1.3)--(1.4),
\[
G_j\ge\Gamma_d
\]
for every prefix, while
\[
G_{i+1,j}\le\max(1,\sigma)^{2d}.
\]
Thus Cauchy--Schwarz and \(L\le2d\) give the explicit Green bound
\[
\sum_{i<j}G_{i+1,j}e_i
\le
\mathcal H_d\sqrt{C_R\mathcal E},
\qquad
\boxed{\mathcal H_d\le\sqrt{2d}\max(1,\sigma)^{2d}.}
\tag{2.0}
\]
This is \(\operatorname{poly}(d)e^{O(d)}\).

### Alternative A — accumulated error already pays

If
\[
\mathcal H_d\sqrt{C_R\mathcal E}
\ge
\frac12\Gamma_dz_0,
\]
then
\[
\boxed{
\mathcal E
\ge
\frac{\Gamma_d^2z_0^2}{4C_R\mathcal H_d^2}
\ge
c(1+d)^{-K}e^{-Cd}z_0^2.
}
\tag{2.1}
\]
This is already polynomial-times-exponential in \(d\).

### Alternative B — every visited marginal packet remains large

Otherwise every visited marginal cell satisfies
\[
\boxed{
z_k\ge\frac12\Gamma_d z_0.
}
\tag{2.2}
\]

## 3. Explicit local-error horn for selected bridge blocks

Let \(m_k\) be the actual selected joint bridge-block amplitude used to leave the marginal cell at step \(k\). The cell response/bridge theorem gives
\[
m_k\ge \frac{\sigma}{\sqrt{D_k}}z_k-e_k.
\tag{3.1}
\]
Because \(D_k\le d\), there are two cases.

### Horn B1 — one local recurrence error is large

If for some visited step
\[
e_k\ge \frac{\sigma}{4\sqrt d}\Gamma_d z_0,
\tag{3.2}
\]
then from \(e_k^2\le C_R\mathcal E\),
\[
\boxed{
\mathcal E
\ge
c\,d^{-1}\Gamma_d^2z_0^2.
}
\tag{3.3}
\]
So the desired exponential class is paid directly.

### Horn B2 — all local recurrence errors are small

Otherwise, by (2.2), (3.1), and \(D_k\le d\), every selected bridge obeys
\[
\boxed{
m_k\ge \frac{\sigma}{4\sqrt d}\Gamma_dz_0.}
\tag{3.4}
\]
Hence on any repeated cycle
\[
\boxed{
m_C^2\ge c\,d^{-1}\Gamma_d^2z_0^2.}
\tag{3.5}
\]

## 4. Terminal service

At a sink, the inherited response/deletion sink receipt pays the same marginal amplitude scale.

At a repeat, the v27 dimension-free repeated-cell theorem gives
\[
m_C^2\le C_C\mathcal E.
\tag{4.1}
\]
Combining (3.5), (4.1), and (1.2), or using the direct-payment horns above, yields in every terminal branch
\[
\boxed{
\mathcal E
\ge
c(1+d)^{-K}e^{-Cd}.
}
\tag{4.2}
\]
No \(d^{-d}\) factor occurs.

## 5. Eighth-power inversion

For the v27 reflection-equivariant odd-cell partition,
\[
\beta_{\rm far}<128\varepsilon^{1/8}.
\tag{5.1}
\]
G1 endpoint-collar deletion is \(O(\varepsilon)\). Therefore for one fixed \(C_0\),
\[
\mathcal E\le C_0\varepsilon^{1/8}
\qquad(0<\varepsilon\le1).
\tag{5.2}
\]
Combining (4.2) and (5.2),
\[
C_0\varepsilon^{1/8}
\ge
c(1+d)^{-K}e^{-Cd}.
\]
Raising to the eighth power and absorbing fixed constants,
\[
\boxed{
S-S_d=\varepsilon
\ge
c_0(1+d)^{-K_0}e^{-C_0'd}.
}
\tag{5.3}
\]
Equivalently,
\[
\boxed{D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).}
\tag{5.4}
\]

**Status:** theorem candidate pending the six-gate v27 hostile re-audit.

## 6. Large-deficit closure

The argument above is written in the small-deficit regime where the retained-mass anchor is at least \(1/2\). If \(\varepsilon\) is above that fixed regime threshold, the claimed lower bound is made automatic by decreasing the universal prefactor \(c_0\), since \((1+d)^{-K_0}e^{-C_0'd}\le1\). Thus (5.3) extends to all finite \(d\) after one fixed constant adjustment.
