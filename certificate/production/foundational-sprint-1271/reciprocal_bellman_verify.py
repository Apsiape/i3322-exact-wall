#!/usr/bin/env python3
"""Verify reciprocal Bellman normalization and exact drift factorization."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PROD = HERE.parent


def load(sprint: int, name: str) -> dict:
    return json.loads(
        (PROD / f"foundational-sprint-{sprint}" / name).read_text(encoding="utf-8")
    )


def exact_identities() -> dict:
    # Positivity is part of the certified graph: b,u,v,F are positive.
    bz, bx, u, v = sp.symbols("b_z b_x u v", positive=True)

    fz = bz * u
    f_minus_z = bz / u
    fx = bx * v
    f_minus_x = bx / v

    p_x = bx**2 / fx
    p_minus_x = bx**2 / f_minus_x
    balanced_a = sp.sqrt(p_x * f_minus_x)
    balanced_b = sp.sqrt(fx * p_minus_x)

    residuals = {
        "reciprocal_x": sp.factor(fx * f_minus_x - bx**2),
        "reciprocal_z": sp.factor(fz * f_minus_z - bz**2),
        "p_x_minus_F_minus_x": sp.factor(p_x - f_minus_x),
        "p_minus_x_minus_F_x": sp.factor(p_minus_x - fx),
        "balanced_A_minus_F_minus_x": sp.simplify(balanced_a - f_minus_x),
        "balanced_B_minus_F_x": sp.simplify(balanced_b - fx),
        "H_x_exponential_residual": sp.factor(fx / f_minus_x - v**2),
        "H_z_exponential_residual": sp.factor(fz / f_minus_z - u**2),
        "chi_exponential_residual": sp.factor(
            (fx / f_minus_x) * (fz / f_minus_z) - (u * v) ** 2
        ),
    }
    kz, kx = sp.symbols("K_z K_x", positive=True)
    corrected_f_minus_z = kz * bz / u
    corrected_f_minus_x = kx * bx / v
    corrected_p_x = bx**2 / fx
    corrected_p_minus_x = bx**2 / corrected_f_minus_x
    corrected_a = sp.sqrt(corrected_p_x * corrected_f_minus_x)
    corrected_b = sp.sqrt(fx * corrected_p_minus_x)
    corrected = {
        "K_x_definition": sp.factor(
            fx * corrected_f_minus_x / bx**2 - kx
        ),
        "K_z_definition": sp.factor(
            fz * corrected_f_minus_z / bz**2 - kz
        ),
        "p_x_minus_F_minus_x_over_K": sp.factor(
            corrected_p_x - corrected_f_minus_x / kx
        ),
        "balanced_A_minus_F_minus_x_over_sqrt_K": sp.simplify(
            corrected_a - corrected_f_minus_x / sp.sqrt(kx)
        ),
        "balanced_B_minus_F_x_over_sqrt_K": sp.simplify(
            corrected_b - fx / sp.sqrt(kx)
        ),
        "H_x_exponential_with_K": sp.factor(
            fx / corrected_f_minus_x - v**2 / kx
        ),
        "H_z_exponential_with_K": sp.factor(
            fz / corrected_f_minus_z - u**2 / kz
        ),
        "chi_exponential_with_K": sp.factor(
            (fx / corrected_f_minus_x) * (fz / corrected_f_minus_z)
            - (u*v)**2 / (kx*kz)
        ),
    }
    return {
        "residuals": {key: str(value) for key, value in residuals.items()},
        "all_symbolic_residuals_zero": all(value == 0 for value in residuals.values()),
        "positive_log_consequence": "chi=2*log(u*v), hence chi=0 iff u*v=1",
        "corrected_residuals": {
            key: str(value) for key, value in corrected.items()
        },
        "all_corrected_residuals_zero": all(
            value == 0 for value in corrected.values()
        ),
        "corrected_positive_log_consequence": (
            "chi=2*log(u*v)-log(K_x)-log(K_z); "
            "chi=0 iff (u*v)^2=K_x*K_z"
        ),
    }


def main() -> None:
    exact = exact_identities()
    graph = load(1192, "exact-invariant-graph-projection.json")
    wing = load(1193, "exact-boundary-wing.json")
    assembly = load(1195, "theorem-assembly.json")
    atlas = load(1270, "exact-reverser-and-atlas-guard.json")

    ancestry = {
        "central_branch_uses_exact_reflection": bool(
            graph["all_tiles_certified"]
            and graph["corrected_plateau_to_section_plus_reflection"]
        ),
        "boundary_wing_and_reflection_complete": bool(
            wing["complete_right_wing_graph"]
        ),
        "global_bellman_graph_assembled": bool(assembly["all_gates_pass"]),
        "same_normalized_F_on_reflected_branch": False,
    }
    # The exact R image is a valid characteristic branch, but the numerical
    # atlas shows that identifying its local amplitude normalization with the
    # globally assembled F is false. That is the preregistered failure mode.

    numerical = {
        "maximum_reciprocal_normalization_residual": atlas["numerical"][
            "maximum_reciprocal_normalization_residual"
        ],
        "registered_atlas_tolerance": 1e-12,
        "reciprocity_candidate_rejected": atlas["numerical"][
            "maximum_reciprocal_normalization_residual"
        ] > 1e-6,
        "reciprocal_normalization_ratio_range": atlas["numerical"][
            "reciprocal_normalization_ratio_range"
        ],
    }
    gates = {
        "conditional_local_symbolics": exact["all_symbolic_residuals_zero"],
        "corrected_defect_factorization": exact["all_corrected_residuals_zero"],
        "certified_graph_ancestry_loaded": all(
            value for key, value in ancestry.items()
            if key != "same_normalized_F_on_reflected_branch"
        ),
        "global_normalization_identification_rejected": (
            not ancestry["same_normalized_F_on_reflected_branch"]
            and numerical["reciprocity_candidate_rejected"]
        ),
    }
    report = {
        "status": "reciprocal candidate rejected; exact defect factorization",
        "exact": exact,
        "ancestry": ancestry,
        "numerical": numerical,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The characteristic reverser is exact, but it does not identify the "
            "local reflected amplitude with the globally normalized Bellman F. "
            "Therefore neither reciprocal normalization nor chi=2 log(uv) is "
            "promoted. With K(x)=F(x)F(-x)/b(x)^2, the corrected exact law is "
            "chi=2 log(uv)-log K(x)-log K(P(x))."
        ),
    }
    assert report["all_gates_pass"], json.dumps(report, indent=2)
    (HERE / "reciprocal-bellman-negative.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
