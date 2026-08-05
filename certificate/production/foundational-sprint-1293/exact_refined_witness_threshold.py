#!/usr/bin/env python3
"""Exact threshold search for the 25,601-knot Bellman witness."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRODUCTION = HERE.parent
CANDIDATE = HERE / "refined-bellman-candidate.json"
LOWER_REPORT = PRODUCTION / "foundational-sprint-1292/exact-dimension-255-lower-bound.json"
OPERATOR_REPORT = PRODUCTION / "foundational-sprint-1287/bellman-operator-weld.json"
BASE_ENGINE = PRODUCTION / "foundational-sprint-1290/exact_fixed_witness_threshold.py"
SCALE = 10**15
SEARCH_LOW = 250_875_380_000_000
SEARCH_HIGH = 250_875_500_000_000


def load_exact_engine():
    spec = importlib.util.spec_from_file_location("fixed_threshold_engine", BASE_ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load exact fixed-threshold engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    engine = load_exact_engine()
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    values = [Fraction(value) for value in candidate["knots_decimal"]]
    nodes = candidate["nodes"]
    grid = [Fraction(-1) + Fraction(2 * index, nodes - 1) for index in range(nodes)]
    digest = hashlib.sha256(
        "\n".join(candidate["knots_decimal"]).encode("ascii")
    ).hexdigest()
    pieces, retained_lines = engine.build_pieces(grid, values)

    low = SEARCH_LOW
    high = SEARCH_HIGH
    low_pass, _, _ = engine.check_threshold(Fraction(low, SCALE), pieces)
    high_pass, _, _ = engine.check_threshold(Fraction(high, SCALE), pieces)
    if low_pass or not high_pass:
        raise RuntimeError("registered refined threshold bracket is invalid")
    evaluations = 2
    while low + 1 < high:
        middle = (low + high) // 2
        passed, _, _ = engine.check_threshold(Fraction(middle, SCALE), pieces)
        evaluations += 1
        if passed:
            high = middle
        else:
            low = middle

    q_pass = Fraction(high, SCALE)
    q_fail = Fraction(low, SCALE)
    pass_gate, pass_minimum, pass_receipt = engine.check_threshold(q_pass, pieces)
    fail_gate, fail_minimum, fail_receipt = engine.check_threshold(q_fail, pieces)
    evaluations += 2

    lower = Fraction(
        json.loads(LOWER_REPORT.read_text(encoding="utf-8"))["certified_value_lower"]
    )
    operator = json.loads(OPERATOR_REPORT.read_text(encoding="utf-8"))
    window = q_pass - lower
    gates = {
        "candidate_iteration_completed_before_cap": (
            candidate["iterations"] < candidate["maximum_iterations"]
        ),
        "candidate_iteration_reached_tolerance": (
            candidate["final_delta"] < candidate["tolerance"]
        ),
        "candidate_hash_matches": (
            digest == candidate["sha256_newline_joined_knots"]
        ),
        "candidate_shape_exact": (
            nodes == 25_601
            and len(values) == nodes
            and grid[0] == -1
            and grid[-1] == 1
        ),
        "all_candidate_knots_positive": min(values) > 0,
        "registered_lower_grid_point_fails": not fail_gate,
        "returned_grid_point_passes": pass_gate,
        "adjacent_grid_points": high == low + 1,
        "upper_endpoint_below_point_25087542": (
            q_pass < Fraction(25087542, 100_000_000)
        ),
        "rigorous_window_below_four_e_minus_eight": (
            0 < window < Fraction(4, 100_000_000)
        ),
        "pass_minimum_nonnegative": pass_minimum >= 0,
        "fail_minimum_negative": fail_minimum < 0,
        "abstract_operator_weld_unchanged_and_valid": operator["all_gates_pass"],
    }
    report = {
        "status": "exact 25,601-knot Bellman threshold on the 10^-15 grid",
        "q_pass": str(q_pass),
        "q_pass_decimal": float(q_pass),
        "q_fail_predecessor": str(q_fail),
        "q_fail_predecessor_decimal": float(q_fail),
        "threshold_resolution": "1/1000000000000000",
        "exact_threshold_evaluations": evaluations,
        "piecewise_linear_knots": nodes,
        "upper_envelope_lines_retained": retained_lines,
        "common_intervals_checked_per_evaluation": len(pieces),
        "pass_minimum_numerator": str(pass_minimum),
        "fail_minimum_numerator": str(fail_minimum),
        "pass_worst_receipt": pass_receipt,
        "fail_worst_receipt": fail_receipt,
        "finite_tensor_lower": str(lower),
        "rigorous_window_width": str(window),
        "rigorous_window_width_decimal": float(window),
        "improvement_over_6401_knot_upper": str(
            Fraction(50175098917669, 200000000000000) - q_pass
        ),
        "exact_engine_reused": BASE_ENGINE.relative_to(HERE.parents[2]).as_posix(),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The committed 25,601-knot rational witness certifies the displayed "
            "commuting-projective I3322 upper bound."
        ),
        "claim_boundary": (
            "Sharp only on the 10^-15 grid for this fixed PL witness. Does not "
            "identify the exact optimum or restore historical corollaries."
        ),
    }
    output = HERE / "exact-refined-witness-threshold.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
