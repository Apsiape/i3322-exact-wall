# Trace normalization makes the upper event boundary cheap

Status: **proved dimension-free cap; lower-boundary selection remains
separate**

## 1. Exact upper-tail mass

For the order--resolution event measure of a density operator `rho`, Sprint
1248 gives

```text
mu({zeta>=S})=Tr W_(exp(S))(rho)
             =Tr rho[exp(S)I+rho]^-1.               (1)
```

Since `rho>=0`, scalar functional calculus gives

```text
rho[exp(S)I+rho]^-1 <=exp(-S)rho.                   (2)
```

Using `Tr rho=1`,

```text
boxed: mu({zeta>=S})<=exp(-S).                      (3)
```

This estimate is independent of Schmidt rank.

## 2. Response crossing at the upper cap

Let a response translate resolution by `h(u)` with `|h(u)|<=B`.  An event can
cross the upper boundary `S` only if its original resolution satisfies

```text
zeta>=S-B.                                          (4)
```

Therefore the total crossing mass of one response is at most

```text
exp(B-S).                                           (5)
```

For the two I3322 responses together the safe bill is

```text
2 exp(B-S).                                         (6)
```

Choosing `S=B+log(1/eta)` makes that bill at most `2 eta` without any
dimension dependence.

## 3. A finite band retaining state mass

For every lower depth `L>=0`, Sprint 1251 gives

```text
mu({zeta>=-L})>=1/2.                                (7)
```

Consequently the finite band

```text
[-L,S]                                              (8)
```

retains at least

```text
1/2-exp(-S).                                        (9)
```

The upper interface is controlled by (6).  The lower interface is exactly
the cut flux already controlled by logarithmic averaging.  Thus restricting
the sign-coherent theorem to a finite band does not revive an unpriced
complement.

This theorem does not yet construct common output prefixes or prove a
universal dimension lower bound.

