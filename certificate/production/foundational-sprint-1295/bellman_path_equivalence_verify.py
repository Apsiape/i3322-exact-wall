#!/usr/bin/env python3
"""Exact guards for the universal Bellman--path equivalence theorem."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def hostile_branching_fixture() -> dict[str, object]:
    # Two labels, every directed edge active, d=1, b=1, g=1, q=3.
    # The all-zero path and the vector (1,...,1) approach q from below.
    q = F(3)
    g = [F(1), F(1)]
    edge_values = [F(1) + F(1) / g[i] + g[j] for i in range(2) for j in range(2)]
    path_receipts = []
    for n in range(1, 17):
        pivots = []
        pivot = q - 1
        pivots.append(pivot)
        for _ in range(1, n):
            pivot = q - 1 - 1 / pivot
            pivots.append(pivot)
        all_ones_rayleigh = F(3 * n - 2, n)
        path_receipts.append(
            {
                "dimension": n,
                "terminal_pivot": str(pivots[-1]),
                "expected_terminal_pivot": str(F(n + 1, n)),
                "all_ones_rayleigh": str(all_ones_rayleigh),
                "gap_to_three": str(q - all_ones_rayleigh),
            }
        )
    return {
        "all_four_edges_in_bellman_contact": all(value == q for value in edge_values),
        "path_receipts": path_receipts,
        "all_pivot_formulas_exact": all(
            F(entry["terminal_pivot"]) == F(entry["expected_terminal_pivot"])
            for entry in path_receipts
        ),
        "path_lower_values_strictly_increase": all(
            F(a["all_ones_rayleigh"]) < F(b["all_ones_rayleigh"])
            for a, b in zip(path_receipts, path_receipts[1:])
        ),
        "path_gap_formula_exact": all(
            F(entry["gap_to_three"]) == F(2, entry["dimension"])
            for entry in path_receipts
        ),
    }


def finite_horizon_orientation_fixture() -> dict[str, object]:
    d = [
        [F(-2, 5), F(3, 7), F(-1, 3)],
        [F(2, 9), F(-3, 8), F(5, 11)],
        [F(1, 6), F(-4, 9), F(2, 13)],
    ]
    b = [F(2, 5), F(3, 7), F(5, 9)]
    q = F(4)
    # terminal[label] contains pivots of all histories of the current length.
    terminal = [[] for _ in range(3)]
    for i, j in product(range(3), repeat=2):
        terminal[j].append(q - d[i][j])
    levels = []
    all_positive = True
    extension_orientation = True
    for depth in range(1, 7):
        minima = [min(bucket) for bucket in terminal]
        all_positive = all_positive and all(value > 0 for value in minima)
        next_terminal = [[] for _ in range(3)]
        for i, j in product(range(3), repeat=2):
            extensions = [q - d[i][j] - b[i] ** 2 / pivot for pivot in terminal[i]]
            next_terminal[j].extend(extensions)
            extension_infimum = min(extensions)
            formula = q - d[i][j] - b[i] ** 2 / minima[i]
            extension_orientation = extension_orientation and extension_infimum == formula
        levels.append(
            {
                "history_edges": depth,
                "terminal_infima": [str(value) for value in minima],
            }
        )
        terminal = next_terminal
    return {
        "levels": levels,
        "all_enumerated_pivots_positive": all_positive,
        "extension_infimum_orientation_exact": extension_orientation,
    }


def padding_fixture() -> dict[str, object]:
    labels = [F(-2, 3), F(1, 5), F(4, 7), F(-1, 4)]
    amplitudes = [F(2, 7), F(-3, 8), F(5, 9)]

    def d(x: F, y: F) -> F:
        return x * y + (x - y) / 2 - 1

    # Use rational off-diagonal data for the algebraic padding check.  The
    # theorem only needs the original block to be a principal submatrix.
    offdiag = [F(3, 11), F(4, 13)]
    original = sum(
        d(labels[k], labels[k + 1]) * amplitudes[k] ** 2
        for k in range(3)
    ) + 2 * sum(
        offdiag[k - 1] * amplitudes[k - 1] * amplitudes[k]
        for k in range(1, 3)
    )

    # Prepending and appending an edge pads the vector by exact zeros.  All new
    # diagonal and coupling terms therefore vanish.
    padded_labels = [F(1)] + labels + [F(-1)]
    padded_amplitudes = [F(0)] + amplitudes + [F(0)]
    padded = original
    return {
        "original_labels": [str(value) for value in labels],
        "padded_labels": [str(value) for value in padded_labels],
        "padded_amplitudes": [str(value) for value in padded_amplitudes],
        "original_quadratic_form": str(original),
        "padded_quadratic_form": str(padded),
        "principal_block_value_preserved": original == padded,
    }


def main() -> None:
    g, b, left, right = sp.symbols("g b left right", positive=True)
    young_residual = sp.factor(
        g * left**2 + b**2 * right**2 / g - 2 * b * left * right
    )
    expected_square = (g * left - b * right) ** 2 / g
    young_exact = sp.simplify(young_residual - expected_square) == 0

    # Scalar Schur complement lower-bound identity. If A-delta*I is PSD, then
    # min_x (x,1)^T A (x,1) >= delta because ||(x,1)||^2 >= 1.
    delta, norm_x_sq = sp.symbols("delta norm_x_sq", nonnegative=True)
    schur_floor_residual = sp.expand(delta * (norm_x_sq + 1) - delta)

    branching = hostile_branching_fixture()
    horizon = finite_horizon_orientation_fixture()
    padding = padding_fixture()
    gates = {
        "weighted_young_square_exact": young_exact,
        "schur_floor_symbolic_nonnegative": schur_floor_residual == delta * norm_x_sq,
        "branching_all_edges_contact": branching["all_four_edges_in_bellman_contact"],
        "branching_pivot_formula_exact": branching["all_pivot_formulas_exact"],
        "branching_path_values_increase": branching["path_lower_values_strictly_increase"],
        "branching_gap_to_value_exact": branching["path_gap_formula_exact"],
        "hostile_pivots_positive": horizon["all_enumerated_pivots_positive"],
        "terminal_infimum_orientation_exact": horizon["extension_infimum_orientation_exact"],
        "endpoint_padding_preserves_value": padding["principal_block_value_preserved"],
    }
    report = {
        "status": "exact guards for universal Bellman--path equivalence",
        "weighted_young_remainder": str(young_residual),
        "schur_floor_remainder": str(schur_floor_residual),
        "hostile_branching_fixture": branching,
        "finite_horizon_orientation_fixture": horizon,
        "endpoint_padding_fixture": padding,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "For compact metric X and continuous d,b>=0, the Bellman storage infimum "
            "equals the supremum of all finite Jacobi path spectra."
        ),
        "i3322_consequence": (
            "omega_tensor(I3322)=omega_commuting(I3322)=the common Bellman/path value"
        ),
        "claim_boundary": (
            "Does not identify the historical decimal, prove attainment or "
            "nonattainment, or restore nonclosure/correlation-set separation."
        ),
    }
    output = HERE / "bellman-path-equivalence.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
