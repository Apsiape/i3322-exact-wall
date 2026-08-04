#!/usr/bin/env python3
"""Freeze every published source, dependency, receipt, paper, and license."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / "release-manifest.json"
ROOT_FILES = {
    ROOT / ".gitattributes",
    ROOT / ".gitignore",
    ROOT / ".zenodo.json",
    ROOT / "CITATION.cff",
    ROOT / "LICENSE.md",
    ROOT / "README.md",
    ROOT / "requirements.txt",
}
TREES = [
    ROOT / ".github",
    ROOT / "LICENSES",
    ROOT / "paper",
    ROOT / "certificate",
    ROOT / "review",
]
EXCLUDED_NAMES = {"release-manifest.json"}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache"}


def published_files() -> list[Path]:
    files = set(ROOT_FILES)
    for tree in TREES:
        files.update(path for path in tree.rglob("*") if path.is_file())
    return sorted(
        path for path in files
        if path.name not in EXCLUDED_NAMES
        and not any(part in EXCLUDED_PARTS for part in path.parts)
        and path.suffix.lower() not in {
            ".pyc", ".aux", ".bbl", ".blg", ".log", ".out", ".fls", ".fdb_latexmk"
        }
    )


def canonical_bytes(path: Path) -> tuple[bytes, str]:
    raw = path.read_bytes()
    if path.suffix.lower() in {".pdf", ".npz"}:
        return raw, "raw"
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n"), "canonical-lf"


def main() -> None:
    files = []
    for path in published_files():
        if not path.is_file():
            raise FileNotFoundError(path)
        payload, mode = canonical_bytes(path)
        files.append({
            "path": path.relative_to(ROOT).as_posix(),
            "canonical_bytes": len(payload),
            "hash_mode": mode,
            "sha256": hashlib.sha256(payload).hexdigest(),
        })
    manifest = {
        "status": "frozen standalone I3322 release custody manifest",
        "schema": 3,
        "files": files,
        "file_count": len(files),
        "scope": (
            "Custody manifest for selected published files. Analytic dependency "
            "closure is checked separately by verify_release.py and is not "
            "inferred from file enumeration alone."
        ),
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST} with {len(files)} files")


if __name__ == "__main__":
    main()
