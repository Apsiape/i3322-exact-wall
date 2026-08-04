#!/usr/bin/env python3
"""Verify the sealed source boundary used by the blind reconstruction."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main() -> None:
    manifest = json.loads(
        (HERE / "source-manifest.json").read_text(encoding="utf-8")
    )
    assert manifest["source_count"] == len(manifest["sources"]) == 19
    checked = []
    for entry in manifest["sources"]:
        logical = Path(entry["path"])
        assert logical.parts[:2] == ("certificate", "production")
        path = HERE / "source-snapshots" / Path(*logical.parts[2:])
        payload = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        assert len(payload) == entry["bytes"], entry["path"]
        assert hashlib.sha256(payload).hexdigest() == entry["sha256"], entry["path"]
        checked.append(entry["path"])
    report = {
        "status": "sealed blind source snapshots verified",
        "source_count": len(checked),
        "all_gates_pass": True,
    }
    (HERE / "source-manifest-audit.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(f"PASS sealed source manifest: {len(manifest['sources'])} files")


if __name__ == "__main__":
    main()
