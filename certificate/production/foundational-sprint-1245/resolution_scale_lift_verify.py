#!/usr/bin/env python3
"""Exact symbolic and hostile numerical guards for the resolution-scale lift."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent


def soft_left(matrix: np.ndarray, t: float) -> np.ndarray:
    gram = matrix @ matrix.T
    return gram @ np.linalg.inv(t * np.eye(gram.shape[0]) + gram)


def main() -> None:
    rho, c, t = sp.symbols("rho c t", positive=True)
    scale_residual = sp.factor(
        c**2 * rho / (t + c**2 * rho) - rho / (t / c**2 + rho)
    )

    fu, fmu, fp, fmp = sp.symbols("F_u F_minus_u F_P F_minus_P", positive=True)
    composed_multiplier = sp.factor((fu / fmu) * (fmp / fp))
    expected_cocycle = fu * fmp / (fmu * fp)
    cocycle_residual = sp.factor(composed_multiplier - expected_cocycle)

    rng = np.random.default_rng(1245)
    maximum_scale_residual = 0.0
    maximum_covariance_residual = 0.0
    fixtures = 0
    for _ in range(10000):
        n = int(rng.integers(2, 12))
        lam = rng.uniform(0.01, 2.0, size=n)
        mult = rng.uniform(0.05, 5.0, size=n)
        d = np.diag(lam)
        cc = np.diag(mult)
        tt = float(10.0 ** rng.uniform(-6.0, 2.0))
        left = soft_left(cc @ d, tt)
        block = np.diag(lam**2 / (tt / mult**2 + lam**2))
        maximum_scale_residual = max(
            maximum_scale_residual, float(np.linalg.norm(left - block, ord="fro"))
        )

        # Exact response correspondence from a permutation of Schmidt values.
        permutation = rng.permutation(n)
        p = np.eye(n)[permutation]
        target = p @ d @ p.T
        c_perm = np.diag(np.diag(target) / lam)
        covariance = soft_left(c_perm @ d, tt) - p @ soft_left(d, tt) @ p.T
        maximum_covariance_residual = max(
            maximum_covariance_residual, float(np.linalg.norm(covariance, ord="fro"))
        )
        fixtures += 1

    report = {
        "status": "resolution-scale lift guard",
        "symbolic_scale_orientation_residual": str(scale_residual),
        "symbolic_i3322_cocycle_residual": str(cocycle_residual),
        "random_fixtures": fixtures,
        "maximum_block_scale_residual": maximum_scale_residual,
        "maximum_unitary_covariance_residual": maximum_covariance_residual,
        "all_gates_pass": bool(
            scale_residual == 0
            and cocycle_residual == 0
            and fixtures == 10000
            and maximum_scale_residual < 1e-10
            and maximum_covariance_residual < 1e-10
        ),
        "claim_boundary": (
            "This certifies the scale orientation, response covariance, and "
            "I3322 cocycle composition. Near-contact commutators and the finite-"
            "rank boundary inequality remain open."
        ),
    }
    (HERE / "resolution-scale-lift-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
