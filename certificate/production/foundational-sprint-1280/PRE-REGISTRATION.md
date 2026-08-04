# Pre-registration: algebraic Bellman contact normal form

For a differentiable active Bellman point with a unique interior predecessor
and `P(x)=x`, derive exactly:

```text
E_B = 4F^2-4F(q+1-x^2)+(1-x^2) = 0,
E_S = (2F+x-1)(-4Fx-2F+2x^2+x-1)/2 = 0.
```

On the low-`F` branch, eliminate `F` and verify that the non-endpoint factor is

```text
4x^4-(4q+5)x^2+(q+2)=0.                 (1)
```

Define its outer negative candidate by

```text
y_+ = [4q+5+sqrt(16q^2+24q-7)]/8,
x_* = -sqrt(y_+),
F_* = (2x_*^2+x_*-1)/(2(2x_*+1)).       (2)
```

Use Arb on the certified `q*` interval and compare (2) against the 51,201-node
global Bellman reconstruction.  Register:

1. all symbolic factorization and substitution residuals vanish exactly;
2. the Arb widths of `x_*`, `F_*`, and
   `c_*=(1-x_*^2)/(4F_*^2)` are below `1e-15`;
3. `c_*>1.16` throughout the Arb box;
4. the numerical bottleneck coordinate is within `5e-6` of `x_*`;
5. `|P_51201(x_*)-x_*|<3e-5` and
   `|F_51201(x_*)-F_*|<2e-5`;
6. `|F'_51201(x_*)-(1/2-x_*)|<0.01`.

Passing proves the conditional exact normal form and a high-resolution
numerical identification.  It does not prove that the continuum Bellman
minimizer realizes the candidate or that its contact is unique/global.
