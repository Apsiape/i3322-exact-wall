"""Read-only release preparation; never a mathematical or publication gate.

check and verify do not write. snapshot writes one new UNRELEASED custody
manifest exclusively; it does not copy, package, replay, or publish sources.
Run under tools/run_capped.py on Windows. No third-party dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MAX_JSON = 8 * 1024 * 1024
EXCLUDED_PARTS = {".git", ".lake", ".venv", "__pycache__", ".pytest_cache"}
EXCLUDED_ROOTS = {"tmp", "output"}
GENERATED_SUFFIXES = {".aux", ".bbl", ".blg", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc", ".olean", ".ilean"}
POLICY = "git tracked plus nonignored untracked; omit caches, generated auxiliaries, tmp/output, and operational review/end-to-end-2026-09-10"


def safe_path(relative: str) -> Path:
    p = PurePosixPath(relative)
    if not relative or p.is_absolute() or ".." in p.parts or "\\" in relative or ":" in relative:
        raise ValueError(f"unsafe relative path: {relative!r}")
    path = ROOT.joinpath(*p.parts)
    if not path.resolve().is_relative_to(ROOT) or any(x.is_symlink() for x in [path, *path.parents] if x != ROOT.parent):
        raise ValueError(f"symlink or path escape: {relative}")
    if not path.is_file():
        raise ValueError(f"missing file: {relative}")
    return path


def record(relative: str) -> dict:
    path = safe_path(relative)
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
    return {"path": relative, "bytes": size, "sha256": digest.hexdigest()}


def excluded(relative: str) -> bool:
    p = PurePosixPath(relative)
    return (bool(EXCLUDED_PARTS.intersection(p.parts)) or p.parts[0] in EXCLUDED_ROOTS
            or relative.startswith(("review/end-to-end-2026-09-10/", "review/revision-2026-09-10/"))
            or p.suffix.lower() in GENERATED_SUFFIXES or relative.endswith(".synctex.gz")
            or relative.startswith("tools/release-preflight-UNRELEASED"))


def inventory() -> list[str]:
    result = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                            cwd=ROOT, capture_output=True, check=True, timeout=15)
    if len(result.stdout) > MAX_JSON:
        raise ValueError("file inventory exceeds 8 MiB")
    paths = sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})
    return [p for p in paths if not excluded(p)]


def source_plan() -> dict:
    """Conservative static closure for this paper, not a general TeX parser."""
    pending = ["resolution.tex"]
    visited = set()
    while pending:
        name = pending.pop()
        if name in visited:
            continue
        path = safe_path("paper/" + name)
        if path.stat().st_size > MAX_JSON:
            raise ValueError("TeX source exceeds 8 MiB")
        source = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text(encoding="utf-8"))
        if re.search(r"\\(?:includegraphics|bibliography|bibliographystyle|write18|openout|read|catcode|csname|IfFileExists|InputIfFileExists)\b", source):
            raise ValueError(f"manual dependency inspection required: {name}")
        commands = re.findall(r"\\(?:input|include)\b", source)
        names = re.findall(r"\\(?:input|include)\s*\{([A-Za-z0-9_./-]+)\}", source)
        if len(commands) != len(names):
            raise ValueError(f"nonliteral input requires manual review: {name}")
        for child in names:
            if "/" in child or child.startswith("."):
                raise ValueError(f"nonflat source input requires manual review: {child}")
            pending.append(child if child.endswith(".tex") else child + ".tex")
        visited.add(name)
    if visited != {"resolution.tex", "LOWER-BOUND-REVISION.tex"}:
        raise ValueError(f"source closure changed; review package policy: {sorted(visited)}")
    return {"status": "STATIC_SOURCE_CLOSURE_ONLY", "engine": "pdflatex -no-shell-escape",
            "archive_members": sorted(visited),
            "files": [record("paper/" + p) for p in sorted(visited)],
            "compile_performed": False, "upload_performed": False}


def raw_provenance_crlf_paths() -> list[str]:
    hazards = []
    for folder in ["baseline", "imported-repair"]:
        for path in (ROOT / "review/revision-2026-09-10" / folder).rglob("*"):
            if path.is_file() and path.suffix.lower() not in {".pdf", ".npz"}:
                if path.stat().st_size > MAX_JSON:
                    raise ValueError(f"provenance text exceeds 8 MiB: {path.name}")
                if b"\r" in path.read_bytes():
                    hazards.append(path.relative_to(ROOT).as_posix())
    return sorted(hazards)


def snapshot() -> dict:
    return {"schema": "i3322-unreleased-custody-v1", "status": "UNRELEASED",
            "hash_mode": "raw-sha256", "inventory_policy": POLICY,
            "excluded_operational_review": "review/end-to-end-2026-09-10/",
            "proof_replay_performed": False, "release_gate_performed": False,
            "files": [record(p) for p in inventory()]}


def verify_manifest(manifest: dict) -> int:
    if (manifest.get("schema") != "i3322-unreleased-custody-v1"
            or manifest.get("status") != "UNRELEASED"
            or manifest.get("hash_mode") != "raw-sha256"
            or manifest.get("inventory_policy") != POLICY
            or manifest.get("proof_replay_performed") is not False
            or manifest.get("release_gate_performed") is not False):
        raise ValueError("not an UNRELEASED custody-only manifest")
    entries = manifest["files"]
    paths = [entry["path"] for entry in entries]
    if len(paths) != len(set(paths)) or paths != inventory():
        raise ValueError("manifest inventory differs (added, removed, duplicated, or reordered file)")
    for entry in entries:
        if entry != record(entry["path"]):
            raise ValueError(f"raw custody mismatch: {entry['path']}")
    return len(entries)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="read-only source closure and candidate inventory")
    make = commands.add_parser("snapshot", help="write a new UNRELEASED custody manifest only")
    make.add_argument("--output", type=Path, required=True)
    verify = commands.add_parser("verify", help="read-only complete inventory and raw hash comparison")
    verify.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    result = {"status": "UNRELEASED", "proof_replay_performed": False, "release_gate_performed": False}
    if args.command == "check":
        result["source_package"] = source_plan()
        result["candidate_file_count"] = len(inventory())
        result["stale_resolution_auxiliaries"] = [p.name for p in (ROOT / "paper").glob("resolution.*")
                                                  if p.suffix in GENERATED_SUFFIXES]
        result["inventory_policy"] = POLICY
        result["raw_provenance_files_requiring_no_text_conversion"] = raw_provenance_crlf_paths()
    elif args.command == "snapshot":
        dest = args.output.resolve()
        allowed = ROOT / "review/end-to-end-2026-09-10"
        if dest.parent != allowed or not re.fullmatch(r"CLEANUP-UNRELEASED[-A-Za-z0-9]*\.json", dest.name):
            raise ValueError("output must be a new review/end-to-end-2026-09-10/CLEANUP-UNRELEASED*.json")
        data = snapshot()
        payload = json.dumps(data, indent=2) + "\n"
        if len(payload.encode()) > MAX_JSON:
            raise ValueError("manifest exceeds 8 MiB")
        with dest.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(payload)
        result.update({"manifest": dest.relative_to(ROOT).as_posix(), "files": len(data["files"])})
    else:
        if args.manifest.stat().st_size > MAX_JSON:
            raise ValueError("manifest exceeds 8 MiB")
        result["custody_files_checked"] = verify_manifest(json.loads(args.manifest.read_text(encoding="utf-8")))
        result["custody_result"] = "RAW_HASH_AND_INVENTORY_MATCH_ONLY"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
