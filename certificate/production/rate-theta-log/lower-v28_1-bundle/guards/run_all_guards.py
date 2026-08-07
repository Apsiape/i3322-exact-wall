#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
names=[
 'guard_g1_endpoint_arithmetic.py',
 'guard_monge_cross_difference.py',
 'guard_cell_grid_and_edge_budget.py',
 'guard_reflection_boundary_atoms.py',
 'guard_grid_transfer_strict.py',
 'guard_actual_Z_projection_squeeze.py',
 'guard_L6_local_error_horn.py',
 'guard_endpoint_certificate_replay.py',
 'guard_return_hygiene.py',
 'guard_live_authority_hygiene.py',
 'guard_historical_hashes.py',
]
for name in names:
    print(f'=== {name} ===',flush=True)
    subprocess.run([sys.executable,str(root/name)],check=True)
print('ALL V28 LOWER-CLOSEOUT GUARDS PASSED')
