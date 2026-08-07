SUPERSEDED STAMP (2026-08-07): this EXTRACT deleted the G1 source's
own status-limiting line (round-3 integrity finding 3 - the F23
pattern). Superseded by the FULL byte-identical source now in
dependencies/G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md.
Retained as history of the defect only.

# G1 — promoted upper-only receipt extract

**Scope:** U1 upper-bound live chain only.  
**Authority:** promoted G1 as specified by the I3322 close-out commission.  
**Source file SHA-256:** `6dbb19c7d00a9fd5d0535b896ab6565f226ce6ae6fab381ea6f71a5f3fa9598a` (`G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md` in sealed v28.1).

This extract carries only the statements consumed by U1.

Let `g=g_S` be the canonical critical storage and
\[
b(t)=\frac{\sqrt{1-t^2}}2.
\]
The promoted G1 receipt gives endpoint positivity and the following lawful conditional endpoint argument: if a sequence of full-zero pairs has a scalar coordinate `t_n` tending to either endpoint of `[-1,1]`, zero-set localization along that sequence gives
\[
g(t_n)g(-t_n)=b(t_n)^2\longrightarrow0.
\]
Continuity then contradicts the promoted positive endpoint values. Consequently no full-zero sequence reaches either scalar endpoint, and the closed full-zero locus is compactly interior:
\[
\boxed{Z:=R_0^{-1}(0)\Subset(-1,1)^2.}
\]
Hence every endpoint label obtained as a limit of the selected full-zero carrier orbit lies in one fixed compact subinterval of `(-1,1)`. On that compact corridor the multiplier functions used below are finite, continuous, and strictly positive.

**Claim boundary.** This extract does not assert any unconditional endpoint identity and does not provide any numerical corridor or rate constant.

---

RETRACTION-BLOCK-BEGIN
Restored retraction notice (U1E ledger entry 6; deleted from the U1
extract by an over-broad literal blacklist — U1 gate finding F5/F23):
the UNCONDITIONAL/global endpoint-product identity g(1)g(-1)=0 is
FALSE as a global receipt and is KILLED. The valid statement is the
conditional one used above: IF a sequence of full-zero labels
approaches an endpoint, zero-set localization and continuity force
g(1)g(-1)=0 — which endpoint positivity contradicts; hence no such
sequence exists and the zero locus is compactly interior. Nothing in
this bundle may consume the unconditional identity.
RETRACTION-BLOCK-END
