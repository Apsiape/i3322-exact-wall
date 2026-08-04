#!/usr/bin/env python3
"""Generate the rational knot witness; this file carries no proof authority."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
NODES = 6401
Q_SOURCE = 0.250875384513976536
TOLERANCE = 1e-13
MAX_ITERATIONS = 5000
QUANTUM = Decimal("0.000000000000000001")


def ordered_lower_envelope(grid: np.ndarray, values: np.ndarray) -> np.ndarray:
    slopes = 0.5 - grid
    intercepts = (
        Q_SOURCE
        + 1.0
        - grid / 2.0
        - (1.0 - grid * grid) / (4.0 * values)
    )
    hull: list[int] = []
    starts: list[float] = []
    for index in range(len(grid)):
        start = -np.inf
        while hull:
            previous = hull[-1]
            start = float(
                (intercepts[index] - intercepts[previous])
                / (slopes[previous] - slopes[index])
            )
            if start > starts[-1]:
                break
            hull.pop()
            starts.pop()
        if not hull:
            start = -np.inf
        hull.append(index)
        starts.append(start)
    hull_array = np.asarray(hull, dtype=int)
    starts_array = np.asarray(starts, dtype=float)
    owners = hull_array[np.searchsorted(starts_array, grid, side="right") - 1]
    return np.minimum(
        Q_SOURCE + (1.0 - grid) / 2.0,
        slopes[owners] * grid + intercepts[owners],
    )


def main() -> None:
    grid = np.linspace(-1.0, 1.0, NODES)
    values = Q_SOURCE + (1.0 - grid) / 2.0
    for iteration in range(1, MAX_ITERATIONS + 1):
        updated = ordered_lower_envelope(grid, values)
        delta = float(np.max(np.abs(updated - values)))
        values = updated
        if delta < TOLERANCE:
            break
    decimals = [
        format(
            Decimal(str(float(value))).quantize(
                QUANTUM, rounding=ROUND_HALF_EVEN
            ),
            "f",
        )
        for value in values
    ]
    digest = hashlib.sha256("\n".join(decimals).encode("ascii")).hexdigest()
    report = {
        "status": "candidate witness only; exact verifier owns the theorem",
        "nodes": NODES,
        "source_q_float": Q_SOURCE,
        "tolerance": TOLERANCE,
        "maximum_iterations": MAX_ITERATIONS,
        "iterations": iteration,
        "final_delta": delta,
        "digits_after_decimal": 18,
        "sha256_newline_joined_knots": digest,
        "knots_decimal": decimals,
        "claim_boundary": (
            "Floating-point iteration chooses an explicit rational witness. "
            "It proves nothing until exact_rational_bellman_subsolution.py passes."
        ),
    }
    output = HERE / "bellman-subsolution-candidate.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "knots_decimal"}, indent=2))


if __name__ == "__main__":
    main()
