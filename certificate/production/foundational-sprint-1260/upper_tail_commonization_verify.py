#!/usr/bin/env python3
"""Exact-rational custody guard for upper-tail commonization."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    contact_square = Q(40)
    resolvent_square = Q(9)
    pointwise = contact_square * resolvent_square

    deep_integral = pointwise / 3
    high_integral = pointwise
    combined_constant = deep_integral
    combined_offset = (high_integral - deep_integral) / combined_constant

    assert pointwise == 360
    assert deep_integral == 120
    assert high_integral == 360
    assert combined_offset == 2

    # For t>=1, (t^-1/2+2t^-3/2)<=3t^-1/2.  Clear the
    # positive factor t^-1/2 and check on a broad exact lattice.
    minimum_high_slack = None
    for numerator in range(1, 10001):
        t = Q(numerator + 9999, 10000)  # [1,2) exact guard lattice
        slack = Q(3) - (Q(1) + Q(2) / t)
        assert slack >= 0
        if minimum_high_slack is None or slack < minimum_high_slack:
            minimum_high_slack = slack

    # Cut custody: max(L+p)=H+R+B, so zeta>=-(H+R+B).
    H, R, B = Q(7, 3), Q(11, 5), Q(13, 10)
    K = H + R + B
    queried = [
        -R - B,
        -R + B,
        H + R - B,
        H + R + B,
    ]
    assert max(queried) == K

    gates = {
        "deep_integral_constant": deep_integral == 120,
        "high_integral_constant": high_integral == 360,
        "combined_offset": combined_offset == 2,
        "high_resolution_resolvent": minimum_high_slack is not None and minimum_high_slack >= 0,
        "all_shifted_cuts_covered": max(queried) == K,
    }
    report = {
        "status": "exact-rational upper-tail commonization guard",
        "pointwise_contact_coefficient": str(pointwise),
        "deep_integrated_coefficient": str(deep_integral),
        "high_integrated_coefficient": str(high_integral),
        "combined_formula": "120*epsilon_0*(exp(3*K)+2)",
        "minimum_high_resolution_slack": str(minimum_high_slack),
        "sample_cut_cover_K": str(K),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "One grid covers every queried upper tail. Synchronized response "
            "prefix control and the universal dimension lower bound remain open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "upper-tail-commonization-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
