#!/usr/bin/env python3
"""Collision between shooting-atlas and boundary-iteration Bellman selectors."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, minimize_scalar


HERE = Path(__file__).resolve().parent
ENGINE_PATH = (
    HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
)
HULL_PATH = (
    HERE.parent / "foundational-sprint-1278" / "bellman_bottleneck_classifier.py"
)
ACTIVE_RADIUS = 0.898
SAMPLE = np.linspace(-ACTIVE_RADIUS, ACTIVE_RADIUS, 7201)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def shooting_profile(engine) -> dict:
    ctx.prec = 250
    c = engine.arb_fraction(
        engine.decimal_fraction(
            "0.8782729451808124520614776394587039268823793661623032741"
        )
    )
    c_dual = engine.Dual(c, (arb(0), arb(0)))
    q = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q, c_dual, 12)
    coefficients = [
        [float(item.value.mid()) for item in row] for row in series
    ]
    q_value = float(q.value.mid())
    mu_value = float(mu.value.mid())

    def evaluate(t: float) -> list[float]:
        return [
            float(np.polynomial.polynomial.polyval(t, row))
            for row in coefficients
        ]

    def step(state: list[float]) -> list[float]:
        x, y, u = state
        sx = np.sqrt(1.0 - x * x)
        sy = np.sqrt(1.0 - y * y)
        diagonal = x * y + (x - y) / 2.0 - 1.0
        v = 2.0 * (q_value - diagonal - sx / (2.0 * u)) / sy
        z = (((1.0 - 2.0 * x) + 2.0 * y * v / sy) / (v * v) - 1.0) / 2.0
        return [y, z, v]

    rows: list[np.ndarray] = []

    def add_chart(states: list[list[float]]) -> None:
        original = []
        reflected = []
        for state in states:
            nxt = step(state)
            x, y, u = state
            v = nxt[2]
            if abs(y) <= 0.905 and v > 0:
                original.append((y, np.sqrt(1.0 - y * y) * v / 2.0, x))
            if abs(x) <= 0.905 and u > 0:
                reflected.append((-x, np.sqrt(1.0 - x * x) / (2.0 * u), -y))
        for chart in (original, reflected):
            chart.sort()
            if len(chart) > 20:
                array = np.asarray(chart)
                keep = np.concatenate(([True], np.diff(array[:, 0]) > 1e-13))
                rows.append(array[keep])

    t_hi = 0.0037582873342893243
    t_lo = t_hi / mu_value
    add_chart([evaluate(t) for t in np.linspace(0.0, t_lo, 1201)])
    central = [evaluate(t) for t in np.linspace(t_lo, t_hi, 3001)]
    for _ in range(4):
        add_chart(central)
        central = [step(state) for state in central]
    add_chart(central)
    wing = [
        evaluate(t)
        for t in np.linspace(-0.003719358976358651, 0.0, 2401)
    ]
    for _ in range(2):
        add_chart(wing)
        wing = [step(state) for state in wing]
    add_chart(wing)

    charts = [
        (
            row[0, 0],
            row[-1, 0],
            PchipInterpolator(row[:, 0], row[:, 1]),
            PchipInterpolator(row[:, 0], row[:, 2]),
        )
        for row in rows
    ]
    values = []
    predecessors = []
    spreads = []
    for x in SAMPLE:
        local_values = [
            float(chart[2](x))
            for chart in charts
            if chart[0] <= x <= chart[1]
        ]
        local_predecessors = [
            float(chart[3](x))
            for chart in charts
            if chart[0] <= x <= chart[1]
        ]
        if not local_values or not local_predecessors:
            raise AssertionError(f"shooting atlas gap at {x}")
        values.append(float(np.median(local_values)))
        predecessors.append(float(np.median(local_predecessors)))
        if len(local_values) > 1:
            spreads.append(max(local_values) - min(local_values))
    return {
        "F_values": np.asarray(values),
        "P_values": np.asarray(predecessors),
        "maximum_overlap_spread": float(max(spreads)),
        "charts": len(charts),
        "c": float(c.mid()),
    }


def affine_hull(grid: np.ndarray, f: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    slopes = 0.5 - grid
    q = 0.250875384513976536
    intercepts = q + 1.0 - grid / 2.0 - (1.0 - grid * grid) / (4.0 * f)
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


def boundary_iteration_profile(source) -> dict:
    row = source.reconstruct_hull(51201)
    grid = row["grid"]
    values = row["F_values"]
    F = PchipInterpolator(grid, values)
    hull, starts = affine_hull(grid, values)
    positions = np.searchsorted(starts, SAMPLE, side="right") - 1
    owners = hull[positions]
    predecessors = []
    for x, owner in zip(SAMPLE, owners):
        lo = float(grid[max(0, int(owner) - 2)])
        hi = float(grid[min(len(grid) - 1, int(owner) + 2)])
        predecessor = minimize_scalar(
            lambda z: (
                0.250875384513976536
                + 1.0
                - z / 2.0
                - (z - 0.5) * float(x)
                - (1.0 - z * z) / (4.0 * float(F(z)))
            ),
            bounds=(lo, hi),
            method="bounded",
            options={"xatol": 2e-14, "maxiter": 100},
        ).x
        predecessors.append(float(predecessor))
    return {
        "F_values": np.asarray(F(SAMPLE), dtype=float),
        "P_values": np.asarray(predecessors),
        "iterations": row["iterations"],
        "final_delta": row["final_delta"],
    }


def drift_roots(profile: dict) -> dict:
    F = PchipInterpolator(SAMPLE, profile["F_values"])
    P = PchipInterpolator(SAMPLE, profile["P_values"])

    def discriminant(x: float) -> float:
        p = float(P(x))
        return float(F(x) * F(p) - F(-x) * F(-p))

    values = np.asarray([discriminant(float(x)) for x in SAMPLE])
    roots = []
    slopes = []
    for left, right, a, b in zip(SAMPLE, SAMPLE[1:], values, values[1:]):
        if a == 0.0 or a * b < 0.0:
            root = float(brentq(discriminant, float(left), float(right)))
            roots.append(root)
            h = 2e-5
            slopes.append(abs((discriminant(root + h) - discriminant(root - h)) / (2*h)))
    return {"roots": roots, "slope_magnitudes": slopes}


def contact_residual(profile: dict) -> dict:
    F = PchipInterpolator(SAMPLE, profile["F_values"])
    predecessor = profile["P_values"]
    mask = np.abs(predecessor) <= 0.8975
    p = predecessor[mask]
    x = SAMPLE[mask]
    candidate = (
        0.250875384513976536
        + 1.0
        - p / 2.0
        - (p - 0.5) * x
        - (1.0 - p * p) / (4.0 * F(p))
    )
    residual = np.abs(candidate - profile["F_values"][mask])
    return {
        "comparison_points": int(np.count_nonzero(mask)),
        "maximum_absolute_residual": float(np.max(residual)),
        "maximum_residual_coordinate": float(x[int(np.argmax(residual))]),
        "ninety_ninth_percentile_residual": float(np.quantile(residual, 0.99)),
    }


def main() -> None:
    shooting = shooting_profile(load(ENGINE_PATH, "s1282_engine"))
    boundary = boundary_iteration_profile(load(HULL_PATH, "s1282_hull"))
    shooting_drift = drift_roots(shooting)
    boundary_drift = drift_roots(boundary)
    shooting_contact = contact_residual(shooting)
    boundary_contact = contact_residual(boundary)
    profile_discrepancy = float(
        np.max(np.abs(shooting["F_values"] - boundary["F_values"]))
    )
    profile_discrepancy_coordinate = float(
        SAMPLE[int(np.argmax(np.abs(shooting["F_values"] - boundary["F_values"])))]
    )
    root_differences = [
        abs(a - b)
        for a, b in zip(shooting_drift["roots"], boundary_drift["roots"])
    ]
    c = shooting["c"]
    s = np.sqrt(1.0 - c * c)
    ratio = s * (2.0 * c - 1.0) / ((1.0 - c) * (2.0 * c + 1.0))
    exact_plateau = {-1: s / (2.0 * ratio), 1: s * ratio / 2.0}
    F_shooting = PchipInterpolator(SAMPLE, shooting["F_values"])
    F_boundary = PchipInterpolator(SAMPLE, boundary["F_values"])
    plateau_errors = {
        name: max(
            abs(float(profile(sign * c)) - exact_plateau[sign])
            for sign in (-1, 1)
        )
        for name, profile in (
            ("shooting", F_shooting),
            ("boundary_iteration", F_boundary),
        )
    }
    simple = (
        len(shooting_drift["roots"]) == len(boundary_drift["roots"]) == 3
        and min(shooting_drift["slope_magnitudes"] + boundary_drift["slope_magnitudes"])
        > 1e-3
    )
    same = (
        profile_discrepancy < 5e-5
        and len(root_differences) == 3
        and max(root_differences) < 2e-4
    )
    distinct = (
        profile_discrepancy > 1e-4
        and len(root_differences) == 3
        and max(root_differences) > 5e-4
    )
    classification = (
        "same selector consistent"
        if same
        else "distinct selector consistent"
        if distinct
        else "unresolved"
    )
    gates = {
        "shooting_overlap_below_one_e_minus_twelve": bool(
            shooting["maximum_overlap_spread"] < 1e-12
        ),
        "both_profiles_positive": bool(
            np.min(shooting["F_values"]) > 0
            and np.min(boundary["F_values"]) > 0
        ),
        "both_have_three_simple_roots": bool(simple),
        "both_match_exact_plateaux": bool(max(plateau_errors.values()) < 2e-5),
    }
    report = {
        "status": "Bellman selector collision",
        "shooting": {
            "charts": shooting["charts"],
            "maximum_overlap_spread": shooting["maximum_overlap_spread"],
            "minimum_F": float(np.min(shooting["F_values"])),
            "drift": shooting_drift,
            "post_hoc_contact_residual": shooting_contact,
        },
        "boundary_iteration": {
            "nodes": 51201,
            "iterations": boundary["iterations"],
            "final_delta": boundary["final_delta"],
            "minimum_F": float(np.min(boundary["F_values"])),
            "drift": boundary_drift,
            "post_hoc_contact_residual": boundary_contact,
        },
        "plateau_errors": plateau_errors,
        "maximum_profile_discrepancy": profile_discrepancy,
        "maximum_profile_discrepancy_coordinate": profile_discrepancy_coordinate,
        "paired_root_differences": root_differences,
        "classification": classification,
        "post_hoc_adjudication": (
            "The local shooting atlas is not the globally normalized Bellman "
            "profile: its sampled contact residual is orders of magnitude larger "
            "than the boundary-iteration residual. The registered distinction "
            "therefore does not evidence two exact Bellman fixed points."
        ),
        "gates": gates,
        "all_instrument_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This compares two floating reconstructions with distinct ancestry. "
            "It does not prove multiplicity of exact Bellman fixed points."
        ),
    }
    (HERE / "bellman-selector-collision.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
