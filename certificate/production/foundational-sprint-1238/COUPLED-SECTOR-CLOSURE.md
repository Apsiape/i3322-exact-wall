# Near-fixed mass forces drift mass

Status: **proved coupled-sector theorem; the universal dimension lower bound
remains open at terminal near-entry localization**

## 1. The correction in one line

The former reconstruction attempted to replace the four full coarse
omissions in the two-frame response theorem by their near-fixed parts. The
valid replacement retains the complementary mass:

```text
Delta_coarse <= delta_cap+4(m_D+m_out).             (1)
```

No response vector is restricted in (1). It is the decomposition of each of
four omission events into its intersection with the near-fixed sector and
its intersection with the complementary drift/tail sector.

## 2. Definitions and certified inputs

Use the constants and notation of the corrected blind reconstruction. Thus

```text
epsilon=epsilon_0+epsilon_A+epsilon_B,
m_N+m_D+m_out=1,
m_out<=C_out epsilon_0,
```

where `m_D` is the active-box complement of the near-fixed set. Put

```text
mu=7/8000,                 K=4656/25,
H=(39/10)K+mu^2/2,
theta=mu^2/(16H).
```

The shifted-grid theorem supplies one common shift for which the total of
the four near-fixed capture losses obeys

```text
delta_cap<=4 theta m_N+C_0 sqrt(epsilon_0),
C_0=100 sqrt(40)/h_0,      h_0=10^-7.               (2)
```

The maximal valid two-frame lemma and `L_sigma^2<=13/10` give

```text
D_A^2+D_B^2
 <=6(epsilon_A+epsilon_B)+(39/10)Delta_coarse.      (3)
```

Sprint 1229 applies to the common packets already constructed by the chosen
shift. If `W` is their total source/target mass, then

```text
(mu^2/2)W
 <=48epsilon_0+K(D_A^2+D_B^2),
W>=m_N-delta_cap.                                  (4)
```

Unlike the retracted proof, (3) is used globally. The drift and tail terms
in (1) are not discarded.

## 3. Coupled-sector inequality

Substituting (1)--(3) into (4) yields

```text
(mu^2/2)m_N
 <=48epsilon_0+6K(epsilon_A+epsilon_B)
   +H delta_cap+J(m_D+m_out),                       (5)

J=4(39/10)K=78K/5.
```

Because `4H theta=mu^2/4`, equations (2) and (5) give

```text
(mu^2/4)m_N
 <=48epsilon_0+6K(epsilon_A+epsilon_B)
   +H C_0 sqrt(epsilon_0)+J(m_D+m_out).             (6)
```

For an entirely rational public constant use `sqrt(40)<7` and define

```text
C0_bar=700/h_0,
C_N=(4/mu^2)(48+6K+H C0_bar),
C_D=(4/mu^2)J.                                      (7)
```

For `epsilon<=1`, every certificate debt is at most `sqrt(epsilon)`, so

```text
m_N<=C_D(m_D+m_out)+C_N sqrt(epsilon).              (8)
```

This is the maximal conclusion of the present argument. It does not say
that near-fixed mass is small.

## 4. A dimension-independent amount of drift is forced

Set

```text
C_T=C_N+(1+C_D)C_out,
w_0=1/[2(1+C_D)].                                   (9)
```

Using `m_out<=C_out sqrt(epsilon)` and the exact partition of total mass,
(8) gives

```text
1<=(1+C_D)m_D+C_T sqrt(epsilon).                    (10)
```

Therefore at least one of the following holds:

```text
epsilon>=1/(4 C_T^2),
m_D>=w_0.                                           (11)
```

The statement is weak numerically but structurally decisive: near-fixed
mass cannot absorb the complete state at arbitrarily small deficit. A fixed
amount of active drift must remain.

## 5. Why this does not yet close the dimension theorem

The original drift ledger treated every entry into the near-fixed sector as
a discard and bounded all such discards by a global estimate
`m_N=O(sqrt(epsilon))`. Equation (8) does not provide that estimate.

The remaining theorem must instead charge the **explicit terminal packet**
of each canonical drift chain. The intended route is to apply the already
valid Sprint 1229 inequality only to terminal packets that have actually been
captured in a common source/target family. This would avoid localizing a
global response defect. It is not established here.

Thus Sprint 1238 repairs the sector logic and forces drift, but it does not
authorize the conditional lower-bound ledger or a v1.3 release.
