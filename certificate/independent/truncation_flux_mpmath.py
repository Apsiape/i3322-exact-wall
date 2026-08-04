#!/usr/bin/env python3
"""Independent symbolic/interval reconstruction of wall truncation flux."""

from __future__ import annotations

import json
from pathlib import Path

from mpmath import iv
import sympy as sp


HERE = Path(__file__).resolve().parent
PLATEAU = HERE / "plateau-series-mpmath.json"


def symbolic_fixture(size: int, left: int, right: int) -> dict[str, object]:
    q = sp.symbols("q", real=True)
    lam = sp.symbols(f"l0:{size}", positive=True)
    coupling = sp.symbols(f"h1:{size}", positive=True)

    diagonal = []
    for index in range(size):
        incoming = coupling[index - 1] * lam[index - 1] if index > 0 else 0
        outgoing = coupling[index] * lam[index + 1] if index + 1 < size else 0
        diagonal.append(sp.factor(q - (incoming + outgoing) / lam[index]))

    norm = sum(lam[index] ** 2 for index in range(left, right + 1))
    principal = sum(
        diagonal[index] * lam[index] ** 2 for index in range(left, right + 1)
    ) + 2 * sum(
        coupling[index - 1] * lam[index - 1] * lam[index]
        for index in range(left + 1, right + 1)
    )
    left_flux = coupling[left - 1] * lam[left - 1] * lam[left] if left > 0 else 0
    right_flux = (
        coupling[right] * lam[right] * lam[right + 1]
        if right + 1 < size
        else 0
    )
    residual = sp.factor(q * norm - principal - left_flux - right_flux)
    omit_left = sp.factor(q * norm - principal - right_flux)
    omit_right = sp.factor(q * norm - principal - left_flux)
    if residual != 0:
        raise AssertionError((size, left, right, residual))
    if left_flux != 0 and omit_left == 0:
        raise AssertionError("left-boundary control failed")
    if right_flux != 0 and omit_right == 0:
        raise AssertionError("right-boundary control failed")
    return {
        "size": size,
        "interval": [left, right],
        "exact_flux_residual": str(residual),
        "omit_left_residual": str(omit_left),
        "omit_right_residual": str(omit_right),
    }


def interval_endpoints(value) -> list[float]:
    return [float(value.a), float(value.b)]


def main() -> None:
    fixtures = [
        symbolic_fixture(5, 1, 3),
        symbolic_fixture(6, 1, 4),
        symbolic_fixture(7, 2, 4),
        symbolic_fixture(8, 2, 6),
    ]

    c, r, q = sp.symbols("c r q", real=True)
    sine = sp.sqrt(1 - c**2)
    ratio = sine * (2 * c - 1) / ((1 - c) * (2 * c + 1))
    q_branch = (4 * c**4 - 5 * c**2 + 2) / (4 * c**2 - 1)
    stationarity_1 = sp.factor(q - (c**2 - 1 + sine * (r + 1 / r) / 2))
    stationarity_2 = sp.factor(
        (1 + 2 * c) * r**2 - (1 - 2 * c) - 2 * c * r / sine
    )
    ratio_residuals = [
        sp.simplify(stationarity_1.subs({r: ratio, q: q_branch})),
        sp.simplify(stationarity_2.subs(r, ratio)),
    ]
    if ratio_residuals != [0, 0]:
        raise AssertionError(ratio_residuals)

    plateau = json.loads(PLATEAU.read_text(encoding="utf-8"))
    c_interval = plateau["c_interval"]
    c_iv = iv.mpf(c_interval)
    ratio_iv = iv.sqrt(1 - c_iv * c_iv) * (2 * c_iv - 1) / (
        (1 - c_iv) * (2 * c_iv + 1)
    )
    log_iv = iv.log(ratio_iv)
    ratio_box = interval_endpoints(ratio_iv)
    log_box = interval_endpoints(log_iv)
    expected_ratio = 1.07809205080209208
    expected_log = 0.07519285919570202

    scores = {
        "P1_exact_two_boundary_flux": all(
            row["exact_flux_residual"] == "0" for row in fixtures
        ),
        "P2_wrong_boundary_controls": all(
            row["omit_left_residual"] != "0" and row["omit_right_residual"] != "0"
            for row in fixtures
        ),
        "P3_ratio_derived_symbolically": ratio_residuals == [0, 0],
        "P4_ratio_enclosure": (
            1 < ratio_box[0] <= expected_ratio <= ratio_box[1]
        ),
        "P5_log_enclosure": (
            0 < log_box[0] <= expected_log <= log_box[1]
        ),
    }
    report = {
        "status": "independent symbolic and mpmath.iv truncation reconstruction",
        "imports_production_engine": False,
        "symbolic_fixtures": fixtures,
        "plateau_ratio_formula": str(ratio),
        "plateau_ratio_residuals": [str(value) for value in ratio_residuals],
        "source_c_interval": c_interval,
        "plateau_ratio_interval": ratio_box,
        "log_plateau_ratio_interval": log_box,
        "registered_prediction_scores": scores,
        "registered_predictions_passed": sum(bool(value) for value in scores.values()),
        "registered_predictions_total": len(scores),
        "all_gates_pass": all(scores.values()),
        "claim_boundary": (
            "This reconstructs the exact finite-section identity and the "
            "certified plateau exponent input independently. It proves no "
            "device-independent dimension lower bound."
        ),
    }
    (HERE / "truncation-flux-independent.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
