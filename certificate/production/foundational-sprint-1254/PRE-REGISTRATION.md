# Pre-registration: a joint lift of both event measures

The separate Alice and Bob order-resolution measures lose the coupling that
the coefficient operator already carries.  Before running a matrix guard,
register the following construction.

For `rho_A=DD*`, `rho_B=D*D`, `t>0`, put

```text
Z_t=sqrt(t) D(tI+rho_B)^(-1).
```

The positive block weights `||E_A Z_t F_B||_HS^2` must have left marginal
`Tr(E_A K_t(rho_A))` and right marginal `Tr(F_B K_t(rho_B))`.  Integrated in
`d log t`, they must therefore define a canonical joint lift of both event
measures.

The second target is an explicit near-contact bill.  With
`C=Y D-D U`, `||D||<=1`, and `0<t<=1`, the coupling cost must obey

```text
||Y Z_t-Z_t U||_HS^2 <=9 ||C||_HS^2/t^3.
```

Falsifiers:

1. either marginal identity fails for rectangular `D`;
2. positivity requires commuting order projections;
3. the commutator `[D*D,U]` is not owned by `C`; or
4. the stated power of `t` is insufficient.

