"""Read-only post-build dependency identity; not an upstream source rebuild."""
from pathlib import Path
import json, subprocess

root=Path(__file__).resolve().parents[1]/'lean/I3322Kernel'
manifest=json.loads((root/'lake-manifest.json').read_text(encoding='utf-8'))
if len(manifest['packages'])!=9:raise ValueError('dependency inventory changed')
# These are scheduling options, not relaxed checks. Large dependency indexes
# otherwise spawn preload/index workers under the hosted 512 MiB check limit.
# Command-local options do not alter the repository or user's Git config.
git=['git','--no-optional-locks','-c','core.preloadIndex=false','-c','index.threads=1']
for p in manifest['packages']:
    path=root/'.lake/packages'/p['name']
    head=subprocess.check_output([*git,'rev-parse','HEAD'],cwd=path,text=True,timeout=10).strip()
    if head!=p['rev']:raise ValueError('dependency pin mismatch: '+p['name'])
    if subprocess.check_output([*git,'status','--porcelain','--untracked-files=no'],cwd=path,timeout=10):
        raise ValueError('tracked dependency tree dirty: '+p['name'])
print('PASS: nine exact dependency revisions with clean tracked trees; official compiled artifacts may be present.')
