# Sprint 1211 pre-registration -- neutral-cycle exclusion margin

Date: 2026-08-03

## Target

Quantitatively exclude the third escape in Sprint 1210: concentration near a
neutral fixed cycle. Extract a sharp scalar stability inequality from the
quarter-ceiling elimination without fitting a neighborhood or numerical
constant.

## Registered prediction

For arbitrary `x,u in [-1,1]`, `rho>0`, put

```text
B=b(x)+b(u),             delta=x-u,
Q=q_*-x*u+1,
E_+=Q-delta/2-rho*B,
E_-=Q+delta/2-B/rho.
```

Then

```text
q_*-[x*u-1+sqrt(B^2+delta^2/4)]
 <= max(|E_+|,|E_-|),
```

while the bracketed scalar is universally at most `1/4`. Consequently

```text
max(|E_+|,|E_-|) >= q_*-1/4
                    > 0.000875384513976535514.
```

## Failure conditions

- the Lipschitz elimination loses a factor larger than one;
- the inequality requires exact contact before it applies;
- endpoint or zero-`B` cases are singular;
- the certified lower endpoint does not preserve a strict positive margin;
- or the two residuals are not the scalar closure equations owned by a
  neutral contact cycle.
