# Cell Response, G1 Collar, and X/U Bridge Recurrence — v28

## 1. G1 is an imported proved receipt, not the invalid v22 strip claim

The live source is `dependencies/G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md`, imported from the consolidated promotion bundle. It proves
\[
g_S(1)>0,\qquad g_S(-1)>0,
\tag{1.1}
\]
using the closed-interval \(3/2\)-Lipschitz modulus and the exact endpoint-line reserves; it then proves that the closed full-zero set
\[
Z=R_{0,S}^{-1}(0)
\]
is compactly interior and that
\[
m_g:=\min_{[-1,1]}g_S>0.
\tag{1.2}
\]
It explicitly supersedes the invalid v22 boundary-set \(\Rightarrow\) fixed-strip inference.

For named v28 constants, put
\[
g_{\partial}:=\min\{g_S(1),g_S(-1)\}>0.
\]
The \(3/2\)-Lipschitz modulus gives
\[
|t-1|\le g_{\partial}/3\Rightarrow g_S(t)\ge g_{\partial}/2,
\]
and similarly at \(-1\). Since \(Z\Subset(-1,1)^2\), choose once and for all
\[
\boxed{
\delta_0>0
}
\tag{1.3}
\]
so that
\[
Z\subset K^2,
\qquad
K:=[-1+\delta_0,1-\delta_0],
\tag{1.4}
\]
and choose \(\delta_0\) no larger than the two Lipschitz endpoint radii above. **The corridor \(K\) is reflection-symmetric:** \(K=-K\). The two separately certified endpoint margins make this common symmetric choice lawful.

Define the endpoint square collar
\[
\mathcal C_{\rm end}:=[-1,1]^2\setminus K^2.
\]
Continuity and \(Z\cap\mathcal C_{\rm end}=\varnothing\) give
\[
c_{\rm end}:=\min_{\mathcal C_{\rm end}}\phi_S>0,
\qquad
\boxed{C_{\rm end}:=2/c_{\rm end}<\infty.}
\tag{1.5}
\]
Uniform \(g_q\to g_S\) and (1.2) imply uniform \(\phi_q\to\phi_S\); hence for all sufficiently near-critical \(q>S\), \(\phi_q\ge c_{\rm end}/2\) on the collar. In the critical finite-nearmax receipt this yields
\[
\boxed{
\beta_{\rm end}\le C_{\rm end}\varepsilon.
}
\tag{1.6}
\]
All constants are independent of \(\varepsilon\) and \(d\).

Finally define
\[
b_{\rm amp}(t)=\frac{\sqrt{1-t^2}}2,
\qquad
\boxed{b_0:=\min_{t\in K}b_{\rm amp}(t)>0,}
\tag{1.7}
\]
and, for the two positive response coefficient functions in the localized identities,
\[
\boxed{
A_{\max}:=\max\Bigl(1,\sup_{t\in K}A(t),\sup_{t\in K}B(t)\Bigr)<\infty,
\qquad
\sigma:=b_0/A_{\max}>0.
}
\tag{1.8}
\]

## 2. Reflection-equivariant spectral-cell partition

Put
\[
r=\varepsilon^{1/8}\in(0,1],
\]
choose the smallest odd integer \(N=2M+1\ge2/r\), and set
\[
\eta=2/N,\qquad a_j=-1+j\eta.
\]
Then
\[
\boxed{r/2<\eta\le r.}
\tag{2.1}
\]
Define
\[
I_j=[a_j,a_{j+1})\quad(0\le j<M),
\]
\[
I_M=[a_M,a_{M+1}],
\]
\[
I_j=(a_j,a_{j+1}]\quad(M<j\le N-1).
\]
The cells are disjoint, cover \([-1,1]\), and satisfy exactly
\[
\boxed{-I_j=I_{N-1-j}}
\tag{2.2}
\]
including boundary atoms. The same partition is used for \(X\) and \(U\).

## 3. Same-marginal response and the definition of \(\xi_I\)

For Alice let
\[
r_A^{\rm step}:=A(X)\psi-W\psi,
\qquad
\|r_A^{\rm step}\|^2\le C_A\varepsilon.
\tag{3.1}
\]
The exact spectral intertwiner gives the destination-localized identity
\[
A(X)E_{-I}(X)\psi-WE_I(X)\psi
=E_{-I}(X)r_A^{\rm step}.
\tag{3.2}
\]
By \(W^*W=b_{\rm amp}(X)^2\), (1.7), and (1.8),
\[
b_0z_I^X
\le
A_{\max}z_{-I}^X+\|E_{-I}r_A^{\rm step}\|.
\]
Define
\[
\boxed{
\xi_I^X:=\frac{\|E_{-I}(X)r_A^{\rm step}\|}{A_{\max}}.
}
\tag{3.3}
\]
Then
\[
\boxed{
z_{-I}^X\ge\sigma z_I^X-\xi_I^X.
}
\tag{3.4}
\]
Orthogonality gives
\[
\sum_I(\xi_I^X)^2\le C_A\varepsilon/A_{\max}^2.
\tag{3.5}
\]
The Bob definitions \(r_B^{\rm step},\xi_J^U\) and inequalities are identical on \(U\)-cells.

## 4. Actual joint X/U bridge; source/destination indexing

For an **X-side walk state** \((\mathsf X,I)\), first reflect to the destination marginal cell \(-I\). Define

- \(D_I\): the number of retained joint cells in the **destination X-row** \(-I\);
- \(c_I\): the deleted joint probability mass in that **same destination row** \(-I\).

Thus \(D_I,c_I\) are destination-indexed quantities even though the walk state is source-indexed by \(I\).

If \(D_I>0\), the Pythagorean joint decomposition gives a retained joint bridge block of amplitude \(m_I\) with
\[
m_I
\ge
D_I^{-1/2}\sqrt{(z_{-I}^X)^2-c_I}
\ge
D_I^{-1/2}\bigl(z_{-I}^X-\sqrt{c_I}\bigr).
\tag{4.1}
\]
That exact joint block belongs to one actual \(U\)-marginal cell, so with the safe scalar error
\[
e_I:=\xi_I^X+\sqrt{c_I}
\tag{4.2}
\]
we obtain
\[
\boxed{
 z_{\rm next}^U
\ge
\frac{\sigma}{\sqrt{D_I}}z_I^X-e_I.
}
\tag{4.3}
\]
The \(U\to X\) step uses the analogous destination column convention. No response intertwiner ever substitutes an \(X\)-projection for a \(U\)-projection; the marginal-family change occurs only through the actual joint state block.

Put the total deletion mass used by this Pythagorean bridge receipt at
\[
\boxed{\beta_{\rm del}:=\beta_{\rm far}+\beta_{\rm end}\le\mathcal E.}
\tag{4.4a}
\]
This symbol is distinct from the normalized Bob gain \(\beta\) in Doc 04.

The v20 Pythagorean identities underlying this collapse are
\[
(y_k^X)^2=w_k+r_k^{\rm del},
\qquad
(y_k^U)^2=w_k+c_k^{\rm del},
\tag{4.4}
\]
\[
\sum_kr_k^{\rm del}\le\beta_{\rm del},
\qquad
\sum_kc_k^{\rm del}\le\beta_{\rm del},
\tag{4.5}
\]
and therefore
\[
\sum_k|y_k^X-y_k^U|^2\le4\beta_{\rm del}.
\tag{4.6}
\]

## 5. Global ownership

Along a simple side-tagged walk, destination response projections are used at most once on each side before the first repeated walk state. Hence
\[
\boxed{
\sum_{\rm walk}e_I^2
\le
C_R\bigl(\varepsilon+\beta_{\rm far}+\beta_{\rm end}\bigr)
=:C_R\mathcal E.
}
\tag{5.1}
\]

## 6. The walk state and the length/degree ledger

A **marginal parity cell** means the side-tagged pair
\[
\boxed{v=(\mathsf X,I)\quad\text{or}\quad v=(\mathsf U,J).}
\tag{6.1}
\]
The walk alternates sides and stops immediately before the first repeated side-tagged state. A geometric interval with the same index on the two different marginal families is therefore **not** a repeat.

There are at most \(m_X\le d\) X-states and \(m_U\le d\) U-states, so
\[
\boxed{L\le m_X+m_U\le2d.}
\tag{6.2}
\]
Reflection is a bijection of the cell set. Distinct X source states therefore use distinct destination rows, so the sum of their bridge degrees is at most \(|E_{\rm cell}|\); likewise U source states use distinct destination columns. Hence
\[
\boxed{
\sum_{\rm walk}D_I\le2|E_{\rm cell}|\le8d-2<8d.
}
\tag{6.3}
\]
Since \(D\le2^D\) for integers \(D\ge1\), every deterministic prefix product satisfies
\[
\boxed{
\Gamma_d:=2^{-4d}\min(1,\sigma)^{2d}
\le
\prod_{k<j}\frac{\sigma}{\sqrt{D_k}}.
}
\tag{6.4}
\]

## 7. Reflection-fixed central cell

The central cell satisfies
\[
I_M=-I_M.
\]
The walk does not stall there: the state is side-tagged, and after the same-marginal reflection the actual joint bridge changes the marginal family. If the exactified minimum lands at \(t_*=0\), the actual-\(Z\) squeeze gives
\[
P(0)=-P(0),
\]
so \(P(0)=0\) and \(z_+=z_-=(0,0)\). This case is killed directly by the exact critical component equation (Doc 04 (5.1)): at \(x_*=u_*=0\), (5.1) gives
\[
\boxed{
S=d(0,0)+\frac12+\frac12=-1+\frac12+\frac12=0<\frac14.
}
\tag{7.1}
\]
No identification of the two limiting fibre vectors, and no separate inference \(\alpha^2=\beta^2=1\), is used.

## 8. Sink service under the odd partition

If an X-side state has \(D_I=0\), the destination row \(-I\) contains no retained joint block. Therefore
\[
(z_{-I}^X)^2\le c_I.
\]
Combining with (3.4),
\[
\sigma z_I^X\le\xi_I^X+\sqrt{c_I},
\]
and hence
\[
\boxed{
(z_I^X)^2
\le
\frac{2}{\sigma^2}\bigl((\xi_I^X)^2+c_I\bigr).
}
\tag{8.1}
\]
Summing sink states and using (5.1) gives
\[
\boxed{
\sum_{I\in\mathrm{sinks}}z_I^2\le C_{\rm sink}\mathcal E,
\qquad C_{\rm sink}=2\sigma^{-2}\max(1,C_R).
}
\tag{8.2}
\]
The U-side case is identical.

## 9. No-dilation dimension hypothesis

Throughout the quantitative lower proof, \(X\) and \(U\) act on the original local Hilbert factors of dimension at most \(d\). No Naimark dilation is used in the cell-count ledger. For binary measurements one may perform the standard dimension-preserving extreme-effect replacement at fixed local dimension before taking the finite-dimensional supremum; the quantitative argument is then applied on those same \(d\)-dimensional factors. Thus
\[
m_X,m_U\le d
\]
is a statement about the actual local dimension being bounded, not a dilated auxiliary space.
