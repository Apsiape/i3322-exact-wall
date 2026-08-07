# Cell Response and X/U Bridge Recurrence — v27

## 1. Reflection-equivariant spectral-cell partition

Put
\[
r=\varepsilon^{1/8}\in(0,1].
\]
Choose the **smallest odd integer**
\[
N=2M+1\ge \frac2r,
\]
and put
\[
\eta=\frac2N,
\qquad
a_j=-1+j\eta\quad(0\le j\le N).
\]
Then
\[
\boxed{\frac r2<\eta\le r.}
\]
Indeed, minimal oddness gives \(N<2/r+2\), hence
\(\eta>r/(1+r)\ge r/2\).

Define a Borel partition \(\{I_j\}_{j=0}^{N-1}\) of \([-1,1]\) by

\[
I_j=[a_j,a_{j+1})\qquad(0\le j<M),
\]

\[
I_M=[a_M,a_{M+1}],
\]

and

\[
I_j=(a_j,a_{j+1}]\qquad(M<j\le N-1).
\]

These sets are disjoint and cover \([-1,1]\). Since
\[
a_{N-j}=-a_j,
\]
reflection acts exactly, including boundary atoms:
\[
\boxed{-I_j=I_{N-1-j}.}
\tag{1.1}
\]
Thus for every self-adjoint scalar operator \(X\), functional calculus gives
\[
E_{I_j}(-X)=E_{I_{N-1-j}}(X)
\]
with no generic-position assumption on the finite spectrum. The same partition is used for \(U\).

This replaces the false v26 statement that ordinary left-closed/right-open cells are reflection-equivariant.

## 2. Far-inversion deletion

The existing far-inversion cover theorem gives
\[
\beta_{\rm far}\le 8\sqrt{\mathcal I}\,\eta^{-3},
\qquad \mathcal I\le4\varepsilon.
\]
Since \(\sqrt{\mathcal I}\le2\varepsilon^{1/2}=2r^4\) and \(\eta>r/2\),
\[
\boxed{\beta_{\rm far}<128\,\varepsilon^{1/8}.}
\tag{2.1}
\]
Only the fixed constant changes from v26; the exponent is unchanged.

## 3. Same-marginal response

Let
\[
z_I^X=\|E_I(X)\psi\|.
\]
On the G1 endpoint-excluded corridor the normalized response coefficient has fixed bounds
\[
0<b_0\le b_{\rm amp}(t),\qquad A(t)\le A_{\max}<\infty,
\]
where
\[
b_{\rm amp}(t)=\frac{\sqrt{1-t^2}}2.
\]
The response intertwiner reflects the X spectrum exactly. By (1.1), localization to a cell \(I\) gives a response in the unique reflected cell \(-I\):
\[
z_{-I}^X\ge \sigma z_I^X-\xi_I^X,
\qquad \sigma=b_0/A_{\max}>0.
\tag{3.1}
\]
The analogous Bob inequality holds on U cells.

## 4. Explicit X/U bridge

After a same-marginal reflection, decompose the destination marginal vector into retained joint cells. If that marginal cell has retained bridge degree \(D_I\), one retained joint block has norm at least
\[
D_I^{-1/2}\bigl(z_{-I}^X-\sqrt{c_I}\bigr),
\]
where \(c_I\) is the joint mass deleted from that row. The same block lies in one actual U marginal cell, so
\[
\boxed{
z_{\rm next}^U
\ge
\frac{\sigma}{\sqrt{D_I}}z_I^X-e_I.
}
\tag{4.1}
\]
The U-to-X step is identical. No X spectral projection is substituted for a U projection inside a response intertwiner; the marginal switch occurs only through an actual joint state block.

## 5. Global ownership and branch geometry

Before the first repeated marginal parity cell, every X or U marginal cell is used at most once at its own parity. Orthogonality of response residual projections and one-time ownership of deleted joint mass give
\[
\boxed{
\sum_{\rm walk} e_I^2
\le C\bigl(\varepsilon+\beta_{\rm far}+\beta_{\rm end}\bigr).
}
\tag{5.1}
\]
Also
\[
L\le m_X+m_U\le2d.
\tag{5.2}
\]
The sum of bridge degrees is bounded by the row-plus-column degree sum of the retained raw-cell graph:
\[
\boxed{
\sum_{\rm walk}D_I\le2|E_{\rm cell}|\le8d.
}
\tag{5.3}
\]
Hence every deterministic prefix product is at least
\[
\boxed{
\Gamma_d:=2^{-4d}\min(1,\sigma)^{2d}=e^{-O(d)}.
}
\tag{5.4}
\]
