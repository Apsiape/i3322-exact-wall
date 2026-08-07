# Shifted-Grid Response Interface Repair — v22

**Date:** 2026-08-06  
**Status:** exact Hilbert-space assembly from ordered paired blocks, current response residuals, v20 X/U bridge, and endpoint service.  
**Purpose:** discharge SG2 without a C034/current-S rigidity rebind.

---

## 1. Inherited ordered paired blocks

Let the shifted-grid clustering produce paired coefficient-matrix blocks

\[
D_k=F_kME_k^{\mathsf T}
\]

with mutually orthogonal left and right supports and

\[
r_k=\operatorname{rank}D_k\ge1,
\qquad
\sum_kr_k\le d.
\tag{1.1}
\]

The retained X-side and U-side scalar supports are strictly ordered. The deleted
matrix is

\[
R=M-\sum_kD_k,
\qquad
\beta=\|R\|_F^2.
\tag{1.2}
\]

The shifted-grid estimate gives

\[
\boxed{\beta\le C\varepsilon^{1/8}}
\tag{1.3}
\]

after the state-chosen grid scale is fixed. The exponent is not claimed sharp.

`SG1_ANTITONE_SUPPORT_REDERIVATION_V22.md` proves independently that the two
ideal response supports on these same block labels are exact antitone relations.

---

## 2. The correct localized response identity

For the Alice response, write the current full-state residual as

\[
r_A=A(X)\psi-W\psi,
\qquad
\|r_A\|^2\le C_A\varepsilon,
\tag{2.1}
\]

with the exact intertwiner

\[
P_J(X)W=WP_{-J}(X).
\tag{2.2}
\]

For every destination X-packet projection \(P_J(X)\),

\[
\boxed{
A(X)P_J(X)\psi
-
W P_{-J}(X)\psi
=
P_J(X)r_A.
}
\tag{2.3}
\]

Thus a response component landing in a destination packet is compared with the
**actual state vector in that destination packet**. The same statement holds on
the U side for

\[
r_B=B(U)\psi-W_B\psi,
\qquad
P_J(U)W_B=W_BP_{-J}(U).
\tag{2.4}
\]

This destination-localized form is the ownership statement used below.

---

## 3. Deleted destinations cost only `epsilon + beta`

Fix one parity and one retained source block. Decompose its ideal response vector
orthogonally over retained and deleted destination block projections.

If destination block \(j\) is deleted, (2.3) gives

\[
\|P_jW\psi\|
\le
\|A(X)P_j\psi\|+\|P_jr_A\|.
\]

The coefficient \(A\) is bounded on `[-1,1]` in the current positive-remainder
construction, so summing deleted destinations and using orthogonality gives

\[
\sum_{j\in\mathrm{deleted}}\|P_jW\psi\|^2
\le
C\beta+C\varepsilon.
\tag{3.1}
\]

The same estimate holds for Bob. Consequently, after discarding deleted
destinations, the ideal response vectors lose total squared norm only

\[
\boxed{O(\varepsilon+\beta).}
\tag{3.2}
\]

No assertion that `W` preserves the clustering deletion subspace is made or
needed.

---

## 4. Outgoing edge-component inequality

Let \(z_k\) be the source marginal amplitude of one retained block in the active
scalar family. On a fixed endpoint-excluded corridor,

\[
b(t)=\frac{\sqrt{1-t^2}}2
\]

has a positive lower bound

\[
b(t)\ge b_0>0.
\tag{4.1}
\]

Because

\[
W^*W=b(X)^2,
\qquad
W_B^*W_B=b(U)^2,
\tag{4.2}
\]

the full ideal response vector issued from the source block has norm at least

\[
b_0z_k.
\]

Project it onto the retained destination blocks. By (3.2), there are orthogonal
edge-component norms \(\zeta_{k\to j}\) satisfying

\[
\boxed{
\left(\sum_{j:k\to j}\zeta_{k\to j}^2\right)^{1/2}
\ge b_0z_k-e_k,
}
\tag{4.3}
\]

with

\[
\boxed{
\sum_ke_k^2\le C(\varepsilon+\beta).
}
\tag{4.4}
\]

Thus the branch-selection theorem may take the uniform response floor

\[
\sigma=b_0.
\]

This coefficient is current and geometric; no historical scalar carrier profile
is used.

---

## 5. Correct X/U bridge on one paired block

For a retained paired block put

\[
w_k=\|D_k\|_F^2.
\]

The original X-side and U-side marginal packet masses decompose as

\[
(y_k^X)^2=w_k+r_k^{\rm del},
\qquad
(y_k^U)^2=w_k+c_k^{\rm del},
\tag{5.1}
\]

because the matched block and the deleted row/column parts have orthogonal
opposite-side supports. Moreover

\[
\sum_kr_k^{\rm del}\le\beta,
\qquad
\sum_kc_k^{\rm del}\le\beta.
\tag{5.2}
\]

Therefore

\[
|y_k^X-y_k^U|
\le
\sqrt{r_k^{\rm del}}+\sqrt{c_k^{\rm del}},
\]

and

\[
\boxed{
\sum_k|y_k^X-y_k^U|^2\le4\beta.
}
\tag{5.3}
\]

This is precisely the v20 bridge. It switches marginal families through the
paired coefficient block; it does **not** replace an X spectral projection by a
U spectral projection inside a response intertwiner.

Combining (4.4) and (5.3), the alternating block-graph error budget is

\[
\boxed{
\sum_{k,p}e_{k,p}^2
\le C(\varepsilon+\beta)
\le C'\varepsilon^{1/8}
}
\tag{5.4}
\]

for \(0<\varepsilon\le1\).

---

## 6. Endpoint strips and graph-sink service

Choose fixed scalar endpoint strips. The promoted current endpoint `R0` gaps pay
all state mass in those strips by

\[
\mu(\text{endpoint strips})\le C_{\rm end}\varepsilon.
\tag{6.1}
\]

After that paid deletion, (4.1) holds uniformly.

Now let a retained parity-state have no outgoing retained edge. Its full ideal
response norm is at least \(b_0z_k\), but every ideal destination component is
either deleted or response-error-owned. By (3.2),

\[
 b_0z_k
\le
 e_k^{\rm resp}+e_k^{\rm del}.
\]

Squaring and summing over graph sinks gives

\[
\boxed{
\sum_{k\in\mathrm{sinks}}z_k^2
\le
C_{\rm sink}(\varepsilon+\beta)
\le
C'_{\rm sink}\varepsilon^{1/8}.
}
\tag{6.2}
\]

Thus a sink created by retained projection is serviced just as a physical
endpoint is.

---

## 7. SG2 verdict

The old SG2 qualifier is discharged at the strength required by v22:

\[
\boxed{
\text{same rank-costed block graph}
+\text{orthogonal outgoing response components}
+\sum e^2=O(\varepsilon^{1/8})
+\text{sink service}.
}
\]

No C034/current-S rigidity rebind is required. The only price is the already
paid shifted-grid deletion \(\beta=O(\varepsilon^{1/8})\), which preserves an
exponential-in-dimension converse after inversion.
