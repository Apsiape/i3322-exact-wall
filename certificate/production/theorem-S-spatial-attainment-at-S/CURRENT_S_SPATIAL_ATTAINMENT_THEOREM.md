# Spatial Attainment at the Current I3322 Supremum by Scalar-Orbit Extraction

**Date:** 2026-08-05  
**Status:** **PROMOTION CANDIDATE — referee-signed conditional on the V1–V9
repairs executed in this package.**  
**Scope:** current certified supremum \(S\); no historical amplitude profile is
used.

---

## 0. Theorem

Let \(I\) be the I3322 Bell functional in the repository's Collins–Gisin
normalisation: classical bound \(0\), with the qubit and qutrit maximum exactly
\(1/4\). Let

\[
S:=\omega_{\mathrm{tensor}}(I3322)
  =\omega_{\mathrm{commuting}}(I3322)
  \in
  (0.2508753845015185,\;0.250875388108398].
\]

Then \(S\) is attained by a normal spatial strategy. There exist six
orthogonal projections—three on each of two copies of \(\ell^2(\mathbb Z)\)—
and a unit vector

\[
\psi_S\in\ell^2(\mathbb Z)\otimes\ell^2(\mathbb Z)
\]

such that

\[
\langle\psi_S,\mathcal B_{3322}\psi_S\rangle=S.
\]

Consequently, using promoted Theorem (N),

\[
\boxed{
C_{qs}(3,3;2,2)\setminus C_q(3,3;2,2)\ne\varnothing.
}
\]

The separation corollary depends on Theorem (N); spatial attainment alone gives
membership in \(C_{qs}\).

---

## 1. Certified inputs

Choose \(q_n\downarrow S\). Let \(g_n=g_{q_n}\) be the positive terminal-pivot
storages from Sprint 1295. From the promoted Theorem-(N) package, after passage
to a subsequence,

\[
g_n\longrightarrow g
\]

uniformly on \([-1,1]\), where:

- \(g\) is concave;
- \(g(x)>0\) for every \(x\in(-1,1)\);
- \(g\) is Bellman-feasible at \(S\);
- the exact endpoint \(R_0\)-gaps hold uniformly in \(n\);
- the full interior zero locus is a one-to-one strictly increasing relation.

Only the limiting-storage part of Receipt (i) is used. Its
finite-dimensional spectral cutoff is not used.

The historical Sprint-1195 fixed point, profile, \(\ell^2\) tail,
eigen-equation and amplitude-compatibility equation are explicitly not used.

---

## 2. A maximizing commuting state

Let \(\mathfrak A_{\mathrm c}\) be the universal commuting I3322
\(C^\ast\)-algebra and \(\mathcal B\) its Bell element.

The state space is weak-\(*\) compact, and evaluation at \(\mathcal B\) is
weak-\(*\) continuous. Hence there is a state \(\omega_\ast\) with

\[
\omega_\ast(\mathcal B)=S.
\]

Let

\[
(\pi,\mathcal H,\Omega)
\]

be its GNS triple.

Unlike Theorem (N), which assumes a finite maximizer for contradiction, this
proof begins with an actually existing commuting maximizer.

---

## 3. Scalar Fatou passage

Put

\[
X=A_1+A_2-I,\qquad U=B_1+B_2-I.
\]

The operators \(X,U\) commute. Let \(\mu\) be their joint spectral measure in
\(\Omega\).

For every \(n\), the generic weld gives

\[
q_nI-\mathcal B
=
R_{0,n}+R_{A,n}+R_{B,n},
\qquad
R_{\nu,n}\succeq0.
\]

Write

\[
R_{0,n}=\phi_n(X,U),
\qquad
\phi_n\ge0.
\]

Since \(\omega_\ast(\mathcal B)=S\),

\[
\sum_\nu
\langle\Omega,R_{\nu,n}\Omega\rangle
=
q_n-S
\longrightarrow0.
\]

In particular,

\[
\int\phi_n\,d\mu\longrightarrow0.
\]

On \((-1,1)^2\),

\[
\phi_n(x,u)\longrightarrow\phi(x,u),
\]

because \(g_n\to g\) uniformly and \(g\) is strictly positive in the interior.

Receipt (iii) gives a uniform positive lower bound for \(\phi_n\) on

\[
E_{\partial}
=
\{x=\pm1\}\cup\{u=\pm1\}.
\]

Therefore

\[
\mu(E_{\partial})=0.
\]

Fatou's lemma gives

\[
\int\phi\,d\mu
\le
\liminf_n\int\phi_n\,d\mu
=
0.
\]

Since \(\phi\ge0\),

\[
\boxed{
\phi=0\quad\mu\text{-almost everywhere}.
}
\]

Thus the maximizing scalar spectral measure is supported on the current
interior full-zero locus.

---

## 4. The correct operator limit: use \(W,W_B\), not global CS involutions

Define

\[
Y=A_2-A_1,\qquad V=B_2-B_1,
\]

\[
W=Y(B_3-I/2),
\qquad
W_B=(A_3-I/2)V.
\]

These bounded self-adjoint operators satisfy

\[
W^2=b(X)^2,
\qquad
WX=-XW,
\]

\[
W_B^2=b(U)^2,
\qquad
W_BU=-UW_B,
\]

where

\[
b(t)=\frac{\sqrt{1-t^2}}2.
\]

No globally defined self-adjoint unitary \(J_A\) or \(K_A\) is assumed. Such a
unitary need not exist when the \(X=\pm1\) commuting corners have unequal
multiplicity.

For each \(n\), put

\[
p_n(x)=\frac{b(x)^2}{g_n(x)},
\]

\[
A_n(x)=\sqrt{p_n(x)g_n(-x)},
\qquad
B_n(u)=\sqrt{g_n(u)p_n(-u)}.
\]

The exact weld remainders are

\[
R_{A,n}=A_n(X)-W,
\qquad
R_{B,n}=B_n(U)-W_B.
\]

### 4.1 Positivity without a CS decomposition

The product law

\[
A_n(x)A_n(-x)=b(x)^2
\]

holds identically. With

\[
T=A_n(X)-W,
\qquad
T'=A_n(-X)+W,
\]

the relations above give

\[
TT'=T'T=0,
\]

\[
T+T'=A_n(X)+A_n(-X)=:D\succeq0,
\]

and

\[
T^2=TD.
\]

Since \(T,D\) commute, the joint spectral relation is
\(t(t-d)=0\) with \(d\ge0\), so \(t\ge0\). Hence

\[
R_{A,n}\succeq0.
\]

The same proof gives \(R_{B,n}\succeq0\).

### 4.2 Uniform bounds and vector convergence

Bellman feasibility at the reflected target gives

\[
A_n(x)
\le
\frac{p_n(x)+g_n(-x)}2
\le
\frac{q_n-d(x,-x)}2.
\]

Thus \(A_n\), and therefore \(R_{A,n}\), are uniformly bounded. Likewise for
\(B_n,R_{B,n}\).

For every \(n\),

\[
A_n(\pm1)=B_n(\pm1)=0.
\]

The interior limit \(A\) may have a nonzero one-sided limit at an endpoint and
is generally discontinuous there. This is harmless because the endpoint
spectral sets are null.

Dominated convergence gives

\[
A_n(X)\Omega\longrightarrow A(X)\Omega,
\]

\[
B_n(U)\Omega\longrightarrow B(U)\Omega.
\]

For a positive operator \(R\),

\[
R^2\preceq\|R\|R.
\]

Therefore

\[
\|R_{A,n}\Omega\|^2
\le
\|R_{A,n}\|
\langle\Omega,R_{A,n}\Omega\rangle
\longrightarrow0,
\]

and similarly for \(R_{B,n}\).

Passing to the vector limit yields

\[
\boxed{
A(X)\Omega=W\Omega,
}
\]

\[
\boxed{
B(U)\Omega=W_B\Omega.
}
\]

No division by \(b(X)\) or \(b(U)\) occurs at the operator level.

---

## 5. Scalar Radon–Nikodym transport

Let \(\mu_X,\mu_U\) be the two spectral marginals.

For bounded Borel \(f\),

\[
\begin{aligned}
\langle W\Omega,f(X)W\Omega\rangle
&=
\langle\Omega,Wf(X)W\Omega\rangle\\
&=
\int b(x)^2f(-x)\,d\mu_X(x),
\end{aligned}
\]

while

\[
\langle A(X)\Omega,f(X)A(X)\Omega\rangle
=
\int A(x)^2f(x)\,d\mu_X(x).
\]

Since \(A(X)\Omega=W\Omega\), scalar division on compact subsets of
\((-1,1)\), followed by monotone convergence, gives

\[
\boxed{
d((-{\rm id})_\ast\mu_X)
=
r_A^2\,d\mu_X,
\qquad
r_A(x)=\frac{A(x)}{b(x)}.
}
\]

Similarly,

\[
\boxed{
d((-{\rm id})_\ast\mu_U)
=
r_B^2\,d\mu_U,
\qquad
r_B(u)=\frac{B(u)}{b(u)}.
}
\]

These identities hold almost everywhere on the endpoint-free support.

The exact product laws are

\[
r_A(t)r_A(-t)=1,
\]

\[
r_B(t)r_B(-t)=1,
\]

\[
r_A(t)r_B(t)=1.
\]

Hence both reflected measures are equivalent to the original measures on the
interior support.

---

## 6. Strict graph and the conull response action

The interior zero locus

\[
Z=\{(x,u)\in(-1,1)^2:\phi(x,u)=0\}
\]

is Borel and is the graph of a strictly increasing one-to-one Borel map

\[
P:Y\to P(Y),
\qquad
Z=\{(P(u),u):u\in Y\}.
\]

The dual-zero involution gives

\[
P(-P(u))=-u
\]

whenever the expressions are defined, and

\[
P(Y)=-Y.
\]

The naive formula

\[
a(u)=P^{-1}(-P(u))
\]

is not defined at every point of \(Y\): \(P(Y)=-Y\) does not imply
\(P(Y)=Y\).

The two Radon–Nikodym laws imply that the required reflected coordinates exist
almost everywhere. Remove the null exceptional domains and then intersect
their images and preimages under the countably many finite words in the
infinite-dihedral generators. This produces a Borel conull set

\[
Y_0\subseteq Y
\]

that is invariant under both response transformations and on which

\[
a(u)=P^{-1}(-P(u)),
\qquad
b(u)=-u
\]

are everywhere-defined decreasing Borel involutions.

Define

\[
\tau=a\circ b.
\]

Because \(a,b\) are decreasing,

\[
\boxed{
\tau\text{ is increasing}.
}
\]

An increasing injective map has no non-fixed periodic orbit.

All statements below are made on \(Y_0\), modulo the displayed null sets.

The scalar transport laws become

\[
\boxed{
\mu_U(aE)
=
\int_E r_A(P(u))^2\,d\mu_U(u),
}
\]

\[
\boxed{
\mu_U(bE)
=
\int_E r_B(u)^2\,d\mu_U(u).
}
\]

---

## 7. Fixed points may exist, but they carry no mass

Let

\[
F=\{u\in Y_0:\tau(u)=u\}.
\]

The set \(F\) is Borel and invariant under \(a,b\). Fixed points are not
claimed to be absent; they may be accumulation points of open response orbits.

On \(F\),

\[
a(u)=b(u)=-u.
\]

For every Borel \(E\subseteq F\), the two transport laws and \(aE=bE\) give

\[
\int_E r_A(P(u))^2\,d\mu_U(u)
=
\int_E r_B(u)^2\,d\mu_U(u).
\]

Thus

\[
r_A(P(u))=r_B(u)
\]

for \(\mu_U\)-almost every \(u\in F\).

Put

\[
x=P(u),
\qquad
\rho=r_A(x)=r_B(u).
\]

The fixed-point relation gives

\[
P(-u)=-x,
\]

so both \((x,u)\) and \((-x,-u)\) are full-zero pairs. Zero-set localization
gives

\[
g(-x)=\rho b(x),
\qquad
g(x)=\frac{b(x)}{\rho},
\]

\[
g(u)=\rho b(u),
\qquad
g(-u)=\frac{b(u)}{\rho}.
\]

The two Bellman equalities are therefore

\[
S-d(x,u)=\rho\bigl(b(x)+b(u)\bigr),
\]

\[
S-d(-x,-u)=\frac{b(x)+b(u)}{\rho}.
\]

The audited Sprint-1198 elimination then gives

\[
S\le\frac14,
\]

contradicting the certified inequality \(S>1/4\).

Hence

\[
\boxed{
\mu_U(F)=0.
}
\]

This nullity, not emptiness of \(F\), is the statement consumed below.

---

## 8. A Borel transversal for the open response orbits

On the conull set \(Y_0\setminus F\), put

\[
Y_+=\{u:\tau(u)>u\},
\qquad
Y_-=\{u:\tau(u)<u\}.
\]

Because \(\tau\) is increasing, these are invariant unions of orbits.

For \(u\in Y_+\), define

\[
\alpha(u)=\inf_{n\in\mathbb Z}\tau^n(u),
\qquad
\beta(u)=\sup_{n\in\mathbb Z}\tau^n(u).
\]

Choose the first rational \(q_k\) in a fixed enumeration of \(\mathbb Q\) with

\[
\alpha(u)<q_k<\beta(u).
\]

Call it \(q(u)\). It is Borel and constant on the orbit.

Then

\[
D_+
=
\{u\in Y_+:u\le q(u)<\tau(u)\}
\]

meets every increasing orbit exactly once.

Apply the same construction to \(\tau^{-1}\) on \(Y_-\). This gives a Borel
transversal for the \(\mathbb Z\)-action.

The reflection relation

\[
b\tau b=\tau^{-1}
\]

induces a Borel involution on this transversal. Choosing the lesser of its two
representatives gives a Borel transversal for the full infinite-dihedral
response relation.

Thus the response relation is smooth and has a standard Borel orbit quotient

\[
\pi:Y_0\setminus F\to T.
\]

---

## 9. Scalar disintegration and normalization

Disintegrate the scalar probability measure:

\[
\mu_U
=
\int_T\mu_t\,d\nu(t),
\]

where every \(\mu_t\) is a probability measure supported on one countable
response orbit.

Because \(\pi\circ b=\pi\), the measure \(b_\ast\mu_U\) disintegrates over the
same base \(\nu\) with conditional probabilities \(b_\ast\mu_t\).

The measure \(r_B^2\mu_U\) has fibre mass

\[
c_B(t)=\int r_B^2\,d\mu_t.
\]

Uniqueness of probability disintegration and the identity

\[
b_\ast\mu_U=r_B^2\mu_U
\]

force

\[
c_B(t)=1
\]

and

\[
\boxed{
b_\ast\mu_t=r_B^2\mu_t
}
\]

for \(\nu\)-almost every \(t\).

Likewise,

\[
\boxed{
a_\ast\mu_t=r_A(P(\cdot))^2\mu_t.
}
\]

Since each orbit is countable, every \(\mu_t\) is purely atomic. Because
\(\phi=0\) almost everywhere, for almost every \(t\) no atom of \(\mu_t\) lies
outside the full-zero locus.

The transport densities are positive and finite on \(Y_0\), so a positive atom
propagates to every point of its complete response orbit.

Choose one conditional orbit measure having all these properties.

---

## 10. Interleaving the characteristic labels and amplitudes

Choose \(u_0\) in the selected orbit and put

\[
u_n=\tau^n(u_0).
\]

The points \(u_n\) are distinct because \(\tau\) is increasing and
fixed-point-free on this orbit.

Define

\[
c_{2n}=u_n,
\]

\[
c_{2n+1}=-P(-u_n).
\]

The dual-zero involution gives

\[
P(c_{2n+1})=c_{2n}.
\]

Also,

\[
u_{n+1}
=
a(-u_n)
=
P^{-1}(-P(-u_n)),
\]

so

\[
P(c_{2n+2})=c_{2n+1}.
\]

Therefore

\[
\boxed{
P(c_{j+1})=c_j
\quad\text{for every }j.
}
\]

Every adjacent pair \((c_j,c_{j+1})\) is a full-zero source-target pair.

Define

\[
\widetilde\lambda_{2n}
=
\sqrt{\mu_t(\{u_n\})},
\]

\[
\widetilde\lambda_{2n+1}
=
\sqrt{\mu_t(\{-u_n\})}.
\]

The \(b\)-transport law gives

\[
\frac{\widetilde\lambda_{2n+1}}
     {\widetilde\lambda_{2n}}
=
r_B(c_{2n}).
\]

Since \(a(u_{n+1})=-u_n\), the \(a\)-transport law gives

\[
\frac{\widetilde\lambda_{2n+2}}
     {\widetilde\lambda_{2n+1}}
=
\frac1{r_A(c_{2n+1})}
=
r_B(c_{2n+1}).
\]

Thus

\[
\boxed{
\frac{\widetilde\lambda_{j+1}}
     {\widetilde\lambda_j}
=
r_B(c_j)
\quad\text{for every }j.
}
\]

The two \(\tau\)-orbits \(\{u_n\}\) and \(\{-u_n\}\) are either disjoint or
identical. Hence

\[
1
\le
\sum_j\widetilde\lambda_j^2
\le
2.
\]

Normalize:

\[
\lambda_j
=
\frac{\widetilde\lambda_j}
{\left(\sum_k\widetilde\lambda_k^2\right)^{1/2}}.
\]

Then

\[
\boxed{
\lambda\in\ell^2(\mathbb Z),
\qquad
\lambda_j>0,
\qquad
\|\lambda\|_2=1.
}
\]

This is where the historical global amplitude-compatibility equation
disappears: the amplitudes are read from an already existing probability
measure rather than constructed and then normalized.

---

## 11. Jacobi eigen-equation

Every even label is a full-zero target. Every odd label is also a full-zero
target by the dual-zero involution. Moreover,

\[
K(t):=\frac{g(t)g(-t)}{b(t)^2}
\]

is invariant under \(t\mapsto-t\). Hence

\[
K(c_j)=1
\]

for every label.

Zero-set localization gives

\[
B(c_j)=g(c_j),
\]

and therefore

\[
r_B(c_j)=\frac{g(c_j)}{b(c_j)}.
\]

Define the bounded Jacobi operator

\[
H_{jj}=d(c_{j-1},c_j),
\]

\[
H_{j-1,j}=H_{j,j-1}=b(c_{j-1}).
\]

This is the Sprint-1295 source-target placement convention after a global
index shift.

The amplitude ratios give

\[
\frac{\lambda_{j+1}}{\lambda_j}
=
\frac{g(c_j)}{b(c_j)},
\]

\[
\frac{\lambda_{j-1}}{\lambda_j}
=
\frac{b(c_{j-1})}{g(c_{j-1})}.
\]

Therefore

\[
\begin{aligned}
\frac{(H\lambda)_j}{\lambda_j}
&=
d(c_{j-1},c_j)
+
\frac{b(c_{j-1})^2}{g(c_{j-1})}
+
g(c_j)\\
&=
d(c_{j-1},c_j)
+
p(c_{j-1})
+
g(c_j)\\
&=S,
\end{aligned}
\]

using Bellman equality at the full-zero pair
\((c_{j-1},c_j)\).

Thus

\[
\boxed{
H\lambda=S\lambda.
}
\]

Every finite principal block of \(H\) is a Sprint-1295 word matrix. Hence

\[
H\preceq SI.
\]

The constructed \(\lambda\) is therefore a top eigenvector and no overshoot is
possible.

---

## 12. Normal spatial reconstruction

Use only Sprint 1206 §§2–4: the alternating rank-one projector blocks and the
**no-endpoint** block-to-Jacobi value identity. Sprint 1206 §1, its status line,
and the historical analytic attainment theorem are not cited or used.

Install the two alternating matchings on two copies of
\(\ell^2(\mathbb Z)\), with cosine labels \(c_j\), and define

\[
\psi_S
=
\sum_{j\in\mathbb Z}
\lambda_j e_j\otimes e_j.
\]

Since

\[
\sum_j\lambda_j^2=1,
\]

\(\psi_S\) is a unit vector.

The six measurement operators are bounded projections. The Bell expectation is
well-defined: diagonal sums are dominated by \(\sum_j\lambda_j^2\), and
nearest-neighbour sums converge absolutely by Cauchy–Schwarz.

The local no-endpoint identity gives

\[
\begin{aligned}
\langle\psi_S,\mathcal B_{3322}\psi_S\rangle
&=
\sum_jd(c_{j-1},c_j)\lambda_j^2\\
&\quad+
2\sum_jb(c_{j-1})\lambda_{j-1}\lambda_j\\
&=
\langle\lambda,H\lambda\rangle\\
&=S.
\end{aligned}
\]

Therefore \(S\) is normally spatially attained.

---

## 13. What changed relative to the decertified route

Sprint 1285 decertified the historical spatial-attainment route because a
constructed amplitude profile failed its global compatibility equation.

The present proof does not repair or solve that equation. It dissolves it.

The new proof derives independently:

- the bi-infinite scalar profile \(c_j\);
- the \(\ell^2\) amplitude vector \(\lambda_j\);
- the Jacobi eigen-equation \(H\lambda=S\lambda\).

All three are extracted from a maximizing commuting state and its conditional
scalar orbit measure. No historical profile, historical tail, or historical
normalization equation re-enters.

---

## 14. Exact dependency boundary

### Used from the current candidate

- weak-\(*\) commuting attainment;
- scalar Fatou passage;
- the \(W,W_B\) operator-limit repair;
- scalar Radon–Nikodym transport;
- conull invariant action \(Y_0\);
- fixed-set nullity;
- explicit Borel transversal;
- normalized scalar disintegration;
- interleaving;
- Jacobi recurrence;
- infinite no-endpoint spatial reconstruction.

### Used from the promoted Theorem-(N) package

- limiting storage, concavity, interior positivity and feasibility;
- exact endpoint gaps;
- reflection-gluing \(K\ge1\);
- zero-set localization;
- strict Monge;
- repaired open-interval plateau exclusions;
- strict full-zero graph;
- Sprint-1198 quarter algebra only for fixed-set nullity.

### Used from the repository

- Sprint 1197 Bell reparameterisation and weld formulas;
- Sprint 1287 generic weld;
- Sprint 1295 \(P=S\), near-critical storages and path convention;
- Sprint 1292 \(S>1/4\);
- Sprint 1294 upper window;
- Sprint 1206 **§§2–4 only**, specifically the no-endpoint local block identity;
- promoted Theorem (N), only for the \(C_{qs}\setminus C_q\) corollary.

### Explicitly not used

- Sprint-1195 fixed point, profile, tail or eigen-equation;
- Sprint-1206 §1 or its historical status line;
- the global amplitude-compatibility equation;
- any global CS involution \(K_A,K_B\);
- a square factorization of \(R_A,R_B\);
- a compact interior spectral carrier;
- direct-integral decomposition of the full GNS representation;
- operator-multiplicity classification;
- DOC-C shooting or heteroclinic artifacts;
- the conditional dimension-necessity campaign.

---

## 15. Artifact scope

The scripts in `artifacts/` are smoke tests and package-integrity controls.
They do not verify Fatou's lemma, Borel disintegration, the conull action or the
infinite theorem.

The mathematical promotion rests on the analytic proof and its independent
referee audit, not on PASS banners.
