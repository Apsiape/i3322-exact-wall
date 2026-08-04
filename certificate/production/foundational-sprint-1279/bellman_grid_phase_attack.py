#!/usr/bin/env python3
"""Grid-phase and deep-refinement attack on the negative Bellman bottleneck."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize_scalar


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent / "foundational-sprint-1278" / "bellman_bottleneck_classifier.py"
)
Q_STAR = 0.250875384513976536
PHASE_NODES = tuple(range(12797, 12806))
DEEP_NODES = (25601, 51201)


def load_source():
    spec = importlib.util.spec_from_file_location("s1279_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def affine_hull(grid: np.ndarray, f: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    slopes = 0.5 - grid
    intercepts = Q_STAR + 1.0 - grid / 2.0 - (1.0 - grid * grid) / (4.0 * f)
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
    return np.asarray(hull, dtype=int), np.asarray(starts, dtype=float)


def inspect(source, nodes: int) -> dict:
    row = source.reconstruct_hull(nodes)
    grid = row["grid"]
    f = row["F_values"]
    F = PchipInterpolator(grid, f)
    hull, starts = affine_hull(grid, f)

    def owner_at(x: float) -> int:
        position = int(np.searchsorted(starts, x, side="right") - 1)
        return int(hull[position])

    def predecessor_with_owner(x: float, owner: int) -> float:
        lo = float(grid[max(0, owner - 2)])
        hi = float(grid[min(len(grid) - 1, owner + 2)])
        return float(
            minimize_scalar(
                lambda z: (
                    Q_STAR
                    + 1.0
                    - z / 2.0
                    - (z - 0.5) * x
                    - (1.0 - z * z) / (4.0 * float(F(z)))
                ),
                bounds=(lo, hi),
                method="bounded",
                options={"xatol": 2e-14, "maxiter": 100},
            ).x
        )

    def predecessor(x: float) -> float:
        return predecessor_with_owner(x, owner_at(x))

    sample = np.linspace(-0.9, 0.0, 3601)
    positions = np.searchsorted(starts, sample, side="right") - 1
    owners = hull[positions]
    predecessors = np.asarray(
        [
            predecessor_with_owner(float(x), int(owner))
            for x, owner in zip(sample, owners)
        ]
    )
    gaps = predecessors - sample
    minimum_index = int(np.argmin(gaps))
    lo = float(sample[max(0, minimum_index - 2)])
    hi = float(sample[min(len(sample) - 1, minimum_index + 2)])
    optimum = minimize_scalar(
        lambda x: predecessor(float(x)) - float(x),
        bounds=(lo, hi),
        method="bounded",
        options={"xatol": 2e-14, "maxiter": 100},
    )
    x = float(optimum.x)
    p = predecessor(x)
    gap = p - x
    coefficient = (1.0 - p * p) / (4.0 * float(F(p)) ** 2)
    return {
        "nodes": nodes,
        "iterations": row["iterations"],
        "final_delta": row["final_delta"],
        "hull_lines": len(hull),
        "minimum_gap": float(gap),
        "minimum_gap_coordinate": x,
        "predecessor_at_minimum": p,
        "bottleneck_multiplier": float(coefficient),
    }


def main() -> None:
    source = load_source()
    phase = [inspect(source, nodes) for nodes in PHASE_NODES]
    deep = [inspect(source, nodes) for nodes in DEEP_NODES]
    all_rows = phase + deep
    phase_robust = (
        max(row["minimum_gap"] for row in phase) < 2.5e-4
        and max(row["minimum_gap"] for row in deep) < 1.5e-4
    )
    strict_reopened = min(row["minimum_gap"] for row in all_rows) > 3e-4
    classification = (
        "phase-robust parabolic signal"
        if phase_robust
        else "strict transit reopened"
        if strict_reopened
        else "unresolved"
    )
    gates = {
        "all_gaps_positive": all(row["minimum_gap"] > 0 for row in all_rows),
        "all_coordinates_near_registered_bottleneck": all(
            abs(row["minimum_gap_coordinate"] + 0.8782) < 0.001
            for row in all_rows
        ),
        "all_multipliers_above_one_point_one_five": all(
            row["bottleneck_multiplier"] > 1.15 for row in all_rows
        ),
    }
    report = {
        "status": "grid-phase and deep-refinement Bellman bottleneck attack",
        "phase_ensemble": phase,
        "deep_refinement": deep,
        "phase_gap_range": [
            min(row["minimum_gap"] for row in phase),
            max(row["minimum_gap"] for row in phase),
        ],
        "deep_gap_range": [
            min(row["minimum_gap"] for row in deep),
            max(row["minimum_gap"] for row in deep),
        ],
        "classification": classification,
        "gates": gates,
        "all_instrument_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This is a floating-point grid-phase and refinement attack. It does "
            "not certify a zero transit gap or a continuum parabolic contact."
        ),
    }
    (HERE / "bellman-grid-phase-attack.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
