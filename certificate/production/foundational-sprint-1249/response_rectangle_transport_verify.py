#!/usr/bin/env python3
"""Hostile noncommuting guard for response-rectangle transport."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def soft_support(matrix: np.ndarray, t: float) -> np.ndarray:
    density = matrix @ matrix.T
    return np.eye(density.shape[0]) - t * np.linalg.inv(t * np.eye(density.shape[0]) + density)


def main() -> None:
    rng = np.random.default_rng(1249)
    safe_constant = 3.0 * np.sqrt(6.0) / 8.0
    max_ratio = 0.0
    max_trace_ratio = 0.0
    minimum_commutator = float("inf")
    too_small_constant_violations = 0

    for _ in range(10000):
        n = int(rng.integers(2, 8))
        d = rng.normal(size=(n, n))
        d /= max(1.0, np.linalg.norm(d, ord="fro"))
        q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        c_values = np.exp(rng.uniform(-1.0, 1.0, size=n))
        c = q @ np.diag(c_values) @ q.T
        j, _ = np.linalg.qr(rng.normal(size=(n, n)))
        s, _ = np.linalg.qr(rng.normal(size=(n, n)))

        # Build an arbitrary response residual; no near-commuting fixture is used.
        m = c @ d
        target = j @ d @ s.T
        delta = float(np.linalg.norm(m - target, ord="fro"))
        t = float(np.exp(rng.uniform(-5.0, 5.0)))
        lhs_matrix = soft_support(m, t) - j @ soft_support(d, t) @ j.T
        rhs = safe_constant * delta / np.sqrt(t)
        ratio = float(np.linalg.norm(lhs_matrix, ord="fro")) / max(rhs, 1e-300)
        max_ratio = max(max_ratio, ratio)

        rank = int(rng.integers(1, n + 1))
        e_basis, _ = np.linalg.qr(rng.normal(size=(n, n)))
        e = e_basis[:, :rank] @ e_basis[:, :rank].T
        trace_lhs = abs(float(np.trace(e @ lhs_matrix)))
        trace_rhs = np.sqrt(rank) * rhs
        max_trace_ratio = max(
            max_trace_ratio, float(trace_lhs / max(float(trace_rhs), 1e-300))
        )

        rho = d @ d.T
        minimum_commutator = min(
            minimum_commutator, float(np.linalg.norm(c @ rho - rho @ c, ord="fro"))
        )
        too_small_rhs = 0.60 * delta / np.sqrt(t)
        if float(np.linalg.norm(lhs_matrix, ord="fro")) > too_small_rhs * (1.0 + 1e-12):
            too_small_constant_violations += 1

    # A scalar derivative fixture approaches 9/(8 sqrt(3))=0.6495..., so a
    # putative universal constant 0.60 must fail independently of randomness.
    t = 0.37
    x = np.sqrt(t / 3.0)
    step = 1e-8
    scalar_lhs = abs(x * x / (t + x * x) - (x + step) ** 2 / (t + (x + step) ** 2))
    scalar_too_small = 0.60 * step / np.sqrt(t)
    if scalar_lhs > scalar_too_small:
        too_small_constant_violations += 1

    gates = {
        "matrix_transport_bound": bool(max_ratio <= 1.0 + 2e-11),
        "rectangle_trace_bound": bool(max_trace_ratio <= 1.0 + 2e-11),
        "hostile_noncommutation": bool(minimum_commutator > 1e-8),
        "too_small_sqrt_t_constant_rejected": bool(too_small_constant_violations > 0),
    }
    report = {
        "status": "response rectangle transport guard",
        "fixtures": 10000,
        "maximum_matrix_bound_ratio": max_ratio,
        "maximum_trace_bound_ratio": max_trace_ratio,
        "minimum_multiplier_density_commutator": minimum_commutator,
        "safe_square_root_constant": float(safe_constant),
        "too_small_constant_violations": too_small_constant_violations,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Individual response pushforwards are controlled on complete rectangles. "
            "The two-response skew-composition flux theorem remains open."
        ),
    }
    (HERE / "response-rectangle-transport-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
