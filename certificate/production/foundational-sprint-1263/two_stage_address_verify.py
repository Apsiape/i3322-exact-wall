#!/usr/bin/env python3
"""Exact-rational guard for two-stage shifted common addresses."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def separated(x: Q, z: Q, shift: Q, width: Q) -> bool:
    return (x - shift) // width != (z - shift) // width


def main() -> None:
    rng = random.Random(1263)
    lattice = 53
    shifts = [Q(k, lattice) for k in range(lattice)]
    source_width = Q(1)
    output_width = Q(1)
    fixtures = 5000
    minimum_total_slack = None

    for _ in range(fixtures):
        rows = []
        for _j in range(rng.randint(1, 30)):
            rows.append(
                (
                    Q(rng.randint(-4 * lattice, 4 * lattice), lattice),
                    Q(rng.randint(-4 * lattice, 4 * lattice), lattice),
                    Q(rng.randint(-4 * lattice, 4 * lattice), lattice),
                    Q(rng.randint(-4 * lattice, 4 * lattice), lattice),
                    Q(rng.randint(1, 50), 29),
                )
            )

        total = sum((row[4] for row in rows), Q(0))
        source_bill = sum(row[4] * abs(row[0] - row[1]) for row in rows)
        output_bill = sum(row[4] * abs(row[2] - row[3]) for row in rows)

        source_losses = [
            sum(
                row[4]
                for row in rows
                if separated(row[0], row[1], shift, source_width)
            )
            for shift in shifts
        ]
        source_shift = min(range(lattice), key=lambda k: source_losses[k])
        assert source_losses[source_shift] <= sum(source_losses, Q(0)) / lattice
        assert sum(source_losses, Q(0)) / lattice <= source_bill

        source_good = [
            row
            for row in rows
            if not separated(row[0], row[1], shifts[source_shift], source_width)
        ]
        output_losses = [
            sum(
                row[4]
                for row in source_good
                if separated(row[2], row[3], shift, output_width)
            )
            for shift in shifts
        ]
        output_shift = min(range(lattice), key=lambda k: output_losses[k])
        assert output_losses[output_shift] <= sum(output_losses, Q(0)) / lattice
        assert sum(output_losses, Q(0)) / lattice <= output_bill

        retained = total - source_losses[source_shift] - output_losses[output_shift]
        lower = total - source_bill - output_bill
        slack = retained - lower
        assert slack >= 0
        if minimum_total_slack is None or slack < minimum_total_slack:
            minimum_total_slack = slack

    gates = {
        "source_shift_selection": True,
        "output_shift_after_restriction": True,
        "additive_positive_measure_bill": minimum_total_slack is not None and minimum_total_slack >= 0,
    }
    report = {
        "status": "exact-rational two-stage common-address guard",
        "fixtures": fixtures,
        "shift_lattice_size": lattice,
        "minimum_additive_bill_slack": str(minimum_total_slack),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Common source and output addresses are purchased by explicit "
            "first-moment bills. The operator prefix assembly remains open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "two-stage-address-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
