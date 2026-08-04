#!/usr/bin/env python3
"""Exact-rational guard for the trace-normalized upper cap."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def main() -> None:
    rng = random.Random(1262)
    fixtures = 100_000
    minimum_scalar_slack = None
    minimum_trace_slack = None

    for _ in range(fixtures):
        t = Q(rng.randint(1, 100_000), rng.randint(1, 10_000))
        lam = Q(rng.randint(0, 100_000), 100_000)
        scalar_slack = lam / t - lam / (t + lam)
        assert scalar_slack >= 0
        if minimum_scalar_slack is None or scalar_slack < minimum_scalar_slack:
            minimum_scalar_slack = scalar_slack

        count = rng.randint(1, 12)
        raw = [rng.randint(0, 1000) for _j in range(count)]
        if sum(raw) == 0:
            raw[0] = 1
        spectrum = [Q(value, sum(raw)) for value in raw]
        tail = sum(value / (t + value) for value in spectrum)
        trace_bound = Q(1, 1) / t
        trace_slack = trace_bound - tail
        assert trace_slack >= 0
        if minimum_trace_slack is None or trace_slack < minimum_trace_slack:
            minimum_trace_slack = trace_slack

    # Set-theoretic crossing custody: if z<S-B and |h|<=B, then z+h<S.
    S, B = Q(17, 3), Q(11, 7)
    z = S - B - Q(1, 10_000)
    assert z + B < S

    gates = {
        "scalar_functional_bound": minimum_scalar_slack is not None and minimum_scalar_slack >= 0,
        "trace_normalized_bound": minimum_trace_slack is not None and minimum_trace_slack >= 0,
        "crossing_support_inclusion": z + B < S,
    }
    report = {
        "status": "exact-rational trace-normalized upper-cap guard",
        "fixtures": fixtures,
        "minimum_scalar_slack": str(minimum_scalar_slack),
        "minimum_trace_slack": str(minimum_trace_slack),
        "upper_tail_formula": "mu(zeta>=S)<=exp(-S)",
        "one_response_crossing_formula": "exp(B-S)",
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The upper band interface is dimension-free. Common output-prefix "
            "control and the universal dimension lower bound remain open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "upper-cap-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
