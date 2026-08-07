# Raw-Cell Parity Edge Budget

## Setup

Let the retained joint spectral support after far-inversion deletion be a bipartite graph
\[
E_{\rm cell}\subset X_{\rm cells}\times U_{\rm cells}.
\]
A joint cell is an edge. The scalar grid is indexed by integers. A **far inversion** is a pair of occupied cells \((p,q),(p',q')\) with opposite order and
\[
|p-p'|\ge2,\qquad |q-q'|\ge2.
\]
The weighted far-inversion cover removes at least one endpoint of every such pair.

## Theorem — four-parity monotone decomposition

Split rows and columns by index parity. For \(r,s\in\{0,1\}\), let \(E_{rs}\) be the edges with row parity \(r\) and column parity \(s\).

If two edges of one \(E_{rs}\) were inverted, their two row indices and two column indices would each differ by at least two. They would therefore form a far inversion, impossible after the cover deletion. Hence every \(E_{rs}\) is monotone.

A monotone bipartite support on \(m_r\) rows and \(n_s\) columns has at most
\[
m_r+n_s-1
\]
edges. Summing the four parity classes gives
\[
|E_{\rm cell}|\le 2m_X+2m_U-4\le2m_X+2m_U.
\]
For local dimension at most \(d\), a self-adjoint local scalar operator has at most \(d\) occupied spectral cells, so
\[
\boxed{|E_{\rm cell}|\le4d.}
\]

This theorem does not invoke component clustering, top-d component selection, or any rank-cost identity.
