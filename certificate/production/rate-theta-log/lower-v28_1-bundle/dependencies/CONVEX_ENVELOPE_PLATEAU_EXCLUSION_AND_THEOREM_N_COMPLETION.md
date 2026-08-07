# Convex-Envelope Plateau Exclusion and Completion of Theorem (N)

**Date:** 2026-08-05  
**Status:** **Analytic promotion candidate; blind round-3 audit still required.**  
**Purpose:** Close the last open receipt without assuming a \(C^1\) storage and
without certifying globally unique first Bellman contact.

---

## 1. Critical storage and contact intercept

Let \(g\) be the continuous critical storage obtained by the limiting-weld
construction at the common value \(S\). On the occupied interior scalar
spectrum,

\[
g>0.
\]

The terminal-pivot representation proves that \(g\) is concave.

Define

\[
b(x)^2=\frac{1-x^2}{4},
\qquad
p(x)=\frac{b(x)^2}{g(x)},
\]

and

\[
C(x)
=
S+1-\frac{x}{2}-p(x).
\]

The first Bellman inequality is

\[
p(x)+g(u)\le S-d(x,u),
\]

or equivalently

\[
\boxed{
g(u)
\le
C(x)+\left(\frac12-x\right)u.
}
\]

At a first Bellman contact, equality holds.

---

## 2. One-sided derivative orientation

A finite concave function has finite one-sided derivatives at every interior
point and

\[
g'_-(x)\ge g'_+(x).
\]

Since \(g(x)>0\) and \(b^2\) is smooth,

\[
p'_\pm(x)
=
\frac{(b^2)'(x)}{g(x)}
-
\frac{b(x)^2g'_\pm(x)}{g(x)^2}.
\]

Therefore

\[
p'_+(x)-p'_-(x)
=
-\frac{b(x)^2}{g(x)^2}
\left(g'_+(x)-g'_-(x)\right)
\ge0.
\]

Consequently,

\[
\boxed{
C'_-(x)\ge C'_+(x).
}
\tag{2.1}
\]

Every nonsmooth corner of \(C\) points downward. There are no upward corners.

This statement requires only concavity and interior positivity. It does not
assume that \(g\) is piecewise linear or \(C^1\).

---

## 3. Lower convex envelope

Let

\[
H=\operatorname{conv}_{\!\downarrow}C
\]

be the greatest convex function below \(C\) on the endpoint-excluded compact
source interval.

The Bellman lower envelope depends only on \(H\):

\[
\boxed{
\inf_x
\left[
C(x)+\left(\frac12-x\right)u
\right]
=
\inf_x
\left[
H(x)+\left(\frac12-x\right)u
\right].
}
\tag{3.1}
\]

Indeed, \(H\le C\) gives one direction. Conversely, each point of \(H\) is
either a contact point with \(C\), or lies on a chord between two contact
points. Affine evaluation along that chord is a convex combination of the two
endpoint evaluations and cannot fall below the infimum obtained from \(C\).

---

## 4. Differentiability of the convex envelope

### Theorem 4.1 — No-kink theorem

\[
\boxed{
H\text{ is differentiable at every interior source point.}
}
\]

### Proof

Assume \(H\) has a convex kink at an interior point \(x_0\):

\[
H'_-(x_0)<H'_+(x_0).
\tag{4.1}
\]

If

\[
H(x_0)<C(x_0),
\]

then \(x_0\) lies in a connected component of the noncontact set
\(\{H<C\}\). On such a component, the greatest convex minorant is the chord
between its boundary contact points, hence is affine. It cannot have a kink.

Therefore \(H(x_0)=C(x_0)\). Put

\[
F=C-H\ge0.
\]

Since \(F(x_0)=0\),

\[
F'_-(x_0)\le0,
\qquad
F'_+(x_0)\ge0.
\]

Thus

\[
C'_-(x_0)\le H'_-(x_0),
\qquad
C'_+(x_0)\ge H'_+(x_0).
\]

Together with (4.1),

\[
C'_-(x_0)
\le
H'_-(x_0)
<
H'_+(x_0)
\le
C'_+(x_0),
\]

so

\[
C'_-(x_0)<C'_+(x_0),
\]

contradicting (2.1).

Hence \(H\) has no kink.

---

## 5. Plateau exclusion

For a fixed target \(u\), minimizing

\[
H(x)+\left(\frac12-x\right)u
\]

is equivalent to minimizing \(H(x)-ux\). A source \(x\) is active exactly
when

\[
u\in\partial H(x).
\]

Since \(H\) is differentiable,

\[
\partial H(x)=\{H'(x)\}.
\]

Therefore:

### Theorem 5.1 — Horizontal plateau exclusion

\[
\boxed{
\text{No source }x
\text{ can be a Bellman contact for two distinct targets.}
}
\]

This is obtained without a \(C^1\) representation of \(g\).

---

## 6. Reflection and vertical plateau exclusion

For the complete transport remainder,

\[
R_0(x,u)
=
S-d(x,u)-A(x)-B(u),
\]

the identities

\[
d(-u,-x)=d(x,u),
\qquad
B(u)=A(-u)
\]

give

\[
\boxed{
R_0(-u,-x)=R_0(x,u).
}
\tag{6.1}
\]

Suppose two distinct sources \(x_1\ne x_2\) share one full-zero target \(u\):

\[
R_0(x_1,u)=R_0(x_2,u)=0.
\]

Then

\[
R_0(-u,-x_1)=R_0(-u,-x_2)=0.
\]

The single source \(-u\) would serve two distinct targets, contradicting
Theorem 5.1.

Hence:

### Theorem 6.1 — Vertical plateau exclusion

\[
\boxed{
\text{No target in }R_0^{-1}(0)
\text{ can have two distinct sources.}
}
\]

---

## 7. Strict graph theorem for the equality locus

The strict Monge calculation gives, for any two full-zero pairs,

\[
(x_1-x_2)(u_1-u_2)\ge0.
\]

The plateau-exclusion theorems show that equality in either coordinate occurs
only when the two pairs coincide.

Therefore:

\[
\boxed{
R_0^{-1}(0)
\text{ is a one-to-one strictly increasing relation on the interior.}
}
\]

On the finite occupied scalar support of a hypothetical finite-dimensional
maximizer, it is therefore the graph of a strictly increasing bijection
between the occupied source and target sets.

---

## 8. Finite-dimensional contradiction

Assume a finite-dimensional tensor-product strategy attains \(S\).

The assembled receipts give:

1. a limiting equality module on its finite interior scalar support;
2. endpoint exclusion;
3. occupied support contained in \(R_0^{-1}(0)\);
4. the strict graph theorem above;
5. total decreasing response bijections \(a\) and \(b:u\mapsto-u\) on the same
   finite ordered support;
6. uniqueness of a decreasing bijection of a finite ordered set, hence
   \(a=b\);
7. the multiplicity-uniform amplitude elimination and quarter ceiling
   \[
   S\le\frac14.
   \]

But the certified lower strategy and common-value theorem give

\[
S>Q_{127}>\frac14.
\]

Contradiction.

Thus, pending blind verification of the assembled receipts,

\[
\boxed{
\text{No finite-dimensional tensor-product strategy attains }S.
}
\]

---

## 9. Authority boundary

This proof does not use:

- the decertified Sprint-1195 fixed point;
- reflected construction of the left wing;
- a \(C^1\) storage;
- global uniqueness of every first Bellman contact;
- DOC-C shooting or heteroclinic artifacts;
- spatial attainment.

The release protocol still requires blind round-3 verification before public
promotion.
