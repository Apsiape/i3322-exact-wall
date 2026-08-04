# Exact contact normal form; argmin identification fails its gate

## Exact result

Assume a differentiable active Bellman point with a unique interior minimizer
and fixed predecessor `P(x)=x`.  Bellman equality and stationarity reduce
exactly to

```text
E_B = 4F^2-4F(q+1-x^2)+(1-x^2)=0,

E_S = (2F+x-1)(-4Fx-2F+2x^2+x-1)/2=0.
```

On the numerical low-`F` branch,

```text
F=(2x^2+x-1)/(2(2x+1)),
4x^4-(4q+5)x^2+(q+2)=0.
```

All symbolic factorization, substitution, and resultant residuals vanish
exactly.

Using the certified `q*` interval, Arb gives

```text
x_* = -0.87827294518081245...
F_* =  0.2217619690903789...
c_* =  1.162282470002661...
```

with interval widths below `3.2e-16`, and `c_*>1.16` throughout the box.

## Registered numerical comparison

Five of six gates pass:

```text
|x_bottleneck-x_*|          2.6642e-6     PASS (<5e-6)
|F_51201(x_*)-F_*|          4.9510e-9     PASS (<2e-5)
|F'_51201(x_*)-(1/2-x_*)|   6.2452e-5     PASS (<0.01)
|P_51201(x_*)-x_*|          1.0280e-4     FAIL (<3e-5 registered)
```

The combined predecessor/value gate therefore fails, and the run is not
reported as all-pass.

## Interpretation

The stable quantities are the value and first derivative of the envelope.
The unstable quantity is the coordinate of its nearly flat minimizer.  That
is the expected conditioning pattern near a parabolic contact: a tiny value-
function perturbation can move the argmin substantially without materially
changing the envelope jet.

This does not establish the contact.  It changes the right proof target.  A
rigorous campaign should not try to enclose `P(x_*)` tightly from a sampled
argmin.  It should prove the global value inequality

```text
L_z(x_*) >= F_*  for every z in [-1,1],
```

with equality at `z=x_*`, using certified bounds for the Bellman profile.
That establishes realization directly and lets stationarity/curvature be
handled locally at an exactly specified algebraic point.

## Consequence if the realization gate lands

At a certified fixed predecessor, every finite positive weight cancels on the
one-point orbit, leaving multiplier `c_*>1.16`.  The Bellman derivative then
cannot be a contraction in any bounded positive weighted sup norm.  The
three-root proof would have to use monotone order bounds, degree, or a
parabolic normal form rather than Banach contraction.

## Claim boundary

The conditional normal form and Arb evaluation are exact.  The global
realization is not proved, and one preregistered numerical gate failed.  No
public theorem is changed.

## Subsequent closure

Sprint 1281 identifies `x_*=-C` exactly, where `C` is the already certified
Sprint-1115 high-plateau coordinate.  Exact reversibility realizes the global
fixed characteristic `(-C,-C,1/R)`.  Thus the missing realization gate in
this document is closed by ancestry, not by repairing the failed sampled
argmin gate.
