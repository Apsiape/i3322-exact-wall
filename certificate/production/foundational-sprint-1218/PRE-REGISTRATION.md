# Sprint 1218 pre-registration -- RMS packet compression

Date: 2026-08-03

## Target

Eliminate the cellwise Bellman-weight oscillation modulus from the robust
dimension campaign. Replace point representatives by exact state-dependent
RMS packet weights.

## Registered prediction

For a packet `v_i` and positive functional-calculus weight `L`, define

```text
z_i=||v_i||,
p_i=||L v_i||/||v_i||.                                (1)
```

If `ell I<=L^2<=u I` on the packet, then

```text
ell<=p_i^2<=u.                                        (2)
```

Moreover a packet transport error

```text
e_i=||K L v_i-L v_(alpha i)||                         (3)
```

implies exactly

```text
|p_i z_i-p_(alpha i)z_(alpha i)|<=e_i.               (4)
```

Thus Sprint 1214 applies with no cell-diameter or oscillation term.

Using Sprint 1216's safe response box, the grouped-packet amplitude cocycle
may be bounded by

```text
M_eff=(p_max/p_min)(q_max/q_min)<=78/5.               (5)
```

## Failure conditions

- RMS compression introduces a dimension or packet-count factor;
- (4) fails because vector directions matter;
- the certified response box does not transfer to RMS weights;
- or the grouped cocycle is incorrectly assigned the sharper pointwise bound
  `13/2`.

## Claim boundary

This theorem deliberately trades the sharp pointwise cocycle ceiling for a
coarser grouped-packet bound. Recovering the plateau exponent is postponed
until after an explicit dimension theorem lands.
