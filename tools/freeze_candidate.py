"""Create a new raw source manifest exclusively; never approve or publish it."""
from pathlib import Path
import argparse, json
from verify_candidate import expected_inventory, safe, sha

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root',type=Path,required=True)
a=parser.parse_args();root=a.root.resolve()
destination=root/'release/SOURCE-MANIFEST.json'
files=[]
for name in expected_inventory(root):
    p=safe(root,name);files.append(dict(path=name,bytes=p.stat().st_size,sha256=sha(p)))
data=json.dumps(dict(schema='i3322-source-manifest-v1',hash_mode='raw-sha256',files=files),indent=2)+'\n'
if len(data.encode())>8*1024*1024:raise ValueError('manifest exceeds 8 MiB')
destination.parent.mkdir(parents=True,exist_ok=True)
with destination.open('x',encoding='utf-8',newline='\n') as f:f.write(data)
print(f'FROZEN CUSTODY ONLY: {len(files)} files; manifest SHA-256 {sha(destination)}; no approval, version selection, tag or publication.')
