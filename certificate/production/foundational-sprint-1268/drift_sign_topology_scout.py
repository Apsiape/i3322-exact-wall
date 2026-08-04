#!/usr/bin/env python3
"""Two-resolution numerical scout for intrinsic Bellman drift chambers."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, minimize_scalar


HERE = Path(__file__).resolve().parent
Q_STAR = 0.250875384513976536


def reconstruct(node_count: int) -> dict:
    grid = np.linspace(-1.0, 1.0, node_count)
    boundary = Q_STAR + (1.0 - grid) / 2.0
    f = boundary.copy()
    x = grid[:, None]
    y = grid[None, :]
    for iteration in range(1, 5001):
        candidates = (
            Q_STAR
            + 1.0
            - x / 2.0
            - (x - 0.5) * y
            - (1.0 - x * x) / (4.0 * f[:, None])
        )
        updated = np.minimum(boundary, np.min(candidates, axis=0))
        updated = np.maximum(updated, 1e-14)
        delta = float(np.max(np.abs(updated - f)))
        f = updated
        if delta < 1e-11:
            break

    profile = PchipInterpolator(grid, f)

    def predecessor(u: float) -> float:
        values = (
            Q_STAR
            + 1.0
            - grid / 2.0
            - (grid - 0.5) * u
            - (1.0 - grid * grid) / (4.0 * f)
        )
        owner = int(np.argmin(values))
        lo = float(grid[max(0, owner - 2)])
        hi = float(grid[min(node_count - 1, owner + 2)])

        def objective(z: float) -> float:
            return (
                Q_STAR
                + 1.0
                - z / 2.0
                - (z - 0.5) * u
                - (1.0 - z * z) / (4.0 * float(profile(z)))
            )

        return float(
            minimize_scalar(
                objective,
                bounds=(lo, hi),
                method="bounded",
                options={"xatol": 2e-14, "maxiter": 100},
            ).x
        )

    def chi(u: float) -> float:
        p = predecessor(u)
        return float(
            np.log(float(profile(u)) / float(profile(-u)))
            - np.log(float(profile(-p)) / float(profile(p)))
        )

    sample = np.linspace(-0.9, 0.9, 7201)
    values = np.array([chi(float(u)) for u in sample])
    brackets = []
    for left, right, a, b in zip(sample, sample[1:], values, values[1:]):
        if a == 0.0 or a * b < 0.0:
            brackets.append((float(left), float(right)))
    roots = [float(brentq(chi, left, right)) for left, right in brackets]

    policy_sample = np.array([predecessor(float(u)) for u in sample])
    inverse = PchipInterpolator(policy_sample, sample)
    separations = []
    slopes = []
    for root in roots:
        p = predecessor(root)
        a_root = float(inverse(-p))
        separations.append(abs(a_root + root))
        h = 2e-5
        slopes.append(abs((chi(root + h) - chi(root - h)) / (2.0 * h)))

    return {
        "nodes": node_count,
        "iterations": iteration,
        "final_delta": delta,
        "minimum_F": float(np.min(f)),
        "predecessor_min_increment": float(np.min(np.diff(policy_sample))),
        "roots": roots,
        "horizontal_separations": separations,
        "root_slope_magnitudes": slopes,
    }


def main() -> None:
    coarse = reconstruct(1601)
    fine = reconstruct(3201)
    root_agreement = max(
        abs(a - b) for a, b in zip(coarse["roots"], fine["roots"])
    )
    target_boxes = [(-0.867, -0.865), (-0.378, -0.376), (0.799, 0.802)]
    gates = {
        "three_roots_at_both_resolutions": len(coarse["roots"]) == len(fine["roots"]) == 3,
        "fine_roots_in_registered_boxes": all(
            left < root < right
            for root, (left, right) in zip(fine["roots"], target_boxes)
        ),
        "two_resolution_root_agreement": root_agreement < 5e-4,
        "registered_horizontal_separation": min(fine["horizontal_separations"]) > 1.0 / 20.0,
        "numerically_simple_roots": min(fine["root_slope_magnitudes"]) > 1e-2,
        "monotone_predecessor_scout": fine["predecessor_min_increment"] > 0.0,
    }
    report = {
        "status": "two-resolution numerical intrinsic-drift scout",
        "discarded_resolution_note": (
            "The initial 801/1601 pair missed the unregistered 5e-4 root-agreement "
            "guard by 1.2e-4; the guard was held fixed and both resolutions doubled."
        ),
        "coarse": coarse,
        "fine": fine,
        "maximum_root_disagreement": root_agreement,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This is a floating-point Bellman/PCHIP scout, not a zero-count proof. "
            "Full-domain interval exclusion and simple-root certificates remain required."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "drift-sign-topology-scout.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
