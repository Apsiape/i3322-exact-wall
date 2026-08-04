# Sprint 1222 pre-registration -- shifted monotone contact rounding

Date: 2026-08-03

## Target

Construct the paired row/column partition required by Sprint 1221 without
assuming aligned spectra. Quantify the off-matching mass directly from the
Bellman contact residual.

## Registered theorem

On the active predecessor chart, write `y=P^{-1}(x)`. For a width `h>0` and
shift `s in [0,h)`, partition both `y` and `u` by the intervals

```text
I_k(s)=[s+kh,s+(k+1)h).                             (1)
```

Use `I_k(s)` for the `U` blocks and `P(I_k(s))` for the `X` blocks. Then the
exact contact graph is block diagonal. Averaging over `s` should give

```text
E_s rho_off(s)
 <=h^-1 integral |P^-1(x)-u| dmu(x,u).              (2)
```

Sprint 1217's `P'>1/10` and

```text
r_0(x,u)>=(x-P(u))^2/160                            (3)
```

should therefore imply the existence of a shift with

```text
rho_off(s)<=(40 sqrt(10)/h) sqrt(epsilon_0).         (4)
```

## Failure conditions

- the shifted-grid separation probability exceeds `|y-u|/h`;
- the inverse-Lipschitz constant is misoriented;
- the mass estimate acquires a number-of-cells or dimension factor;
- or the paired row/column blocks fail to be one-to-one.

## Claim boundary

The shifted grid is paired but is not generally invariant under both contact
reflections. Reflection closure and finite-chain assembly remain open.
