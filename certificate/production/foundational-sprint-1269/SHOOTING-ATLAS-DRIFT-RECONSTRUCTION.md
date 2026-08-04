# The naive shooting atlas fails at the reflection section

Status: **registered negative result; reversible atlas remains open**

This reconstruction does not solve the Bellman min-plus equation used by
Sprint 1268.  It starts from the separately certified local shooting series,
propagates overlapping orbit charts, and reads

```text
F(x)=sqrt(1-x^2)u/2,
P(y)=x                                             (1)
```

directly from adjacent shooting states.

The registered construction fails.  Indiscriminately propagating every local
parameter past the reflection section gives

```text
maximum F overlap spread       about 0.195,
minimum predecessor increment about -0.093,
apparent drift roots           11 rather than 3.     (2)
```

All four registered comparison targets fail.

This is not evidence against Sprint 1268's three-root scout.  It reproduces a
known chart error: Sprint 1192 explicitly proves the positive branch only up
to the reflection section and states that the remaining half is its exact
reversible image.  Forward propagation beyond that section is the wrong
chart.  The large overlap contradiction is the guard detecting precisely that
mistake.

The next construction must first derive and verify the map's exact reverser,
then build the negative atlas from that reversible image.  No median gluing or
post-hoc monotone repair is admissible.
