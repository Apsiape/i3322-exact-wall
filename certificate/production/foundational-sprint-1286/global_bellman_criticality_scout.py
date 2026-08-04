#!/usr/bin/env python3
"""Resolution/offset scout for global Bellman positivity criticality."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
Q_CENTER = 0.250875384513976536
RESOLUTIONS = (801, 1601, 3201, 6401)
OFFSETS = (-1e-4, -1e-5, -1e-6, 0.0, 1e-6, 1e-5, 1e-4)
TOLERANCE = 1e-11
MAX_ITERATIONS = 5000


def ordered_lower_envelope(
    grid: np.ndarray,
    values: np.ndarray,
    q_value: float,
) -> np.ndarray:
    slopes = 0.5 - grid
    intercepts = (
        q_value
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
    return slopes[owners] * grid + intercepts[owners]


def run(node_count: int, offset: float) -> dict:
    q_value = Q_CENTER + offset
    grid = np.linspace(-1.0, 1.0, node_count)
    boundary = q_value + (1.0 - grid) / 2.0
    values = boundary.copy()
    delta = float("inf")
    classification = "unresolved"
    for iteration in range(1, MAX_ITERATIONS + 1):
        envelope = ordered_lower_envelope(grid, values, q_value)
        updated = np.minimum(boundary, envelope)
        delta = float(np.max(np.abs(updated - values)))
        minimum = float(np.min(updated))
        values = updated
        if minimum <= 0.0:
            classification = "collapsed"
            break
        if delta < TOLERANCE:
            classification = "fixed"
            break
    return {
        "nodes": node_count,
        "offset": offset,
        "q": q_value,
        "classification": classification,
        "iterations": iteration,
        "minimum_F": float(np.min(values)),
        "maximum_F": float(np.max(values)),
        "final_delta": delta,
    }


def main() -> None:
    rows = [run(nodes, offset) for nodes in RESOLUTIONS for offset in OFFSETS]

    def selected(predicate):
        return [row for row in rows if predicate(row)]

    negative = selected(lambda row: row["offset"] < 0)
    zero = selected(lambda row: row["offset"] == 0)
    positive = selected(lambda row: row["offset"] > 0)
    zero_by_resolution = {row["nodes"]: row for row in zero}
    gates = {
        "all_negative_offsets_collapse": all(
            row["classification"] == "collapsed" for row in negative
        ),
        "all_zero_offsets_converge_positive": all(
            row["classification"] == "fixed" and row["minimum_F"] > 0
            for row in zero
        ),
        "all_positive_offsets_converge_positive": all(
            row["classification"] == "fixed" and row["minimum_F"] > 0
            for row in positive
        ),
        "zero_offset_minimum_above_point_zero_four": min(
            row["minimum_F"] for row in zero
        ) > 0.04,
        "fine_zero_offset_minima_agree_below_five_e_minus_five": abs(
            zero_by_resolution[3201]["minimum_F"]
            - zero_by_resolution[6401]["minimum_F"]
        ) < 5e-5,
        "no_unresolved_runs": all(
            row["classification"] != "unresolved" for row in rows
        ),
    }
    report = {
        "status": "global Bellman positivity criticality scout",
        "q_center": Q_CENTER,
        "resolutions": list(RESOLUTIONS),
        "offsets": list(OFFSETS),
        "tolerance": TOLERANCE,
        "maximum_iterations": MAX_ITERATIONS,
        "runs": rows,
        "zero_offset_fine_minimum_disagreement": abs(
            zero_by_resolution[3201]["minimum_F"]
            - zero_by_resolution[6401]["minimum_F"]
        ),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "classification": (
            "resolution-robust numerical critical point"
            if all(gates.values())
            else "registered criticality pattern failed"
        ),
        "claim_boundary": (
            "This is a floating-point ordered-hull iteration scout. It does "
            "not certify exact Bellman criticality or restore the I3322 theorem."
        ),
    }
    output = HERE / "global-bellman-criticality-scout.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
