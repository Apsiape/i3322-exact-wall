#!/usr/bin/env python3
"""Reconstruct Bellman drift from overlapping shooting charts only."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator


HERE = Path(__file__).resolve().parent
ENGINE_PATH = HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
REFERENCE_ROOTS = np.array([-0.8660799622164113, -0.37693687789581193, 0.7999949210929129])


def load_engine():
    spec = importlib.util.spec_from_file_location("s1269_engine", ENGINE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def midpoint(value) -> float:
    return float(value.mid())


def main() -> None:
    engine = load_engine()
    ctx.prec = 250
    c = engine.arb_fraction(
        engine.decimal_fraction(
            "0.8782729451808124520614776394587039268823793661623032741"
        )
    )
    c_dual = engine.Dual(c, (arb(0), arb(0)))
    q = engine.q_formula(c_dual)
    series, _mu = engine.parameterization(q, c_dual, 12)
    coefficients = [
        [midpoint(entry.value) for entry in row]
        for row in series
    ]
    q_value = midpoint(q.value)

    def evaluate(t: float) -> list[float]:
        return [float(np.polynomial.polynomial.polyval(t, row)) for row in coefficients]

    def step(state: list[float]) -> list[float] | None:
        x, y, u = state
        if abs(x) >= 1 or abs(y) >= 1 or u == 0:
            return None
        sx = np.sqrt(1 - x * x)
        sy = np.sqrt(1 - y * y)
        diagonal = x * y + (x - y) / 2 - 1
        v = 2 * (q_value - diagonal - sx / (2 * u)) / sy
        z = (((1 - 2 * x) + 2 * y * v / sy) / (v * v) - 1) / 2
        if not np.isfinite(v) or not np.isfinite(z):
            return None
        return [y, z, v]

    chart_rows: list[tuple[np.ndarray, np.ndarray, np.ndarray]] = []

    def build_family(parameters: np.ndarray, iterates: int) -> None:
        states = [evaluate(float(t)) for t in parameters]
        for _iterate in range(iterates):
            coordinates = []
            f_values = []
            predecessors = []
            next_states = []
            for state in states:
                nxt = step(state)
                next_states.append(nxt)
                if nxt is None:
                    continue
                x, y, _u = state
                v = nxt[2]
                if -0.905 <= y <= 0.905 and v > 0:
                    coordinates.append(y)
                    f_values.append(np.sqrt(max(0.0, 1-y*y))*v/2)
                    predecessors.append(x)
            if len(coordinates) > 50:
                order = np.argsort(coordinates)
                xx = np.asarray(coordinates)[order]
                ff = np.asarray(f_values)[order]
                pp = np.asarray(predecessors)[order]
                unique = np.concatenate(([True], np.diff(xx) > 1e-13))
                chart_rows.append((xx[unique], ff[unique], pp[unique]))
            states = [state for state in next_states if state is not None]
            if len(states) != len(parameters):
                break

    build_family(np.linspace(0.0, 0.0037582873342893243, 3001), 11)
    build_family(np.linspace(-0.003719358976358651, 0.0, 2001), 3)

    charts = [
        (xx[0], xx[-1], PchipInterpolator(xx, ff), PchipInterpolator(xx, pp))
        for xx, ff, pp in chart_rows
        if len(xx) >= 4 and np.all(np.diff(xx) > 0)
    ]

    def predictions(value: float, slot: int) -> list[float]:
        return [float(row[2+slot](value)) for row in charts if row[0] <= value <= row[1]]

    sample = np.linspace(-0.9, 0.9, 7201)
    f_sample = []
    p_sample = []
    overlap_spreads = []
    for value in sample:
        fs = predictions(float(value), 0)
        ps = predictions(float(value), 1)
        assert fs and ps
        f_sample.append(float(np.median(fs)))
        p_sample.append(float(np.median(ps)))
        if len(fs) > 1:
            overlap_spreads.append(max(fs)-min(fs))
    f_sample = np.asarray(f_sample)
    p_sample = np.asarray(p_sample)
    f_profile = PchipInterpolator(sample, f_sample)
    p_profile = PchipInterpolator(sample, p_sample)
    inverse_order = np.argsort(p_sample)
    inverse_x = p_sample[inverse_order]
    inverse_y = sample[inverse_order]
    inverse_unique = np.concatenate(([True], np.diff(inverse_x) > 1e-12))
    p_inverse = PchipInterpolator(inverse_x[inverse_unique], inverse_y[inverse_unique])
    predecessor_min_increment = float(np.min(np.diff(p_sample)))

    p_values = p_profile(sample)
    chi = (
        np.log(f_profile(sample)/f_profile(-sample))
        -np.log(f_profile(-p_values)/f_profile(p_values))
    )
    roots = []
    for i in range(len(sample)-1):
        if chi[i] == 0 or chi[i]*chi[i+1] < 0:
            # Linear interpolation is enough for the registered 2e-3 test.
            left, right = sample[i], sample[i+1]
            weight = abs(chi[i])/(abs(chi[i])+abs(chi[i+1]))
            roots.append(float(left+(right-left)*weight))
    roots_array = np.asarray(roots)
    separations = []
    for root in roots:
        predecessor = float(p_profile(root))
        a_root = float(p_inverse(-predecessor))
        separations.append(abs(a_root+root))

    root_error = float(np.max(np.abs(roots_array-REFERENCE_ROOTS))) if len(roots)==3 else float("inf")
    max_overlap = float(max(overlap_spreads)) if overlap_spreads else 0.0
    registered_targets = {
        "shooting_charts_cover_active_box": len(charts) >= 8,
        "registered_overlap_spread": max_overlap < 1e-4,
        "three_roots": len(roots) == 3,
        "agrees_with_bellman_scout": root_error < 2e-3,
        "horizontal_root_separation": len(separations) == 3 and min(separations) > 1/20,
        "composite_predecessor_near_monotone": predecessor_min_increment > -1e-4,
    }
    report = {
        "status": "registered naive shooting-atlas failure",
        "shooting_charts": len(charts),
        "maximum_F_overlap_spread": max_overlap,
        "composite_predecessor_min_increment": predecessor_min_increment,
        "roots": roots,
        "maximum_root_difference_from_sprint_1268": root_error,
        "horizontal_separations": separations,
        "registered_targets": registered_targets,
        "registered_predictions_passed": sum(registered_targets.values()),
        "registered_predictions_total": len(registered_targets),
        "naive_atlas_rejected": not all(registered_targets.values()),
        "failure_matches_known_wrong_chart": max_overlap > 1e-2 and len(roots) > 3,
        "claim_boundary": (
            "This is a floating-point reconstruction from shooting charts, not "
            "an interval zero-count certificate."
        ),
    }
    assert report["naive_atlas_rejected"]
    assert report["failure_matches_known_wrong_chart"]
    (HERE/"shooting-atlas-drift-reconstruction.json").write_text(
        json.dumps(report, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
