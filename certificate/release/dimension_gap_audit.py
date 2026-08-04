#!/usr/bin/env python3
"""Separate the numerical truncation illustration from the dimension theorem."""

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
PLATEAU_RATIO = 1.07809205080209208
NECESSITY_AUDIT = (
    HERE.parent / "independent" / "dimension-necessity"
    / "post-blind-exact-audit.json"
)


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
    necessity = json.loads(NECESSITY_AUDIT.read_text(encoding="utf-8"))
    assert necessity["all_gates_pass"] is True
    assert necessity["Gamma"] == "9475854336"
    output = {
        "status": "numerical truncation audit separated from analytic dimension law",
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
        "analytic_necessity": {
            "Gamma": necessity["Gamma"],
            "kappa_decimal_80": necessity["c_decimal_80"],
            "form": "q_*-Q_d >= kappa d^-4 Gamma^-d",
        },
        "observed_reading": "The centered aligned sequence illustrates the independently proved wall-truncation exponent log(R).",
        "theorem_boundary": [
            "The table itself does not bound arbitrary dimension-d strategies.",
            "The lower bound comes from the separate robust certificate proof, not a fit to these data.",
            "The exact reversal proof alone remains quantitatively unstable.",
        ],
        "open_problem": "Close the gap between the constructive exponent log(R) and the conservative necessity exponent log(Gamma).",
        "all_data_gates_pass": True,
    }
    (HERE / "dimension-gap-audit.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
