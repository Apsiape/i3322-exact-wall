# Current-\(S\) Carrier Profile by Endpoint Cesàro Transport

**Date:** 2026-08-05  
**Status:** exact logarithmic-rate reduction, conditional only on a coarse
interior endpoint receipt.  
**Supersedes:** `current-S-carrier-profile-v1`.

The v1 package unnecessarily demanded endpoint hyperbolicity and used an
over-specialized two-cycle formula. Neither is required for the logarithmic
finite-carrier rate.

---

## 1. Current exact carrier

Theorem (S) supplies a positive unit vector

\[
\lambda\in\ell^2(\mathbb Z)
\]

and a bi-infinite label sequence \(c_j\in(-1,1)\) satisfying

\[
P(c_{j+1})=c_j,
\]

\[
\frac{\lambda_{j+1}}{\lambda_j}=r_B(c_j),
\]

and

\[
H\lambda=S\lambda,
\]

with

\[
H_{jj}=d(c_{j-1},c_j),
\qquad
H_{j-1,j}=b(c_{j-1}).
\]

Here

\[
b(t)=\frac{\sqrt{1-t^2}}2,
\qquad
r_B(t)=\sqrt{\frac{g(t)}{g(-t)}}.
\]

The response-orbit representation is

\[
c_{2n}=u_n,
\qquad
c_{2n+1}=P(u_{n+1}),
\qquad
u_n=\tau^n(u_0).
\]

---

## 2. Exact two-boundary flux identity

For a finite interval

\[
I=[a,b]\cap\mathbb Z,
\qquad
M_I=\sum_{j=a}^b\lambda_j^2,
\]

let \(H_I\) be the principal compression and

\[
v_I=\frac{\langle\lambda_I,H_I\lambda_I\rangle}{M_I}.
\]

Then

\[
\boxed{
S-v_I
=
\frac{
b(c_{a-1})\lambda_{a-1}\lambda_a
+
b(c_b)\lambda_b\lambda_{b+1}
}{M_I}.
}
\]

This is exact: every internal Jacobi contribution survives compression and
only the two cut edges are unpaid.

---

## 3. Exact finite spatial realization constant

A finite principal path matrix is realized by the Sprint-1295 open
Pál--Vértesi padding:

1. prepend the endpoint label \(1\);
2. append the endpoint label \(-1\);
3. if necessary, add one dummy internal label to obtain the required odd
   carrier.

The Rayleigh vector is padded by zeros, so its quotient is unchanged.

Therefore every interval \(I\) has a finite spatial realization in local
dimension at most

\[
\boxed{|I|+3.}
\]

Consequently,

\[
\boxed{
S-S_{|I|+3}
\le
S-v_I.
}
\]

The constant three is worst-case and has no effect on the exponential rate.

---

## 4. Endpoint limits

Because \(\tau\) is increasing and the selected orbit is non-fixed, \(u_n\)
is monotone. Hence the extended limits

\[
\alpha=\lim_{n\to+\infty}u_n,
\qquad
\beta=\lim_{n\to-\infty}u_n
\]

exist.

The only remaining coarse geometric receipt needed below is:

\[
\boxed{
\alpha,\beta,
\lim_{n\to+\infty}P(u_n),
\lim_{n\to-\infty}P(u_n)
\in(-1,1).
}
\]

Call the two source-endpoint limits

\[
x_+=\lim_{n\to+\infty}P(u_n),
\qquad
x_-=\lim_{n\to-\infty}P(u_n).
\]

Since \(g\) is continuous and positive in the interior, \(r_B\) is continuous
and positive at all four endpoint labels.

No derivative of \(P,\tau\), or \(r_B\) is required.

---

## 5. The two outward amplitude multipliers

At the forward end,

\[
\frac{\lambda_{2n+2}}{\lambda_{2n}}
=
r_B(u_n)r_B(P(u_{n+1})).
\]

Therefore

\[
\boxed{
\rho_+
=
\lim_{n\to+\infty}
\frac{\lambda_{2n+2}}{\lambda_{2n}}
=
r_B(\alpha)r_B(x_+).
}
\]

Using \(r_A(t)r_B(t)=1\),

\[
\boxed{
\rho_+
=
\frac{r_B(\alpha)}{r_A(x_+)}.
}
\]

At the negative end, outward motion reverses the characteristic index. Thus

\[
\boxed{
\rho_-
=
\lim_{n\to+\infty}
\frac{\lambda_{-2n-2}}{\lambda_{-2n}}
=
\frac1{r_B(\beta)r_B(x_-)}
=
\frac{r_A(x_-)}{r_B(\beta)}.
}
\]

These formulas remain valid when the source and target endpoint intervals are
slightly asymmetric.

---

## 6. Why \(0<\rho_\pm<1\) needs no numerical multiplier certificate

Positivity of the interior cocycle gives

\[
\rho_\pm>0.
\]

Because \(\lambda\in\ell^2(\mathbb Z)\),

\[
\lambda_j\to0
\]

at both ends. If \(\rho_+>1\), the positive even subsequence would eventually
increase geometrically, impossible. Hence

\[
\rho_+\le1.
\]

Likewise,

\[
\rho_-\le1.
\]

Now suppose \(\rho_+=1\). Then

\[
r_B(\alpha)=r_A(x_+).
\]

The endpoint is a fixed response sector in the closure of the full-zero graph.
The two endpoint full-zero pairs and the equality of the transport densities
supply exactly the Sprint-1198 amplitude-elimination hypotheses. Its algebraic
conclusion is

\[
S\le\frac14,
\]

contradicting the certified fact \(S>1/4\).

Therefore

\[
\boxed{
0<\rho_+<1.
}
\]

The same argument at the other end gives

\[
\boxed{
0<\rho_-<1.
}
\]

Thus strict exponential decay follows from:

- existence of the exact probability carrier;
- endpoint cocycle limits;
- and the quarter-ceiling obstruction.

It does not require a hyperbolic base map.

---

## 7. Cesàro logarithmic tail theorem

Let

\[
a_n=\lambda_{2n}.
\]

Since

\[
\frac{a_{n+1}}{a_n}\to\rho_+,
\]

we have

\[
\log a_n
=
\log a_0
+
\sum_{k=0}^{n-1}
\log\frac{a_{k+1}}{a_k}.
\]

Cesàro convergence gives

\[
\boxed{
\lim_{n\to\infty}
-\frac1n\log\lambda_{2n}
=
-\log\rho_+.
}
\]

The odd subsequence differs by one bounded positive endpoint ratio, so it has
the same logarithmic rate.

At the negative end,

\[
\boxed{
\lim_{n\to\infty}
-\frac1n\log\lambda_{-2n}
=
-\log\rho_-.
}
\]

No summability of cocycle errors is needed.

Define the two one-sided boundary-flux exponents per characteristic site:

\[
\boxed{
\kappa_+=-\log\rho_+,
\qquad
\kappa_-=-\log\rho_-.
}
\]

Then

\[
\lim_{R\to\infty}
-\frac1R
\log\!\left(
b(c_R)\lambda_R\lambda_{R+1}
\right)
=
\kappa_+,
\]

and similarly on the left with exponent \(\kappa_-\).

---

## 8. Optimal finite-carrier allocation

For an interval retaining \(L\) sites to the left and \(R\) sites to the
right,

\[
|I|=L+R+1,
\]

the exact flux receipt has logarithmic form

\[
S-v_I
=
\exp(-\kappa_-L+o(L))
+
\exp(-\kappa_+R+o(R)).
\]

The optimal allocation balances the two exponents:

\[
\kappa_-L
\sim
\kappa_+R.
\]

Hence the effective exponent per total carrier dimension is

\[
\boxed{
\kappa_{\mathrm{eff}}
=
\left(
\frac1{\kappa_-}
+
\frac1{\kappa_+}
\right)^{-1}
=
\frac{\kappa_-\kappa_+}{\kappa_-+\kappa_+}.
}
\]

There are finite spatial strategies of dimensions \(d+O(1)\) satisfying

\[
\boxed{
S-S_{d+O(1)}
\le
\exp\!\left(
-\kappa_{\mathrm{eff}}d+o(d)
\right).
}
\]

Equivalently,

\[
\boxed{
\liminf_{d\to\infty}
-\frac1d\log(S-S_d)
\ge
\kappa_{\mathrm{eff}}.
}
\]

And the constructive carrier complexity obeys

\[
\boxed{
D_{\mathrm{upper}}(\varepsilon)
\le
\frac{\log(1/\varepsilon)}
{\kappa_{\mathrm{eff}}}
+
o(\log(1/\varepsilon)).
}
\]

---

## 9. Symmetric-endpoint corollary

If the response closure identifies the two outward rates,

\[
\rho_+=\rho_-=\rho,
\]

then

\[
\kappa_{\mathrm{eff}}
=
-\frac12\log\rho.
\]

Define

\[
\boxed{
R_S=\rho^{-1/2}.
}
\]

Then

\[
\boxed{
S-S_{d+O(1)}
\le
R_S^{-d+o(d)}.
}
\]

At the forward endpoint,

\[
\boxed{
R_S
=
\sqrt{\frac{r_A(x_+)}{r_B(\alpha)}}.
}
\]

This is the correct general endpoint formula.

The v1 expression

\[
\sqrt{\frac{r_B(\beta)}{r_B(\alpha)}}
\]

is valid only after an additional endpoint-pairing identity identifies
\(r_A(x_+)=r_B(\beta)\). That identity was not yet certified and is no longer
silently assumed.

---

## 10. Numerical scout

The spatial-attainment referee reconstructed approximately

\[
r_B(\alpha)\approx0.9276,
\]

\[
r_A(x_+)\approx1.0766.
\]

The corrected one-tail scout is therefore

\[
\rho_{\mathrm{scout}}
=
\frac{0.9276}{1.0766}
\approx
0.8616013,
\]

\[
\boxed{
R_{S,\mathrm{scout}}
=
\sqrt{\frac{1.0766}{0.9276}}
\approx
1.0773252.
}
\]

Thus

\[
\frac1{\log R_{S,\mathrm{scout}}}
\approx
13.4262.
\]

These values remain reconnaissance, not certified intervals.

---

## 11. Receipt collapse

The v1 profile program requested:

- endpoint hyperbolicity;
- a Lipschitz bound on \(\log r_B\);
- explicit exponential orbit-entry estimates;
- and separate strict multiplier inequalities.

For the logarithmic finite-carrier rate, all four are unnecessary.

The exact remaining receipts are now:

### E1 — Coarse interior endpoint receipt

Prove that the four endpoint labels

\[
\alpha,\beta,x_+,x_-
\]

lie in one compact subinterval of \((-1,1)\).

No sharp decimal is required.

### E2 — Optional numerical rate certificate

Certify intervals for the four endpoint transport densities and therefore for

\[
\rho_\pm,\quad
\kappa_\pm,\quad
\kappa_{\mathrm{eff}}.
\]

This computes the rate but is not needed to prove that it is strictly positive.

### E3 — Matching lower profile

Prove

\[
S-S_d
\ge
\exp\!\left(
-\kappa_{\mathrm{eff}}d-o(d)
\right),
\]

or identify the unavoidable loss.

Only E3 is needed to turn the constructive rate into the exact asymptotic
profile.

---

## 12. Foundational meaning

The rate does not require smooth hyperbolic dynamics. It is fixed by the
asymptotic settlement ratio of continuation receipts:

\[
\boxed{
\text{carrier exponent}
=
\text{harmonic combination of the two endpoint receipt exponents}.
}
\]

The finite carrier pays exactly at its two artificial boundaries. The
completed state is normal because the total continuation mass is a
probability measure; the convergence rate is the Cesàro average of the
logarithmic transport receipts along that measure.

---

## 13. Claim boundary

Proved here, conditional on Theorem (S) and E1:

- strict geometric decay at the logarithmic level;
- the two one-sided endpoint exponents;
- optimal two-tail allocation;
- the constructive finite-dimension exponent;
- the exact worst-case padding constant \(3\).

Not proved:

- a certified decimal interval for the rate;
- a matching lower exponent;
- a multiplicative asymptotic constant.
