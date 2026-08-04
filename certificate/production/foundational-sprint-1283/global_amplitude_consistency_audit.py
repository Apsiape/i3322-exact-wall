#!/usr/bin/env python3
"""Audit local shooting amplitudes against the assembled global Bellman profile."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.interpolate import PchipInterpolator


HERE = Path(__file__).resolve().parent
ENGINE_PATH = (
    HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
)
ACTIVE_RADIUS = 0.898
SAMPLE = np.linspace(-ACTIVE_RADIUS, ACTIVE_RADIUS, 7201)


def load_engine():
    spec = importlib.util.spec_from_file_location("s1283_engine", ENGINE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def inspect(engine, order: int) -> dict:
    ctx.prec = 300
    c = engine.arb_fraction(
        engine.decimal_fraction(
            "0.8782729451808124520614776394587039268823793661623032741"
        )
    )
    c_dual = engine.Dual(c, (arb(0), arb(0)))
    q = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q, c_dual, order)
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
    transitions: list[tuple[float, float, float, float, str, float]] = []

    def add_chart(states: list[list[float]]) -> None:
        original = []
        reflected = []
        for state in states:
            nxt = step(state)
            x, y, u = state
            v = nxt[2]
            sx = np.sqrt(1.0 - x * x)
            sy = np.sqrt(1.0 - y * y)
            source_value = sx * u / 2.0
            target_value = sy * v / 2.0
            raw_candidate = (
                q_value
                + 1.0
                - x / 2.0
                - (x - 0.5) * y
                - (1.0 - x * x) / (4.0 * source_value)
            )
            raw_residual = abs(raw_candidate - target_value)
            if abs(y) <= 0.905 and v > 0:
                original.append((y, target_value, x))
                if abs(x) <= ACTIVE_RADIUS and abs(y) <= ACTIVE_RADIUS:
                    transitions.append(
                        (x, y, source_value, target_value, "original", raw_residual)
                    )
            if abs(x) <= 0.905 and u > 0:
                reflected_source = -y
                reflected_target = -x
                reflected_source_value = sy / (2.0 * v)
                reflected_target_value = sx / (2.0 * u)
                reflected.append((reflected_target, reflected_target_value, reflected_source))
                reflected_candidate = (
                    q_value
                    + 1.0
                    - reflected_source / 2.0
                    - (reflected_source - 0.5) * reflected_target
                    - (1.0 - reflected_source * reflected_source)
                    / (4.0 * reflected_source_value)
                )
                reflected_residual = abs(
                    reflected_candidate - reflected_target_value
                )
                if (
                    abs(reflected_source) <= ACTIVE_RADIUS
                    and abs(reflected_target) <= ACTIVE_RADIUS
                ):
                    transitions.append(
                        (
                            reflected_source,
                            reflected_target,
                            reflected_source_value,
                            reflected_target_value,
                            "reflected",
                            reflected_residual,
                        )
                    )
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
        )
        for row in rows
    ]
    assembled = []
    overlap_spreads = []
    for coordinate in SAMPLE:
        values = [
            float(chart[2](coordinate))
            for chart in charts
            if chart[0] <= coordinate <= chart[1]
        ]
        if not values:
            raise AssertionError(f"atlas gap at {coordinate}")
        assembled.append(float(np.median(values)))
        if len(values) > 1:
            overlap_spreads.append(max(values) - min(values))
    F_global = PchipInterpolator(SAMPLE, np.asarray(assembled))
    mismatch_rows = []
    raw_residuals = []
    for source, target, source_value, target_value, kind, raw_residual in transitions:
        mismatch_rows.append(
            (
                abs(float(F_global(source)) - source_value),
                source,
                target,
                kind,
                source_value,
                float(F_global(source)),
            )
        )
        raw_residuals.append(raw_residual)
    mismatch_rows.sort(reverse=True)
    mismatches = np.asarray([row[0] for row in mismatch_rows])
    maximum = mismatch_rows[0]
    return {
        "series_order": order,
        "charts": len(charts),
        "transitions_checked": len(transitions),
        "maximum_raw_local_Bellman_residual": float(max(raw_residuals)),
        "maximum_target_overlap_spread": float(max(overlap_spreads)),
        "maximum_global_source_mismatch": float(maximum[0]),
        "maximum_mismatch_source": float(maximum[1]),
        "maximum_mismatch_target": float(maximum[2]),
        "maximum_mismatch_chart_kind": maximum[3],
        "local_source_value_at_maximum": float(maximum[4]),
        "assembled_source_value_at_maximum": float(maximum[5]),
        "mismatch_ninety_ninth_percentile": float(np.quantile(mismatches, 0.99)),
        "mismatch_median": float(np.median(mismatches)),
    }


def main() -> None:
    engine = load_engine()
    rows = [inspect(engine, order) for order in (12, 14, 16)]
    maxima = [row["maximum_global_source_mismatch"] for row in rows]
    persistent = (
        min(maxima) > 5e-5
        and abs(maxima[-1] - maxima[0]) < 0.1 * maxima[0]
    )
    artifact = (
        maxima[-1] < 1e-6
        and maxima[1] / maxima[0] < 0.2
        and maxima[2] / maxima[1] < 0.2
    )
    classification = (
        "persistent global mismatch"
        if persistent
        else "truncation artifact"
        if artifact
        else "unresolved"
    )
    gates = {
        "all_raw_local_Bellman_residuals_below_one_e_minus_twelve": all(
            row["maximum_raw_local_Bellman_residual"] < 1e-12 for row in rows
        ),
        "all_target_overlap_spreads_below_one_e_minus_twelve": all(
            row["maximum_target_overlap_spread"] < 1e-12 for row in rows
        ),
    }
    report = {
        "status": "global Bellman amplitude consistency audit",
        "orders": rows,
        "maximum_mismatch_ratios": [
            maxima[1] / maxima[0], maxima[2] / maxima[1]
        ],
        "classification": classification,
        "gates": gates,
        "all_instrument_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This is a multi-order floating-point persistence audit. A theorem "
            "gap requires an Arb interval exclusion of zero at a typed transition."
        ),
    }
    (HERE / "global-amplitude-consistency-audit.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
