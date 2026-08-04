# Pre-registration: exact two-response skew action

Sprints 1247--1249 control each response separately on the common
order-resolution event measure.  Before attempting a quantitative flux
theorem, compose the exact equality-case actions and fix every orientation.

Registered targets:

1. Alice must act by
   `(u,zeta)->(a(u),zeta+2 log(alpha(u)))`.
2. Bob must act by
   `(u,zeta)->(-u,zeta+2 log(beta(u)))`.
3. In the order `Bob` then `Alice`, the composition must be

   ```text
   (u,zeta)->(a(-u),zeta+log C(u)),
   C(u)=F(u)F(-P(-u))/[F(-u)F(P(-u))].
   ```

4. The exact action must recover finite-dimensional nonattainment: finite
   horizontal support plus finite vertical mass forces every occupied base
   point to be fixed and its vertical cocycle to be one.
5. Reversing the response order or evaluating Alice's multiplier at `u`
   instead of `-u` must be detected.

