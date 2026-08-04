#!/usr/bin/env python3
"""Guard the exact public claim boundary of the prospective v1.3 release."""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def main() -> None:
    trunc = load("certificate/independent/truncation-flux-independent.json")
    lower = load(
        "certificate/independent/dimension-necessity/post-blind-exact-audit.json"
    )
    source = load(
        "certificate/independent/dimension-necessity/source-manifest-audit.json"
    )

    gamma = 312**4
    assert gamma == 9_475_854_336
    assert int(lower["Gamma"]) == gamma
    assert lower["candidate_four_is_exact_minimum"] is True
    assert Decimal(lower["c_decimal_80"]) > 0

    r_lo, r_hi = map(Decimal, map(str, trunc["plateau_ratio_interval"]))
    log_lo, log_hi = map(Decimal, map(str, trunc["log_plateau_ratio_interval"]))
    assert Decimal(1) < r_lo < r_hi
    assert Decimal(0) < log_lo < log_hi
    assert trunc["registered_predictions_passed"] == 5
    assert trunc["registered_predictions_total"] == 5
    for fixture in trunc["symbolic_fixtures"]:
        assert fixture["exact_flux_residual"] == "0"
        assert fixture["omit_left_residual"] != "0"
        assert fixture["omit_right_residual"] != "0"

    reduction = (
        ROOT
        / "certificate/production/foundational-sprint-1237/RESULT-001-SAME-DIMENSION-REDUCTION.md"
    ).read_text(encoding="utf-8")
    manuscript = (ROOT / "paper/manuscript.tex").read_text(encoding="utf-8")
    release_notes = (ROOT / "paper/RELEASE-NOTES-v1.3.0.md").read_text(
        encoding="utf-8"
    )
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")

    assert "No dilation is used." in reduction
    assert "mixed states and binary POVMs" in reduction
    assert "\\varepsilon\\downarrow0" in manuscript
    assert "does not cover signaling, postselection" in manuscript
    assert "not yet a tagged archival release" in release_notes
    assert "version: 1.2.0" in citation
    assert "doi: 10.5281/zenodo.21782750" in citation
    assert source["all_gates_pass"] is True

    result = {
        "status": "prospective v1.3 public claim contract",
        "two_boundary_flux_independently_guarded": True,
        "constructive_rate_strictly_positive": True,
        "same_dimension_povm_quantifier_closed_without_dilation": True,
        "blind_lower_bound_constants_exactly_reconstructed": True,
        "Gamma": str(gamma),
        "kappa_decimal_80": lower["c_decimal_80"],
        "asymptotic_theta_scoped_to_epsilon_down_to_zero": True,
        "literature_scope_distinguishes_canonical_i3322_from_general_dimension_witnesses": True,
        "prospective_metadata_remains_at_v1_2": True,
        "all_gates_pass": True,
        "claim_boundary": (
            "This is a custody and public-quantifier guard. It does not replace "
            "the analytic packet proof or establish bibliographic priority."
        ),
    }
    output = HERE / "v13-claim-contract.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
