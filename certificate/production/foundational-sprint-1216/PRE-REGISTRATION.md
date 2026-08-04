# Sprint 1216 pre-registration -- certified global weight box

Date: 2026-08-03

## Target

Extract explicit conservative constants for the balanced response weights and
the square-root cocycle from the existing validated Bellman certificates. Do
not promote the floating min-plus hull to a proof instrument.

## Registered prediction

The load-bearing interval artifacts of Sprints 1192--1195 imply

```text
1/5 < F(t) < 13/10                 for every t in [-1,1],
Z subset [-9/10,9/10]^2           for the double-contact zero set.   (1)
```

On this square, the balanced response weights obey

```text
A(t),B(t)>1/12,
A(t),B(t)<13/10,                                           (2)
```

and their packet square roots obey `p_min^2,q_min^2>1/12`,
`p_max^2<13/10`. Consequently Sprint 1214's recurrence bound becomes

```text
sum s_i^2
 <=24 sum (e^A_i)^2 +(1872/5) sum (e^B_i)^2,              (3)
```

while the amplitude cocycle has

```text
c_i<=13/2.                                                 (4)
```

## Failure conditions

- an interval artifact does not cover one Bellman branch;
- the saved lower bounds do not clear `1/5`;
- the terminal predecessor box reaches `9/10`;
- or any rational response/cocycle inequality fails.

## Claim boundary

This sprint will not certify a numerical lower bound for `r_0` away from the
contact tube. That coercivity constant remains the final analytic input to the
global quantitative assembly.
