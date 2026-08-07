# Raw-Cell Inversion Receipt and Parity Edge Budget — v28

## 1. Exact state-anchored inversion payment

On the critical weld write
\[
\phi_S(x,u)=R_{0,S}(x,u)=S-d(x,u)-A(x)-B(u),
\]
with
\[
d(x,u)=xu+\frac{x-u}{2}-1.
\]
Hence \(\phi_S\) has the **bilinear + separable** form
\[
\boxed{
\phi_S(x,u)=C-xu-F_X(x)-F_U(u)
}
\tag{1.1}
\]
for
\[
C=S+1,\qquad F_X(x)=\frac x2+A(x),\qquad F_U(u)=B(u)-\frac u2.
\]
The pointwise receipt for this form and for \(\phi_S\ge0\) at all four cross-points used below is `dependencies/CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md` §5. Thus no unnamed “state-anchored Monge theorem” is imported.

For any two spectral points \((x,u),(x',u')\), the cross-difference is exactly
\[
\phi_S(x,u)+\phi_S(x',u')-\phi_S(x,u')-\phi_S(x',u)
=-(x-x')(u-u').
\tag{1.2}
\]
Since \(\phi_S\ge0\),
\[
\big[(x-x')(u-u')\big]_{-}
\le \phi_S(x,u)+\phi_S(x',u').
\tag{1.3}
\]
Let \(\mu\) be the joint spectral probability measure of \((X,U)\) in \(\psi\), and define the ordered inversion energy
\[
\mathcal I
=
\iint
\big[(x-x')(u-u')\big]_{-}
\,d\mu(x,u)d\mu(x',u').
\]
Integrating (1.3) gives
\[
\boxed{
\mathcal I\le2\langle\psi,R_{0,S}\psi\rangle\le2\varepsilon.
}
\tag{1.4}
\]
The last inequality is the finite near-maximizer \(R_{0,S}\) receipt from Doc 03/06.

## 2. Far-inversion cover

Use the reflection-equivariant odd partition from Doc 02, of common geometric width \(\eta\). If two retained joint cells have index gaps
\[
|p-p'|\ge2,\qquad |q-q'|\ge2,
\]
and opposite order, then every spectral pair across those cells is an inversion and, by the strict grid-transfer lemma below,
\[
|x-x'|>\eta,\qquad |u-u'|>\eta.
\]
Thus each such cell pair is paid by more than \(\eta^2m_vm_w\). The existing weighted vertex-cover lemma therefore gives
\[
\boxed{
\beta_{\rm far}\le8\sqrt{\mathcal I}\,\eta^{-3}.
}
\tag{2.1}
\]
With (1.4), \(r=\varepsilon^{1/8}\), and the v28 odd partition satisfying \(r/2<\eta\le r\), this is in particular
\[
\boxed{
\beta_{\rm far}<128\,\varepsilon^{1/8}.
}
\tag{2.2}
\]
The constant is deliberately conservative.

## 3. Strict grid-transfer lemma for the mixed-closure partition

Let \(I_p,I_{p'}\) be two v28 cells with \(p<p'\) and \(p'-p\ge2\). Their geometric endpoints are separated by at least one full cell width. For gaps \(p'-p\ge3\), strictness is immediate: the geometric separation exceeds one full cell width before endpoint ownership is considered. The only closure-sensitive case is the nearest gap \(p'=p+2\). Equality \(|x'-x|=\eta\) there would require **simultaneously**

- the right endpoint of the lower-index cell \(I_p\) to belong to \(I_p\), and
- the left endpoint of the higher-index cell \(I_{p+2}\) to belong to \(I_{p+2}\).

The mixed convention forbids that simultaneous ownership. On the left half, cells are \([a_j,a_{j+1})\), so the **right** endpoint of the lower cell is excluded. On the right half, cells are \((a_j,a_{j+1}]\), so the **left** endpoint of the higher cell is excluded. In the cases meeting or crossing the closed central cell, at least one of those two facing endpoints is still excluded. Therefore
\[
\boxed{
|p-p'|\ge2\quad\Longrightarrow\quad |x-x'|>\eta.
}
\tag{3.1}
\]
The same statement holds on the \(U\) axis. `guard_grid_transfer_strict.py` attacks boundary atoms explicitly.

## 4. Four-parity monotone decomposition

After far-inversion deletion let
\[
E_{\rm cell}\subset X_{\rm cells}\times U_{\rm cells}
\]
be the retained raw joint support. Split edges by row parity and column parity. Within any nonempty parity class, an inversion would have both index gaps at least two and hence would be a deleted far inversion. Every nonempty parity subgraph is therefore monotone.

Let \(k_{\rm par}\in\{1,2,3,4\}\) be the number of nonempty parity subgraphs when \(E_{\rm cell}\ne\varnothing\). Summing the monotone edge bounds gives the corrected display
\[
\boxed{
|E_{\rm cell}|
\le
2m_X+2m_U-k_{\rm par}
\le
4d-1.
}
\tag{4.1}
\]
If the graph is empty, the bound is trivial. The older unconditional display \(2m_X+2m_U-4\) is false for, e.g., a \(1\times1\) graph and is retired.

The only dimension input is
\[
m_X\le d,\qquad m_U\le d,
\tag{4.2}
\]
because \(X\) and \(U\) act on the original \(d\)-dimensional local factors. No component clustering or component rank-cost identity is used.
