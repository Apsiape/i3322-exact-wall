# Repeated Cell-Cycle Exactification — v28

This document restores the blind-verified v27 §2 localization paragraph verbatim from `historical/v27_authority_docs/03_REPEATED_CELL_CYCLE_EXACTIFICATION_V27.md`. The restored §2 byte-content (from its heading through the paragraph before §3) has SHA-256 `95b51d04aeaa15560e9b8b3fd8d8ded236ecedd8884ce65a3dd0105ff9ef7e91`. Retention rule from v28.1 onward: any preamble claim that content is “unchanged” must be backed by an explicit source hash or an explicit diff hunk.

## 1. Cycle normalization and evenness

A walk state is side-tagged as in Doc 02. The X/U bridge graph is bipartite:
\[
X_{\rm cells}\sqcup U_{\rm cells}.
\]
Every walk edge changes side, hence
\[
\boxed{\text{every closed walk cycle has even length}.}
\tag{1.1}
\]
For every X/U switch choose the actual retained joint bridge block used by the selected walk and put
\[
m_C:=\min_{e\in C}\|Q_e\psi\|.
\]
Assume the contradiction sequence
\[
\frac{\mathcal E_n}{m_{C,n}^2}\to0,
\qquad
\mathcal E_n=\varepsilon_n+\beta_{{\rm far},n}+\beta_{{\rm end},n}.
\tag{1.2}
\]

## 2. Finite near-maximizer R0 localization

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
\tag{2.1}
\]
Since
\[
R_{0,S}=\phi_S(X,U)
\]
is joint functional calculus of the commuting pair, every joint spectral bridge projection \(Q_e\) commutes with \(R_{0,S}\). Therefore
\[
\frac{\langle Q_e\psi,R_{0,S}Q_e\psi\rangle}{\|Q_e\psi\|^2}
\le
\frac{\varepsilon}{m_C^2}\to0
\tag{2.2}
\]
uniformly around the cycle.

Let \(Z=\phi_S^{-1}(0)\) inside the fixed G1 compact corridor. Define the sublevel localization modulus
\[
\Omega(s):=
\sup\{\operatorname{dist}(z,Z):z\text{ in the compact corridor},\ \phi_S(z)\le s\}.
\]
Compactness and continuity give
\[
\Omega(s)\downarrow0\quad(s\downarrow0).
\tag{2.3}
\]
Choose \(s_n\downarrow0\) with
\[
\frac{\varepsilon_n}{s_nm_{C,n}^2}\to0.
\tag{2.4}
\]
Trimming each selected bridge block to \(\{\phi_S\le s_n\}\) loses \(o(m_C)\) norm. Every surviving bridge cell is of diameter \(O(\eta_n)\), hence every point of its trimmed support lies within
\[
\delta_n:=C\bigl(\eta_n+\Omega(s_n)\bigr)\to0
\tag{2.5}
\]
of an actual point of \(Z\), uniformly around the cycle.

## 3. Four-line derivation of the two actual-\(Z\) relations

Fix the two-response-step convention **Bob first, then Alice**; starting on the other side is the same cycle after a cyclic relabeling. Choose actual zero projections
\[
(P(t_k),t_k)\in Z
\]
from the source bridge and
\[
(P(s_k),s_k)\in Z
\]
from the bridge after Bob reflection.

1. Bob reflects the U-coordinate of the source from \(t_k\) to \(-t_k\). Reflection-equivariant shrinking cells plus actual-\(Z\) projection therefore give
   \[
   \boxed{|s_k+t_k|\le\delta_n.}
   \tag{3.4}
   \]
2. The same bridge is the source for the Alice response, whose X-coordinate is \(P(s_k)\).
3. Alice reflects that X-coordinate to \(-P(s_k)\).
4. The next actual joint bridge projects to \((P(t_{k+1}),t_{k+1})\in Z\), hence shrinking cells give
   \[
   \boxed{|P(t_{k+1})+P(s_k)|\le\delta_n.}
   \tag{3.5}
   \]

Every occurrence of \(P\) in (3.4)--(3.5) is at an actual member of \(D=\operatorname{dom}P\).

## 4. Minimum-point actual-\(Z\) squeeze

Because \(Z\) is a compact one-to-one increasing graph, \(P\) is uniformly continuous on \(D\). Put
\[
\omega_P(h)=\sup\{|P(a)-P(b)|:a,b\in D,\ |a-b|\le h\}.
\]
Choose
\[
t_j=\min_k t_k.
\]
Then monotonicity and (3.5) give
\[
P(t_j)+P(s_j)\le\delta_n.
\tag{4.1}
\]
For the predecessor, \(t_{j-1}\ge t_j\) and (3.4) imply
\[
s_{j-1}\le s_j+2\delta_n.
\]
Thus
\[
P(s_{j-1})\le P(s_j)+\omega_P(2\delta_n),
\]
and (3.5) at \(j-1\) gives
\[
P(t_j)+P(s_j)\ge-\delta_n-\omega_P(2\delta_n).
\]
Therefore
\[
\boxed{
|P(t_j)+P(s_j)|\le\delta_n+\omega_P(2\delta_n),
\qquad
|s_j+t_j|\le\delta_n.
}
\tag{4.2}
\]
Passing to a subsequence gives
\[
\boxed{
s_*=-t_*,\qquad P(s_*)=-P(t_*).
}
\tag{4.3}
\]
Hence the exact zero points are
\[
z_+=(x_*,u_*):=(P(t_*),t_*),
\]
\[
z_-=(-x_*,-u_*):=(P(-t_*),-t_*).
\tag{4.4}
\]

No evaluation of the zero-graph map at an undeclared reflected finite label, no a.e. \(Y_0\), and no finite-n \(a\) or \(\tau\) occurs.
