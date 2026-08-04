#!/usr/bin/env python3
"""Exact-rational guard for one-grid four-coordinate addressing."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def cell(x: Q, shift: Q, width: Q) -> int:
    return (x - shift) // width


def main() -> None:
    rng = random.Random(1265)
    lattice = 101
    shifts = [Q(k, lattice) for k in range(lattice)]
    width = Q(1)
    fixtures = 2_000
    minimum_average_slack = None
    minimum_selected_slack = None
    prefix_checks = 0

    for _ in range(fixtures):
        rows = []
        for _j in range(rng.randint(1, 30)):
            rows.append(
                (
                    Q(rng.randint(-5 * lattice, 5 * lattice), lattice),
                    Q(rng.randint(-5 * lattice, 5 * lattice), lattice),
                    Q(rng.randint(-5 * lattice, 5 * lattice), lattice),
                    Q(rng.randint(-5 * lattice, 5 * lattice), lattice),
                    Q(rng.randint(1, 50), 37),
                )
            )

        losses = []
        for shift in shifts:
            loss = Q(0)
            for y, u, a, b, mass in rows:
                if cell(y, shift, width) != cell(u, shift, width) or cell(
                    a, shift, width
                ) != cell(b, shift, width):
                    loss += mass
            losses.append(loss)

        average = sum(losses, Q(0)) / lattice
        first_moment = sum(
            mass * (abs(y - u) + abs(a - b)) / width
            for y, u, a, b, mass in rows
        )
        average_slack = first_moment - average
        selected_slack = average - min(losses)
        assert average_slack >= 0
        assert selected_slack >= 0
        if minimum_average_slack is None or average_slack < minimum_average_slack:
            minimum_average_slack = average_slack
        if minimum_selected_slack is None or selected_slack < minimum_selected_slack:
            minimum_selected_slack = selected_slack

        best = min(range(lattice), key=lambda k: losses[k])
        shift = shifts[best]
        good = [
            row
            for row in rows
            if cell(row[0], shift, width) == cell(row[1], shift, width)
            and cell(row[2], shift, width) == cell(row[3], shift, width)
        ]
        if good:
            cell_ids = [
                cell(value, shift, width)
                for row in good
                for value in row[:4]
            ]
            for cut in range(min(cell_ids) - 1, max(cell_ids) + 2):
                for y, u, a, b, _mass in good:
                    assert (cell(y, shift, width) <= cut) == (
                        cell(u, shift, width) <= cut
                    )
                    assert (cell(a, shift, width) <= cut) == (
                        cell(b, shift, width) <= cut
                    )
                    prefix_checks += 2

    m0 = Q(7, 8000)
    shared_width = Q(25, 97006) * m0
    source_width = Q(25, 41769) * m0
    assert shared_width < source_width

    gates = {
        "one_shift_average": minimum_average_slack is not None and minimum_average_slack >= 0,
        "deterministic_shift": minimum_selected_slack is not None and minimum_selected_slack >= 0,
        "common_prefix_identities": prefix_checks > 1_000,
        "shared_width_refines_source_width": shared_width < source_width,
    }
    report = {
        "status": "exact-rational one-grid four-coordinate guard",
        "fixtures": fixtures,
        "shift_lattice_size": lattice,
        "prefix_identity_checks": prefix_checks,
        "minimum_average_slack": str(minimum_average_slack),
        "minimum_selected_slack": str(minimum_selected_slack),
        "shared_width_for_safe_m0": str(shared_width),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "One numerical grid supplies both original and response prefix "
            "identities. Final operator-error integration remains open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "one-grid-four-coordinate-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
