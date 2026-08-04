#!/usr/bin/env python3
"""Verify custody and replay the complete standalone I3322 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROD = "certificate/production"
IND = "certificate/independent"
REL = "certificate/release"

REPLAY = [
    f"{PROD}/foundational-sprint-1115/plateau_hyperbolicity_certificate.py",
    f"{PROD}/foundational-sprint-1116/analytic_tail_graph_transform.py",
    f"{PROD}/foundational-sprint-1116/validated_exact_shooting_degree.py",
    f"{PROD}/foundational-sprint-1192/exact_invariant_graph_projection.py",
    f"{PROD}/foundational-sprint-1193/exact_boundary_wing.py",
    f"{PROD}/foundational-sprint-1194/inactive_outer_guard.py",
    f"{PROD}/foundational-sprint-1195/contact_covariance_verify.py",
    f"{PROD}/foundational-sprint-1195/theorem_assembly_verify.py",
    f"{PROD}/foundational-sprint-1196/cyclic_sos_verify.py",
    f"{PROD}/foundational-sprint-1197/bellman_quantum_dual_verify.py",
    f"{PROD}/foundational-sprint-1197/symmetrized_dual_guard.py",
    f"{PROD}/foundational-sprint-1197/operator_remainder_random_guard.py",
    f"{PROD}/foundational-sprint-1197/theorem_assembly_verify.py",
    f"{PROD}/foundational-sprint-1198/equality_kernel_verify.py",
    f"{PROD}/foundational-sprint-1198/theorem_assembly_verify.py",
    f"{PROD}/foundational-sprint-1199/commuting_certificate_verify.py",
    f"{PROD}/foundational-sprint-1199/theorem_assembly_verify.py",
    f"{PROD}/foundational-sprint-1200/independent_nonattainment_verify.py",
    f"{PROD}/foundational-sprint-1200/dependency_audit.py",
    f"{PROD}/foundational-sprint-1206/spatial_realization_verify.py",
    f"{PROD}/foundational-sprint-1207/truncation_flux_verify.py",
    f"{PROD}/foundational-sprint-1208/robust_response_factorization_verify.py",
    f"{PROD}/foundational-sprint-1209/response_measure_verify.py",
    f"{PROD}/foundational-sprint-1211/neutral_cycle_margin_verify.py",
    f"{PROD}/foundational-sprint-1212/matched_block_transport_verify.py",
    f"{PROD}/foundational-sprint-1214/square_root_cocycle_verify.py",
    f"{PROD}/foundational-sprint-1216/certified_weight_box_verify.py",
    f"{PROD}/foundational-sprint-1217/predecessor_derivative_interval.py",
    f"{PROD}/foundational-sprint-1217/coercivity_algebra_verify.py",
    f"{PROD}/foundational-sprint-1218/rms_packet_verify.py",
    f"{PROD}/foundational-sprint-1222/shifted_rounding_verify.py",
    f"{PROD}/foundational-sprint-1223/moving_partition_verify.py",
    f"{PROD}/foundational-sprint-1224/ordered_temporal_rank_verify.py",
    f"{PROD}/foundational-sprint-1225/two_frame_packet_verify.py",
    f"{PROD}/foundational-sprint-1226/weighted_closure_verify.py",
    f"{PROD}/foundational-sprint-1227/pullback_pairing_verify.py",
    f"{PROD}/foundational-sprint-1228/common_target_rms_verify.py",
    f"{PROD}/foundational-sprint-1229/near_fixed_gap_verify.py",
    f"{PROD}/foundational-sprint-1230/finite_rank_exit_verify.py",
    f"{PROD}/foundational-sprint-1232/inactive_quadratic_interval.py",
    f"{PROD}/foundational-sprint-1234/outer_affine_dominance_verify.py",
    f"{PROD}/foundational-sprint-1235/packet_path_ownership_verify.py",
    f"{PROD}/foundational-sprint-1237/same_dimension_extreme_verify.py",
    f"{PROD}/foundational-sprint-1238/coupled_sector_verify.py",
    f"{PROD}/foundational-sprint-1239/terminal_fork_verify.py",
    f"{PROD}/foundational-sprint-1240/schmidt_correspondence_verify.py",
    f"{PROD}/foundational-sprint-1241/marginal_volume_nogo_verify.py",
    f"{PROD}/foundational-sprint-1242/regularized_schmidt_flag_verify.py",
    f"{PROD}/foundational-sprint-1243/grid_free_contact_flag_verify.py",
    f"{PROD}/foundational-sprint-1244/mixed_flag_distance_verify.py",
    f"{PROD}/foundational-sprint-1245/resolution_scale_lift_verify.py",
    f"{PROD}/foundational-sprint-1246/operator_valued_resolution_verify.py",
    f"{PROD}/foundational-sprint-1247/order_resolution_measure_verify.py",
    f"{PROD}/foundational-sprint-1248/rectangle_reconstruction_verify.py",
    f"{PROD}/foundational-sprint-1249/response_rectangle_transport_verify.py",
    f"{PROD}/foundational-sprint-1250/event_skew_action_verify.py",
    f"{PROD}/foundational-sprint-1251/log_cut_flux_verify.py",
    f"{PROD}/foundational-sprint-1252/order_coalescence_verify.py",
    f"{PROD}/foundational-sprint-1253/order_resolution_dichotomy_verify.py",
    f"{PROD}/foundational-sprint-1254/joint_order_resolution_verify.py",
    f"{PROD}/foundational-sprint-1255/finite_monotone_skew_flow_verify.py",
    f"{PROD}/foundational-sprint-1256/charged_common_cell_verify.py",
    f"{PROD}/foundational-sprint-1257/common_cell_quarter_wall_verify.py",
    f"{PROD}/foundational-sprint-1258/monotone_fibre_transport_verify.py",
    f"{PROD}/foundational-sprint-1259/synchronized_prefix_verify.py",
    f"{PROD}/foundational-sprint-1260/upper_tail_commonization_verify.py",
    f"{PROD}/foundational-sprint-1261/sign_coherent_cells_verify.py",
    f"{PROD}/foundational-sprint-1262/upper_cap_verify.py",
    f"{PROD}/foundational-sprint-1263/two_stage_address_verify.py",
    f"{PROD}/foundational-sprint-1264/output_cell_sign_verify.py",
    f"{PROD}/foundational-sprint-1265/one_grid_four_coordinate_verify.py",
    f"{PROD}/foundational-sprint-1266/one_sided_prefix_flux_verify.py",
    f"{PROD}/foundational-sprint-1267/cancellation_preserving_localization_verify.py",
    f"{PROD}/foundational-sprint-1268/drift_sign_topology_scout.py",
    f"{PROD}/foundational-sprint-1269/shooting_atlas_drift_reconstruction.py",
    f"{PROD}/foundational-sprint-1270/exact_reverser_and_atlas_verify.py",
    f"{PROD}/foundational-sprint-1271/reciprocal_bellman_verify.py",
    f"{PROD}/foundational-sprint-1272/normalization_defect_geometry_scout.py",
    f"{PROD}/foundational-sprint-1273/log_free_drift_verify.py",
    f"{PROD}/foundational-sprint-1274/lower_envelope_characteristic_atlas.py",
    f"{PROD}/foundational-sprint-1275/morse_filtered_characteristic_atlas.py",
    f"{PROD}/foundational-sprint-1276/weighted_bellman_contraction_scout.py",
    f"{PROD}/foundational-sprint-1277/continuous_predecessor_debt_scout.py",
    f"{PROD}/foundational-sprint-1278/bellman_bottleneck_classifier.py",
    f"{PROD}/foundational-sprint-1279/bellman_grid_phase_attack.py",
    f"{PROD}/foundational-sprint-1280/algebraic_bellman_contact_verify.py",
    f"{PROD}/foundational-sprint-1281/reversed_plateau_obstruction_verify.py",
    f"{PROD}/foundational-sprint-1282/bellman_selector_collision.py",
    f"{PROD}/foundational-sprint-1283/global_amplitude_consistency_audit.py",
    f"{PROD}/foundational-sprint-1284/arb_matched_amplitude_adjudication.py",
    f"{PROD}/foundational-sprint-1285/wide_bracket_amplitude_exclusion.py",
    f"{PROD}/foundational-sprint-1231/dimension_bound_algebra_verify.py",
    f"{PROD}/foundational-sprint-1233/master_ledger_verify.py",
    f"{REL}/normalization_concordance_verify.py",
    f"{REL}/dimension_gap_audit.py",
    f"{IND}/arithmetic_selftest.py",
    f"{IND}/plateau_series_mpmath.py",
    f"{IND}/analytic_tail_mpmath.py",
    f"{IND}/shooting_miranda_mpmath.py",
    f"{IND}/global_graph_mpmath.py",
    f"{IND}/amplitude-gap/amplitude_gap_mpmath.py",
    f"{IND}/amplitude-gap/amplitude_gap_concordance.py",
    f"{IND}/verify_independent_reconstruction.py",
    f"{IND}/spatial_symbolic_verify.py",
    f"{IND}/truncation_flux_mpmath.py",
    f"{IND}/dimension-necessity/verify_source_manifest.py",
    f"{IND}/dimension-necessity/verify_constants.py",
    f"{IND}/dimension-necessity/post_blind_exact_verify.py",
    f"{REL}/v13_claim_contract_verify.py",
]

PRIVATE_MARKERS = [
    b"C:" + b"\\Infanox\\" + b"finite-contact",
    b"C:" + b"/Infanox/" + b"finite-contact",
    b"fsd" + b"/frontier/",
    b"fsd" + b"\\frontier\\",
    b"." + b"codex",
]


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def custody_bytes(path: Path, mode: str) -> bytes:
    raw = path.read_bytes()
    if mode == "raw":
        return raw
    assert mode == "canonical-lf", (path, mode)
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def check_hashes() -> tuple[int, set[str]]:
    manifest = load(f"{REL}/release-manifest.json")
    assert manifest["schema"] == 3
    frozen = set()
    for entry in manifest["files"]:
        relative = entry["path"]
        path = ROOT / relative
        assert path.is_file(), relative
        payload = custody_bytes(path, entry["hash_mode"])
        assert len(payload) == entry["canonical_bytes"], relative
        assert hashlib.sha256(payload).hexdigest() == entry["sha256"], relative
        frozen.add(relative)
    assert len(frozen) == manifest["file_count"]
    return len(frozen), frozen


def check_private_exclusion(frozen: set[str]) -> None:
    for relative in frozen:
        path = ROOT / relative
        if path.suffix.lower() in {".pdf", ".npz"}:
            continue
        payload = path.read_bytes()
        for marker in PRIVATE_MARKERS:
            assert marker not in payload, f"private marker in {relative}: {marker!r}"


def check_semantics() -> None:
    true_fields = {
        f"{PROD}/foundational-sprint-1192/exact-invariant-graph-projection.json": "all_tiles_certified",
        f"{PROD}/foundational-sprint-1193/exact-boundary-wing.json": "complete_right_wing_graph",
        f"{PROD}/foundational-sprint-1195/contact-covariance.json": "all_exact_checks_zero",
        f"{PROD}/foundational-sprint-1195/theorem-assembly.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1196/cyclic-sos.json": "all_matrix_residuals_zero",
        f"{PROD}/foundational-sprint-1197/bellman-quantum-dual.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1197/symmetrized-dual-guard.json": "passes_registered_guard",
        f"{PROD}/foundational-sprint-1197/operator-remainder-random-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1197/theorem-assembly.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1198/equality-kernel-audit.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1198/theorem-assembly.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1199/commuting-certificate-audit.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1199/theorem-assembly.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1200/dependency-audit.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1200/independent-nonattainment.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1206/spatial-realization-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1207/truncation-flux-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1208/robust-response-factorization.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1209/response-measure-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1211/neutral-cycle-margin-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1212/matched-block-transport-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1214/square-root-cocycle-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1216/certified-weight-box-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1217/predecessor-derivative-interval.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1217/coercivity-algebra-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1218/rms-packet-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1222/shifted-rounding-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1223/moving-partition-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1224/ordered-temporal-rank-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1225/two-frame-packet-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1226/weighted-closure-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1227/pullback-pairing-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1250/event-skew-action-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1251/log-cut-flux-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1252/order-coalescence-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1253/order-resolution-dichotomy-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1254/joint-order-resolution-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1255/finite-monotone-skew-flow-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1256/charged-common-cell-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1257/common-cell-quarter-wall-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1258/monotone-fibre-transport-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1259/synchronized-prefix-recovery-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1260/upper-tail-commonization-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1261/sign-coherent-cells-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1262/upper-cap-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1263/two-stage-address-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1264/output-cell-sign-coherence-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1265/one-grid-four-coordinate-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1266/one-sided-prefix-flux-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1267/cancellation-preserving-localization-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1268/drift-sign-topology-scout.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1270/exact-reverser-and-atlas-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1271/reciprocal-bellman-negative.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1273/log-free-drift-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1238/coupled-sector-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1239/terminal-fork-guard.json": "all_gates_pass",
        f"{PROD}/foundational-sprint-1232/inactive-quadratic-interval.json": "all_gates_pass",
        f"{REL}/normalization-concordance.json": "all_gates_pass",
        f"{REL}/dimension-gap-audit.json": "all_data_gates_pass",
        f"{IND}/independent-reconstruction.json": "audit_consistent",
        f"{IND}/spatial-symbolic-guard.json": "all_gates_pass",
        f"{IND}/truncation-flux-independent.json": "all_gates_pass",
        f"{IND}/dimension-necessity/source-manifest-audit.json": "all_gates_pass",
        f"{IND}/dimension-necessity/post-blind-exact-audit.json": "all_gates_pass",
        f"{REL}/v13-claim-contract.json": "all_gates_pass",
    }
    for relative, field in true_fields.items():
        assert load(relative)[field] is True, f"{relative}: {field}"
    outer = load(f"{PROD}/foundational-sprint-1194/inactive-outer-guard.json")
    assert outer["successor_monotonicity_repair"] is True
    assert outer["right_outer_contacts_excluded"] is True
    assert outer["left_outer_contacts_excluded_by_reflection"] is True
    historical_assembly = load(
        f"{PROD}/foundational-sprint-1195/theorem-assembly.json"
    )
    assert historical_assembly["historical_local_gates_pass"] is True
    assert historical_assembly["global_amplitude_compatibility"] is False
    assert historical_assembly["headline_assembly_closed"] is False
    assert historical_assembly["gap_receipt_passes"] is True
    audit = load(f"{PROD}/foundational-sprint-1200/dependency-audit.json")
    assert float(audit["q_lower_minus_quarter"]) > 0
    source_manifest = load(f"{IND}/dimension-necessity/source-manifest.json")
    assert source_manifest["source_count"] == 21
    source_paths = {entry["path"] for entry in source_manifest["sources"]}
    assert f"{PROD}/foundational-sprint-1226/WEIGHTED-CLOSURE-COERCIVITY.md" in source_paths
    assert f"{PROD}/foundational-sprint-1227/NEAR-FIXED-PULLBACK-PAIRING.md" in source_paths
    near_fixed = (
        ROOT / f"{PROD}/foundational-sprint-1229/RESULT-001-NEAR-FIXED-MASS-GAP.md"
    ).read_text(encoding="utf-8")
    packets = (
        ROOT / f"{PROD}/foundational-sprint-1235/RESULT-001-CANONICAL-PACKET-PATHS.md"
    ).read_text(encoding="utf-8")
    assert "<=48 epsilon_0" in near_fixed
    assert "Y^-1(g_k I_i)" in packets
    coupled = load(f"{PROD}/foundational-sprint-1238/coupled-sector-guard.json")
    terminal = load(f"{PROD}/foundational-sprint-1239/terminal-fork-guard.json")
    rejected_atlas = load(
        f"{PROD}/foundational-sprint-1269/shooting-atlas-drift-reconstruction.json"
    )
    normalization_scout = load(
        f"{PROD}/foundational-sprint-1272/normalization-defect-geometry-scout.json"
    )
    lower_envelope = load(
        f"{PROD}/foundational-sprint-1274/lower-envelope-characteristic-atlas.json"
    )
    morse_selector = load(
        f"{PROD}/foundational-sprint-1275/morse-filtered-characteristic-atlas.json"
    )
    weighted_contraction = load(
        f"{PROD}/foundational-sprint-1276/weighted-bellman-contraction-scout.json"
    )
    predecessor_debt = load(
        f"{PROD}/foundational-sprint-1277/continuous-predecessor-debt-scout.json"
    )
    bottleneck = load(
        f"{PROD}/foundational-sprint-1278/bellman-bottleneck-classifier.json"
    )
    phase_attack = load(
        f"{PROD}/foundational-sprint-1279/bellman-grid-phase-attack.json"
    )
    algebraic_contact = load(
        f"{PROD}/foundational-sprint-1280/algebraic-bellman-contact.json"
    )
    reversed_plateau = load(
        f"{PROD}/foundational-sprint-1281/reversed-plateau-obstruction.json"
    )
    selector_collision = load(
        f"{PROD}/foundational-sprint-1282/bellman-selector-collision.json"
    )
    amplitude_audit = load(
        f"{PROD}/foundational-sprint-1283/global-amplitude-consistency-audit.json"
    )
    arb_amplitude = load(
        f"{PROD}/foundational-sprint-1284/arb-matched-amplitude-adjudication.json"
    )
    wide_amplitude = load(
        f"{PROD}/foundational-sprint-1285/wide-bracket-amplitude-exclusion.json"
    )
    independent_amplitude = load(
        f"{IND}/amplitude-gap/amplitude-gap-mpmath.json"
    )
    amplitude_concordance = load(
        f"{IND}/amplitude-gap/amplitude-gap-concordance.json"
    )
    assert coupled["terminal_near_entry_closed"] is False
    assert coupled["universal_dimension_lower_bound_proved"] is False
    assert terminal["scalar_terminal_commonization_proved"] is False
    assert terminal["shared_factor_forms_exact"] is True
    assert rejected_atlas["naive_atlas_rejected"] is True
    assert rejected_atlas["failure_matches_known_wrong_chart"] is True
    assert normalization_scout["exact"]["all_exact_residuals_zero"] is True
    assert normalization_scout["predictions_passed"] == 2
    assert normalization_scout["predictions_total"] == 5
    assert normalization_scout["predictions"]["unique_numerical_maximum_at_zero"] is False
    assert normalization_scout["predictions"]["registered_half_q_excess_bound"] is False
    assert normalization_scout["predictions"]["tariff_zeros_coincide_with_drift_roots"] is False
    assert lower_envelope["all_gates_pass"] is False
    assert lower_envelope["gates"]["complete_coverage"] is True
    assert lower_envelope["gates"]["selected_predecessor_near_monotone"] is False
    assert len(lower_envelope["roots"]) == 15
    assert morse_selector["all_gates_pass"] is False
    assert morse_selector["gates"]["complete_coverage"] is False
    assert morse_selector["first_uncovered_coordinate"] == -0.9
    assert weighted_contraction["all_gates_pass"] is False
    assert weighted_contraction["gates"]["one_cycle_each"] is False
    assert weighted_contraction["gates"]["weighted_contraction"] is True
    assert predecessor_debt["all_gates_pass"] is False
    assert predecessor_debt["gates_passed"] == 4
    assert predecessor_debt["gates_total"] == 5
    assert predecessor_debt["gates"][
        "coarse_fine_h_uniform_disagreement_below_five_e_minus_three"
    ] is False
    assert predecessor_debt["maximum_coarse_fine_h_disagreement"] > 0.25
    assert bottleneck["all_instrument_gates_pass"] is True
    assert bottleneck["classification"] == "parabolic-contact consistent"
    assert bottleneck["dense_hull_agreement"]["maximum_F_disagreement"] < 1e-14
    assert bottleneck["dense_hull_agreement"]["discrete_owner_disagreements"] == 0
    assert bottleneck["resolutions"][-1]["minimum_gap"] < 1e-4
    assert bottleneck["resolutions"][-1]["bottleneck_multiplier"] > 1.16
    assert phase_attack["all_instrument_gates_pass"] is True
    assert phase_attack["classification"] == "phase-robust parabolic signal"
    assert phase_attack["phase_gap_range"][1] < 2.5e-4
    assert phase_attack["deep_gap_range"][1] < 1.5e-4
    assert phase_attack["deep_refinement"][-1]["minimum_gap"] < 2.2e-5
    assert algebraic_contact["all_gates_pass"] is False
    assert algebraic_contact["gates"]["all_symbolic_checks_exact"] is True
    assert algebraic_contact["gates"][
        "coefficient_strictly_above_one_point_one_six"
    ] is True
    assert algebraic_contact["gates"][
        "predecessor_and_value_match_candidate"
    ] is False
    assert algebraic_contact["numerical_identification"]["F_value_residual"] < 5e-9
    assert algebraic_contact["numerical_identification"][
        "fixed_predecessor_residual"
    ] > 1e-4
    assert reversed_plateau["all_gates_pass"] is True
    assert all(reversed_plateau["exact_checks"].values())
    assert all(reversed_plateau["dependency_gates"].values())
    assert reversed_plateau["gates"][
        "multiplier_strictly_above_one_on_branch"
    ] is True
    assert selector_collision["all_instrument_gates_pass"] is True
    assert selector_collision["classification"] == "distinct selector consistent"
    assert selector_collision["maximum_profile_discrepancy"] > 1e-3
    assert max(selector_collision["paired_root_differences"]) > 1e-3
    assert selector_collision["shooting"]["post_hoc_contact_residual"][
        "maximum_absolute_residual"
    ] > 1e-4
    assert selector_collision["boundary_iteration"]["post_hoc_contact_residual"][
        "maximum_absolute_residual"
    ] < 3e-8
    assert amplitude_audit["all_instrument_gates_pass"] is True
    assert amplitude_audit["classification"] == "persistent global mismatch"
    assert min(
        row["maximum_global_source_mismatch"] for row in amplitude_audit["orders"]
    ) > 1.6e-4
    assert max(amplitude_audit["maximum_mismatch_ratios"]) == 1.0
    assert max(
        row["maximum_raw_local_Bellman_residual"] for row in amplitude_audit["orders"]
    ) < 4e-16
    assert arb_amplitude["all_gates_pass"] is False
    assert sum(arb_amplitude["gates"].values()) == 3
    assert arb_amplitude["gates"][
        "amplitude_difference_excludes_zero_by_one_e_minus_four"
    ] is True
    assert arb_amplitude["amplitude_difference_lower_absolute_bound"] > 1.62e-4
    assert arb_amplitude["gates"][
        "t2_bracket_width_below_one_e_minus_fifteen"
    ] is False
    assert arb_amplitude["gates"]["raw_local_Bellman_equality_certified"] is False
    assert wide_amplitude["all_gates_pass"] is True
    assert all(wide_amplitude["gates"].values())
    assert wide_amplitude["amplitude_difference_lower_absolute_bound"] > 1.4e-4
    assert wide_amplitude["amplitude_difference_over_complete_bracket"][
        "contains_zero"
    ] is False
    assert independent_amplitude["all_gates_pass"] is True
    assert independent_amplitude["imports_production_engine"] is False
    assert independent_amplitude["largest_y_derivative_upper"] < -285
    assert independent_amplitude[
        "amplitude_difference_lower_absolute_bound"
    ] > 1.4e-4
    assert amplitude_concordance["all_gates_pass"] is True
    assert amplitude_concordance["gates"]["amplitude_intervals_overlap"] is True
    assert weighted_contraction["gates"]["cycle_radius_below_point_nine"] is True
    assert weighted_contraction["gates"]["weight_range_below_ten"] is True


def replay() -> None:
    for relative in REPLAY:
        print(f"[replay] {relative}", flush=True)
        subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, check=True)


def normalize_generated_receipts() -> None:
    """Keep replay output byte-stable across Windows and POSIX checkouts."""
    for path in (ROOT / "certificate").rglob("*.json"):
        raw = path.read_bytes()
        normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        if normalized != raw:
            path.write_bytes(normalized)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="rerun every load-bearing engine")
    args = parser.parse_args()
    count, frozen = check_hashes()
    check_private_exclusion(frozen)
    check_semantics()
    if args.full:
        replay()
        normalize_generated_receipts()
        check_semantics()
        post_count, post_frozen = check_hashes()
        assert post_count == count
        assert post_frozen == frozen
        check_private_exclusion(post_frozen)
    print(json.dumps({
        "status": "CUSTODY_PASS_THEOREM_GAP",
        "frozen_files_checked": count,
        "deterministic_replay_completed": args.full,
        "private_path_exclusion_checked": True,
        "constructive_dimension_rate_checked": True,
        "conditional_lower_bound_ledger_replayed_but_not_promoted": True,
        "headline_theorem_certificate_closed": False,
        "load_bearing_gap": (
            "Sprint 1285 and an independent mpmath.iv reconstruction exactly "
            "exclude global amplitude compatibility in the current Bellman assembly"
        ),
        "independence_boundary": (
            "production Arb stack plus separate mpmath.iv reconstruction and "
            "independent symbolic spatial-carrier/truncation reconstruction, "
            "plus a separately written 21-source conditional dimension-necessity "
            "reconstruction; the Bellman normalization gap is reproduced by "
            "independent Arb and mpmath.iv engines; the original chronology is "
            "not externally time-sealed and the remaining parameter-absorption "
            "gap is disclosed"
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
