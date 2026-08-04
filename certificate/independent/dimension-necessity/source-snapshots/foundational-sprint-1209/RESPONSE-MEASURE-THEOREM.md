# Response debt is reflected-measure asymmetry

Status: **representation-free measure theorem; two-response composition still
open**

## Theorem

Use the notation of Sprint 1208. Let `E=E_A(eta)` be the sign-symmetric good
projection, and put

```text
w=E L_A psi,
delta_A=||(I-K_A)w||,
m_A=||w||^2.                                         (1)
```

Define the finite positive spectral measure `nu_A` on `[-1,1]` by

```text
integral f(x) d nu_A(x) = <w,f(X)w>.                 (2)
```

Let `sigma(x)=-x`. Then, with the dual total-variation norm

```text
||rho||_TV* = sup_{||f||_infinity<=1} |integral f d rho|,
```

one has

```text
||nu_A-sigma_*nu_A||_TV* <= 2 sqrt(m_A) delta_A.     (3)
```

If `m_A>0`, the normalized measure `hat_nu_A=nu_A/m_A` satisfies

```text
||hat_nu_A-sigma_*hat_nu_A||_TV*
    <= 2 delta_A/sqrt(m_A).                          (4)
```

Sprint 1208 gives `delta_A<=sqrt(2 epsilon_A)`. If
`||(I-E)psi||^2<=theta_A<1`, then `m_A>=eta(1-theta_A)` and therefore

```text
||hat_nu_A-sigma_*hat_nu_A||_TV*
 <= 2 sqrt(2 epsilon_A/[eta(1-theta_A)]).            (5)
```

The identical statement holds for Bob.

## Proof

The symmetric cutoff commutes with `K_A`, and the sign relation gives

```text
K_A f(X) K_A=f(-X).                                  (6)
```

Hence, for `F=f(X)`,

```text
<w,Fw>-<w,f(-X)w>
 = <w,Fw>-<K_A w,F K_A w>
 = <w-K_Aw,Fw>+<K_Aw,F(w-K_Aw)>.                    (7)
```

Both `K_A` and `f(X)` have their expected operator norms. Cauchy--Schwarz
turns (7) into

```text
absolute difference <= 2 ||f||_infinity ||w|| delta_A,
```

which proves (3). Division by `m_A` gives (4). On the range of `E`,
`L_A^2=A(X)>=eta`; consequently

```text
m_A=<E psi,A(X)E psi> >= eta ||E psi||^2,
```

and (5) follows.

No spectral atom, multiplicity basis, Schmidt form, or aligned carrier enters
the proof.

## What this changes

Near-optimality now has a basis-free operational consequence:

```text
local response debt
  => failed weighted reflection in Hilbert norm
  => reflected-measure asymmetry in total variation.                 (8)
```

This closes the passage from operator remainders to classical transport
measures. It also reveals the next obstruction. Alice and Bob do not preserve
one common unweighted measure; they preserve differently weighted measures.
The ratio between those weights is the amplitude cocycle that produced the
geometric wall and its exponential boundary law. Normalizing the two measures
independently would erase precisely the quantity that owns the dimension
rate.

## Next gate

Construct the cocycle-valued composition of the two approximate reflected
measures along the `R_0` contact coupling. The required theorem must show that
on a rank-`d` carrier this composition decomposes into finite directed chains,
not cycles, and that the cocycle bounds each chain's weight growth. Sprint
1207's sharp endpoint lemma can then charge the chain boundary.
