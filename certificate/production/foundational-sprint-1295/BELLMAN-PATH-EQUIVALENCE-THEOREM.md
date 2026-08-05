# Universal Bellman--path equivalence

Status: **analytic theorem with exact algebraic and finite hostile guards**

## 1. Abstract theorem

Let `X` be a compact metric space, let `d:X x X -> R` be continuous, and let
`b:X -> [0,infinity)` be continuous.  For a word

```text
x=(x_0,...,x_n),       n>=1,
```

define the real symmetric `n x n` Jacobi matrix `J_x` by

```text
(J_x)_(k,k)       = d(x_k,x_(k+1)),
(J_x)_(k-1,k)     = (J_x)_(k,k-1) = b(x_k).
```

Put

```text
S = sup_(n,x) lambda_max(J_x)
```

and

```text
P = inf_(g in C(X), g>0)
      sup_(i,j in X) [d(i,j)+b(i)^2/g(i)+g(j)].                 (1)
```

Then

```text
P=S.                                                            (2)
```

The theorem concerns equality of values.  It does not say that every flow in
the Hellinger dual is itself one path.

## 2. The easy inequality: paths cannot beat Bellman storage

Fix a positive continuous `g`.  At every internal letter `x_k`,

```text
2 b(x_k) a_(k-1) a_k
 <= g(x_k) a_(k-1)^2 + b(x_k)^2/g(x_k) a_k^2.                  (3)
```

After summation, the coefficient of `a_k^2` is bounded by

```text
d(x_k,x_(k+1)) + b(x_k)^2/g(x_k) + g(x_(k+1)).                 (4)
```

The two endpoint coefficients only omit nonnegative terms.  Thus every
Rayleigh quotient of every `J_x` is bounded by the supremum in (1).  Taking
the two infima/suprema gives `S<=P`.

The source/target placement in (4) is important: `b(x_k)^2/g(x_k)` belongs to
the edge leaving `x_k`, while `g(x_(k+1))` is paid by the edge entering its
target.  This is exactly the convention in the I3322 operator weld.

## 3. The reverse inequality: terminal Schur pivots build the storage

Fix `q>S` and write `delta=q-S>0`.  For every word, the matrix

```text
q I - J_x >= delta I.                                          (5)
```

Its scalar LDL/Schur pivots satisfy

```text
p_0 = q-d(x_0,x_1),
p_k = q-d(x_k,x_(k+1))-b(x_k)^2/p_(k-1).                       (6)
```

Every pivot is at least `delta`.  Indeed, a pivot is the final scalar Schur
complement of a matrix bounded below by `delta I`; evaluating that Schur
complement as a quadratic minimization leaves at least `delta`.

For `j in X`, define

```text
g(j) = inf {terminal pivot of a finite history ending at j}.    (7)
```

Consequently `g>=delta`.  Extending any history ending at `i` by the edge
`i->j`, and using that the right side of (6) increases with the preceding
pivot, gives

```text
g(j) <= q-d(i,j)-b(i)^2/g(i).                                  (8)
```

This is precisely Bellman feasibility at `q`.

## 4. Why the infimum in (7) is continuous

This is the gate that prevents a measurable-storage shortcut.  Every terminal
pivot ending at `j` has the form

```text
constant(history,i) - d(i,j).                                 (9)
```

The one-edge histories have the same form without the nonnegative quotient.
Because `d` is continuous on compact `X x X`, all functions in (9) share one
uniform modulus of continuity in `j`.  The infimum of a family with a common
modulus has that same modulus.  Hence the `g` in (7) belongs to `C(X)`.

Thus every `q>S` is feasible in (1), so `P<=q`.  Letting `q` decrease to `S`
proves `P<=S`, completing (2).  Zeros of `b` cause no division and require no
limiting removal.

## 5. I3322 consequence

For this repository,

```text
X=[-1,1],
d(x,u)=x*u+(x-u)/2-1,
b(x)=sqrt(1-x^2)/2.                                             (10)
```

Sprint 1287 proves that every positive continuous `g` satisfying the Bellman
inequality at `q` gives

```text
omega_commuting(I3322) <= q.                                   (11)
```

Every finite path matrix from (10) occurs as a principal block of an open
Pal--Vertesi path with endpoints `1,-1`: prepend `1`, append `-1`, and, if
needed, add one dummy internal label to obtain the required odd carrier.
Padding a Rayleigh vector by zeros preserves its quotient exactly.  Internal
endpoint labels may equivalently be moved inward and recovered by continuity.
The exact block-to-Jacobi identity therefore gives

```text
omega_tensor(I3322) >= S.                                      (12)
```

Combining (2), (11), (12), and the standard inclusion of tensor strategies in
commuting strategies yields

```text
omega_tensor(I3322) = omega_commuting(I3322) = P = S.           (13)
```

Equation (13) restores equality of the two model values as a variational
theorem.  It does **not** identify that value with the historical decimal.

## 6. What is and is not repaired

The shrinking exact numerical window now brackets one common value, rather
than two potentially different model values.  Branching in the
Bellman--Hellinger flow dual cannot create a tensor/commuting value gap.

Still open:

- an exact closed form or independent characterization of the common value;
- whether the common value equals the historical shooting decimal;
- finite-dimensional attainment or nonattainment at the true value;
- spatial attainment at the true value; and
- the historical nonclosure and `C_qs \ C_q` corollaries.

No statement about those questions is inherited from the failed amplitude
assembly.
