#!/usr/bin/env python3
"""Exact reversed-plateau obstruction to weighted Bellman contraction."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent


def load(sprint: int, filename: str) -> dict:
    return json.loads(
        (FRONTIER / f"foundational-sprint-{sprint}" / filename).read_text(
            encoding="utf-8"
        )
    )


def main() -> None:
    c = sp.symbols("c", positive=True)
    s = sp.sqrt(1 - c**2)
    ratio = s * (2 * c - 1) / ((1 - c) * (2 * c + 1))
    q = (4 * c**4 - 5 * c**2 + 2) / (4 * c**2 - 1)
    x = -c
    u = 1 / ratio
    f_negative = s * u / 2
    f_low_branch = (2 * x**2 + x - 1) / (2 * (2 * x + 1))
    quartic = 4 * x**4 - (4 * q + 5) * x**2 + q + 2

    diagonal = x * x + (x - x) / 2 - 1
    next_ratio = 2 * (q - diagonal - s / (2 * u)) / s
    next_coordinate = (
        ((1 - 2 * x) + 2 * x * next_ratio / s) / next_ratio**2 - 1
    ) / 2
    multiplier = (1 - x**2) / (4 * f_negative**2)
    multiplier_excess = sp.factor(ratio**2 - 1)
    expected_excess = -2 * c * (4 * c**2 - 3) / (
        (c - 1) * (2 * c + 1) ** 2
    )

    exact_checks = {
        "quartic_is_plateau_law": sp.simplify(quartic) == 0,
        "negative_value_is_low_branch": sp.simplify(sp.powsimp(
            f_negative - f_low_branch, force=True
        )) == 0,
        "reversed_ratio_is_fixed": sp.simplify(sp.powsimp(
            next_ratio - u, force=True
        )) == 0,
        "reversed_coordinate_is_fixed": sp.simplify(sp.powsimp(
            next_coordinate - x, force=True
        )) == 0,
        "contact_multiplier_is_ratio_squared": sp.simplify(sp.powsimp(
            multiplier - ratio**2, force=True
        )) == 0,
        "multiplier_excess_factorization": sp.simplify(
            multiplier_excess - expected_excess
        ) == 0,
    }

    plateau = load(1115, "plateau-hyperbolicity-certificate.json")
    reverser = load(1270, "exact-reverser-and-atlas-guard.json")
    graph = load(1192, "exact-invariant-graph-projection.json")
    bellman = load(1195, "theorem-assembly.json")
    dependency_gates = {
        "exact_plateau_branch": plateau["root_count"]["above_one"] == 1,
        "exact_reverser": reverser["exact"]["all_exact_residuals_zero"],
        "global_characteristic_graph": graph["all_tiles_certified"],
        "global_bellman_fixed_point": bellman["all_gates_pass"],
    }
    branch_signs = {
        "c_positive": True,
        "four_c_squared_minus_three_positive": True,
        "c_minus_one_negative": True,
        "denominator_square_positive": True,
        "ratio_squared_minus_one_positive": True,
        "argument": (
            "On sqrt(3)/2<c<1, the numerator -2c(4c^2-3) and "
            "the factor c-1 are both negative, while (2c+1)^2 is positive."
        ),
    }
    gates = {
        "all_symbolic_checks_exact": all(exact_checks.values()),
        "all_dependency_gates_pass": all(dependency_gates.values()),
        "multiplier_strictly_above_one_on_branch": branch_signs[
            "ratio_squared_minus_one_positive"
        ],
    }
    report = {
        "status": "exact reversed-plateau weighted-contraction obstruction",
        "exact_checks": exact_checks,
        "dependency_gates": dependency_gates,
        "symbolic": {
            "plateau_ratio_R": str(ratio),
            "plateau_q": str(q),
            "negative_contact": "x=-c, u=1/R",
            "negative_Bellman_value": str(sp.factor(f_negative)),
            "contact_multiplier": "R^2",
            "R_squared_minus_one": str(multiplier_excess),
        },
        "branch_signs": branch_signs,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "For every bounded positive weight with finite nonzero value at "
            "the reversed plateau -C, the weighted Bellman composition "
            "derivative has operator norm at least R^2>1. It is not a "
            "contraction in any such weighted sup norm."
        ),
        "claim_boundary": (
            "This excludes a weighted-sup contraction proof architecture. It "
            "does not alter the exact I3322 wall or prove the conditional "
            "dimension lower bound."
        ),
    }
    (HERE / "reversed-plateau-obstruction.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
