# Exponential Lower Assembly — v28

Let
\[
\mathcal E=\varepsilon+\beta_{\rm far}+\beta_{\rm end}.
\tag{1.1}
\]
For sufficiently small deficit, retained joint mass is at least \(1/2\). Since the original local X factor has dimension at most \(d\), at most \(d\) X marginal cells are occupied. Therefore
\[
\boxed{z_0^2\ge\frac1{2d}.}
\tag{1.2}
\]
No dilation or component-rank ledger is used.

Doc 02 gives
\[
L\le2d,
\qquad
\sum D_k<8d,
\qquad
\sum e_k^2\le C_R\mathcal E.
\tag{1.3}
\]
Put
\[
\bar\sigma=\min(1,\sigma),
\qquad
\Gamma_d=2^{-4d}\bar\sigma^{2d}.
\tag{1.4}
\]

## 2. Green dichotomy

Let \(g_k=\sigma/\sqrt{D_k}\). Iterating
\[
z_{k+1}\ge g_kz_k-e_k
\]
gives, for every prefix,
\[
z_j\ge G_jz_0-\sum_{i<j}G_{i+1,j}e_i,
\]
with
\[
G_j\ge\Gamma_d,
\qquad
G_{i+1,j}\le\max(1,\sigma)^{2d}.
\]
Therefore
\[
\sum_{i<j}G_{i+1,j}e_i
\le
\mathcal H_d\sqrt{C_R\mathcal E},
\qquad
\boxed{\mathcal H_d\le\sqrt{2d}\max(1,\sigma)^{2d}.}
\tag{2.1}
\]

### Alternative A — accumulated error pays

If
\[
\mathcal H_d\sqrt{C_R\mathcal E}\ge\frac12\Gamma_dz_0,
\]
then
\[
\mathcal E
\ge
\frac{\Gamma_d^2z_0^2}{4C_R\mathcal H_d^2}.
\]
Substituting (1.2) **at this line**, as required by the audit,
\[
\boxed{
\mathcal E
\ge
\frac{\Gamma_d^2}{8d\,C_R\mathcal H_d^2}
\ge
c(1+d)^{-K}e^{-Cd}.
}
\tag{2.2}
\]

### Alternative B — all visited marginal packets remain large

Otherwise every visited state satisfies
\[
\boxed{z_k\ge\frac12\Gamma_dz_0.}
\tag{2.3}
\]

## 3. Local-error horn before any bridge floor

Let \(m_k\) be the actual selected joint bridge amplitude. Then
\[
m_k\ge\frac{\sigma}{\sqrt{D_k}}z_k-e_k.
\tag{3.1}
\]
Since \(D_k\le d\):

- if for some step
  \[
  e_k\ge\frac{\sigma}{4\sqrt d}\Gamma_dz_0,
  \]
  then
  \[
  \mathcal E\ge c\,d^{-1}\Gamma_d^2z_0^2
  \ge c' d^{-2}\Gamma_d^2;
  \tag{3.2}
  \]
- otherwise every selected bridge satisfies
  \[
  \boxed{
  m_k\ge\frac{\sigma}{4\sqrt d}\Gamma_dz_0,
  }
  \tag{3.3}
  \]
  and on a repeat
  \[
  \boxed{
  m_C^2\ge c\,d^{-1}\Gamma_d^2z_0^2
  \ge c' d^{-2}\Gamma_d^2.
  }
  \tag{3.4}
  \]

## 4. Terminal service

A sink is paid by Doc 02 (8.2). In Alternative B the visited sink state still obeys (2.3), so the composition is explicitly
\[
z_k^2\ge\frac14\Gamma_d^2z_0^2,
\]
\[
z_k^2\le C_{\rm sink}\mathcal E,
\]
\[
\boxed{\mathcal E\ge\frac{\Gamma_d^2z_0^2}{4C_{\rm sink}}\ge\frac{\Gamma_d^2}{8d\,C_{\rm sink}}.}
\tag{4.1a}
\]
A repeat is paid by Doc 04:
\[
m_C^2\le C_C\mathcal E.
\]
Together with the direct horns above,
\[
\boxed{
\mathcal E\ge c(1+d)^{-K}e^{-Cd}.
}
\tag{4.1}
\]

## 5. Eighth-power inversion

Docs 01/02 give
\[
\beta_{\rm far}<128\varepsilon^{1/8},
\qquad
\beta_{\rm end}\le C_{\rm end}\varepsilon.
\]
Thus for one fixed \(C_0\),
\[
\mathcal E\le C_0\varepsilon^{1/8}
\qquad(0<\varepsilon\le1).
\tag{5.1}
\]
Combining with (4.1) and raising to the eighth power,
\[
\boxed{
S-S_d=\varepsilon
\ge
c_0(1+d)^{-K_0}e^{-C_0'd}.
}
\tag{5.2}
\]
Equivalently,
\[
\boxed{D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).}
\tag{5.3}
\]

For deficits above the fixed small-deficit regime threshold, decrease the universal prefactor \(c_0\); since \((1+d)^{-K_0}e^{-C_0'd}\le1\), the same displayed bound then holds for all finite \(d\).
