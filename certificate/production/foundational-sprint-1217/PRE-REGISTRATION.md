# Sprint 1217 pre-registration -- predecessor derivative coercivity

Date: 2026-08-03

## Target

Certify explicit strong-concavity constants for the exact Bellman function by
recovering the derivative ratio discarded by the earlier validated graph
engines.

## Registered prediction

Across the complete active predecessor chart, including the central branch,
reflection, and both boundary wings,

```text
1/10 < P'(u) < 2.                                      (1)
```

Because `F'(u)=1/2-P(u)`, this implies `-F''(u)>=1/10`.
For active predecessor coordinates `x,u`, the two Bellman gaps then give

```text
r_0(x,u)
 >=[(x-P(u))^2+(u+P(-x))^2]/160.                      (2)
```

## Failure conditions

- any interval derivative ratio intersects `0`, `1/10`, or `2`;
- a central or wing chart is not covered with the inherited analytic-tail
  enlargement;
- the Bregman coefficient is oriented incorrectly;
- or the Cauchy assembly loses more than the stated factor two.

## Claim boundary

Equation (2) applies on the active predecessor square. The inactive sliver
between `x_*` and `9/10` remains a separately priced boundary strip. A final
dimension theorem also needs the packet/cell assembly to consume these
constants without duplicating local blocks.
