# Rank-Costed Packet Identity and Alternating-Block Truncation

**Status:** Abstract theorem package with a conditional I3322 sharp-profile corollary.  
**Purpose:** Close the packet-identity and multiplicity accounting receipts,
freeze the constructive rank/index convention, and reduce the matching upper
bound to a scalar tail estimate.

---

## 1. Joint spectral packet identity

Let

\[
|\psi\rangle
=
\operatorname{vec}(M)
\in
\mathcal H_A\otimes\mathcal H_B
\]

be a normalized pure state, with coefficient matrix \(M\).

Let

\[
\{E_j\}_j\subset B(\mathcal H_A),
\qquad
\{F_j\}_j\subset B(\mathcal H_B)
\]

be mutually orthogonal spectral projections paired by the equality graph.

Define the paired packet block

\[
D_j=F_jME_j^{\mathsf T},
\]

with the transpose adjusted to the chosen vectorization convention.

Then

\[
(E_j\otimes F_j)|\psi\rangle
=
\operatorname{vec}(D_j),
\]

and therefore

\[
\boxed{
w_j
:=
\|D_j\|_F^2
=
\langle\psi,E_j\otimes F_j\,\psi\rangle.
}
\]

Thus the matched-block packet weight is exactly the state's total probability
mass on the corresponding joint scalar-orbit cell.

This remains true with arbitrary fibre multiplicity. Fibre multiplicity changes

\[
r_j:=\operatorname{rank}D_j,
\]

but not the packet mass identity.

### Scalar-wall specialization

If the equality representation has one-dimensional scalar fibres and diagonal
state amplitudes

\[
|\psi\rangle
=
\sum_j\lambda_j|j,j\rangle,
\]

then

\[
D_j=[\lambda_j],
\qquad
r_j=1,
\qquad
\boxed{w_j=\lambda_j^2.}
\]

This is the packet identity needed to connect the scalar cocycle mass to the
finite-rank theorem.

---

## 2. Exact rank additivity

Assume the packet blocks have mutually orthogonal left and right supports:

\[
F_iF_j=0,
\qquad
E_iE_j=0
\qquad(i\ne j).
\]

Then for every finite packet set \(J\),

\[
\boxed{
\operatorname{rank}
\left(
\sum_{j\in J}D_j
\right)
=
\sum_{j\in J}r_j.
}
\]

### Proof

Choose bases respecting the orthogonal decompositions

\[
\mathcal H_A
=
\bigoplus_jE_j\mathcal H_A
\oplus\mathcal H_A^\perp,
\]

\[
\mathcal H_B
=
\bigoplus_jF_j\mathcal H_B
\oplus\mathcal H_B^\perp.
\]

The sum is block diagonal with diagonal blocks \(D_j\). Matrix rank is additive
over a block diagonal sum.

---

## 3. Exact rank-costed packet profile

For packet set \(J\), define

\[
\operatorname{cost}(J)
=
\sum_{j\in J}r_j,
\]

and

\[
\operatorname{mass}(J)
=
\sum_{j\in J}w_j.
\]

The maximum packet mass that a rank-\(d\) carrier can retain is

\[
\boxed{
\Phi(d)
=
\sup_{\operatorname{cost}(J)\le d}
\operatorname{mass}(J).
}
\]

If

\[
W=\sum_jw_j,
\]

the exact unavoidable packet loss is

\[
\boxed{
\mathcal T_{\rm rank}(d)
=
W-\Phi(d).
}
\]

This is a zero-one knapsack profile whose item weights are state masses and
whose item costs are fibre ranks.

The multiplicity-blind tail

\[
\sum_{j>d}w_{(j)}
\]

is a universal relaxation because every nonzero packet costs at least one
Schmidt direction:

\[
\boxed{
\mathcal T_{\rm rank}(d)
\ge
\sum_{j>d}w_{(j)}.
}
\]

Equality holds when every packet has rank one.

---

## 4. Bounded-multiplicity comparison

Assume

\[
1\le r_j\le m
\]

for all packets.

Let \(w_{(j)}\) be the decreasing mass rearrangement. Then

\[
\boxed{
\sum_{j>d}w_{(j)}
\le
\mathcal T_{\rm rank}(d)
\le
\sum_{j>\lfloor d/m\rfloor}w_{(j)}.
}
\]

### Proof

A rank-\(d\) carrier cannot retain more than \(d\) nonzero packets, giving the
lower bound.

It can always retain the \(\lfloor d/m\rfloor\) largest packets, whose total
cost is at most \(d\), giving the upper bound.

Thus bounded multiplicity preserves the packet-tail universality class but
rescales the exponential rate when it is expressed per unit Schmidt rank.

---

## 5. Constructive rank-one wall

Suppose the exact scalar wall is represented in a common local basis by:

1. a diagonal Schmidt state
   \[
   |\psi\rangle=\sum_{j\in\mathbb Z}\lambda_j|j,j\rangle,
   \qquad
   \lambda_j>0;
   \]
2. binary measurements whose nontrivial blocks are rank-one \(2\times2\)
   projectors on two alternating nearest-neighbour matchings;
3. possible one-dimensional endpoint blocks.

For a finite interval

\[
I=[-L,R]\cap\mathbb Z,
\]

truncate and normalize:

\[
|\psi_I\rangle
=
\frac{
\sum_{j\in I}\lambda_j|j,j\rangle
}{
\left(\sum_{j\in I}\lambda_j^2\right)^{1/2}
}.
\]

Complete every severed alternating measurement block by a one-dimensional
projector at the finite endpoint.

Then:

- every local measurement remains a valid projection;
- the local dimension is
  \[
  N=|I|=L+R+1;
  \]
- every retained amplitude is positive, so
  \[
  \boxed{
  \operatorname{Schmidt\,rank}|\psi_I\rangle=N.
  }
  \]

Thus in the constructive rank-one wall,

\[
\boxed{
d=N
}
\]

exactly. There is no multiplicity conversion between total retained orbit sites
and Schmidt rank.

---

## 6. Response-step index convention

Let \(S_{\rm char}\) be one characteristic shooting step.

The supplied response typing is

\[
\tau=S_{\rm char}^2.
\]

Therefore one response step advances two characteristic sites and preserves
parity.

The full scalar state nevertheless contains both parity subsequences, joined
by the alternating bond structure. Consequently:

- one parity response depth \(n\) spans approximately \(2n\) characteristic
  sites;
- a two-sided physical truncation counts all retained characteristic sites;
- its local dimension and Schmidt rank equal the total site count.

Hence:

\[
\boxed{
\text{response depth on one parity}
\ne
\text{total packet count}
=
\text{constructive Schmidt rank}.
}
\]

This freezes the index ledger:

| Quantity | Unit |
|---|---|
| shooting index | one characteristic site step |
| response index | two characteristic steps on one parity |
| packet count | all retained scalar orbit cells |
| half-width | sites retained on one side |
| total width | left + right + centre |
| constructive local dimension | total retained sites |
| constructive Schmidt rank | total retained sites |

---

## 7. Alternating-block truncation error

Assume every Bell expectation in the scalar wall is a finite linear
combination of:

\[
\lambda_j^2
\]

and nearest-neighbour terms

\[
\lambda_j\lambda_{j+1},
\]

with uniformly bounded coefficients.

Let

\[
T_I
=
\sum_{j\notin I}\lambda_j^2
\]

be omitted mass, and let

\[
B_I
=
|\lambda_{-L-1}\lambda_{-L}|
+
|\lambda_R\lambda_{R+1}|
\]

be the two cut-bond masses.

Then there is a functional-dependent constant \(C_B<\infty\) such that

\[
\boxed{
0\le
S-\mathcal B(\psi_I)
\le
C_B
\frac{T_I+B_I}{1-T_I}.
}
\]

### Proof sketch

Inside \(I\), the infinite and finite alternating blocks agree exactly.

Every term removed from the infinite expectation is either:

- a diagonal term supported outside \(I\), bounded by omitted mass;
- a nearest-neighbour term entirely outside \(I\), bounded by tail mass using
  \(2|\lambda_j\lambda_{j+1}|\le\lambda_j^2+\lambda_{j+1}^2\);
- one of the two severed boundary bonds.

Normalization contributes the factor \((1-T_I)^{-1}\).

Since the Bell functional has finitely many bounded terms, their constants sum
to \(C_B\).

---

## 8. Geometric-tail upper bound

Assume the packet masses satisfy two-sided tail estimates

\[
\lambda_j^2
\asymp
|j|^{-p_\pm}e^{-\kappa_\pm|j|}
\]

on the two tails.

Then

\[
|\lambda_j\lambda_{j+1}|
\asymp
\lambda_j^2
\]

on each tail.

The alternating-block truncation theorem gives

\[
S-\mathcal B(\psi_{[-L,R]})
\lesssim
w_L^-+w_R^+.
\]

Optimal allocation under

\[
L+R+1=d
\]

therefore yields

\[
\boxed{
S-Q_d
\lesssim
d^{-p_{\rm eff}}
e^{-\kappa_{\rm eff}d},
}
\]

with the same harmonic effective exponents as the packet-rearrangement lower
bound.

Thus a matching tail theorem for the scalar amplitudes closes the matching
upper-bound receipt.

---

## 9. I3322 receipt ledger

### D1 — Packet identity

**Closed abstractly.**

The matched blocks \(D_j\) are the joint spectral blocks of the state
coefficient matrix, and

\[
w_j=\|D_j\|_F^2
\]

is their exact scalar-cell state mass.

For the released alternating rank-one wall,

\[
w_j=\lambda_j^2.
\]

### D2 — Coupling comparison

**Qualitatively closed; exact tail constants remain artifact-dependent.**

The Jacobi coupling is

\[
b(x)=\frac{\sqrt{1-x^2}}2.
\]

Endpoint exclusion confines the state-carrying orbit to a compact interior
interval, so

\[
0<b_-\le b(x_j)\le\frac12.
\]

If the positive cocycle gives two-sided adjacent mass-ratio bounds, then

\[
c_j=b(x_j)\lambda_j\lambda_{j+1}
\asymp
\lambda_j^2=w_j.
\]

The supplied record states geometric scalar tails, but the exact ratio
constants are not in the pasted artifact package.

### D3 — Multiplicity density

**Closed for the constructive wall; exact universally by rank cost.**

For arbitrary fibres, the cost of packet \(j\) is \(r_j\), and the exact
profile is the rank-costed knapsack \(\mathcal T_{\rm rank}\).

For the released constructive scalar wall, all alternating scalar blocks are
rank one, so the cost is exactly one Schmidt direction per retained orbit cell.

### D4 — Index convention

**Closed for the constructive wall.**

Total retained orbit sites = local dimension = Schmidt rank.

One response step = two characteristic steps on one parity. This does not add
a factor of two to total packet count because both parities are present.

### D5 — Matching upper bound

**Reduced to the two-sided scalar tail receipt.**

Alternating-block truncation gives a valid finite strategy and bounds its
deficit by omitted scalar mass plus the two cut bonds.

A two-sided scalar mass estimate of the form

\[
\lambda_{(j)}^2
\asymp
j^{-4}\Gamma^{-j}
\]

would therefore yield

\[
S-Q_d
\lesssim
d^{-4}\Gamma^{-d}.
\]

Combined with the banked lower bound, this would prove the sharp profile.

---

## 10. Arithmetic anatomy of the supplied constant

The accepted private constant is

\[
\Gamma=9{,}475{,}854{,}336.
\]

It factorizes exactly as

\[
\boxed{
\Gamma
=
312^4
=
97{,}344^2
=
2^{12}3^4 13^4.
}
\]

Therefore a packet-mass floor

\[
w_j
\gtrsim
j^{-4}\Gamma^{-j}
\]

is equivalent to an amplitude floor

\[
\boxed{
\lambda_j
\gtrsim
j^{-2}97{,}344^{-j}.
}
\]

Because one response step consists of two characteristic steps, the further
factorization

\[
97{,}344=312^2
\]

is consistent with—but does not by itself prove—a characteristic-step
amplitude bound using base \(312\).

No ancestry for the number \(312\) is claimed without the private quantitative
artifact.

---

## 11. Correct sharp-profile target

The remaining quantitative theorem is no longer five unrelated receipts.

It is one scalar-tail equivalence:

\[
\boxed{
\lambda_{(j)}^2
\asymp
j^{-4}\Gamma^{-j}
}
\]

for the normalized exact scalar wall, with indexing explicitly tied to total
rank-one packet count.

Once that is proved:

- packet identity gives the lower profile;
- bounded interior couplings give conductance matching;
- rank-one truncation gives the finite upper profile;
- the index ledger removes factor-of-two ambiguity.

Therefore:

\[
\boxed{
S-Q_d
\asymp
d^{-4}\Gamma^{-d}.
}
\]

---

## 12. Claim boundary

This theorem proves:

- exact packet/state-mass identity;
- exact multiplicity-aware rank cost;
- rank-one rank–width equality for the constructive alternating wall;
- an alternating-block truncation upper bound;
- the exact indexing ledger.

It does not prove the two-sided I3322 scalar amplitude tail or identify the
ancestry of \(312\).

Until that tail is certified, the banked \(d^{-4}\Gamma^{-d}\) result remains
a rigorous lower bound and a conditional sharp profile.
