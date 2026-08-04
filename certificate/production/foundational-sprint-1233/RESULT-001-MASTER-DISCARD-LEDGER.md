# The quantitative proof has one owner per debt

Status: **second analytic reconstruction; master algebra exact; blind
independent proof still required for public promotion**

## 1. Abstract ledger theorem

Put `t=sqrt(epsilon)`, `A=20^2`, and `M=78/5`. Suppose fixed positive
constants `alpha,beta,lambda` satisfy

```text
L_d<=lambda A^d t,                                  (1)
W_D>=1-alpha t-L_d.                                 (2)
```

If `alpha t+L_d>=1/2`, then either

```text
t>=1/(4 alpha)
```

or

```text
t>=1/(4 lambda A^d).                                (3)
```

Both imply the final exponential law after reducing its universal prefactor.

Otherwise `W_D>=1/2`. If the finite-rank exit lower bill and the owned upper
bill are

```text
B>=W_D/[(d+1)M^(2d)],                               (4)
B<=beta[d t+L_d],                                   (5)
```

then (1), (4), and (5) give

```text
1/[2(d+1)M^(2d)]
 <=beta[d+lambda A^d]t
 <=beta(1+lambda)d A^d t.                           (6)
```

Therefore

```text
t>=c_1/[d(d+1)(AM^2)^d],                            (7)
epsilon=t^2
 >=c_2 d^-4(A^2M^4)^(-d)
 =c_2 d^-4(20M)^(-4d).                              (8)
```

This is exactly Sprint 1231's base `312^4`.

## 2. Concrete ownership map

| abstract slot | sole concrete owner |
|---|---|
| `alpha t` in (2) | saturated contact/boundary rounding, near-fixed mass, and far endpoint cutoff |
| `L_d` in (1)--(2) | sum of moving-frame source/target contact discards along the one specified history |
| `d epsilon` | repeated global response defect in the recurrence energy; bounded by `d t` in (5) |
| `d t` | terminal entries into near/far charged sectors across at most `d` exit times |
| lower bill (4) | reverse endpoint recurrence on one initial slice, with per-chain length at most `d` |

There is no slot for:

- a global flow;
- all reduced dihedral frames;
- a top-`d` selection repeated in time;
- a fibre partial isometry;
- a probability density; or
- a fixed gap on the inactive sliver.

## 3. Concrete-to-abstract verification

The mapping uses only direct-sum inequalities:

1. At one time, descendants of distinct initial cells lie in disjoint moving
   coarse blocks; their squared packet errors add.
2. The history has at most `d` response times, producing the factor `d` and
   no frame multiplicity beyond the specified path.
3. At one exit time, terminal packets are orthogonal; summing over at most
   `d` exit times produces the second factor `d` and no chain-count factor.
4. Saturated contact rounding and the near-fixed theorem concern the fixed
   state measure, so their total mass may be reused only through that explicit
   exit-time factor.
5. Sprint 1223's summed moving loss already includes every visited frame; it
   is not multiplied by `d` again in `L_d`.

These rules reproduce equations (1)--(5) without an unowned term. The second
reconstruction therefore agrees with Sprint 1231 after the two corrections:
near-fixed `O(sqrt(epsilon))` and saturated inactive-tail coercivity.

## Verdict

The internal analytic proof is complete. The public promotion gate is now
procedural but mandatory: a blind reconstruction must rebuild the
concrete-to-abstract map without reading Sprints 1231 or 1233, then compare
term by term. A failure changes the theorem; a pass ports it to the standalone
I3322 repository.

