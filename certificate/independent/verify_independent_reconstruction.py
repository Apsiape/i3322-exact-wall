#!/usr/bin/env python3
"""Assemble seven mathematical gates plus import hygiene, then compare."""

from __future__ import annotations

import ast
import json
import re
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def forbidden_imports():
    failures = []
    for path in HERE.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            else:
                continue
            for name in names:
                if name == "flint" or name.startswith("flint."):
                    failures.append({"file": path.name, "module": name})
    return failures


def main() -> None:
    arithmetic = load(HERE/"arithmetic-selftest.json")
    plateau = load(HERE/"plateau-series-mpmath.json")
    analytic = load(HERE/"analytic-tail-mpmath.json")
    shooting = load(HERE/"shooting-miranda-mpmath.json")
    graph = load(HERE/"global-graph-mpmath.json")
    forbidden = forbidden_imports()

    gates = {
        "independent_arithmetic": arithmetic["all_gates_pass"],
        "plateau_and_degree12_series": plateau["all_gates_pass"],
        "analytic_graph_transform": analytic["all_gates_pass"],
        "miranda_shooting_zero": shooting["all_gates_pass"],
        "central_invariant_graph": graph["central"]["all_gates_pass"],
        "boundary_wing": graph["boundary_wing"]["all_gates_pass"],
        "inactive_exterior": graph["inactive_exterior"]["all_gates_pass"],
        "no_forbidden_interval_import": not forbidden,
    }
    independent_pass = all(gates.values())

    # Comparison is deliberately delayed until after the independent verdict.
    production = load(ROOT/"certificate/production/foundational-sprint-1116/validated-exact-shooting-degree.json")
    production_q_text = production["rectangle"]["Q"]
    independent_q = shooting["rectangle"]["Q"]
    match = re.fullmatch(r"\[([0-9.]+) \+/- ([0-9.e-]+)\]", production_q_text)
    assert match
    production_center, production_radius = Decimal(match.group(1)), Decimal(match.group(2))
    production_bounds = [production_center-production_radius, production_center+production_radius]
    independent_bounds = [Decimal(independent_q[0]), Decimal(independent_q[1])]
    q_intervals_overlap = independent_bounds[0] <= production_bounds[1] and production_bounds[0] <= independent_bounds[1]
    displayed = Decimal("0.250875384513976536")
    display_quantum = Decimal("1e-18")
    independent_rounded = [
        value.quantize(display_quantum, rounding=ROUND_HALF_EVEN)
        for value in independent_bounds
    ]
    q_decimal_agreement = independent_rounded == [displayed, displayed]
    result = {
        "status": "independent reconstruction of the complete computer-assisted Bellman input",
        "independence_contract": {
            "interval_backend": "mpmath.iv",
            "complex_backend": "locally implemented rectangular intervals",
            "production_modules_imported": False,
            "forbidden_imports": forbidden,
            "comparison_performed_after_independent_verdict": True,
        },
        "gates": gates,
        "gate_score": f"{sum(gates.values())}/{len(gates)}",
        "all_gates_pass": independent_pass,
        "post_verdict_comparison": {
            "production_q_receipt": production_q_text,
            "production_q_decimal_bounds": [str(value) for value in production_bounds],
            "independent_q_directed_bounds": independent_q,
            "intervals_overlap": q_intervals_overlap,
            "independent_bounds_round_to_displayed_decimal": q_decimal_agreement,
            "rounding_rule": "round-half-even to 18 digits after the decimal point",
            "analytic_correction_ratio_independent_over_production": analytic["original_coordinate_correction_upper"]/2.213018857104665e-25,
        },
        "claim_boundary": "This is method-independent interval reconstruction of every computer-assisted Bellman gate. Analytic operator and nonattainment proofs remain exact-paper arguments with separate symbolic engines.",
    }
    (HERE/"independent-reconstruction.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert independent_pass and q_decimal_agreement and q_intervals_overlap


if __name__ == "__main__":
    main()
