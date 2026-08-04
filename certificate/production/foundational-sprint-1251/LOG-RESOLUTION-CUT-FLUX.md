# Averaging logarithmic resolution prices every boundary crossing

Status: **proved full-measure flux theorem; order/contact closure still open**

## 1. Abstract cut theorem

Let `mu` be a finite positive measure on `Omega x R`, with total mass `d`.
For measurable shifts `h_j:Omega->R`, suppose

```text
|h_j(u)|<=B_j.                                        (1)
```

At depth `L`, retain the upper vertical tail `zeta>=-L` and define

```text
Flux_j(L)
 =integral |1_{zeta>=-L}-1_{zeta+h_j(u)>=-L}| dmu.   (2)
```

For one event `(u,zeta)`, the two indicators differ precisely while the moving
boundary `-L` lies between `zeta` and `zeta+h_j(u)`.  The set of such `L` has
length at most `|h_j(u)|`.  Tonelli therefore gives

```text
integral_0^H Flux_j(L) dL<=B_j d.                    (3)
```

Summing over `m` response maps and averaging proves that some `L in [0,H]`
satisfies

```text
sum_(j=1)^m Flux_j(L)
 <=d(sum_j B_j)/H.                                   (4)
```

This theorem uses the complete measure.  No sector is declared invariant and
no complement is deleted: every inbound or outbound crossing is counted in
(2).

## 2. The cut retains a nonzero core

For the Schmidt event measure, Sprint 1248 identifies the retained mass as

```text
M_L=Tr W_(exp(-L))(rho).                              (5)
```

If `Tr rho=1` and `L>=0`,

```text
M_L>=1/[1+exp(-L)]>=1/2.                             (6)
```

Thus the averaged cut cannot win merely by moving below all relevant state
mass.  It simultaneously has controlled response flux and a
dimension-independent occupied core.

## 3. I3322 specialization

The two equality-case response shifts are

```text
h_A(u)=2 log alpha(u),
h_B(u)=2 log beta(u).                                 (7)
```

Sprint 1216's certified amplitude ratio bound gives

```text
|h_A|,|h_B|<=2 log(13/2).                            (8)
```

Since the event measure has total mass at most the local dimension `d`, choose

```text
H=kappa d.                                            (9)
```

Equations (4) and (8) yield a cut with

```text
Flux_A(L)+Flux_B(L)
 <=4 log(13/2)/kappa.                                (10)
```

The right side is independent of dimension.  Increasing `kappa` makes the
boundary bill smaller than any fixed closure tolerance.

At this cut, `t=exp(-L)>=exp(-kappa d)`.  Sprint 1249 bounds each rank-`k`
response rectangle error by

```text
(9/2)sqrt(k epsilon_sigma/t)
 <=(9/2)sqrt(d epsilon_sigma) exp(kappa d/2).         (11)
```

Therefore any fixed positive closure tolerance would force an inequality of
the shape

```text
sqrt(d epsilon) exp(kappa d/2)>=constant,

epsilon>=constant*d^(-1)*exp(-kappa d).              (12)
```

Equation (12) is not yet asserted for I3322 because the fixed closure
tolerance has not been transferred from the Bellman matrix inequality to the
two event-measure response pushforwards.  What is now proved is the part the
packet route lacked: the response restriction can always be chosen with every
boundary crossing explicitly and dimension-independently charged.

## 4. Exact remaining lemma

It is enough to prove a grid-free closure statement of the following type at
the cut selected above:

```text
retained event mass >=1/2
+ both response rectangle errors small
+ contact flag error small
+ total vertical flux small
=> q_*<=1/4+controlled error.                         (13)
```

The coefficient `q_*-1/4` is already certified.  The unresolved work is now a
measure-coupling inequality, not localization, rank counting, or response
stability.

