# Pre-registration: the exact shooting reverser repairs the atlas

Let the shooting map be

```text
M(x,y,u)=(y,z,v).                                   (1)
```

Register the candidate reverser

```text
R(x,y,u)=(-y,-x,1/v).                               (2)
```

The exact algebraic gates are:

1. the third coordinate of `M(R(x,y,u))` is `1/u`;
2. consequently `R^2=identity`;
3. `R M R=M^-1` wherever the displayed denominators are nonzero; and
4. `R(x,y,u)=(x,y,u)` is exactly the shooting reflection section
   `x+y=0, v=1/u`.

After those identities pass, rebuild the numerical shooting atlas using only
the certified pre-section pieces and their `R` images.  The corrected atlas
must remove Sprint 1269's overlap contradiction and recover the three
Sprint-1268 drift roots.  Failure of either the exact identities or corrected
overlap kills this repair.

