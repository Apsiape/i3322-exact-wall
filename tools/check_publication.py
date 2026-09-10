"""Read-only public-package checks. No mathematical or human release approval.

Run under run_capped.py on Windows. Reads bounded text and Git inventories;
never stages, commits, overwrites certificates, or publishes.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ('review/end-to-end-2026-09-10/', 'review/revision-2026-09-10/')
DOCS = ['README.md', 'VERIFY.md', 'REVIEW-START-HERE.md',
        'paper/CERTIFICATE-MAP.md', 'paper/REVISION-NOTES.md',
        'paper/ARXIV-SUBMISSION.md', 'certificate/production/lower-weighted-flow/README.md']

def digest(p):
    with p.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

def read(p):
    assert p.stat().st_size < 2*1024*1024, 'oversized text'
    return p.read_text(encoding='utf-8')

def run(args, data=None):
    r = subprocess.run(['git', *args], input=data, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, cwd=ROOT, timeout=10)
    assert r.returncode == 0, r.stderr.decode(errors='replace')[:400]
    assert len(r.stdout) < 8*1024*1024
    return r.stdout

def main():
    names = None
    if (ROOT/'.git').exists():
        names = sorted(set(run(['ls-files', '-z', '--cached', '--others', '--exclude-standard']).decode().split('\0'))-{''})
        assert not any(n.startswith(PRIVATE) for n in names), 'private operational file exposed to Git'
        assert not any('/.lake/' in n or n.startswith(('output/','tmp/','.env')) for n in names), 'cache or private file exposed'
        for private in PRIVATE:
            run(['check-ignore', private+'PUBLICATION-NEGATIVE-CONTROL.txt'])
    else:
        assert not any((ROOT/p).exists() for p in PRIVATE), 'private audit directory inside public archive'
    for name in DOCS:
        p = ROOT/name
        text = read(p)
        assert not any(x in text for x in PRIVATE), 'private entry link: '+name
        assert not re.search(r'(?i)\bC:[/\\]', text), 'workstation path: '+name
        for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', text):
            target = target.split('#',1)[0].strip('<>')
            if not target or re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', target):
                continue
            local = (p.parent/unquote(target)).resolve()
            assert local.is_relative_to(ROOT) and local.exists(), (name,target)
    tex = read(ROOT/'paper/resolution.tex')
    for stale in ['Internal review draft','in this internal revision',
                  'No new public archive identifier', 'risk was discharged',
                  'whether their particular family converges',
                  'Whether their family nonetheless converges']:
        assert stale not in tex, 'stale manuscript statement: '+stale
    assert 'full finite' in tex and 'Theorem~1' in tex and r'\cite{Pauwels}' in tex
    assert 'not formalized' in tex and 'for all sufficiently small' in tex
    assert r'\date{10 September 2026}' in tex
    receipt = json.loads(read(ROOT/'paper/BUILD.json'))
    assert receipt['kind'] == 'source-pdf-build-identity-not-proof'
    assert set(receipt['sha256']) == {'resolution.tex','LOWER-BOUND-REVISION.tex','resolution.pdf'}
    for name, value in receipt['sha256'].items():
        assert digest(ROOT/'paper'/name) == value, 'PDF/source receipt mismatch: '+name
    if names is not None:
        for name in names:
            p = ROOT/name
            if not p.is_file() or p.stat().st_size > 2*1024*1024:
                continue
            data = p.read_bytes()
            if b'\r\n' not in data or b'\0' in data:
                continue
            assert run(['hash-object','--stdin'], data) == run(['hash-object','--stdin','--path='+name], data), 'Git normalization changes frozen bytes: '+name
    print('PASS: public entry links, private/cache exclusion, manuscript hygiene, source/PDF hashes and Git clean-filter stability. No proof or release approval.')

if __name__ == '__main__':
    main()
