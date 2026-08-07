# State-Carrying Common Return and Neutral Gain — v27

Let the corrected actual-Z squeeze produce
\[
z_+=(x_*,u_*)\in Z,
\qquad
z_-=(-x_*,-u_*)\in Z.
\tag{1.1}
\]
Both scalar reflections therefore carry the same source zero point to the same destination zero point.

## 1. Nonzero state-carrying fibres

The two selected bridge blocks adjacent to the minimum node have norm at least
\[
m_C-o(m_C).
\]
The live one-step response residuals have total squared norm \(O(\varepsilon)\); under the contradiction normalization
\[
\mathcal E/m_C^2\to0
\]
they vanish after division by \(m_C\).

The sublevel trimming from the corrected L3 proof loses only \(o(m_C)\) norm. Since the marginal cells shrink and the strict zero graph is single-valued in both coordinates, the source X- and U-marginal packet vectors concentrate on the same shrinking joint neighborhood of \(z_+\), and the two reflected destination packets concentrate on the same shrinking joint neighborhood of \(z_-\).

A Hilbert ultraproduct, or equivalently compactness of these normalized finite norm equations, therefore yields nonzero complete-fibre vectors
\[
v_+\ne0,
\qquad
v_-\ne0
\]
carried by the exact fibres over \(z_+\) and \(z_-\).

## 2. Same source and same destination

The exact equality-kernel response laws on the endpoint-free zero module are scalar functional-calculus transports between complete fibres. Thus the two normalized exact response transports satisfy
\[
\boxed{
K_Av_+=\alpha v_-,
\qquad
K_Bv_+=\beta v_-,
}
\tag{2.1}
\]
for positive scalars \(\alpha,\beta\). No rank-one fibre, invariant line, or simple spectrum is assumed.

The normalized transports are isometric/unitary on the relevant exact response subspaces. Taking norms in (2.1),
\[
\|v_+\|=\alpha\|v_-\|,
\qquad
\|v_+\|=\beta\|v_-\|.
\]
Since \(v_-\ne0\),
\[
\boxed{\alpha=\beta.}
\tag{2.2}
\]
This is the repair of the v22B kill. A scalar fixed return alone is insufficient; neutral gain follows from the **same nonzero state source, same state destination, and the two exact response equations**.

## 3. Quarter ceiling and compact contradiction

At neutral distortion \(q=\alpha/\beta=1\), the promoted multiplicity-uniform return algebra gives
\[
S\le\frac14,
\]
contradicting the certified
\[
S>\frac14.
\]
Therefore no sequence with \(\mathcal E/m_C^2\to0\) exists. By contraposition there is a constant \(C_C<\infty\), independent of local dimension and cycle length, such that
\[
\boxed{m_C^2\le C_C\mathcal E.}
\tag{3.1}
\]

## 4. R1 distorted-return service

Separately, for any already-typed finite common return with
\[
q=\alpha/\beta\le1,
\]
R1 gives
\[
(1-q)z\le e_{\rm ret}.
\]
Thus every \(q<889/1000\) return is directly serviced. R1 is live only in this distorted-return scope and is not used to obtain (2.2).
