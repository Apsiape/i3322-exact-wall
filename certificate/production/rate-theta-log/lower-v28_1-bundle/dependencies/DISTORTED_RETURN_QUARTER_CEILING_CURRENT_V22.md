# Current Distorted-Return Quarter Ceiling — v22

**Date:** 2026-08-06  
**Status:** exact scalar theorem.  
**Purpose:** derive the cycle ceiling

\[
F(q)=\frac14+\frac{(1-q)^2}{16q}
\]

directly from the current multiplicity-uniform return equations.

---

## 1. Exact return datum

Let

\[
b(t)=\frac{\sqrt{1-t^2}}2,
\qquad
 d(x,u)=xu+\frac{x-u}{2}-1.
\]

Suppose one exact scalar return sector has positive response gains

\[
\alpha>0,\qquad\beta>0
\]

and satisfies the two current component equalities

\[
\boxed{
Q
=
d(x,u)+\alpha b(x)+\beta b(u),
}
\tag{1.1}
\]

\[
\boxed{
Q
=
d(-x,-u)+\frac{b(x)}\alpha+\frac{b(u)}\beta.
}
\tag{1.2}
\]

These are the two multiplicity-uniform norm-ratio equations obtained by
traversing the two reflected response sides of a closed scalar component.
No equality \(\alpha=\beta\) is assumed.

Put

\[
q=\frac\alpha\beta.
\]

If \(q>1\), reverse the orientation and replace \(q\) by \(1/q\). Hence it is
enough to consider

\[
0<q\le1.
\]

---

## 2. Weighted return identity

Set

\[
p=\alpha\beta,
\qquad
\lambda=\frac1{1+p}.
\]

Since (1.1) and (1.2) have the same left side,

\[
Q=\lambda(1.1)+(1-\lambda)(1.2).
\]

Define

\[
h=\frac{1-p}{1+p},
\qquad
\gamma=\frac{2\sqrt p}{1+p}.
\]

Then

\[
h^2+\gamma^2=1.
\tag{2.1}
\]

Write

\[
r=\sqrt q,
\qquad
c=r+\frac1r\ge2.
\tag{2.2}
\]

Because

\[
\alpha=\sqrt p\,r,
\qquad
\beta=\frac{\sqrt p}{r},
\]

we have

\[
\frac{\alpha+\beta}{1+p}
=
\frac{c\gamma}{2}.
\]

Using

\[
\lambda d(x,u)+(1-\lambda)d(-x,-u)
=
xu-1+\frac h2(x-u),
\]

and \(b(t)=\sqrt{1-t^2}/2\), the exact return value is

\[
\boxed{
Q
=
xu-1
+\frac h2(x-u)
+\frac{c\gamma}{4}
\left(\sqrt{1-x^2}+\sqrt{1-u^2}\right).
}
\tag{2.3}
\]

---

## 3. Two-coordinate compression identity

Put

\[
s_x=\sqrt{1-x^2},
\qquad
s_u=\sqrt{1-u^2},
\]

\[
A=s_x+s_u,
\qquad
D=x-u,
\qquad
R^2=A^2+D^2.
\]

If \(R=0\), the desired bound is immediate. Assume \(R>0\).

Let

\[
t=1-xu,
\qquad
p_s=s_xs_u.
\]

The exact identities

\[
R^2=2(t+p_s),
\tag{3.1}
\]

and

\[
D^2=t^2-p_s^2=(t-p_s)(t+p_s)
\tag{3.2}
\]

give

\[
\boxed{
1-xu
=\frac{R^2}{4}+\frac{D^2}{R^2}.
}
\tag{3.3}
\]

Therefore (2.3) becomes

\[
Q
=
-\frac{R^2}{4}
-\frac{D^2}{R^2}
+\frac h2D
+\frac{c\gamma}{4}A.
\tag{3.4}
\]

Write

\[
A=R\cos\theta,
\qquad
D=R\sin\theta.
\]

Dropping the nonpositive term \(-\sin^2\theta\),

\[
Q
\le
-\frac{R^2}{4}
+R\left(
\frac h2\sin\theta
+\frac{c\gamma}{4}\cos\theta
\right).
\]

For fixed \(\theta\), the right side is at most the square of the linear
coefficient:

\[
Q
\le
\left(
\frac h2\sin\theta
+\frac{c\gamma}{4}\cos\theta
\right)^2.
\]

Cauchy--Schwarz gives

\[
Q
\le
\frac{h^2}{4}+\frac{c^2\gamma^2}{16}.
\]

Using \(\gamma^2=1-h^2\) and \(c\ge2\),

\[
\frac{h^2}{4}+\frac{c^2\gamma^2}{16}
=
\frac{c^2}{16}
-\frac{c^2-4}{16}h^2
\le
\frac{c^2}{16}.
\]

Thus

\[
\boxed{
Q\le\frac{c^2}{16}
=\frac{(1+q)^2}{16q}
=\frac14+\frac{(1-q)^2}{16q}.
}
\tag{3.5}
\]

This proves the distorted-return ceiling.

---

## 4. Equality and quarter ceiling

At \(q=1\),

\[
c=2
\]

and (3.5) becomes

\[
\boxed{Q\le\frac14.}
\]

Thus the promoted exact finite-return quarter ceiling is the neutral-return
member of the stronger one-parameter family (3.5).

For fixed \(q\), equality in the proof requires in particular \(h=0\), hence

\[
\alpha\beta=1,
\]

and \(x=u\) at the scalar optimum. Then

\[
\alpha=\sqrt q,
\qquad
\beta=1/\sqrt q
\]

up to reversed orientation.

---

## 5. Exact current return gap

Let

\[
q_0=889/1000.
\]

Since

\[
F'(q)=\frac{q^2-1}{16q^2}\le0
\qquad(0<q\le1),
\]

for every \(q\in[q_0,1]\),

\[
F(q)\le F(q_0).
\]

With the certified current lower wall

\[
S_-=0.2508753845015185,
\]

exact arithmetic gives

\[
\boxed{
S_--F(q_0)
=
\frac{16308643699893}{1778000000000000000}
>0.
}
\tag{5.1}
\]

This is the scalar gap consumed by the v22 compact-stability cycle theorem.

---

## 6. Dependency boundary

Used:

- the current multiplicity-uniform two-sided response component equations
  (1.1)--(1.2);
- elementary scalar identities and Cauchy--Schwarz;
- the certified current lower wall only for the numerical/rational gap (5.1).

Not used:

- C034;
- a historical shooting ratio;
- scalar holonomy;
- operator-fibre rigidity;
- exact wall-value identification.
