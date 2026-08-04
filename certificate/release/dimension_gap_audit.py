#!/usr/bin/env python3
"""Audit the truncation data and keep the failed converse explicitly typed."""

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
        "status": "numerical truncation audit separated from conditional necessity ledger",
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
        "conditional_necessity_ledger": {
            "Gamma": necessity["Gamma"],
            "kappa_decimal_80": necessity["c_decimal_80"],
            "form": "q_*-Q_d >= kappa d^-4 Gamma^-d",
            "proved": False,
            "blocker": "uncontrolled near-fixed response localization/commutator term",
        },
        "observed_reading": "The centered aligned sequence illustrates the independently proved wall-truncation exponent log(R).",
        "theorem_boundary": [
            "The table itself does not bound arbitrary dimension-d strategies.",
            "No universal lower bound is presently proved by the packet campaign.",
            "The exact reversal proof alone remains quantitatively unstable.",
        ],
        "open_problem": "Prove a localized-response/flux theorem or find a different quantitative necessity argument.",
        "all_data_gates_pass": True,
    }
    (HERE / "dimension-gap-audit.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
