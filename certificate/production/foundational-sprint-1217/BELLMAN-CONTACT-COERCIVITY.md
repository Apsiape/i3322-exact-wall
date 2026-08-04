# The transport remainder quadratically controls both contact equations

Status: **interval-certified active-chart coercivity; inactive sliver and
global assembly remain open**

## 1. Predecessor derivative box

The validated characteristic charts parameterize consecutive predecessor and
target coordinates `(x,y)` by the same interval parameter. The exact
predecessor derivative is therefore

```text
P'(y)=(dx/dt)/(dy/dt).                                 (1)
```

A fresh Arb pass uses the same degree-12 validated connection, analytic-tail
enlargements, central chart, reflection section, and boundary-wing bracket as
Sprints 1192--1193. It certifies on every tile

```text
1/10<P'(y)<2.                                         (2)
```

Reflection supplies the omitted symmetric halves with the same derivative
box.

The certified extremal interval endpoints were

```text
min lower(P') = 0.15502852969802916,
max upper(P') = 1.1127851121127605.                    (2a)
```

The first coarse diagnostic used one quarter of the inherited main-chart
resolution and suffered interval wrapping on the last propagated piece.
The final engine restores the original 32,768 tiles per main chart and keeps
the preregistered `(1/10,2)` box unchanged.

## 2. One Bellman gap is a Bregman divergence

For active predecessor `x=P(y)`, its supporting line is tangent to `F` at
`y`. Hence the forward Bellman deficit at target `u` is

```text
Delta_+(x,u)
 =q_*-d(x,u)-p(x)-F(u)
 =F(y)+F'(y)(u-y)-F(u).                               (3)
```

Since

```text
F'(u)=1/2-P(u),
-F''(u)=P'(u)>=1/10,                                  (4)
```

strong concavity gives

```text
Delta_+(x,u)>=(u-y)^2/20.                             (5)
```

The upper derivative bound in (2) makes `P` two-Lipschitz, so

```text
|x-P(u)|=|P(y)-P(u)|<=2|y-u|.
```

Therefore

```text
Delta_+(x,u)>=(x-P(u))^2/80.                          (6)
```

Applying the same argument to predecessor `-u` and target `-x` gives

```text
Delta_-(x,u)>=(u+P(-x))^2/80.                         (7)
```

## 3. The transport remainder owns both gaps

Put

```text
Q=q_*-d(x,u),
s_+=p(x)+F(u)=Q-Delta_+,
s_-=F(-x)+p(-u)=Q-Delta_-.
```

The balanced response weights satisfy

```text
A(x)+B(u)<=sqrt(s_+s_-)
          <=(s_++s_-)/2.                             (8)
```

Consequently

```text
r_0=Q-A(x)-B(u)
 >=(Delta_++Delta_-)/2
 >=[(x-P(u))^2+(u+P(-x))^2]/160.                     (9)
```

This is the required explicit double-contact coercivity on the active
predecessor square.

In particular, for any `delta>0`, mass on which either contact residual has
magnitude at least `delta` is bounded by

```text
mu_bad<=160 epsilon_0/delta^2.                        (10)
```

No two-dimensional interval minimization of `r_0` is needed.

## 4. Remaining strip and assembly

The active predecessor range ends at

```text
x_*=0.898116482394039... .
```

Sprint 1216 used the rational square `[-0.9,0.9]^2`; (9) does not silently
extend over its inactive sliver. The final assembly must either:

1. discard that sliver using a separately validated positive `r_0` gap; or
2. choose an inner rational active cutoff and separately prove that the exact
   double-contact set misses the removed active fringe.

The first route is safer and is the next numerical gate.

## Claim boundary

The active-chart contact tube is now explicit. No final `q_*-Q_d` inequality
is claimed until the inactive sliver and packet/cell assembly are closed.
