#!/usr/bin/env python3
"""Generate the preregistered endpoint-clustered Bellman witness candidate."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN
import hashlib
import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
NODES = 25_601
HALF = (NODES - 1) // 2
Q_SOURCE = 0.250875384513976536
TOLERANCE = 1e-13
MAX_ITERATIONS = 5000
QUANTUM = Decimal("0.000000000000000001")


def fixed_grid_decimals() -> list[str]:
    left: list[Decimal] = []
    for index in range(HALF + 1):
        t = index / (NODES - 1)
        raw = ((2.0 * t - 1.0) - math.cos(math.pi * t)) / 2.0
        value = Decimal(str(raw)).quantize(QUANTUM, rounding=ROUND_HALF_EVEN)
        left.append(value)
    left[0] = Decimal("-1.000000000000000000")
    left[-1] = Decimal("0.000000000000000000")
    right = [-value for value in reversed(left[:-1])]
    return [format(value, "f") for value in left + right]


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
    grid_decimal = fixed_grid_decimals()
    grid = np.asarray([float(value) for value in grid_decimal])
    if not np.all(np.diff(grid) > 0):
        raise RuntimeError("quantized endpoint-clustered grid is not strict")
    values = Q_SOURCE + (1.0 - grid) / 2.0
    for iteration in range(1, MAX_ITERATIONS + 1):
        updated = ordered_lower_envelope(grid, values)
        delta = float(np.max(np.abs(updated - values)))
        values = updated
        if delta < TOLERANCE:
            break
    knot_decimal = [
        format(
            Decimal(str(float(value))).quantize(QUANTUM, rounding=ROUND_HALF_EVEN),
            "f",
        )
        for value in values
    ]
    digest = hashlib.sha256(
        ("\n".join(grid_decimal) + "\n--\n" + "\n".join(knot_decimal)).encode(
            "ascii"
        )
    ).hexdigest()
    report = {
        "status": "endpoint-clustered candidate only; exact verifier owns theorem",
        "nodes": NODES,
        "grid_formula": "x(t)=((2t-1)-cos(pi*t))/2, then exact sign reflection",
        "source_q_float": Q_SOURCE,
        "tolerance": TOLERANCE,
        "maximum_iterations": MAX_ITERATIONS,
        "iterations": iteration,
        "final_delta": delta,
        "digits_after_decimal": 18,
        "minimum_floating_knot": float(np.min(values)),
        "minimum_grid_spacing": float(np.min(np.diff(grid))),
        "maximum_grid_spacing": float(np.max(np.diff(grid))),
        "sha256_grid_separator_knots": digest,
        "grid_decimal": grid_decimal,
        "knots_decimal": knot_decimal,
        "claim_boundary": (
            "Floating search chooses a rational witness and proves nothing until "
            "the exact nonuniform-grid verifier passes."
        ),
    }
    output = HERE / "endpoint-clustered-candidate.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                key: value
                for key, value in report.items()
                if key not in {"grid_decimal", "knots_decimal"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
