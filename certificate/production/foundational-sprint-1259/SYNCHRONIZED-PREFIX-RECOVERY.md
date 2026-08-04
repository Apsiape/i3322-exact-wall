# Complete prefixes recover the vertical fibre bill

Status: **proved abstract recovery theorem; I3322 synchronized-prefix bound
remains open**

## 1. Tail data on ordered fibres

Let `mu_1,...,mu_n` be finite positive measures on log resolution, and put

```text
f_i(L)=mu_i({zeta:zeta>=-L}).                        (1)
```

For shifts `p_i,q_i in [-B,B]`, define the individual and cumulative tail
differences

```text
r_i(L)=f_i(L+p_i)-f_i(L+q_i),
R_j(L)=sum_(i<=j) r_i(L),       R_0=0.               (2)
```

The `R_j` are exactly the data supplied by a complete ordered flag if the two
response transports can be compared on synchronized source prefixes.

## 2. Translation is area between tails

For one event at `zeta`, the indicators in `r_i` differ on an interval of
cut coordinates of length `|p_i-q_i|`.  If `zeta in [-H,0]`, both endpoints
of that interval lie in

```text
I=[-B,H+B].                                         (3)
```

Tonelli therefore gives

```text
mu_i([-H,0]) |p_i-q_i|
 <=integral_I |r_i(L)| dL.                          (4)
```

No density or boundary regularity is used.

## 3. Finite differencing costs only the number of fibres

Since `r_i=R_i-R_(i-1)`, pointwise in `L`,

```text
sum_i |r_i|
 <=|R_n|+2 sum_(i<n)|R_i|
 <=(2n-1) max_(1<=j<=n)|R_j|
 <=2n max_j |R_j|.                                  (5)
```

Summing (4) and integrating (5) proves

```text
boxed:
sum_i mu_i([-H,0]) |p_i-q_i|
 <=2n integral_(-B)^(H+B) max_j |R_j(L)| dL.        (6)
```

The coefficient depends on rank through the number of occupied ordered
fibres, but it is completely independent of their spacing and internal
multiplicity.

## 4. The conditional master inequality

Let `M_core=sum_i mu_i([-H,0])`, let

```text
D_H=sum_i mu_i([-H,0]) |A_i-B_i|,                   (7)
E_sync=integral_(-B)^(H+B) max_j |R_j(L)| dL,       (8)
```

and assume the Sprint 1257 half-wall on every retained fibre.  With
`n<=d`, integration followed by (6) yields

```text
boxed:
(m_0/2) M_core
 <=(182/5) D_H +(169/50) d E_sync.                  (9)
```

Thus the universal lower-bound campaign has been reduced to two receipts of
matching type:

1. the horizontal monotone cost `D_H`, already controlled in uncoarsened
   form by Sprint 1252; and
2. the synchronized-prefix area `E_sync`.

The second receipt is the only new analytic gate.  Marginal rectangle bounds
do not automatically furnish it: the two prefixes must be shown to refer to
the same canonical carrier after contact commonization.  Equation (9) is
therefore conditional and no dimension lower bound is promoted.

