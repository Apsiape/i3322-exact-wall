# Pointwise minimum does not select the Bellman branch

Status: **registered selector rejected**

Thirteen propagated shooting charts produce as many as ten characteristic
sheets over one target.  Selecting the least positive `F` candidate at each
target passes coverage and fails every substantive gate:

```text
minimum increment of selected P     -0.0382
apparent roots                       15
maximum F disagreement               0.1948
maximum P disagreement               0.0665
```

The Bellman solution is therefore not the pointwise minimum of untyped
characteristic values after arbitrary forward propagation.

This is not a failure of the Bellman minimum principle.  A characteristic is
only a stationary extremal.  Beyond a fold or conjugate point it need not be
an admissible minimizing branch, even when its displayed value is smaller.
The missing datum is a stability/Morse type on each sheet.  The certified
global graph already supplies the relevant necessary condition: its
predecessor projection is strictly increasing, equivalently the Bellman
envelope is strictly concave.

The next selector must first discard sheets with nonpositive local
`dP/dx`, then compare values only among the remaining stable sheets.  If that
also fails, a local Morse sign is insufficient and a global action/viscosity
selection rule is required.
