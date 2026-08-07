# State-Carrying Common Return and Neutral Gain

Let
\[
z_-=(x_*,-u_*),\qquad z_+=(-x_*,u_*),
\]
with both points in the strict full-zero graph as obtained by the repeated-cell exactification.

The trimmed bridge vectors at the minimum node and its adjacent bridge have norms \(\ge m_C-o(m_C)\). The live one-step response residuals have total squared norm \(O(\varepsilon)\), so after division by \(m_C\) they vanish. A Hilbert ultraproduct (or equivalent finite norm-equation compactness argument) therefore gives nonzero complete-fibre state components \(v_-\) and \(v_+\) satisfying the exact component response equations.

Bob sends \(z_+\) to \(z_-\). Alice sends \(z_-\) to \(z_+\), and its normalized scalar-reflection transport is involutive, so the inverse Alice edge sends \(z_+\) to \(z_-\). Thus the two exact transports share the **same nonzero source component** \(v_+\) and **same destination state component** \(v_-\):
\[
K_Av_+=\alpha v_-,\qquad K_Bv_+=\beta v_-.
\]
The normalized transports are isometric on the endpoint-free exact fibre, hence
\[
\|v_+\|=\alpha\|v_-\|=\beta\|v_-\|.
\]
Therefore
\[
\boxed{\alpha=\beta.}
\]
This is the repair of the v22B kill. A scalar fixed point alone does **not** imply neutral gain; the conclusion uses the state-carrying common source and destination.

The promoted multiplicity-uniform exact return algebra is fibre-dimension independent. At neutral gain its quarter ceiling gives
\[
S\le\frac14,
\]
contradicting the certified \(S>1/4\). Therefore the assumed sequence cannot exist, and compact contradiction yields a dimension-independent constant
\[
\boxed{m_C^2\le C_C\mathcal E.}
\]

## R1 distorted-return service

Separately, for a finite typed common return with \(q=\alpha/\beta\le1\), R1 gives
\[
(1-q)z\le e_{\rm ret}.
\]
Thus every \(q<889/1000\) return is directly serviced. R1 is live only in this scope and is not the source of \(\alpha=\beta\).
