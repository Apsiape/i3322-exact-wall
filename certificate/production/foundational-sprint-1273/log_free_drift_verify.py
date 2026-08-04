#!/usr/bin/env python3
"""Verify the log-free global drift discriminant."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq
import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "foundational-sprint-1272" / "normalization_defect_geometry_scout.py"


def load_source():
    spec = importlib.util.spec_from_file_location("s1273_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def exact_identities() -> dict:
    fp, fm, gp, gm = sp.symbols("F_p F_m G_p G_m", positive=True)
    D = fp*gp-fm*gm
    exponential_residual = sp.factor(
        fp*gp/(fm*gm)-1-D/(fm*gm)
    )

    bx, bz, u, v, kx, kz = sp.symbols(
        "b_x b_z u v K_x K_z", positive=True
    )
    fx = bx*v
    fz = bz*u
    fmx = kx*bx/v
    fmz = kz*bz/u
    characteristic_residual = sp.factor(
        (fx*fz-fmx*fmz)
        - bx*bz/(u*v)*((u*v)**2-kx*kz)
    )
    return {
        "exponential_minus_one_residual": str(exponential_residual),
        "characteristic_defect_residual": str(characteristic_residual),
        "all_exact_residuals_zero": (
            exponential_residual == 0 and characteristic_residual == 0
        ),
        "positive_denominator_consequence": (
            "sign(chi)=sign(exp(chi)-1)=sign(D); chi=0 iff D=0"
        ),
    }


def roots(sample: np.ndarray, values: np.ndarray, function) -> list[float]:
    found = []
    for index in range(len(sample)-1):
        left, right = values[index], values[index+1]
        if left == 0 or left*right < 0:
            found.append(float(brentq(
                function, sample[index], sample[index+1],
                xtol=5e-15, rtol=1e-14
            )))
    return found


def inspect(row: dict) -> dict:
    sample = row["sample"]
    chi = row["chi"]
    D = row["D"]
    F = row["F_callable"]
    P = row["P_callable"]

    def chi_function(x: float) -> float:
        p = P(float(x))
        return float(np.log(F(x)/F(-x))+np.log(F(p)/F(-p)))

    def D_function(x: float) -> float:
        p = P(float(x))
        return float(F(x)*F(p)-F(-x)*F(-p))
    mask = (np.abs(chi) > 1e-9) & (np.abs(D) > 1e-12)
    disagreements = int(np.count_nonzero(np.sign(chi[mask]) != np.sign(D[mask])))
    chi_roots = roots(sample, chi, chi_function)
    D_roots = roots(sample, D, D_function)
    root_difference = (
        max(abs(a-b) for a,b in zip(chi_roots,D_roots))
        if len(chi_roots) == len(D_roots) else float("inf")
    )
    return {
        "nodes": row["nodes"],
        "sign_comparison_points": int(np.count_nonzero(mask)),
        "sign_disagreements": disagreements,
        "chi_roots": chi_roots,
        "D_roots": D_roots,
        "maximum_root_difference": root_difference,
        "three_matched_roots": (
            len(chi_roots) == len(D_roots) == 3 and root_difference < 1e-8
        ),
    }


def main() -> None:
    source = load_source()
    exact = exact_identities()
    coarse = inspect(source.reconstruct(1601))
    fine = inspect(source.reconstruct(3201))
    gates = {
        "exact_factorization": exact["all_exact_residuals_zero"],
        "no_sign_disagreement": (
            coarse["sign_disagreements"] == fine["sign_disagreements"] == 0
        ),
        "same_three_roots": (
            coarse["three_matched_roots"] and fine["three_matched_roots"]
        ),
    }
    report = {
        "status": "exact log-free drift discriminant and numerical ancestry guard",
        "exact": exact,
        "coarse": coarse,
        "fine": fine,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The algebraic sign/root equivalence is exact. The three-root count "
            "is still numerical; the next gate is full-domain Arb exclusion."
        ),
    }
    assert report["all_gates_pass"], json.dumps(report, indent=2)
    (HERE/"log-free-drift-guard.json").write_text(
        json.dumps(report, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
