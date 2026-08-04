# Pre-registration: the order-resolution event measure

The family of regularized supports from Sprints 1242--1246 still treats the
resolution parameter `t` as an external dial.  Before attempting another
finite-rank estimate, differentiate with respect to logarithmic resolution
and test whether the resulting object is a finite positive measure.

Registered claims:

1. For `rho>=0`,

   ```text
   K_t(rho)=t rho(tI+rho)^(-2)=-d W_t(rho)/d log(t)
   ```

   is positive and integrates over `d log(t)` to the support projection.
2. Pairing `K_t` with an ordered spectral projection-valued measure produces
   a positive measure on `order x log-resolution` of total mass `rank(rho)`.
3. On a commuting response block `C=c`, congruence by `C` translates the
   *event* resolution coordinate by `+2 log(c)`.  This is the dual convention
   to Sprint 1245's translation of the queried scale by `-2 log(c)`.
4. Unitary response transport pushes the order coordinate forward without
   changing total event mass.
5. The construction must fail loudly if the sign of the scale translation is
   reversed or if the `t` factor in `K_t` is omitted.

The general measure is expected to be standard spectral calculus.  The
I3322-specific question is whether its two response pushforwards and the
certified cocycle yield a quantitative finite-mass escape theorem.

