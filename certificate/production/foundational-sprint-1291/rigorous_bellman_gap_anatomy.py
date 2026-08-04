#!/usr/bin/env python3
"""Rigorous decomposition of the current I3322 upper/lower window."""

from __future__ import annotations

from fractions import Fraction
import hashlib
from math import isqrt
import json
from pathlib import Path

from mpmath import iv
from mpmath.libmp import to_str


HERE = Path(__file__).resolve().parent
PRODUCTION = HERE.parent
UPPER_CANDIDATE = PRODUCTION / "foundational-sprint-1287/bellman-subsolution-candidate.json"
LOWER_CANDIDATE = PRODUCTION / "foundational-sprint-1288/finite-strategy-candidate.json"
LOWER_REPORT = PRODUCTION / "foundational-sprint-1288/exact-finite-strategy-lower-bound.json"
UPPER_REPORT = PRODUCTION / "foundational-sprint-1290/exact-fixed-witness-threshold.json"
SQRT_SCALE = 10**60
iv.dps = 160


def box(value: Fraction):
    return iv.mpf(value.numerator) / iv.mpf(value.denominator)


def endpoints(value) -> list[str]:
    return [to_str(value._mpi_[0], 170), to_str(value._mpi_[1], 170)]


def rational_sqrt_floor(value: Fraction) -> Fraction:
    scaled_square = value.numerator * SQRT_SCALE * SQRT_SCALE // value.denominator
    return Fraction(isqrt(scaled_square), SQRT_SCALE)


def aligned_cost(x: Fraction, y: Fraction) -> Fraction:
    return x * y + (x - y) / 2 - 1


def main() -> None:
    upper_candidate = json.loads(UPPER_CANDIDATE.read_text(encoding="utf-8"))
    lower_candidate = json.loads(LOWER_CANDIDATE.read_text(encoding="utf-8"))
    lower_report = json.loads(LOWER_REPORT.read_text(encoding="utf-8"))
    upper_report = json.loads(UPPER_REPORT.read_text(encoding="utf-8"))

    upper_values = [Fraction(entry) for entry in upper_candidate["knots_decimal"]]
    nodes = len(upper_values)
    upper_grid = [Fraction(-1) + Fraction(2 * i, nodes - 1) for i in range(nodes)]
    profile = [Fraction(entry) for entry in lower_candidate["profile_decimal"]]
    amplitude = [Fraction(entry) for entry in lower_candidate["vector_decimal"]]
    dimension = len(amplitude)
    norm = sum((entry * entry for entry in amplitude), Fraction(0))
    q = Fraction(upper_report["q_pass"])
    certified_lower = Fraction(lower_report["certified_value_lower"])
    rigorous_window = q - certified_lower

    upper_digest = hashlib.sha256(
        "\n".join(upper_candidate["knots_decimal"]).encode("ascii")
    ).hexdigest()
    lower_digest = hashlib.sha256(
        "\n".join(
            lower_candidate["profile_decimal"]
            + ["--"]
            + lower_candidate["vector_decimal"]
        ).encode("ascii")
    ).hexdigest()

    def G(x: Fraction) -> Fraction:
        position = (x + 1) * Fraction(nodes - 1, 2)
        index = min(
            nodes - 2,
            max(0, position.numerator // position.denominator),
        )
        return upper_values[index] + (
            (upper_values[index + 1] - upper_values[index])
            * (x - upper_grid[index])
            / (upper_grid[index + 1] - upper_grid[index])
        )

    flow_mass = [entry * entry / norm for entry in amplitude]
    row = [Fraction(0) for _ in profile]
    column = [Fraction(0) for _ in profile]
    for index, mass in enumerate(flow_mass):
        row[index] += mass
        column[index + 1] += mass

    contact_terms = []
    for index, mass in enumerate(flow_mass):
        x = profile[index]
        y = profile[index + 1]
        residual = q - aligned_cost(x, y) - (1 - x * x) / (4 * G(x)) - G(y)
        contact_terms.append(mass * residual)
    contact_slack = sum(contact_terms, Fraction(0))

    interior_positive = Fraction(0)
    interior_neighbor = iv.mpf(0)
    true_neighbor = iv.mpf(0)
    floored_neighbor = Fraction(0)
    for index in range(1, dimension):
        radicand = 1 - profile[index] * profile[index]
        sine = iv.sqrt(box(radicand))
        neighbor_weight = amplitude[index - 1] * amplitude[index] / norm
        interior_positive += (
            row[index] * radicand / (4 * G(profile[index]))
            + column[index] * G(profile[index])
        )
        interior_neighbor += sine * box(neighbor_weight)
        true_neighbor += sine * box(neighbor_weight)
        floored_neighbor += rational_sqrt_floor(radicand) * neighbor_weight
    interior_balance = box(interior_positive) - interior_neighbor

    source_slack = column[0] * G(profile[0])
    sink_slack = column[-1] * G(profile[-1])
    endpoint_slack = source_slack + sink_slack
    sqrt_floor_tax = true_neighbor - box(floored_neighbor)

    assembled = (
        box(contact_slack)
        + interior_balance
        + box(endpoint_slack)
        + sqrt_floor_tax
    )
    closure_residual = box(rigorous_window) - assembled
    window_box = box(rigorous_window)
    contact_fraction = box(contact_slack) / window_box
    balance_fraction = interior_balance / window_box
    endpoint_fraction = box(endpoint_slack) / window_box

    gates = {
        "upper_candidate_hash_matches": (
            upper_digest == upper_candidate["sha256_newline_joined_knots"]
        ),
        "lower_candidate_hash_matches": (
            lower_digest == lower_candidate["sha256_profile_separator_vector"]
        ),
        "dimensions_and_endpoints_match": (
            dimension == 127
            and len(profile) == 128
            and profile[0] == 1
            and profile[-1] == -1
        ),
        "all_edge_contact_terms_nonnegative": min(contact_terms) >= 0,
        "contact_target_interval": bool(
            box(contact_slack).a > iv.mpf("1.90e-7").b
            and box(contact_slack).b < iv.mpf("1.92e-7").a
        ),
        "interior_balance_strictly_positive": bool(interior_balance.a > 0),
        "interior_balance_target_interval": bool(
            interior_balance.a > iv.mpf("8.1e-8").b
            and interior_balance.b < iv.mpf("8.3e-8").a
        ),
        "source_endpoint_charge_zero": source_slack == 0,
        "terminal_sink_target_interval": (
            Fraction(257, 10**10) < sink_slack < Fraction(259, 10**10)
        ),
        "sqrt_floor_tax_positive": bool(sqrt_floor_tax.a > 0),
        "sqrt_floor_tax_below_one_e_minus_fifty_eight": bool(
            sqrt_floor_tax.b < iv.mpf("1e-58").a
        ),
        "four_way_ledger_closes": bool(
            closure_residual.a <= 0 <= closure_residual.b
        ),
        "contact_is_largest_structural_bill": bool(
            box(contact_slack).a > interior_balance.b
            and box(contact_slack).a > box(endpoint_slack).b
        ),
    }
    report = {
        "status": "rigorous Bellman upper/lower gap anatomy",
        "precision_decimal_digits": 160,
        "upper_q": str(q),
        "certified_lower": str(certified_lower),
        "rigorous_window": str(rigorous_window),
        "rigorous_window_interval": endpoints(window_box),
        "contact_slack_exact": str(contact_slack),
        "contact_slack_interval": endpoints(box(contact_slack)),
        "interior_balance_slack_interval": endpoints(interior_balance),
        "terminal_sink_slack_exact": str(sink_slack),
        "terminal_sink_slack_interval": endpoints(box(sink_slack)),
        "source_endpoint_slack_exact": str(source_slack),
        "sqrt_floor_tax_interval": endpoints(sqrt_floor_tax),
        "closure_residual_interval": endpoints(closure_residual),
        "fractions_of_window": {
            "contact": endpoints(contact_fraction),
            "interior_balance": endpoints(balance_fraction),
            "terminal_sink": endpoints(endpoint_fraction),
        },
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "For the committed upper witness and lower path, the complete "
            "rigorous window equals contact slack plus interior Hellinger "
            "balance slack plus terminal sink slack plus square-root floor tax."
        ),
        "claim_boundary": (
            "This diagnoses the present certificates. It does not prove that "
            "the same proportions persist for optimized or continuum witnesses."
        ),
    }
    output = HERE / "rigorous-bellman-gap-anatomy.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
