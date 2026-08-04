#!/usr/bin/env python3
"""Two-resolution continuous predecessor-debt Lyapunov scout."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent
    / "foundational-sprint-1272"
    / "normalization_defect_geometry_scout.py"
)
KAPPA = 0.9
HORIZON = 200
CARRIER_POINTS = 7201


def load_source():
    spec = importlib.util.spec_from_file_location("s1277_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def debt_potential(start: np.ndarray, F, P) -> tuple[np.ndarray, np.ndarray, float]:
    current = np.asarray(start, dtype=float).copy()
    cumulative = np.zeros_like(current)
    maximum = np.zeros_like(current)
    maximizing_step = np.zeros_like(current, dtype=int)
    late_maximum = -np.inf

    for step in range(1, HORIZON + 1):
        predecessor = np.asarray(P(current), dtype=float)
        f_predecessor = np.asarray(F(predecessor), dtype=float)
        coefficient = (
            (1.0 - predecessor * predecessor)
            / (4.0 * f_predecessor * f_predecessor)
        )
        increment = np.log(coefficient) - np.log(KAPPA)
        cumulative += increment
        improved = cumulative > maximum
        maximum[improved] = cumulative[improved]
        maximizing_step[improved] = step
        if step >= 181:
            late_maximum = max(late_maximum, float(np.max(increment)))
        current = predecessor

    return maximum, maximizing_step, late_maximum


def inspect(source, nodes: int) -> tuple[dict, np.ndarray]:
    reconstruction = source.reconstruct(nodes)
    F = reconstruction["F_callable"]
    P = reconstruction["P_profile"]
    carrier = np.linspace(-0.9, 0.9, CARRIER_POINTS)
    predecessor = np.asarray(P(carrier), dtype=float)
    f_predecessor = np.asarray(F(predecessor), dtype=float)
    coefficient = (
        (1.0 - predecessor * predecessor)
        / (4.0 * f_predecessor * f_predecessor)
    )

    h, maximizing_step, late_maximum = debt_potential(carrier, F, P)
    h_after_one_step, _, _ = debt_potential(predecessor, F, P)
    weighted = coefficient * np.exp(h_after_one_step - h)
    weight_dynamic_range = float(np.exp(np.max(h) - np.min(h)))

    return {
        "bellman_nodes": nodes,
        "carrier_points": len(carrier),
        "horizon": HORIZON,
        "maximum_weighted_multiplier": float(np.max(weighted)),
        "maximum_weighted_multiplier_coordinate": float(
            carrier[int(np.argmax(weighted))]
        ),
        "minimum_weighted_multiplier": float(np.min(weighted)),
        "weight_dynamic_range": weight_dynamic_range,
        "maximum_h": float(np.max(h)),
        "maximum_h_coordinate": float(carrier[int(np.argmax(h))]),
        "latest_maximizing_step": int(np.max(maximizing_step)),
        "maximum_increment_steps_181_through_200": late_maximum,
        "predecessor_range": [float(np.min(predecessor)), float(np.max(predecessor))],
    }, h


def main() -> None:
    source = load_source()
    coarse, coarse_h = inspect(source, 1601)
    fine, fine_h = inspect(source, 3201)
    h_difference = np.abs(coarse_h - fine_h)
    disagreement_index = int(np.argmax(h_difference))
    h_disagreement = float(h_difference[disagreement_index])
    carrier = np.linspace(-0.9, 0.9, CARRIER_POINTS)
    gates = {
        "weighted_multiplier_at_most_registered_kappa": max(
            coarse["maximum_weighted_multiplier"],
            fine["maximum_weighted_multiplier"],
        ) <= 0.900001,
        "weight_dynamic_range_below_ten": max(
            coarse["weight_dynamic_range"], fine["weight_dynamic_range"]
        ) < 10.0,
        "maximizers_before_step_one_hundred": max(
            coarse["latest_maximizing_step"], fine["latest_maximizing_step"]
        ) < 100,
        "late_increments_strictly_negative": max(
            coarse["maximum_increment_steps_181_through_200"],
            fine["maximum_increment_steps_181_through_200"],
        ) < 0.0,
        "coarse_fine_h_uniform_disagreement_below_five_e_minus_three": (
            h_disagreement < 5e-3
        ),
    }
    report = {
        "status": "two-resolution continuous predecessor-debt Lyapunov scout",
        "registered_kappa": KAPPA,
        "coarse": coarse,
        "fine": fine,
        "maximum_coarse_fine_h_disagreement": h_disagreement,
        "maximum_h_disagreement_coordinate": float(carrier[disagreement_index]),
        "coarse_h_at_maximum_disagreement": float(coarse_h[disagreement_index]),
        "fine_h_at_maximum_disagreement": float(fine_h[disagreement_index]),
        "gates": gates,
        "gates_passed": sum(gates.values()),
        "gates_total": len(gates),
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This certifies only two finite-resolution, finite-horizon floating-point "
            "reconstructions. A continuous theorem requires interval orbit trapping, "
            "a certified negative tail, and cellwise interval evaluation."
        ),
    }
    (HERE / "continuous-predecessor-debt-scout.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
