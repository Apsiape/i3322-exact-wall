# Disclosure — small-d truncation fixture (DEMOTED to [V] artifact)

Demoted from guards/ per U1-gate findings F20-F22: (1) the six
committed segments are the per-d ARGMAX over all admissible windows of
the 12-site fixture excerpt (verified independently: rank 1 of N at
every d) — legitimate for a supremum but previously undisclosed, and
the "parity-resolved rise" compares non-nested windows selected by
that rule; (2) the fixture's source payload hash covers a 255-entry
payload of which only 11 profile + 12 vector entries are present, and
no guard recomputes it; (3) the results JSON was rewritten on replay
with platform line endings, breaking its manifest seal (the sealed LF
content survives as GUARD_SMALL_D_STDOUT.txt, byte-identical).

The 140-decimal exact-rational interval arithmetic in the script is
genuine and fail-capable (gate-verified). The scores are correct for
what they are: Bell values of specific truncated-window strategies on
the fixture excerpt, all strictly below the certified window. They are
NOT load-bearing for any theorem and are NOT a second engine for the
U1E construction. The construction's second engine is
guards/guard_second_engine_projectors.py (symbolic projector
verification at arbitrary block angles; its PART B uses the PV
open-endpoint padding convention, not the endpoint-projector
completion — see its NOTE). [UPDATED 2026-08-07, round-5 integrity
finding 6: PART B was PROMOTED in the U1G round to load-bearing for
EXACTLY ONE FACT — the exhibited values at d = 24 and d = 33 strictly
exceed 1/4 (guard-asserted, Rayleigh-backed; proof section 1b). For
every OTHER purpose, including this fixture and the truncation
construction, PART B remains non-load-bearing, and its PV-padding
convention never touches the exhibited values.]
