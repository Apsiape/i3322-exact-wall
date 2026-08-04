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
    f"{REL}/normalization_concordance_verify.py",
    f"{REL}/dimension_gap_audit.py",
    f"{IND}/arithmetic_selftest.py",
    f"{IND}/plateau_series_mpmath.py",
    f"{IND}/analytic_tail_mpmath.py",
    f"{IND}/shooting_miranda_mpmath.py",
    f"{IND}/global_graph_mpmath.py",
    f"{IND}/verify_independent_reconstruction.py",
    f"{IND}/spatial_symbolic_verify.py",
    f"{IND}/truncation_flux_mpmath.py",
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
    assert manifest["complete_dependency_closure"] is True
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
        f"{REL}/normalization-concordance.json": "all_gates_pass",
        f"{REL}/dimension-gap-audit.json": "all_data_gates_pass",
        f"{IND}/independent-reconstruction.json": "all_gates_pass",
        f"{IND}/spatial-symbolic-guard.json": "all_gates_pass",
        f"{IND}/truncation-flux-independent.json": "all_gates_pass",
    }
    for relative, field in true_fields.items():
        assert load(relative)[field] is True, f"{relative}: {field}"
    outer = load(f"{PROD}/foundational-sprint-1194/inactive-outer-guard.json")
    assert outer["successor_monotonicity_repair"] is True
    assert outer["right_outer_contacts_excluded"] is True
    assert outer["left_outer_contacts_excluded_by_reflection"] is True
    audit = load(f"{PROD}/foundational-sprint-1200/dependency-audit.json")
    assert float(audit["q_lower_minus_quarter"]) > 0


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
    print(json.dumps({
        "status": "PASS",
        "frozen_files_checked": count,
        "deterministic_replay_completed": args.full,
        "private_corpus_dependency": False,
        "independence_boundary": (
            "production Arb stack plus separate mpmath.iv reconstruction and "
            "independent symbolic spatial-carrier and truncation reconstruction"
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
