#!/usr/bin/env python3
"""Hostile guards for the noncommutative resolution identity."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent


def soft_left(matrix: np.ndarray, t: float) -> np.ndarray:
    rho = matrix @ matrix.T
    return rho @ np.linalg.inv(t * np.eye(rho.shape[0]) + rho)


def main() -> None:
    rho, c, t = sp.symbols("rho c t", positive=True)
    scalar_residual = sp.factor(
        c**2 * rho / (t + c**2 * rho) - rho / (t / c**2 + rho)
    )
    wrong_orientation = sp.factor(
        c**2 * rho / (t + c**2 * rho) - rho / (t * c**2 + rho)
    )

    rng = np.random.default_rng(1246)
    maximum_identity_residual = 0.0
    maximum_flag_trace_residual = 0.0
    maximum_right_identity_residual = 0.0
    minimum_commutator_norm = float("inf")
    fixtures = 0

    for _ in range(10000):
        n = int(rng.integers(2, 11))
        d = rng.normal(size=(n, n))
        d /= max(np.linalg.norm(d, ord="fro"), 1e-12)
        q, _ = np.linalg.qr(rng.normal(size=(n, n)))
        eigenvalues = rng.uniform(0.1, 4.0, size=n)
        cc = q @ np.diag(eigenvalues) @ q.T
        cinv = np.linalg.inv(cc)
        cminus2 = cinv @ cinv
        tt = float(10.0 ** rng.uniform(-5.0, 2.0))
        rho_left = d @ d.T

        direct = soft_left(cc @ d, tt)
        inner = rho_left @ np.linalg.inv(tt * cminus2 + rho_left)
        lifted = cc @ inner @ cinv
        maximum_identity_residual = max(
            maximum_identity_residual, float(np.linalg.norm(direct - lifted, ord="fro"))
        )
        minimum_commutator_norm = min(
            minimum_commutator_norm, float(np.linalg.norm(cc @ rho_left - rho_left @ cc))
        )

        # Spectral flags of C commute with C but generically not with rho.
        rank = int(rng.integers(0, n + 1))
        flag = q[:, :rank] @ q[:, :rank].T
        trace_direct = float(np.trace(flag @ direct))
        trace_inner = float(np.trace(flag @ inner))
        maximum_flag_trace_residual = max(
            maximum_flag_trace_residual, abs(trace_direct - trace_inner)
        )

        # Right multiplier: transpose the entire statement through D^T.
        rho_right = d.T @ d
        direct_right = soft_left(cc @ d.T, tt)
        inner_right = rho_right @ np.linalg.inv(tt * cminus2 + rho_right)
        lifted_right = cc @ inner_right @ cinv
        maximum_right_identity_residual = max(
            maximum_right_identity_residual,
            float(np.linalg.norm(direct_right - lifted_right, ord="fro")),
        )
        fixtures += 1

    report = {
        "status": "operator-valued resolution guard",
        "symbolic_commuting_residual": str(scalar_residual),
        "wrong_scale_orientation_control": str(wrong_orientation),
        "random_noncommuting_fixtures": fixtures,
        "maximum_left_identity_residual": maximum_identity_residual,
        "maximum_flag_trace_residual": maximum_flag_trace_residual,
        "maximum_right_identity_residual": maximum_right_identity_residual,
        "minimum_sampled_multiplier_density_commutator": minimum_commutator_norm,
        "all_gates_pass": bool(
            scalar_residual == 0
            and wrong_orientation != 0
            and fixtures == 10000
            and maximum_identity_residual < 1e-9
            and maximum_flag_trace_residual < 1e-9
            and maximum_right_identity_residual < 1e-9
            and minimum_commutator_norm > 1e-8
        ),
        "claim_boundary": (
            "This verifies the exact noncommutative identity on hostile "
            "noncommuting fixtures. Relative Alice/Bob metric composition and "
            "finite-rank closure remain open."
        ),
    }
    (HERE / "operator-valued-resolution-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
