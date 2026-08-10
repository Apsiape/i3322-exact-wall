#!/usr/bin/env python3
"""U1G live-authority hygiene guard (scope-coincidence IMPLEMENTED).

Checks (all fail-capable; guard exits nonzero on any failure):
  H0 SCOPE COINCIDENCE: the authored scan set is GENERATED from the
     filesystem (proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md +
     authority/*.md glob + STATUS_U1E.json) and cross-checked against
     the banner's LIVE CHAIN "AUTHORED" list, parsed from the banner
     text. Any mismatch in either direction — a banner-listed file
     missing on disk, or a file on disk the banner does not list —
     FAILS. (Round-3 integrity finding 1 / blocker 1.)
  RB RETRACTION-BLOCK CONTENT VALIDATION: every marked block in every
     live file must contain retraction language (retract/kill/
     superseded/historical) and must NOT contain live-assertion
     markers; the U1G proof must contain NO retraction block at all
     (banner rule). Only validated blocks are exempt from scans.
     (Round-3 integrity finding 5 / blocker 2.)
  H1 killed literals absent from live text: authored files get the
     full scan; dependency copies get the killed-IDENTITY scan only
     (historical scouts inside sealed sources are provenance content).
  H2 kill-#12 route tokens absent from EVERY authored live file
     outside validated blocks, and absent from the U1G proof entirely.
     (Round-3 integrity finding 6.)
  H3 required U1G proof content present (whitespace-normalized).
  H4 ledger carries the kill declarations and the custody entry.
  H5 REAL PREDECESSOR ANCHORS, PARSED NOT HAND-MAINTAINED: the
     certificate hashes (proof §1a) and Lean kernel hashes (proof §1b)
     are PARSED from the proof text and re-verified against the public
     trees; the five dependency copies are re-hashed and their digests
     must appear verbatim in the proof. HARD-FAILS if either anchored
     tree is absent — no soft SKIP. (Round-3 integrity finding 7.)
  H6 dangling-pointer check: every dependencies/, audit_archive/,
     artifacts/ path named in an authored live file must exist.
     (Round-3 finding F16.)

INSTRUMENT REPAIR 2026-08-10 (public-window defect G6 — portability,
no check weakened):
  * The public-repo root was a hard-coded machine-local absolute path.
    It is now DERIVED: the guard walks up from __file__ for the public
    repo's own root signature, so any clone works. An explicit
    I3322_PUBLIC_ROOT override exists for the ONE case where walk-up
    cannot work — the injection self-test, which runs a COPY of this
    guard from a system temp directory outside the repo.
  * The external SEALED-SOURCE anchors used by H7 (six of the seven
    dependency sources) and by H10 (the blind-batch-v19 verdict
    originals) were hard-coded absolute paths into the author's
    PRIVATE tree; they are unreachable for any external cloner, so
    those comparisons could never run off this machine. They now
    resolve under the environment variable I3322_PRIVATE_SOURCE_ROOT.
    When it is unset or the tree is absent, ONLY the external
    comparisons are skipped, each with a printed
    "[MACHINE-LOCAL SKIP]" disclosure; every in-repo check still runs
    and still HARD-FAILS.
  * H7's in-repo half (copy vs the EXPECTED_DIGESTS registry pinned in
    this file) was already fail-capable without the external tree, so
    it is unchanged and still hard-fails.
  * H10 previously had NO in-repo half: with the private originals
    absent it would have been reduced to nothing. So H10 now carries
    VERDICT_CUSTODY_DIGESTS — the same pinned-digest pattern H7
    already uses (a digest change requires a guard edit that the
    manifest, git and the gate all see). That half ALWAYS hard-fails;
    the byte-for-byte comparison against the blind-batch originals is
    the part that becomes machine-local. Injection I30 (archived
    verdict rewritten, manifest re-pinned) therefore still fires with
    no private tree present.
  * No private-tree path literal remains in this file.
"""

from __future__ import annotations
import hashlib
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
PROOF = HERE / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
BANNER = HERE / "authority" / "00_AUTHORITY_BANNER_U1E.md"

# --- PUBROOT, derived (repair 2026-08-10) -----------------------------
# Signature files that identify the public repository root. Walk-up
# wins over the environment override so the genuine enclosing clone is
# always preferred; the override only serves a guard copy that has been
# lifted out of the tree (the injection self-test sandbox).
_PUBROOT_SIGNATURE = ("certificate/release/verify_release.py",
                      "lean/I3322Kernel")


def _looks_like_pubroot(cand: Path) -> bool:
    return all((cand / rel).exists() for rel in _PUBROOT_SIGNATURE)


def _resolve_pubroot() -> Path:
    for cand in Path(__file__).resolve().parents:
        if _looks_like_pubroot(cand):
            return cand
    env = os.environ.get("I3322_PUBLIC_ROOT")
    if env and _looks_like_pubroot(Path(env)):
        return Path(env)
    print("FAIL cannot locate the public repository root from "
          f"{Path(__file__).resolve()} (no ancestor carries "
          f"{_PUBROOT_SIGNATURE} and I3322_PUBLIC_ROOT is unset or "
          f"does not point at a public tree)")
    sys.exit(1)


PUBROOT = _resolve_pubroot()
CERT = PUBROOT / "certificate" / "production" / \
    "theorem-S-spatial-attainment-at-S"
LEAN = PUBROOT / "lean" / "I3322Kernel"

# --- Private sealed-source root, environment-supplied (repair
# 2026-08-10). Unset/absent => the EXTERNAL comparisons below are
# skipped with a printed disclosure; nothing in-repo is relaxed.
_PRIV_ENV = os.environ.get("I3322_PRIVATE_SOURCE_ROOT")
PRIVATE_ROOT = Path(_PRIV_ENV) if _PRIV_ENV else None
if PRIVATE_ROOT is not None and not PRIVATE_ROOT.is_dir():
    PRIVATE_ROOT = None
SKIP_BANNER = (
    "[MACHINE-LOCAL SKIP] external sealed-source comparison requires "
    "the author's private tree (set I3322_PRIVATE_SOURCE_ROOT); the "
    "in-repo digest-registry checks below cover the shipped copies")

# H7 digest registry (round-5 integrity finding 1): the EXPECTED
# sha256 of every dependency copy, pinned IN THIS GUARD's code — so a
# lockstep tamper of copy + external source (injection N1c) fails
# against these digests, which change only with a guard edit that the
# manifest, git, and the gate all see.
EXPECTED_DIGESTS = {
    "ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md":
        "1ed80a067d3afcbd04c58a8792f1c98ae83aff0d783947496f81b7db4b4472b4",
    "G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md":
        "6dbb19c7d00a9fd5d0535b896ab6565f226ce6ae6fab381ea6f71a5f3fa9598a",
    "RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md":
        "908874eed6fe673c80a4c4ac1481809f62b8f6d716556de34228b8fb4b07c8f9",
    "ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md":
        "d486e3e33f83afcea41a68b1930f2548e399eaa584e371c7ea03dc619df054bb",
    "THEOREM_S_SIGNED_PUBLIC_STATEMENT.md":
        "7978e7caad9ce9f5c1f47404ca0f183c15a8b378a005b3fc696eeedafe4ae900",
    "08_ENDPOINT_RECEIPT_PROVENANCE.md":
        "ec4ffeadf81a33553dfd3a215c2ed4cacaf72f0d226be1068838344183dd4fdc",
    "REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md":
        "589bb7d804984910cff814a3a7513a94634ce37b8c0e7f2cc49a281bb8b0f216",
}

# H7 external-source paths (byte-identity is checked against BOTH the
# digest registry above and these sealed locations). Six of the seven
# live in the author's PRIVATE tree; their locations are pinned here as
# paths RELATIVE to I3322_PRIVATE_SOURCE_ROOT (repair 2026-08-10 — the
# relative structure is still pinned evidence, only the machine-local
# prefix moved to the environment). The seventh source is public and
# in-repo, so it is anchored unconditionally.
_V281_REL = "I3322_V28_1_LOWER_BOUND_FINAL_FIXES_BUNDLE_2026-08-06"
_CONS_REL = "i3322_consolidated_promotion_bundle"
_BLIND_REL = "fsd/papers/i3322-exact-wall/blind-batch-v19"
PRIVATE_SOURCE_RELPATHS = {
    "ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md":
        f"{_V281_REL}/dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md",
    "G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md":
        f"{_V281_REL}/dependencies/"
        "G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md",
    "RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md":
        f"{_V281_REL}/dependencies/"
        "RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md",
    "ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md":
        f"{_V281_REL}/upper_artifacts/"
        "ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md",
    "08_ENDPOINT_RECEIPT_PROVENANCE.md":
        f"{_CONS_REL}/new_docs/08_ENDPOINT_RECEIPT_PROVENANCE.md",
    "REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md":
        f"{_V281_REL}/dependencies/"
        "REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md",
}
# Always anchorable: source lives in this repository.
EXTERNAL_SOURCES = {
    "THEOREM_S_SIGNED_PUBLIC_STATEMENT.md":
        CERT / "THEOREM_S_SIGNED_PUBLIC_STATEMENT.md",
}
if PRIVATE_ROOT is not None:
    for _name, _rel in PRIVATE_SOURCE_RELPATHS.items():
        EXTERNAL_SOURCES[_name] = PRIVATE_ROOT / _rel

# H10 IN-REPO custody registry (repair 2026-08-10): the sha256 of the
# three early-round verdict copies whose byte-identity against the
# blind-batch-v19 originals H10 asserts. Pinned here for the same
# reason EXPECTED_DIGESTS is — so an evidence rewrite with the bundle
# manifest re-pinned (injection I30) still fires when the external
# originals are unreachable. Changing one requires a guard edit that
# the manifest, git and the gate all see.
VERDICT_CUSTODY_DIGESTS = {
    "VERDICT-U1-AUDITOR-1-PROOF.md":
        "935e2759cc97b8619c945dea05dec81c1146439ce6af102535b29b05ddb968e0",
    "VERDICT-U1-AUDITOR-2-INTEGRITY.md":
        "08a173aeaad05d32274ccc20668750b7d7f6b9929eaa4b125dd326b20c1559c8",
    "VERDICT-U1E-AUDITOR-2-INTEGRITY.md":
        "9531639cba4317f890ff7bc6003f79a37664a020b11d68082010f625ef13f0cc",
}

# RB registry (round-4 finding 3; round-5 finding 2): the exact set
# of legitimate retraction blocks, pinned by file AND by the sha256 of
# each block's whitespace-normalized CONTENT. Editing the interior of
# a registered block (injection N3), adding a block, or placing one in
# a copy all FAIL. Changing a legitimate block requires updating this
# registry in the same commit — visible to manifest, git, and gate.
# Filled by tools/regenerate at seal; verified here.
RB_CONTENT_DIGESTS = {
    "authority/00_AUTHORITY_BANNER_U1E.md": ["560d3a9c2f4bc21d354a6f137401e116b2037b8e268893e0cdc2bc58a3af52dc"],
    "authority/U1E_CORRECTION_LEDGER.md": [
        "ab973451747db0a45fd4658709bb27fff0b7b22657c33ae78fb39e15248f3133", "9132fc7f7056af422eb08608e8b1e6ec65bb10cd26739bd79aa5da27280f9061", "03fbf68e4b1beda31f9c0b90a93b80c7ed0407df117031647b53cbe3da2aec30"],
}

# FULL FILENAME ALLOWLIST (round-5 blocker 3) — the complete pinned
# file set of the sealed bundle, regenerated at each seal.
# BEGIN-ALLOWED-FILES
ALLOWED_FILES = [
    "PROMOTION_RECORD.md",
    "README.md",
    "STATUS_U1E.json",
    "U1_TO_U1E_CHANGES.md",
    "artifacts/GUARD_DATA_PROVENANCE.md",
    "artifacts/commission_history/CESARO_MULTIPLIER_IDENTIFICATION_TWO_ROUTES.md",
    "artifacts/commission_history/guard_kappa_bracket_retrodiction.RETIRED.py",
    "artifacts/small_d_demoted/DISCLOSURE.md",
    "artifacts/small_d_demoted/GUARD_SMALL_D_STDOUT.txt",
    "artifacts/small_d_demoted/SMALL_D_TRUNCATION_SOURCE_DATA.json",
    "artifacts/small_d_demoted/guard_small_d_endpoint_projector_truncation.py",
    "artifacts/small_d_demoted/small_d_endpoint_projector_truncation_results.json",
    "audit_archive/AXIOMCHECK_RECEIPT_2026-08-07.txt",
    "audit_archive/DISTORTED_RETURN_QUARTER_CEILING_CURRENT_V22.KILL_PROVENANCE.md",
    "audit_archive/G1_PROMOTED_UPPER_RECEIPT.EXTRACT.SUPERSEDED.md",
    "audit_archive/SELF_AUDIT_U1.SUPERSEDED.md",
    "audit_archive/SOURCE_HASH_ANCHORS.json",
    "audit_archive/TRUNCATION_UPPER_RECEIPT.EXTRACT.SUPERSEDED.md",
    "audit_archive/U1_GUARD_RESULTS.HISTORICAL.txt",
    "audit_archive/VERDICT-U1-AUDITOR-1-PROOF.md",
    "audit_archive/VERDICT-U1-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1E-AUDITOR-1-PROOF.md",
    "audit_archive/VERDICT-U1E-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1F-AUDITOR-1-PROOF.md",
    "audit_archive/VERDICT-U1F-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1G-AUDITOR-1-PROOF.md",
    "audit_archive/VERDICT-U1G-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1G-R5-AUDITOR-1-PROOF.md",
    "audit_archive/VERDICT-U1G-R5-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1G-R6-AUDITOR-1-PROOF-DELTA.md",
    "audit_archive/VERDICT-U1G-R6-AUDITOR-2-INTEGRITY.md",
    "audit_archive/VERDICT-U1G-R7-AUDITOR-1-PROOF-DELTA.md",
    "audit_archive/VERDICT-U1G-R7-AUDITOR-2-INTEGRITY.md",
    "audit_diff/V28_1_LEDGER_TO_U1_LEDGER.patch",
    "authority/00_AUTHORITY_BANNER_U1E.md",
    "authority/PROMOTED_LOWER_RATE_RECEIPT.md",
    "authority/U1E_CORRECTION_LEDGER.md",
    "authority/U1E_DEPENDENCY_GRAPH.md",
    "dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md",
    "dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md",
    "dependencies/ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md",
    "dependencies/G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md",
    "dependencies/RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md",
    "dependencies/REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md",
    "dependencies/THEOREM_S_SIGNED_PUBLIC_STATEMENT.md",
    "guards/guard_a8_strictness.py",
    "guards/guard_live_upper_authority_hygiene.py",
    "guards/guard_second_engine_projectors.py",
    "guards/guard_selftest_injection.py",
    "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md",
    "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1E.md",
    "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1F.md",
    "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
]
# END-ALLOWED-FILES

KILLED_AUTHORED = ["g(1)g(-1)=0", "g(1) g(-1) = 0", "13.299", "13.426"]
KILLED_COPIES = ["g(1)g(-1)=0 holds", "g(1) g(-1) = 0 holds"]
SHORTCUT = ["square summability gives", "square-summability gives"]
KILL_ROUTE = ["q_ret", "RHO_Q", "F(q)"]

BLOCK_RE = re.compile(r"RETRACTION-BLOCK-BEGIN(.*?)RETRACTION-BLOCK-END",
                      re.S)
RB_REQUIRED = re.compile(r"(?i)(retract|kill|superseded|historical)")
RB_FORBIDDEN = re.compile(r"(?i)(is a live assertion|THEOREM:|PROVED:"
                          r"|THEOREM \()")


def fail(msg: str):
    print(f"FAIL {msg}")
    sys.exit(1)


def generated_authored() -> list[Path]:
    files = [PROOF] + sorted((HERE / "authority").glob("*.md")) + [
        HERE / "STATUS_U1E.json"]
    missing = [p for p in files if not p.exists()]
    if missing:
        fail(f"H0 generated live file missing on disk: {missing}")
    return files


def h0_scope_coincidence() -> list[Path]:
    text = BANNER.read_text(encoding="utf-8")
    m = re.search(r"AUTHORED \(.*?\):\n(.*?)\n\nCOPIES", text, re.S)
    if not m:
        fail("H0 cannot parse the banner's AUTHORED live-chain list")
    banner_list = sorted(
        line.strip()[2:].strip()
        for line in m.group(1).splitlines() if line.strip().startswith("- "))
    gen = generated_authored()
    gen_rel = sorted(p.relative_to(HERE).as_posix() for p in gen)
    if banner_list != gen_rel:
        fail(f"H0 scope mismatch — banner: {banner_list} vs "
             f"filesystem: {gen_rel}")
    print(f"PASS H0 scope coincidence: banner AUTHORED list == generated "
          f"scan set ({len(gen)} files)")
    return gen


def validate_and_strip_blocks(path: Path, text: str) -> str:
    blocks = BLOCK_RE.findall(text)
    try:
        rel = path.relative_to(HERE).as_posix()
    except ValueError:
        rel = path.name
    allowed = RB_CONTENT_DIGESTS.get(rel, [])
    if len(blocks) != len(allowed):
        fail(f"RB registry violation in {rel}: {len(blocks)} block(s) "
             f"found, registry pins exactly {len(allowed)} (laundering "
             f"guard — any new block requires a registry change in the "
             f"same commit)")
    for body, want in zip(blocks, allowed):
        norm = " ".join(body.split())
        got = hashlib.sha256(norm.encode("utf-8")).hexdigest()
        if got != want:
            fail(f"RB block CONTENT digest mismatch in {rel} "
                 f"(interior of a registered block was edited — "
                 f"injection N3 class)")
        if not RB_REQUIRED.search(body):
            fail(f"RB block in {path.name} lacks retraction language")
        if RB_FORBIDDEN.search(body):
            fail(f"RB block in {path.name} contains a live-assertion "
                 f"marker")
    return BLOCK_RE.sub("", text)


def main() -> None:
    authored = h0_scope_coincidence()
    copies = sorted((HERE / "dependencies").glob("*.md"))
    if len(copies) != 7:
        fail(f"provenance model expects exactly 7 dependency copies, "
             f"found {len(copies)}")
    stray = [p for p in (HERE / "dependencies").iterdir()
             if p.suffix != ".md"]
    if stray:
        fail(f"non-.md file(s) in dependencies/: "
             f"{[p.name for p in stray]}")

    proof_raw = PROOF.read_text(encoding="utf-8")

    # RB + H1 + H2 over authored files.
    for p in authored:
        raw = p.read_text(encoding="utf-8")
        body = validate_and_strip_blocks(p, raw)
        for lit in KILLED_AUTHORED:
            if lit in body:
                fail(f"H1 killed literal {lit!r} in {p.name}")
        low = body.lower()
        for s in SHORTCUT:
            if s in low:
                fail(f"H1 retired shortcut in {p.name}")
        for tok in KILL_ROUTE:
            if tok in body:
                fail(f"H2 kill-#12 route token {tok!r} in {p.name}")
    if "RETRACTION-BLOCK" in proof_raw:
        fail("RB the U1G proof must contain no retraction block")
    for tok in KILL_ROUTE:
        if tok in proof_raw:
            fail(f"H2 kill-#12 route token {tok!r} in the U1G proof")
    print("PASS RB retraction blocks validated (registry + content "
          "check); none in the proof")
    print("PASS H1 killed literals absent (authored full scan)")
    print("PASS H2 kill-#12 route tokens absent from all authored live "
          "files")

    # H1 copies: identity-assertion scan; RB registry applies to copies
    # too (round-4 finding 3: zero blocks allowed in any copy).
    for p in copies:
        body = p.read_text(encoding="utf-8")
        validate_and_strip_blocks(p, body)
        for lit in KILLED_COPIES:
            if lit in body:
                fail(f"H1 killed-identity assertion {lit!r} in copy "
                     f"{p.name}")
    print("PASS H1 dependency copies: killed-identity scan clean; zero "
          "retraction blocks (7 full faithful copies)")

    # H3 required content.
    required = [
        "S_d :=", "D_upper(eps) :=", "NO DILATION",
        "P(c_{j+1}) = c_j", "strictly increasing",
        "\u00a710:792", "\u00a76:446",
        "band_identity", "s_mul_one_sub_s_le_quarter",
        "band_quarter_ceiling", "amplitude_b_le_half",
        "quarter_lt_window_lower", "6e6adb5",
        "2.001750769003037", "0.9590241", "0.9197272",
        "0.0836782", "0.0418391", "23.9010650",
        "d = |I|", "limsup",
        "IF AND ONLY IF this U1G gate promotes",
        "residual", "DISCLOSURE.md",
    ]
    proof_norm = " ".join(proof_raw.split())
    for token in required:
        if token not in proof_norm:
            fail(f"H3 required proof content missing: {token!r}")
    print("PASS H3 required U1G proof content present "
          "(whitespace-normalized)")

    # H4 ledger.
    ledger = (HERE / "authority" / "U1E_CORRECTION_LEDGER.md"
              ).read_text(encoding="utf-8")
    for token in ["kill #2", "kill #12", "G1 extract", "CUSTODY",
                  "VERDICT-U1E-AUDITOR-1-PROOF.md"]:
        if token not in ledger:
            fail(f"H4 ledger missing: {token!r}")
    print("PASS H4 ledger carries kill declarations + custody entry")

    # H5 anchors, parsed from the proof — HARD-FAIL if trees absent.
    if not CERT.exists():
        fail("H5 public certificate tree ABSENT — the predecessor anchor "
             "cannot be verified on this machine (hard-fail, no SKIP)")
    if not LEAN.exists():
        fail("H5 public Lean kernel tree ABSENT — the kernel anchor "
             "cannot be verified on this machine (hard-fail, no SKIP)")
    pairs = re.findall(r"\n\s+([0-9a-f]{64})\n\s+(\S+)", proof_raw)
    pub_pairs = [(h, n) for h, n in pairs if n.startswith("certificate/")]
    lean_pairs = [(h, n) for h, n in pairs if n.endswith(".lean")]
    cert_pairs = [(h, n) for h, n in pairs
                  if (h, n) not in pub_pairs and (h, n) not in lean_pairs]
    if (len(cert_pairs), len(lean_pairs), len(pub_pairs)) != (5, 6, 2):
        fail(f"H5 parsed anchor count wrong: {len(cert_pairs)} cert "
             f"(want 5), {len(lean_pairs)} lean (want 6), "
             f"{len(pub_pairs)} public-repo (want 2)")
    for want, name in cert_pairs:
        f = CERT / name
        if not f.exists():
            fail(f"H5 anchored certificate file missing: {name}")
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got != want:
            fail(f"H5 certificate hash mismatch: {name}")
    # Lean anchors are COMMIT-BLOB digests (round-4 proof finding
    # F-03): verify via git cat-file against the public commit THE
    # PROOF NAMES — parsed, not hardcoded (round-5 proof finding
    # I-03/AI-6b) — never the working tree.
    import subprocess
    mcommit = re.search(r"public commit ([0-9a-f]{7,40})", proof_raw)
    if not mcommit:
        fail("H5 cannot parse the Lean public commit id from proof §1b")
    lean_commit = mcommit.group(1)
    for want, name in lean_pairs:
        r = subprocess.run(
            ["git", "-C", str(PUBROOT), "cat-file", "blob",
             f"{lean_commit}:lean/I3322Kernel/{name}"],
            capture_output=True)
        if r.returncode != 0:
            fail(f"H5 cannot read Lean blob at commit {lean_commit}: "
                 f"{name} (hard-fail, no SKIP)")
        got = hashlib.sha256(r.stdout).hexdigest()
        if got != want:
            fail(f"H5 Lean kernel COMMIT-BLOB hash mismatch at "
                 f"{lean_commit}: {name}")
    for want, name in pub_pairs:
        f = PUBROOT / name
        if not f.exists():
            fail(f"H5 anchored public-repo file missing: {name}")
        got = hashlib.sha256(f.read_bytes()).hexdigest()
        if got != want:
            fail(f"H5 public-repo hash mismatch: {name}")
    for p in copies:
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if digest not in proof_raw:
            fail(f"H5 dependency copy digest not quoted in proof: "
                 f"{p.name} ({digest[:12]}...)")
    print("PASS H5 anchors parsed from proof and re-verified: 5 "
          "certificate + 6 Lean commit-blob + 2 public-repo + 7 "
          "dependency hashes (hard-fail mode, no SKIP path)")

    # H9 — FENCING PHRASES (round-4 proof finding F-06, adopted from
    # its recommended list): the proof must not contain unfencing
    # language, and the required fencing sentences must be present.
    H9_FORBIDDEN = [
        "is unconditional",       # the bound is anchored, never this
        "unconditionally",
        "does not depend on this gate",
        "sharp equality",
        "= 23.9010650 exactly",
        "NO RESIDUAL RISK",
        "no residual risk remains",
        "establishes S > S_LO by machine",
        "best possible",          # round-5 proof AI-3 paraphrase set
        "attained in the limit",
        "no further improvement",
    ]
    # Bundle-wide fencing (round-5 integrity finding 7): every
    # AUTHORED live file, blocks stripped, plus the proof's stricter
    # bare-word rule.
    for p in authored:
        body = validate_and_strip_blocks(
            p, p.read_text(encoding="utf-8"))
        for tok in H9_FORBIDDEN:
            if tok.lower() in body.lower():
                fail(f"H9 unfencing phrase in {p.name}: {tok!r}")
    if "unconditional" in proof_raw.lower():
        fail("H9 the proof must not contain the word 'unconditional' "
             "in any form")
    # Round-6 blocker 4 (N2c, partial-close + disclose): README.md and
    # U1_TO_U1E_CHANGES.md are allowed-but-not-authored files with no
    # legitimate killed content — scan them with the full token set.
    # The HISTORICAL files (superseded proofs, artifacts, audit trees)
    # are unscanned-by-design and the banner discloses why: they are
    # records that legitimately QUOTE killed content (the verdicts
    # quote the very literals they killed).
    for extra in [HERE / "README.md", HERE / "U1_TO_U1E_CHANGES.md"]:
        body = extra.read_text(encoding="utf-8")
        for lit in KILLED_AUTHORED:
            if lit in body:
                fail(f"H9x killed literal {lit!r} in {extra.name}")
        for tok in KILL_ROUTE:
            if tok in body:
                fail(f"H9x kill-route token {tok!r} in {extra.name}")
        for tok in H9_FORBIDDEN:
            if tok.lower() in body.lower():
                fail(f"H9x unfencing phrase in {extra.name}: {tok!r}")
    print("PASS H9x README + change list token-scanned (historical "
          "files unscanned-by-design, disclosed in the banner)")

    # H10 — VERDICT CUSTODY (round-6 finding 3 / blocker 6): the three
    # early-round verdict copies must be unaltered. Two halves since
    # the 2026-08-10 repair: (a) IN-REPO — each copy must hash to the
    # digest pinned in VERDICT_CUSTODY_DIGESTS above; this ALWAYS runs
    # and always hard-fails. (b) EXTERNAL — byte-for-byte against the
    # blind-batch-v19 originals in the author's private tree; runs only
    # when I3322_PRIVATE_SOURCE_ROOT is supplied, otherwise skipped
    # with a printed disclosure.
    BLIND = (PRIVATE_ROOT / _BLIND_REL) if PRIVATE_ROOT else None
    for name, want in VERDICT_CUSTODY_DIGESTS.items():
        copy = HERE / "audit_archive" / name
        if not copy.exists():
            fail(f"H10 archived verdict copy missing: {name}")
        if hashlib.sha256(copy.read_bytes()).hexdigest() != want:
            fail(f"H10 archived verdict copy differs from its pinned "
                 f"custody digest (evidence tampering?): {name}")
    print(f"PASS H10a early-round verdict copies match the pinned "
          f"in-repo custody digests "
          f"({len(VERDICT_CUSTODY_DIGESTS)} files)")
    if BLIND is None or not BLIND.is_dir():
        print(f"SKIP H10b blind-batch-v19 byte-identity - {SKIP_BANNER}")
    else:
        for name in VERDICT_CUSTODY_DIGESTS:
            orig = BLIND / name
            copy = HERE / "audit_archive" / name
            if not orig.exists():
                fail(f"H10b blind-batch original ABSENT under the "
                     f"supplied private root: {name} (hard-fail)")
            if copy.read_bytes() != orig.read_bytes():
                fail(f"H10b archived verdict copy differs from its "
                     f"blind-batch original (evidence tampering?): "
                     f"{name}")
        print("PASS H10b early-round verdict copies byte-identical to "
              "their blind-batch-v19 originals")
    H9_REQUIRED_IN_PROOF = [
        "claiming no sharpness",
        "DISCLOSED RESIDUAL RISK",
        "IF AND ONLY IF this U1G gate promotes",
        "checks ONLY the literal rational comparison",
    ]
    proof_norm9 = " ".join(proof_raw.split())
    for tok in H9_REQUIRED_IN_PROOF:
        if tok not in proof_norm9:
            fail(f"H9 required fencing sentence missing: {tok!r}")
    print("PASS H9 fencing phrases: forbidden absent, required present")

    # H7 — DIGEST-ANCHORED byte-identity of every dependency copy
    # (round-4 finding 2 / round-5 finding 1): each copy AND its
    # external sealed source must both hash to the digest pinned in
    # EXPECTED_DIGESTS — a lockstep tamper of copy + source (N1c)
    # fails here. Hard-fails if a source tree is absent.
    # Repair 2026-08-10: the copy-vs-registry half below is unchanged
    # and always hard-fails. The external half runs for every source
    # reachable on this machine; the six private-tree sources are
    # skipped-with-disclosure when I3322_PRIVATE_SOURCE_ROOT is not
    # supplied. A source that IS registered must still exist and match
    # — hard-fail, no silent pass.
    ext_checked = 0
    ext_skipped = []
    for p in copies:
        want = EXPECTED_DIGESTS.get(p.name)
        if want is None:
            fail(f"H7 dependency copy has no pinned digest: {p.name}")
        got = hashlib.sha256(p.read_bytes()).hexdigest()
        if got != want:
            fail(f"H7 dependency copy digest mismatch vs pinned "
                 f"registry: {p.name}")
        if (p.name not in EXTERNAL_SOURCES
                and p.name not in PRIVATE_SOURCE_RELPATHS):
            fail(f"H7 dependency copy has no registered external "
                 f"source: {p.name}")
        src = EXTERNAL_SOURCES.get(p.name)
        if src is None:
            ext_skipped.append(p.name)
            continue
        if not src.exists():
            fail(f"H7 external sealed source ABSENT for {p.name}: {src} "
                 f"(hard-fail, no SKIP)")
        if hashlib.sha256(src.read_bytes()).hexdigest() != want:
            fail(f"H7 external sealed source digest mismatch vs pinned "
                 f"registry (source tampered?): {p.name}")
        ext_checked += 1
    print(f"PASS H7 all {len(copies)} dependency copies match the "
          f"pinned digest registry; {ext_checked} external sealed "
          f"source(s) re-hashed and matched")
    if ext_skipped:
        print(f"SKIP H7 external sealed-source comparison for "
              f"{len(ext_skipped)} copy/copies "
              f"({', '.join(sorted(ext_skipped))}) - {SKIP_BANNER}")

    # H6 dangling pointers in authored files.
    checked = 0
    for p in authored:
        text = p.read_text(encoding="utf-8")
        text = re.sub(r"(dependencies/|audit_archive/|artifacts/)"
                      r"\s*\n\s*(?=[A-Z0-9])",
                      r"\1", text)
        for mref in re.finditer(
                r"(?:dependencies|audit_archive|artifacts)"
                r"[/][A-Za-z0-9_\-./]*[A-Za-z0-9_\-/]", text):
            rel = mref.group(0).rstrip("/.,;:)")
            if rel.endswith("*") or "*" in rel:
                continue
            if not (HERE / rel).exists():
                fail(f"H6 dangling pointer in {p.name}: {rel!r}")
            checked += 1
    print(f"PASS H6 no dangling pointers ({checked} path references "
          f"verified)")

    # H8 — MANIFEST PARTITION (round-4 integrity finding 4 / blocker
    # 3): the manifest must match the filesystem exactly (every entry
    # re-hashed; no unlisted files), and the banner's AUTHORED ∪
    # COPIES ∪ HISTORICAL classification must partition the manifest —
    # every file in the bundle is live-authored, a dependency copy, or
    # inside a declared historical/instrument location. Any file
    # anywhere else is a scope escape and FAILS.
    import json
    man_path = HERE / "MANIFEST_U1E_SHA256.json"
    if not man_path.exists():
        fail("H8 manifest missing")
    man = json.loads(man_path.read_text(encoding="utf-8"))["sha256"]
    # The ONLY filesystem exclusion is compiled bytecode (*.pyc)
    # INSIDE a __pycache__ directory — scoped per round-6 integrity
    # finding 7 so the code matches its own comment: a .pyc placed
    # anywhere else (injection E4) is a scope escape, as is any
    # non-pyc file inside __pycache__ (I20).
    fs = {}
    for p in sorted(HERE.rglob("*")):
        if not p.is_file() or p.name == "MANIFEST_U1E_SHA256.json":
            continue
        if p.suffix == ".pyc" and "__pycache__" in p.parts:
            continue
        fs[p.relative_to(HERE).as_posix()] = hashlib.sha256(
            p.read_bytes()).hexdigest()
    if set(man) != set(fs):
        only_man = sorted(set(man) - set(fs))[:5]
        only_fs = sorted(set(fs) - set(man))[:5]
        fail(f"H8 manifest/filesystem mismatch — manifest-only: "
             f"{only_man}; filesystem-only: {only_fs}")
    bad = [k for k in man if man[k] != fs[k]]
    if bad:
        fail(f"H8 manifest hash mismatch: {bad[:5]}")
    # FULL FILENAME ALLOWLIST (round-5 integrity findings 3/4, blocker
    # 3): the complete bundle file set is pinned here explicitly —
    # exactly as proof/ already was. Any new, missing, or relocated
    # file ANYWHERE (including artifacts/, guards/, audit trees, or a
    # brand-new directory) fails the gate. Adding a file to the bundle
    # requires editing this list in the same commit.
    if set(fs) != set(ALLOWED_FILES):
        extra = sorted(set(fs) - set(ALLOWED_FILES))[:5]
        missing = sorted(set(ALLOWED_FILES) - set(fs))[:5]
        fail(f"H8 filename-allowlist violation — unexpected: {extra}; "
             f"missing: {missing}")
    print(f"PASS H8 manifest partition + full filename allowlist: "
          f"{len(fs)} files re-hashed, zero unlisted, file set pinned "
          f"exactly (sole disclosed exclusion: *.pyc bytecode)")

    print("U1G LIVE-AUTHORITY HYGIENE: ALL PASS")


if __name__ == "__main__":
    main()
