# A shifted monotone grid makes contact rank-visible

Status: **exact averaged-rounding theorem; reflection closure remains open**

## 1. Paired contact cells

Work on the active chart where `P` is an increasing bijection and put

```text
y=P^-1(x).                                           (1)
```

For `h>0` and `s in [0,h)`, let

```text
I_k(s)=[s+kh,s+(k+1)h),
J_k(s)=P(I_k(s)).                                    (2)
```

The `I_k` are disjoint `U` cells and the `J_k` are disjoint `X` cells, with a
one-to-one common index. Every exact contact point `(P(u),u)` belongs to
`J_k x I_k` for one `k`. Thus the matched part of the state coefficient
matrix is precisely the block diagonal required by Sprint 1221.

## 2. Shift-averaged mismatch

For fixed real `y,u`, a uniformly shifted width-`h` grid separates them only
when a grid boundary lies between them. The measure of such shifts in one
period is `min(h,|y-u|)`. Hence

```text
Pr_s[cell_s(y)!=cell_s(u)]
 =min(1,|y-u|/h)
 <=|y-u|/h.                                         (3)
```

For the joint spectral probability measure `mu`, Tonelli gives

```text
E_s rho_off(s)
 <=h^-1 integral |P^-1(x)-u| dmu(x,u).              (4)
```

There is therefore at least one deterministic shift no worse than the right
side of (4). The statement is measure-theoretic and has no number-of-cells,
spectral-atom, multiplicity, or dimension factor.

## 3. Explicit I3322 constant

Sprint 1217 certifies `P'(t)>1/10` on the complete active predecessor chart.
The mean-value theorem makes the inverse `10`-Lipschitz:

```text
|P^-1(x)-u|<=10|x-P(u)|.                            (5)
```

The same sprint proves

```text
r_0(x,u)>=(x-P(u))^2/160.                           (6)
```

If `epsilon_0=int r_0 dmu`, Cauchy--Schwarz yields

```text
int |P^-1(x)-u| dmu
 <=10 sqrt(int (x-P(u))^2 dmu)
 <=10 sqrt(160 epsilon_0)
 =40 sqrt(10) sqrt(epsilon_0).                       (7)
```

Combining (4) and (7), some shift satisfies

```text
rho_off(s)<=[40 sqrt(10)/h] sqrt(epsilon_0).         (8)
```

Sprint 1221 then shows that, after retaining the `d` largest paired cells,
the additional discarded matched mass is no greater than the same
`rho_off(s)`. Thus total mass lost to pairing plus rank compression is at most

```text
2 rho_off(s)<=[80 sqrt(10)/h] sqrt(epsilon_0).       (9)
```

This square-root dependence is intentionally accepted. It weakens constants
but still permits an explicit exponential dimension lower bound if the
reflection-transport assembly is linear in Hilbert norm.

## 4. What remains

The shifted partition is not automatically permuted by

```text
b(u)=-u,
a(u)=P^-1(-P(u)).                                   (10)
```

Taking the full dihedral refinement may create infinitely many increasingly
thin cells near fixed endpoints, so reflection closure cannot be asserted by
finite refinement. The next theorem must either:

1. construct an orbit-adapted measurable partition with a quantitative
   modulus on the nonneutral region; or
2. prove a reflection-rounding estimate between successive shifted paired
   partitions, charging the mismatch as endpoint leakage.

Equation (8) solves contact pairing and rank visibility. It does not solve
the dynamical closure problem.
