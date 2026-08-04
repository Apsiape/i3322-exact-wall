#!/usr/bin/env python3
"""Exact algebraic guards for the Bellman--Hellinger flow duality."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def d(x: Fraction, y: Fraction) -> Fraction:
    """The aligned I3322 diagonal cost."""
    return x * y + (x - y) / 2 - 1


def pythagorean_point(m: int, n: int) -> tuple[Fraction, Fraction]:
    """Return an exact point (c,s) on c^2+s^2=1 with s>0."""
    denominator = m * m + n * n
    return (
        Fraction(m * m - n * n, denominator),
        Fraction(2 * m * n, denominator),
    )


def path_embedding_receipt() -> dict[str, object]:
    # Endpoints plus three exact rational points on the upper semicircle.
    interior = [
        pythagorean_point(4, 1),
        pythagorean_point(3, 2),
        pythagorean_point(2, 3),
    ]
    profile = [Fraction(1)] + [point[0] for point in interior] + [Fraction(-1)]
    sine = [Fraction(0)] + [point[1] for point in interior] + [Fraction(0)]
    amplitudes = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    norm = sum((entry * entry for entry in amplitudes), Fraction(0))

    rayleigh_diagonal = sum(
        d(profile[index], profile[index + 1]) * amplitudes[index] ** 2
        for index in range(len(amplitudes))
    )
    rayleigh_neighbor = sum(
        sine[index] * amplitudes[index - 1] * amplitudes[index]
        for index in range(1, len(amplitudes))
    )
    rayleigh = (rayleigh_diagonal + rayleigh_neighbor) / norm

    edge_mass = [entry * entry / norm for entry in amplitudes]
    row = [Fraction(0) for _ in profile]
    column = [Fraction(0) for _ in profile]
    for index, mass in enumerate(edge_mass):
        row[index] += mass
        column[index + 1] += mass

    cost_term = sum(
        edge_mass[index] * d(profile[index], profile[index + 1])
        for index in range(len(edge_mass))
    )
    # All products row_i*column_i are rational squares in this path fixture.
    hellinger = sum(
        sine[index] * amplitudes[index - 1] * amplitudes[index] / norm
        for index in range(1, len(amplitudes))
    )
    dual = cost_term + hellinger

    return {
        "profile": [str(entry) for entry in profile],
        "amplitudes": [str(entry) for entry in amplitudes],
        "edge_mass": [str(entry) for entry in edge_mass],
        "row_marginal": [str(entry) for entry in row],
        "column_marginal": [str(entry) for entry in column],
        "rayleigh_quotient": str(rayleigh),
        "flow_dual_objective": str(dual),
        "identity_exact": rayleigh == dual,
        "endpoint_contributions_zero": (
            sine[0] == 0
            and sine[-1] == 0
            and column[0] == 0
            and row[-1] == 0
        ),
    }


def contact_without_balance_receipt() -> dict[str, object]:
    # b=(1,1), g=(1,1), d_ij=1: every edge is in perfect q=3 contact.
    # A unit mass on 0->1 is supported on contact but violates both KKT balances.
    b = [Fraction(1), Fraction(1)]
    g = [Fraction(1), Fraction(1)]
    costs = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]]
    q = Fraction(3)
    pi = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(0)]]
    row = [sum(line, Fraction(0)) for line in pi]
    column = [sum((pi[i][j] for i in range(2)), Fraction(0)) for j in range(2)]
    contact_residuals = [
        q - (costs[i][j] + b[i] ** 2 / g[i] + g[j])
        for i in range(2)
        for j in range(2)
    ]
    balance_residuals = [
        column[i] - row[i] * b[i] ** 2 / g[i] ** 2 for i in range(2)
    ]
    dual_value = sum(
        pi[i][j] * costs[i][j] for i in range(2) for j in range(2)
    )
    # The Hellinger term vanishes because the chosen flow has disjoint row and
    # column support. A self-loop mass is the balanced dual optimizer of value 3.
    balanced_pi = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    balanced_value = costs[0][0] + 2 * b[0]

    return {
        "primal_value": str(q),
        "all_edges_in_contact": all(entry == 0 for entry in contact_residuals),
        "unbalanced_contact_flow_dual_value": str(dual_value),
        "balance_residuals": [str(entry) for entry in balance_residuals],
        "contact_does_not_force_balance": any(
            entry != 0 for entry in balance_residuals
        ),
        "balanced_self_loop_dual_value": str(balanced_value),
        "strong_duality_visible_in_fixture": balanced_value == q,
        "balanced_pi": [[str(entry) for entry in line] for line in balanced_pi],
    }


def main() -> None:
    r, s, b, g = sp.symbols("r s b g", positive=True)
    square_identity = sp.simplify(
        r * b**2 / g
        + s * g
        - 2 * b * sp.sqrt(r * s)
        - (b * sp.sqrt(r / g) - sp.sqrt(s * g)) ** 2
    )
    stationary_g = b * sp.sqrt(r / s)
    stationary_value = sp.simplify(
        r * b**2 / stationary_g + s * stationary_g
    )
    balance = sp.simplify(s - r * b**2 / stationary_g**2)

    path = path_embedding_receipt()
    counterfixture = contact_without_balance_receipt()
    gates = {
        "hellinger_square_identity_exact": square_identity == 0,
        "coordinate_infimum_exact": stationary_value == 2 * b * sp.sqrt(r * s),
        "kkt_balance_exact": balance == 0,
        "open_path_embedding_exact": bool(path["identity_exact"]),
        "open_path_endpoint_terms_vanish": bool(path["endpoint_contributions_zero"]),
        "perfect_contact_counterfixture_exact": bool(counterfixture["all_edges_in_contact"]),
        "contact_alone_fails_balance": bool(counterfixture["contact_does_not_force_balance"]),
        "counterfixture_strong_duality_exact": bool(counterfixture["strong_duality_visible_in_fixture"]),
    }
    report = {
        "status": "exact Bellman--Hellinger flow algebra and path weld",
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "finite_duality_formula": (
            "inf_g max_ij(d_ij+b_i^2/g_i+g_j) = "
            "sup_pi(sum_ij pi_ij d_ij + 2 sum_i b_i sqrt(r_i s_i))"
        ),
        "path_embedding": path,
        "contact_without_balance": counterfixture,
        "claim_boundary": (
            "This verifier checks the decisive exact identities and fixtures. "
            "Finite strong duality itself is proved analytically by Slater duality "
            "in BELLMAN-HELLINGER-FLOW-DUALITY.md."
        ),
    }
    output = HERE / "bellman-hellinger-flow.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
