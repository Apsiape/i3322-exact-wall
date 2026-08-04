#!/usr/bin/env python3
"""Exact-rational hostile guard for logarithmic cut averaging."""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def interval_intersection_length(a: Fraction, b: Fraction, h: Fraction) -> Fraction:
    lo = max(min(a, b), Fraction(0))
    hi = min(max(a, b), h)
    return max(Fraction(0), hi - lo)


def flux_at(events, shifts, cut: Fraction) -> Fraction:
    total = Fraction(0)
    for weight, zeta in events:
        for shift in shifts:
            before = zeta >= -cut
            after = zeta + shift >= -cut
            if before != after:
                total += weight
    return total


def main() -> None:
    rng = random.Random(1251)
    fixtures = 0
    minimum_average_slack = None
    minimum_selection_slack = None

    for _ in range(10000):
        count = rng.randrange(1, 25)
        response_count = rng.randrange(1, 5)
        events = [
            (
                Fraction(rng.randrange(1, 20), rng.randrange(1, 20)),
                Fraction(rng.randrange(-200, 201), rng.randrange(1, 20)),
            )
            for _ in range(count)
        ]
        shifts = [Fraction(rng.randrange(-40, 41), rng.randrange(1, 20)) for _ in range(response_count)]
        horizon = Fraction(rng.randrange(1, 100), rng.randrange(1, 10))
        mass = sum((weight for weight, _ in events), Fraction(0))
        shift_bill = sum((abs(shift) for shift in shifts), Fraction(0))

        # Exact integral of total flux over cut depth.
        integral = Fraction(0)
        breakpoints = {Fraction(0), horizon}
        for weight, zeta in events:
            for shift in shifts:
                left = -zeta
                right = -(zeta + shift)
                integral += weight * interval_intersection_length(left, right, horizon)
                breakpoints.add(max(Fraction(0), min(horizon, left)))
                breakpoints.add(max(Fraction(0), min(horizon, right)))

        average_bound = mass * shift_bill
        average_slack = average_bound - integral
        assert average_slack >= 0
        if minimum_average_slack is None or average_slack < minimum_average_slack:
            minimum_average_slack = average_slack

        # Flux is constant between crossing endpoints. Check all interval
        # midpoints and endpoints to exhibit a cut no worse than the average.
        ordered = sorted(breakpoints)
        candidates = set(ordered)
        candidates.update((x + y) / 2 for x, y in zip(ordered, ordered[1:]))
        best = min(flux_at(events, shifts, cut) for cut in candidates)
        selected_bound = average_bound / horizon
        selection_slack = selected_bound - best
        assert selection_slack >= 0
        if minimum_selection_slack is None or selection_slack < minimum_selection_slack:
            minimum_selection_slack = selection_slack
        fixtures += 1

    gates = {
        "exact_average_flux_bound": fixtures == 10000 and minimum_average_slack >= 0,
        "cut_selection_bound": minimum_selection_slack >= 0,
    }
    report = {
        "status": "log-resolution cut-flux guard",
        "exact_rational_fixtures": fixtures,
        "minimum_average_bound_slack": str(minimum_average_slack),
        "minimum_selected_cut_slack": str(minimum_selection_slack),
        "i3322_two_shift_bill": "4*log(13/2)",
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Full-measure vertical boundary flux is controlled by shifted-cut averaging. "
            "The grid-free order/contact closure inequality remains open."
        ),
    }
    (HERE / "log-cut-flux-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

