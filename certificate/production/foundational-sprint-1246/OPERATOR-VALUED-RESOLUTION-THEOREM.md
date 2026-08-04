# Response multipliers generate operator-valued resolution

Status: **exact noncommutative extension of the resolution-scale lift**

## Theorem

Let `D` be any finite coefficient operator, let

```text
rho=DD^*,       W_t(D)=rho(tI+rho)^(-1),             (1)
```

and let `C` be positive and invertible. Then

```text
W_t(CD)
 =C [rho(t C^(-2)+rho)^(-1)] C^(-1).                (2)
```

No commutation between `C` and `rho` is assumed.

## Proof

Factor the resolvent exactly:

```text
tI+C rho C=C(t C^(-2)+rho)C.                        (3)
```

Therefore

```text
(tI+C rho C)^(-1)
 =C^(-1)(t C^(-2)+rho)^(-1)C^(-1).                 (4)
```

Multiplying `C rho C` by (4) proves (2).

If `E` is any projection commuting with `C`, cyclicity gives the flag identity

```text
Tr[E W_t(CD)]
 =Tr[E rho(t C^(-2)+rho)^(-1)].                    (5)
```

It is not necessary for `E` to commute with `rho`.

The right-support analogue follows by applying the same proof to `D^*`:

```text
W_t^R(DC^T)
 =C^T [rho_R(t(C^T)^(-2)+rho_R)^(-1)](C^T)^(-1),   (6)
```

where `rho_R=D^*D`.

## Relation to Sprint 1245

When `[C,rho]=0`, equation (2) reduces on a `C=c` block to

```text
W_t(CD)=W_(t/c^2)(D).                               (7)
```

Thus scalar logarithmic translation is the commutative shadow of a more
general operation:

```text
scalar resolution tI  ->  anisotropic resolution tC^(-2).               (8)
```

For I3322, `C_A` and `C_B` are functions of the ordered contact coordinates,
so every cumulative spectral flag commutes with the corresponding resolution
metric. Equation (5) is therefore the correct flag-level object even away
from exact decomposability.

This removes one anticipated near-contact commutator problem. The unresolved
issue is relative: the two response metrics must still be composed on the
same contact flag and charged in finite rank.
