# Endpoint-clustered Bellman collider: mixed registered result

Status: **exact stronger upper certificate; preregistered quantitative targets
failed**

## Exact theorem

The committed symmetric nonuniform 25,601-knot rational witness proves

```text
omega_tensor <= omega_commuting <= 0.250875388108398.
```

Together with the exact dimension-255 lower strategy, this gives

```text
0.2508753845015185 < omega_tensor
                     <= omega_commuting <= 0.250875388108398,
```

with exact width recorded in `exact-endpoint-clustered-threshold.json` and
decimal width

```text
3.606879488552207e-9.
```

The immediate `10^-15` predecessor fails by a strictly negative exact
quadratic numerator.  The passing endpoint has a strictly positive exact
minimum.  These theorem gates are separate from the failed performance wager.

## Registered wager: failed

The preregistration required an upper endpoint below `0.250875387500000` and
a window below `3e-9`.  The exact result misses both targets.  No grid
parameter is retuned in this sprint.

## What the failure teaches

At the same knot count, the new window is approximately `1.956` times narrower
than the uniform-grid window.  Endpoint resolution therefore matters.  But
the improvement is materially smaller than the registered target.

The worst minimizer remains near `-0.8934`, and its envelope owner moves to
approximately `-0.99732634`, still inside the preregistered endpoint/contact
region.  Endpoint clustering did not displace the bottleneck; it resolved the
same coupled cell more efficiently.  The surviving receipt says that the
next mesh experiment should charge the owner endpoint more aggressively while
retaining adequate resolution at its interior partner.

## Claim boundary

This is a stronger fixed-witness upper theorem, not an exact-value theorem.
The performance miss blocks any claim that the registered blended mesh is
optimal or that an `h^2` continuum estimate has been proved.  Independent
reconstruction is required before this bound replaces Sprint 1293 in the
public packet.
