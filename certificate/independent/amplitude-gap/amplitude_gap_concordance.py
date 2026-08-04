#!/usr/bin/env python3
"""Post-verdict concordance of production Arb and independent mpmath.iv receipts."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE.parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def overlap(a: dict, b: dict) -> bool:
    return max(a["lower"], b["lower"]) <= min(a["upper"], b["upper"])


def main() -> None:
    independent = load(HERE / "amplitude-gap-mpmath.json")
    production = load(
        CERTIFICATE
        / "production"
        / "foundational-sprint-1285"
        / "wide-bracket-amplitude-exclusion.json"
    )
    independent_gap = independent[
        "amplitude_difference_over_complete_bracket"
    ]
    production_gap = production[
        "amplitude_difference_over_complete_bracket"
    ]
    gates = {
        "production_passed": production["all_gates_pass"],
        "independent_passed": independent["all_gates_pass"],
        "production_excludes_zero": not production_gap["contains_zero"],
        "independent_excludes_zero": not independent_gap["contains_zero"],
        "amplitude_intervals_overlap": overlap(production_gap, independent_gap),
        "lower_endpoints_agree_below_one_e_minus_nine": (
            abs(production_gap["lower"] - independent_gap["lower"]) < 1e-9
        ),
        "upper_endpoints_agree_below_one_e_minus_nine": (
            abs(production_gap["upper"] - independent_gap["upper"]) < 1e-9
        ),
    }
    report = {
        "status": "post-verdict amplitude-gap concordance",
        "production_backend": "python-flint Arb",
        "independent_backend": "mpmath.iv and independent iv_core",
        "production_interval": production_gap,
        "independent_interval": independent_gap,
        "endpoint_disagreements": {
            "lower": abs(production_gap["lower"] - independent_gap["lower"]),
            "upper": abs(production_gap["upper"] - independent_gap["upper"]),
        },
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Concordance confirms the diagnosed certificate gap across two "
            "interval implementations; it does not determine a corrected optimum."
        ),
    }
    output = HERE / "amplitude-gap-concordance.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
