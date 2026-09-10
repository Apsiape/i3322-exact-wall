"""Bounded byte-custody regression tests; no scientific validation."""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib, json, subprocess
from check_git_snapshot import verify

def main():
    with TemporaryDirectory(prefix='i3322-blobs-') as tmp:
        root=Path(tmp); (root/'release').mkdir()
        def git(*args):
            return subprocess.check_output(['git','-c','core.autocrlf=false',*args],cwd=root,stderr=subprocess.STDOUT,timeout=10)
        git('init','-q');git('config','user.name','Custody fixture');git('config','user.email','fixture@example.invalid')
        source=root/'sample.txt';manifest=root/'release/SOURCE-MANIFEST.json'
        (root/'release/RELEASE-DECISIONS.json').write_bytes(b'{}\n')
        def freeze():
            raw=source.read_bytes()
            manifest.write_bytes((json.dumps(dict(schema='i3322-source-manifest-v1',hash_mode='raw-sha256',files=[dict(path='sample.txt',bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())]))+'\n').encode())
        def reject(index=True):
            try:verify(root,index)
            except ValueError:return
            raise AssertionError('incorrect Git bytes accepted')
        source.write_bytes(b'alpha\nbeta\n');freeze();git('add','.');git('commit','-qm','fixture')
        assert verify(root,True)==3 and verify(root)==3
        # A refreshed manifest and unchanged index must not hide CRLF/LF drift.
        source.write_bytes(b'alpha\r\nbeta\r\n');freeze();git('add','release/SOURCE-MANIFEST.json');reject();reject(False)
        git('add','sample.txt');assert verify(root,True)==3;reject(False)
        git('commit','-qm','consistent CRLF fixture');assert verify(root)==3
        # Same-size altered content exercises SHA checking, not merely size.
        source.write_bytes(b'ALPHA\r\nbeta\r\n');freeze();git('add','release/SOURCE-MANIFEST.json');reject()
        git('add','sample.txt');assert verify(root,True)==3
        (root/'extra.txt').write_bytes(b'extra');git('add','extra.txt');reject()
        git('rm','--cached','extra.txt');git('rm','--cached','sample.txt');reject()
    print('PASS: actual index/commit bytes; CRLF drift; stale index; same-size tamper; missing/extra files rejected.')

if __name__=='__main__':main()
