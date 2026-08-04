#!/usr/bin/env python3
"""Exact normal form and numerical identification of the Bellman contact."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import minimize_scalar
import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent / "foundational-sprint-1278" / "bellman_bottleneck_classifier.py"
)
PHASE_RECEIPT = (
    HERE.parent / "foundational-sprint-1279" / "bellman-grid-phase-attack.json"
)
Q_MID = "0.250875384513976536000"
Q_RAD = "0.000000000000000000486"


def load_source():
    spec = importlib.util.spec_from_file_location("s1280_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def symbolic_normal_form() -> dict:
    x, f, q = sp.symbols("x f q")
    bellman = sp.expand(4 * f**2 - 4 * f * (q + 1 - x**2) + (1 - x**2))
    stationarity = sp.expand(
        4 * f**2 * (-sp.Rational(1, 2) - x)
        + 2 * x * f
        + (1 - x**2) * (sp.Rational(1, 2) - x)
    )
    stationarity_factor = (
        (2 * f + x - 1) * (-4 * f * x - 2 * f + 2 * x**2 + x - 1) / 2
    )
    low_branch = -4 * f * x - 2 * f + 2 * x**2 + x - 1
    quartic = 4 * x**4 - (4 * q + 5) * x**2 + q + 2
    resultant = sp.factor(sp.resultant(bellman, low_branch, f))
    y_plus = (4 * q + 5 + sp.sqrt(16 * q**2 + 24 * q - 7)) / 8
    y_residual = sp.simplify(4 * y_plus**2 - (4 * q + 5) * y_plus + q + 2)
    f_low = (2 * x**2 + x - 1) / (2 * (2 * x + 1))
    return {
        "bellman_polynomial": str(bellman),
        "stationarity_factorization": str(sp.factor(stationarity)),
        "low_branch_resultant": str(resultant),
        "quartic": str(quartic),
        "checks": {
            "stationarity_factorization_exact": sp.expand(
                stationarity - stationarity_factor
            ) == 0,
            "low_branch_substitution_exact": sp.simplify(
                low_branch.subs(f, f_low)
            ) == 0,
            "resultant_factor_exact": sp.expand(
                resultant - 8 * (x + 1) * quartic
            ) == 0,
            "outer_squared_root_exact": y_residual == 0,
        },
    }


def arb_candidate() -> tuple[dict, float, float]:
    ctx.prec = 160
    q = arb(Q_MID, Q_RAD)
    y = (4 * q + 5 + (16 * q * q + 24 * q - 7).sqrt()) / 8
    x = -y.sqrt()
    f = (2 * x * x + x - 1) / (2 * (2 * x + 1))
    coefficient = (1 - x * x) / (4 * f * f)

    def row(value: arb) -> dict:
        return {
            "interval": str(value),
            "midpoint": float(value.mid()),
            "width_upper_bound": float(2 * value.rad()),
            "lower": float(value.lower()),
            "upper": float(value.upper()),
        }

    return {
        "q": row(q),
        "x_star": row(x),
        "F_star": row(f),
        "coefficient_star": row(coefficient),
    }, float(x.mid()), float(f.mid())


def affine_hull(grid: np.ndarray, f: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    slopes = 0.5 - grid
    intercepts = (
        float(Q_MID) + 1.0 - grid / 2.0 - (1.0 - grid * grid) / (4.0 * f)
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
    return np.asarray(hull, dtype=int), np.asarray(starts, dtype=float)


def numerical_identification(source, x_star: float, f_star: float) -> dict:
    row = source.reconstruct_hull(51201)
    grid = row["grid"]
    values = row["F_values"]
    F = PchipInterpolator(grid, values)
    hull, starts = affine_hull(grid, values)

    def predecessor(x: float) -> float:
        position = int(np.searchsorted(starts, x, side="right") - 1)
        owner = int(hull[position])
        lo = float(grid[max(0, owner - 2)])
        hi = float(grid[min(len(grid) - 1, owner + 2)])
        return float(
            minimize_scalar(
                lambda z: (
                    float(Q_MID)
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

    p = predecessor(x_star)
    receipt = json.loads(PHASE_RECEIPT.read_text(encoding="utf-8"))
    bottleneck_coordinate = float(
        receipt["deep_refinement"][-1]["minimum_gap_coordinate"]
    )
    return {
        "nodes": 51201,
        "bottleneck_coordinate": bottleneck_coordinate,
        "coordinate_disagreement": abs(bottleneck_coordinate - x_star),
        "predecessor_at_x_star": p,
        "fixed_predecessor_residual": abs(p - x_star),
        "F_at_x_star": float(F(x_star)),
        "F_value_residual": abs(float(F(x_star)) - f_star),
        "F_derivative_at_x_star": float(F.derivative()(x_star)),
        "envelope_derivative_target": 0.5 - x_star,
        "envelope_derivative_residual": abs(
            float(F.derivative()(x_star)) - (0.5 - x_star)
        ),
    }


def main() -> None:
    symbolic = symbolic_normal_form()
    candidate, x_star, f_star = arb_candidate()
    numerical = numerical_identification(load_source(), x_star, f_star)
    widths = [
        candidate[key]["width_upper_bound"]
        for key in ("x_star", "F_star", "coefficient_star")
    ]
    gates = {
        "all_symbolic_checks_exact": all(symbolic["checks"].values()),
        "all_candidate_widths_below_one_e_minus_fifteen": max(widths) < 1e-15,
        "coefficient_strictly_above_one_point_one_six": (
            candidate["coefficient_star"]["lower"] > 1.16
        ),
        "bottleneck_coordinate_matches_candidate": (
            numerical["coordinate_disagreement"] < 5e-6
        ),
        "predecessor_and_value_match_candidate": (
            numerical["fixed_predecessor_residual"] < 3e-5
            and numerical["F_value_residual"] < 2e-5
        ),
        "envelope_derivative_matches_candidate": (
            numerical["envelope_derivative_residual"] < 0.01
        ),
    }
    report = {
        "status": "conditional exact Bellman contact normal form",
        "symbolic": symbolic,
        "arb_candidate": candidate,
        "numerical_identification": numerical,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The normal form is exact under the stated contact hypotheses. "
            "The global Bellman realization is numerical and is not certified."
        ),
    }
    (HERE / "algebraic-bellman-contact.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
