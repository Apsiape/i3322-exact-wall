# U2 — Expanded write-up of certificate §§6–9

**STATUS.** U2 EXPANSION DRAFT v0.2 — discharges the certificate's disclosed
sections-6-9 residual risk; gated blind before any public amendment; the
certificate text remains authoritative until then.

**Round-1 gate result and repair record.** v0.1 was submitted to a two-surface
blind gate on 2026-08-07 (frozen commit c628e20e). The two verdicts are
`VERDICT-U2-AUDITOR-1-PROOF.md` (proof surface: **DENIED on source fidelity**;
blockers B1–B4, findings M1–M3, m4–m8; *no mathematical obstruction found*) and
`VERDICT-U2-AUDITOR-2-ADVERSARY.md` (countermodel surface: **NO COUNTEREXAMPLE
FOUND** in twenty-two attacks; defects S1, S2; wording repairs R1–R12). This
v0.2 executes **every** item of both verdicts:

- **B1 / R6 / attack-14** — the operative full-locus anchor is re-pointed to
  `CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` (boxed
  theorem at CEPE:224): §0.0 file table, OX.1 rows A6/A6′, OX.4 inventory,
  SCOPE FLAG 6.1.A (the false "CZS:124–125 are theorems" deleted), and finding
  F1 (downgraded to *resolved by a boxed theorem*; recommended public action
  corrected).
- **B2 / S2 / R2** — the CERT:417 quantifier upgrade is re-derived from the
  pre-division identity CERT:376–390 (§6, "The two transport laws"); OX.1 gains
  rows A13′ (CERT:376–390) and A15′ (CERT:433); A14/A15 descriptions corrected.
- **S1 / R1** — the generic weld \(\mathcal B=d(X,U)+W+W_B\) is now **displayed
  and anchored** inside Claim 0.1; OX.1 gains row A7′; OX.4's two false
  completeness sentences are corrected; F4 updated.
- **B3 / M3 / R3** — the false parenthetical after Claim 6.3.3 is deleted, the
  \(D_{\mathbf a}\)-conullity argument is restated using only (\(\Rightarrow\)),
  Claim 6.3.2's genuine consumers are named (L7.5/L7.6 \(\rho\), L9.5(2),
  L7.7's single-conull-set count), and OX.3/OX.4 accounting is corrected.
- **B4 / m4** — full line-number sweep against the live files (CERT 66→69,
  68→70, 69→71, 71→72 and every derived range; CZS 35→34; A25's display and
  justification ranges; the CERT:526 attribution → CERT:522–528).
- **m5–m8, R4, R5, R7, R9–R12** — I9 remark corrected (the product laws are
  identities on \((-1,1)\); the "\(K=1\)" clause deleted); L9.1(5) finiteness
  hypothesis added; L6.5's input header corrected; two typographic defects
  fixed; the \(q(u)\)-on-orbit note and the load-bearing non-strict \(\le\)
  stated at L8.3/L8.4; L7.5's receipt corrected (needed only at \((x,u)\); the
  false "p-halves genuinely new" parenthetical deleted); L9.1's small-orbit
  duplicate-representative sentence added; CORRECTION 0.A and F3 extended with
  the \(Y\), \(q\), \(\pi\) collisions and U2's own \(q\) reuse renamed to
  \(\theta\); g-continuity re-anchored; OX.2's case-(a) note and OX.3's
  \(\delta_t\)-absorption row corrected.
- **Positive receipts** from the adversary (the \(r_B(0)=1\) consistency check
  and the \(+8.75\times10^{-4}\) elimination margin) are recorded in the
  findings register under **Gate receipts**.

**Date:** 2026-08-07 (v0.1), 2026-08-07 (v0.2 repair round).
**Adjudicating track.**
**Target:** `CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md` §§6–9 (conull invariant
set, Borel transversal, uniqueness of disintegration), the sections carrying
the residual proof risk disclosed in that document's header (CERT:9–11).
**Commission:** `U2-OBLIGATIONS-AND-COMMISSION.md`, obligations O6.1–O9.6 and
OX.1–OX.4. Every obligation O*k.j* is discharged as Lemma *k.j* below, or is
flagged in a marked **GAP** / **SCOPE FLAG** / **CORRECTION** block.

---

## 0. Standing conventions, symbol hygiene, and two preliminary claims

### 0.0 File anchors used throughout

| tag | file |
|---|---|
| **CERT** | `C:\Infanox\i3322-exact-wall\certificate\production\theorem-S-spatial-attainment-at-S\CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md` |
| **CZS** | `C:\Infanox\i3322-exact-wall\certificate\production\theorem-N-four-receipts-at-S\CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md` |
| **CEPE** | `C:\Infanox\i3322-exact-wall\certificate\production\theorem-N-four-receipts-at-S\CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` |
| **FR** | `C:\Infanox\i3322-exact-wall\certificate\production\theorem-N-four-receipts-at-S\FOUR_RECEIPTS_AT_S_ASSEMBLY.md` |
| **QC** | `C:\Infanox\i3322-exact-wall\lean\I3322Kernel\I3322Kernel\QuarterCeiling.lean` |
| **MAN** | `C:\Infanox\i3322-exact-wall\paper\MANUSCRIPT.md` (LaTeX twin: `paper\manuscript.tex`) |

**CEPE was added in v0.2** (B1/R6): it is the document that actually *proves*
the full-interior-locus graph property, and v0.1 never cited it. **MAN was
added in v0.2** (S1/R1; round-2 F-1: an earlier exclusivity claim here was false in the conservative direction and is retracted — a second, machine-verified display in bipartite tensor form is certificate/production/foundational-sprint-1197/EXACT-I3322-QUANTUM-SUPREMUM.md:38-47, verified per its lines 49-50, exactly the source CERT:1078 names): it is a place in the public repository where
the generic weld consumed by Claim 0.1 is displayed as an identity.

Citations are `TAG:line` or `TAG:line–line`, referring to the files as they
stood on 2026-08-07.

### 0.1 CORRECTION 0.A — five symbol collisions in the certificate

**(A) The letter \(b\).** CERT uses the single letter \(b\) for **two different
objects**:

- the *amplitude function* \(b(t)=\tfrac{\sqrt{1-t^2}}{2}\) (CERT:229), which
  appears in \(W^2=b(X)^2\), in \(p=b^2/g\), in \(r_A=A/b\), \(r_B=B/b\), and
  in the Jacobi off-diagonal \(H_{j-1,j}=b(c_{j-1})\) (CERT:920);
- the *response involution* \(b(u)=-u\) (CERT:489), one of the two generators
  of the infinite-dihedral group.

These occur in the *same displayed formulas* — e.g. the boxed display at
**CERT:522–528** reads \(\mu_U(bE)=\int_E r_B(u)^2\,d\mu_U(u)\) (the integrand
itself is on CERT:526), where the outer \(b\) is the involution and the \(b\)
hidden inside \(r_B=B/b\) is the amplitude. This is a live legibility hazard for
exactly the a.e.-versus-pointwise reader this document is written for.

**Convention adopted here (and recommended for the public amendment):**

- \(b(t)=\tfrac{\sqrt{1-t^{2}}}{2}\) — amplitude, lower-case italic, always
  written with an argument;
- \(\mathbf a,\mathbf b\) — the two response involutions, bold;
  \(\mathbf b(u)=-u\), \(\mathbf a=P^{-1}\circ(-\mathrm{id})\circ P\);
- \(\tau=\mathbf a\circ\mathbf b\);
- \(G:=\langle \mathbf a,\mathbf b\mid \mathbf a^{2}=\mathbf b^{2}=1\rangle
  \cong D_\infty\), the *response group*.

**(B) The letters \(A,B\).** CERT uses \(A(x),B(u)\) for the transport factors
while the O7.6 commission text writes \(A:=S-xu+1\) and \(B:=b(x)+b(u)\). To
avoid a second collision, Lemma 7.6 writes \(\Sigma:=S-xu+1\) and
\(\Lambda:=b(x)+b(u)\); the dictionary to the commission's letters is stated
there.

**Three further live collisions, added in v0.2 (R9).** The round-1 adversary's
source-collation attack found three more, all live in CERT:

**(C) The letter \(Y\) — the most serious.** CERT:203 defines the *operator*
\(Y=A_2-A_1\) (one of the two anticommuting partners used to build \(W\)),
while CERT:449 defines \(Y\) as the *subset of \((-1,1)\)* that is the domain of
\(P\) (`P:Y\to P(Y)`). **The whole of §6 — and the whole of this document — is
built on the second \(Y\).** No display mixes them, but they are two paragraphs
apart in the same theorem and a referee reading §6 cold has no warning.
*Convention here:* \(Y\), \(Y_0\), \(Y_1\), \(Y_\pm\) are always subsets of
\((-1,1)\); the operator \(A_2-A_1\) is written out in full whenever it occurs
(only in Claim 0.1's weld display).

**(D) The letter \(q\).** CERT:59 uses \(q_n\downarrow S\) for the approximating
Bellman levels; CERT:644 uses \(q_k\) for a fixed enumeration of \(\mathbb Q\)
and CERT:650 writes \(q(u)\) for the selected rational. **v0.1 of this document
reproduced the collision** (Claim 0.1's \(q_n\to S\) against Lemma 8.2's
\(q(u)\)). *Convention adopted in v0.2:* \(q_n\) is reserved for the Bellman
levels, and the rational enumeration of Lemmas 8.2–8.4 is renamed
\(\theta_1,\theta_2,\dots\) with selected value \(\theta(u)\). The dictionary to
CERT is: \(\theta_k=\) CERT's \(q_k\) (CERT:644), \(\theta(u)=\) CERT's \(q(u)\)
(CERT:650).

**(E) The letter \(\pi\).** CERT:98 uses \(\pi\) for the GNS representation;
CERT:678 uses \(\pi\) for the orbit quotient \(Y_0\setminus F\to T\). This
document adds \(\pi_x,\pi_u\) (coordinate projections, L6.1(4)) and
\(\pi_{\mathbb Z}\) (the \(\mathbb Z\)-transversal retraction, L8.4). *Convention
here:* the GNS representation is never referred to after §0.2 — every \(\pi\)
below is a projection or a transversal retraction, distinguished by subscript,
with the unsubscripted \(\pi\) reserved for the orbit quotient of Lemma 8.6.

### 0.2 The objects, fixed once

From CERT §§1–5 and CZS:

\[
d(i,j)=ij+\frac{i-j}{2}-1 \qquad \text{(CZS:34)},
\]

\[
b(t)=\frac{\sqrt{1-t^{2}}}{2}\quad\text{(CERT:229)},\qquad
p(x)=\frac{b(x)^{2}}{g(x)}\quad\text{(CZS:49)},
\]

\[
A(x)=\sqrt{p(x)g(-x)},\qquad
B(u)=\sqrt{g(u)p(-u)}=A(-u)\qquad\text{(CZS:87)},
\]

\[
h(x,u)=S-d(x,u),\qquad R_0(x,u)=h(x,u)-A(x)-B(u)\qquad\text{(CZS:91)},
\]

\[
K(t)=\frac{g(t)g(-t)}{b(t)^{2}}\qquad\text{(CZS:79)},
\]

\[
r_A(x)=\frac{A(x)}{b(x)}\ \text{(CERT:401)},\qquad
r_B(u)=\frac{B(u)}{b(u)}\ \text{(CERT:413)}.
\]

\(\mu\) is the joint spectral measure of \((X,U)\) in the GNS vector \(\Omega\)
(CERT:112–117), a Borel **probability** measure on \([-1,1]^2\); \(\mu_X,\mu_U\)
are its marginals (CERT:370). \(g\) is the uniform interior limit of the
Sprint-1295 storages (CERT:64), **continuous and concave** (FR:49: "where `g`
is continuous and concave"; concavity also boxed at CZS:41 and listed at
CERT:69), and **strictly positive on \((-1,1)\)** (CERT:70, FR:63).

### Claim 0.1 (the certificate's \(\phi\) is CZS's \(R_0\))

\[
\phi=R_0 \quad\text{pointwise on }(-1,1)^2 .
\]

**The scalarisation input, supplied in v0.2 (S1/R1).** The step from the
operator weld to a scalar formula for \(\phi_n\) consumes one operator identity
that CERT **names but never displays** (CERT:1078–1079 lists "Sprint 1197 Bell
reparameterisation and weld formulas; Sprint 1287 generic weld" as repository
inputs). It is displayed in the public repository at **MAN:498–507**, quoted
verbatim:

> \[
> \mathcal B_{3322}
> =G(X,U)+Y(B_3-I/2)+(A_3-I/2)V,                  \tag{4.3}
> \]
>
> where
>
> \[
> G(X,U)=XU+X/2-U/2-I.                            \tag{4.4}
> \]

With \(X=A_1+A_2-I\), \(Y=A_2-A_1\), \(U=B_1+B_2-I\), \(V=B_2-B_1\) (MAN:483–485
= CERT:113, CERT:203) and \(W=Y(B_3-I/2)\), \(W_B=(A_3-I/2)V\) (CERT:207–209),
and since \(d(x,u)=xu+\tfrac{x-u}{2}-1\) (CZS:34) gives
\(G(X,U)=d(X,U)\) by the joint functional calculus of the commuting pair
\((X,U)\), this is exactly the **generic weld**

\[
\boxed{\ \mathcal B=d(X,U)+W+W_B\ }
\tag{0.1.W}
\]

*(The LaTeX twin of the same display is `paper\manuscript.tex:436` —
"`\B=G(X,U)+Y(B_3-\id/2)+(A_3-\id/2)V, \label{eq:reparam}`". The S1 referee
independently replicated it from the Collins–Gisin coefficient list:
SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md:284, "**Sprint-1197
reparameterisation** `𝓑 = XU + X/2 − U/2 − I + Y(B_3−I/2) + (A_3−I/2)V`", with
"the 1197 value equals the Collins–Gisin value exactly" at :286. **v0.1 used
(0.1.W) silently; the adversary was right that this was the one place a GAP
block was owed. It is now an anchored input, row A7′ of OX.1.**)*

*Proof.* CERT:132 defines \(\phi_n\) by \(R_{0,n}=\phi_n(X,U)\), and the
generic weld (CERT:122–126) sets
\(R_{0,n}=q_nI-\mathcal B-R_{A,n}-R_{B,n}\) with
\(R_{A,n}=A_n(X)-W\), \(R_{B,n}=B_n(U)-W_B\) (CERT:251–253). Substituting
(0.1.W), the two response blocks cancel **exactly**:
\[
R_{0,n}=q_nI-\bigl(d(X,U)+W+W_B\bigr)-\bigl(A_n(X)-W\bigr)-\bigl(B_n(U)-W_B\bigr)
=q_nI-d(X,U)-A_n(X)-B_n(U),
\]
so at the scalar level \(\phi_n(x,u)=q_n-d(x,u)-A_n(x)-B_n(u)\). Fix
\((x,u)\in(-1,1)^2\). Then \(q_n\to S\) (CERT:59, CERT:143), and
\(g_n\to g\) uniformly (CERT:64) with \(g>0\) on \((-1,1)\) (CERT:70), so
\(p_n(x)=b(x)^2/g_n(x)\to p(x)\) and hence
\(A_n(x)=\sqrt{p_n(x)g_n(-x)}\to\sqrt{p(x)g(-x)}=A(x)\), likewise
\(B_n(u)\to B(u)\). Therefore
\(\phi_n(x,u)\to S-d(x,u)-A(x)-B(u)=R_0(x,u)\). CERT:156 names this limit
\(\phi\). \(\square\)

Consequently the CERT §6 zero locus
\(Z=\{(x,u)\in(-1,1)^2:\phi(x,u)=0\}\) (CERT:443) is exactly
\(R_0^{-1}(0)\cap(-1,1)^2\), and the CZS results about \(R_0^{-1}(0)\) apply to
it verbatim. **This identification is load-bearing for O6.2 and O7.5** and is
not displayed in CERT; it is supplied here.

### Claim 0.2 (\(\mu\) is carried by \(Z\), and \(\mu_X=P_*\mu_U\) once \(P\) exists)

\[
\mu(Z)=1 .
\]

*Proof.* CERT:171–173 gives \(\mu(E_\partial)=0\) with
\(E_\partial=\{x=\pm1\}\cup\{u=\pm1\}\), so \(\mu((-1,1)^2)=1\). CERT:186–191
gives \(\phi=0\) \(\mu\)-a.e. Hence
\(\mu\bigl((-1,1)^2\setminus Z\bigr)=0\), i.e. \(\mu(Z)=1\). \(\square\)

The second half of Claim 0.2 is stated and proved as Claim 6.3.1, after \(P\)
is available.

### 0.3 Quantifier vocabulary

Every lemma header carries exactly one of:

- **[pointwise on \(Y_0\)]** (or on \(Y\), or on \((-1,1)\)) — the statement
  holds at *every* point of the named set, no exceptional set;
- **[\(\mu_U\)-a.e.]** — holds off a \(\mu_U\)-null Borel set, *named in the
  proof*;
- **[\(\nu\)-a.e. \(t\)]** — holds off a \(\nu\)-null Borel subset of \(T\).

Where a lemma has both a pointwise core and an a.e. envelope, both labels are
given and the boundary between them is stated in the proof. The OX.3 audit
table re-collects all of these.

---

# §6 — Strict graph and the conull response action

## Lemma 6.1 (O6.1) — \(Z\) is Borel and is the graph of a strictly increasing one-to-one Borel map \(P\)

**[inputs: CERT:73; CEPE:177–225 — the boxed full-locus graph theorem at
CEPE:224, THE OPERATIVE ANCHOR (v0.2); CZS:115–126 (strict Monge only);
CZS:86–91; FR:49; CERT:69, CERT:70; Claim 0.1]**
**[quantifier: pointwise on \((-1,1)^2\) / pointwise on \(Y\)]**

**Statement.** Let \(Z=R_0^{-1}(0)\cap(-1,1)^2\) and
\(Y:=\{u\in(-1,1):\exists x\in(-1,1),\ (x,u)\in Z\}\). Then:

1. \(Z\) is closed in \((-1,1)^2\), hence Borel;
2. for every \(u\in Y\) there is exactly one \(x\) with \((x,u)\in Z\); write
   \(P(u):=x\);
3. \(P:Y\to P(Y)\) is a bijection and is strictly increasing:
   \(u_1<u_2 \Rightarrow P(u_1)<P(u_2)\) for \(u_1,u_2\in Y\);
4. \(Y\) and \(P(Y)\) are Borel subsets of \((-1,1)\) and \(P\), \(P^{-1}\)
   are Borel;
5. \(Z=\{(P(u),u):u\in Y\}\) (CERT:451).

**Proof.**

*(1).* \(g\) is continuous on \((-1,1)\) and \(g>0\) there (CERT:70). **[v0.2,
R10: the continuity anchor is corrected.** v0.1 wrote "uniform limit of the
continuous \(g_n\), CERT:64"; CERT:64 asserts only \(g_n\to g\) and says nothing
about the \(g_n\). The correct anchors are **FR:49** — "where `g` is continuous
and concave" — or, independently, concavity (CZS:41 boxed, CERT:69) plus the
standard fact that a finite concave function on an open interval is continuous
there. Either suffices; nothing else in the proof changes.**]** Hence
\(p=b^2/g\) is continuous on \((-1,1)\), and so are
\(A(x)=\sqrt{p(x)g(-x)}\) and \(B(u)=\sqrt{g(u)p(-u)}\) (composition of
continuous functions with \(\sqrt{\cdot}\) on \([0,\infty)\); the radicands are
\(>0\) on \((-1,1)\)). \(d\) is a polynomial. Therefore
\(R_0=S-d-A-B\) is continuous on \((-1,1)^2\), and \(Z=R_0^{-1}(\{0\})\) is
relatively closed, hence Borel.

*(2)–(3).* **[v0.2, B1/R6: the operative anchor is CEPE, not CZS §6.]** The
full-locus statement is a **boxed theorem** of the Theorem-(N) package,
`CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` (status line
CEPE:4: "**PROMOTED after round-3 repair W1–W4**"), whose domain is fixed at
CEPE:15 as

> \[
> g(x)>0\qquad(x\in D:=(-1,1)).
> \]

— i.e. \(D\) **is** the open interval \((-1,1)\), so \(D^2=(-1,1)^2\) and the
theorem below is a statement about the *full* interior locus, with no occupancy
hypothesis anywhere in the document. The three ingredients, quoted verbatim:

*Horizontal exclusion* — CEPE §7 "Binding to the full zero locus — W1 repair"
(CEPE:177–194), which is where the *full source domain* enters:

> If `(x,u) in R_0^{-1}(0)`, zero-set localization gives the first Bellman
> equality as an equality:
>
> \[
> g(u)=C(x)+\left(\frac12-x\right)u.
> \]
>
> Feasibility gives the corresponding inequality for **every** `y in D`. Thus
> `x` is active for the full source domain `D`, not for a restricted interval,
> and
>
> \[
> u=H'(x).
> \]
>
> Consequently one source cannot serve two distinct full-zero targets.
> [CEPE:179–194]

*Vertical exclusion* — CEPE §8 "Dual tie and vertical exclusion"
(CEPE:196–210):

> The definitional identity `B(u)=A(-u)` and polynomial identity
> `d(-u,-x)=d(x,u)` give
>
> \[
> \boxed{R_0(-u,-x)=R_0(x,u).}
> \]
>
> If two distinct sources shared one full-zero target, reflection would produce
> one source with two distinct full-zero targets, contradicting Section 7.
> [CEPE:198–206]

*Assembly* — CEPE §9 "Strict graph and completion" (CEPE:212–225):

> Strict Monge gives
>
> \[
> (x_1-x_2)(u_1-u_2)\ge0
> \]
>
> for full-zero pairs. Horizontal and vertical equality are excluded unless the
> pairs coincide. Therefore
>
> \[
> \boxed{R_0^{-1}(0)\cap D^2\text{ is a one-to-one strictly increasing
> relation}.}
> \]
> [CEPE:214–225, box at CEPE:224]

The strict-Monge inequality itself is proved at **CZS:115–122** ("For two
full-zero pairs `(x_1,u_1)` and `(x_2,u_2)`, own equalities and cross Bellman
inequalities imply \((x_1-x_2)(u_1-u_2)\ge0\)"), and CZS:124–126 are the
one-line *pointer* sentences that hand the two exclusions to CEPE §§7–8; see
SCOPE FLAG 6.1.A. Reading off the three consequences separately, which is what
"a one-to-one strictly increasing relation" means:

- *Single-valuedness.* If \((x_1,u)\) and \((x_2,u)\in Z\) with \(x_1\ne x_2\),
  these are two full-zero pairs with equal zero-targets and distinct sources —
  excluded by **CEPE:205–206** (vertical exclusion). Hence \(x_1=x_2\).
- *Injectivity.* If \((x,u_1),(x,u_2)\in Z\) with \(u_1\ne u_2\), these are two
  full-zero pairs with equal sources and distinct zero-targets — excluded by
  **CEPE:191–194** (\(u=H'(x)\) with \(H\) differentiable, CEPE:148–150). Hence
  \(u_1=u_2\).
- *Strict monotonicity.* Let \(u_1<u_2\) in \(Y\), \(x_i=P(u_i)\). By CZS:121,
  \((x_1-x_2)(u_1-u_2)\ge0\), so \(x_1\le x_2\); by injectivity \(x_1\ne x_2\);
  hence \(x_1<x_2\).

*(4).* The coordinate projection \(\pi_u:(x,u)\mapsto u\) restricted to \(Z\)
is Borel and, by (2), **injective**. \(Z\) is a Borel subset of the Polish
space \((-1,1)^2\). By the Lusin–Souslin theorem — *an injective Borel image of
a Borel subset of a Polish space is Borel, and the inverse of the injection is
Borel on the image* — the set \(Y=\pi_u(Z)\) is Borel and
\((\pi_u|_Z)^{-1}:Y\to Z\) is Borel. **[standard]** *(reason: Lusin–Souslin;
this is the Borel-graph fact named in O6.1, applied in its injective form.)*
Then \(P=\pi_x\circ(\pi_u|_Z)^{-1}\) is Borel. The same argument with
\(\pi_x\) (injective on \(Z\) by (2)) gives \(P(Y)\) Borel and \(P^{-1}\)
Borel.

A second, descriptive-set-theory-free proof that \(P\) is Borel, recorded
because it is cheaper to check: a strictly increasing function \(P\) on a set
\(Y\subseteq\mathbb R\) is Borel, since for every \(c\in\mathbb R\) the set
\(\{u\in Y:P(u)>c\}\) is *upward closed in \(Y\)* (if \(P(u)>c\) and
\(u'>u\) in \(Y\) then \(P(u')>P(u)>c\)), hence equals \(Y\cap(t,\infty)\) or
\(Y\cap[t,\infty)\) with \(t=\inf\{u\in Y:P(u)>c\}\) — Borel given \(Y\) Borel.
Only the Borel-ness of \(Y\) genuinely consumes Lusin–Souslin.

*(5).* Immediate from (2) and the definition of \(Y\). \(\square\)

### SCOPE FLAG 6.1.A — which document licenses "the **full** interior zero locus"

CERT:73 lists as a certified input:

> "the full interior zero locus is a one-to-one strictly increasing relation."

Its natural source, FR Receipt (ii), states the **weaker, occupancy-restricted**
form (FR:177–179):

> \[\boxed{R_0^{-1}(0)\text{ on the occupied interior support is a one-to-one,
> strictly increasing relation}.}\]

The occupancy qualifier is **not harmless for this document**: Lemma 6.2 needs
the domain of \(P\) to be closed under \((x,u)\mapsto(-u,-x)\), which is free on
the full interior locus (the identity CZS:134 is pointwise on \((-1,1)^2\)) but
would additionally require \(\operatorname{supp}\mu\cap(-1,1)^2\) to be
invariant under that map — a joint-support symmetry established **nowhere** in
the package (the RN laws of CERT §5 are marginal statements only).

**Resolution used here — CORRECTED IN v0.2 (B1/M1/R6, adversary attack 14).**

v0.1 named CZS §6 (CZS:115–126) as the operative anchor and asserted that
"CZS:124–125 are theorems about \(R_0\) and the convex envelope of \(g\)".
**That sentence was false and is deleted.** CZS:124–125 read, in full:

> The convex-envelope theorem excludes equal sources with distinct zero-targets;
> the dual-tie involution excludes equal zero-targets with distinct sources.

These are **one-line pointer sentences**: they *name* two results and neither
states nor proves them; CZS contains no convex-envelope theorem and no dual-tie
argument. What CZS §6 does prove is strict Monge (CZS:117–122). Anchoring the
full-locus graph property at CZS:115–126 would therefore point a referee at a
summary containing two unproved appeals.

**The operative anchor is CEPE §§7–9**, i.e.
`CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md`, a **PROMOTED**
component of the Theorem-(N) package (CEPE:4), where the two exclusions are
actually proved on the full source domain and the conclusion is **boxed**:

> \[
> \boxed{R_0^{-1}(0)\cap D^2\text{ is a one-to-one strictly increasing
> relation}.}
> \]
> [CEPE:223–225, box at **CEPE:224**]

with \(D:=(-1,1)\) fixed at **CEPE:15**. §7 (CEPE:177–194) proves horizontal
exclusion via \(u=H'(x)\) with \(x\) "active for the full source domain `D`,
not for a restricted interval" (CEPE:186–188); §8 (CEPE:196–210) proves the
dual-tie/vertical exclusion; §9 (CEPE:212–225) assembles the two with strict
Monge. This is quoted verbatim in the proof of Lemma 6.1(2)–(3) above.

**Why this is *stronger* than v0.1's resolution, not merely different.** v0.1
argued that FR Receipt (ii) is "the *minimum* Theorem (N) needs, not the
*maximum* CZS proves", inferring this from the word "**weaker**" in FR:172's
heading — authorial-intent reasoning about a heading. That inference is now
unnecessary: **CEPE:208–210 settles it in the document's own words**:

> This theorem concerns `R_0^{-1}(0)`. The raw first-contact correspondence may
> have vertical ties at chord endpoints; at most one such source is a full-zero
> source.

i.e. the *object* of the boxed theorem is the full zero locus \(R_0^{-1}(0)\);
what is deliberately **not** claimed is global uniqueness of the *raw
first-contact* correspondence (compare FR:191–192, and the package's explicit
nonclaim "global uniqueness of the raw first Bellman contact", README:58). The
occupancy qualifier in FR Receipt (ii) is a restriction of the *consumer*
(Theorem (N)'s finite-maximizer contradiction), not a limitation of the proved
theorem. Corroborating pointers: README:29–30 lists CEPE as "the repaired
open-interval convex-minorant proof and **strict full-zero graph**"; the S1
referee's dependency list cites "`CONVEX_ENVELOPE…COMPLETION` §§1–9 **as
repaired by round-3 W1–W4** — … and the strict graph theorem `R_0^{-1}(0) ∩ D²`
one-to-one and strictly increasing" (SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md:
511–513).

**Action for the gate (CORRECTED).** The public amendment should re-anchor
**CERT:73** and **CERT:1073** ("strict full-zero graph") to
`CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` §§7–9, citing
the box at **CEPE:224**. **CZS:115–126 is a secondary anchor only, for the
strict-Monge inequality (CZS:121)**; v0.1's recommendation to re-anchor
CERT:73/CERT:1073 *to CZS:115–126* is **withdrawn**, since it would send a
referee to two unproved appeals instead of to the boxed theorem. A referee
following CERT §14's pointer to FR Receipt (ii) alone lands on the qualified
statement and cannot reconstruct Lemma 6.2; that remains the defect to fix, and
it is a *citation* defect, not a mathematical one.

## Lemma 6.2 (O6.2) — the dual-zero involution, and \(P(Y)=-Y\)

**[inputs: CZS:128–138 (the exact symmetry identity); Claim 0.1; Lemma 6.1]**
**[quantifier: pointwise on \(Y\)]**

**The symmetry identity, quoted verbatim.** CZS §7 "Asymmetry hygiene",
CZS:131–138:

> The involution
>
> \[R_0(-u,-x)=R_0(x,u)\]
>
> is not a symmetry assumption on `g`; it follows from `B(u)=A(-u)` and the
> exact identity `d(-u,-x)=d(x,u)`.

This is a **pointwise identity of functions on \((-1,1)^2\)**, with no
measure-theoretic or occupancy content. For completeness, its one-line proof:
\(d(-u,-x)=(-u)(-x)+\frac{-u+x}{2}-1=xu+\frac{x-u}{2}-1=d(x,u)\); and
\(A(-u)+B(-x)=B(u)+A(x)\) using \(B=A\circ(-\mathrm{id})\) (CZS:87) twice.
Hence \(R_0(-u,-x)=h(-u,-x)-A(-u)-B(-x)=h(x,u)-B(u)-A(x)=R_0(x,u)\).

**Statement.** Define \(\sigma:Y\to\mathbb R\) by \(\sigma(u):=-P(u)\). Then

1. \((x,u)\in Z \iff (-u,-x)\in Z\);
2. \(\sigma(Y)\subseteq Y\), and \(\sigma\circ\sigma=\mathrm{id}_Y\); hence
   \(\sigma\) is an involutive bijection of \(Y\);
3. \(P(\sigma(u))=P(-P(u))=-u\) for **every** \(u\in Y\) (CERT:457);
4. \(P(Y)=-Y\) (CERT:463).

**Proof.**

*(1).* By Claim 0.1, \(Z=R_0^{-1}(0)\cap(-1,1)^2\). If \((x,u)\in(-1,1)^2\)
then \((-u,-x)\in(-1,1)^2\), and CZS:134 gives \(R_0(-u,-x)=R_0(x,u)\); so one
vanishes iff the other does.

*(2)–(3).* Let \(u\in Y\) and \(x=P(u)\), so \((x,u)\in Z\). By (1),
\((-u,-x)\in Z\). Reading off the target coordinate of this pair:
\(-x=-P(u)=\sigma(u)\in Y\). Reading off the source coordinate and using
single-valuedness (Lemma 6.1(2)) at the target \(\sigma(u)\):
\(P(\sigma(u))=-u\). This is (3), which is CERT:457. Applying \(\sigma\) once
more,
\[
\sigma(\sigma(u))=-P(\sigma(u))=-(-u)=u ,
\]
so \(\sigma^2=\mathrm{id}_Y\) and \(\sigma\) is a bijection of \(Y\).

*(4).* By (2), \(-P(Y)=\sigma(Y)=Y\), i.e. \(P(Y)=-Y\). \(\square\)

**Note (the certificate's own caveat, CERT:468–473).** \(P(Y)=-Y\) does *not*
give \(P(Y)=Y\); the map \(\mathbf a=P^{-1}\circ(-\mathrm{id})\circ P\) is
therefore not everywhere defined on \(Y\). Lemma 6.3 is precisely the repair.

## Lemma 6.3 (O6.3) — THE CONULL INVARIANT SET

*(round-2 F-2: the inputs include CERT:214–224 — \(W^2=b(X)^2\), \(WX=-XW\); \(W_B^2=b(U)^2\), \(W_BU=-UW_B\) — so the U-side pre-division argument below is self-anchored rather than resting on CERT:405's "Similarly".)*

**[inputs: CERT:396–402, CERT:408–414 (the two RN laws, quoted below);
CERT:376–390 (the pre-division identity, quoted below — the operative source of
the quantifier, v0.2); CERT:352–361; CERT:70, CERT:229 (positivity of \(g\),
\(b\) on the interior); Claim 0.2; Lemmas 6.1, 6.2]**
**[quantifier: parts (ii) pointwise on \((-1,1)\); parts (i),(iii)
\(\mu_U\)-a.e.; part (iv) pointwise on \(Y_0\)]**

### The two transport laws, quoted verbatim

CERT:395–403:

> \[
> \boxed{
> d((-{\rm id})_\ast\mu_X)
> =
> r_A^2\,d\mu_X,
> \qquad
> r_A(x)=\frac{A(x)}{b(x)}.
> }
> \]

CERT:407–415:

> \[
> \boxed{
> d((-{\rm id})_\ast\mu_U)
> =
> r_B^2\,d\mu_U,
> \qquad
> r_B(u)=\frac{B(u)}{b(u)}.
> }
> \]

### The quantifier of the RN laws — REPLACED IN v0.2 (B2/M2/S2/R2)

CERT:417 qualifies both boxes: "These identities hold almost everywhere on the
endpoint-free support."

**What v0.1 argued, and why it was a non-sequitur.** v0.1 upgraded CERT:417 to
"for every Borel \(E\subseteq(-1,1)\)" on the ground that
\(\mu(E_\partial)=0\) (CERT:171–173), so the endpoint-free support is
\(\mu\)-conull. **Endpoint-nullity addresses \(\pm1\); it says nothing about
extending an on-the-support statement to sets off the support**, and the
upgrade is consumed at exactly such sets (\(Y^c\), \((-Y)^c\), \(D_0^c\)). The
round-1 adversary gave an explicit countermodel to the *inference*: let
\(\mu_X\) be carried by \([0,0.5]\) and assert the law only on the support;
it then fails at \(E=[-0.5,-0.4]\). What is genuinely needed is
\((-\mathrm{id})_*\mu_X\ll\mu_X\) and back.

**The correct derivation, from CERT:376–390.** The certificate proves the laws
by scalar division from a *pre-division* identity that is already universal
over test functions. CERT:372–390, quoted verbatim:

> For bounded Borel \(f\),
>
> \[
> \begin{aligned}
> \langle W\Omega,f(X)W\Omega\rangle
> &=
> \langle\Omega,Wf(X)W\Omega\rangle\\
> &=
> \int b(x)^2f(-x)\,d\mu_X(x),
> \end{aligned}
> \]
>
> while
>
> \[
> \langle A(X)\Omega,f(X)A(X)\Omega\rangle
> =
> \int A(x)^2f(x)\,d\mu_X(x).
> \]

and CERT:392–393: "Since \(A(X)\Omega=W\Omega\), scalar division on compact
subsets of \((-1,1)\), followed by monotone convergence, gives" — the boxes
above. Write the division out; it takes three lines and leaves **no**
exceptional set.

*Line 1.* \(A(X)\Omega=W\Omega\) (CERT:352–356, boxed), so the two left-hand
sides coincide and, **for every bounded Borel \(f\)**,
\[
\int b(x)^2f(-x)\,d\mu_X(x)=\int A(x)^2f(x)\,d\mu_X(x).
\]

*Line 2.* Substituting \(y=-x\) in the left integral and using that \(b\) is
**even** (\(b(t)=\sqrt{1-t^2}/2\), CERT:229, so \(b(-y)=b(y)\)),
\[
\int b(y)^2f(y)\,d\bigl((-\mathrm{id})_*\mu_X\bigr)(y)
=\int A(y)^2f(y)\,d\mu_X(y)
\qquad\text{for every bounded Borel }f .
\]
Two finite Borel measures on \([-1,1]\) that integrate every bounded Borel
function equally are equal, so
\[
b^2\,d\bigl((-\mathrm{id})_*\mu_X\bigr)=A^2\,d\mu_X
\tag{6.3.0}
\]
as an identity of finite Borel measures — **no a.e., no support caveat.**

*Line 3.* Both \(\mu_X\) and \((-\mathrm{id})_*\mu_X\) are carried by
\((-1,1)\) (\(\mu(E_\partial)=0\), CERT:171–173, and \(E_\partial\) is
symmetric), and on \((-1,1)\) we have \(b(x)^2\in(0,\infty)\) **at every
point** (CERT:229; \(1-x^2>0\)). Hence \(1/b^2\) is a finite nonnegative Borel
function there (finiteness of \(A^2\,d\mu_X\) follows from (6.3.0) at \(f\equiv 1\): the left side is at most 1/4 — round-2 F-3), and applying it to (6.3.0) gives, for **every** Borel
\(E\subseteq(-1,1)\),
\[
(-\mathrm{id})_*\mu_X(E)
=\int_E\frac{1}{b^2}\;b^2\,d\bigl((-\mathrm{id})_*\mu_X\bigr)
=\int_E\frac{A^2}{b^2}\,d\mu_X
=\int_E r_A^2\,d\mu_X .
\]
The same argument with \(W_B,B(U),\mu_U\) (CERT:358–362, CERT:405–415) gives the
\(U\)-law. Therefore
\[
(-\mathrm{id})_*\mu_X(E)=\int_E r_A^2\,d\mu_X,\qquad
(-\mathrm{id})_*\mu_U(E)=\int_E r_B^2\,d\mu_U
\tag{RN-X},(RN-U)
\]
**for every Borel \(E\subseteq(-1,1)\)**, where
\((-\mathrm{id})_*\lambda(E)=\lambda(-E)\).

*(Here the endpoint nullity does real but limited work: it puts both measures
on \((-1,1)\), which is exactly where \(b^2>0\). It is **not** what licenses
the extension off the support — (6.3.0) already holds globally, and mutual
absolute continuity is read off it. CERT:433 records the same content in one
sentence — "Hence both reflected measures are equivalent to the original
measures on the interior support" — and was also uncited in v0.1; it is now
OX.1 row A15′.)*

### Claim 6.3.1 — \(\mu_X=P_*\mu_U\), and \(\mu_U(Y)=1\)

*Statement.* \(\mu_U(Y)=1\), and for every Borel \(E\subseteq(-1,1)\),
\(\mu_X(E)=\mu_U(P^{-1}(E))\).

*Proof.* By Claim 0.2, \(\mu(Z)=1\). Every \((x,u)\in Z\) has \(u\in Y\), so
\(\mu_U(Y)=\mu(\{(x,u):u\in Y\})\ge\mu(Z)=1\). For the second part, let
\(E\subseteq(-1,1)\) be Borel. Then
\[
\mu_X(E)=\mu(E\times(-1,1))=\mu\bigl((E\times(-1,1))\cap Z\bigr)
=\mu\bigl(\{(P(u),u):u\in Y,\ P(u)\in E\}\bigr),
\]
using \(\mu(Z)=1\) and Lemma 6.1(5). The last set has \(u\)-projection
\(P^{-1}(E)\cap Y=P^{-1}(E)\), and \(\mu\) restricted to \(Z\) is carried by a
graph, so its \(\mu\)-measure equals the \(\mu_U\)-measure of that projection:
\(\mu_X(E)=\mu_U(P^{-1}(E))\). (Formally: the map \(u\mapsto(P(u),u)\) is a
Borel isomorphism of \(Y\) onto \(Z\) by Lemma 6.1(4), and it pushes
\(\mu_U|_Y\) to \(\mu|_Z\), because both measures agree on the sets
\((E\times F)\cap Z\), which correspond to \(P^{-1}(E)\cap F\).) \(\square\)

### (ii) THE KEY LEMMA — the transport densities are pointwise positive and finite

**Claim 6.3.2.** For **every** \(x\in(-1,1)\): \(0<r_A(x)<\infty\).
For **every** \(u\in(-1,1)\): \(0<r_B(u)<\infty\).

*Proof.* Fix \(x\in(-1,1)\). Then \(b(x)=\tfrac{\sqrt{1-x^2}}{2}\in(0,\infty)\)
(CERT:229; \(1-x^2>0\)). Also \(-x\in(-1,1)\), so \(g(x)>0\) and \(g(-x)>0\)
(CERT:70, FR:63). Hence \(p(x)=b(x)^2/g(x)\in(0,\infty)\) and
\(A(x)=\sqrt{p(x)g(-x)}\in(0,\infty)\) (CZS:87). Therefore
\(r_A(x)=A(x)/b(x)\in(0,\infty)\). The argument for \(r_B(u)=B(u)/b(u)\) with
\(B(u)=\sqrt{g(u)p(-u)}\) is identical. \(\square\)

This is a **pointwise** statement on the whole interior, stronger than the
a.e. statement O6.3(ii) asks for.

**Where Claim 6.3.2 is genuinely load-bearing — CORRECTED IN v0.2 (B3/M3/R3).**
v0.1 attributed the pointwise strengthening loosely to "the null-set
bookkeeping below". The round-1 proof auditor traced the actual dependency and
it is narrower. Claim 6.3.2 is load-bearing at **exactly three** places:

1. **\(\rho\in(0,\infty)\) in Lemmas 7.5–7.6.** \(\rho=r_A(x)=r_B(u)\) must be a
   strictly positive *real number at the single point* produced by Lemma 7.7,
   because Lemma 7.6 Step 5 multiplies the two Bellman equalities and cancels
   \(\rho\). An a.e. statement gives nothing at a chosen point unless the
   exceptional set is folded into the conull count — and folding it in is
   precisely what Lemma 7.7's single-intersection argument avoids.
2. **Atom propagation, Lemma 9.5(2).** The induction over words divides by
   \(r_B(u)^2\) and \(r_A(P(u))^2\) at *every* point of a countable orbit; a
   null set of bad points is not visible to a countable orbit argument, so the
   positivity must be pointwise.
3. **The single-conull-set count in Lemma 7.7.** Because everything else in
   Lemmas 7.4–7.6 is pointwise on \(F\), the a.e.-to-existence step needs
   exactly **one** intersection (\(C_1\)), not a countable stack of them.

It is **not** needed for Claim 6.3.3 as used in §6, for Claim 6.3.5, for Claim
6.3.5′, or for the induction of Claim 6.3.6 — see the note after Claim 6.3.3
and the corrected proof of Claim 6.3.5. Trace of the counterfactual: if Claim
6.3.2 held only \(\mu_U\)-a.e., §6 would survive unchanged, and L7.6, L7.7 and
L9.5 would break. As it stands the claim is pointwise from \(g(x)>0\) for every
\(x\in(-1,1)\) (CERT:70, FR:63), so nothing breaks.

**Claim 6.3.3 (quasi-invariance, both directions).** For Borel
\(N\subseteq(-1,1)\):
\[
\mu_U(N)=0 \iff \mu_U(-N)=0,\qquad
\mu_X(N)=0 \iff \mu_X(-N)=0 .
\]

*Proof.* (\(\Rightarrow\)) If \(\mu_U(N)=0\), then by (RN-U)
\(\mu_U(-N)=(-\mathrm{id})_*\mu_U(N)=\int_N r_B^2\,d\mu_U=0\), since the
integral of any nonnegative Borel function over a null set is \(0\).
(\(\Leftarrow\)) If \(\mu_U(-N)=0\), then \(\int_N r_B^2\,d\mu_U=0\); the
integrand is **strictly positive at every point** of \(N\subseteq(-1,1)\) by
Claim 6.3.2; a nonnegative Borel function with vanishing integral is \(0\)
a.e., so \(r_B^2=0\) \(\mu_U\)-a.e. on \(N\), which forces \(\mu_U(N)=0\). The
\(\mu_X\) statement is the same argument with (RN-X) and \(r_A\). \(\square\)

*(This is the step the commission calls "what licenses the countable
intersection".)*

**Note on what this claim is and is not needed for — v0.2 (B3/M3/R3).** v0.1
appended here the parenthetical "without pointwise positivity, only the
\(\Rightarrow\) direction would be available, and the induction of Claim 6.3.6
would fail." **That sentence was FALSE as placed and is deleted.** Two separate
corrections:

- The (\(\Leftarrow\)) half proved above is *not* needed to run §6. Both
  directions of quasi-invariance follow from (\(\Rightarrow\)) alone, applied
  to the reflected set: for Borel \(N\subseteq(-1,1)\), (\(\Rightarrow\))
  applied at \(-N\) gives \(\mu_U(-N)=0\Rightarrow\mu_U(N)=0\), since
  \(-(-N)=N\) and \(\mathbf b\) is an involution. The same remark applies to
  \(\mu_X\), and it is what the corrected proof of Claim 6.3.5 below uses.
- The induction of Claim 6.3.6 consequently does **not** fail without pointwise
  positivity; it needs only that each of \(\mathbf a,\mathbf b\) carries null
  sets to null sets in both directions, which the involution argument supplies.

Claim 6.3.2's genuine consumers are listed after its proof above (\(\rho\) in
L7.5/L7.6, atom propagation in L9.5(2), the conull count in L7.7). Both
directions are nevertheless recorded here because Claim 6.3.5′ and Claim 6.3.6
quote the two-directional form for brevity.

### (i) Each RN law forces its reflected coordinate to exist a.e.

**Claim 6.3.4 (the \(\mathbf b\)-domain).** Let
\(D_{\mathbf b}:=Y\cap(-Y)\). Then \(D_{\mathbf b}\) is Borel,
\(\mu_U(D_{\mathbf b})=1\), \(\mathbf b(D_{\mathbf b})=D_{\mathbf b}\), and
\(\mathbf b(u)=-u\) is an involutive bijection of \(D_{\mathbf b}\).

*Proof.* Borel: Lemma 6.1(4). By Claim 6.3.1, \(\mu_U(Y)=1\), i.e.
\(\mu_U(Y^c\cap(-1,1))=0\); by Claim 6.3.3 (\(\Rightarrow\)),
\(\mu_U(-(Y^c\cap(-1,1)))=\mu_U((-Y)^c\cap(-1,1))=0\), i.e.
\(\mu_U(-Y)=1\). Hence \(\mu_U(Y\cap(-Y))=1\). Invariance:
\(-\bigl(Y\cap(-Y)\bigr)=(-Y)\cap Y=D_{\mathbf b}\). Involution: obvious.
\(\square\)

**Claim 6.3.5 (the \(\mathbf a\)-domain).** Let
\(D_{\mathbf a}:=\{u\in Y: P(u)\in Y\}=P^{-1}(Y)\). Then \(D_{\mathbf a}\) is
Borel, \(\mu_U(D_{\mathbf a})=1\), \(\mathbf a\) is everywhere defined on
\(D_{\mathbf a}\), \(\mathbf a(D_{\mathbf a})=D_{\mathbf a}\), and
\(\mathbf a\) is an involutive bijection of \(D_{\mathbf a}\) with
\(P(\mathbf a(u))=-P(u)\).

*Proof.* *Definedness.* \(\mathbf a(u)=P^{-1}(-P(u))\) is defined iff
\(-P(u)\in P(Y)\). By Lemma 6.2(4), \(P(Y)=-Y\), so this holds iff
\(P(u)\in Y\). Hence the domain of \(\mathbf a\) is exactly \(P^{-1}(Y)\),
which is Borel by Lemma 6.1(4).

*Conullity — this is the promised argument, not a gesture.* Suppose, for the
contradiction the obligation asks to rule out, that \(\mu_U(D_{\mathbf a})<1\).
We compute \(\mu_U(D_{\mathbf a})\) exactly. By Claim 6.3.1,
\[
\mu_U(D_{\mathbf a})=\mu_U(P^{-1}(Y))=\mu_X(Y).
\]
Now \(\mu_X(P(Y))=\mu_U(P^{-1}(P(Y)))=\mu_U(Y)=1\), and \(P(Y)=-Y\) (Lemma
6.2(4)), so \(\mu_X(-Y)=1\), i.e.
\(\mu_X\bigl((-Y)^c\cap(-1,1)\bigr)=0\). By Claim 6.3.3 applied to \(\mu_X\)
with \(N=(-Y)^c\cap(-1,1)\), we get \(\mu_X(-N)=0\), and
\(-N=Y^c\cap(-1,1)\). Hence \(\mu_X(Y)=1\), so
\(\mu_U(D_{\mathbf a})=1\) — contradicting the supposition. (Equivalently and
without contradiction: \(\mu_U(D_{\mathbf a})=\mu_X(Y)=1\).)

**Quantifier note — CORRECTED IN v0.2 (B3/M3/R3, adversary S2 second half).**
The displayed derivation above consumes Claim 6.3.3 **in the
(\(\Rightarrow\)) direction only**: it is applied to the null set
\(N=(-Y)^c\cap(-1,1)\) and concludes that \(-N=Y^c\cap(-1,1)\) is null. No
pointwise positivity of \(r_A\) is used anywhere in it. v0.1 followed it with a
second, (\(\Leftarrow\))-and-positivity route and presented that route as "the
mechanism"; the round-1 auditors independently found it **redundant**, and its
displayed complement expression was malformed. Both are repaired below.

The mechanism, stated plainly as O6.3(i) demands and using only
(\(\Rightarrow\)): the domain of \(\mathbf a\) is the \(P\)-preimage of \(Y\);
\(\mu_X\) already charges \(-Y\) fully, because \(\mu_X=P_*\mu_U\) is carried by
\(P(Y)=-Y\); and (RN-X) says the reflection \((-\mathrm{id})_*\mu_X\) is
absolutely continuous with respect to \(\mu_X\), so it kills every \(\mu_X\)-null
set. Applying that to the \(\mu_X\)-null set \((-Y)^c\cap(-1,1)\) transfers full
mass onto \(Y\): \(\mu_X(Y)=1\), i.e. \(\mu_U(D_{\mathbf a})=1\).

*(Redundant illustration, recorded only because O6.3(i) asks for the "two sides
disagree" form, and **not** used: if \(\mu_X(Y^c\cap(-1,1))=\epsilon>0\), then
(RN-X) at \(E=Y^c\cap(-1,1)\) gives
\[
\mu_X\bigl((-Y)^{c}\cap(-1,1)\bigr)
=\mu_X\bigl(-(Y^{c}\cap(-1,1))\bigr)
=\int_{Y^{c}\cap(-1,1)}r_A^2\,d\mu_X>0,
\]
strictly, because \(r_A^2>0\) at every point of the interior (Claim 6.3.2) and
\(\mu_X(Y^c\cap(-1,1))=\epsilon>0\) — contradicting \(\mu_X(-Y)=1\). This route
does use pointwise positivity; the boxed derivation above does not, and it is
the one Claim 6.3.5 rests on.)*

*Invariance and involutivity.* Let \(u\in D_{\mathbf a}\) and
\(v=\mathbf a(u)=P^{-1}(-P(u))\). Then \(v\in Y\) (as \(P^{-1}\) maps into
\(Y\)) and \(P(v)=-P(u)=\sigma(u)\), which lies in \(Y\) by Lemma 6.2(2).
Hence \(v\in P^{-1}(Y)=D_{\mathbf a}\). Moreover
\(\mathbf a(v)=P^{-1}(-P(v))=P^{-1}(P(u))=u\). So
\(\mathbf a|_{D_{\mathbf a}}\) is an involutive bijection onto
\(D_{\mathbf a}\), and \(P\circ\mathbf a=-P\) pointwise on
\(D_{\mathbf a}\). \(\square\)

**Claim 6.3.5′ (the \(\mathbf a\)-transport law and \(\mathbf a\)-quasi-invariance).**
For every Borel \(E\subseteq D_{\mathbf a}\),
\[
\mu_U(\mathbf aE)=\int_E r_A(P(u))^2\,d\mu_U(u),
\]
and consequently \(\mu_U(N)=0\iff\mu_U(\mathbf aN)=0\) for Borel
\(N\subseteq D_{\mathbf a}\).

*Proof.* \(\mathbf a\) is a Borel involution of \(D_{\mathbf a}\)
(Claim 6.3.5, Lemma 6.1(4)), so \(\mathbf aE\) is Borel. Using
\(P\circ\mathbf a=-P\) and \(\mathbf a\) bijective,
\(P(\mathbf aE)=-P(E)\). Then by Claim 6.3.1, (RN-X), and the change of
variables \(\mu_X=P_*\mu_U\):
\[
\mu_U(\mathbf aE)=\mu_X\bigl(P(\mathbf aE)\bigr)
=\mu_X\bigl(-P(E)\bigr)
=(-\mathrm{id})_*\mu_X\bigl(P(E)\bigr)
=\int_{P(E)}r_A^2\,d\mu_X
=\int_E r_A(P(u))^2\,d\mu_U(u).
\]
(The first equality uses \(\mu_U(F)=\mu_X(P(F))\) for Borel \(F\subseteq Y\),
which is Claim 6.3.1 read through the bijection \(P\); the last is the change
of variables for the pushforward \(\mu_X=P_*\mu_U\).) The density
\(u\mapsto r_A(P(u))^2\) is strictly positive and finite at every point of
\(D_{\mathbf a}\subseteq Y\subseteq(-1,1)\) with \(P(u)\in(-1,1)\), by Claim
6.3.2; the two-directional null-set statement then follows exactly as in Claim
6.3.3. \(\square\)

*(**v0.2, B3/M3:** as at Claim 6.3.3, the positivity route is convenient but not
necessary here. The backward direction also follows from the forward one by the
involution: applying the displayed law at \(\mathbf aN\) and using
\(\mathbf a^2=\mathrm{id}\) gives \(\mu_U(N)=\int_{\mathbf aN}r_A(P)^2d\mu_U\),
so \(\mu_U(\mathbf aN)=0\Rightarrow\mu_U(N)=0\). Claim 6.3.2 is therefore **not**
among this claim's essential inputs; its essential consumers are listed after
its proof.)*

*(Claim 6.3.5′ is CERT:514–519 with a proof; the certificate displays it
without derivation.)*

### (iii) The countable intersection

**Claim 6.3.6.** Put \(D_0:=D_{\mathbf a}\cap D_{\mathbf b}\) (Borel,
\(\mu_U\)-conull). For a finite word
\(w=s_k s_{k-1}\cdots s_1\) with \(s_i\in\{\mathbf a,\mathbf b\}\) (\(k\ge0\);
\(k=0\) is the empty word \(e\)), define
\[
G_w:=\{u\in D_0:\ s_j\cdots s_1(u)\text{ is defined and lies in }D_0
\text{ for every }1\le j\le k\}.
\]
Then each \(G_w\) is Borel and \(\mu_U(G_w)=1\).

*Proof.* Induction on \(|w|=k\). Base \(k=0\): \(G_e=D_0\), Borel and conull
by Claims 6.3.4, 6.3.5. Inductive step: let \(w'=s\,w\) with
\(s\in\{\mathbf a,\mathbf b\}\). Then
\[
G_{w'}=G_w\cap (w|_{G_w})^{-1}\bigl(D_0\cap s^{-1}(D_0)\bigr).
\]
Here \(w|_{G_w}\) is a Borel injection of \(G_w\) into \(D_0\) (a finite
composition of the Borel involutions \(\mathbf a,\mathbf b\), each restricted
to a set where it is defined), so the preimage is Borel; \(G_{w'}\) is Borel.

For conullity: \(D_0\cap s^{-1}(D_0)=D_0\cap s(D_0)\) (as \(s\) is an
involution on its domain) is conull — indeed \(D_0^c\cap D_s\) is
\(\mu_U\)-null, so by the two-directional quasi-invariance (Claim 6.3.3 for
\(s=\mathbf b\); Claim 6.3.5′ for \(s=\mathbf a\)) its \(s\)-image is null,
whence \(s(D_0)\cap D_s\) is conull. Call this conull Borel set \(H_s\).

Now \(G_{w'}=G_w\cap w^{-1}(H_s)\). \(G_w\) is conull by induction. And
\(w^{-1}(H_s^c)\cap G_w\) is null: \(H_s^c\cap D_0\) is null, and \(w\)
restricted to \(G_w\) is a composition of at most \(k\) maps each of which
carries null sets to null sets **in both directions** (Claims 6.3.3, 6.3.5′);
by induction on \(k\), \(w^{-1}\) of a null set intersected with \(G_w\) is
null. Hence \(\mu_U(G_{w'})=1\). \(\square\)

**Claim 6.3.7 (definition and properties of \(Y_0\)).** Put
\[
Y_0:=\bigcap_{w}G_w ,
\]
the intersection over the countably many finite words \(w\) in
\(\{\mathbf a,\mathbf b\}\). Then:

1. \(Y_0\) is Borel and \(\mu_U(Y_0)=1\);
2. every finite word \(w\) in \(\mathbf a,\mathbf b\) is defined at every point
   of \(Y_0\);
3. \(\mathbf a(Y_0)=Y_0\) and \(\mathbf b(Y_0)=Y_0\);
4. \(Y_0\subseteq Y\subseteq(-1,1)\), and for \(u\in Y_0\) both \(P(u)\) and
   \(P(-u)\) are defined and lie in \((-1,1)\).

*Proof.* (1) There are countably many finite words over a two-letter alphabet;
a countable intersection of Borel conull sets is Borel and conull (Claim
6.3.6). (2) Immediate from the definition of \(G_w\). (3) Let \(u\in Y_0\) and
\(s\in\{\mathbf a,\mathbf b\}\). For any word \(w\), \(w(s(u))=(ws)(u)\) is
defined and its partial products lie in \(D_0\) because \(u\in G_{ws}\) and all
partial products of \(ws\) at \(u\) are exactly the partial products of \(w\)
at \(s(u)\), preceded by \(s(u)\in D_0\). Hence \(s(u)\in G_w\) for all \(w\),
i.e. \(s(u)\in Y_0\). So \(s(Y_0)\subseteq Y_0\); applying \(s\) again and
using \(s^2=\mathrm{id}\) gives \(Y_0\subseteq s(Y_0)\). (4) \(Y_0\subseteq
D_0\subseteq Y\subseteq(-1,1)\), \(P\) is defined on \(Y\), and
\(-u=\mathbf b(u)\in Y_0\subseteq Y\) by (3). \(\square\)

### (iv) \(\mathbf a\) and \(\mathbf b\) are decreasing involutions on \(Y_0\)

**Claim 6.3.8.** On \(Y_0\), both \(\mathbf a\) and \(\mathbf b\) are strictly
decreasing Borel involutions of \(Y_0\) onto itself.

*Proof.* \(\mathbf b(u)=-u\) is strictly decreasing, Borel, involutive, and maps
\(Y_0\) onto \(Y_0\) (Claim 6.3.7(3)).

\(\mathbf a=P^{-1}\circ(-\mathrm{id})\circ P\). By Lemma 6.1(3), \(P\) is
strictly increasing on \(Y\), hence \(P^{-1}\) is strictly increasing on
\(P(Y)\) (the inverse of a strictly increasing bijection between subsets of
\(\mathbb R\) is strictly increasing). \(-\mathrm{id}\) is strictly decreasing.
The composition increasing∘decreasing∘increasing is strictly decreasing.
It is Borel by Lemma 6.1(4), and involutive with \(\mathbf a(Y_0)=Y_0\) by
Claims 6.3.5, 6.3.7(3). \(\square\)

**This completes Lemma 6.3.** The set \(Y_0\) of CERT:481 exists, is Borel,
is \(\mu_U\)-conull, is invariant under both response transformations, and
\(\mathbf a,\mathbf b\) are everywhere-defined decreasing Borel involutions on
it (CERT:486–492). \(\square\)

## Lemma 6.4 (O6.4) — \(\tau\) is strictly increasing and has no non-fixed periodic point

**[inputs: Lemma 6.3 (Claim 6.3.8)]**
**[quantifier: pointwise on \(Y_0\)]**

**Statement.** \(\tau:=\mathbf a\circ\mathbf b\) is a strictly increasing Borel
bijection of \(Y_0\) onto \(Y_0\), and for every \(u\in Y_0\) and every
\(n\in\mathbb Z\setminus\{0\}\),
\[
\tau^n(u)=u \implies \tau(u)=u .
\]

**Proof.** *Increasing.* \(\mathbf a,\mathbf b\) are strictly decreasing
bijections of \(Y_0\) (Claim 6.3.8); a composition of two strictly decreasing
maps is strictly increasing: \(u_1<u_2\Rightarrow \mathbf b(u_1)>\mathbf b(u_2)
\Rightarrow \mathbf a(\mathbf b(u_1))<\mathbf a(\mathbf b(u_2))\). It is a
bijection of \(Y_0\) with inverse \(\tau^{-1}=\mathbf b\circ\mathbf a\)
(using \(\mathbf a^2=\mathbf b^2=\mathrm{id}\)), also strictly increasing.

*No non-fixed periodic point.* Fix \(u\in Y_0\), and suppose \(\tau(u)\ne u\).

- Case \(\tau(u)>u\). We show \(\tau^n(u)>u\) for every \(n\ge1\) by induction.
  \(n=1\) is the hypothesis. If \(\tau^{n}(u)>u\), then applying the strictly
  increasing \(\tau\): \(\tau^{n+1}(u)>\tau(u)>u\). Hence \(\tau^n(u)\ne u\)
  for all \(n\ge1\). For \(n\le-1\), write \(m=-n\ge1\); applying the strictly
  increasing \(\tau^{m}\) to \(\tau^{n}(u)=\tau^{-m}(u)\): if
  \(\tau^{-m}(u)=u\) then \(u=\tau^{m}(u)>u\), a contradiction. So
  \(\tau^n(u)\ne u\) for all \(n\ne 0\).
- Case \(\tau(u)<u\). Symmetric: by induction \(\tau^n(u)<u\) for \(n\ge1\)
  (if \(\tau^n(u)<u\) then \(\tau^{n+1}(u)<\tau(u)<u\)), and the negative case
  as above.

Contrapositively, \(\tau^n(u)=u\) for some \(n\ne0\) forces \(\tau(u)=u\).
\(\square\)

*(This is CERT:503–508 with both directions and the negative exponents written
out; CERT states only "An increasing injective map has no non-fixed periodic
orbit.")*

## Lemma 6.5 (O6.5) — the two transport laws restated on \(Y_0\)

**[inputs: (RN-X), (RN-U) as fixed in Lemma 6.3 from CERT:376–390; Claims
6.3.3, 6.3.5′; Claim 6.3.7]**
**[quantifier: for every Borel \(E\subseteq Y_0\) — no exceptional set in
\(E\), and, after the v0.2 derivation of (RN-X)/(RN-U), none upstream either]**

*(**v0.2, m7:** v0.1's header listed **CERT:514–527** as an *input*. CERT:514–527
is the pair of boxed transport laws in **CERT §6** — i.e. part of the very
output this document is expanding — and listing it as an input contradicts
OX.4's "No CERT §§6–9 display is used as an input". The genuine inputs are the
§5 RN laws; CERT:514–527 is what this lemma **supplies a derivation for**, and
is cited that way in the proof and in F5. The proof itself was and is
unaffected.)*

**Statement.** For **every** Borel set \(E\subseteq Y_0\),
\[
\boxed{\ \mu_U(\mathbf aE)=\int_E r_A(P(u))^2\,d\mu_U(u)\ }
\tag{T-a}
\]
\[
\boxed{\ \mu_U(\mathbf bE)=\int_E r_B(u)^2\,d\mu_U(u)\ }
\tag{T-b}
\]
Equivalently, since \(\mathbf a,\mathbf b\) are involutions of \(Y_0\),
\[
\mathbf a_*\mu_U=r_A(P(\cdot))^2\,\mu_U,\qquad
\mathbf b_*\mu_U=r_B^2\,\mu_U
\]
as Borel measures on \(Y_0\).

**Proof.** (T-a) is Claim 6.3.5′ restricted to \(E\subseteq Y_0\subseteq
D_{\mathbf a}\). (T-b): \(\mathbf bE=-E\), so (RN-U) gives
\(\mu_U(\mathbf bE)=\mu_U(-E)=(-\mathrm{id})_*\mu_U(E)=\int_E r_B^2\,d\mu_U\).
For the pushforward form: \(\mathbf b_*\mu_U(E)=\mu_U(\mathbf b^{-1}E)
=\mu_U(\mathbf bE)\) since \(\mathbf b^{-1}=\mathbf b\); likewise for
\(\mathbf a\). \(\square\)

**Quantifier note (updated in v0.2).** The measurable-set quantifier is
*universal over Borel \(E\subseteq Y_0\)*, with no null exception. After the
v0.2 derivation in Lemma 6.3, (RN-X)/(RN-U) are identities of Borel measures on
\((-1,1)\) holding for **every** Borel \(E\) — obtained from the pre-division
identity (6.3.0) plus \(b^2>0\) pointwise, with **no a.e. content to consume at
all** and no support caveat. (v0.1 said the a.e. content of CERT:417 "was
consumed once"; that phrasing is superseded — there is none.) Nothing recurs
per-\(E\). This matters in Lemma 7.3, which quantifies over all Borel
\(E\subseteq F\).

---

# §7 — Fixed points carry no mass

Throughout §7, \(F:=\{u\in Y_0:\tau(u)=u\}\) (CERT:536–537).

## Lemma 7.1 (O7.1) — \(F\) is Borel and \(\mathbf a,\mathbf b\)-invariant

**[inputs: Lemmas 6.3, 6.4]**
**[quantifier: pointwise on \(Y_0\)]**

**Statement.** \(F\) is Borel, \(\mathbf a(F)=F\), \(\mathbf b(F)=F\), and
\(\tau(F)=F\).

**Proof.** *Borel:* \(\tau\) and \(\mathrm{id}\) are Borel maps \(Y_0\to
\mathbb R\); \(F=\{u\in Y_0:\tau(u)-u=0\}\) is the preimage of \(\{0\}\) under
a Borel function, hence Borel.

*The conjugation identity.* Since \(\mathbf a^2=\mathbf b^2=\mathrm{id}\) on
\(Y_0\),
\[
\mathbf b\,\tau\,\mathbf b=\mathbf b(\mathbf a\mathbf b)\mathbf b
=(\mathbf b\mathbf a)(\mathbf b\mathbf b)=\mathbf b\mathbf a=\tau^{-1}.
\tag{7.1.1}
\]

*\(\mathbf b\)-invariance.* Let \(u\in F\), i.e. \(\mathbf a(\mathbf b(u))=u\).
Apply \(\mathbf a\) to both sides: \(\mathbf b(u)=\mathbf a(u)\). Then
\[
\tau(\mathbf b(u))=\mathbf a(\mathbf b(\mathbf b(u)))=\mathbf a(u)=\mathbf b(u),
\]
so \(\mathbf b(u)\in F\). Hence \(\mathbf b(F)\subseteq F\); applying
\(\mathbf b\) again gives \(F\subseteq\mathbf b(F)\), so \(\mathbf b(F)=F\).

*\(\mathbf a\)-invariance.* With \(u\in F\) we just showed
\(\mathbf a(u)=\mathbf b(u)\); therefore \(\mathbf a(u)\in F\) by the previous
paragraph, and \(\mathbf a(F)=F\) by the same involution argument.

*\(\tau\)-invariance.* \(\tau(u)=u\) for \(u\in F\), so \(\tau(F)=F\)
trivially. \(\square\)

## Lemma 7.2 (O7.2) — on \(F\), \(\mathbf a(u)=\mathbf b(u)=-u\)

**[inputs: Lemma 7.1]**
**[quantifier: pointwise on \(F\) — no exceptional set]**

**Statement.** For **every** \(u\in F\): \(\mathbf a(u)=\mathbf b(u)=-u\).

**Proof.** \(u\in F\) means \(\mathbf a(\mathbf b(u))=u\). Applying the
involution \(\mathbf a\) to both sides gives \(\mathbf b(u)=\mathbf a(u)\).
And \(\mathbf b(u)=-u\) by definition (Claim 6.3.8). \(\square\)

*(CERT:546. Note the quantifier: this is exact and pointwise, which is what
Lemma 7.3 needs in order to identify the two transported sets.)*

## Lemma 7.3 (O7.3) — equal integrals over every Borel \(E\subseteq F\) force equal densities \(\mu_U\)-a.e. on \(F\)

**[inputs: Lemma 6.5 (T-a),(T-b); Lemma 7.2]**
**[quantifier: hypothesis pointwise on \(F\); conclusion \(\mu_U\)-a.e. on
\(F\)]**

**Statement.** \(r_A(P(u))=r_B(u)\) for \(\mu_U\)-almost every \(u\in F\).

**Proof.**

*Step 1 — \(\mathbf aE=\mathbf bE\) pointwise, for every \(E\subseteq F\).*
Let \(E\subseteq F\) be Borel. By Lemma 7.2, \(\mathbf a\) and \(\mathbf b\)
agree at every point of \(F\), hence at every point of \(E\). Therefore the
image sets coincide: \(\mathbf aE=\{\mathbf a(u):u\in E\}=\{-u:u\in E\}=-E
=\mathbf bE\). *(This is the justification O7.3 flags as needed pointwise:
"both equal \(-E\)". It is not an a.e. statement and could not be, since
\(\mathbf aE\) and \(\mathbf bE\) are sets, not measure classes.)*

*Step 2 — equal integrals.* By Lemma 6.5, for every Borel \(E\subseteq F\),
\[
\int_E r_A(P(u))^2\,d\mu_U(u)=\mu_U(\mathbf aE)=\mu_U(\mathbf bE)
=\int_E r_B(u)^2\,d\mu_U(u).
\tag{7.3.1}
\]
(CERT:551–555.)

*Step 3 — integrability.* Taking \(E=F\) in (7.3.1),
\(\int_F r_A(P)^2\,d\mu_U=\mu_U(\mathbf aF)\le1\) and
\(\int_F r_B^2\,d\mu_U=\mu_U(\mathbf bF)\le1\), since \(\mu_U\) is a
probability measure. So both densities are \(\mu_U\)-integrable on \(F\), and
\(h:=r_A(P(\cdot))^2-r_B(\cdot)^2\) is a well-defined \(\mu_U\)-integrable
Borel function on \(F\) with \(\int_E h\,d\mu_U=0\) for every Borel
\(E\subseteq F\).

*Step 4 — densities equal a.e.* **[standard, written out]** Put
\(E_+:=F\cap\{h>0\}\) and \(E_-:=F\cap\{h<0\}\); both are Borel. Then
\(\int_{E_+}h\,d\mu_U=0\) with \(h>0\) on \(E_+\). A nonnegative
\(\mu_U\)-integrable function with zero integral vanishes \(\mu_U\)-a.e.; since
\(h>0\) *everywhere* on \(E_+\), this forces \(\mu_U(E_+)=0\). Symmetrically
with \(-h\), \(\mu_U(E_-)=0\). Hence \(h=0\) \(\mu_U\)-a.e. on \(F\), i.e.
\(r_A(P(u))^2=r_B(u)^2\) for \(\mu_U\)-a.e. \(u\in F\).

*Step 5 — from squares to values.* By Claim 6.3.2 both \(r_A(P(u))\) and
\(r_B(u)\) are **strictly positive** at every \(u\in Y_0\); equality of squares
of positive reals gives equality of the reals. Hence
\(r_A(P(u))=r_B(u)\) \(\mu_U\)-a.e. on \(F\). \(\square\)

**Named null set.** Let \(N_1:=\{u\in F:r_A(P(u))\ne r_B(u)\}\); \(N_1\) is
Borel and \(\mu_U(N_1)=0\). Set \(F^\ast:=F\setminus N_1\). All of §7 below
is **pointwise on \(F^\ast\)**.

**Notation (CERT:567–571).** For \(u\in F^\ast\) put
\[
x:=P(u),\qquad \rho:=r_A(x)=r_B(u)\in(0,\infty).
\]
The positivity and finiteness of \(\rho\) is Claim 6.3.2, pointwise — this
discharges the "\(\rho>0\)" check that O7.6 requires.

## Lemma 7.4 (O7.4) — both \((x,u)\) and \((-x,-u)\) are full-zero pairs

**[inputs: Lemma 7.2; Lemma 6.1(5)]**
**[quantifier: pointwise on \(F\) (hence on \(F^\ast\))]**

**Statement.** For every \(u\in F\), with \(x=P(u)\):
\(P(-u)=-x\), and both \((x,u)\in Z\) and \((-x,-u)\in Z\).

**Proof.** \((x,u)=(P(u),u)\in Z\) by Lemma 6.1(5), since \(u\in F\subseteq
Y_0\subseteq Y\).

By Lemma 7.2, \(\mathbf a(u)=-u\), i.e. \(P^{-1}(-P(u))=-u\). Apply \(P\):
\(-P(u)=P(-u)\), i.e.
\[
P(-u)=-x .
\]
(CERT:576.) Since \(-u\in Y_0\subseteq Y\) (Claim 6.3.7(3)), Lemma 6.1(5)
gives \((P(-u),-u)=(-x,-u)\in Z\). \(\square\)

*Remark.* This can also be read off Lemma 6.2(1) applied twice, but the direct
route above uses only \(\tau u=u\) and is shorter.

## Lemma 7.5 (O7.5) — the four zero-set-localization identities

**[inputs: the localization receipt CZS:82–111, quoted below — CONSUMED ONCE,
at \((x,u)\) (v0.2, R5); CZS:49 (\(p=b^2/g\)); CZS:79; CZS:87; Claim 6.3.2;
Lemma 7.4]**
**[quantifier: pointwise on \(F^\ast\)]**

### The localization receipt, stated precisely and quoted verbatim

**Document:** `CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md`, a **PROMOTED
component of Theorem (N)** (CZS:4).
**Section:** §5, "Full transport remainder and zero-set localization"
(CZS:82).
**Displays consumed** — CZS:84–111 verbatim:

> Define
>
> \[A(x)=\sqrt{p(x)g(-x)},\qquad B(u)=\sqrt{g(u)p(-u)}=A(-u),\]
>
> \[h(x,u)=S-d(x,u),\qquad R_0(x,u)=h(x,u)-A(x)-B(u).\]
>
> The two Bellman inequalities and Cauchy–Schwarz give `R_0>=0`.
> If `R_0(x,u)=0`, then both Bellman inequalities and Cauchy are equalities and
>
> \[K(x)K(u)=1.\]
>
> Since `K>=1`,
>
> \[\boxed{K(x)=K(u)=1,}\]
>
> and in particular
>
> \[p(x)=g(-x),\qquad p(-u)=g(u).\]

together with CZS:78–80:

> \[\boxed{K(t):=\frac{g(t)g(-t)}{b(t)^2}\ge1\quad(t\in(-1,1)).}\]

**Statement.** For every \(u\in F^\ast\), with \(x=P(u)\) and
\(\rho=r_A(x)=r_B(u)\):
\[
g(-x)=\rho\,b(x),\qquad g(x)=\frac{b(x)}{\rho},\qquad
g(u)=\rho\,b(u),\qquad g(-u)=\frac{b(u)}{\rho}.
\tag{L1--L4}
\]
Moreover \(A(x)=g(-x)\), \(B(u)=g(u)\), \(A(-x)=g(x)\), \(B(-u)=g(-u)\).

**Proof.** All four points \(x,-x,u,-u\) lie in \((-1,1)\) (Lemma 6.1,
Claim 6.3.7(4)), so \(g>0\), \(b>0\), \(p>0\) at each of them.

*Step 1 — apply the receipt at the pair \((x,u)\).* By Lemma 7.4,
\(R_0(x,u)=0\). The receipt (CZS:101–111) gives
\[
K(x)=K(u)=1,\qquad p(x)=g(-x),\qquad p(-u)=g(u).
\tag{7.5.1}
\]

*Step 2 — the reflected identities, from (7.5.1) alone — SIMPLIFIED IN v0.2
(R5, adversary attack 6).* v0.1 applied the localization receipt a **second**
time, at the pair \((-x,-u)\), and claimed in a parenthetical that "the
\(p\)-halves are genuinely new". **That parenthetical was false and is
deleted:** the reflected \(p\)-identities follow from \(K(x)=K(u)=1\) and the
definition \(p=b^2/g\) (CZS:49) with no second application of the receipt.
Explicitly, using \(b(-t)=b(t)\) and \(K(x)=1\), i.e. \(g(x)g(-x)=b(x)^2\)
(CZS:79):
\[
p(-x)=\frac{b(-x)^2}{g(-x)}=\frac{b(x)^2}{g(-x)}
=\frac{g(x)g(-x)}{g(-x)}=g(x),
\]
and identically from \(K(u)=1\), i.e. \(g(u)g(-u)=b(u)^2\):
\[
p(u)=\frac{b(u)^2}{g(u)}=\frac{g(u)g(-u)}{g(u)}=g(-u).
\]
So
\[
K(-x)=K(-u)=1,\qquad p(-x)=g(x),\qquad p(u)=g(-u),
\tag{7.5.2}
\]
where the \(K\)-halves are literally the \(K\)-halves of (7.5.1), since
\(K(-t)=K(t)\) identically (CZS:79 with \(b(-t)=b(t)\)). **The localization
receipt is therefore consumed exactly once, at \((x,u)\).**

*(**Lemma 7.4 is still needed**, and this is not a saving there: the second
full-zero membership \((-x,-u)\in Z\) is what supplies \(R_0(-x,-u)=0\), hence
the second Bellman equality (7.6.2) in Lemma 7.6. What Step 2 no longer needs is
a second *invocation of the localization receipt* at that pair.)*

*Step 3 — evaluate \(A\) and \(B\).* Using CZS:87 and (7.5.1):
\[
A(x)=\sqrt{p(x)g(-x)}=\sqrt{g(-x)^2}=g(-x),\qquad
B(u)=\sqrt{g(u)p(-u)}=\sqrt{g(u)^2}=g(u),
\]
(positive square roots of squares of positive numbers). Using (7.5.2):
\[
A(-x)=\sqrt{p(-x)g(x)}=\sqrt{g(x)^2}=g(x),\qquad
B(-u)=\sqrt{g(-u)p(u)}=\sqrt{g(-u)^2}=g(-u).
\]

*Step 4 — the four identities.* From \(\rho=r_A(x)=A(x)/b(x)\) (CERT:401) and
Step 3:
\[
\rho=\frac{g(-x)}{b(x)}\ \Longrightarrow\ \boxed{g(-x)=\rho\,b(x)}\quad(L1).
\]
From \(K(x)=1\), i.e. \(g(x)g(-x)=b(x)^2\) (CZS:79), and (L1):
\[
g(x)=\frac{b(x)^2}{g(-x)}=\frac{b(x)^2}{\rho\,b(x)}
=\boxed{\frac{b(x)}{\rho}}\quad(L2).
\]
From \(\rho=r_B(u)=B(u)/b(u)\) (CERT:413) and Step 3:
\[
\rho=\frac{g(u)}{b(u)}\ \Longrightarrow\ \boxed{g(u)=\rho\,b(u)}\quad(L3).
\]
From \(K(u)=1\), i.e. \(g(u)g(-u)=b(u)^2\), and (L3):
\[
g(-u)=\frac{b(u)^2}{g(u)}=\frac{b(u)^2}{\rho\,b(u)}
=\boxed{\frac{b(u)}{\rho}}\quad(L4).
\]
These are exactly CERT:582–592. \(\square\)

**Consistency check (not needed, but it pins the receipt).** *(v0.2, m8: this
paragraph's first sentence broke off mid-formula in v0.1 and is completed
here.)* There are two routes to \(\rho\), and they must agree. The first is
(L1): \(r_A(x)=A(x)/b(x)=g(-x)/b(x)=\rho\). The second goes through \(p\): by
(7.5.1), \(p(x)=g(-x)=A(x)\), so
\[
r_A(x)=\frac{A(x)}{b(x)}=\frac{p(x)}{b(x)}=\frac{b(x)^2/g(x)}{b(x)}
=\frac{b(x)}{g(x)}
\overset{\text{(L2)}}{=}\frac{b(x)}{b(x)/\rho}=\rho .
\]
The two routes agree, which is exactly the content of \(K(x)=1\).

## Lemma 7.6 (O7.6) — THE ELIMINATION, Lean-anchored

**[inputs: Lemma 7.5 (L1–L4); CZS:34 (\(d\)); CZS:91 (\(R_0=0\Rightarrow
h=A+B\)); Claim 6.3.2 (\(\rho>0\)); CERT:229 (\(b>0\) interior);
QC:77–90 `quarter_ceiling`; QC:95–97 `quarter_lt_window_lower`; CERT:24–28
(the window); FR:196–208 (Receipt (iv), \(S>1/4\))]**
**[quantifier: pointwise on \(F^\ast\) — the conclusion is a contradiction at a
single point]**

**Statement.** \(F^\ast=\varnothing\).

**Notation dictionary (avoiding the collision flagged in §0.1).** The
commission writes \(A:=S-xu+1\), \(\delta:=(x-u)/2\), \(B:=b(x)+b(u)\). Since
\(A(\cdot)\) and \(B(\cdot)\) are already taken, this document writes
\[
\Sigma:=S-xu+1\ \ (\text{commission's }A),\qquad
\delta:=\frac{x-u}{2},\qquad
\Lambda:=b(x)+b(u)\ \ (\text{commission's }B).
\]

**Proof.** Suppose \(u\in F^\ast\); put \(x=P(u)\), \(\rho=r_A(x)=r_B(u)\).

*Step 1 — the two Bellman equalities.* By Lemma 7.4, \(R_0(x,u)=0\) and
\(R_0(-x,-u)=0\). By CZS:91, \(R_0=h-A-B\) with \(h(x,u)=S-d(x,u)\). Hence,
using the evaluations of Lemma 7.5 Step 3 and then (L1)–(L4):
\[
S-d(x,u)=A(x)+B(u)=g(-x)+g(u)=\rho\,b(x)+\rho\,b(u)
=\rho\bigl(b(x)+b(u)\bigr)=\rho\Lambda,
\tag{7.6.1}
\]
\[
S-d(-x,-u)=A(-x)+B(-u)=g(x)+g(-u)=\frac{b(x)}{\rho}+\frac{b(u)}{\rho}
=\frac{b(x)+b(u)}{\rho}=\frac{\Lambda}{\rho}.
\tag{7.6.2}
\]
These are CERT:596–602.

*Step 2 — the two \(d\)-values.* By CZS:34, \(d(i,j)=ij+\frac{i-j}{2}-1\), so
\[
d(x,u)=xu+\frac{x-u}{2}-1,\qquad
d(-x,-u)=xu+\frac{-x+u}{2}-1=xu-\frac{x-u}{2}-1 .
\]
Therefore
\[
d(x,u)+d(-x,-u)=2xu-2,\qquad d(x,u)-d(-x,-u)=x-u,
\]
and
\[
S-d(x,u)=\Sigma-\delta,\qquad S-d(-x,-u)=\Sigma+\delta,
\]
with \(\Sigma=S-xu+1\) and \(\delta=(x-u)/2\) as declared.

*Step 3 — the system.* (7.6.1)–(7.6.2) become
\[
\Sigma-\delta=\rho\Lambda,\qquad \Sigma+\delta=\frac{\Lambda}{\rho}.
\tag{7.6.3}
\]

*Step 4 — the positivity checks the commission demands.* \(x,u\in(-1,1)\), so
\(b(x)>0\) and \(b(u)>0\) (CERT:229), hence \(\Lambda>0\). By Claim 6.3.2,
\(\rho\in(0,\infty)\). Hence \(\rho\Lambda>0\) and \(\Lambda/\rho>0\), so both
\(\Sigma-\delta>0\) and \(\Sigma+\delta>0\); adding,
\(\Sigma>0\) — which also follows directly from
\(\Sigma=S+(1-xu)\) with \(S>0\) and \(|xu|<1\).

*Step 5 — MULTIPLY to eliminate \(\rho\).* This is the step for which
\(\rho\ne0\) is required (Step 4). Multiplying the two equations of (7.6.3):
\[
(\Sigma-\delta)(\Sigma+\delta)=\rho\Lambda\cdot\frac{\Lambda}{\rho}=\Lambda^2,
\]
i.e.
\[
\Sigma^2-\delta^2=\Lambda^2,\qquad\text{so}\qquad \Sigma^2=\Lambda^2+\delta^2 .
\]
Since \(\Sigma>0\) (Step 4), taking the positive square root,
\[
\Sigma=\sqrt{\Lambda^2+\delta^2}.
\]
Unwinding \(\Sigma=S-xu+1\), \(\Lambda=b(x)+b(u)\), \(\delta=(x-u)/2\):
\[
\boxed{\ S=xu-1+\sqrt{\bigl(b(x)+b(u)\bigr)^{2}+\frac{(x-u)^{2}}{4}}\ }
\tag{7.6.4}
\]

*Step 6 — the machine-checked ceiling.* The Lean kernel theorem, quoted
verbatim from QC:75–90:

```lean
/-- (e): the quarter ceiling — the paper's displayed conclusion.
    Any closed strategy value is capped at 1/4. -/
theorem quarter_ceiling (hx : x ^ 2 ≤ 1) (hu : u ^ 2 ≤ 1) :
    x * u - 1
      + Real.sqrt
          ((Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
            + (x - u) ^ 2 / 4)
    ≤ 1 / 4 := by
  set E := (Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
    + (x - u) ^ 2 / 4 with hE
  have hEt : E ≤ 1 - x * u := amplitude_le hx hu
  have ht : (0 : ℝ) ≤ 1 - x * u := by nlinarith
  have hsqrt : Real.sqrt E ≤ Real.sqrt (1 - x * u) := Real.sqrt_le_sqrt hEt
  have hceil : -(1 - x * u) + Real.sqrt (1 - x * u) ≤ 1 / 4 :=
    scalar_quarter_ceiling ht
  linarith
```

**Hypotheses:** exactly `hx : x ^ 2 ≤ 1` and `hu : u ^ 2 ≤ 1`, on real
variables `{x u : ℝ}` (QC:28). **Hypothesis discharge:** our \(x=P(u)\in(-1,1)\)
and \(u\in(-1,1)\) (Lemma 6.1, Claim 6.3.7(4)), so \(x^2<1\le1\) and
\(u^2<1\le1\); the labels are interior, and interiority is *strictly stronger*
than what the theorem needs. **Term match:** the Lean expression
`Real.sqrt (1 - x^2)/2` is exactly \(b(x)\) (CERT:229), and
`Real.sqrt (1 - u^2)/2` is \(b(u)\); so the Lean conclusion reads
\[
xu-1+\sqrt{\bigl(b(x)+b(u)\bigr)^2+\frac{(x-u)^2}{4}}\ \le\ \frac14 .
\]
Combining with (7.6.4):
\[
S\le\frac14 .
\tag{7.6.5}
\]

*Step 7 — the contradiction, with honest scope.* CERT:24–28 certifies
\[
S\in(0.2508753845015185,\ 0.250875388108398],
\]
and QC:95–97 machine-checks
```lean
theorem quarter_lt_window_lower :
    (1 : ℚ) / 4 < 2508753845015185 / 10 ^ 16 := by
  norm_num
```
i.e. \(\tfrac14<0.2508753845015185<S\). Independently, FR:196–208 (Receipt
(iv)) certifies \(S>1/4\) from the Sprint-1292 exact dimension-255 strategy.
Either route contradicts (7.6.5). Hence no \(u\in F^\ast\) exists:
\(F^\ast=\varnothing\). \(\square\)

**Honest-scope note (as in the rate note).** `quarter_ceiling` is the
**algebraic core only**; QC:16–19 states its claim boundary explicitly:

> CLAIM BOUNDARY: this is the algebraic core only. The reduction of a
> finite-dimensional maximizer to this two-variable form (kernel
> equations, W-operator anticommutation, the closure step) is NOT
> formalized here.

The reduction *in this document* is Steps 1–5 above, which are hand-verified
and consume only Lemma 7.5, CZS:34, CZS:91 and \(\rho>0\). Steps 1–5 replace
the certificate's prose "The audited Sprint-1198 elimination then gives
\(S\le\frac14\)" (CERT:604–608), which cited no display. **This is the
expansion's centrepiece: a one-line prose appeal has become five checkable
steps ending in a machine-checked inequality.**

## Lemma 7.7 (O7.7) — \(\mu_U(F)=0\)

**[inputs: Lemma 7.3 (the named null set \(N_1\)); Lemma 7.6]**
**[quantifier: \(\mu_U\)-a.e. hypothesis \(\to\) pointwise existence \(\to\)
contradiction]**

**Statement.** \(\mu_U(F)=0\).

**Proof.** Suppose \(\mu_U(F)>0\). The conull conditions in play are exactly
**one** in number:

- \(C_1:=\{u\in F:r_A(P(u))=r_B(u)\}\), with \(\mu_U(F\setminus C_1)=0\)
  by Lemma 7.3.

*(Everything else used in Lemmas 7.4–7.6 — membership \(u\in Y_0\), \(x=P(u)\)
defined, \(-u\in Y_0\), \(P(-u)=-x\), \(R_0(x,u)=R_0(-x,-u)=0\), the four
localization identities, \(\rho\in(0,\infty)\), \(x,u\in(-1,1)\) — is
**pointwise on \(F\)**, by Lemmas 6.1, 6.3, 7.2, 7.4, 7.5 and Claim 6.3.2. This
is why the a.e.-to-existence step needs only a single intersection — it is
**consumer 3 of Claim 6.3.2** in the list recorded after that claim's proof, and
one of the exactly three places its pointwise form is load-bearing.)*

Then \(\mu_U(C_1)=\mu_U(F)-\mu_U(F\setminus C_1)=\mu_U(F)>0\). A set of
strictly positive measure is non-empty. **Choose a point \(u\in C_1=F^\ast\).**
This is the a.e.-to-existence step written explicitly: an almost-everywhere
identity on a positive-measure set yields an actual point at which the
identity, and every pointwise fact, hold simultaneously.

But \(F^\ast=\varnothing\) by Lemma 7.6 — contradiction. Hence
\(\mu_U(F)=0\). \(\square\)

*(CERT:614–620: "This nullity, not emptiness of \(F\), is the statement
consumed below." Lemma 7.6 does show \(F^\ast=\varnothing\), i.e. \(F\) minus a
null set is empty, which is the same content as \(\mu_U(F)=0\); \(F\) itself may
be non-empty, consisting entirely of points of \(N_1\).)*

**Standing domain from here on.**
\[
Y_1:=Y_0\setminus F,\qquad \mu_U(Y_1)=1,
\]
Borel, and invariant under \(\mathbf a,\mathbf b,\tau\) (Lemma 7.1 gives
\(F\) invariant; \(Y_0\) is invariant by Claim 6.3.7(3)).

---

# §8 — A Borel transversal for the open response orbits

Throughout §8, all statements are **pointwise on \(Y_1=Y_0\setminus F\)**
unless labelled otherwise. For \(u\in Y_1\) write
\[
\mathcal O_{\mathbb Z}(u):=\{\tau^n(u):n\in\mathbb Z\},\qquad
\mathcal O_{G}(u):=\{w(u):w\in G\},
\]
the \(\mathbb Z\)-orbit and the full response (dihedral) orbit. Since
\(G=\langle\mathbf a,\mathbf b\rangle\) with \(\mathbf a^2=\mathbf b^2=1\) and
\(\tau=\mathbf a\mathbf b\), every element of \(G\) is \(\tau^n\) or
\(\tau^n\mathbf b\); hence
\[
\mathcal O_G(u)=\mathcal O_{\mathbb Z}(u)\cup\mathcal O_{\mathbb Z}(\mathbf b(u)).
\tag{8.0.1}
\]

## Lemma 8.1 (O8.1) — \(Y_\pm\) are Borel, invariant unions of \(\mathbb Z\)-orbits

**[inputs: Lemma 6.4; Lemma 7.7]**
**[quantifier: pointwise on \(Y_1\)]**

**Statement.** Put \(Y_+=\{u\in Y_1:\tau(u)>u\}\),
\(Y_-=\{u\in Y_1:\tau(u)<u\}\). Then \(Y_+\), \(Y_-\) are Borel,
\(Y_1=Y_+\sqcup Y_-\), and each is \(\tau\)-invariant in both directions:
\(\tau(Y_\pm)=Y_\pm\).

**Proof.** *Borel and partition:* \(\tau\) is Borel, so \(Y_\pm\) are Borel;
and \(u\in Y_1\) means \(\tau(u)\ne u\), so exactly one of \(\tau(u)>u\),
\(\tau(u)<u\) holds.

*Invariance.* Let \(u\in Y_+\), so \(\tau(u)>u\). Applying the strictly
increasing \(\tau\) (Lemma 6.4): \(\tau(\tau(u))>\tau(u)\), so
\(\tau(u)\in Y_+\). Applying the strictly increasing \(\tau^{-1}\) to
\(\tau(u)>u\): \(u>\tau^{-1}(u)\), i.e.
\(\tau(\tau^{-1}(u))=u>\tau^{-1}(u)\), so \(\tau^{-1}(u)\in Y_+\). Hence
\(\tau(Y_+)=Y_+\), and \(Y_+\) is a union of \(\mathbb Z\)-orbits. Same for
\(Y_-\). \(\square\)

**Caution.** \(Y_\pm\) are unions of **\(\mathbb Z\)-orbits**, not of full
response orbits — see Correction 8.5.A.

## Lemma 8.2 (O8.2) — \(\alpha,\beta,\theta\) are Borel and orbit-constant; strict monotonicity of \(n\mapsto\tau^n(u)\)

*(**v0.2, R9 — symbol change.** v0.1 wrote this lemma's rational selector as
\(q(u)\), following CERT:644–650, and thereby **reproduced inside this document**
the CERT collision between \(q_n\downarrow S\) (CERT:59, used in Claim 0.1) and
the rational enumeration \(q_k\) (CERT:644). The selector is renamed
\(\theta\) throughout §8: \(\theta_1,\theta_2,\dots\) enumerates \(\mathbb Q\)
and \(\theta(u)\) is the selected rational. Dictionary to the certificate:
\(\theta_k=q_k\) of CERT:644, \(\theta(u)=q(u)\) of CERT:650. Nothing
mathematical changes.)*

**[inputs: Lemmas 6.4, 8.1]**
**[quantifier: pointwise on \(Y_+\)]**

**Statement.** For \(u\in Y_+\):

1. \(n\mapsto\tau^n(u)\) is strictly increasing on \(\mathbb Z\);
2. \(\alpha(u):=\inf_{n\in\mathbb Z}\tau^n(u)\) and
   \(\beta(u):=\sup_{n\in\mathbb Z}\tau^n(u)\) are Borel functions
   \(Y_+\to[-1,1]\), constant on each \(\mathbb Z\)-orbit, with
   \(\alpha(u)<u<\beta(u)\);
3. \(\theta(u):=\theta_{k(u)}\), where \(\theta_1,\theta_2,\dots\) is a fixed
   enumeration of \(\mathbb Q\) and
   \(k(u):=\min\{k:\alpha(u)<\theta_k<\beta(u)\}\), is well-defined, Borel, and
   constant on each \(\mathbb Z\)-orbit.

**Proof.**

*(1).* By Lemma 8.1 every \(\tau^n(u)\in Y_+\). Fix \(n\); then
\(\tau^{n+1}(u)=\tau(\tau^n(u))>\tau^n(u)\) since \(\tau^n(u)\in Y_+\). So the
sequence is strictly increasing in \(n\).

*(2).* Each \(u\mapsto\tau^n(u)\) is Borel; a countable infimum/supremum of
Borel functions is Borel. Values lie in \([-1,1]\) because
\(Y_+\subseteq(-1,1)\). Orbit-constancy:
\(\alpha(\tau(u))=\inf_n\tau^{n+1}(u)=\inf_m\tau^m(u)=\alpha(u)\), and
likewise for \(\beta\); by induction, constant on the whole
\(\mathbb Z\)-orbit. Strictness: by (1), \(\tau^{-1}(u)<u=\tau^0(u)<\tau(u)\),
so \(\alpha(u)\le\tau^{-1}(u)<u\) and \(\beta(u)\ge\tau(u)>u\).

*(3).* *Well-defined:* \(\alpha(u)<\beta(u)\) by (2), so the open interval
\((\alpha(u),\beta(u))\) is non-empty and contains a rational; hence the index
set is non-empty and has a minimum. *Borel:* for each \(k\),
\[
\{u\in Y_+:k(u)=k\}
=\Bigl(\bigcap_{j<k}\bigl(\{\alpha\ge\theta_j\}\cup\{\beta\le\theta_j\}\bigr)
\Bigr)
\cap\{\alpha<\theta_k\}\cap\{\beta>\theta_k\},
\]
a finite Boolean combination of Borel sets, hence Borel. \(\theta\) is constant
with value \(\theta_k\) on this Borel piece, so \(\theta\) is Borel.
**[standard: countable first-rational selection; reason: the selection is a
minimum over a countable index set of Borel conditions, so each level set is
Borel.]**
*Orbit-constant:* \(k(u)\) depends only on \((\alpha(u),\beta(u))\), which is
orbit-constant by (2). \(\square\)

## Lemma 8.3 (O8.3) — \(D_+\) meets each increasing \(\mathbb Z\)-orbit exactly once

**[inputs: Lemma 8.2]**
**[quantifier: pointwise — existence and uniqueness for every
\(\mathbb Z\)-orbit in \(Y_+\)]**

**Statement.** Put \(D_+:=\{u\in Y_+: u\le\theta(u)<\tau(u)\}\)
(CERT:654–657). \(D_+\) is Borel, and for every \(u_\bullet\in Y_+\) the set
\(\mathcal O_{\mathbb Z}(u_\bullet)\cap D_+\) is a singleton.

**Proof.** *Borel:* \(\theta\) and \(\tau\) are Borel, so \(D_+\) is Borel.

Fix \(u_\bullet\in Y_+\) and write \(v_n:=\tau^n(u_\bullet)\),
\(\theta:=\theta(u_\bullet)\) (constant along the orbit, Lemma 8.2(3)),
\(\alpha:=\alpha(u_\bullet)\), \(\beta:=\beta(u_\bullet)\), so
\(\alpha<\theta<\beta\) and \(n\mapsto v_n\) is strictly increasing with
\(\inf_n v_n=\alpha\), \(\sup_n v_n=\beta\).

Note that for a point \(v_n\) of the orbit, the defining condition of \(D_+\)
reads \(v_n\le\theta<v_{n+1}\) (since \(\theta(v_n)=\theta\) and
\(\tau(v_n)=v_{n+1}\)).

*Existence.* Let \(I:=\{n\in\mathbb Z:v_n\le\theta\}\).
- \(I\ne\varnothing\): \(\inf_n v_n=\alpha<\theta\), so by definition of
  infimum there is \(n\) with \(v_n<\theta\), hence \(n\in I\).
- \(I\) is bounded above: \(\sup_n v_n=\beta>\theta\), so there is \(m\) with
  \(v_m>\theta\); by strict monotonicity \(v_n\ge v_m>\theta\) for all
  \(n\ge m\), so \(I\subseteq\{n:n<m\}\).

A non-empty subset of \(\mathbb Z\) bounded above has a maximum; let
\(n_0:=\max I\). Then \(v_{n_0}\le\theta\) and \(v_{n_0+1}>\theta\), i.e.
\(v_{n_0}\le\theta<v_{n_0+1}\), so \(v_{n_0}\in D_+\).

*Uniqueness.* Suppose \(v_n,v_m\in D_+\) with \(n<m\). From \(v_n\in D_+\),
\(\theta<v_{n+1}\); from \(m\ge n+1\) and strict monotonicity,
\(v_m\ge v_{n+1}>\theta\). But \(v_m\in D_+\) requires \(v_m\le\theta\) —
contradiction. Hence \(n=m\). \(\square\)

### Note 8.3.A — why the non-strict \(\le\) is load-bearing here (v0.2, R4)

*(Added on the round-1 adversary's attack A1-ii, which probed \(D_+\) for
missing or double-hitting an orbit and found no countermodel but a **latent
hazard the document had not flagged**.)*

The selected rational \(\theta(u)\) is chosen from the open interval
\((\alpha(u),\beta(u))\), and **nothing prevents it from being an orbit point**:
\(\theta(u)=v_n\) for some \(n\) is entirely possible — the orbit
\(\{v_n\}\) may consist of rationals, and \(\theta\) is only required to be the
first rational strictly between the infimum and the supremum, not to avoid the
orbit. (Example: \(Y_0=\mathbb R\), \(\tau(u)=u+1\); every orbit is a coset of
\(\mathbb Z\) and \(\alpha=-\infty\), \(\beta=+\infty\), so \(\theta\) is the
first rational in the enumeration, which lies on the orbit of any point
congruent to it mod \(1\).)

In that case the defining condition \(v_n\le\theta<v_{n+1}\) is satisfied with
**equality on the left**: the selected representative is \(v_n=\theta\) itself.
Consequently:

- With the non-strict \(\le\) as written, existence still holds — the maximum of
  \(I=\{n:v_n\le\theta\}\) exists and is attained at \(n\) with
  \(v_n=\theta\).
- **With a strict \(<\) in place of \(\le\)**, i.e. with
  \(D_+':=\{u\in Y_+:u<\theta(u)<\tau(u)\}\), such an orbit would be **missed
  entirely**: no point of it satisfies \(v_n<\theta<v_{n+1}\), because the only
  candidate index has \(v_n=\theta\). \(D_+'\) would then fail to be a
  transversal, and Lemmas 8.4–8.6 would collapse.

So the \(\le\) is not a stylistic choice; it is what makes \(D_+\) meet
*every* increasing orbit. Uniqueness is unaffected: the argument above uses only
\(\theta<v_{n+1}\) and strict monotonicity, both of which survive the equality
case. (This is a *different* role for a non-strict inequality from the one in
Lemma 8.5(4), where \(\le\) is what admits the degenerate case (a); both are
recorded because they are the two places a reader is tempted to "tighten" the
statement and would break it.)

## Lemma 8.4 (O8.4) — the mirror construction on \(Y_-\), and the \(\mathbb Z\)-transversal

**[inputs: Lemmas 8.1–8.3 applied to \(\tau^{-1}\)]**
**[quantifier: pointwise on \(Y_1\)]**

**Statement.** \(Y_-\) is exactly the set where \(\tau^{-1}\) increases:
\(Y_-=\{u\in Y_1:\tau^{-1}(u)>u\}\). Applying Lemmas 8.2–8.3 verbatim with
\(\tau^{-1}\) in place of \(\tau\) yields a Borel set \(D_-\subseteq Y_-\)
meeting each \(\mathbb Z\)-orbit in \(Y_-\) exactly once. Consequently
\[
D:=D_+\sqcup D_-
\]
is a Borel transversal for the \(\mathbb Z\)-action of \(\tau\) on \(Y_1\):
every \(\mathbb Z\)-orbit meets \(D\) in exactly one point.

**Proof.** If \(u\in Y_-\), \(\tau(u)<u\); applying the strictly increasing
\(\tau^{-1}\) gives \(u<\tau^{-1}(u)\). Conversely if \(\tau^{-1}(u)>u\) then
\(u>\tau(u)\). So \(Y_-\) is the "\(\tau^{-1}\)-increasing" set.

\(\tau^{-1}=\mathbf b\mathbf a\) is a strictly increasing Borel bijection of
\(Y_1\) (Lemma 6.4) with the same orbits as \(\tau\)
(\(\{(\tau^{-1})^n(u)\}=\{\tau^{-n}(u)\}=\mathcal O_{\mathbb Z}(u)\)), and it is
fixed-point-free on \(Y_1\) (if \(\tau^{-1}(u)=u\) then \(\tau(u)=u\)). Hence
every hypothesis of Lemmas 8.2 and 8.3 holds with \(\tau\) replaced by
\(\tau^{-1}\) and \(Y_+\) replaced by \(Y_-\), and the conclusions transfer
verbatim, producing \(D_-\).

Since \(Y_1=Y_+\sqcup Y_-\) (Lemma 8.1) and each \(\mathbb Z\)-orbit lies
entirely in \(Y_+\) or entirely in \(Y_-\) (Lemma 8.1 invariance), each orbit
meets exactly one of \(D_+,D_-\), in exactly one point. \(\square\)

**Note 8.4.A (v0.2, R4).** Because \(D_-\) is produced by applying Lemma 8.3
*verbatim* to \(\tau^{-1}\), **Note 8.3.A transfers verbatim as well**: the
selected rational may be an orbit point of a decreasing orbit, and the
non-strict \(\le\) in \(D_-=\{u\in Y_-:u\le\theta(u)<\tau^{-1}(u)\}\) is what
keeps that orbit from being missed. The transversal property of
\(D=D_+\sqcup D_-\) therefore rests on the non-strict inequality on **both**
halves.

Write \(\pi_{\mathbb Z}:Y_1\to D\) for the map sending \(u\) to the unique
point of \(\mathcal O_{\mathbb Z}(u)\cap D\).

**Claim 8.4.1.** \(\pi_{\mathbb Z}\) is Borel, \(\pi_{\mathbb Z}|_D=\mathrm{id}\),
and \(\pi_{\mathbb Z}\circ\tau=\pi_{\mathbb Z}\).

*Proof.* For \(u\in Y_1\) there is a unique \(n(u)\in\mathbb Z\) with
\(\tau^{n(u)}(u)\in D\) (Lemma 8.4), and
\(\{u:n(u)=n\}=\tau^{-n}(D)\cap Y_1\) is Borel. On that piece
\(\pi_{\mathbb Z}=\tau^n\), a Borel map. A function that is Borel on each of
countably many Borel pieces partitioning its domain is Borel. The last two
properties are immediate from uniqueness. \(\square\)

## Lemma 8.5 (O8.5) — \(\mathbf b\tau\mathbf b=\tau^{-1}\); the induced involution on \(D\); the full dihedral transversal

**[inputs: Lemma 7.1 (7.1.1); Lemmas 8.1–8.4; Claim 8.4.1]**
**[quantifier: pointwise on \(Y_1\) / on \(D\)]**

**Statement.**

1. \(\mathbf b\tau\mathbf b=\tau^{-1}\) on \(Y_1\), hence
   \(\mathbf b\,\tau^n\,\mathbf b=\tau^{-n}\) for all \(n\in\mathbb Z\), and
   \(\mathbf b\) maps \(\mathbb Z\)-orbits onto \(\mathbb Z\)-orbits, reversing
   the \(\mathbb Z\)-parametrisation.
2. \(\iota:=\pi_{\mathbb Z}\circ\mathbf b|_D:D\to D\) is a Borel involution.
3. **Casework.** For \(d\in D\), exactly one of:
   (a) \(\mathcal O_{\mathbb Z}(d)\) is \(\mathbf b\)-invariant, in which case
   \(\iota(d)=d\) and \(\mathcal O_G(d)=\mathcal O_{\mathbb Z}(d)\);
   (b) \(\mathcal O_{\mathbb Z}(d)\) is not \(\mathbf b\)-invariant, in which
   case \(\iota(d)\ne d\), \(\mathcal O_{\mathbb Z}(d)\) and
   \(\mathcal O_{\mathbb Z}(\mathbf b(d))\) are **disjoint**, and
   \(\mathcal O_G(d)\) is their disjoint union.
4. \(T:=\{d\in D:d\le\iota(d)\}\) is Borel and meets every full response orbit
   in \(Y_1\) in **exactly one** point. \(T\) is a Borel transversal for the
   infinite-dihedral response relation.

**Proof.**

*(1).* (7.1.1) gives \(\mathbf b\tau\mathbf b=\tau^{-1}\). Conjugation is a
group homomorphism, so \(\mathbf b\tau^n\mathbf b=(\mathbf b\tau\mathbf b)^n
=\tau^{-n}\). Hence
\(\mathbf b(\tau^n(u))=\tau^{-n}(\mathbf b(u))\), so
\(\mathbf b(\mathcal O_{\mathbb Z}(u))=\mathcal O_{\mathbb Z}(\mathbf b(u))\),
with the index reversed.

*(2).* \(\mathbf b\) and \(\pi_{\mathbb Z}\) are Borel, so \(\iota\) is Borel,
and \(\iota(d)\in D\). Involutivity: write \(\iota(d)=\tau^{k}(\mathbf b(d))\)
for the unique \(k\) with \(\tau^k(\mathbf b(d))\in D\). Then by (1),
\[
\mathbf b(\iota(d))=\mathbf b\bigl(\tau^{k}(\mathbf b(d))\bigr)
=\tau^{-k}\bigl(\mathbf b(\mathbf b(d))\bigr)=\tau^{-k}(d)
\in\mathcal O_{\mathbb Z}(d),
\]
so \(\iota(\iota(d))=\pi_{\mathbb Z}(\mathbf b(\iota(d)))
=\pi_{\mathbb Z}(\tau^{-k}(d))=\pi_{\mathbb Z}(d)=d\) (Claim 8.4.1).

*(3) — the casework the commission asks for, both cases.*
The question "can a \(\mathbb Z\)-orbit be \(\mathbf b\)-invariant?" has answer
**yes, and it must be handled**, because two distinct \(\mathbb Z\)-orbits are
either equal or disjoint.

- (a) Suppose \(\mathbf b(\mathcal O_{\mathbb Z}(d))=\mathcal O_{\mathbb Z}(d)\).
  Then \(\mathbf b(d)\in\mathcal O_{\mathbb Z}(d)\), so
  \(\iota(d)=\pi_{\mathbb Z}(\mathbf b(d))=\pi_{\mathbb Z}(d)=d\). By (8.0.1),
  \(\mathcal O_G(d)=\mathcal O_{\mathbb Z}(d)\cup
  \mathcal O_{\mathbb Z}(\mathbf b(d))=\mathcal O_{\mathbb Z}(d)\).
- (b) Otherwise \(\mathbf b(d)\notin\mathcal O_{\mathbb Z}(d)\) (if it were,
  case (a) would apply by (1)); \(\mathbb Z\)-orbits being the classes of an
  equivalence relation, \(\mathcal O_{\mathbb Z}(d)\) and
  \(\mathcal O_{\mathbb Z}(\mathbf b(d))\) are disjoint. Their transversal
  points \(d\) and \(\iota(d)\) lie in different orbits, hence
  \(\iota(d)\ne d\). By (8.0.1) \(\mathcal O_G(d)\) is their disjoint union.

*(4).* \(T\) is Borel since \(\iota\) is Borel and \(\le\) is a closed
relation on \(\mathbb R^2\).

*Existence and uniqueness of the \(T\)-point in a full orbit.* Let
\(u\in Y_1\) and \(d:=\pi_{\mathbb Z}(u)\). By (8.0.1) and Lemma 8.4, the points
of \(\mathcal O_G(u)\) lying in \(D\) are exactly \(d\) and \(\iota(d)\) (the
\(D\)-points of the at most two \(\mathbb Z\)-orbits composing
\(\mathcal O_G(u)\)).

- In case (a), \(d=\iota(d)\), so \(\mathcal O_G(u)\cap D=\{d\}\) and
  \(d\le\iota(d)=d\), so \(d\in T\): exactly one \(T\)-point.
- In case (b), \(d\ne\iota(d)\) are two **distinct real numbers**, so exactly
  one of \(d<\iota(d)\), \(\iota(d)<d\) holds. Since \(\iota\) is an involution
  (part 2), \(\iota(\iota(d))=d\), so the two conditions "\(d\le\iota(d)\)" and
  "\(\iota(d)\le\iota(\iota(d))=d\)" are mutually exclusive and exhaustive.
  Exactly one of \(d,\iota(d)\) lies in \(T\): exactly one \(T\)-point.

*Well-definedness of "the lesser of its two representatives", spelled out as
O8.5 demands:* the pair \(\{d,\iota(d)\}\) is produced by the **Borel** map
\(d\mapsto(d,\iota(d))\) (part 2), and the choice "lesser" is the Borel
condition \(d\le\iota(d)\) — no choice principle is invoked, and in case (a)
the "pair" degenerates to a single point, which the non-strict \(\le\) admits.
Using \(<\) instead of \(\le\) would **lose** case (a) entirely; this is the
one place the degenerate case changes the formula. \(\square\)

### CORRECTION 8.5.A — the commission's "exchanging \(Y_+/Y_-\)" is false

O8.5 anticipates that "\(\mathbf b\) maps orbits to orbits **exchanging
\(Y_+/Y_-\)** ORBIT-WISE". This is **not** what happens; \(\mathbf b\)
**preserves** \(Y_+\) and \(Y_-\) setwise.

*Proof.* From (7.1.1), \(\tau\mathbf b=\mathbf b\tau^{-1}\). Let \(u\in Y_+\),
so \(\tau^{-1}(u)<u\). Since \(\mathbf b\) is strictly **decreasing** (Claim
6.3.8), \(\mathbf b(\tau^{-1}(u))>\mathbf b(u)\), i.e.
\(\tau(\mathbf b(u))>\mathbf b(u)\), i.e. \(\mathbf b(u)\in Y_+\). Symmetrically
\(\mathbf b(Y_-)\subseteq Y_-\). \(\square\)

*Model check.* Take \(Y_0=\mathbb R\), \(\tau(u)=u+1\), \(\mathbf b(u)=-u\),
\(\mathbf a(u)=1-u\) (both strictly decreasing involutions,
\(\mathbf a\mathbf b=\tau\), \(\mathbf b\tau\mathbf b=\tau^{-1}\)). Here
\(Y_+=\mathbb R\), \(Y_-=\varnothing\), and \(\mathbf b\) certainly does not
exchange them.

**Impact: none on the construction.** What \(\mathbf b\) actually does is
reverse the \(\mathbb Z\)-parametrisation *within* \(Y_+\) (part 1), which is
all Lemma 8.5(2)–(4) uses. The certificate text itself (CERT:665–673) claims
only "The reflection relation \(b\tau b=\tau^{-1}\) induces a Borel involution
on this transversal" — it does **not** claim the \(Y_\pm\) exchange. So the
error is in the commission's expectation, not in CERT; recorded here so the
blind gate does not chase it as a defect in the certificate.

## Lemma 8.6 (O8.6) — the orbit projection \(\pi:Y_1\to T\), constructed directly

**[inputs: Lemma 8.5; Claim 8.4.1]**
**[quantifier: pointwise on \(Y_1\)]**

**Statement.** Define \(\pi:Y_1\to T\) by
\[
\pi(u):=\min\bigl\{\pi_{\mathbb Z}(u),\ \iota(\pi_{\mathbb Z}(u))\bigr\}.
\]
Then:

1. \(\pi(u)\) is the unique point of \(\mathcal O_G(u)\cap T\);
2. \(\pi\) is Borel;
3. \(\pi\circ w=\pi\) for every \(w\in G\); in particular
   \(\pi\circ\mathbf a=\pi\circ\mathbf b=\pi\);
4. \(\pi|_T=\mathrm{id}_T\), and for \(t\in T\),
   \(\pi^{-1}(t)=\mathcal O_G(t)\), a **countable** set;
5. \(T\) is a Borel subset of \((-1,1)\), hence a standard Borel space, and
   \(T\) **is** the orbit quotient — no abstract quotient theory is used.

**Proof.**

*(1).* By Lemma 8.5(4), \(\mathcal O_G(u)\cap D=\{\pi_{\mathbb Z}(u),
\iota(\pi_{\mathbb Z}(u))\}\) (a one- or two-element set) and exactly one of
these lies in \(T\); by the proof of Lemma 8.5(4), the \(T\)-member is the
lesser of the two (equal in case (a)). Hence \(\pi(u)\) is that unique point.

*(2).* \(\pi_{\mathbb Z}\) is Borel (Claim 8.4.1), \(\iota\) is Borel (Lemma
8.5(2)), and \(\min\) is continuous \(\mathbb R^2\to\mathbb R\).

*(3).* \(\mathcal O_G(w(u))=\mathcal O_G(u)\) for \(w\in G\), and \(\pi\)
depends only on the full orbit by (1).

*(4).* If \(t\in T\), then \(t\in\mathcal O_G(t)\cap T\), and by (1)
\(\pi(t)=t\). For the fibre: \(\pi(u)=t\iff t\in\mathcal O_G(u)\iff
u\in\mathcal O_G(t)\) (orbits are equivalence classes). \(\mathcal O_G(t)\) is
the image of the countable group \(G\), hence countable.

*(5).* \(T\subseteq D\subseteq Y_1\subseteq(-1,1)\) is Borel (Lemma 8.5(4)); a
Borel subset of a Polish space is standard Borel **[standard]**. The map \(\pi\)
is a Borel retraction of \(Y_1\) onto \(T\) whose fibres are exactly the full
response orbits, which is precisely the assertion "\(\pi:Y_0\setminus F\to T\)
is a standard Borel orbit quotient" (CERT:675–679). **The response relation is
smooth by exhibition of \(T\); no appeal to the Becker–Kechris/Burgess
machinery is made.** \(\square\)

**Remark on the commission's alternative formula.** O8.6 suggests
"\(\pi(u)=w(u)\) where \(w\) = first word with \(w(u)\in\) transversal". That
also works (enumerate \(G\), take the least index \(i\) with
\(w_i(u)\in T\); the level sets \(\{u:i(u)=i\}\) are Borel), and gives the same
map by uniqueness in (1). The route via \(\pi_{\mathbb Z}\) and \(\iota\) is
given above because it makes the two-case structure of Lemma 8.5(3) visible;
both are recorded because Lemma 9.1 uses the word-enumeration form.

## Lemma 8.7 (O8.7) — QUANTIFIER AUDIT for §8

**[inputs: Lemmas 6.3, 7.7, 8.1–8.6]**
**[quantifier: this lemma *is* the quantifier statement]**

**Statement.** Every assertion of Lemmas 8.1–8.6 is **pointwise on
\(Y_1=Y_0\setminus F\)**, with no exceptional set inside \(Y_1\). The set
\(Y_1\) itself is:

- Borel (Claim 6.3.7(1), Lemma 7.1);
- \(\mu_U(Y_1)=1\), i.e. its complement in \((-1,1)\) is \(\mu_U\)-null. The
  complement decomposes into exactly two named null pieces:
  \[
  (-1,1)\setminus Y_1\ \subseteq\ \bigl((-1,1)\setminus Y_0\bigr)\ \cup\ F,
  \]
  where \(\mu_U((-1,1)\setminus Y_0)=0\) by Claim 6.3.7(1) — itself a countable
  union \(\bigcup_w(D_0\setminus G_w)\cup((-1,1)\setminus D_0)\) of null sets —
  and \(\mu_U(F)=0\) by Lemma 7.7;
- invariant under \(\mathbf a,\mathbf b,\tau\) and hence under all of \(G\).

**Final domain for §§8–9:** \(Y_1\), Borel, \(G\)-invariant, \(\mu_U\)-conull.
No statement below is asserted outside \(Y_1\). \(\square\)

---

# §9 — Scalar disintegration and normalization

Throughout §9, \(\mu_U\) is regarded as a Borel probability measure on \(Y_1\)
(legitimate since \(\mu_U(Y_1)=1\)), and
\[
\nu:=\pi_*\mu_U,
\]
a Borel probability measure on \(T\). Fix once and for all an enumeration
\(w_1=e,w_2,w_3,\dots\) of the countable group \(G\). Each \(w_i\) acts as a
Borel bijection of \(Y_1\) (Lemma 8.7), and restricts to a Borel map
\(T\to Y_1\).

## Lemma 9.1 (O9.1) — elementary countable-fibre disintegration

**[inputs: Lemma 8.6; Lemma 8.7; Radon–Nikodym for finite measures on a
standard Borel space]**
**[quantifier: the family is defined for every \(t\in T\); the identities hold
for every Borel \(E\), and the "probability" property holds \(\nu\)-a.e. \(t\)
(then repaired to hold for every \(t\) by a redefinition on a \(\nu\)-null
set)]**

**Statement.** There is a family \((\mu_t)_{t\in T}\) of Borel probability
measures on \(Y_1\) such that

1. \(\mu_t\bigl(\pi^{-1}(t)\bigr)=1\) for every \(t\in T\), and \(\mu_t\) is
   purely atomic with all atoms in the countable set
   \(\mathcal O_G(t)=\pi^{-1}(t)\);
2. \(t\mapsto\mu_t(E)\) is Borel for every Borel \(E\subseteq Y_1\);
3. \(\displaystyle \mu_U(E)=\int_T\mu_t(E)\,d\nu(t)\) for every Borel
   \(E\subseteq Y_1\);
4. (extension) \(\displaystyle \int_{Y_1}f\,d\mu_U
   =\int_T\Bigl(\int f\,d\mu_t\Bigr)d\nu(t)\) for every Borel
   \(f:Y_1\to[0,\infty]\).

Moreover:

5. **(a.e.-uniqueness)** If \((\mu'_t)_{t\in T}\) is any family of finite Borel
   measures on \(Y_1\) with \(\mu'_t(\pi^{-1}(t))=\mu'_t(Y_1)\) for every
   \(t\), \(t\mapsto\mu'_t(E)\) Borel for every Borel \(E\),
   **\(\displaystyle\lambda(Y_1):=\int_T\mu'_t(Y_1)\,d\nu(t)<\infty\)**, and
   \(\int_T\mu'_t(E)\,d\nu(t)=\int_T\mu''_t(E)\,d\nu(t)\) for every Borel
   \(E\), for another such family \((\mu''_t)\), then \(\mu'_t=\mu''_t\) for
   \(\nu\)-a.e. \(t\).

   *(**v0.2, m6 — hypothesis made explicit.** The finiteness condition
   \(\lambda(Y_1)<\infty\) was used in the proof of (5) below — "a finite Borel
   measure, as \(\mu'_t(Y_1)\) is \(\nu\)-integrable" — but was **not stated in
   the hypothesis list** of v0.1. The round-1 auditor's countermodel attack on
   L9.3 correctly observed that, taken in isolation and without it, (5) is
   **false**: an infinite-mass family makes \(t\mapsto\mu'_t(C_i)\) fail to be
   \(\nu\)-integrable and the "equal integrals over every \(E\Rightarrow\) equal
   \(\nu\)-a.e." step of Lemma 7.3 Step 4 is unavailable. It is harmless in both
   applications inside this document — in Lemma 9.3 Part 2 both families are
   probabilities \(\nu\)-a.e., so \(\lambda(Y_1)=1\) — but the hypothesis must
   be carried by the statement, not by the proof.)*

**Proof.** *(No Rokhlin, no abstract disintegration theorem is used; the only
non-elementary ingredient is Radon–Nikodym for finite measures.)*

*Step 1 — a Borel partition into "first-representation" pieces.* For
\(i\ge1\) set
\[
C_i:=\bigl\{u\in Y_1:\ w_i(\pi(u))=u\ \text{ and }\ w_j(\pi(u))\ne u\ \
\forall\,j<i\bigr\}.
\]
Each \(C_i\) is Borel: \(u\mapsto w_j(\pi(u))\) is Borel (composition of the
Borel maps \(\pi\) and \(w_j\)), and \(C_i\) is a finite Boolean combination of
equalizers of pairs of Borel real-valued functions. The \(C_i\) are pairwise
disjoint by construction, and they cover \(Y_1\): for \(u\in Y_1\),
\(u\in\pi^{-1}(\pi(u))=\mathcal O_G(\pi(u))\) (Lemma 8.6(4)), so
\(u=w_i(\pi(u))\) for some \(i\); take the least such \(i\).

Note the *fibrewise* meaning: for \(t\in T\),
\[
C_i\cap\pi^{-1}(t)=
\begin{cases}
\{w_i(t)\} & \text{if }w_j(t)\ne w_i(t)\ \forall j<i,\\
\varnothing & \text{otherwise,}
\end{cases}
\tag{9.1.1}
\]
so the non-empty sets among \(\{C_i\cap\pi^{-1}(t)\}_{i\ge1}\) enumerate the
singletons of the fibre \(\pi^{-1}(t)\), **each exactly once**.

**Small-orbit caution (v0.2, R7; adversary attack A1-iv).** On a *small* orbit
— one whose stabiliser in \(G\) is nontrivial, e.g. the \(\mathbf b\)-invariant
orbits of Lemma 8.5(3) case (a) — distinct group elements can give the same
point: \(w_i(t)=w_j(t)\) with \(i\ne j\) is possible, and then
\(t\mapsto w_i(t)\) and \(t\mapsto w_j(t)\) are *duplicate representatives* of
one atom. The "each exactly once" in (9.1.1) is a statement about the
**non-empty** sets: the defining minimality clause \(w_j(\pi(u))\ne u\)
\(\forall j<i\) kills every duplicate index beyond the first, so the *singletons*
are still enumerated without repetition. What it does **not** say — and what a
reader is invited to infer falsely — is that \(f_i(t)\) is the mass of the atom
\(w_i(t)\) for each \(i\): \(f_i\) is a Radon–Nikodym derivative, hence defined
only up to \(\nu\)-null sets, and the identification
\(\mu_t(\{w_i(t)\})=f_i(t)\) holds only for \(t\in T_{\rm good}\) with
\(C_i\cap\pi^{-1}(t)\ne\varnothing\) — i.e. \(\nu\)-a.e. and only at the
*first* representative index. Nothing downstream uses more: Lemma 9.1(3),(4)
integrate over \(i\), and Lemma 9.1(5) compares \(\mu'_t(C_i)\) with
\(\mu''_t(C_i)\) — never \(f_i\) itself.

*Step 2 — the base densities.* Define finite Borel measures on \(T\):
\[
\nu_i(E):=\pi_*\bigl(\mu_U|_{C_i}\bigr)(E)=\mu_U\bigl(C_i\cap\pi^{-1}(E)\bigr),
\qquad E\subseteq T\ \text{Borel}.
\]
Then \(\nu_i(E)\le\mu_U(\pi^{-1}(E))=\nu(E)\), so \(\nu_i\le\nu\); in
particular \(\nu_i\ll\nu\). By the Radon–Nikodym theorem there is a Borel
\(f_i:T\to[0,1]\) with \(d\nu_i=f_i\,d\nu\). Since the \(C_i\) partition
\(Y_1\), \(\sum_i\nu_i=\nu\) (countable additivity), so
\(\int_E\sum_if_i\,d\nu=\nu(E)\) for all Borel \(E\) (monotone convergence),
whence
\[
\sum_{i\ge1}f_i(t)=1\qquad\text{for }\nu\text{-a.e. }t.
\tag{9.1.2}
\]
Let \(T_{\rm good}:=\{t\in T:\sum_if_i(t)=1\}\), Borel with \(\nu(T_{\rm good})=1\).

*Step 3 — the fibre measures.* Define
\[
\mu_t:=\sum_{i\ge1}f_i(t)\,\delta_{w_i(t)}\quad (t\in T_{\rm good}),
\qquad \mu_t:=\delta_t\quad (t\in T\setminus T_{\rm good}).
\]

*(1).* For \(t\in T_{\rm good}\), \(\mu_t\) is a countable convex combination
of point masses at points \(w_i(t)\in\mathcal O_G(t)=\pi^{-1}(t)\), with total
mass \(\sum_if_i(t)=1\): a probability measure, purely atomic, carried by
\(\pi^{-1}(t)\). For \(t\notin T_{\rm good}\), \(\delta_t\) is a probability
measure carried by \(\{t\}\subseteq\pi^{-1}(t)\).

*(2).* For Borel \(E\), on \(T_{\rm good}\)
\(\mu_t(E)=\sum_i f_i(t)\mathbf 1_E(w_i(t))\): a countable sum of products of
Borel functions of \(t\), hence Borel; and \(\mathbf 1_E(t)\) on the Borel
complement. So \(t\mapsto\mu_t(E)\) is Borel.

*(3).* Fix Borel \(E\subseteq Y_1\). Since \(\nu(T\setminus T_{\rm good})=0\),
\[
\int_T\mu_t(E)\,d\nu(t)
=\int_{T}\sum_i f_i(t)\mathbf 1_E(w_i(t))\,d\nu(t)
=\sum_i\int_T \mathbf 1_E(w_i(t))\,f_i(t)\,d\nu(t)
\]
(monotone convergence for the interchange). Since \(d\nu_i=f_i\,d\nu\) and
\(t\mapsto\mathbf 1_E(w_i(t))\) is a bounded Borel function on \(T\),
\[
\int_T\mathbf 1_E(w_i(t))\,f_i(t)\,d\nu(t)
=\int_T\mathbf 1_E(w_i(t))\,d\nu_i(t).
\]
By the change-of-variables formula for \(\nu_i=\pi_*(\mu_U|_{C_i})\),
\[
\int_T\mathbf 1_E(w_i(t))\,d\nu_i(t)
=\int_{C_i}\mathbf 1_E\bigl(w_i(\pi(u))\bigr)\,d\mu_U(u)
=\int_{C_i}\mathbf 1_E(u)\,d\mu_U(u)=\mu_U(C_i\cap E),
\]
where the middle equality uses the defining property \(w_i(\pi(u))=u\) on
\(C_i\). Summing over \(i\) and using that \(\{C_i\}\) partitions \(Y_1\):
\(\int_T\mu_t(E)\,d\nu(t)=\sum_i\mu_U(C_i\cap E)=\mu_U(E)\).

*(4).* (3) is the case \(f=\mathbf 1_E\); extend by linearity to nonnegative
simple functions and by monotone convergence to all Borel
\(f:Y_1\to[0,\infty]\), using (2) to ensure the inner integral is a Borel
function of \(t\) (it is a monotone limit of Borel functions).

*(5) — the a.e.-uniqueness, proved directly.* Let \((\mu'_t),(\mu''_t)\) be as
stated, with common "integral" \(\lambda(E):=\int_T\mu'_t(E)\,d\nu(t)
=\int_T\mu''_t(E)\,d\nu(t)\) (a finite Borel measure, as \(\mu'_t(Y_1)\) is
\(\nu\)-integrable — this is part of the hypothesis that the integrals are
finite; in our applications all the families are probabilities).

Fix \(i\ge1\) and a Borel \(E\subseteq T\). Because \(\mu'_t\) is carried by
\(\pi^{-1}(t)\),
\[
\mu'_t\bigl(C_i\cap\pi^{-1}(E)\bigr)=\mathbf 1_E(t)\,\mu'_t(C_i),
\]
since \(\pi^{-1}(E)\cap\pi^{-1}(t)=\pi^{-1}(t)\) if \(t\in E\) and
\(=\varnothing\) otherwise. Integrating against \(\nu\),
\[
\int_E\mu'_t(C_i)\,d\nu(t)=\lambda\bigl(C_i\cap\pi^{-1}(E)\bigr)
=\int_E\mu''_t(C_i)\,d\nu(t).
\]
Both \(t\mapsto\mu'_t(C_i)\) and \(t\mapsto\mu''_t(C_i)\) are Borel and
\(\nu\)-integrable, and their integrals agree over every Borel \(E\subseteq T\);
by the argument of Lemma 7.3 Step 4 they agree \(\nu\)-a.e. Let \(M_i\) be the
\(\nu\)-null set where they differ, and \(M:=\bigcup_iM_i\), \(\nu(M)=0\).

For \(t\notin M\): \(\mu'_t(C_i)=\mu''_t(C_i)\) for every \(i\). By (9.1.1) the
sets \(C_i\cap\pi^{-1}(t)\) are exactly the singletons of the countable fibre
\(\pi^{-1}(t)\), each occurring once. Both \(\mu'_t\) and \(\mu''_t\) are
carried by \(\pi^{-1}(t)\), which is countable, hence both are purely atomic and
determined by their values on those singletons. Therefore
\(\mu'_t=\mu''_t\). \(\square\)

**Why this matters.** CERT:705 invokes "Uniqueness of probability
disintegration" as a black box. Part (5) *is* that uniqueness, in the only
generality needed, proved from Radon–Nikodym and the countability of the
fibres. This removes the third named residual risk.

## Lemma 9.2 (O9.2) — \(\pi\circ\mathbf a=\pi\circ\mathbf b=\pi\), and the transported families fibre over the same \(\nu\)

**[inputs: Lemma 8.6(3); Lemma 9.1]**
**[quantifier: (1) pointwise on \(Y_1\); (2)–(3) for every \(t\in T\) and every
Borel \(E\)]**

**Statement.**

1. \(\pi\circ\mathbf a=\pi\circ\mathbf b=\pi\) pointwise on \(Y_1\), and
   \(\mathbf a(\pi^{-1}(t))=\mathbf b(\pi^{-1}(t))=\pi^{-1}(t)\) for every
   \(t\in T\);
2. \(\pi_*(\mathbf b_*\mu_U)=\nu\) and \(\pi_*(\mathbf a_*\mu_U)=\nu\);
3. \((\mathbf b_*\mu_t)_{t\in T}\) is a family of Borel probability measures,
   Borel in \(t\), with \(\mathbf b_*\mu_t\) carried by \(\pi^{-1}(t)\), and
   \(\int_T\mathbf b_*\mu_t\,d\nu=\mathbf b_*\mu_U\). Likewise for
   \(\mathbf a\).

**Proof.**

*(1).* \(\mathbf a,\mathbf b\in G\); apply Lemma 8.6(3). Fibre invariance:
\(\pi^{-1}(t)=\mathcal O_G(t)\) (Lemma 8.6(4)) and \(\mathcal O_G(t)\) is
\(G\)-invariant.

*(2).* \(\pi_*(\mathbf b_*\mu_U)=(\pi\circ\mathbf b)_*\mu_U=\pi_*\mu_U=\nu\)
by (1) and functoriality of pushforward. Same for \(\mathbf a\).

*(3).* \(\mathbf b_*\mu_t(E)=\mu_t(\mathbf b^{-1}E)=\mu_t(\mathbf bE)\), Borel
in \(t\) by Lemma 9.1(2) applied to the Borel set \(\mathbf bE\); total mass
\(1\); carried by \(\mathbf b(\pi^{-1}(t))=\pi^{-1}(t)\) by (1). And
\[
\int_T\mathbf b_*\mu_t(E)\,d\nu(t)=\int_T\mu_t(\mathbf b^{-1}E)\,d\nu(t)
=\mu_U(\mathbf b^{-1}E)=\mathbf b_*\mu_U(E)
\]
by Lemma 9.1(3). \(\square\)

## Lemma 9.3 (O9.3) — THE NORMALIZATION, simplified

**[inputs: Lemma 6.5 (T-a),(T-b); Lemma 9.1 (3),(4),(5); Lemma 9.2;
Claim 6.3.2]**
**[quantifier: \(c_B=c_A=1\) \(\nu\)-a.e. \(t\); the fibre transport laws
\(\nu\)-a.e. \(t\)]**

**Statement.** Put
\[
c_B(t):=\int r_B^2\,d\mu_t,\qquad
c_A(t):=\int r_A(P(\cdot))^2\,d\mu_t .
\]
Then

1. \(c_B(t)=1\) and \(c_A(t)=1\) for \(\nu\)-a.e. \(t\) — **proved without any
   uniqueness theorem**;
2. \(\mathbf b_*\mu_t=r_B^2\,\mu_t\) and
   \(\mathbf a_*\mu_t=r_A(P(\cdot))^2\,\mu_t\) for \(\nu\)-a.e. \(t\).

**Proof.**

*Part 1 — the pushforward computation.* By Lemma 6.5,
\(\mathbf b_*\mu_U=r_B^2\,\mu_U\) as measures on \(Y_1\). Push both sides
forward by \(\pi\).

*LHS.* \(\pi_*(\mathbf b_*\mu_U)=(\pi\circ\mathbf b)_*\mu_U=\pi_*\mu_U=\nu\)
(Lemma 9.2(2)).

*RHS — the Fubini step, written out.* Let \(E\subseteq T\) be Borel. Then
\[
\pi_*\bigl(r_B^2\mu_U\bigr)(E)
=\int_{Y_1}\mathbf 1_{\pi^{-1}(E)}(u)\,r_B(u)^2\,d\mu_U(u)
\overset{\text{L9.1(4)}}{=}
\int_T\Bigl(\int_{Y_1}\mathbf 1_{\pi^{-1}(E)}(u)\,r_B(u)^2\,d\mu_t(u)\Bigr)
d\nu(t).
\]
The application of Lemma 9.1(4) is legitimate because
\(u\mapsto\mathbf 1_{\pi^{-1}(E)}(u)r_B(u)^2\) is Borel and nonnegative. Now
fix \(t\). Since \(\mu_t\) is carried by \(\pi^{-1}(t)\) (Lemma 9.1(1)), we
have \(\mathbf 1_{\pi^{-1}(E)}(u)=\mathbf 1_E(\pi(u))=\mathbf 1_E(t)\) for
\(\mu_t\)-a.e. \(u\) — indeed for every \(u\) in the carrier. Hence the inner
integral equals \(\mathbf 1_E(t)\int r_B^2\,d\mu_t=\mathbf 1_E(t)c_B(t)\), and
\[
\pi_*\bigl(r_B^2\mu_U\bigr)(E)=\int_E c_B(t)\,d\nu(t).
\]
So \(\pi_*(r_B^2\mu_U)\) has density \(c_B\) with respect to \(\nu\).

*Conclusion of Part 1.* Equating: \(\nu(E)=\int_Ec_B\,d\nu\) for every Borel
\(E\subseteq T\). Since \(\nu\) is finite, \(c_B\) is \(\nu\)-integrable, and by
the argument of Lemma 7.3 Step 4 (applied to \(c_B-1\)) we get
\(c_B=1\) \(\nu\)-a.e. The identical computation with (T-a) and
\(\pi\circ\mathbf a=\pi\) gives \(c_A=1\) \(\nu\)-a.e.

**No uniqueness theorem was consumed for this half** — only Lemma 9.1(4) and
the fact that a measure with density \(c\) against \(\nu\) equal to \(\nu\)
forces \(c=1\) a.e.

*Part 2 — the fibre equality, via the elementary uniqueness.* Consider the two
families
\[
\mathcal F':=(\mathbf b_*\mu_t)_{t\in T},\qquad
\mathcal F'':=\bigl(r_B^2\,\mu_t\bigr)_{t\in T}.
\]

*Both are admissible for Lemma 9.1(5):*
- \(\mathcal F'\): Lemma 9.2(3) — Borel in \(t\), carried by \(\pi^{-1}(t)\),
  finite (probabilities).
- \(\mathcal F''\): \(r_B^2\mu_t\) is carried by \(\pi^{-1}(t)\) because
  \(\mu_t\) is; \(t\mapsto(r_B^2\mu_t)(E)=\int\mathbf 1_Er_B^2\,d\mu_t
  =\sum_if_i(t)\mathbf 1_E(w_i(t))r_B(w_i(t))^2\) is Borel; total mass
  \(c_B(t)=1\) for \(\nu\)-a.e. \(t\), hence finite \(\nu\)-a.e. (redefine
  \(r_B^2\mu_t:=\mu_t\) on the \(\nu\)-null exceptional set to make every
  member finite — this changes nothing \(\nu\)-a.e.).

*They have the same \(\nu\)-integral:* by Lemma 9.2(3),
\(\int_T\mathbf b_*\mu_t\,d\nu=\mathbf b_*\mu_U\); by Lemma 9.1(4),
\(\int_T(r_B^2\mu_t)(E)\,d\nu(t)=\int_{Y_1}\mathbf 1_Er_B^2\,d\mu_U
=(r_B^2\mu_U)(E)\). And \(\mathbf b_*\mu_U=r_B^2\mu_U\) by Lemma 6.5. So the
two families integrate to the same finite measure.

*Apply Lemma 9.1(5):* \(\mathbf b_*\mu_t=r_B^2\mu_t\) for \(\nu\)-a.e. \(t\).

*Mirror for \(\mathbf a\):* identical, with (T-a),
\(\mathbf a_*\mu_U=r_A(P(\cdot))^2\mu_U\), \(\pi\circ\mathbf a=\pi\), and
\(c_A=1\) \(\nu\)-a.e. \(\square\)

**Named null set.** Let \(N_2\subseteq T\) be the \(\nu\)-null Borel set off
which all four conclusions (\(c_B=1\), \(c_A=1\), and the two fibre transport
laws) hold simultaneously; \(N_2\) is the union of four \(\nu\)-null sets.

## Lemma 9.4 (O9.4) — atomicity, and the fibres sit in the full-zero locus

**[inputs: Lemma 9.1(1); Lemma 8.6(4); Claim 6.3.7(4); Lemma 6.1(5)]**
**[quantifier: (1) pointwise for every \(t\in T\); (2) pointwise for every
\(t\in T\), with the general \(\nu\)-a.e. null-fibre lemma recorded as (3)]**

**Statement.**

1. Every \(\mu_t\) is purely atomic, with atoms contained in the countable set
   \(\pi^{-1}(t)=\mathcal O_G(t)\).
2. For **every** \(t\in T\) and **every** atom \(u\) of \(\mu_t\): \(u\in Y_0\)
   and \((P(u),u)\in Z\), i.e. \(u\) is the target coordinate of a full-zero
   pair; and \(-u\) is likewise. In particular no atom lies outside the
   full-zero locus.
3. (general null-fibre lemma, recorded because the certificate's phrasing needs
   it) If \(N\subseteq Y_1\) is Borel with \(\mu_U(N)=0\), then
   \(\mu_t(N)=0\) for \(\nu\)-a.e. \(t\).

**Proof.**

*(1).* By construction \(\mu_t=\sum_if_i(t)\delta_{w_i(t)}\) (or \(\delta_t\)),
carried by the countable set \(\mathcal O_G(t)\) (Lemma 8.6(4)). A measure
carried by a countable set is purely atomic.

*(2).* The atoms lie in \(\mathcal O_G(t)\subseteq Y_1\subseteq Y_0\subseteq
Y\) (Lemma 8.7). By Lemma 6.1(5), every \(u\in Y\) satisfies
\((P(u),u)\in Z=R_0^{-1}(0)\cap(-1,1)^2\). And \(-u=\mathbf b(u)\in Y_0\)
(Claim 6.3.7(3)), so \((P(-u),-u)\in Z\) too.

**Note the strengthening.** CERT:735–737 states this \(\nu\)-a.e.
("Because \(\phi=0\) almost everywhere, for almost every \(t\) no atom of
\(\mu_t\) lies outside the full-zero locus"). In the present construction the
statement is **pointwise for every \(t\)**, because the a.e. content of
\(\phi=0\) was already spent, once, in defining \(Y\) and \(Y_0\)
(Claim 0.2, Claim 6.3.1, Claim 6.3.7) — the fibres live in \(Y_0\) by
construction and never leave it. This removes a quantifier from the interface.

*(3).* By Lemma 9.1(3), \(0=\mu_U(N)=\int_T\mu_t(N)\,d\nu(t)\) with a
nonnegative Borel integrand; hence \(\mu_t(N)=0\) \(\nu\)-a.e. \(\square\)

## Lemma 9.5 (O9.5) — a positive atom propagates along the whole response orbit

**[inputs: Lemma 9.3(2); Claim 6.3.2; Lemma 9.4]**
**[quantifier: \(\nu\)-a.e. \(t\) (namely \(t\notin N_2\)); then pointwise over
the whole orbit]**

**Statement.** For every \(t\in T\setminus N_2\):

1. \(\mu_t(\{\mathbf b(u)\})=r_B(u)^2\,\mu_t(\{u\})\) and
   \(\mu_t(\{\mathbf a(u)\})=r_A(P(u))^2\,\mu_t(\{u\})\) for every
   \(u\in\pi^{-1}(t)\);
2. if \(\mu_t(\{u\})>0\) for some \(u\in\pi^{-1}(t)\), then
   \(\mu_t(\{v\})>0\) for **every** \(v\in\pi^{-1}(t)=\mathcal O_G(t)\);
3. \(\mu_t(\{v\})>0\) for every \(v\in\mathcal O_G(t)\).

**Proof.**

*(1).* Let \(t\notin N_2\), so \(\mathbf b_*\mu_t=r_B^2\mu_t\) (Lemma 9.3(2)).
Evaluate both sides at the Borel singleton \(\{u\}\):
\[
\mathbf b_*\mu_t(\{u\})=\mu_t(\mathbf b^{-1}\{u\})=\mu_t(\{\mathbf b(u)\}),
\qquad
\bigl(r_B^2\mu_t\bigr)(\{u\})=\int_{\{u\}}r_B^2\,d\mu_t
=r_B(u)^2\,\mu_t(\{u\}),
\]
using \(\mathbf b^{-1}=\mathbf b\). The \(\mathbf a\)-identity is identical with
\(\mathbf a_*\mu_t=r_A(P(\cdot))^2\mu_t\).

*(2) — induction over words.* By Claim 6.3.2, \(r_B(u)^2\in(0,\infty)\) and
\(r_A(P(u))^2\in(0,\infty)\) for every \(u\in Y_0\) — **pointwise**, no
exceptional set. So (1) shows: \(\mu_t(\{u\})>0\Rightarrow
\mu_t(\{s(u)\})>0\) for \(s\in\{\mathbf a,\mathbf b\}\), and conversely
(divide). Let \(v\in\mathcal O_G(t)=\mathcal O_G(u)\); write
\(v=s_k\cdots s_1(u)\) as a finite word in the generators (possible since
\(G=\langle\mathbf a,\mathbf b\rangle\) and \(v,u\) are in the same orbit).
Induct on \(k\): \(\mu_t(\{s_1(u)\})>0\); if
\(\mu_t(\{s_j\cdots s_1(u)\})>0\) then \(\mu_t(\{s_{j+1}\cdots s_1(u)\})>0\).
After \(k\) steps, \(\mu_t(\{v\})>0\).

*(3).* \(\mu_t\) is a probability measure carried by the countable set
\(\mathcal O_G(t)\) (Lemma 9.4(1)); a countable family of nonnegative numbers
summing to \(1\) has a strictly positive member. So some atom is positive;
apply (2). \(\square\)

## Lemma 9.6 (O9.6) — existence of a good \(t\), and the exact interface into §10

**[inputs: Lemmas 9.1, 9.3, 9.4, 9.5; \(\nu(T)=1\)]**
**[quantifier: existence of a single \(t^\ast\); all listed properties hold
pointwise for that \(t^\ast\)]**

**Statement.** There exists \(t^\ast\in T\) such that all of the following hold
simultaneously. Write \(\mathcal O:=\mathcal O_G(t^\ast)=\pi^{-1}(t^\ast)\) and
\(\mu_\ast:=\mu_{t^\ast}\).

| # | property | source |
|---|---|---|
| I1 | \(\mathcal O\subseteq Y_1=Y_0\setminus F\) is a **single** full response orbit, countable, and \(G\)-invariant | L8.6(4), L8.7 |
| I2 | \(\mu_\ast\) is a **purely atomic probability measure** with \(\mu_\ast(\mathcal O)=1\) and no mass outside \(\mathcal O\) | L9.1(1), L9.4(1) |
| I3 | \(\mu_\ast(\{v\})>0\) for **every** \(v\in\mathcal O\) | L9.5(3) |
| I4 | \(\mu_\ast(\{\mathbf b(v)\})=r_B(v)^2\mu_\ast(\{v\})\) for every \(v\in\mathcal O\) | L9.5(1) |
| I5 | \(\mu_\ast(\{\mathbf a(v)\})=r_A(P(v))^2\mu_\ast(\{v\})\) for every \(v\in\mathcal O\) | L9.5(1) |
| I6 | \(\tau|_{\mathcal O}\) is strictly increasing and **fixed-point-free**; \(\mathcal O=\mathcal O_{\mathbb Z}(v)\cup\mathcal O_{\mathbb Z}(-v)\) for any \(v\in\mathcal O\), the two \(\mathbb Z\)-orbits being equal or disjoint | L6.4, L7.7, L8.5(3), (8.0.1) |
| I7 | every \(v\in\mathcal O\) lies in \((-1,1)\), \(P(v)\) and \(P(-v)\) are defined and lie in \((-1,1)\), \((P(v),v)\in Z\) and \((P(-v),-v)\in Z\) | L6.1, L9.4(2), Claim 6.3.7(4) |
| I8 | \(P(-P(v))=-v\) for every \(v\in\mathcal O\) (dual-zero involution) | L6.2(3) |
| I9 | \(r_A(s)r_B(s)=1\), \(r_A(s)r_A(-s)=1\), \(r_B(s)r_B(-s)=1\), all in \((0,\infty)\), for every \(s\in(-1,1)\) | CERT:422,426,430; Claim 6.3.2 |

**Proof.** The conditions on \(t\) that are not automatic are exactly
\(t\notin N_2\) (Lemma 9.3, needed for I4, I5) — a **single** \(\nu\)-null Borel
set, itself a union of four \(\nu\)-null sets. Everything else in the table
holds for **every** \(t\in T\) (I1, I2, I6, I7, I8, I9 are pointwise; I3 follows
from I4/I5 by Lemma 9.5(3), hence also needs only \(t\notin N_2\)).

Therefore \(\nu(T\setminus N_2)=\nu(T)-0=1>0\), so \(T\setminus N_2\ne
\varnothing\); choose \(t^\ast\in T\setminus N_2\). *(\(\nu(T)=1\) because
\(\nu=\pi_*\mu_U\) with \(\mu_U(Y_1)=1\), Lemma 8.7.)* \(\square\)

**Remark on I9 — CORRECTED IN v0.2 (m5/R8, adversary attack 16).** The product
laws are CERT:419–431. v0.1's remark said the computations are "valid where
\(K=1\), i.e. on full-zero coordinates". **That clause was wrong — it
contradicts I9 itself, which asserts the identities for every
\(s\in(-1,1)\) — and it is deleted.** The identities hold **identically on
\((-1,1)\)**, with no zero-locus membership:
\[
A(t)B(t)=\sqrt{p(t)g(-t)}\cdot\sqrt{g(t)p(-t)}
=\sqrt{p(t)p(-t)\,g(t)g(-t)}
=\sqrt{\frac{b(t)^2b(-t)^2}{g(t)g(-t)}\;g(t)g(-t)}
=b(t)^2 ,
\]
using \(p=b^2/g\) (CZS:49) and \(b(-t)=b(t)\); hence
\(r_A(t)r_B(t)=A(t)B(t)/b(t)^2=1\) **unconditionally**, and likewise
\(A(t)A(-t)=b(t)^2\) gives \(r_A(t)r_A(-t)=1\) and \(B(t)B(-t)=b(t)^2\) gives
\(r_B(t)r_B(-t)=1\). Every factor is in \((0,\infty)\) on \((-1,1)\) by Claim
6.3.2. This matches the certificate's own unconditional statement of the
product law at CERT:258–264 (\(A_n(x)A_n(-x)=b(x)^2\), CERT:261, which
CERT:264 says "holds identically") and the
displays CERT:422/426/430, and is corroborated by the S1 referee verdict:150,
"The three product identities are exact and require **no** zero-locus
membership … `r_A(t)r_B(t) = A(t)B(t)/b(t)² = 1` since
`A(t)B(t) = √(p(t)p(−t)g(t)g(−t)) = b(t)²`" (SPATIAL-ATTAINMENT-S1-REFEREE-
VERDICT.md:148–151). §10 uses them at the labels \(c_j\), which are in any case
full-zero coordinates by I7 — but that membership is **not** a hypothesis of
I9. **[Recorded as a dependency, not re-derived: the product laws are
certificate displays CERT:422/426/430 within the promoted §5; the one-line
verification above is given only to show the \(K=1\) clause was spurious.]**

---

# OX.1 — Inputs table (every consumed display, with file and line)

| # | display / statement | anchor | consumed by |
|---|---|---|---|
| A1 | \(S\in(0.2508753845015185,\ 0.250875388108398]\) | CERT:24–28 | L7.6 Step 7 |
| A2 | \(g_n\to g\) uniformly | CERT:64 | Claim 0.1 |
| A2′ | \(g\) **continuous** and concave | **FR:49**; concavity also CZS:41, CERT:69 | L6.1(1) *(v0.2, R10: v0.1 anchored continuity at CERT:64, which asserts only \(g_n\to g\))* |
| A3 | \(g(x)>0\) for every \(x\in(-1,1)\) | **CERT:70**; FR:53–64 (box FR:63) | Claim 6.3.2, L6.1(1) |
| A4 | \(g\) Bellman-feasible at \(S\) | **CERT:71** | (via CZS:94) |
| A5 | exact endpoint \(R_0\)-gaps uniform in \(n\) | **CERT:72**; FR:119–168 | CERT:172, Claim 0.2 |
| A6 | **the full interior zero locus is a one-to-one strictly increasing relation** | CERT:73 (**operative anchor: A6′ below**; see SCOPE FLAG 6.1.A) | L6.1(2),(3) |
| A6′ | **\(\boxed{R_0^{-1}(0)\cap D^2\text{ is a one-to-one strictly increasing relation}}\), \(D:=(-1,1)\)** | **CEPE:224** (box); §7 horizontal exclusion CEPE:177–194, §8 vertical exclusion CEPE:196–210, §9 assembly CEPE:212–225; \(D\) fixed at CEPE:15; scope sentence CEPE:208–210 | **L6.1(2),(3) — THE operative anchor (v0.2, B1/R6; v0.1 cited this document nowhere)** |
| A7 | \(R_{0,n}=\phi_n(X,U)\), \(\phi_n\ge0\) | CERT:132–134 | Claim 0.1 |
| A7′ | **the generic weld \(\mathcal B=d(X,U)+W+W_B\)**, i.e. \(\mathcal B_{3322}=G(X,U)+Y(B_3-I/2)+(A_3-I/2)V\) with \(G(X,U)=XU+X/2-U/2-I\) | **MAN:498–507** (LaTeX twin `manuscript.tex:436`); named but not displayed in CERT (CERT:1078–1079); independently replicated at SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md:284 | **Claim 0.1 (scalarisation) — added v0.2 (S1/R1); v0.1 consumed it without an anchor. Second anchor (round-2 F-1): foundational-sprint-1197/EXACT-I3322-QUANTUM-SUPREMUM.md:38-47 (tensor form, machine-verified)** |
| A8 | \(\phi_n\to\phi\) on \((-1,1)^2\) | CERT:156 | Claim 0.1 |
| A9 | \(\mu(E_\partial)=0\) | CERT:171–173 | Claim 0.2 |
| A10 | \(\phi=0\) \(\mu\)-a.e. | CERT:186–191 | Claim 0.2 |
| A11 | \(b(t)=\sqrt{1-t^2}/2\) | CERT:229 | everywhere; L7.6 Step 6 term match |
| A12 | \(p_n(x)=b(x)^2/g_n(x)\); \(A_n,B_n\) | CERT:239–245 | Claim 0.1 |
| A13 | \(A(X)\Omega=W\Omega\), \(B(U)\Omega=W_B\Omega\) | CERT:352–361 | (upstream of A13′/A14/A15) |
| A13′ | **PRE-DIVISION IDENTITY:** for every bounded Borel \(f\), \(\int b(x)^2f(-x)d\mu_X=\int A(x)^2f(x)d\mu_X\) (and the \(U\)-analogue) | **CERT:376–390**; division sentence CERT:392–393 | **L6.3 — the derivation of (RN-X)/(RN-U) for every Borel \(E\subseteq(-1,1)\). Added v0.2 (B2/M2/S2/R2); uncited in v0.1** |
| A14 | **RN law X (post-division, boxed):** \(d((-\mathrm{id})_*\mu_X)=r_A^2d\mu_X\), \(r_A=A/b\) — *as printed, qualified by A16; the unqualified form used here is derived in L6.3 from A13′, not read off this box* | CERT:395–403 (quoted verbatim in L6.3) | Claims 6.3.3, 6.3.5, 6.3.5′ |
| A15 | **RN law U (post-division, boxed):** \(d((-\mathrm{id})_*\mu_U)=r_B^2d\mu_U\), \(r_B=B/b\) — *same caveat as A14* | CERT:407–415 (quoted verbatim in L6.3) | Claims 6.3.3, 6.3.4; L6.5 |
| A15′ | **mutual equivalence:** "both reflected measures are equivalent to the original measures on the interior support" | **CERT:433** | L6.3 (corroborates the A13′ derivation; uncited in v0.1) |
| A16 | scope of the printed boxes: "hold almost everywhere on the endpoint-free support" | CERT:417 | L6.3 quantifier discussion — **not** consumed as a premise in v0.2 |
| A17 | product laws \(r_Ar_A(-\cdot)=1\), \(r_Br_B(-\cdot)=1\), \(r_Ar_B=1\) | CERT:422, 426, 430 | L9.6 I9; §10 line 829–831 |
| A18 | \(d(i,j)=ij+(i-j)/2-1\) | **CZS:34** (display CZS:33–35) | L6.2, L7.6 Step 2, Claim 0.1 |
| A19 | \(p(x)=b(x)^2/g(x)\) | CZS:49 | L6.1(1), L7.5 |
| A20 | \(K(t)=g(t)g(-t)/b(t)^2\ge1\) | CZS:78–80 | L7.5 (L2),(L4) |
| A21 | \(A(x)=\sqrt{p(x)g(-x)}\), \(B(u)=\sqrt{g(u)p(-u)}=A(-u)\) | CZS:86–88 | Claim 0.1, L6.1(1), L6.2, L7.5 |
| A22 | \(h=S-d\), \(R_0=h-A-B\) | CZS:90–92 | Claim 0.1, L7.6 Step 1 |
| A23 | **ZERO-SET LOCALIZATION RECEIPT:** \(R_0(x,u)=0\Rightarrow K(x)=K(u)=1\), \(p(x)=g(-x)\), \(p(-u)=g(u)\) | **CZS:94–111**, boxed at CZS:103–105, displayed at CZS:109–111 | L7.5 (all four identities) |
| A24 | **strict Monge only:** \((x_1-x_2)(u_1-u_2)\ge0\) for two full-zero pairs | **CZS:117–122**; CZS:124–125 are *pointer sentences* to CEPE §§7–8, CZS:126 the summary | L6.1(2),(3) via A6′ — **secondary anchor (v0.2, B1/R6)** |
| A25 | **\(\phi\) SYMMETRY:** \(R_0(-u,-x)=R_0(x,u)\), from \(B(u)=A(-u)\) and \(d(-u,-x)=d(x,u)\) | **CZS:128–138**, display at **CZS:133–135** (formula CZS:134), justification at **CZS:137–138**; also boxed at CEPE:202 (display CEPE:201–203) | L6.2(1) — hence \(\sigma\), \(P(-P(u))=-u\), \(P(Y)=-Y\) |
| A26 | Receipt (ii), occupancy-qualified graph statement | FR:172–192 (box at FR:177–179; scope sentence FR:191–192) | SCOPE FLAG 6.1.A only — **not** used as the operative anchor |
| A27 | Receipt (iv): \(S>1/4\) | FR:196–208 | L7.6 Step 7 |
| A28 | Lean `quarter_ceiling` (hyps \(x^2\le1\), \(u^2\le1\)) | **QC:77–90** (quoted verbatim in L7.6) | L7.6 Step 6 |
| A29 | Lean `quarter_lt_window_lower` | **QC:95–97** (quoted verbatim in L7.6) | L7.6 Step 7 |
| A30 | Lean claim boundary | QC:16–19 | L7.6 honest-scope note |

---

# OX.2 — Interface-out table: exactly what §10 consumes

Checked line-by-line against the actual text of CERT §10 (CERT:746–880), plus
the two items §11 draws directly from §§6–9.

| §10 line | what §10 asserts / uses | supplied by | status |
|---|---|---|---|
| CERT:748 | "Choose \(u_0\) in the selected orbit" | L9.6 (\(t^\ast\), \(\mathcal O\), I1) | **supplied** |
| CERT:750–751 | \(u_n=\tau^n(u_0)\) well-defined for all \(n\in\mathbb Z\) | L6.3 (\(\tau\) a bijection of \(Y_0\)), I1 (\(\mathcal O\) \(G\)-invariant) | **supplied** |
| CERT:754–755 | the \(u_n\) are **distinct**, "\(\tau\) increasing and fixed-point-free on this orbit" | L6.4 (no non-fixed periodic point) + L7.7 (\(\mathcal O\cap F=\varnothing\)), I6 | **supplied** |
| CERT:760 | \(c_{2n}=u_n\); labels must be cosines in \((-1,1)\) | I7 | **supplied** |
| CERT:764 | \(c_{2n+1}=-P(-u_n)\) — needs \(-u_n\in\operatorname{dom}P\) | Claim 6.3.7(3) (\(Y_0\) is \(\mathbf b\)-invariant) + L6.1 (\(P\) defined on \(Y\)); I7 | **supplied** |
| CERT:764 | \(c_{2n+1}\in(-1,1)\) | L6.2(2) (\(\sigma(Y)\subseteq Y\subseteq(-1,1)\)) | **supplied** |
| CERT:767–771 | \(P(c_{2n+1})=c_{2n}\) "by the dual-zero involution" | L6.2(3) applied at the point \(-u_n\in Y_0\): \(P(-P(-u_n))=u_n\) | **supplied** |
| CERT:776–781 | \(u_{n+1}=\mathbf a(-u_n)=P^{-1}(-P(-u_n))\) | L6.3: \(\tau=\mathbf a\mathbf b\), so \(u_{n+1}=\tau(u_n)=\mathbf a(\mathbf b(u_n))=\mathbf a(-u_n)\) | **supplied** |
| CERT:786 | \(P(c_{2n+2})=c_{2n+1}\) | Claim 6.3.5 (\(P\circ\mathbf a=-P\)): \(P(u_{n+1})=-P(-u_n)=c_{2n+1}\) | **supplied** |
| CERT:792–796 | \(P(c_{j+1})=c_j\) for **every** \(j\in\mathbb Z\) | the two preceding rows, even/odd | **supplied** |
| CERT:798 | "Every adjacent pair \((c_j,c_{j+1})\) is a full-zero source-target pair" | L6.1(5) with \(P(c_{j+1})=c_j\); I7 | **supplied** |
| CERT:803–806 | \(\widetilde\lambda_{2n}=\sqrt{\mu_t(\{u_n\})}\) — needs \(u_n\) to be an atom | I2, I3 | **supplied** |
| CERT:808–811 | \(\widetilde\lambda_{2n+1}=\sqrt{\mu_t(\{-u_n\})}\) — needs \(-u_n\in\mathcal O\) | \(-u_n=\mathbf b(u_n)\in\mathcal O\) by I1 (\(G\)-invariance); I3 | **supplied** |
| CERT:814–821 | \(\widetilde\lambda_{2n+1}/\widetilde\lambda_{2n}=r_B(c_{2n})\) | I4 at \(v=u_n\): \(\mu_\ast(\{-u_n\})=r_B(u_n)^2\mu_\ast(\{u_n\})\); positive square roots by I3, I9 | **supplied** |
| CERT:823–832 | \(\widetilde\lambda_{2n+2}/\widetilde\lambda_{2n+1}=1/r_A(c_{2n+1})=r_B(c_{2n+1})\), "Since \(a(u_{n+1})=-u_n\)" | \(\mathbf a(u_{n+1})=\mathbf a(\mathbf a(-u_n))=-u_n\) (L6.3); I5 at \(v=u_{n+1}\) with \(P(u_{n+1})=c_{2n+1}\); then I9 (\(r_Ar_B=1\)) | **supplied** |
| CERT:836–844 | \(\widetilde\lambda_{j+1}/\widetilde\lambda_j=r_B(c_j)\) for every \(j\) | the two preceding rows | **supplied** |
| CERT:846–847 | "The two \(\tau\)-orbits \(\{u_n\}\) and \(\{-u_n\}\) are either disjoint or identical" | **L8.5(3) casework** (case (a) identical, case (b) disjoint) | **supplied — and this is exactly the case (a)/(b) split** |
| CERT:849–855 | \(1\le\sum_j\widetilde\lambda_j^2\le2\) | I2 (\(\mu_\ast\) probability on \(\mathcal O\)) + (8.0.1): \(\sum_j\widetilde\lambda_j^2=\mu_\ast(\mathcal O_{\mathbb Z}(u_0))+\mu_\ast(\mathcal O_{\mathbb Z}(-u_0))\), which is \(=1\) in case (b) and \(=2\) in case (a) | **supplied (sharpened: the sum is exactly \(1\) or exactly \(2\))** — see Note OX.2.A |
| CERT:857–864 | the normalisation \(\lambda_j=\widetilde\lambda_j/(\sum_k\widetilde\lambda_k^2)^{1/2}\) | preceding row; the divisor is \(1\) in case (b) and \(\sqrt2\) in case (a) | **supplied — and the \(\sqrt2\) is substantive, not cosmetic; see Note OX.2.A** |
| CERT:857–875 | \(\lambda\in\ell^2(\mathbb Z)\), \(\lambda_j>0\), \(\|\lambda\|_2=1\) | preceding row + I3 (all atoms strictly positive) | **supplied** |
| CERT:886–899 (§11) | \(K(c_j)=1\) for every label | A23 (localization) at the full-zero pair \((c_{j-1},c_j)\), source and target halves; I7 | **supplied** |
| CERT:901–911 (§11) | \(B(c_j)=g(c_j)\), hence \(r_B(c_j)=g(c_j)/b(c_j)\) | A23 target half + A21, exactly as in L7.5 Step 3; every \(c_j\) is a full-zero **target** (of \((c_{j-1},c_j)\)) and a **source** (of \((c_j,c_{j+1})\)) by CERT:792–796 | **supplied** |
| CERT:961–962 (§11) | "Bellman equality at the full-zero pair \((c_{j-1},c_j)\)" | CZS:91–95 (\(R_0=0\Rightarrow h=A+B\)); CERT:798 row | **supplied** |

### Note OX.2.A — what case (a) does to the label enumeration (v0.2, R11)

*(Added on the round-1 adversary's attack A4, which attacked the "exactly 1 or
exactly 2" sharpening with a coinciding-representative orbit and found the
sharpening is precisely what that model produces.)*

The sharpening has a consequence for §10's bookkeeping that v0.1 left implicit
and that a referee will want stated:

- **In case (b)** (\(\mathcal O_{\mathbb Z}(u_0)\) and
  \(\mathcal O_{\mathbb Z}(-u_0)\) disjoint), \(j\mapsto c_j\) is injective, the
  \(\widetilde\lambda_j^2\) are the masses of \(2\times\infty\) distinct atoms
  exhausting \(\mathcal O\), and \(\sum_j\widetilde\lambda_j^2=\mu_\ast(\mathcal
  O)=1\). The normalisation at CERT:857–864 divides by \(1\).
- **In case (a)** (the two \(\mathbb Z\)-orbits coincide — the
  \(\mathbf b\)-invariant orbit of Lemma 8.5(3)(a), built explicitly by the
  adversary and surviving), the *same* atom is reached both as \(u_n\) and as
  \(-u_m\) for suitable \(n,m\). Hence **\(\widetilde\lambda\) enumerates each
  atom of \(\mathcal O\) exactly twice, \(j\mapsto c_j\) need not be
  injective**, and \(\sum_j\widetilde\lambda_j^2=2\mu_\ast(\mathcal O)=2\).

Consequently the \(\sqrt2\) in CERT:857–864 is **substantive**: in case (a) it
is exactly the factor that converts a doubly-counted orbit mass back into a
unit \(\ell^2\) norm. It is not an artefact of a loose \([1,2]\) bound. Nothing
downstream is affected — the ratio law CERT:836–844 and the eigen-equation
CERT:966–970 are invariant under a global positive rescaling of \(\lambda\) —
but a reader who assumes \(j\mapsto c_j\) injective will mis-read case (a).

**Nothing in §10 or in §11's draw on §§6–9 is left unsupplied.** Two entries are
supplied in *sharpened* form (CERT:849–855: the sum is exactly \(1\) or exactly
\(2\), not merely in \([1,2]\); CERT:735–737 via L9.4(2): pointwise for every
\(t\), not \(\nu\)-a.e.).

**One interface caution for the gate.** §10 writes \(\mu_t\) throughout without
re-stating which \(t\); the \(t\) is \(t^\ast\) of Lemma 9.6, and the properties
it must carry are I1–I9. The public amendment should insert "\(t=t^\ast\) as
selected in §9, carrying I1–I9" at CERT:748, because as written §10's
\(\mu_t\) has no antecedent binding beyond CERT:742 ("Choose one conditional
orbit measure having all these properties"), and "all these properties" is not
enumerated in the certificate.

---

# OX.3 — a.e.-versus-pointwise audit, every lemma

| lemma | statement quantifier | exceptional set (named) |
|---|---|---|
| Claim 0.1 | pointwise on \((-1,1)^2\) | none |
| Claim 0.2 | \(\mu(Z)=1\) — measure statement | \((-1,1)^2\setminus Z\), \(\mu\)-null |
| **L6.1** | pointwise on \((-1,1)^2\) / on \(Y\) | none |
| **L6.2** | pointwise on \(Y\) | none |
| Claim 6.3.1 | \(\mu_U(Y)=1\); \(\mu_X=P_*\mu_U\) as measures | \((-1,1)\setminus Y\), \(\mu_U\)-null |
| **Claim 6.3.2** | **pointwise on \((-1,1)\)** — the key strengthening | **none** |
| Claim 6.3.3 | measure statement (null \(\iff\) null) | none |
| Claim 6.3.4 | \(\mu_U(D_{\mathbf b})=1\); invariance pointwise | \((-1,1)\setminus D_{\mathbf b}\), \(\mu_U\)-null |
| Claim 6.3.5 | \(\mu_U(D_{\mathbf a})=1\); invariance pointwise | \((-1,1)\setminus D_{\mathbf a}\), \(\mu_U\)-null |
| Claim 6.3.5′ | for every Borel \(E\subseteq D_{\mathbf a}\) | none |
| Claim 6.3.6 | \(\mu_U(G_w)=1\) for each of countably many \(w\) | \(D_0\setminus G_w\), each \(\mu_U\)-null |
| Claim 6.3.7 | \(\mu_U(Y_0)=1\); (2),(3),(4) pointwise on \(Y_0\) | \((-1,1)\setminus Y_0\), \(\mu_U\)-null |
| Claim 6.3.8 | pointwise on \(Y_0\) | none |
| **L6.4** | pointwise on \(Y_0\) | none |
| **L6.5** | universal over Borel \(E\subseteq Y_0\) | none — **and none upstream either** (v0.2: (RN-X)/(RN-U) are derived in L6.3 from the pre-division identity A13′ and \(b^2>0\) pointwise, so A16's a.e. qualifier is never consumed as a premise) |
| **L7.1** | pointwise on \(Y_0\) | none |
| **L7.2** | pointwise on \(F\) | none |
| **L7.3** | hypothesis pointwise on \(F\); **conclusion \(\mu_U\)-a.e. on \(F\)** | \(N_1=\{u\in F:r_A(P(u))\ne r_B(u)\}\), \(\mu_U\)-null |
| **L7.4** | pointwise on \(F\) | none |
| **L7.5** | pointwise on \(F^\ast=F\setminus N_1\) | \(N_1\) |
| **L7.6** | pointwise on \(F^\ast\) (a contradiction at a single point) | \(N_1\) |
| **L7.7** | \(\mu_U(F)=0\) — measure statement, obtained by a.e.\(\to\)existence over the single conull set \(C_1=F^\ast\) | \(N_1\) |
| **L8.1–L8.6** | **pointwise on \(Y_1=Y_0\setminus F\)** | none inside \(Y_1\) |
| **L8.7** | the audit itself | \(((-1,1)\setminus Y_0)\cup F\), \(\mu_U\)-null |
| **L9.1(1),(2)** | every \(t\in T\) | none |
| L9.1(3),(4) | every Borel \(E\) / every Borel \(f\ge0\) | none — \(T\setminus T_{\rm good}\) is absorbed by the \(\delta_t\) redefinition **for (3) and (4) only**; see the row note below (v0.2, R12) |
| **L9.1(5)** | **\(\nu\)-a.e. \(t\)** | \(M=\bigcup_iM_i\), \(\nu\)-null |
| **L9.2** | (1) pointwise on \(Y_1\); (2),(3) every \(t\), every Borel \(E\) | none |
| **L9.3** | **\(\nu\)-a.e. \(t\)** | \(N_2\subseteq T\), \(\nu\)-null (union of four) |
| **L9.4(1),(2)** | **every \(t\in T\)** (pointwise; stronger than CERT:735–737) | none |
| L9.4(3) | \(\nu\)-a.e. \(t\) | depends on \(N\) |
| **L9.5** | \(\nu\)-a.e. \(t\) (namely \(t\notin N_2\)); then pointwise over the whole orbit | \(N_2\) |
| **L9.6** | existence of one \(t^\ast\); I1–I9 pointwise at \(t^\ast\) | \(N_2\) |

**Row note on the \(\delta_t\) redefinition — CORRECTED IN v0.2 (R12,
adversary attack 11).** v0.1's table said flatly that \(T\setminus T_{\rm
good}\) is "absorbed by the \(\delta_t\) redefinition". **That is true only for
L9.1(3) and (4)**, where the redefinition is invisible because
\(\nu(T\setminus T_{\rm good})=0\) and the identities are integrals against
\(\nu\). It is **not** the mechanism at L9.3, L9.5 or L9.6:

- The fibres \(\mu_t=\delta_t\) for \(t\notin T_{\rm good}\) are **inadmissible**
  for the transport conclusions — a single point mass at \(t\) cannot satisfy
  \(\mathbf b_*\mu_t=r_B^2\mu_t\) unless \(\mathbf b(t)=t\), which is false on
  \(Y_1\) (fixed points were removed at L7.7).
- They are excluded not by absorption but **by definition of \(N_2\)**: \(N_2\)
  is the \(\nu\)-null set off which all four conclusions of L9.3 hold, and
  \(T\setminus T_{\rm good}\subseteq N_2\) automatically, since the conclusions
  fail on it. L9.5 and L9.6 then quantify over \(t\notin N_2\), so no
  \(\delta_t\) fibre is ever selected.

The distinction is bookkeeping, not mathematics — the sets involved are
\(\nu\)-null either way — but stating it wrongly invites the reading that a
\(\delta_t\) fibre could be the \(t^\ast\) of L9.6, which it cannot.

**Total null-set budget.** The entire argument consumes exactly:

- \(\mu\)-null: \(E_\partial\) and \(\{\phi\ne0\}\) (A9, A10) — Claim 0.2;
- \(\mu_U\)-null: \((-1,1)\setminus D_{\mathbf a}\),
  \((-1,1)\setminus D_{\mathbf b}\), the countably many \(D_0\setminus G_w\),
  and \(N_1\) — assembled into \((-1,1)\setminus Y_1\);
- \(\nu\)-null: \(M\) (uniqueness) and \(N_2\) (normalization).

Nothing else. There is no place where an a.e. statement is used as if pointwise:
the two a.e.\(\to\)pointwise transitions are **L7.7** (positive measure
\(\Rightarrow\) non-empty) and **L9.6** (conull \(\Rightarrow\) non-empty), and
both are written explicitly.

**Two accounting corrections in v0.2 (B3/M3).** (i) The \(\mu_U\)-null list
above is unchanged, but the *reason* \((-1,1)\setminus D_{\mathbf a}\) is null
is now recorded correctly: it comes from the (\(\Rightarrow\)) half of Claim
6.3.3 alone (Claim 6.3.5), not from strict positivity of \(r_A\). (ii) Claim
6.3.2's pointwise positivity is charged to its three genuine consumers —
\(\rho\in(0,\infty)\) at L7.5/L7.6, atom propagation at L9.5(2), and the
single-conull-set count at L7.7 — and **not** to Claims 6.3.3/6.3.5/6.3.5′ or
to the induction of Claim 6.3.6, which survive an a.e.-only positivity
hypothesis. This does not change any null set in the budget; it changes which
lemma each one is attributed to.

---

# OX.4 — Axiom inventory

**Used.**

1. **ZFC**, with countable choice only in the form of choosing one point from a
   non-empty set (L7.7, L9.6) — actually no choice at all, as both are single
   choices.
2. **Standard Borel space facts, cited as [standard], with reason:**
   - *Lusin–Souslin*: an injective Borel image of a Borel subset of a Polish
     space is Borel, and the inverse injection is Borel — L6.1(4). *(Only place
     descriptive set theory is genuinely consumed. The Borel-ness of \(P\)
     itself is proved elementarily from monotonicity, also in L6.1(4).)*
   - *A Borel subset of a Polish space is standard Borel* — L8.6(5).
   - *Countable first-rational selection*: a minimum over a countable index set
     of Borel conditions has Borel level sets — L8.2(3).
   - *A function Borel on each of countably many Borel pieces partitioning its
     domain is Borel* — Claim 8.4.1, L9.1 Step 3(2).
   - *Radon–Nikodym for finite measures* — L9.1 Step 2. *(v0.2: the derivation
     of (RN-X)/(RN-U) in L6.3 does **not** use Radon–Nikodym; it divides the
     measure identity (6.3.0) by the strictly positive finite Borel function
     \(b^2\), which is elementary. Whether the certificate's own passage from
     A13′ to the boxes A14/A15 is read as R–N or as scalar division is
     immaterial here, since this document re-derives it.)*
   - *Monotone convergence / standard measure theory* — throughout.
3. **The promoted inputs of the certificate and its package**, exactly the rows
   of OX.1 **as corrected in v0.2** — namely: CERT §§1–5 displays; CZS §§2–7
   displays; **CEPE §§7–9 (row A6′), which v0.1's inventory omitted although
   Lemma 6.1(2),(3) depends on it**; **the Sprint-1197/1287 generic weld
   displayed at MAN:498–507 (row A7′), which v0.1 consumed in Claim 0.1 without
   listing it**; FR Receipts (iii),(iv); and the Lean kernel of item 4. No
   CERT §§6–9 display is used as an input (they are the output) — the one v0.1
   header that listed CERT:514–527 as an input to L6.5 was an error and is
   corrected (m7).

   *(**v0.2 correction, S1 + B1.** v0.1 wrote "exactly the rows of OX.1: CERT
   §§1–5 displays and CZS §§2–7 displays." **Both halves of that sentence were
   false as written**: the inventory was not exhaustive (CEPE and the weld were
   consumed but unlisted), and the sources are not confined to CERT and CZS.
   The corrected sentence above is exhaustive against the corrected OX.1.)*
4. **The Lean kernel** `I3322Kernel.QuarterCeiling`: `quarter_ceiling`
   (QC:77–90) and `quarter_lt_window_lower` (QC:95–97), with hypotheses
   discharged in L7.6 Step 6.

**Deliberately NOT used (and flagged if a reader thinks otherwise).**

- **No Rokhlin disintegration theorem.** L9.1 constructs the disintegration by
  hand from Radon–Nikodym and countability of fibres.
- **No abstract "uniqueness of probability disintegration."** L9.1(5) proves
  the needed uniqueness directly. This retires the CERT:705 black box.
- **No Becker–Kechris / Burgess smoothness machinery.** L8.5–L8.6 exhibit the
  transversal and the retraction \(\pi\) explicitly; "smooth" is a *conclusion*,
  not an input.
- **No measurable selection theorem** (Jankov–von Neumann, Kuratowski–Ryll-
  Nardzewski). The only selections are the first-rational one (L8.2(3)) and the
  lesser-of-two (L8.5(4)), both explicit Borel formulas.
- **No joint-support symmetry assumption** on \(\operatorname{supp}\mu\) — see
  SCOPE FLAG 6.1.A for why this matters and how it is avoided.
- **No symmetry assumption on \(g\)** — CZS:136 is explicit that the
  \(R_0\)-involution is *not* such an assumption; L6.2 re-derives it from
  \(B=A\circ(-\mathrm{id})\) and \(d(-u,-x)=d(x,u)\).
- **No Sprint-1195 objects**, per CERT:78–79 and CERT:1088.

**New axioms introduced by this document: none.** *(v0.2, S1: this line stands,
but v0.1 paired it with the false "exactly the rows of OX.1" sentence, which
made it read as a self-containedness claim it could not support. The precise
statement is: **no axiom is introduced, and no unlisted input is consumed** —
the second half being true only after the v0.2 additions of rows A6′, A7′,
A13′, A15′ and A2′. The adversary was right that this was the one place a GAP
block was owed and not given; it is now discharged by anchoring rather than by
a GAP, since the sources exist in the public repository.)*

---

# Findings register (for the blind gate)

| id | kind | content | disposition |
|---|---|---|---|
| **F1** | **SCOPE FLAG 6.1.A** | CERT:73 asserts the graph property for "the **full** interior zero locus"; CERT:1073 points at Theorem (N), whose FR Receipt (ii) box (FR:177–179) states it only "**on the occupied interior support**". The occupancy qualifier would break L6.2, which needs the domain closed under \((x,u)\mapsto(-u,-x)\) — free on the full locus, but on the occupied support it would additionally require \(\operatorname{supp}\mu\cap(-1,1)^2\) to be \((x,u)\mapsto(-u,-x)\)-invariant, which **nothing in the package establishes** (CERT §5 gives marginal quasi-invariance only). | **RESOLVED BY A BOXED THEOREM (downgraded in v0.2; B1/M1/R6, adversary attack 14).** The full-locus form is not an inference from a heading — it is proved and **boxed** at **CEPE:224**, "\(R_0^{-1}(0)\cap D^2\) is a one-to-one strictly increasing relation", with \(D:=(-1,1)\) at CEPE:15, horizontal exclusion on the full source domain at CEPE:177–194, vertical exclusion at CEPE:196–210, assembly at CEPE:212–225; the document is PROMOTED (CEPE:4) and CEPE:208–210 states its own scope. v0.1's claim that "CZS:124–125 are theorems" was **false** (they are one-line pointer sentences) and is retracted. **Action (CORRECTED):** re-anchor CERT:73 and CERT:1073 to `CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md` §§7–9, box CEPE:224; keep **CZS:115–126 as a secondary, strict-Monge-only anchor (CZS:121)**. v0.1's recommendation to re-anchor to CZS:115–126 is **withdrawn** — it would have pointed a public referee at two unproved appeals. This is no longer "the closest call" of the document. |
| **F2** | **CORRECTION 8.5.A** | The commission's O8.5 expects \(\mathbf b\) to map orbits "exchanging \(Y_+/Y_-\)". **False:** \(\tau\mathbf b=\mathbf b\tau^{-1}\) plus \(\mathbf b\) decreasing gives \(\mathbf b(Y_\pm)=Y_\pm\). What \(\mathbf b\) does is reverse the \(\mathbb Z\)-parametrisation *within* \(Y_+\) (resp. \(Y_-\)). Model witness: \(\tau(u)=u+1\), \(\mathbf b(u)=-u\) on \(\mathbb R\), where \(Y_-=\varnothing\). | **No impact.** CERT:665–673 never claims the exchange; only the commission does. L8.5(2)–(4) uses only the parametrisation reversal. |
| **F3** | **CORRECTION 0.A** | **Five** live symbol collisions in CERT (v0.1 recorded one; the other three CERT ones were added in v0.2 per R9). **(A)** \(b\): amplitude \(b(t)=\sqrt{1-t^2}/2\) (CERT:229) vs response involution \(b(u)=-u\) (CERT:489) — colliding inside a single display at **CERT:522–528**, where \(r_B=B/b\) hides the amplitude \(b\) under an involution \(b\). **(B)** \(A,B\): transport factors vs the commission's \(A:=S-xu+1\), \(B:=b(x)+b(u)\). **(C)** \(Y\): the operator \(A_2-A_1\) (CERT:203) vs the subset \(\operatorname{dom}P\subseteq(-1,1)\) (CERT:449) — **the most serious, because the whole of §6 is built on the second**. **(D)** \(q\): \(q_n\downarrow S\) (CERT:59) vs the rational enumeration \(q_k\) (CERT:644) and \(q(u)\) (CERT:650) — **and v0.1 of this document reproduced the collision itself**. **(E)** \(\pi\): the GNS representation (CERT:98) vs the orbit quotient (CERT:678); this document adds \(\pi_x,\pi_u,\pi_{\mathbb Z}\). | **Legibility defect (five instances).** This document uses \(\mathbf a,\mathbf b\) bold for the involutions, \(\Sigma,\Lambda\) for the commission's \(A,B\), reserves \(Y\) for subsets of \((-1,1)\), and — **new in v0.2** — renames its own rational enumeration to \(\theta_k\), \(\theta(u)\) (Lemmas 8.2–8.4), removing the \(q\) collision it had inherited. Recommend all five conventions in the public amendment; (C) and (D) are the two that can actually mislead a reader of §§6–8. |
| **F4** | **supplied missing step** *(scope corrected in v0.2, S1/R1)* | CERT never displays \(\phi=R_0\) (needed to import CZS's results about \(R_0^{-1}(0)\) into CERT's \(Z=\{\phi=0\}\)) nor \(\mu_X=P_*\mu_U\) (needed for every use of the X-side RN law on the U-side). **And the scalarisation inside Claim 0.1 itself consumes a third item CERT never displays: the generic weld \(\mathcal B=d(X,U)+W+W_B\)**, which CERT only *names* at CERT:1078–1079. v0.1 called F4 a "supplied missing step" while itself resting on that unanchored identity — the one place this document owed a GAP block and did not give one. | Supplied as **Claim 0.1** and **Claim 6.3.1**. The weld is now **displayed and anchored** inside Claim 0.1 at **MAN:498–507** (display (0.1.W); OX.1 row A7′), with the two response blocks shown cancelling exactly; the LaTeX twin is `manuscript.tex:436` and the S1 referee's independent replication is at SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md:284–288. No GAP block is needed: the source exists in the public repository. Recommend all three be displayed in the amendment — the weld first, since \(\phi=R_0\) depends on it. |
| **F5** | **supplied missing derivation** | CERT:514–519 displays the \(\mathbf a\)-transport law \(\mu_U(\mathbf aE)=\int_E r_A(P(u))^2d\mu_U\) with no derivation. | Derived as **Claim 6.3.5′** from A14 + Claim 6.3.1. |
| **F6** | **black box retired** | CERT:705 "Uniqueness of probability disintegration" — an unnamed, uncited appeal, and one of the three disclosed residual risks. | Replaced by **L9.1(5)**, proved from Radon–Nikodym + countable fibres. |
| **F7** | **prose appeal replaced** | CERT:604 "The audited Sprint-1198 elimination then gives \(S\le1/4\)" — no display, no anchor. | Replaced by **L7.6 Steps 1–5** (hand-checkable) **+ Step 6** (machine-checked `quarter_ceiling`, QC:77–90). |
| **F8** | **interface binding** | §10's \(\mu_t\) has no enumerated antecedent (CERT:742 says only "having all these properties"). | **L9.6 I1–I9** enumerates them; recommend inserting the binding at CERT:748. See OX.2 caution. |

**GAP blocks: none.** Every obligation O6.1–O9.6 and OX.1–OX.4 is discharged
from the stated inputs — where "the stated inputs" now means the **corrected**
OX.1, including rows A6′ (CEPE) and A7′ (the generic weld), whose absence from
v0.1 was the substance of blocker B1 and defect S1. F1 is no longer the closest
call: it is resolved by a **boxed theorem** that exists (CEPE:224), and is
recorded as a *citation* defect of the certificate, not a mathematical gap.

## Gate receipts — positive results recorded from round 1 (v0.2)

Two of the round-1 adversary's twenty-two attacks produced *confirmations* that
the document should carry, because each is a check that could have failed and
did not. Both are attributed to the round-1 countermodel-hunting adversary
(`VERDICT-U2-AUDITOR-2-ADVERSARY.md`) and are recorded here as evidence, not as
new claims of this document.

**GR-1 — the self-paired point of a \(\mathbf b\)-invariant orbit: \(r_B(0)=1\)
(attack 3, sub-case \(k\) even).** The adversary built explicit
\(\mathbf b\)-invariant dihedral orbits end-to-end to attack Lemma 8.5(3)
case (a): case (b) via \(Y_0=\{n\pm 1/3\}\), case (a) via \(Y_0=\{n+1/2\}\) with
\(k\) odd. The sub-case \(k\) **even** forces a *self-paired* point
\(v\) with \(\mathbf b(v)=v\), i.e. \(v=0\). Interface item **I4** then reads
\(\mu_\ast(\{\mathbf b(0)\})=r_B(0)^2\mu_\ast(\{0\})\) with
\(\mathbf b(0)=0\), which **forces \(r_B(0)=1\)** — a constraint on the
*analytic* data \(g,b\) imposed by the *combinatorial* structure of the orbit.
It holds: \(B(0)=b(0)\) identically, since \(B(0)=\sqrt{g(0)p(-0)}
=\sqrt{g(0)b(0)^2/g(0)}=b(0)\), so \(r_B(0)=B(0)/b(0)=1\). The two sides are
independent — nothing in the construction of \(Y_0\) or \(\mathcal O\) knows
about the value of \(g\) at the origin — so this is a genuine consistency check
between §9's interface and §5's transport factors, and it passes non-trivially.
*Recorded as a positive receipt at the adversary's explicit request.*

**GR-2 — the §7 elimination has a strictly positive numeric margin (attack A2
numeric confirmation, adversary's own engine).** The centrepiece identity of
Lemma 7.6 was independently recomputed:
\[
E:=\bigl(b(x)+b(u)\bigr)^2+\frac{(x-u)^2}{4}
=\frac{1+\sqrt{(1-x^2)(1-u^2)}-xu}{2},
\]
exact to \(10^{-12}\) over \(4\times10^5\) random points; \(E\le1-xu\)
everywhere; and \(\sup\bigl(xu-1+\sqrt E\bigr)=1/4\), **attained only at
\(x=u=-\sqrt3/2\)**. At the certified value \(S=0.2508753845015185\),
\[
\min\bigl(\Sigma^2-\delta^2-\Lambda^2\bigr)=+8.75\times10^{-4}>0
\]
on a \(3000^2\) grid, while at \(S=1/4\) the same quantity touches \(0\).
So the contradiction of Lemma 7.6 Step 5 — which requires
\(\Sigma^2-\delta^2=\Lambda^2\) exactly — is not a marginal cancellation: the
system (7.6.3) is infeasible at the certified \(S\) with a **strictly positive
margin**, and the margin closes exactly at the quarter ceiling, as the Lean
theorem `quarter_ceiling` (QC:77–90) requires. The extremiser
\(x=u=-\sqrt3/2\approx-0.866\) lies **inside** CZS:130–131's reconnaissance
source range \([-0.8936,+0.8981]\), so no range-based evasion of the elimination
is available. *This is an independent second engine on the document's
centrepiece, and it agrees.*

---

*End of U2 EXPANSION DRAFT v0.2 (repair round on
`VERDICT-U2-AUDITOR-1-PROOF.md` and `VERDICT-U2-AUDITOR-2-ADVERSARY.md`).*
