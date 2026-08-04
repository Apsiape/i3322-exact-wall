# Neutral contact cycles have a universal closure defect

Status: **exact sharp scalar stability theorem; operator-to-cycle transfer
still open**

## Theorem

Let

```text
b(t)=sqrt(1-t^2)/2,
B=b(x)+b(u),
delta=x-u,
Q=q_*-x*u+1,                                         (1)
```

for arbitrary `x,u in [-1,1]` and `rho>0`. Define the two closure residuals

```text
E_+=Q-delta/2-rho B,
E_-=Q+delta/2-B/rho.                                 (2)
```

Then

```text
max(|E_+|,|E_-|) >= q_*-1/4.                        (3)
```

For the certified wall,

```text
q_*-1/4 > 0.000875384513976535514.                  (4)
```

The constant is sharp relative to the scalar quarter ceiling.

## Proof

Put

```text
delta_0=B(1/rho-rho),
S(delta)=sqrt(B^2+delta^2/4).                        (5)
```

Because `B>=0` and `rho>0`,

```text
S(delta_0)=B(rho+1/rho)/2.                           (6)
```

Adding and subtracting (2) gives the exact relations

```text
Q=S(delta_0)+(E_++E_-)/2,
delta-delta_0=E_--E_+.                               (7)
```

The function `S` is globally `1/2`-Lipschitz in `delta`. Therefore

```text
|Q-S(delta)|
 <= |E_++E_-|/2+|E_--E_+|/2
 = max(|E_+|,|E_-|).                                 (8)
```

Now define

```text
Phi(x,u)=x*u-1+S(x-u).                               (9)
```

Writing `s_x=sqrt(1-x^2)`, `s_u=sqrt(1-u^2)`, and `t=1-x*u`, one has

```text
S(x-u)^2=(t+s_x s_u)/2 <= t,                        (10)
```

because

```text
t^2-s_x^2 s_u^2=(x-u)^2>=0.                         (11)
```

Thus

```text
Phi(x,u)<=-t+sqrt(t)<=1/4.                           (12)
```

Since `Q-S(delta)=q_*-Phi(x,u)>=q_*-1/4>0`, equations
(8)--(12) prove (3). There is no endpoint division and `B=0` is harmless.

## Meaning for the skew-product

At an exact neutral fixed cycle, `rho` is the component-amplitude ratio and
`E_+=E_-=0`; (3) makes that impossible by a fixed margin. More importantly,
an approximate cycle cannot make both scalar closure equations smaller than
the same margin. This removes Sprint 1210's third escape without selecting a
neighborhood or invoking compactness.

The robust campaign therefore reduces to:

```text
operator/measure deficit
 -> approximate skew-product residuals E_+,E_-
 -> neutral cycles cost at least q_*-1/4
 -> remaining mass lies on nonneutral cycles or finite chains.            (13)
```

The still-open arrow is the first one: convert the total-variation response
bounds and `R_0` contact tube into an approximate cycle decomposition whose
scalar residuals are controlled by the Bell deficit. Once obtained,
nonneutral cycles are charged by holonomy and chains by Sprint 1207's endpoint
lemma.
