"""Generate local import provenance, not a scientific or release manifest."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
review = root/'review/revision-2026-09-10'
rows = []
for folder in ['baseline', 'imported-repair']:
    for path in sorted((review/folder).iterdir()):
        if not path.is_file():
            continue
        assert path.stat().st_size <= 8*1024*1024
        rows.append({'path':path.relative_to(root).as_posix(),
                     'bytes':path.stat().st_size,
                     'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
assert len(rows) <= 100
result = {'kind':'import-provenance-only', 'date':'2026-09-10',
          'baseline_commit':'fe470d3f296262a64c68c6811770c9f5d3194fcc',
          'repair_source':'C:/Infanox/ak-working/synthesis/audits/i3322-common-return-2026-09-10',
          'mode':'byte-preserving copies; source repository left unchanged',
          'hash_mode':'raw SHA-256', 'files':rows}
(review/'IMPORTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'Imported/baseline files inventoried: {len(rows)}. Not a release manifest.')
