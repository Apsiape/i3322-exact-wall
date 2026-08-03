#!/usr/bin/env python3
"""Audit what the finite carrier data do and do not prove about dimension."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
Q_STAR = 0.250875384513976536
DATA = [
    (31, 0.250492717483438),
    (63, 0.250850779989507),
    (127, 0.250875195790122),
    (191, 0.250875382981378),
    (255, 0.250875384501519),
]
PLATEAU_RATIO = 1.078092050202774


def main() -> None:
    n = np.array([row[0] for row in DATA], dtype=float)
    gaps = np.array([Q_STAR - row[1] for row in DATA], dtype=float)
    assert np.all(gaps > 0)
    assert np.all(gaps[1:] < gaps[:-1])

    exp_slope, exp_intercept = np.polyfit(n, np.log(gaps), 1)
    asymptotic_slopes = [
        math.log(gaps[i] / gaps[i + 1]) / (n[i + 1] - n[i])
        for i in range(len(n) - 1)
    ]
    output = {
        "status": "numerical convergence audit; no quantitative dimension theorem",
        "q_star": Q_STAR,
        "data": [
            {"dimension": int(dim), "value": value, "gap": Q_STAR - value}
            for dim, value in DATA
        ],
        "global_log_linear_fit": {
            "log_gap_slope_per_dimension": float(exp_slope),
            "intercept": float(exp_intercept),
        },
        "successive_log_gap_rates": asymptotic_slopes,
        "plateau_log_ratio": math.log(PLATEAU_RATIO),
        "observed_reading": "The centered aligned sequence is consistent with gap Theta(R^{-n}), R approximately the positive plateau ratio.",
        "theorem_boundary": [
            "The data do not upper-bound arbitrary dimension-d strategies.",
            "The nonattainment proof uses exact finite support reversal and is not quantitatively stable as written.",
            "No device-independent lower bound on dimension is claimed.",
        ],
        "next_lemma": "Prove a robust finite-support reversal theorem or a dimension-d defect bound for the three PSD remainders.",
        "all_data_gates_pass": True,
    }
    (HERE / "dimension-gap-audit.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
