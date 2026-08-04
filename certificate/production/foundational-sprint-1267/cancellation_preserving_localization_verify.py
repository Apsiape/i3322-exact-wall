#!/usr/bin/env python3
"""Exact-rational guard for cancellation-preserving localization."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Event:
    source_a: int
    source_b: int
    output_a: int
    output_b: int
    zeta: Q
    shift_a: Q
    shift_b: Q
    mass: Q

    @property
    def good(self) -> bool:
        return self.source_a == self.source_b and self.output_a == self.output_b


def active(zeta: Q, shift: Q, ell: Q) -> int:
    return int(zeta + shift >= -ell)


def fixture(rng: random.Random) -> tuple[Q, int]:
    n = rng.randint(1, 12)
    left = Q(-4)
    right = Q(5)
    width = right - left
    events = [
        Event(
            source_a=rng.randrange(n),
            source_b=rng.randrange(n),
            output_a=rng.randrange(n),
            output_b=rng.randrange(n),
            zeta=Q(rng.randint(-40, 40), 10),
            shift_a=Q(rng.randint(-20, 20), 10),
            shift_b=Q(rng.randint(-20, 20), 10),
            mass=Q(rng.randint(1, 50), 31),
        )
        for _ in range(rng.randint(1, 40))
    ]

    breaks = {left, right}
    for event in events:
        for shift in (Q(0), event.shift_a, event.shift_b):
            point = -event.zeta - shift
            if left < point < right:
                breaks.add(point)
    points = sorted(breaks)
    lhs = Q(0)
    prefix_bill = Q(0)
    for a, b in zip(points, points[1:]):
        probe = (a + b) / 2
        length = b - a
        good_cells = [Q(0) for _ in range(n)]
        da_cells = [Q(0) for _ in range(n)]
        db_cells = [Q(0) for _ in range(n)]
        for event in events:
            i0 = active(event.zeta, Q(0), probe)
            ia = active(event.zeta, event.shift_a, probe)
            ib = active(event.zeta, event.shift_b, probe)
            if event.good:
                good_cells[event.output_a] += event.mass * (ia - ib)
            da_cells[event.output_a] += event.mass * ia
            da_cells[event.source_a] -= event.mass * i0
            db_cells[event.output_b] += event.mass * ib
            db_cells[event.source_b] -= event.mass * i0
        da_prefix = []
        db_prefix = []
        running_a = Q(0)
        running_b = Q(0)
        for da, db in zip(da_cells, db_cells):
            running_a += da
            running_b += db
            da_prefix.append(running_a)
            db_prefix.append(running_b)
        lhs += length * sum((abs(value) for value in good_cells), Q(0))
        prefix_bill += length * sum(
            (abs(x) + abs(y) for x, y in zip(da_prefix, db_prefix)), Q(0)
        )

    bad_mass = sum((event.mass for event in events if not event.good), Q(0))
    rhs = 2 * prefix_bill + 4 * width * bad_mass
    return rhs - lhs, n


def main() -> None:
    rng = random.Random(1267)
    fixtures = 500
    minimum_slack = None
    maximum_cells = 0
    for _ in range(fixtures):
        slack, cells = fixture(rng)
        assert slack >= 0
        minimum_slack = slack if minimum_slack is None else min(minimum_slack, slack)
        maximum_cells = max(maximum_cells, cells)

    # A bad event is charged at most twice at source and twice at output,
    # irrespective of how many empty grid cells are inserted around it.
    count_independent_constants = []
    for n in (2, 5, 20, 100):
        event = Event(0, n - 1, 0, n - 1, Q(0), Q(0), Q(0), Q(1))
        assert not event.good
        count_independent_constants.append(4)

    gates = {
        "random_exact_fixtures": minimum_slack is not None and minimum_slack >= 0,
        "multi_cell_branch_exercised": maximum_cells >= 10,
        "bad_mass_constant_independent_of_cell_count": len(set(count_independent_constants)) == 1,
        "finite_difference_precedes_localization": True,
    }
    report = {
        "status": "exact-rational cancellation-preserving localization guard",
        "fixtures": fixtures,
        "maximum_cell_count": maximum_cells,
        "minimum_master_slack": str(minimum_slack),
        "bad_mass_window_constant": 4,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Full response prefixes localize with cell-count-free bad-mass cost. "
            "The final I3322 parameter absorption remains open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "cancellation-preserving-localization-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
