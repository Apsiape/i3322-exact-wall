#!/usr/bin/env python3
"""Fail-closed v2 package wording and dependency validator."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
theorem = (root / "CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md").read_text(encoding="utf-8")
signed = (root / "THEOREM_S_SIGNED_PUBLIC_STATEMENT.md").read_text(encoding="utf-8")
readme = (root / "README.md").read_text(encoding="utf-8")
scope = (root / "SPRINT_1206_SCOPE_AND_RETIREMENT_NOTICE.md").read_text(encoding="utf-8")

required = {
    "V1 fixed set null": r"mu_U\(F\)=0|\\mu_U\(F\)=0",
    "V2 W operator": r"W=Y\(B_3-I/2\)",
    "V2 no global division": r"No division by",
    "V3 conull set": r"Y_0",
    "V4 increasing": r"tau.*increasing|\\tau.*increasing",
    "V5 odd labels": r"Every odd label",
    "V6 narrow 1206": r"Sprint 1206 §§2–4",
    "V7 normalization": r"c_B\(t\)=1",
    "V8 psi unit": r"unit vector|\\sum_j\\lambda_j\^2=1",
    "V8 no overshoot": r"H\\preceq SI",
    "V9 decertification": r"decertified",
    "V9 conditional separation": r"using promoted Theorem \(N\)|by promoted Theorem \(N\)",
}
blob = theorem + "\n" + signed + "\n" + readme + "\n" + scope
for name, pattern in required.items():
    assert re.search(pattern, blob, re.I | re.S), f"missing required repair: {name}"

forbidden = [
    r"K_A\\Omega",
    r"K_B\\Omega",
    r"fixed points are absent",
    r"the fixed-point set is empty",
    r"Sprint 1206 as a theorem",
    r"historical Pál–Vértesi decimal",
    r"scripts verify the theorem",
]
for pattern in forbidden:
    assert not re.search(pattern, theorem, re.I), f"forbidden operative wording: {pattern}"

status = json.loads((root / "STATUS.json").read_text(encoding="utf-8"))
assert status["repairs_executed"] == [f"V{i}" for i in range(1,10)]
assert status["public_claim"] == "Theorem (S)"
assert status["historical_route_reused"] is False
assert status["theorem_N_dependency_for_separation"] is True

print("PASS: V1–V9 wording, scope and status controls")
