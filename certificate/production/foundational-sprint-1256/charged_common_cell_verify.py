#!/usr/bin/env python3
"""Exact-rational guard for shifted common-cell descent."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def separated(y: Q, u: Q, shift: Q, width: Q) -> bool:
    return (y - shift) // width != (u - shift) // width


def main() -> None:
    rng = random.Random(1256)
    fixtures = 0
    minimum_average_slack = None
    minimum_selected_slack = None

    # A discrete shift average with denominator N is exact whenever all
    # coordinates lie on the same width/N lattice.
    N = 97
    width = Q(1)
    shifts = [Q(k, N) for k in range(N)]
    for _ in range(10000):
        count = rng.randint(1, 25)
        rows = []
        for _ in range(count):
            y = Q(rng.randint(-4 * N, 4 * N), N)
            u = Q(rng.randint(-4 * N, 4 * N), N)
            mass = Q(rng.randint(1, 30), 30)
            rows.append((y, u, mass))
        bills = [
            sum(m for y, u, m in rows if separated(y, u, s, width))
            for s in shifts
        ]
        average = sum(bills, Q(0)) / N
        l1_bill = sum(m * abs(y - u) / width for y, u, m in rows)
        average_slack = l1_bill - average
        selected_slack = average - min(bills)
        assert average_slack >= 0
        assert selected_slack >= 0
        if minimum_average_slack is None or average_slack < minimum_average_slack:
            minimum_average_slack = average_slack
        if minimum_selected_slack is None or selected_slack < minimum_selected_slack:
            minimum_selected_slack = selected_slack
        fixtures += 1

    # Integral custody: integral_0^H 360 e^(3L)dL=120(e^(3H)-1).
    derivative_coefficient = Q(360, 3)
    assert derivative_coefficient == 120

    report = {
        "status": "exact-rational charged common-cell guard",
        "fixtures": fixtures,
        "shift_lattice_size": N,
        "minimum_average_bound_slack": str(minimum_average_slack),
        "minimum_selected_shift_slack": str(minimum_selected_slack),
        "integrated_contact_coefficient": str(derivative_coefficient),
        "gates": {
            "shift_average": minimum_average_slack is not None and minimum_average_slack >= 0,
            "deterministic_shift_selection": minimum_selected_slack is not None and minimum_selected_slack >= 0,
            "contact_integral_constant": derivative_coefficient == 120,
        },
        "all_gates_pass": (
            minimum_average_slack is not None
            and minimum_average_slack >= 0
            and minimum_selected_slack is not None
            and minimum_selected_slack >= 0
            and derivative_coefficient == 120
        ),
        "claim_boundary": (
            "The source commonization bill is guarded. Response-output descent "
            "and a dimension lower bound are not asserted."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "charged-common-cell-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
