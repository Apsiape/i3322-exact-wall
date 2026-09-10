"""Check actual index/commit blobs against the frozen release inventory.

Run under a finite process/memory cap. This is custody, not proof validation.
Unlike a clean working tree or a fresh staging simulation, this reads the
objects that a real commit/tag/archive contains.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess
from verify_candidate import ROOT, sha, bounded, require

def verify(root, index=False, ref='HEAD'):
    m=json.loads(bounded(root/'release/SOURCE-MANIFEST.json'))
    require(m.get('schema')=='i3322-source-manifest-v1' and m.get('hash_mode')=='raw-sha256','manifest schema')
    expected={x['path']:(x['bytes'],x['sha256']) for x in m['files']}
    require(len(expected)==len(m['files']),'duplicate manifest path')
    for name in ['release/SOURCE-MANIFEST.json','release/RELEASE-DECISIONS.json']:
        p=root/name;expected[name]=(p.stat().st_size,sha(p))
    if index:
        args=['ls-files','--stage','-z']
    else:
        oid=subprocess.check_output(['git','rev-parse','--verify','--end-of-options',ref+'^{commit}'],cwd=root,timeout=10).decode().strip()
        args=['ls-tree','-r','-z','--full-tree',oid]
    raw=subprocess.check_output(['git',*args],cwd=root,timeout=15)
    require(len(raw)<=8*1024*1024,'oversized tree')
    objects={}
    for row in raw.split(b'\0'):
        if not row:continue
        header,name=row.split(b'\t',1);parts=header.decode().split();name=name.decode()
        require(parts[0] in {'100644','100755'},'non-regular tree entry: '+name)
        require((parts[2]=='0') if index else (parts[1]=='blob'),'unmerged/nonblob entry')
        require(name not in objects,'duplicate tree entry')
        objects[name]=parts[1] if index else parts[2]
    require(set(objects)==set(expected),'actual Git inventory differs from frozen inventory')
    proc=subprocess.Popen(['git','cat-file','--batch'],cwd=root,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    try:
        for name,oid in sorted(objects.items()):
            proc.stdin.write((oid+'\n').encode());proc.stdin.flush()
            header=proc.stdout.readline().decode().split()
            require(len(header)==3 and header[1]=='blob','invalid Git object response')
            size=int(header[2]);require(size<=16*1024*1024,'oversized blob')
            require(size==expected[name][0],'Git blob size mismatch: '+name)
            digest=hashlib.sha256();remaining=size
            while remaining:
                chunk=proc.stdout.read(min(remaining,65536))
                require(bool(chunk),'short Git object read');remaining-=len(chunk);digest.update(chunk)
            require(proc.stdout.read(1)==b'\n','invalid Git object terminator')
            require(digest.hexdigest()==expected[name][1],'Git blob hash mismatch: '+name)
    finally:
        if proc.poll() is None:
            proc.stdin.close()
            try:proc.wait(timeout=5)
            except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=5)
        proc.stdout.close()
    require(proc.returncode==0,'Git object reader failed')
    return len(expected)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--index',action='store_true');parser.add_argument('--ref',default='HEAD')
    args=parser.parse_args()
    print('PASS:',verify(ROOT,args.index,args.ref),'actual Git blobs exactly match frozen source/control bytes; custody only.')
