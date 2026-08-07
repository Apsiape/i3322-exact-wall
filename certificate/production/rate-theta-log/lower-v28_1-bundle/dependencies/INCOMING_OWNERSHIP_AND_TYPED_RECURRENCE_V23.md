# Incoming Ownership and Typed Antitone-Walk Recurrence — v23

**Date:** 2026-08-06  
**Status:** exact Hilbert-space repair of the v22 incoming-edge error.  
**Supersedes:** the false implication “edge response norm \(\zeta_{v\to w}\) is already destination state amplitude \(z_w\).”

## 1. Current localized response identity

Write the Alice response residual

\[
r_A=A(X)\psi-W\psi,
\qquad
\|r_A\|^2\le C_A\varepsilon,
\]

and use the exact scalar reflection intertwiner

\[
P_J(X)W=WP_{-J}(X).
\]

Then for every destination packet \(J\),

\[
\boxed{
A(X)P_J\psi-WP_{-J}\psi=P_Jr_A.
}
\tag{1.1}
\]

This is the ownership identity. The response vector on the right side of an edge is compared with the **actual state vector in the destination packet**, not identified with it.

The Bob identity is identical with \(B(U),W_B\).

## 2. Incoming conversion lemma

Fix one retained Alice edge \(v\to w\). Let

\[
\zeta_{v\to w}:=\|P_{I_w}WP_{-I_w}\psi_v\|
\]

be its ideal response-component norm, and let

\[
z_w:=\|P_{I_w}\psi\|.
\]

On the retained coefficient corridor define the named finite constant

\[
\boxed{
A_{\max}:=\sup_{t\in K}|A(t)|<\infty.
}
\tag{2.1}
\]

Taking norms in (1.1) gives

\[
\zeta_{v\to w}
\le A_{\max}z_w+\|P_{I_w}r_A\|.
\]

Hence

\[
\boxed{
z_w
\ge
\frac{\zeta_{v\to w}-\|P_{I_w}r_A\|}{A_{\max}}.
}
\tag{2.2}
\]

This is the missing v18/v22 incoming-ownership conversion.

## 3. Outgoing response floor and effective gain

On a fixed endpoint-excluded corridor \(K\Subset(-1,1)\),

\[
b(t)=\frac{\sqrt{1-t^2}}2
\]

has the named positive floor

\[
\boxed{
b_0:=\inf_{t\in K}b(t)>0.}
\tag{3.1}
\]

Because \(W^*W=b(X)^2\), the full ideal response norm issued from a source packet of amplitude \(z_v\) is at least \(b_0z_v\). If the retained destination degree is \(D_v\), the largest orthogonal outgoing component obeys

\[
\zeta_{v\to w}
\ge \frac{b_0}{\sqrt{D_v}}z_v-e_v^{\rm out}.
\tag{3.2}
\]

Combining (2.2) and (3.2),

\[
\boxed{
z_w
\ge
\frac{\sigma}{\sqrt{D_v}}z_v-e_v,
\qquad
\sigma:=\frac{b_0}{A_{\max}}.
}
\tag{3.3}
\]

The old v22 value \(\sigma=b_0\) is retracted.

## 4. Residual ownership is \(\ell^2\)-cheap

Along a simple alternating walk, a retained block is used as a destination at most once per parity, hence at most twice. Therefore

\[
\sum_{\text{walk}}
\|P_{I_w}r_A\|^2
\le2\|r_A\|^2
\le2C_A\varepsilon,
\]

and similarly

\[
\sum_{\text{walk}}
\|P_{J_w}r_B\|^2
\le2C_B\varepsilon.
\]

After the once-global X/U bridge and top-\(d\) deletion are included,

\[
\boxed{
\sum_{\text{walk}}e_v^2
\le
C_{\rm walk}(\varepsilon+\beta_{\rm tot}).
}
\tag{4.1}
\]

No residual is charged once per branch depth; the incoming correction is globally square-summable.

## 5. Branch-product consequence

The v22 antitone edge theorem is retained. On at most \(d\) retained labels, the two response relations have total edge budget at most \(4d-2\), hence along any simple largest-component walk

\[
\prod_vD_v^{-1/2}\ge2^{-2d+1}.
\]

With (3.3), the deterministic response-gain part of a length-\(n\le2d\) walk is bounded below by

\[
\sigma^n2^{-2d+1}=e^{-O(d)}.
\]

Thus the P3 repair changes only the exponential constant.

## 6. Claim boundary

This theorem requires a fixed endpoint-excluded corridor to make \(b_0>0\). v23 does **not** obtain that corridor from the invalid v22 endpoint-strip claim. The uniform-corridor issue is listed separately as Gate G1.
