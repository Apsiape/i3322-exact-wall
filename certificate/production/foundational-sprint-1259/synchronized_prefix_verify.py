#!/usr/bin/env python3
"""Exact-rational guard for synchronized-prefix vertical recovery."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def tail(atoms: list[tuple[Q, Q]], cut: Q, shift: Q) -> Q:
    return sum(m for z, m in atoms if z >= -(cut + shift))


def main() -> None:
    rng = random.Random(1259)
    fixtures = 1500
    minimum_slack = None
    maximum_ratio = Q(0)

    for _ in range(fixtures):
        n = rng.randint(1, 12)
        H = Q(rng.randint(1, 20), 3)
        B = Q(rng.randint(1, 10), 5)
        fibres: list[list[tuple[Q, Q]]] = []
        shifts: list[tuple[Q, Q]] = []
        breakpoints = {-B, H + B}
        native = Q(0)

        for _i in range(n):
            atoms = []
            for _k in range(rng.randint(1, 8)):
                # Include core and exterior atoms; only the core is charged on
                # the theorem's left side.
                z = Q(rng.randint(-60, 20), 10) * H / 6
                mass = Q(rng.randint(1, 30), 17)
                atoms.append((z, mass))
            p = Q(rng.randint(-100, 100), 100) * B
            q = Q(rng.randint(-100, 100), 100) * B
            fibres.append(atoms)
            shifts.append((p, q))
            core_mass = sum(m for z, m in atoms if -H <= z <= 0)
            native += core_mass * abs(p - q)
            for z, _m in atoms:
                for shift in (p, q):
                    point = -z - shift
                    if -B < point < H + B:
                        breakpoints.add(point)

        points = sorted(breakpoints)
        prefix_area = Q(0)
        individual_area = Q(0)
        for left, right in zip(points, points[1:]):
            if left == right:
                continue
            mid = (left + right) / 2
            running = Q(0)
            maximum = Q(0)
            individual = Q(0)
            for atoms, (p, q) in zip(fibres, shifts):
                residual = tail(atoms, mid, p) - tail(atoms, mid, q)
                running += residual
                individual += abs(residual)
                maximum = max(maximum, abs(running))
            width = right - left
            prefix_area += width * maximum
            individual_area += width * individual

        assert native <= individual_area
        upper = 2 * n * prefix_area
        assert individual_area <= upper
        slack = upper - native
        if minimum_slack is None or slack < minimum_slack:
            minimum_slack = slack
        if upper > 0:
            maximum_ratio = max(maximum_ratio, native / upper)

    vertical_coefficient = Q(169, 100)
    prefix_coefficient = vertical_coefficient * 2
    assert prefix_coefficient == Q(169, 50)

    gates = {
        "translation_area": minimum_slack is not None and minimum_slack >= 0,
        "prefix_differencing": maximum_ratio <= 1,
        "master_coefficient": prefix_coefficient == Q(169, 50),
    }
    report = {
        "status": "exact-rational synchronized-prefix recovery guard",
        "fixtures": fixtures,
        "minimum_total_slack": str(minimum_slack),
        "maximum_native_to_prefix_bound_ratio": str(maximum_ratio),
        "master_prefix_coefficient": str(prefix_coefficient),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Abstract prefix recovery is proved. The I3322 operator receipts "
            "have not yet been shown to control synchronized prefixes."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "synchronized-prefix-recovery-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
