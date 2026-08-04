# Sprint 1246 pre-registration -- operator-valued resolution

Date: 2026-08-04

## Target

Remove the commutation hypothesis from Sprint 1245. Determine whether a
positive response multiplier acts exactly by replacing scalar resolution with
an operator-valued resolution metric.

## Registered prediction

For `rho=DD^*`, positive invertible `C`, and `t>0`,

```text
W_t(CD)
 =C [rho (t C^(-2)+rho)^(-1)] C^(-1).               (1)
```

If a flag projection `E` commutes with `C`, cyclicity should remove the
similarity:

```text
Tr[E W_t(CD)]
 =Tr[E rho (t C^(-2)+rho)^(-1)].                    (2)
```

When `[C,rho]=0`, this must reduce to Sprint 1245's blockwise scale law
`t -> t/c^2`.

## Failure conditions

- the inverse in (1) has the wrong order;
- the metric is `tC^2` rather than `tC^(-2)`;
- (2) requires `E` to commute with `rho` as well as `C`;
- or the right-multiplier analogue has a different orientation.

## Claim boundary

This is an exact matrix identity. It does not by itself compare Alice's and
Bob's operator-valued metrics or prove finite-rank closure.
