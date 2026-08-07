# Projected Return Mismatch R1 — v23

**Date:** 2026-08-06  
**Status:** exact operator lemma plus current packet-typing assembly.  
**Purpose:** restore the load-bearing R1 receipt discarded by v22B, with the **same distortion variable** \(q\) used by the exact \(F(q)\) theorem.

## 1. The two parallel return transports

At a rounded common-return packet, the two response laws provide two normalized scalar-reflection transports from the same source packet toward the same reflected destination packet. Let

\[
K_A,\ K_B
\]

be the normalized response intertwiners on the endpoint-excluded source corridor. Before packet compression they are isometric/unitary on the relevant scalar-reflection subspaces, so for a source packet vector \(v\),

\[
\|K_Av\|=\|K_Bv\|=\|v\|.
\tag{1.1}
\]

Let \(w\) be the repeated/reflected destination packet vector. The destination-localized response identities and the once-global X/U bridge give positive gains \(\alpha,\beta\) and error vectors \(r_A^{\rm ret},r_B^{\rm ret}\) such that, after all deleted-destination leakage is included in the errors,

\[
K_Av=\alpha w+r_A^{\rm ret},
\qquad
K_Bv=\beta w+r_B^{\rm ret}.
\tag{1.2}
\]

This is the current projected-block version of the two multiplicity-uniform return channels. It does **not** assert pointwise multiplier equality.

Orient the return so

\[
\boxed{
q:=\frac\alpha\beta\in(0,1].
}
\tag{1.3}
\]

This is exactly the distortion variable in

\[
F(q)=\frac{(1+q)^2}{16q}.
\]

## 2. R1 from reverse triangle

Subtract \(q\) times the second identity in (1.2) from the first. Since \(\alpha-q\beta=0\),

\[
K_Av-qK_Bv=r_A^{\rm ret}-q r_B^{\rm ret}.
\tag{2.1}
\]

On the other hand, by (1.1),

\[
\begin{aligned}
\|K_Av-qK_Bv\|
&\ge
\bigl|\|K_Av\|-q\|K_Bv\|\bigr|\\
&=(1-q)\|v\|.
\end{aligned}
\]

Therefore, with

\[
z:=\|v\|,
\qquad
e_{\rm ret}:=\|r_A^{\rm ret}-q r_B^{\rm ret}\|,
\]

we obtain

\[
\boxed{
(1-q)z\le e_{\rm ret}.
}
\tag{2.2}
\]

Equivalently, putting \(T=K_A^*K_B\) gives \(\|T\|=1\) on the full normalized response subspace and

\[
\|(I-qT)v\|=e_{\rm ret},
\]

so (2.2) is the standard contraction-return inequality.

## 3. Current ownership of the error

**v28 classification:** this section retains the historical TOP_D deletion as **R1-only optional provenance**. The main v28 neutral-return route does not consume TOP_D. If R1 is invoked as an early distorted-return service, this historical provenance is included and indexed accordingly.

The identities in (1.2) are not obtained by declaring a reflected source norm to be destination mass. They use the v23 incoming conversion

\[
z_w\ge
\frac{\zeta_{v\to w}-\|P_wr\|}{A_{\max}},
\]

and the once-global paired-block bridge. Hence every term in \(r_A^{\rm ret},r_B^{\rm ret}\) is one of:

1. a projected response residual;
2. a destination block removed by the top-\(d\) selection;
3. the once-global X/U paired-block mismatch.

In the historical v23 construction, along a simple walk through at most \(d\) TOP_D-selected labels, orthogonality gives

\[
\boxed{
e_{\rm ret}^2\le C_{R1}(\varepsilon+\beta_{\rm tot})}
\tag{3.1}
\]

up to the already explicit exponential comparison factor when everything is normalized to one marked walk amplitude.

## 4. Why the v22 null-set problem is absent

No pointwise identity

\[
r_{A,{\rm mult}}(P(u))=r_{B,{\rm mult}}(u)
\]

on the spatial fixed set is used. The spatial theorem proves such an identity only \(\mu\)-a.e. on a fixed set subsequently shown null; v23 consumes none of it.

Instead, \(q\) is the ratio of the **two actual projected response gains** \(\alpha,\beta\) on a finite-dimensional rounded return packet, and R1 compares the two normalized transport vectors directly.

## 5. Cycle split

If

\[
q<q_0:=\frac{889}{1000},
\]

then (2.2) yields

\[
\boxed{
z^2\le\frac{e_{\rm ret}^2}{(1-q_0)^2}.}
\tag{5.1}
\]

If \(q\ge q_0\), the exact scalar ceiling supplies the rational gap

\[
\Delta_{\rm ret}
=S_- -F(q_0)
=
\frac{16308643699893}{1778000000000000000}>0,
\]

**provided** the separate robust Bell-localization receipt R2 is available.

## 6. Claim boundary

**Closed here:** the current operator provenance of R1 and its identification with the exact \(F(q)\) distortion variable.

**Still open:** R2, namely the rank-independent robust passage from the two rounded packet response equations to a localized Bell deficit controlled by \(F(q)\).
