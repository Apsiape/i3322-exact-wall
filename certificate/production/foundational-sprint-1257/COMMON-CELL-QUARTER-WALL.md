# The quarter wall survives a common coarse cell

Status: **proved pointwise stable wall; response-flow variation remains
open**

## 1. The sharper unrounded wall

Sprint 1253 proves, before its final substitution into the composed
translation, that every active contact coordinate `r` obeys

```text
m_0 <=(182/5)|a(r)+r|
      +(169/50)|log(alpha(r))-log(beta(r))|,         (1)

m_0=q_*-1/4.                                        (2)
```

The same certified active box gives

```text
Lip(a)<=20,
Lip(log(alpha))<=14,
Lip(log(beta))<=7.                                  (3)
```

## 2. Replace the representative by the coupled event

Let `(y,u,zeta)` lie in the retained common-cell measure of Sprint 1256.
Thus `y` and `u` lie in one half-open cell of width `h`.  Choose any
representative `r` in that cell and put

```text
p(y)=2 log(alpha(y)),
q(u)=2 log(beta(u)).                                (4)
```

Because all three coordinates are in the same cell,

```text
|a(r)+r|
 <=|a(y)+u|+20|r-y|+|r-u|
 <=|a(y)+u|+21h,                                   (5)

|log(alpha(r))-log(beta(r))|
 <=|p(y)-q(u)|/2+14|r-y|+7|r-u|
 <=|p(y)-q(u)|/2+21h.                              (6)
```

Substituting (5)--(6) into (1) gives the exact coarse stability law

```text
boxed:
m_0 <=(182/5)|a(y)+u|
      +(169/100)|p(y)-q(u)|
      +(41769/50)h.                                (7)
```

Indeed

```text
21[(182/5)+(169/50)]=41769/50.                     (8)
```

Therefore, whenever

```text
h<=25m_0/41769,                                    (9)
```

every retained event obeys

```text
boxed:
m_0/2 <=(182/5)|a(y)+u|
         +(169/100)|p(y)-q(u)|.                    (10)
```

## 3. Why this is the correct intermediate theorem

Equation (10) is stated on the **actual** response outputs and translations
of the canonical joint coupling.  It does not identify spectral atoms,
round output coordinates, or localize a response vector.  Consequently the
cell operation has consumed only the explicitly billed source mismatch from
Sprint 1256.

The remaining gate is now sharply typed.  The two actual pushed output
measures must be approximated by decreasing finite lists while bounding the
resulting total-variation flow `V` of Sprint 1255.  Equation (10) guarantees
that any matched fixed component then carries a nonzero horizontal or
vertical displacement; it does not itself supply the required variation
bound or a universal dimension law.

