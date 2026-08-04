# Pre-registration: rigorous Bellman-gap anatomy

## Status of the numbers below

A non-rigorous high-precision scout has already estimated the decomposition.
This sprint is a certification campaign, not a blind discovery claim.

## Wager

For every positive Bellman witness `G`, rational endpoint `q`, and probability
flow `pi`, prove the exact identity

```text
q - Dual(pi)
 = sum_ij pi_ij [q-d_ij-b_i^2/G_i-G_j]
   + sum_i [r_i b_i^2/G_i+s_i G_i-2b_i sqrt(r_i s_i)].
```

Both sums are nonnegative when `G` is feasible. Apply the identity to the
Sprint 1290 upper witness and the Sprint 1288 path flow. Split the certified
upper-minus-rational-lower window into:

1. exact rational contact slack;
2. interval-certified interior balance slack;
3. exact rational terminal sink slack `s(-1)G(-1)`;
4. interval-certified rational-square-root floor tax.

## Certification targets informed by the scout

- contact slack lies in `[1.90e-7, 1.92e-7]`;
- interior balance slack lies in `[8.1e-8, 8.3e-8]`;
- terminal sink slack lies in `[2.57e-8, 2.59e-8]`;
- the 60-place square-root floor tax is positive and below `1e-58`;
- the four certified pieces enclose the exact rigorous window;
- contact is the largest of the three structural bills.

## Semantic correction under test

`b(+/-1)=0` makes the unmatched endpoints invisible to the **dual objective**.
It does not make them free relative to an arbitrary fixed positive primal
witness. The terminal column marginal pays `s(-1)G(-1)` unless the primal
endpoint tends to zero.

## Decision

- If the four-way ledger does not close, abandon the proposed gap anatomy.
- If it closes, prioritize an endpoint-adaptive/contact-adaptive upper witness
  before increasing the lower certificate's square-root precision.
