#!/usr/bin/env python3
"""Test positive-projection/Morse filtering before envelope selection."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/"foundational-sprint-1274"/"lower_envelope_characteristic_atlas.py"


def main() -> None:
    spec=importlib.util.spec_from_file_location("s1275_source",SOURCE)
    module=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    report=module.run("stable_least")
    report["claim_boundary"]=(
        "This is a floating-point local-Morse selector test. Passing would "
        "still require interval derivative signs and global Bellman closure."
    )
    (HERE/"morse-filtered-characteristic-atlas.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
