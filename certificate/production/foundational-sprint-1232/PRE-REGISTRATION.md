# Sprint 1232 pre-registration

Use the exact Sprint 1194 outer-wing parameterization, 300-bit Arb, and
32,768 inherited tiles. On every tile require

```text
dx/dt<0,
dS/dt<0,
(dS/dt)/(dx/dt)>1/100.
```

No adaptive weakening is permitted after the run. A pass licenses the
analytic integration

```text
S(x)-1 >= (x-x_*)/100,
L_x(1)-F(1) >= (x-x_*)^2/200.
```

