# A rigorously characterized (I_{3322}) quantum wall and finite-dimensional nonattainment

**Seth Douglas**

[ORCID 0009-0007-4708-3252](https://orcid.org/0009-0007-4708-3252) ·
[apsiape@gmail.com](mailto:apsiape@gmail.com)

**Release candidate — theorem claims independently reconstructed; priority
language remains provisional until archival posting.**

## Abstract

We determine the supremum of the (I_{3322}) Bell functional in both the
tensor-product and commuting-operator models. The value is the rigorously
characterized domain-wall constant

\[
q_*=0.250875384513976536\ldots,
\qquad
q_*\in[0.250875384513976535514,0.250875384513976536486].
\]

The proof has two parts. A computer-assisted shooting argument produces a
positive Bellman fixed point and a sequence of finite tensor-product
strategies approaching (q_*). A representation-free operator certificate,
obtained by geometrically combining a Bellman inequality with its reflected
counterpart, gives the matching upper bound for commuting measurements.

We then classify equality in the certificate. On a finite joint spectrum, the
two local equality kernels induce decreasing bijections of the same finite
ordered support and must therefore coincide. Their amplitude compatibility
reduces every putative finite attaining component to a scalar expression
bounded by (1/4). Since (q_*>1/4), no finite-dimensional tensor-product or
commuting-operator strategy attains the supremum.

The decimal above is not asserted to have an elementary closed form. Its
meaning is the unique validated zero of an explicit domain-wall shooting
problem, enclosed by interval arithmetic.

## 1. The Bell functional

Let (A_1,A_2,A_3) and (B_1,B_2,B_3) be projections. In the commuting model
they act on one Hilbert space and satisfy

\[
[A_i,B_j]=0\qquad(1\le i,j\le3).
\]

The normalization used here is

\[
\begin{aligned}
\mathcal B_{3322}={}&-A_2-B_1-2B_2
 +A_1B_1+A_1B_2+A_2B_1+A_2B_2\\
&-A_1B_3+A_2B_3-A_3B_1+A_3B_2 .
\end{aligned} \tag{1.1}
\]

Its classical bound is (0). Qubit strategies attain (1/4). Pál and
Vértesi constructed growing finite-dimensional strategies approaching
approximately (0.250875384514) and conjectured that finite dimension is
insufficient to attain the true maximum.

Our projector convention agrees term-for-term with their best-response
recursion. In the standard Collins--Gisin table it is obtained by swapping the
first two settings on both sides. The exact affine conversion to the
dichotomic convention is recorded in `NORMALIZATION-CONCORDANCE.md`.

Write

\[
\omega_{\mathrm c}(\mathcal B_{3322})
=\sup_{\mathcal H,\psi,A_i,B_j}
\langle\psi,\mathcal B_{3322}\psi\rangle
\]

for the commuting-operator value. The tensor-product value
(omega_{\otimes}) is defined by requiring a spatial bipartite
representation.

### Main theorem

There is a rigorously characterized constant (q_*) with

\[
q_*\in
[0.250875384513976535514,0.250875384513976536486]
\tag{1.2}
\]

such that

\[
\boxed{
\omega_{\otimes}(\mathcal B_{3322})
=\omega_{\mathrm c}(\mathcal B_{3322})=q_* .}
\tag{1.3}
\]

No finite-dimensional tensor-product strategy and no finite-dimensional
commuting-operator strategy attains (q_*).

The NPA hierarchy and its recent ncKKT refinements provide increasingly sharp
numerical bounds for this problem. Very recent budgeted moment-selection work
still uses (I_{3322}) as a hard NPA benchmark rather than supplying an exact
theorem. Our proof instead extracts an exact operator certificate from the
limiting domain-wall recursion.

## 2. The certified Bellman datum

Define

\[
b(x)=\frac{\sqrt{1-x^2}}2,
\qquad
d(x,u)=xu+\frac{x-u}{2}-1.                     \tag{2.1}
\]

The computer-assisted part of the proof establishes the following datum.

### Certified Bellman proposition

There are a constant (q_*) satisfying (1.2), a positive continuous concave
function (F:[-1,1]\to(0,\infty)), and a strictly increasing predecessor map
(P:[-1,1]\to[-1,1]) such that, with

\[
p(x)=\frac{b(x)^2}{F(x)},                       \tag{2.2}
\]

one has

\[
p(x)+F(u)\le q_*-d(x,u)                         \tag{2.3}
\]

for every (x,u\in[-1,1]). For every (u), equality in (2.3) holds at the
unique point (x=P(u)). Finally, a sequence of finite-dimensional
tensor-product strategies has values converging to (q_*).

Equivalently, (F) is a fixed point of the min-plus Bellman operator

\[
(T_qF)(u)
=\min_{x\in[-1,1]}
\left(q+1-\frac x2-(x-\tfrac12)u
-\frac{1-x^2}{4F(x)}\right).                   \tag{2.4}
\]

The interval proof of this proposition is summarized in Section 7. Everything
from Section 3 onward is an analytic consequence of the proposition.

## 3. Geometric symmetrization

Apply (2.3) at ((x,u)) and at the reflected pair ((-u,-x)). Because

\[
d(-u,-x)=d(x,u),                                 \tag{3.1}
\]

we have

\[
\begin{aligned}
p(x)+F(u)&\le q_*-d(x,u),\\
F(-x)+p(-u)&\le q_*-d(x,u).
\end{aligned}                                    \tag{3.2}
\]

Define

\[
a(x)=\sqrt{p(x)F(-x)},
\qquad
c(u)=\sqrt{F(u)p(-u)}.                            \tag{3.3}
\]

Cauchy–Schwarz applied to the vectors

\[
(\sqrt{p(x)},\sqrt{F(u)}),
\qquad
(\sqrt{F(-x)},\sqrt{p(-u)})
\]

gives

\[
a(x)+c(u)\le q_*-d(x,u).                         \tag{3.4}
\]

Direct multiplication yields the two exact product laws

\[
a(x)a(-x)=b(x)^2,
\qquad
c(u)c(-u)=b(u)^2.                                \tag{3.5}
\]

These identities are the entire scalar input to the operator certificate.

## 4. A commuting-operator certificate

Set

\[
X=A_1+A_2-I,\quad Y=A_2-A_1,
\qquad
U=B_1+B_2-I,\quad V=B_2-B_1.                    \tag{4.1}
\]

The projection relations imply

\[
X^2+Y^2=I,\quad XY+YX=0,
\qquad
U^2+V^2=I,\quad UV+VU=0.                        \tag{4.2}
\]

A direct expansion of (1.1) gives

\[
\mathcal B_{3322}
=G(X,U)+Y(B_3-I/2)+(A_3-I/2)V,                  \tag{4.3}
\]

where

\[
G(X,U)=XU+X/2-U/2-I.                            \tag{4.4}
\]

Introduce

\[
\alpha(x)=\frac12-a(x),
\qquad
\beta(u)=q_*-\frac12-c(u).                      \tag{4.5}
\]

Since (X) and (U) commute, joint functional calculus applied to (3.4)
gives

\[
R_0:=\alpha(X)+\beta(U)-G(X,U)\ge0.             \tag{4.6}
\]

For the Alice response term, let (J_A) be the polar sign of (Y) on the
support of (I-X^2). Then

\[
Y=2b(X)J_A,
\qquad
J_Af(X)=f(-X)J_A.                               \tag{4.7}
\]

Put (S_B=2B_3-I) and (L_A=\sqrt{a(X)}). Cross-party commutation implies
([J_A,S_B]=0). The product law (3.5) gives

\[
L_AJ_AS_BL_A=b(X)J_AS_B=Y(B_3-I/2).             \tag{4.8}
\]

Consequently

\[
\begin{aligned}
R_A&:=\frac12I-\alpha(X)-Y(B_3-I/2)\\
&=L_A(I-J_AS_B)L_A\ge0.                         \tag{4.9}
\end{aligned}
\]

The operator (J_AS_B) is a self-adjoint contraction. Endpoint summands,
where (b(X)=Y=0), follow by continuity and leave only a nonnegative diagonal
term.

The identical argument with (S_A=2A_3-I) and the polar sign (J_B) of (V)
gives

\[
R_B:=(q_*-\tfrac12)I-\beta(U)-(A_3-I/2)V
=\sqrt{c(U)}(I-S_AJ_B)\sqrt{c(U)}\ge0.           \tag{4.10}
\]

Adding (4.6), (4.9), and (4.10), all potentials cancel:

\[
\boxed{q_*I-\mathcal B_{3322}=R_0+R_A+R_B\ge0.} \tag{4.11}
\]

This proves (omega_{\mathrm c}\le q_*). The sequence in the certified
Bellman proposition consists of tensor-product strategies, so
(omega_{\otimes}\ge q_*). Since
(omega_{\otimes}\le\omega_{\mathrm c}), equation (1.3) follows.

## 5. Equality kernels on finite support

Assume for contradiction that a finite-dimensional strategy attains (q_*),
and choose a unit attaining vector (psi). Positivity in (4.11) implies

\[
R_0\psi=R_A\psi=R_B\psi=0.                      \tag{5.1}
\]

The scalar value of (R_0) at a joint spectral pair ((x,u)) is

\[
q_*-d(x,u)-a(x)-c(u).                            \tag{5.2}
\]

Equality in (5.2) forces equality in both Bellman inequalities (3.2) and in
Cauchy–Schwarz. Therefore every occupied pair satisfies

\[
x=P(u),\qquad -u=P(-x).                          \tag{5.3}
\]

Let (Sigma) be the finite set of occupied (u)-coordinates. Strict
monotonicity makes (P) injective, so (u\in\Sigma) identifies the complete
pair ((P(u),u)).

On the occupied interior support define

\[
K_A=J_AS_B,\quad K_B=S_AJ_B,
\qquad
r_A(x)=\frac{a(x)}{b(x)},\quad
r_B(u)=\frac{c(u)}{b(u)}.                        \tag{5.4}
\]

The two local kernel equations become

\[
K_A\psi=r_A(X)\psi,
\qquad
K_B\psi=r_B(U)\psi.                             \tag{5.5}
\]

The first reverses (x), and uniqueness of the zero graph makes it act on
(Sigma) by

\[
\mathfrak a(u)=P^{-1}(-P(u)).                    \tag{5.6}
\]

The second reverses (u) directly:

\[
\mathfrak b(u)=-u.                               \tag{5.7}
\]

Both are decreasing bijections of the same finite ordered set. There is only
one such bijection: the (k)-th smallest element must map to the (k)-th
largest. Hence

\[
\mathfrak a=\mathfrak b.                         \tag{5.8}
\]

Every occupied ((x,u)) is therefore paired with ((-x,-u)).

## 6. Amplitude holonomy and the quarter ceiling

Let (psi_+) and (psi_-) be the nonzero spectral components at
((x,u)) and ((-x,-u)). Taking norms in (5.5), and using (3.5), gives one
ratio in two ways:

\[
\rho:=\frac{\|\psi_-\|}{\|\psi_+\|}
=\sqrt{\frac{F(-x)}{F(x)}}
=\sqrt{\frac{F(u)}{F(-u)}}.                     \tag{6.1}
\]

Equality in (3.2) and in Cauchy–Schwarz then forces

\[
F(x)=\frac{b_x}{\rho},\quad
F(-x)=\rho b_x,\quad
F(u)=\rho b_u,\quad
F(-u)=\frac{b_u}{\rho},                         \tag{6.2}
\]

where (b_x=b(x)), (b_u=b(u)). At the reflected components,

\[
\begin{aligned}
q_*-d(x,u)&=\rho(b_x+b_u),\\
q_*-d(-x,-u)&=(b_x+b_u)/\rho.
\end{aligned}                                    \tag{6.3}
\]

Subtracting gives

\[
x-u=(b_x+b_u)(\rho^{-1}-\rho).                  \tag{6.4}
\]

Eliminating (ho) between (6.3) and (6.4) yields

\[
q_*=xu-1+
\sqrt{(b_x+b_u)^2+\frac{(x-u)^2}{4}}.            \tag{6.5}
\]

Let (s_x=\sqrt{1-x^2}), (s_u=\sqrt{1-u^2}), and (t=1-xu\ge0). Then

\[
(b_x+b_u)^2+\frac{(x-u)^2}{4}
=\frac{1-xu+s_xs_u}{2}\le t,                    \tag{6.6}
\]

because

\[
(1-xu)^2-s_x^2s_u^2=(x-u)^2\ge0.                \tag{6.7}
\]

Thus

\[
q_*\le-t+\sqrt t\le\frac14,                     \tag{6.8}
\]

where the last inequality is

\[
\frac14-(-t+\sqrt t)=(\sqrt t-\tfrac12)^2.
\]

This contradicts (1.2), proving finite-dimensional nonattainment.

For finite-dimensional commuting representations there is also an independent
argument: finite commuting matrix algebras decompose into a finite direct sum
of spatial matrix blocks. The Bell value is a convex combination of block
values, so equality would force one finite tensor block to attain (q_*),
which the preceding argument forbids.

## 7. Computer-assisted certificate

Only the certified Bellman proposition is computer-assisted. Its proof uses
the exact characteristic shooting map obtained from Bellman equality and
stationarity. In coordinates ((z,x,r)), with

\[
\Delta=zx+\frac{z-x}{2}-1,
\]

the successor ratio is

\[
v=\frac{2\left(q-\Delta-\sqrt{1-z^2}/(2r)\right)}
{\sqrt{1-x^2}},                                  \tag{7.1}
\]

and the successor coordinate is the rational-radical expression determined
by stationarity. The selected orbit leaves a hyperbolic positive plateau,
meets a two-condition reflection section, and returns by reversing symmetry.

The validation stack contains:

1. a 400-bit Miranda/interval-degree enclosure of the shooting zero and
   (1.2);
2. an exact symbolic identity showing that the shooting map preserves the
   Bellman envelope one-form up to the positive multiplier (1/v^2);
3. 300-bit interval covers of the central invariant graph and both wings;
4. strict derivative signs on every graph tile, proving a single-valued
   strictly increasing predecessor map;
5. an interval exclusion of every inactive outer predecessor;
6. positivity of the complete Bellman function;
7. square-summable domain-wall tails and finite truncations converging to
   (q_*).

Every computer-assisted item in this list was also reconstructed through a
second implementation using `mpmath.iv` and locally implemented rectangular
complex intervals, with no imports from the Arb/FLINT production engine. Its
eight registered gates pass and its directed shooting interval overlaps the
production enclosure. Thus the certificate stack has both deterministic
production replay and method-independent interval reconstruction.

The exact recurrence, interval margins, tile counts, failed guards, and
independence contract are in `TECHNICAL-SUPPLEMENT.md`. The file-to-claim map,
commands, hashes, and machine-readable receipts are listed in
`CERTIFICATE-MAP.md` and `release/release-manifest.json`.

## 8. Scope

The result determines one Bell-functional supremum and proves its
finite-dimensional nonattainment in the tensor and commuting models. It does
not assert a closed form for (q_*), spatiality of all commuting correlations,
or experimental accessibility of the limiting value. It has no dependence on
the broader foundational interpretation of the repository. General
finite/infinite-dimensional separations are already known; the value here is
the exact resolution of the canonical three-setting binary functional. The
observed finite-carrier gaps are exponentially consistent with the plateau
multiplier, but no quantitative device-independent dimension bound is claimed.

**Computational disclosure.** Frontier language models were used extensively
for proof discovery, implementation, adversarial auditing, and editorial
assistance. The named author assumes responsibility for the release. Every
load-bearing computer-assisted claim is mapped to independently replayable
certificates.

**Artifacts.** The complete sources, frozen receipts, and independent
reconstruction are at
[github.com/Apsiape/i3322-exact-wall](https://github.com/Apsiape/i3322-exact-wall).

## References

1. D. Collins and N. Gisin, *A relevant two qubit Bell inequality inequivalent
   to the CHSH inequality*, J. Phys. A 37 (2004), 1775–1787,
   [arXiv:quant-ph/0306129](https://arxiv.org/abs/quant-ph/0306129).
2. K. F. Pál and T. Vértesi, *Maximal violation of the I3322 inequality using
   infinite dimensional quantum systems*, Phys. Rev. A 82 (2010), 022116,
   [arXiv:1006.3032](https://arxiv.org/abs/1006.3032).
3. M. Navascués, S. Pironio, and A. Acín, *A convergent hierarchy of
   semidefinite programs characterizing the set of quantum correlations*, New
   J. Phys. 10 (2008), 073013, [arXiv:0803.4290](https://arxiv.org/abs/0803.4290).
4. M. Araújo, I. Klep, A. J. P. Garner, T. Vértesi, and M. Navascués,
   *First-order optimality conditions for non-commutative optimization
   problems*, Found. Comput. Math. (2026),
   [doi:10.1007/s10208-026-09761-x](https://doi.org/10.1007/s10208-026-09761-x).
5. F. Flora, L. Matos, T. Kriváchy, A. Garriga, and A. Acín,
   *Moment Optimization in the Navascués–Pironio–Acín Hierarchy* (2026),
   [arXiv:2607.14755](https://arxiv.org/abs/2607.14755).
