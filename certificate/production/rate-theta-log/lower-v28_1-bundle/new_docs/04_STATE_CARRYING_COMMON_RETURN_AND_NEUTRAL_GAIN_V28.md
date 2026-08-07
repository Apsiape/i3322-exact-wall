# State-Carrying Common Return and Normalized Neutral Gain — v28

Let Doc 03 produce the exact zero pair
\[
z_+=(x_*,u_*)\in Z,
\qquad
z_-=(-x_*,-u_*)\in Z.
\tag{0.1}
\]

## 1. Normalized transports — the gains consumed by \(F(q)\)

On the reflection-symmetric G1 corridor \(K\),
\[
b_{\rm amp}(t)=\frac{\sqrt{1-t^2}}2\ge b_0>0.
\]
The raw response operators satisfy
\[
W^*W=b_{\rm amp}(X)^2,
\qquad
W_B^*W_B=b_{\rm amp}(U)^2
\]
(`SHIFTED_GRID_RESPONSE_INTERFACE_REPAIR_V22.md`, (4.2)). Because \(b_{\rm amp}\) is even and \(WX=-XW\), \(W\) commutes with \(b_{\rm amp}(X)\); similarly for Bob. Define on the corridor
\[
\boxed{
K_A:=W\,b_{\rm amp}(X)^{-1},
\qquad
K_B:=W_B\,b_{\rm amp}(U)^{-1}.
}
\tag{1.1}
\]
Then \(K_A^*K_A=K_B^*K_B=I\) on the relevant response subspaces. In the exact equality module, Theorem-(N) Round 3 item 9 further gives self-adjoint unitarity and
\[
\boxed{K_A^2=K_B^2=I.}
\tag{1.2}
\]

**Gain convention (pinned).** The symbols \(\alpha,\beta>0\) below are the **source-evaluated normalized multiplier gains**
\[
\boxed{\alpha:=r_{A,{\rm mult}}(x_*),\qquad \beta:=r_{B,{\rm mult}}(u_*).}
\tag{1.3}
\]
They are exactly the variables consumed by
\[
F(q)=\frac{(1+q)^2}{16q},
\qquad q=\alpha/\beta.
\tag{1.4}
\]
Because the normalized transports are involutive, \(r_{A,{\rm mult}}(t)r_{A,{\rm mult}}(-t)=r_{B,{\rm mult}}(t)r_{B,{\rm mult}}(-t)=1\). Therefore the **source-to-destination vector coefficient** seen after projecting to \(z_-\) is \(1/\alpha\) for Alice and \(1/\beta\) for Bob. This pins the previous \(\alpha\leftrightarrow1/\alpha\) ambiguity between §§2 and 5. Reversing the common-return orientation replaces \(q\) by \(1/q\), and the scalar ceiling is unchanged because \(F(q)=F(1/q)\).

The raw gains of \(W,W_B\) contain extra factors \(b_{\rm amp}(x_*),b_{\rm amp}(u_*)\). At normalized neutral gain the raw ratio can therefore be
\[
q_{\rm raw}=b_{\rm amp}(x_*)/b_{\rm amp}(u_*),
\]
which need not equal one. The quarter ceiling is **not** applied to raw gains.

## 2. Parallelism comes from the multiplier law, not isometry

At finite n, `SHIFTED_GRID_RESPONSE_INTERFACE_REPAIR_V22.md` (2.1)--(2.3) supplies the destination-localized response equation; after the m_C-rescaled residual tends to zero, its exact-limit form is the scalar multiplier law. The exact scalar-orbit multiplier receipt (`CURRENT_S_SPATIAL_ATTAINMENT_BY_SCALAR_ORBIT.md`) is
\[
K_A\psi=r_{A,{\rm mult}}(X)\psi,
\qquad
K_B\psi=r_{B,{\rm mult}}(U)\psi,
\tag{2.1}
\]
with positive scalar multipliers on the G1 corridor. Let \(E_{z_+},E_{z_-}\) denote the complete joint zero-fibre projections in the exact limit. Strict graph uniqueness identifies the whole \(X=x_*\) occupied component with \(z_+\) and the whole \(X=-x_*\) component with \(z_-\). Therefore
\[
\begin{aligned}
E_{z_-}K_AE_{z_+}\psi
&=E_{-x_*}^XK_AE_{x_*}^X\psi\\
&=E_{-x_*}^XK_A\psi\\
&=E_{-x_*}^Xr_{A,{\rm mult}}(X)\psi\\
&=r_{A,{\rm mult}}(-x_*)E_{z_-}\psi
=\frac1\alpha E_{z_-}\psi.
\end{aligned}
\tag{2.2}
\]
Likewise strict U-graph uniqueness and involutivity give
\[
\boxed{
E_{z_-}K_BE_{z_+}\psi
=r_{B,{\rm mult}}(-u_*)E_{z_-}\psi
=\frac1\beta E_{z_-}\psi.
}
\tag{2.3}
\]
Thus both response images are multiples of **one and the same destination vector**. Isometry alone would not imply this parallelism.

## 3. Why the naive ultraproduct is insufficient; the \(m_C\)-rescaled nonzero fibres

A naive ultraproduct of the unscaled states need not contain atoms at \(z_\pm\): the shrinking joint-cell masses may tend to zero. The contradiction normalization instead satisfies
\[
\mathcal E_n/m_{C,n}^2\to0,
\]
and every selected bridge has norm at least \(m_{C,n}\). Divide the two shrinking joint components by \(m_{C,n}\). Their norms are then nonzero, but could a priori be unbounded. The G1 multiplier functions are pinched between fixed positive finite constants, so the source and destination component norms satisfy
\[
n_{+,n}\asymp n_{-,n}
\tag{3.1}
\]
with constants independent of \(d,n\). Choose the second common normalization scale as \(n_{+,n}:=\max(1,\|\widetilde v_{+,n}\|)\), where \(\widetilde v_{+,n}\) is the source component after the \(m_C\)-rescaling. Thus \(n_{+,n}\ge1\) **by construction**; the fixed multiplier pinching in (3.1) keeps the destination component comparable. Divide both components by this same \(n_{+,n}\). The resulting two sequences are norm-bounded and both have nonzero ultraproduct limits
\[
\boxed{v_+\ne0,\qquad v_-\ne0.}
\tag{3.2}
\]

The live one-step residual **squared** budget is \(O(\mathcal E_n)\), not merely \(O(\varepsilon_n)\). Hence every localized residual divided by \(m_{C,n}\) tends to zero, and the second normalization cannot enlarge it because \(n_{+,n}\ge1\).

The marginal-to-joint collapse uses the exact Pythagorean identities from `SHIFTED_GRID_RESPONSE_INTERFACE_REPAIR_V22.md`, (5.1)--(5.3):
\[
(y_k^X)^2=w_k+r_k^{\rm del},
\qquad
(y_k^U)^2=w_k+c_k^{\rm del},
\]
\[
\sum r_k^{\rm del},\ \sum c_k^{\rm del}\le\beta_{\rm del},
\qquad
\sum|y_k^X-y_k^U|^2\le4\beta_{\rm del}.
\tag{3.3}
\]
Here \(\beta_{\rm del}:=\beta_{\rm far}+\beta_{\rm end}\le\mathcal E\), distinct from the normalized Bob gain \(\beta\). Since \(\beta_{\rm del}/m_C^2\to0\), both marginals collapse onto the same selected joint component after rescaling. In scalar coordinates, strict graph uniqueness gives both a modulus \(\omega_P\) and, because \(P\) is a strictly increasing homeomorphism between compact projections of \(Z\), a modulus
\[
\boxed{
\omega_{P^{-1}}(h)\to0.
}
\tag{3.4}
\]
These two moduli turn shrinking one-coordinate cells plus \(R_0\)-sublevel localization into shrinking **joint** neighborhoods of \(z_+\) and \(z_-\).

Passing the multiplier equations (2.2)--(2.3) through this normalized limit, with the source-evaluated convention (1.3), yields
\[
\boxed{
K_Av_+=\frac1\alpha v_-,
\qquad
K_Bv_+=\frac1\beta v_-,
\qquad
\alpha,\beta>0.
}
\tag{3.5}
\]

## 4. State-level neutral gain

Because the images in (3.5) are parallel to the same nonzero \(v_-\), and \(K_A,K_B\) are normalized isometries,
\[
\|v_+\|=\frac1\alpha\|v_-\|,
\qquad
\|v_+\|=\frac1\beta\|v_-\|.
\]
Thus
\[
\boxed{\alpha=\beta.}
\tag{4.1}
\]
This is the v22B repair. A scalar fixed return alone is insufficient; the conclusion uses the same nonzero source, the same nonzero destination, and the multiplier-law parallelism.

## 5. Involutivity and both exact component equations

By (1.2), the reverse normalized gains are \(1/\alpha\) and \(1/\beta\). The exact common-return equality module therefore supplies the two component equations consumed by `DISTORTED_RETURN_QUARTER_CEILING_CURRENT_V22.md`:
\[
\boxed{
Q
=
d(x_*,u_*)
+\alpha b_{\rm amp}(x_*)
+\beta b_{\rm amp}(u_*),
}
\tag{5.1}
\]
\[
\boxed{
Q
=
d(-x_*,-u_*)
+\frac{b_{\rm amp}(x_*)}{\alpha}
+\frac{b_{\rm amp}(u_*)}{\beta}.
}
\tag{5.2}
\]
Here \(Q=S\) follows directly from the zero-set receipt, not from an extra limiting-weld slogan. Since \(z_+\in Z=\phi_S^{-1}(0)\),
\[
0=\phi_S(z_+)
=S-\bigl[d(x_*,u_*)+\alpha b_{\rm amp}(x_*)+\beta b_{\rm amp}(u_*)\bigr],
\]
which is (5.1) with \(Q=S\). Since \(z_-\in Z\) and involutivity gives the reciprocal source multipliers on the reflected component,
\[
0=\phi_S(z_-)
=S-\left[d(-x_*,-u_*)+\frac{b_{\rm amp}(x_*)}{\alpha}+\frac{b_{\rm amp}(u_*)}{\beta}\right],
\]
which is (5.2) with the same left side. Therefore
\[
\boxed{Q=S.}
\tag{5.3}
\]

Only **after** (5.1)--(5.3) are established do we insert (4.1), giving normalized distortion \(q=1\). The exact scalar theorem then gives
\[
F(1)=\frac14,
\qquad
\boxed{S\le\frac14,}
\]
contradicting the certified \(S>1/4\).

## 6. Dimension-free repeat payment

Therefore no sequence with \(\mathcal E_n/m_{C,n}^2\to0\) exists. By contraposition, there is a fixed constant \(C_C<\infty\), independent of local dimension and cycle length, such that
\[
\boxed{m_C^2\le C_C\mathcal E.}
\tag{6.1}
\]

## 7. R1 and R2 scope

For an already-typed distorted finite common return, R1 separately gives
\[
(1-q)z\le e_{\rm ret}.
\]
It may service \(q<889/1000\), but is not used to derive (4.1). The historical robust packet-local Bell-localization receipt **R2 (formerly G2) remains OPEN and is not on the v28 critical path**; this is only a status-wording/alias change: the neutral contradiction is obtained only after exactification to (5.1)--(5.3).
