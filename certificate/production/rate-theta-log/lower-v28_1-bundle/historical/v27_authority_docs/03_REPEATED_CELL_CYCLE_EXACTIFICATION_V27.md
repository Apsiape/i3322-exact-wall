# Repeated Cell-Cycle Exactification — v27

## 1. Cycle normalization

Let a repeated marginal parity cell form an even alternating cycle. For every X/U switch choose the actual retained joint bridge block used by the selected walk, and define
\[
m_C:=\min_{e\in C}\|Q_e\psi\|.
\]
This is the **minimum bridge-block amplitude**, not a scalar-coordinate minimum.

Assume for contradiction a sequence with
\[
\frac{\mathcal E_n}{m_{C,n}^2}\to0,
\qquad
\mathcal E_n:=\varepsilon_n+\beta_{{\rm far},n}+\beta_{{\rm end},n}.
\tag{1.1}
\]
Then \(\varepsilon_n\to0\), the reflection-equivariant cell width \(\eta_n\to0\), and every selected bridge block has nonzero norm at least \(m_{C,n}\).

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

## 3. Actual-Z projection variables

The strict full-zero relation is a one-to-one increasing graph
\[
Z=\{(P(t),t):t\in D\},
\tag{3.1}
\]
where \(D=\pi_U(Z)\) is compact. Since \(Z\) is compact and is the graph of a single-valued function, \(P:D\to\pi_X(Z)\) has closed graph on a compact domain and is therefore continuous; hence it is uniformly continuous. Let
\[
\omega_P(h):=
\sup\{|P(a)-P(b)|:a,b\in D,\ |a-b|\le h\},
\qquad \omega_P(h)\to0.
\tag{3.2}
\]

For each two-response step choose **actual zero-graph projections**
\[
(P(t_k),t_k)\in Z,
\qquad
(P(s_k),s_k)\in Z,
\tag{3.3}
\]
from the trimmed source bridge and the bridge after the first scalar reflection. Reflection-equivariance of the marginal cells and the second reflected bridge give, after increasing the constant in \(\delta_n\),
\[
\boxed{|s_k+t_k|\le\delta_n,}
\tag{3.4}
\]
\[
\boxed{|P(t_{k+1})+P(s_k)|\le\delta_n.}
\tag{3.5}
\]
Indices are cyclic. Every evaluation of \(P\) in (3.4)--(3.5) is therefore at an element of the actual domain \(D\).

## 4. Minimum-point actual-Z squeeze

Choose
\[
t_j=\min_k t_k.
\tag{4.1}
\]
Because \(P\) is increasing,
\[
P(t_j)\le P(t_{j+1}).
\]
Using (3.5) at \(k=j\),
\[
\boxed{P(t_j)+P(s_j)\le\delta_n.}
\tag{4.2}
\]

For the predecessor, \(t_{j-1}\ge t_j\). From (3.4),
\[
s_{j-1}\le -t_{j-1}+\delta_n
\le -t_j+\delta_n
\le s_j+2\delta_n.
\tag{4.3}
\]
If \(s_{j-1}\le s_j\), monotonicity gives \(P(s_{j-1})\le P(s_j)\). If \(s_{j-1}>s_j\), then (4.3) gives
\(|s_{j-1}-s_j|\le2\delta_n\), so uniform continuity gives
\[
P(s_{j-1})\le P(s_j)+\omega_P(2\delta_n).
\]
Thus in all cases
\[
P(s_{j-1})\le P(s_j)+\omega_P(2\delta_n).
\tag{4.4}
\]
Using (3.5) at \(k=j-1\),
\[
P(t_j)+P(s_{j-1})\ge-\delta_n,
\]
and hence
\[
\boxed{
P(t_j)+P(s_j)
\ge
-\delta_n-\omega_P(2\delta_n).
}
\tag{4.5}
\]
Combining (4.2) and (4.5),
\[
\boxed{
|P(t_j)+P(s_j)|
\le
\delta_n+\omega_P(2\delta_n).
}
\tag{4.6}
\]
Together with (3.4),
\[
|s_j+t_j|\le\delta_n.
\tag{4.7}
\]

Take a subsequence with
\[
t_j\to t_*,\qquad s_j\to s_*.
\]
Then (4.7) gives \(s_*=-t_*\). Since \((P(t_j),t_j)\) and \((P(s_j),s_j)\) lie in the closed set \(Z\), their limits also lie in \(Z\); (4.6) gives
\[
P(s_*)=-P(t_*).
\]
Therefore
\[
\boxed{
s_*=-t_*,
\qquad
P(-t_*)=-P(t_*).
}
\tag{4.8}
\]
The two exact zero points are
\[
z_+=(x_*,u_*):=(P(t_*),t_*),
\]
\[
z_-=(-x_*,-u_*):=(P(-t_*),-t_*).
\tag{4.9}
\]
Alice reflection of \(x_*\) and Bob reflection of \(u_*\) therefore have the same exact scalar destination \(z_-\).

## 5. Claim boundary

The proof uses only:

- actual projections onto the compact zero graph;
- reflection-equivariant shrinking spectral cells;
- monotonicity and closedness of the strict zero graph;
- uniform continuity of \(P\) on its compact actual domain.

It does **not** evaluate the zero-graph function on reflected finite labels outside its declared domain, does not invoke the a.e. `Y_0` construction, and does not require a total finite-n response map \(a\) or \(\tau\).
