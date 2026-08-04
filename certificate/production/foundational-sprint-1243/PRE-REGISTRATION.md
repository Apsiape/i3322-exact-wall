# Sprint 1243 pre-registration -- grid-free contact flags

Date: 2026-08-04

## Target

Use the saturated contact coordinate `Y(X)` from Sprint 1232 to control the
entire nested spectral flag directly, without shifted grids or packet capture.

## Registered prediction

For

```text
E_s=1_{Y(X)<=s},       F_s=1_{U<=s},
delta_s=||(E_s tensor I-I tensor F_s)psi||,
```

the layer-cake identity and global contact coercivity imply

```text
integral_[-1,1] delta_s^2 ds
 = E_psi |Y(X)-U|
 <= sqrt(40 epsilon_0).                              (1)
```

Combining (1) with Sprint 1242 should give, for the regularized Schmidt flags,

```text
integral |Tr(E_s W_A,t)-Tr(F_s W_B,t)|^2 ds
 <= r sqrt(40 epsilon_0)/(4t).                       (2)
```

## Failure conditions

- the indicator layer-cake identity has a missing factor;
- saturation makes `Y(X)` leave `[-1,1]`;
- Sprint 1232 does not globally own `(U-Y(X))^2/40`;
- or the soft-flag estimate introduces a grid or occurrence multiplier.

## Claim boundary

This controls contact identification of the ordered flags. Transporting both
flags through the two response correspondences and proving finite-rank
closure remain separate.
