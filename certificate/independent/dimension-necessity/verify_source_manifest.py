#!/usr/bin/env python3
"""Verify the review-adjudicated packet for the conditional reconstruction."""

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
    assert manifest["source_count"] == len(manifest["sources"]) == 21
    required = {
        "certificate/production/foundational-sprint-1226/WEIGHTED-CLOSURE-COERCIVITY.md",
        "certificate/production/foundational-sprint-1227/NEAR-FIXED-PULLBACK-PAIRING.md",
    }
    review_adjudicated_live_matches = required | {
        "certificate/production/foundational-sprint-1229/RESULT-001-NEAR-FIXED-MASS-GAP.md",
    }
    checked = []
    for entry in manifest["sources"]:
        logical = Path(entry["path"])
        assert logical.parts[:2] == ("certificate", "production")
        path = HERE / "source-snapshots" / Path(*logical.parts[2:])
        payload = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        assert len(payload) == entry["bytes"], entry["path"]
        assert hashlib.sha256(payload).hexdigest() == entry["sha256"], entry["path"]
        if entry["path"] in review_adjudicated_live_matches:
            production = ROOT / logical
            assert production.is_file(), entry["path"]
            production_payload = production.read_bytes().replace(
                b"\r\n", b"\n"
            ).replace(b"\r", b"\n")
            assert production_payload == payload, entry["path"]
        checked.append(entry["path"])
    assert required.issubset(checked)
    report = {
        "status": "review-adjudicated conditional source snapshots verified",
        "source_count": len(checked),
        "all_gates_pass": True,
    }
    (HERE / "source-manifest-audit.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(f"PASS conditional source manifest: {len(manifest['sources'])} files")


if __name__ == "__main__":
    main()
