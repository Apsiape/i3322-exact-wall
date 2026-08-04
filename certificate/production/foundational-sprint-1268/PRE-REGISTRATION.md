# Pre-registration after scout: certify the intrinsic drift chambers

This registration follows a non-rigorous PCHIP/Bellman scout and precedes any
interval proof.  It is therefore a certification target, not a blind
prediction.

On the active contact interval define

```text
p(u)=2 log alpha(u),
q(u)=2 log beta(u),
chi(u)=q(u)-p(u).                                   (1)
```

The scout predicts:

1. `chi` has exactly three simple zeros on `[-9/10,9/10]`, one in each of

   ```text
   [-0.867,-0.865],
   [-0.378,-0.376],
   [ 0.799, 0.802];                                (2)
   ```

2. at every zero `r`,

   ```text
   |a(r)+r|>1/20;                                  (3)
   ```

3. no additional zero is hidden in a boundary wing or between the three
   displayed boxes.

The mathematical consequence, if certified, is a four-chamber intrinsic
partition of order space.  Events near a chamber boundary cannot also be
horizontally coalesced, while away from the boundaries the sign of the actual
vertical difference is stable under the certified Lipschitz perturbation.

The target dies if the zero count exceeds three, a zero is multiple, or the
horizontal separation in (3) fails.  A floating-point root census is not
enough: the required result is a full-domain interval exclusion with a
separate simple-root certificate in each box.

