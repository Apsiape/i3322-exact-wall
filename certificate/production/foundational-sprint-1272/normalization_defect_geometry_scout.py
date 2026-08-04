#!/usr/bin/env python3
"""Two-resolution scout for the Bellman normalization defect K."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, minimize_scalar
import sympy as sp


HERE = Path(__file__).resolve().parent
Q_STAR = 0.250875384513976536


def exact_tariffs() -> dict:
    a, c, kz, kx = sp.symbols("a c K_z K_x", positive=True)
    A = a * sp.sqrt(kz)
    B = c / sp.sqrt(kx)
    f_minus_z = a * kz
    p_minus_x = c / kx
    residuals = {
        "symmetrization_tariff": sp.factor(
            (a+c-A-B) - (a*(1-sp.sqrt(kz))+c*(1-1/sp.sqrt(kx)))
        ),
        "reflected_bellman_tariff": sp.factor(
            (a+c-f_minus_z-p_minus_x) - (a*(1-kz)+c*(1-1/kx))
        ),
    }
    return {
        "residuals": {key: str(value) for key, value in residuals.items()},
        "all_exact_residuals_zero": all(value == 0 for value in residuals.values()),
        "K_is_even_by_definition": True,
    }


def reconstruct(node_count: int) -> dict:
    grid = np.linspace(-1.0, 1.0, node_count)
    boundary = Q_STAR + (1.0-grid)/2.0
    f = boundary.copy()
    gx = grid[:, None]
    gy = grid[None, :]
    for iteration in range(1, 5001):
        candidates = (
            Q_STAR + 1.0 - gx/2.0 - (gx-0.5)*gy
            - (1.0-gx*gx)/(4.0*f[:, None])
        )
        updated = np.maximum(np.minimum(boundary, np.min(candidates, axis=0)), 1e-14)
        delta = float(np.max(np.abs(updated-f)))
        f = updated
        if delta < 1e-11:
            break

    F = PchipInterpolator(grid, f)
    sample = np.linspace(-0.9, 0.9, 3601)

    def predecessor(x: float) -> float:
        values = (
            Q_STAR + 1.0 - grid/2.0 - (grid-0.5)*x
            - (1.0-grid*grid)/(4.0*f)
        )
        owner = int(np.argmin(values))
        lo = float(grid[max(0, owner-2)])
        hi = float(grid[min(node_count-1, owner+2)])
        return float(minimize_scalar(
            lambda z: (
                Q_STAR + 1.0 - z/2.0 - (z-0.5)*x
                - (1.0-z*z)/(4.0*float(F(z)))
            ),
            bounds=(lo, hi), method="bounded",
            options={"xatol": 2e-14, "maxiter": 100},
        ).x)

    fs = F(sample)
    fminus = F(-sample)
    bsq = (1.0-sample*sample)/4.0
    K = fs*fminus/bsq
    P = np.asarray([predecessor(float(x)) for x in sample])
    Fp = F(P)
    Fmp = F(-P)
    bp2 = (1.0-P*P)/4.0
    Kp = Fp*Fmp/bp2
    pP = bp2/Fp
    pminus_x = bsq/fminus
    A = np.sqrt(pP*Fmp)
    B = np.sqrt(fs*pminus_x)
    rsym_direct = pP+fs-A-B
    rsym_formula = pP*(1.0-np.sqrt(Kp))+fs*(1.0-1.0/np.sqrt(K))
    rref_direct = pP+fs-Fmp-pminus_x
    rref_formula = pP*(1.0-Kp)+fs*(1.0-1.0/K)
    H = np.log(fs/fminus)
    Hp = np.log(Fp/Fmp)
    chi = H+Hp

    roots = []
    for i in range(len(sample)-1):
        if chi[i] == 0 or chi[i]*chi[i+1] < 0:
            interpolant = PchipInterpolator(sample[i:i+2], chi[i:i+2])
            roots.append(float(brentq(interpolant, sample[i], sample[i+1])))
    rsym_profile = PchipInterpolator(sample, rsym_direct)
    rsym_at_drift_roots = [float(rsym_profile(root)) for root in roots]
    positive = sample >= 0
    k_positive = K[positive]
    active = np.abs(sample) <= 0.898
    exterior = np.abs(sample) > 0.898
    K_profile = PchipInterpolator(sample, K)
    probe_coordinates = [0.0, 0.8, 0.89, 0.895, 0.898, 0.898116482394039, 0.899, 0.9]
    return {
        "nodes": node_count,
        "iterations": iteration,
        "final_delta": delta,
        "sample": sample,
        "K": K,
        "K_minimum": float(np.min(K)),
        "K_maximum": float(np.max(K)),
        "K_at_zero": float(K[len(K)//2]),
        "K_maximum_coordinate": float(sample[int(np.argmax(K))]),
        "positive_half_largest_increment": float(np.max(np.diff(k_positive))),
        "active_K_minimum": float(np.min(K[active])),
        "active_K_maximum": float(np.max(K[active])),
        "active_K_maximum_coordinate": float(
            sample[np.flatnonzero(active)[int(np.argmax(K[active]))]]
        ),
        "exterior_K_minimum": float(np.min(K[exterior])),
        "exterior_K_maximum": float(np.max(K[exterior])),
        "K_boundary_probes": {
            str(x): float(K_profile(x)) for x in probe_coordinates
        },
        "tariff_formula_maximum_residual": float(max(
            np.max(np.abs(rsym_direct-rsym_formula)),
            np.max(np.abs(rref_direct-rref_formula)),
        )),
        "drift_roots": roots,
        "symmetrization_tariff_at_drift_roots": rsym_at_drift_roots,
        "symmetrization_tariff_minimum": float(np.min(rsym_direct)),
        "symmetrization_tariff_maximum": float(np.max(rsym_direct)),
        "reflected_tariff_minimum": float(np.min(rref_direct)),
        "reflected_tariff_maximum": float(np.max(rref_direct)),
    }


def public(row: dict) -> dict:
    return {key: value for key, value in row.items() if key not in {"sample", "K"}}


def main() -> None:
    exact = exact_tariffs()
    coarse = reconstruct(1601)
    fine = reconstruct(3201)
    K_disagreement = float(np.max(np.abs(
        coarse["K"]-fine["K"]
    )))
    q_excess = Q_STAR-0.25
    root_tariffs = fine["symmetrization_tariff_at_drift_roots"]
    predictions = {
        "K_at_least_one_with_resolution_allowance": (
            fine["K_minimum"] >= 1.0-2.0*K_disagreement
        ),
        "unique_numerical_maximum_at_zero": (
            fine["K_maximum_coordinate"] == 0.0
            and fine["positive_half_largest_increment"] < 1e-10
        ),
        "registered_half_q_excess_bound": (
            fine["K_maximum"]-1.0 < 0.5*q_excess
        ),
        "exact_tariff_formulas": (
            exact["all_exact_residuals_zero"]
            and fine["tariff_formula_maximum_residual"] < 1e-12
        ),
        "tariff_zeros_coincide_with_drift_roots": (
            len(root_tariffs) == 3 and max(abs(x) for x in root_tariffs) < 1e-8
        ),
    }
    report = {
        "status": "two-resolution normalization-defect geometry scout",
        "exact": exact,
        "coarse": public(coarse),
        "fine": public(fine),
        "maximum_K_disagreement": K_disagreement,
        "q_star_minus_quarter": q_excess,
        "predictions": predictions,
        "predictions_passed": sum(predictions.values()),
        "predictions_total": len(predictions),
        "all_predictions_pass": all(predictions.values()),
        "claim_boundary": (
            "The tariff identities are exact. K topology and all zero-set "
            "comparisons are floating-point scouts and are not theorem claims."
        ),
    }
    (HERE/"normalization-defect-geometry-scout.json").write_text(
        json.dumps(report, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
