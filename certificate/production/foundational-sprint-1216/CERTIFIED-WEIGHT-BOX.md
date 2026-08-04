# A certified global Bellman and response-weight box

Status: **explicit conservative constants from existing interval
certificates; off-contact coercivity still open**

## 1. Custody of the Bellman lower bound

The exact characteristic construction divides `[-1,1]` into the active
predecessor range and its two outer wings.

- Sprint 1192's central and reflected graph pieces certify every active pivot
  above `0.2577` except later pieces whose lowest certified value remains
  above `0.2564`.
- Sprint 1193's boundary-wing pieces remain above `0.2564`.
- Sprint 1194 directly certifies every outer target value above
  `0.2103999`.

The theorem-assembly gates certify that these pieces form the complete
Bellman graph and that the outer guard closes both tails. Therefore the safe
rational bound

```text
F(t)>1/5                                                  (1)
```

holds globally.

The older tile engines serialized their Arb lower endpoints through binary64.
The custody guard subtracts `10^-12` from every such lower endpoint before
testing (1), more than three decimal orders above the conversion error and
more than four decimal orders below the available margin.

Sprint 1195 gives

```text
F(t)<=q_*+(1-t)/2.                                      (2)
```

Its validated interval has `q_*<0.251`, so

```text
F(t)<1.251<13/10.                                       (3)
```

No floating min-plus approximation enters (1)--(3).

## 2. The double-contact set is uniformly interior

The exact predecessor map has image

```text
[-x_*,x_*],
x_*<0.898117<9/10.                                     (4)
```

At double contact,

```text
x=P(u),
-u=P(-x).                                              (5)
```

Both coordinates therefore belong to the predecessor image, and

```text
Z subset (-9/10,9/10)^2.                               (6)
```

This proves a strict endpoint separation. A numerical lower bound for `r_0`
on the complement of a chosen contact tube is a separate coercivity task.

## 3. Balanced response-weight bounds

For either balanced response weight,

```text
W(t)=b(t)sqrt(F(sigma t)/F(t)),
b(t)=sqrt(1-t^2)/2,                                    (7)
```

with the appropriate reflection orientation. On `|t|<=9/10`,

```text
b(t)^2>=19/400.                                        (8)
```

Using (1) and (3),

```text
W(t)^2> (19/400)(2/13)=19/2600>1/144,
W(t)^2< (1/4)(13/2)=13/8<(13/10)^2.                   (9)
```

Hence

```text
1/12<W(t)<13/10.                                      (10)
```

For the packet weights `p=sqrt(A)`, `q=sqrt(B)`, equation (10) says

```text
p_min^2,q_min^2>1/12,
p_max^2,q_max^2<13/10.                                (11)
```

Sprint 1214's abstract energy inequality therefore specializes to

```text
sum_i s_i^2
 <=24 sum_i (e^A_i)^2
  +(1872/5) sum_i (e^B_i)^2.                          (12)
```

Finally the exact reflection ratios give

```text
c_i^2=C_i<=([13/10]/[1/5])^2=(13/2)^2,
c_i<=13/2.                                            (13)
```

These constants are deliberately conservative. Their purpose is to land an
explicit theorem before optimizing the sharp plateau exponent.

## 4. Remaining constant

Everything in the abstract endpoint theorem now has a numerical owner except
the off-contact coercivity:

```text
kappa(delta)
 =min{r_0(x,u): distance((x,u),Z)>=delta,
                     |x|,|u|<=9/10}.                 (14)
```

For any fixed rational `delta>0`, compactness proves `kappa(delta)>0`, but a
usable dimension theorem needs a validated lower number and a compatible
cell-oscillation modulus. The next campaign should build one interval engine
for (14), using the certified Bellman chart rather than the floating hull.

## Claim boundary

This package certifies global Bellman ancestry, response-weight bounds,
cocycle bound, and recurrence constants. It does not yet prove the final
`q_*-Q_d` inequality.
