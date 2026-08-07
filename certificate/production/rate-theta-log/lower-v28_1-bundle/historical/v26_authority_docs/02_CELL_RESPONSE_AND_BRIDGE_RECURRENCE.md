# Cell Response and X/U Bridge Recurrence

## Reflection-symmetric grid

Put \(r=\varepsilon^{1/8}\), \(N=\lceil2/r\rceil\), and \(\eta=2/N\). Partition \([-1,1]\) into the \(N\) half-open intervals with endpoints \(-1+2j/N\). Reflection sends cell \(j\) exactly to cell \(N-1-j\). Moreover
\[
\frac{2}{3}r\le\eta\le r\qquad(0<r\le1).
\]

The existing far-inversion cover theorem gives
\[
\beta_{\rm far}\le 8\sqrt{\mathcal I}\,\eta^{-3},
\qquad \mathcal I\le4\varepsilon,
\]
so
\[
\boxed{\beta_{\rm far}\le54\varepsilon^{1/8}.}
\]

## Same-marginal response

Let \(z_I^X=\|E_I(X)\psi\|\). On the G1 endpoint-excluded corridor the normalized response coefficient has fixed bounds
\[
0<b_0\le b_{\rm amp}(t),\qquad A(t)\le A_{\max}<\infty,
\]
where
\[
b_{\rm amp}(t)=\frac{\sqrt{1-t^2}}2.
\]
The response intertwiner reflects the X spectrum exactly, so localization to cell \(I\) gives
\[
z_{-I}^X\ge \sigma z_I^X-\xi_I^X,
\qquad \sigma=b_0/A_{\max}>0.
\]
The analogous Bob inequality holds on U cells.

## Explicit X/U bridge

After a same-marginal reflection, decompose the destination marginal vector into retained joint cells. If that marginal cell has retained bridge degree \(D_I\), one retained joint block has norm at least
\[
D_I^{-1/2}\bigl(z_{-I}^X-\sqrt{c_I}\bigr),
\]
where \(c_I\) is the joint mass deleted from that row. The same block lies in one U marginal cell, so
\[
\boxed{
z_{\rm next}^U
\ge
\frac{\sigma}{\sqrt{D_I}}z_I^X-e_I.
}
\]
The U-to-X step is identical.

Before the first repeated marginal parity cell, every row/column is used at most once at its own parity. Therefore
\[
\sum e_I^2\le C(\varepsilon+\beta_{\rm far}+\beta_{\rm end}).
\]
Also
\[
L\le m_X+m_U\le2d,
\]
and the sum of bridge degrees is bounded by the sum of all row and column degrees:
\[
\boxed{\sum_{\rm walk}D_I\le2|E_{\rm cell}|\le8d.}
\]
Hence every deterministic prefix product is at least
\[
\boxed{\Gamma_d:=2^{-4d}\min(1,\sigma)^{2d}=e^{-O(d)}.}
\]
