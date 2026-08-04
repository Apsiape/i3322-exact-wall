# Quantitative dimension necessity at the exact I3322 wall

Status: **conditional algebraic consequence; near-fixed response localization
is unproved and the theorem claim is withdrawn**

## Conditional theorem

Let `Q_d` be the largest value of the normalized I3322 functional among
tensor-product quantum strategies whose two local Hilbert spaces have
dimension at most `d`. Let `q_*` be the exact validated supremum of Sprint
1197. If the missing localized-response estimate described below holds, there
is a computable universal constant `c_*>0` such that, for every `d>=1`,

```text
q_*-Q_d
 >=c_* d^-4 Gamma^-d,
Gamma=(20*78/5)^4
     =312^4
     =9475854336.                                   (1)
```

Consequently every strategy with Bell deficit `epsilon` requires

```text
d >= [log(1/epsilon)-O(log log(1/epsilon))]/log Gamma. (2)
```

The exponent is intentionally crude. The displayed implication is not
presently a proved device-independent dimension bound.

## 1. Fixed constants and sectors

Let

```text
epsilon=q_*-<psi,B psi>
       =epsilon_0+epsilon_A+epsilon_B.               (3)
```

Use the certified active box and put

```text
mu=7/8000,
h_0=10^-7,
theta=10^-12,
Delta=theta h_0/20.                                  (4)
```

The pullback separation fraction on

```text
N={u:|tau(u)-u|<=Delta}                              (5)
```

is at most `theta`.

The first assembly incorrectly assigned one fixed positive gap to the whole
inactive sliver. Sprint 1232 supplies the correct saturated coordinate. Put

```text
I=P([-1,1]),
Y(x)=P^-1(clamp_I x).                                (6)
```

The complete rational response box obeys

```text
r_0(x,u)
 >=[(u-Y(x))^2+(x+Y(-u))^2]/40
   +[dist(x,I)^2+dist(u,I)^2]/400.                  (7)
```

The sliver is included in the saturated boundary cells. Its mean coordinate
and response-weight error is `O(sqrt(epsilon_0))`. Only the far endpoint
region outside the rational box has a fixed positive gap and is discarded.
No density of the joint spectral measure is used.

## 2. Near-fixed mass is `O(sqrt(epsilon))`

Apply the common-source/common-target construction of Sprint 1228 with mesh
`h_0`. Sprint 1229 gives, on captured pairs,

```text
(mu^2/2)W_c
 <=48 epsilon_0,c
   +(4656/25)(E_A,c^2+E_B,c^2).                     (8)
```

The coefficient `48` includes the possible double use of global contact mass
by the internally orthogonal source and target packet families; mutual
source--target orthogonality is not assumed.

The original assembly asserted that the two-frame theorem gives

```text
E_A,c^2+E_B,c^2
 <=6(epsilon_A+epsilon_B)+3 Gamma_c,                (9)
```

where `Gamma_c` is the sum of the four weighted source/target discard
masses. This is the unresolved step: the shifted pullback estimate controls
near-fixed occurrence omissions but not the full coarse complements in the
two-frame theorem. Restricting the response vector introduces an uncharged
commutator/flux term. Conditional on a new theorem controlling that term,
fixed-width shifted contact rounding would be proportional to
`sqrt(epsilon_0)/h_0`; with fixed `h_0`, and using the saturated coercivity
(7), every non-pullback
part is bounded by `C_c sqrt(epsilon)`. The pullback separation contributes
at most

```text
Gamma_c<=C_c sqrt(epsilon)+(26/5)theta mu(N).        (10)
```

The factor `26/5` is the conservative sum of four weight bounds `13/10`.
Likewise

```text
W_c>=(1-theta)mu(N)-C'_c sqrt(epsilon).              (11)
```

Substituting (9)--(11) into (8), the coefficient of `mu(N)` on the right is
at most

```text
(4656/25)*3*(26/5)*theta < 3000 theta.               (12)
```

Since `theta=10^-12` and `mu^2/4>10^-7`, this term is absorbed on the left.
Thus one fixed constant `C_N<infinity`, independent of `d` and of the
strategy, satisfies

```text
mu(N)<=C_N sqrt(epsilon).                            (13)
```

This is why the pullback fraction had to be chosen at the squared closure-gap
scale rather than merely below `1/16`.

## 3. Moving-grid loss on the drift sector

On `D=N^c` use the shifted predecessor grid of width

```text
h_d=Delta/(100*20^d).                                (14)
```

Through at most `d` nonlinear frames, every cell hull has diameter at most
`Delta/100`, so Sprint 1224's ordered-disjoint condition holds with slack on
every retained orbit segment. Sprint 1223's one-shift average over all needed
frames gives total unweighted off-contact/discard mass

```text
L_d
 <=C_L Delta^-1 20^(2d) sqrt(epsilon_0)
 <=C_L Delta^-1 20^(2d) sqrt(epsilon),              (15)
```

for one universal numerical `C_L`. This sum already includes every frame;
there is no additional cell-count or spectral-atom factor.

Measurable points whose orbit enters `N` or the far endpoint discard are
stopped at their first entry. Points that remain in `D` are grouped by their first-exit time. These
are Borel subsets of the moving interval cells. Their containing interval
hulls remain ordered and disjoint, so restricting to them preserves the
rank argument. This avoids assigning any uncontrolled mass to boundary cells.

## 4. Initial drift mass and the first case split

The initial paired drift mass obeys

```text
W_D>=1-C_D sqrt(epsilon)-L_d,                        (16)
```

where `C_D` collects the saturated-tail error from (7), (13), fixed-weight
cutoffs, and the initial contact discard.

If either `C_D sqrt(epsilon)>=1/4` or `L_d>=1/4`, then (1) follows after decreasing
`c_*`: the first alternative is a fixed positive deficit, while the second
and (15) give

```text
epsilon>=c Delta^2 20^(-4d),                        (17)
```

which is stronger than (1).

It remains to treat the small-loss case, where

```text
W_D>=1/2.                                           (18)
```

## 5. Finite-rank exit and energy upper bound

Start from the nonzero cells in the one initial `U` spectral slice. Follow
only their descendants under the exact moving addresses. On the retained
drift sector, each chain visits pairwise disjoint spectral subsets of the
same local `d`-dimensional operator. It therefore has at most `d` good sites.

Sprint 1230, with `M=78/5`, gives

```text
E_exit+E_rec
 >=W_D/[(d+1)(78/5)^(2d)]
 >=1/[2(d+1)(78/5)^(2d)].                           (19)
```

At each response time, descendants of distinct initial cells are disjoint,
so Sprint 1225 bounds their summed packet error with no chain-count factor.
There are at most `d` times. Sprints 1214 and 1218 then give

```text
E_rec<=C_R[d epsilon+L_d].                           (20)
```

A terminal amplitude is either zero, in the near-fixed set, in the far
endpoint discard, or in a discarded contact block. At any fixed exit time these terminal
packets are orthogonal. Summing over at most `d` possible exit times and using
(7), (13), and (15) gives

```text
E_exit<=C_E[d sqrt(epsilon)+L_d].                    (21)
```

Combining (15), (19)--(21), with one universal `C_*`,

```text
1/[2(d+1)(78/5)^(2d)]
 <=C_*[d sqrt(epsilon)
       +Delta^-1 20^(2d)sqrt(epsilon)].              (22)
```

Every discard has now appeared exactly once: fixed near/saturated-boundary
error in `d sqrt(epsilon)`, and moving contact/source/target loss in `L_d`.

## 6. Algebraic conclusion

For `d>=1`, `d<=d20^(2d)`. Hence (22) implies

```text
sqrt(epsilon)
 >=c_0/[d(d+1)(20*78/5)^(2d)]                      (23)
```

for a computable `c_0>0` depending only on the fixed constants above.
Squaring and using `(d+1)^2<=4d^2` gives

```text
epsilon
 >=(c_0^2/4)d^-4(20*78/5)^(-4d),                   (24)
```

which is (1) with `c_*=c_0^2/4` and
`Gamma=312^4=9475854336`.

Because the proof applies to every dimension-`d` strategy, compactness of the
finite-dimensional strategy space permits taking its optimum and yields the
claimed bound on `q_*-Q_d`.

## Claim boundary

This is a mathematical dimension-necessity theorem, not a new Bell
inequality, physical law, or foundational result. The public theorem should
not be promoted until an independent reconstruction verifies the layered
discard ledger and the `C_c,C_L,C_R,C_E` ownership. Numerical optimization of
`c_*` and the exponent is a separate problem.
