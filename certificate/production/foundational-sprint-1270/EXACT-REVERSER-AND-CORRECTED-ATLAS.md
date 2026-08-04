# The exact reverser repairs the shooting atlas

Status: **exact reverser; corrected atlas is a numerical ancestry check**

For `M(x,y,u)=(y,z,v)`, define

```text
R(x,y,u)=(-y,-x,1/v).                               (1)
```

The diagonal cost is unchanged by `(x,y)->(-y,-x)`.  Substituting the
definition of `v` into the next response ratio gives exactly

```text
third(M(R(x,y,u)))=1/u.                             (2)
```

The second coordinate is `-w`, where `(w,x,r)=M^-1(x,y,u)`.  Hence

```text
R^2=I,             R M R=M^-1.                     (3)
```

Moreover `R(s)=s` is precisely

```text
x+y=0,             v=1/u,                          (4)
```

the two reflection residuals used by the validated shooting degree.

The corrected numerical atlas uses only the chart pieces certified before
the section in Sprints 1192--1193 and their images under (1).  It never
propagates a generic parameter forward past the section.  Its symmetric
carrier is `[-0.898,0.898]`: the exact boundary contact has predecessor
`0.898116...`, while Sprint 1217 types the remaining edge as an inactive
outer sliver rather than part of the shooting graph.  All three registered
roots lie in this active carrier.  Unlike Sprint 1269's rejected atlas, the
corrected overlaps are single-valued and the three drift roots reappear in
the registered boxes.

The reverser identities are exact.  The reconstructed root count remains a
floating-point cross-check; Sprint 1268's interval zero-count gate is still
open.

The atlas also records, but does not gate on, the reciprocal-normalization
diagnostic `F(x)F(-x)-b(x)^2`.  Sprint 1271 uses its nonzero value to reject
the inference that the exact characteristic reverser automatically preserves
the globally assembled Bellman amplitude normalization.  Sprint 1272 further
clarifies that this atlas diagnostic is local: it must not be quoted as the
global Bellman normalization-defect profile.
