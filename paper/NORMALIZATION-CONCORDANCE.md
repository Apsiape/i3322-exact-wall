# Normalization concordance

This note removes normalization ambiguity between the repository theorem and
the principal I3322 conventions in the literature. All identities below are
checked by `release/normalization_concordance_verify.py` using exact integer
coefficient tables.

## 1. Repository and Pal--Vertesi projector convention

For projections `A1,A2,A3,B1,B2,B3`, the repository Bell operator is

```text
B = -A2-B1-2B2
    +A1B1+A1B2-A1B3
    +A2B1+A2B2+A2B3
    -A3B1+A3B2.
```

Holding Bob fixed, its three Alice best-response coefficients are

```text
B1+B2-B3,
B1+B2+B3-I,
-B1+B2.
```

Holding Alice fixed, its Bob coefficients are

```text
A1+A2-A3-I,
A1+A2+A3-2I,
-A1+A2.
```

These are exactly Eqs. (9)--(14) of Pal and Vertesi,
arXiv:1006.3032. No scaling or additive shift occurs. Their reported limiting
number `0.250875384514` is therefore the same quantity called `q_*` here.

## 2. Collins--Gisin probability table

Permute the settings by

```text
(A1,A2,A3)_CG = (A2,A1,A3),
(B1,B2,B3)_CG = (B2,B1,B3).
```

The marginal and joint coefficient table becomes

```text
        -2  -1   0
 -1 |    1   1   1
  0 |    1   1  -1
  0 |    1  -1   0
```

with local bound zero. This is the standard Collins--Gisin I3322 table.

## 3. Dichotomic full-correlation table

In the Collins--Gisin order put

```text
P_i=(I-A_i)/2,   Q_j=(I+B_j)/2,
```

where `A_i,B_j` are dichotomic observables. Direct substitution gives

```text
B_projector = -I + H_dichotomic/4,
```

where `H_dichotomic` has table

```text
       -1  -1   0
 -1 |  -1  -1  -1
 -1 |  -1  -1   1
  0 |  -1   1   0.
```

This is Eq. (6.36) of Araujo--Klep--Garner--Vertesi--Navascues (2026).
Consequently their full-correlation objective and the repository value obey

```text
<H_dichotomic>/4 = 1 + <B_projector>.
```

Any comparison of bounds must apply this affine shift.
