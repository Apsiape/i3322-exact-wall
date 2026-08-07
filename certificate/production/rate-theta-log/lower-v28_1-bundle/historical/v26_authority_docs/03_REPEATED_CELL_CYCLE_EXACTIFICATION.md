# Repeated Cell-Cycle Exactification

## Cycle normalization

Let a repeated marginal parity cell form an even alternating cycle. For every X/U switch choose the actual retained joint bridge block used by the selected walk, and define
\[
m_C:=\min_{e\in C}\|Q_e\psi\|.
\]
This is the **minimum bridge-block amplitude**, not a scalar coordinate minimum.

Assume for contradiction a sequence with
\[
\frac{\mathcal E_n}{m_{C,n}^2}\to0,
\qquad
\mathcal E_n:=\varepsilon_n+\beta_{{\rm far},n}+\beta_{{\rm end},n}.
\]
Then \(\varepsilon_n\to0\) and the grid width \(\eta_n\to0\).

## Finite near-maximizer R0 localization

The generic weld at \(q>S\) gives
\[
qI-\mathcal B=R_{0,q}+R_{A,q}+R_{B,q},\qquad R_{\nu,q}\succeq0.
\]
For a strategy of value \(S-\varepsilon\),
\[
\langle R_{0,q}\rangle\le(q-S)+\varepsilon.
\]
G1 gives \(g_S\ge m_g>0\) and uniform \(g_q\to g_S\), hence uniform \(\phi_q\to\phi_S\). Sending \(q\downarrow S\),
\[
\boxed{\langle\psi,R_{0,S}\psi\rangle\le\varepsilon.}
\]
Since \(R_{0,S}=\phi_S(X,U)\) is joint functional calculus of the commuting pair, every joint spectral block \(Q_e\) commutes with \(R_{0,S}\), so
\[
\frac{\langle Q_e\psi,R_{0,S}Q_e\psi\rangle}{\|Q_e\psi\|^2}
\le\frac{\varepsilon}{m_C^2}\to0
\]
uniformly around the cycle.

Choose a sublevel threshold \(s_n\downarrow0\) with \(\varepsilon/(s_nm_C^2)\to0\). Trimming each bridge block to \(\{\phi_S\le s_n\}\) loses \(o(m_C)\) norm. Compactness of the strict zero graph \(Z=\phi_S^{-1}(0)\), plus \(\eta_n\to0\), makes every trimmed bridge block concentrate on a unique shrinking neighborhood of one point of \(Z\).

## Minimum-U order squeeze — no pointwise tau

Index one two-response step by a source U label \(u_k\). The Bob reflection and first bridge give an approximate zero pair
\[
(x_k,-u_k)\in Z+o(1),
\]
and the Alice reflection and second bridge give
\[
(-x_k,u_{k+1})\in Z+o(1).
\]
Equivalently, uniformly around the cycle,
\[
P(u_{k+1})+P(-u_k)=o(1).
\]
Choose \(u_j=\min_k u_k\). Since \(P\) is increasing,
\[
P(u_j)\le P(u_{j+1}),
\qquad
P(-u_{j-1})\le P(-u_j).
\]
Using the outgoing relation at \(j\) and incoming relation at \(j-1\) gives
\[
P(u_j)+P(-u_j)=o(1).
\]
After a subsequence \(u_j\to u_*\), closedness of \(Z\) gives
\[
\boxed{P(-u_*)=-P(u_*).}
\]
Therefore the reflected exact pairs
\[
(P(-u_*),-u_*),\qquad (-P(-u_*),u_*)
\]
form a common two-state return sector.

No finite-n evaluation of \(a=P^{-1}(-P(\cdot))\), no a.e. `Y_0`, and no total Borel \(\tau\) are used.
