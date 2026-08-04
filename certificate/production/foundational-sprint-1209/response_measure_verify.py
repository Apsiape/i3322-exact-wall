#!/usr/bin/env python3
"""Exact and rational guards for response debt as measure asymmetry."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    wp, wm, fp, fm = sp.symbols("w_plus w_minus f_plus f_minus", real=True)
    w = sp.Matrix([wp, wm])
    K = sp.Matrix([[0, 1], [1, 0]])
    F = sp.diag(fp, fm)
    F_reflected = sp.diag(fm, fp)

    conjugacy = (K * F * K - F_reflected).applyfunc(sp.expand)
    difference = (w.T * F * w)[0] - (w.T * F_reflected * w)[0]
    polarization = (
        ((w - K * w).T * F * w)[0]
        + ((K * w).T * F * (w - K * w))[0]
    )
    polarization_residual = sp.factor(sp.expand(difference - polarization))

    rng = random.Random(1209)
    rational_checks = []
    for _ in range(500):
        w0 = Fraction(rng.randint(-20, 20), rng.randint(1, 20))
        w1 = Fraction(rng.randint(-20, 20), rng.randint(1, 20))
        f0 = Fraction(rng.randint(-20, 20), 20)
        f1 = Fraction(rng.randint(-20, 20), 20)
        norm_f = max(abs(f0), abs(f1))
        diff = abs(f0 * w0 * w0 + f1 * w1 * w1 - f1 * w0 * w0 - f0 * w1 * w1)
        norm_w_sq = w0 * w0 + w1 * w1
        defect_sq = (w0 - w1) ** 2 + (w1 - w0) ** 2
        # Square the claimed nonnegative inequality to keep exact arithmetic.
        rhs_sq = 4 * norm_f * norm_f * norm_w_sq * defect_sq
        assert diff * diff <= rhs_sq
        rational_checks.append(
            {
                "difference_squared": str(diff * diff),
                "bound_squared": str(rhs_sq),
                "passes": True,
            }
        )

    wrong_reflection = (K * F * K - F).applyfunc(sp.expand)
    report = {
        "status": "exact reflected-measure identity and rational TV-bound guard",
        "conjugacy_residual": [[str(x) for x in row] for row in conjugacy.tolist()],
        "polarization_residual": str(polarization_residual),
        "wrong_reflection_control": [
            [str(x) for x in row] for row in wrong_reflection.tolist()
        ],
        "wrong_reflection_detected": any(x != 0 for x in wrong_reflection),
        "rational_inequality_checks": len(rational_checks),
        "all_rational_checks_pass": all(row["passes"] for row in rational_checks),
        "all_gates_pass": (
            conjugacy == sp.zeros(2)
            and polarization_residual == 0
            and any(x != 0 for x in wrong_reflection)
            and all(row["passes"] for row in rational_checks)
        ),
        "claim_boundary": (
            "This verifies the reflection/polarization algebra and exact rational "
            "instances of the norm bound. Contact coupling, cocycle composition, "
            "finite-chain extraction, and dimension necessity remain separate."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "response-measure-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
