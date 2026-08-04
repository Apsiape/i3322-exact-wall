#!/usr/bin/env python3
"""Memory-safe high-resolution classifier for the negative Bellman bottleneck."""

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
    HERE.parent
    / "foundational-sprint-1272"
    / "normalization_defect_geometry_scout.py"
)
Q_STAR = 0.250875384513976536


def load_source():
    spec = importlib.util.spec_from_file_location("s1278_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ordered_lower_envelope(
    grid: np.ndarray, f: np.ndarray, query: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
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

    hull_array = np.asarray(hull, dtype=int)
    starts_array = np.asarray(starts, dtype=float)
    positions = np.searchsorted(starts_array, query, side="right") - 1
    owners = hull_array[positions]
    values = slopes[owners] * query + intercepts[owners]
    return values, owners


def reconstruct_hull(node_count: int) -> dict:
    grid = np.linspace(-1.0, 1.0, node_count)
    boundary = Q_STAR + (1.0 - grid) / 2.0
    f = boundary.copy()
    owners = np.zeros(node_count, dtype=int)

    for iteration in range(1, 5001):
        envelope, owners = ordered_lower_envelope(grid, f, grid)
        updated = np.maximum(np.minimum(boundary, envelope), 1e-14)
        delta = float(np.max(np.abs(updated - f)))
        f = updated
        if delta < 1e-11:
            break

    return {
        "nodes": node_count,
        "grid": grid,
        "F_values": f,
        "owners": owners,
        "iterations": iteration,
        "final_delta": delta,
    }


def continuous_predecessor_factory(row: dict):
    grid = row["grid"]
    f = row["F_values"]
    F = PchipInterpolator(grid, f)

    def predecessor(x: float) -> float:
        line_values = (
            Q_STAR
            + 1.0
            - grid / 2.0
            - (grid - 0.5) * x
            - (1.0 - grid * grid) / (4.0 * f)
        )
        owner = int(np.argmin(line_values))
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

    return F, predecessor


def bottleneck(row: dict) -> dict:
    F, predecessor = continuous_predecessor_factory(row)
    sample = np.linspace(-0.9, 0.0, 3601)
    gaps = np.asarray([predecessor(float(x)) - x for x in sample])
    owner = int(np.argmin(gaps))
    lo = float(sample[max(0, owner - 2)])
    hi = float(sample[min(len(sample) - 1, owner + 2)])
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
        "nodes": row["nodes"],
        "iterations": row["iterations"],
        "final_delta": row["final_delta"],
        "minimum_gap": float(gap),
        "minimum_gap_coordinate": x,
        "predecessor_at_minimum": p,
        "bottleneck_multiplier": float(coefficient),
    }


def dense_agreement(source, hull: dict) -> dict:
    dense = source.reconstruct(3201)
    f_difference = float(np.max(np.abs(dense["F_values"] - hull["F_values"])))
    _, dense_owners = ordered_lower_envelope(
        dense["grid"], dense["F_values"], dense["grid"]
    )
    _, hull_owners = ordered_lower_envelope(
        hull["grid"], hull["F_values"], hull["grid"]
    )
    owner_disagreements = int(np.count_nonzero(dense_owners != hull_owners))
    return {
        "maximum_F_disagreement": f_difference,
        "discrete_owner_disagreements": owner_disagreements,
    }


def main() -> None:
    source = load_source()
    hulls = [reconstruct_hull(nodes) for nodes in (3201, 6401, 12801)]
    agreement = dense_agreement(source, hulls[0])
    rows = [bottleneck(row) for row in hulls]
    by_nodes = {row["nodes"]: row for row in rows}
    gap_6401 = by_nodes[6401]["minimum_gap"]
    gap_12801 = by_nodes[12801]["minimum_gap"]
    strict = gap_12801 > 3e-4 and abs(gap_12801 - gap_6401) < 1e-4
    parabolic = gap_12801 < 3e-4 and gap_12801 / gap_6401 < 0.8
    classification = (
        "strict-transit consistent"
        if strict
        else "parabolic-contact consistent"
        if parabolic
        else "unresolved"
    )
    gates = {
        "hull_reproduces_dense_fixed_point": (
            agreement["maximum_F_disagreement"] <= 2e-11
            and agreement["discrete_owner_disagreements"] <= 2
        ),
        "all_measured_transit_gaps_positive": all(
            row["minimum_gap"] > 0.0 for row in rows
        ),
        "all_bottleneck_multipliers_above_one_point_one": all(
            row["bottleneck_multiplier"] > 1.1 for row in rows
        ),
    }
    report = {
        "status": "memory-safe high-resolution Bellman bottleneck classifier",
        "dense_hull_agreement": agreement,
        "resolutions": rows,
        "gap_12801_over_gap_6401": gap_12801 / gap_6401,
        "classification": classification,
        "gates": gates,
        "all_instrument_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The hull equivalence is a floating-point implementation check. "
            "The bottleneck classification is numerical evidence only and is "
            "not a continuum Bellman theorem."
        ),
    }
    (HERE / "bellman-bottleneck-classifier.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
