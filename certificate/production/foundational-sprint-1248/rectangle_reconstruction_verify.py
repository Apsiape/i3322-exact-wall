#!/usr/bin/env python3
"""Numerical guards for exact rectangle reconstruction."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def soft_weights(values: np.ndarray, t: float) -> np.ndarray:
    return values / (t + values)


def kernel_weights(values: np.ndarray, t: float) -> np.ndarray:
    return t * values / (t + values) ** 2


def main() -> None:
    rng = np.random.default_rng(1248)
    nodes, weights = np.polynomial.legendre.leggauss(400)

    max_tail_residual = 0.0
    minimum_lower_slack = float("inf")
    minimum_upper_rank_slack = float("inf")
    minimum_upper_trace_slack = float("inf")
    wrong_tail_min_residual = float("inf")

    for _ in range(1000):
        rank = int(rng.integers(1, 20))
        raw = np.exp(rng.uniform(-25.0, 0.0, size=rank))
        values = raw / np.sum(raw)
        t = float(np.exp(rng.uniform(-12.0, 8.0)))

        exact_tail = soft_weights(values, t)

        # Integrate from log(t) to a sufficiently remote upper endpoint.
        z0 = math.log(t)
        z1 = max(40.0, float(np.max(np.log(values))) + 40.0)
        zetas = (z1 - z0) * (nodes + 1.0) / 2.0 + z0
        quad = (z1 - z0) * weights / 2.0
        integrated = np.sum(
            quad[:, None]
            * kernel_weights(values[None, :], np.exp(zetas)[:, None]),
            axis=0,
        )
        max_tail_residual = max(
            max_tail_residual, float(np.max(np.abs(integrated - exact_tail)))
        )

        total = float(np.sum(exact_tail))
        minimum_lower_slack = min(minimum_lower_slack, total - 1.0 / (1.0 + t))
        minimum_upper_rank_slack = min(minimum_upper_rank_slack, rank - total)
        minimum_upper_trace_slack = min(minimum_upper_trace_slack, 1.0 / t - total)

        # The opposite tail is support minus W_t and must not be confused with W_t.
        wrong = 1.0 - exact_tail
        wrong_tail_min_residual = min(
            wrong_tail_min_residual, float(np.linalg.norm(wrong - exact_tail))
        )

    gates = {
        "upper_tail_reconstructs_soft_support": max_tail_residual < 2e-9,
        "dimension_free_lower_mass": minimum_lower_slack > -2e-14,
        "rank_upper_mass": minimum_upper_rank_slack > -2e-14,
        "trace_upper_mass": minimum_upper_trace_slack > -2e-9,
        "opposite_tail_rejected": wrong_tail_min_residual > 1e-5,
    }
    report = {
        "status": "rectangle reconstruction guard",
        "fixtures": 1000,
        "maximum_tail_quadrature_residual": max_tail_residual,
        "minimum_lower_bound_slack": minimum_lower_slack,
        "minimum_rank_upper_bound_slack": minimum_upper_rank_slack,
        "minimum_trace_upper_bound_slack": minimum_upper_trace_slack,
        "minimum_wrong-tail_residual": wrong_tail_min_residual,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Soft flags are exact rectangles of the event measure. The response-flux "
            "inequality needed for a universal dimension lower bound remains open."
        ),
    }
    (HERE / "rectangle-reconstruction-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
