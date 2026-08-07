#!/usr/bin/env python3
"""Assert historical archive hashes used for v28 provenance."""
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
items=[
 (root/'historical/current-S-antitone-walk-v23.ORIGINAL.zip','705c3dc4a3d090954c3bca220842c08e316c4a9ebc50f1f9cff69628ea7cc420','v23'),
 (root/'historical/I3322_CONSOLIDATED_PROMOTION_BUNDLE_2026-08-06.zip','06cc24c0da33d7f7b88e4ab9c945010a0a55ef19f88b5b611fd1021b0decf6ef','consolidated'),
 (root/'historical/I3322_V26_LOWER_BOUND_REAUDIT_BUNDLE_2026-08-06.zip','9fe8c2bc90d42c0a8adbf9090afd10c024b5d2afa36dbb599e6288a3f4bdf90c','v26'),
 (root/'historical/I3322_V27_LOWER_BOUND_REAUDIT_BUNDLE_2026-08-06.zip','3801b4a1504a7a589cd495a3233046266464cfcef920b3d5deed392a2ef56cd7','v27'),
]
for p,h,label in items:
    assert p.is_file(),p
    assert sha(p)==h,(label,sha(p),h)
print('PASS v28 historical hash assertions')
for _,h,label in items: print(f'  {label}={h}')
