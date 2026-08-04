#!/usr/bin/env python3
"""Hostile guards for the order-resolution event measure."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def sym_function(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.T


def kernel(rho: np.ndarray, t: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(rho)
    values = np.where(values > 1e-12, values, 0.0)
    weights = t * values / (t + values) ** 2
    return (vectors * weights) @ vectors.T


def soft_support(rho: np.ndarray, t: float) -> np.ndarray:
    values, vectors = np.linalg.eigh(rho)
    values = np.where(values > 1e-12, values, 0.0)
    weights = values / (t + values)
    return (vectors * weights) @ vectors.T


def main() -> None:
    rng = np.random.default_rng(1247)

    # Gauss-Legendre integration in zeta.  The spectrum is deliberately kept
    # in a range for which [-32,32] makes the omitted logistic tails tiny.
    nodes, weights = np.polynomial.legendre.leggauss(500)
    zetas = 32.0 * nodes
    quad_weights = 32.0 * weights

    max_rank_mass_residual = 0.0
    max_operator_mass_residual = 0.0
    max_translation_residual = 0.0
    wrong_sign_min_residual = float("inf")
    max_unitary_covariance_residual = 0.0

    for _ in range(250):
        dimension = int(rng.integers(2, 8))
        rank = int(rng.integers(1, dimension + 1))
        q, _ = np.linalg.qr(rng.normal(size=(dimension, dimension)))
        positive = np.exp(rng.uniform(-5.0, 0.0, size=rank))
        values = np.concatenate((positive, np.zeros(dimension - rank)))
        rho = q @ np.diag(values) @ q.T

        # Fundamental theorem in logarithmic scale:
        # integral_[z0,z1] K_exp(z) dz = W_exp(z0)-W_exp(z1).
        # Very wide endpoints make the comparison with the support projection
        # a numerically stable guard even for the smallest sampled eigenvalue.
        integrated = soft_support(rho, math.exp(-50.0)) - soft_support(
            rho, math.exp(50.0)
        )
        support = q[:, :rank] @ q[:, :rank].T
        max_rank_mass_residual = max(
            max_rank_mass_residual, abs(float(np.trace(integrated)) - rank)
        )
        max_operator_mass_residual = max(
            max_operator_mass_residual,
            float(np.linalg.norm(integrated - support, ord="fro")),
        )

        # A commuting block must translate event centres by +2 log(c).
        diagonal_rho = np.diag(np.exp(rng.uniform(-4.0, 0.0, size=dimension)))
        c = np.exp(rng.uniform(-1.0, 1.0, size=dimension))
        transformed = np.diag(c) @ diagonal_rho @ np.diag(c)
        for zeta in rng.uniform(-8.0, 8.0, size=8):
            left = kernel(transformed, math.exp(float(zeta)))
            right = np.diag(
                [
                    kernel(diagonal_rho, math.exp(float(zeta - 2.0 * math.log(ci))))[
                        index, index
                    ]
                    for index, ci in enumerate(c)
                ]
            )
            wrong = np.diag(
                [
                    kernel(diagonal_rho, math.exp(float(zeta + 2.0 * math.log(ci))))[
                        index, index
                    ]
                    for index, ci in enumerate(c)
                ]
            )
            max_translation_residual = max(
                max_translation_residual,
                float(np.linalg.norm(left - right, ord="fro")),
            )
            wrong_sign_min_residual = min(
                wrong_sign_min_residual,
                float(np.linalg.norm(left - wrong, ord="fro")),
            )

        # Simultaneously transport density and ordered projections.
        u, _ = np.linalg.qr(rng.normal(size=(dimension, dimension)))
        t = float(np.exp(rng.uniform(-5.0, 5.0)))
        k0 = kernel(rho, t)
        k1 = kernel(u @ rho @ u.T, t)
        max_unitary_covariance_residual = max(
            max_unitary_covariance_residual,
            float(np.linalg.norm(k1 - u @ k0 @ u.T, ord="fro")),
        )

    # The scalar identity guards the required t factor independently.
    scalar_lambda = 0.37
    scalar_integral = float(
        np.sum(
            quad_weights
            * (
                np.exp(zetas)
                * scalar_lambda
                / (np.exp(zetas) + scalar_lambda) ** 2
            )
        )
    )
    scalar_first_moment = float(
        np.sum(
            quad_weights
            * zetas
            * (
                np.exp(zetas)
                * scalar_lambda
                / (np.exp(zetas) + scalar_lambda) ** 2
            )
        )
    )

    gates = {
        "scalar_unit_mass": abs(scalar_integral - 1.0) < 2e-12,
        "scalar_log_first_moment": abs(scalar_first_moment - math.log(scalar_lambda))
        < 2e-11,
        "rank_mass": max_rank_mass_residual < 2e-10,
        "operator_support_mass": max_operator_mass_residual < 2e-10,
        "positive_translation_orientation": max_translation_residual < 2e-13,
        "wrong_translation_orientation_rejected": wrong_sign_min_residual > 1e-8,
        "unitary_covariance": max_unitary_covariance_residual < 2e-13,
    }
    report = {
        "status": "order-resolution event-measure guard",
        "fixtures": 250,
        "scalar_integral": scalar_integral,
        "scalar_first_moment": scalar_first_moment,
        "expected_scalar_first_moment": math.log(scalar_lambda),
        "maximum_rank_mass_residual": max_rank_mass_residual,
        "maximum_operator_support_residual": max_operator_mass_residual,
        "maximum_translation_residual": max_translation_residual,
        "minimum_wrong-sign_residual": wrong_sign_min_residual,
        "maximum_unitary_covariance_residual": max_unitary_covariance_residual,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The canonical measure and its exact commuting response action are verified. "
            "A quantitative I3322 finite-mass escape inequality is not yet proved."
        ),
    }
    (HERE / "order-resolution-measure-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
