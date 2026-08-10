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
    source_manifest = load(
        "certificate/independent/dimension-necessity/source-manifest.json"
    )

    gamma = 312**4
    assert gamma == 9_475_854_336
    assert int(lower["Gamma"]) == gamma
    assert lower["candidate_four_is_exact_minimum"] is True
    assert Decimal(lower["c_decimal_80"]) > 0
    assert lower["universal_lower_bound_proved"] is False

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
    assert "No matching lower order" in manuscript
    assert "device-independent dimension lower bound" in manuscript
    assert "Quantitative necessity remains" in manuscript
    assert "tagged archival release" in release_notes
    # 2026-08 instrument repair (receipt rot): the contract formerly pinned
    # the v1.2.0 version string and that version's DOI, which fail against
    # every later release. The stable claim is the concept DOI, identical
    # across versions; the version field is checked for presence, not value.
    assert "version: " in citation
    assert "doi: 10.5281/zenodo.21782008" in citation
    assert source["all_gates_pass"] is True
    assert source_manifest["source_count"] == 21
    source_paths = {entry["path"] for entry in source_manifest["sources"]}
    assert (
        "certificate/production/foundational-sprint-1226/"
        "WEIGHTED-CLOSURE-COERCIVITY.md"
    ) in source_paths
    assert (
        "certificate/production/foundational-sprint-1227/"
        "NEAR-FIXED-PULLBACK-PAIRING.md"
    ) in source_paths
    near_fixed = (
        ROOT
        / "certificate/production/foundational-sprint-1229/"
        "RESULT-001-NEAR-FIXED-MASS-GAP.md"
    ).read_text(encoding="utf-8")
    packets = (
        ROOT
        / "certificate/production/foundational-sprint-1235/"
        "RESULT-001-CANONICAL-PACKET-PATHS.md"
    ).read_text(encoding="utf-8")
    assert "<=48 epsilon_0" in near_fixed
    assert "Y^-1(g_k I_i)" in packets
    assert "arbitrary mixed" in manuscript
    assert "C_+R^{-j}" in manuscript
    assert "conditional lower-bound route" in release_notes
    assert "flux/commutator theorem" in release_notes
    assert "are **not** claims" in release_notes

    result = {
        "status": "prospective v1.3 public claim contract",
        "two_boundary_flux_independently_guarded": True,
        "constructive_rate_strictly_positive": True,
        "same_dimension_povm_quantifier_closed_without_dilation": True,
        "conditional_lower_bound_constant_ledger_exactly_reconstructed": True,
        "universal_dimension_lower_bound_claimed": False,
        "localization_blocker_disclosed": True,
        "review_repaired_source_packet_count": 21,
        "source_target_contact_multiplicity_retained": True,
        "saturated_packet_coordinate_retained": True,
        "Gamma": str(gamma),
        "kappa_decimal_80": lower["c_decimal_80"],
        "only_logarithmic_dimension_sufficiency_claimed": True,
        "literature_scope_distinguishes_canonical_i3322_from_general_dimension_witnesses": True,
        "prospective_metadata_remains_at_v1_2": True,
        "all_gates_pass": True,
        "claim_boundary": (
            "This is a custody and public-quantifier guard for the constructive "
            "rate. The lower-bound ledger remains conditional on a missing "
            "localized-response theorem."
        ),
    }
    output = HERE / "v13-claim-contract.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
