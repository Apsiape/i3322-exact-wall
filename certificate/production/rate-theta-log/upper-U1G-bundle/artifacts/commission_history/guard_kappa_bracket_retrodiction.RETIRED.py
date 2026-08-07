# RETIRED (2026-08-07, round-3 finding F20): this guard consumes the
# RETIRED selected-tail bracket and printed a green PASS line naming
# strictness. It is NOT part of the U1G live chain or its guards; kept
# only as commission history of the retrodiction analysis (provenance
# entanglement, ledger entry 12). Do not run as part of the gate.
#!/usr/bin/env python3
"""U1E guard: strictness bracket + retrodiction check.

Verifies, from the promoted exact q* bracket:
  (1) q* < 8604/10000 < 1  (strictness consumed by proof (3.3));
  (2) 1/kappa_eff = 2/(-log q*) evaluated on the bracket CONTAINS the
      historically retracted scout coefficient 13.2991468418
      (proof (3.6) — evidence note, not a numerical claim);
  (3) the bracket endpoints reproduce to 25 significant digits at two
      working precisions (60 and 120 dps), guarding against precision
      artifacts.
log is monotone, so directed endpoint assignment is exact.
"""

from mpmath import mp, mpf, log, nstr

Q_LO = "0.860375661183927"
Q_HI = "0.860376162879071"
SCOUT = "13.2991468418"


def bracket(dps: int):
    mp.dps = dps
    qlo, qhi = mpf(Q_LO), mpf(Q_HI)
    assert qhi < mpf(8604) / mpf(10000) < 1, "strictness (3.3) fails"
    assert 0 < qlo < qhi
    inv_lo = 2 / (-log(qlo))   # smaller q -> larger -log -> smaller 2/(-log)? no:
    inv_hi = 2 / (-log(qhi))
    # -log is decreasing in q, so -log(qlo) > -log(qhi) > 0, hence
    # 2/(-log(qlo)) < 2/(-log(qhi)): lo end from qlo, hi end from qhi.
    lo, hi = inv_lo, inv_hi
    assert lo < hi
    return lo, hi


def main() -> None:
    lo60, hi60 = bracket(60)
    lo120, hi120 = bracket(120)
    assert nstr(lo60, 25) == nstr(lo120, 25), "precision artifact (lo)"
    assert nstr(hi60, 25) == nstr(hi120, 25), "precision artifact (hi)"
    mp.dps = 120
    scout = mpf(SCOUT)
    # The sharper retrodiction (discovered when the naive "contains"
    # predicate failed by 9e-11): the scout IS the bracket's
    # upper-endpoint evaluation, rounded to its 10 stated decimals.
    diff = abs(scout - hi120)
    assert diff < mpf("5e-11"), (
        f"retrodiction FAILS: |scout - 2/(-log q_hi)| = {nstr(diff, 6)}"
        f" exceeds the 10-decimal rounding tolerance 5e-11")
    # And containment within rounding tolerance of the interval.
    assert lo120 - mpf("5e-11") <= scout <= hi120 + mpf("5e-11")
    print("PASS U1E strictness + retrodiction guard")
    print(f"  q* bracket ({Q_LO}, {Q_HI}); q* < 8604/10000 < 1")
    print(f"  1/kappa_eff in [{nstr(lo120, 15)}, {nstr(hi120, 15)}]")
    print(f"  retracted scout {SCOUT} = upper-endpoint evaluation "
          f"rounded to 10 decimals (|diff| = {nstr(diff, 4)})")


if __name__ == "__main__":
    main()
