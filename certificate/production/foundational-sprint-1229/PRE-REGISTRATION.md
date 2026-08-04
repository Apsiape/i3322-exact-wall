# Sprint 1229 pre-registration

Register the conservative constants

```text
Lip(sqrt(A)), Lip(sqrt(B)) <= 28,
packet ratio coefficient <= 24,
c_A=1344,
c_B=672,
c_0=54,
C_h=131498424/5,
mu=7/8000,
h_0=1/10000000.
```

The gate is

```text
C_h h_0^2 < mu^2/2.
```

The verifier must check this exactly over the rationals and independently
test the completed scalar inequality on hostile generated fixtures.

