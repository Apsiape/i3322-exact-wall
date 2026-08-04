# Pre-registration: Arb matched-coordinate amplitude adjudication

Fix the discovered central parameter

```text
t1 = 0.0015293272133344497
```

and propagate the certified unstable parameterization four steps.  Write the
resulting state as `(x1,y1,u1)` with next ratio `v1`.  The reflected transition
carries source coordinate `-y1` and source amplitude

```text
A = sqrt(1-y1^2)/(2v1).
```

On the original four-step chart, solve with Arb intervals for the unique `t2`
near `0.001588` satisfying

```text
y4(t2) + y1 = 0.
```

Its target amplitude at the same coordinate is

```text
B = sqrt(1-y4(t2)^2) v4(t2)/2.
```

Use the certified connection rectangle `C_center +/- 1e-20`, 300-bit or
higher precision, the order-12 graph-transform polynomial, an initial outward
value allowance `3e-25` per state coordinate, and direct interval propagation.

Registered gates:

1. the two initial `t2` bracket faces have strict opposite signs;
2. bisection contracts the matched-coordinate bracket below `1e-15`;
3. the final coordinate residual interval contains zero;
4. the raw local Bellman equality interval contains zero with width below
   `1e-15`;
5. the amplitude-difference interval `B-A` excludes zero and has lower
   absolute bound above `1e-4`.

If all gates pass, the existing global amplitude assembly is rigorously
incompatible with the reflected local source amplitude at one matched
coordinate.  The aligned-wall/Bellman theorem assembly must then be marked as
having a load-bearing normalization gap until repaired; the result does not
by itself show that the stated I3322 constant is false.
