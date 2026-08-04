# Result 001 -- blind reconstruction of quantitative I3322 dimension necessity

Status: **retracted as a proof; retained as a conditional reconstruction with
the failure localized at equation (16)**

## Correction notice

Adversarial review found that equation (16) is not implied by the packet. The
two-frame theorem applied to `w=L_sigma psi` contains omissions on the full
vector. Equation (15) controls pullback omissions only inside the selected
near-fixed occurrences. It does not control the coarse complement or the
commutator created by first restricting `w` to the near-fixed sector.

The maximal valid localized sub-PVM estimate is

```text
D^2 <= 3[||E'(K w-w)||^2
          +||(E-G)w||^2+||(E'-G')w||^2].
```

The last two terms cannot be replaced by occurrence-internal near-fixed
omissions under the stated hypotheses. Consequently equations (20) and all
later uses of `m_N<=C_N sqrt(epsilon)` are conditional. The arithmetic below
is retained to make the exact downstream consequence of a future flux lemma
reproducible; it is not a theorem proof.

## 1. Theorem and fixed constants

Let `Q_d` and `q_*` have the meanings in the blind brief. Then, for every
integer `d>=1`,

```text
q_*-Q_d >= c d^-4 Gamma^-d,                         (1)
```

where the following is one explicit admissible choice:

```text
M       = 78/5,
Gamma   = (20 M)^4 = 312^4 = 9,475,854,336.         (2)
```

The positive constant `c`, independent of `d`, is displayed exactly in
Section 11. Its arithmetic value is approximately

```text
c = 4.2946546143271442... * 10^-52.                 (3)
```

No optimization of `c` or `Gamma` is claimed.

## 2. Strategy reduction and certificate debts

Sprint 1237 gives a pure projective representative of the dimension-`d`
optimum without a dilation. Fix it and put

```text
epsilon = q_*-Q_d.
```

Sprints 1197 and 1208 give three positive remainders and the exact ledger

```text
epsilon=epsilon_0+epsilon_A+epsilon_B,
epsilon_sigma=<psi,R_sigma psi> >=0.                (4)
```

For `sigma=A,B`, write `L_sigma` and `K_sigma` for the balanced weight and
response involution. Then

```text
||(I-K_A)L_A psi||^2=2 epsilon_A,
||(I-K_B)L_B psi||^2=2 epsilon_B.                   (5)
```

All spectral masses below are values of the finite positive joint spectral
measure

```text
nu(S)=<psi,E_(X,U)(S)psi>.                          (6)
```

No density of `nu` is introduced. Because `X` and `U` act on opposite tensor
factors, their spectral projections commute and (6) is the ordinary joint
projection-valued spectral measure.

## 3. Saturated coordinates and the complete inactive-tail charge

Let `I=[-x_*,x_*]` and let `Y` be the saturated predecessor coordinate of
Sprint 1232. Its global coercivity inequality is

```text
r_0(x,u)
 >=[(u-Y(x))^2+(x+Y(-u))^2]/40
   +[dist(x,I)^2+dist(u,I)^2]/400.                  (7)
```

Since `x_*<0.898117`, put

```text
delta_out=9/10-898117/10^6=1883/10^6,
C_out=400/delta_out^2
     =400*10^12/1883^2.                             (8)
```

For the far response tail

```text
O={|x|>9/10 or |u|>9/10},
m_out=nu(O),
```

(7) and Markov's inequality for the finite measure (6) give the complete
tail bill

```text
m_out<=C_out epsilon_0.                             (9)
```

The inactive sliver between `x_*` and `9/10` is **not** discarded. It is in
the saturated boundary cell and its quadratic distance debt remains in (7).
Thus no false fixed positive gap on the complete sliver is used.

On the complement of `O`, Sprints 1216 and 1218 give

```text
1/12<L_A^2,L_B^2<13/10,
max(c_k,c_k^-1)<=M=78/5                             (10)
```

for every nonzero grouped packet recurrence coefficient.
The upper bound `L_sigma^2<13/10` is global: from `1/5<F<13/10` and
`b<=1/2`, the weight formula in Sprint 1216 gives
`L_sigma^2<sqrt(13/8)<13/10`. Only the lower bound requires the response
box.

## 4. Near-fixed mass, including every capture and response charge

The constants in this section are deliberately very small/large, but fixed
once and for all. Define

```text
mu     =7/8000,
h_0    =10^-7,
K      =4656/25,
H      =(39/10)K+mu^2/2,
theta  =mu^2/(16H),
Delta_N=theta h_0/20,
Delta  =Delta_N/8.                                  (11)
```

Thus `20 Delta_N/h_0=theta`. Let

```text
N={u: |tau(u)-u|<Delta_N},
m_N=nu({|x|,|u|<=9/10, u in N}).                    (12)
```

Here and below boundary sets may be assigned to either side; this can only
reduce a retained mass.

For completeness, the near-fixed shifted capture used in Sprint 1229 is
reconstructed rather than assumed. If `|tau(u)-u|<Delta_N`, a uniformly
shifted width-`h_0` grid separates the two pullback coordinates on a set of
shifts of relative measure at most

```text
20 Delta_N/h_0=theta,                               (13)
```

because the only nonlinear pullback has Lipschitz constant at most `20`.
This is exactly the shifted-grid estimate of Sprint 1222. Charge it in all
four source/target occurrences of the two response transports, rather than
assuming cancellations.

The common-source/common-target construction has four source/target
occurrences across the two response laws. Each relevant pullback word has at
most one nonlinear `a`, so its distortion is at most `20`. Their total
contact factor is therefore bounded by

```text
4*20=80<100.                                       (14)
```

From (7), Cauchy--Schwarz, and shifted averaging, one common deterministic
shift therefore has total source/target omission at most

```text
delta_N=4 theta m_N+C_0 sqrt(epsilon_0),
C_0=100 sqrt(40)/h_0.                               (15)
```

This overcharges both the four pullback boundary losses and all four
source/target contact mismatches.

Apply the exact two-frame theorem (Sprint 1225) to `w=L_A psi` and
`w=L_B psi`, with the common source/target projections of Sprint 1228.
The upper weight bound in (10), the three-term inequality, and (5) give

```text
D_A^2+D_B^2
 <=6(epsilon_A+epsilon_B)+(39/10)delta_N.           (16)
```

**This is the invalid step.** The valid right side contains the four actual
coarse omissions `nu(E_sigma-G)+nu(E'_sigma-G')`. The shifted estimate (15)
does not bound them; they may include order-one mass outside the near-fixed
restriction. A quantitative no-inbound/no-outbound-flux or commutator estimate
is required.

Indeed, each response defect contributes `3*2 epsilon_sigma`, and the sum
of all weighted source/target omissions is at most `(13/10)delta_N` before
the factor `3`.

Let `W` be the captured source/target packet mass in Sprint 1229. Source
omission is one of the terms already in (15), so

```text
W>=m_N-delta_N.                                     (17)
```

Sprint 1229's repaired absorbed closure inequality says

```text
(mu^2/2)W<=48 epsilon_0+K(D_A^2+D_B^2).             (18)
```

The coefficient `48` retains the source/target contact multiplicity.  Each
family is internally orthogonal, but the two families need not be mutually
orthogonal, so their combined contact energy is bounded by `2 epsilon_0`, not
by `epsilon_0`.

Combining (15)--(18) gives

```text
(mu^2/2)m_N
 <=48epsilon_0+6K(epsilon_A+epsilon_B)+H delta_N.
```

The choice of `theta` makes

```text
4H theta=mu^2/4.                                    (19)
```

For `epsilon<=1`, absorption and
`epsilon_i<=epsilon<=sqrt(epsilon)` yield the complete near-fixed charge

```text
m_N<=C_N sqrt(epsilon),                             (20)

C_N=(4/mu^2)[48+6K+H C_0].                         (21)
```

This accounts for near-fixed capture, all four source/target omissions, both
reused response debts, and coefficient oscillation already absorbed in the
explicit Sprint 1229 constant. It introduces no fibre map.

## 5. Moving drift frames and their full contact loss

Use an independent shifted grid of width

```text
h_d=Delta/(4*20^d).                                 (22)
```

The one-sided histories needed for a `tau=ab` recurrence are exactly

```text
g_k=tau^k,                 0<=k<=d,
h_k=b tau^k,               0<=k<d.                  (23)
```

There are `d+1` principal and `d` intermediate frames. The frame `g_k` and
`h_k` each contain exactly `k` nonlinear `a` occurrences. Hence the complete
all-frame distortion sum -- including multiplicity -- is

```text
S_d=sum_(k=0)^d 20^k+sum_(k=0)^(d-1)20^k
   =(21*20^d-2)/19
   <=(21/19)20^d.                                   (24)
```

This is not the multiplicity-free geometric sum retracted in Sprint 1223.

At frame `g`, use `Y(x)` and `u` as the paired coordinates. Equation (7)
gives

```text
integral |Y(x)-u| dnu<=sqrt(40 epsilon_0).          (25)
```

The moved-grid estimate and one average over the common shift imply that the
sum of all contact mismatches in (23) is at most

```text
R_d<=[sqrt(40)/h_d] S_d sqrt(epsilon_0)
   <=K_R 20^(2d)sqrt(epsilon_0),                    (26)

K_R=84sqrt(40)/(19Delta).                           (27)
```

The saturated coordinate makes the boundary cell exact under sign reversal,
as stated in Sprint 1232, so (26) includes the inactive sliver without a
coarse-to-fine amplitude substitution.

Cells touching the boundary of the retained set
`|tau(u)-u|>=Delta` are stopped. A frame-`k` cell has diameter at most

```text
20^k h_d<=Delta/4.                                  (28)
```

Since `Lip(tau)<=20`, the function `tau(u)-u` is `21`-Lipschitz. A cell that
touches `|tau(u)-u|<Delta` is therefore contained in

```text
|tau(u)-u|<Delta+21Delta/4<8Delta=Delta_N,           (29)
```

and is charged to (20). Every remaining drift cell has one fixed orientation
and gap at least `Delta`; (28) gives the strict ordered-cell condition
`Delta>2H_cell` of Sprints 1224--1225.

Let `F_d` denote the sum, over all `2d+1` frame occurrences, of state mass
discarded by contact mismatch, the far response tail, or the stopped
near-fixed/boundary sector. The global masses (9) and (20) can each be reused
at most `2d+1<=3d` times. From (9), (20), and (26), for `epsilon<=1`,

```text
F_d
 <=R_d+(2d+1)(m_out+m_N)
 <=C_F 20^(2d)sqrt(epsilon),                         (30)

C_F=K_R+3(C_out+C_N).                               (31)
```

The last inequality uses `d<=20^(2d)` for `d>=1`. Equation (30) is the
complete moving-frame contact/exit loss through stopping time, not merely a
per-frame bound.

## 6. Packet ancestry, uniqueness, and temporal rank

At frame `g`, the coarse cells are

```text
U: g(I_i),
X: Y^-1(g(I_i)),                                    (32)
```

with fine projection their commuting joint intersection, further restricted
to the retained response and drift set. Sprint 1232's saturated address law
and Sprint 1225 give exact coarse maps

```text
K_B: (i,g)->(i,bg),
K_A: (i,bg)->(i,abg)=(i,tau g).                     (33)
```

Thus a physical packet `(i,k)` has exactly one possible predecessor
`(i,k-1)` when `k>0` and at most one possible successor `(i,k+1)`. A missing
fine target stops the chain; it never creates a second target. Distinct `i`
occupy orthogonal cells in every fixed frame because a moved partition is a
bijection of a partition. This proves the required no-branch/no-merge
ancestry statement without an orbit disintegration.

In the initial slice, the local dimension-`d` operator `U` has at most `d`
nonzero spectral projections among the disjoint cells. More importantly, in
each individual retained drift chain, (28)--(29) and Sprint 1224 make its
successive `U` cells pairwise disjoint. Their nonzero local spectral
projections are orthogonal, so

```text
n_i<=d                                               (34)
```

for every chain `i`. We do **not** claim `sum_i n_i<=d`; the finite-rank exit
theorem does not require it.

## 7. Recurrence-residual upper energy

At each of the at most `d` Bob steps and `d` Alice steps, apply Sprint 1225.
The response debt in (5) is reused once per corresponding time, while a frame
discard in (30) occurs as source or target in at most two adjacent response
maps. Consequently the direct-sum packet errors obey

```text
sum e_A^2+sum e_B^2
 <=6d(epsilon_A+epsilon_B)+(39/5)F_d.               (35)
```

The factors are:

```text
6d  = d times [3-term square factor 3] times
      [response norm debt 2 epsilon_sigma],
39/5=2 adjacent uses times 3 times 13/10.            (36)
```

RMS compression (Sprint 1218) passes from each Hilbert packet to its norm,
and the common intermediate target in Sprint 1228 lets the Bob and Alice
relations compose. Sprint 1214 and the certified weight box give

```text
E_rec:=sum_(i,k) s_(k,i)^2
 <=24 sum e_A^2+(1872/5)sum e_B^2
 <=(1872/5)[6d epsilon+(39/5)F_d].                  (37)
```

No cell representative, fine amplitude, packet count, or dimension factor is
hidden in (37). The conservative grouped-packet coefficient is the `M=78/5`
in (10), not the point-contact value `13/2`.

## 8. Terminal/exit upper energy

A chain stops only when its next local spectral projection is zero, it leaves
the paired response box/contact capture, or it reaches the near-fixed/boundary
sector. To avoid identifying the last retained amplitude with an exit
amplitude, use the at most two final response estimates. With an unused error
set to zero when exit occurs after the first response, two reverse-triangle
inequalities give

```text
z_s
 <=sqrt(12)e_B+12sqrt(13/10)e_A+(78/5)z_exit,
z_s^2
 <=(2808/5)(e_A^2+e_B^2)+(18252/25)z_exit^2.       (38a)
```

If the exit projection is zero, the last term vanishes. Otherwise its
exit mass is in a discarded frame projection counted by `F_d`. Exact
same-index ancestry makes terminal edges orthogonal in each fixed frame; the
frame sum is already priced in (30). With
`E_pack=sum e_A^2+sum e_B^2`,

```text
E_exit<=(2808/5)E_pack+(18252/25)F_d.               (38b)
```

There is no reuse beyond the response-error and `2d+1` frame multiplicities
already present in (35) and (30). Combining (30), (35), (37), and (38b),

```text
E_exit+E_rec
 <=A d epsilon+B C_F 20^(2d)sqrt(epsilon),          (39)

A=5616,
B=200772/25.                                        (40)
```

This is the requested terminal/exit and recurrence-residual upper ledger.

## 9. Initial retained drift mass

Let `W_D` be the sum of squared norms of all initial paired packets inside the
retained oriented drift region. No top-`d` selection is performed. By the
union bound for the finite measure (6), the only initial losses are (9), (20),
and the frame-zero term of (26). Therefore

```text
W_D
 >=1-m_out-m_N-[sqrt(40)/h_d]sqrt(epsilon_0)
 >=1-C_I 20^(2d)sqrt(epsilon),                      (41)

C_I=C_out+C_N+4sqrt(40)/Delta.                      (42)
```

The second line again uses `epsilon<=1` and `20^d<=20^(2d)`. Equation (41)
is the initial retained drift-mass ledger.

## 10. Finite-rank recurrence lower energy

For every chain, RMS compression gives positive coefficients satisfying

```text
z_(k+1,i)=c_(k,i)z_(k,i)+s_(k,i),
max(c_(k,i),c_(k,i)^-1)<=M,
n_i<=d.                                             (43)
```

The reverse endpoint theorem of Sprint 1230, summed over arbitrarily many
chains, gives

```text
E_exit+E_rec
 >=W_D/[(d+1)M^(2d)].                               (44)
```

The factor `d+1` counts the one terminal amplitude and at most `d` residuals
inside each chain; `M^(2d)` is the squared worst backward product. Equation
(44) needs neither a bound on the number of chains nor a bound on the sum of
their lengths.

## 11. Final case split and algebra

Define the positive, dimension-independent constants

```text
c_0=1,
c_1=1/(4 C_I^2),
c_2=1/(8 A),
c_3=1/(64 B^2 C_F^2),
c=min(c_0,c_1,c_2,c_3).                             (45)
```

Every entry is explicit in (8), (11), (21), (27), (31), (40), and (42).
The independent arithmetic guard `verify_constants.py` finds
`c=c_3=4.2946546143271442...*10^-52`.

If `epsilon>=1`, (1) follows from `c<=1`, `d^-4<=1`, and `Gamma^-d<=1`.
Assume henceforth `epsilon<1`.

If the loss term in (41) is at least `1/2`, then

```text
epsilon>=1/[4 C_I^2 20^(4d)]
        >=c_1 d^-4 Gamma^-d,                        (46)
```

because `Gamma=(20M)^4>20^4`.

Otherwise `W_D>=1/2`. Equations (39) and (44) imply

```text
1/[2(d+1)M^(2d)]
 <=A d epsilon+B C_F 20^(2d)sqrt(epsilon).          (47)
```

At least one term on the right is at least half the left side.

If it is the first term, then, using `d+1<=2d`,

```text
epsilon>=1/[4A d(d+1)M^(2d)]
        >=c_2 d^-4 Gamma^-d.                        (48)
```

If it is the second term, squaring and again using `d+1<=2d`,

```text
epsilon
 >=1/[16B^2 C_F^2(d+1)^2(20M)^(4d)]
 >=c_3 d^-4 Gamma^-d.                               (49)
```

Conditional on the missing localization estimate, equations (46), (48), and
(49) exhaust the algebraic cases and would prove (1).

## 12. Multiplicity and prohibited-shortcut audit

The complete debt reuse is:

- each response norm debt: at most `d` times, producing `6d` in (35);
- each fine frame discard: at most two adjacent response maps, producing
  `39/5` in (35);
- contact rounding: exactly the `d+1` principal plus `d` intermediate frames
  in (24), producing `20^(2d)` only after inserting the mesh;
- inactive-tail and near-fixed global masses: at most `2d+1` frame
  occurrences in (30);
- each terminal edge: at most its two final response errors (already in
  (35)) and one exit projection in its terminal frame (already in `F_d`);
- recurrence lower bound: one `d+1` factor per chain, with arbitrary chain
  count.

The proof uses no spectral density, global orbit disintegration, fibre
partial isometry, simultaneous top-`d` selection, full-sliver positive gap,
sum-of-chain-lengths bound, coarse-to-fine amplitude substitution, or
multiplicity-free all-frame sum.

## 13. Standard facts and references

The only mathematical facts beyond the sealed sources are Cauchy--Schwarz,
triangle/Minkowski, Tonelli's theorem for a nonnegative shifted-grid
integrand, Markov's inequality for a finite positive measure, the spectral
theorem/functional calculus for commuting finite-dimensional self-adjoint
operators, and additivity of rank for orthogonal nonzero projections. Standard
references are:

- J. B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990,
  chapters on spectral theory and functional calculus.
- G. B. Folland, *Real Analysis*, 2nd ed., Wiley, 1999, chapters on integration
  (Tonelli and integral inequalities).

The reconstruction implicitly introduced the missing localization premise at
equation (16). No such premise is present in the frozen sources.
