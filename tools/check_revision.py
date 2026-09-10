"""Development checks for the 2026-09-10 revision, NOT a release gate.

Run under tools/run_capped.py on Windows. --report writes a generated check
receipt, not a release manifest. Lean and clean builds are separate commands.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'review/revision-2026-09-10'

def read(path):
    assert path.stat().st_size <= 8*1024*1024, path
    return path.read_text(encoding='utf-8')

def sha(path):
    assert path.stat().st_size <= 8*1024*1024, path
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--provenance', action='store_true', help='also check local, unpublished development imports')
    args = parser.parse_args()
    checks = []
    if args.provenance:
        baseline = REVIEW / 'baseline/resolution.tex'
        assert sha(baseline) == 'd4c15492297de8232c4de135eb7085e9287ed43cd63727051dfeba3950485f8b'
        frozen = json.loads(read(REVIEW / 'imported-repair/REVISION-MANIFEST.json'))
        for entry in frozen['files']:
            assert sha(REVIEW / 'imported-repair' / entry['path']) == entry['sha256'], entry['path']
        imports = json.loads(read(REVIEW / 'IMPORTS.json'))
        for entry in imports['files']:
            path = (ROOT / entry['path']).resolve()
            assert path.is_relative_to(REVIEW.resolve())
            assert sha(path) == entry['sha256'], entry['path']
        checks.append('local-only pre-revision manuscript and imported source provenance')

    draft = read(ROOT / 'paper/resolution.tex')
    proof = read(ROOT / 'paper/LOWER-BOUND-REVISION.tex')
    assert draft.count(r'\input{LOWER-BOUND-REVISION.tex}') == 1
    assert 'unjustified component-identification' in draft
    assert 'no such bound is imported' in proof.lower()
    assert 'from strongly connected components' in proof
    assert r'every $0<\eta<\keff$' in draft
    assert r'1+20R_{\max}/b_0' in draft
    assert r'\subsection*{Data availability}' in draft
    expanded = draft.replace(r'\input{LOWER-BOUND-REVISION.tex}', proof)
    labels = re.findall(r'\\label\{([^}]+)\}', expanded)
    assert len(labels) == len(set(labels)), 'duplicate labels'
    refs = set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', expanded))
    assert refs <= set(labels), refs-set(labels)
    bibs = set(re.findall(r'\\bibitem\{([^}]+)\}', expanded))
    citations = {k.strip() for group in re.findall(r'\\cite\{([^}]+)\}', expanded) for k in group.split(',')}
    assert citations <= bibs, citations-bibs
    checks.append(f'correction/scope disclosures; {len(labels)} labels and {len(bibs)} bibliography entries resolve')

    lean = read(ROOT / 'lean/I3322Kernel/I3322Kernel/WeightedFlow.lean')
    assert not re.search(r'\b(?:sorry|admit)\b|^\s*(?:axiom|unsafe)\b', lean, re.M)
    assert 'potential is an explicit hypothesis' in lean
    checks.append('new Lean source has no admissions/new axioms; kernel execution is reported separately')
    runs = []
    for name in ['check_interfaces.py', 'check_weighted_flow.py']:
        relative = 'certificate/production/lower-weighted-flow/' + name
        result = subprocess.run([sys.executable, relative], cwd=ROOT,
                                capture_output=True, text=True, encoding='utf-8', timeout=45)
        assert len(result.stdout)+len(result.stderr) <= 65536
        print(result.stdout, end='')
        if result.returncode:
            print(result.stderr, file=sys.stderr)
            raise RuntimeError(relative)
        runs.append({'path':relative, 'sha256':sha(ROOT/relative), 'exit_code':0, 'stdout':result.stdout})
    checks.append('exact development controls passed; no asymptotic conclusion from finite tests')
    log = ROOT / 'output/pdf/resolution.log'
    if log.exists():
        text = read(log)
        for marker in ['Overfull', 'undefined references', 'multiply defined', 'LaTeX Error']:
            assert marker not in text, marker
        assert 'Output written on' in text
        checks.append('available development TeX log has no overfull boxes or unresolved references')
    for item in checks:
        print('PASS:', item)
    report = {'kind':'development-check-receipt', 'date':'2026-09-10',
              'final_independent_review_performed':False, 'clean_release_gate_performed':False,
              'lean_kernel_run_in_this_command':False, 'checks':checks, 'runs':runs,
              'sources':{p:sha(ROOT/p) for p in ['paper/resolution.tex', 'paper/LOWER-BOUND-REVISION.tex',
                       'lean/I3322Kernel/I3322Kernel/WeightedFlow.lean']}}
    if args.report:
        dest = args.report.resolve()
        assert dest.is_relative_to(REVIEW.resolve()) or dest.is_relative_to((ROOT/'tmp').resolve())
        dest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('Development checks complete. Final independent review and clean release gate: NOT RUN.')

if __name__ == '__main__':
    main()
