"""Bounded release engineering checks; neither proof approval nor publication.

Run via run_capped.py on Windows, or a finite host process limit on Linux.
The approved hashes must come from a separately protected human approval
environment, not from this repository or untrusted workflow inputs.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, re, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
CONTROL={'release/SOURCE-MANIFEST.json','release/OPERATIONAL-MANIFEST.json','release/UNRELEASED.json','release/RELEASE-DECISIONS.json'}
SKIP_PARTS={'.git','.lake','.venv','__pycache__','.pytest_cache'}
SKIP_SUFFIX={'.aux','.bbl','.blg','.log','.out','.fls','.fdb_latexmk','.pyc','.olean','.ilean'}

def require(condition,message):
    if not condition: raise ValueError(message)

def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def bounded(p):
    require(p.stat().st_size<=8*1024*1024,'input exceeds 8 MiB')
    return p.read_text(encoding='utf-8')

def safe(root,name):
    p=PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name,'unsafe path')
    target=root.joinpath(*p.parts)
    require(target.resolve().is_relative_to(root.resolve()),'path escapes root')
    require(not any(x.is_symlink() or (hasattr(x,'is_junction') and x.is_junction()) for x in [target,*target.parents] if x.is_relative_to(root)), 'linked input')
    require(target.is_file(),'missing input: '+name)
    return target

def excluded(name):
    p=PurePosixPath(name)
    return name in CONTROL or bool(SKIP_PARTS.intersection(p.parts)) or p.parts[0] in {'tmp','output'} or name.startswith(('review/end-to-end-2026-09-10/','review/revision-2026-09-10/')) or p.suffix in SKIP_SUFFIX or name.endswith('.synctex.gz') or name.startswith('tools/release-preflight-UNRELEASED')

def expected_inventory(root):
    # Git inventories ignored versus publishable files on the actual checkout.
    # A packaged candidate has no .git and is checked by walking its exact tree.
    if (root/'.git').exists():
        data=subprocess.check_output(['git','ls-files','-z','--cached','--others','--exclude-standard'],cwd=root,timeout=15)
        require(len(data)<8*1024*1024,'oversized inventory')
        names=set(data.decode('utf-8').split('\0'))-{''}
    else:
        names={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    return sorted(n for n in names if not excluded(n))

def integrity(root,manifest):
    m=json.loads(bounded(manifest))
    require(m.get('schema')=='i3322-source-manifest-v1' and m.get('hash_mode')=='raw-sha256','wrong source manifest')
    entries=m['files']; names=[e['path'] for e in entries]
    require(names==expected_inventory(root) and len(names)==len(set(names)),'source inventory mismatch')
    for e in entries:
        p=safe(root,e['path'])
        require(e==dict(path=e['path'],bytes=p.stat().st_size,sha256=sha(p)),'source hash mismatch: '+e['path'])
    return len(entries)

def axioms(log,root=ROOT):
    requested=re.findall(r'^#print axioms (\S+)$',bounded(root/'lean/I3322Kernel/AxiomCheck.lean'),re.M)
    require(len(requested)==37 and len(set(requested))==37,'selected declaration list changed')
    text=bounded(log)
    lines=[line for line in text.splitlines() if line.strip()]
    found=[]
    for line in lines:
        match=re.fullmatch(r"'([^']+)' depends on axioms: \[([^\]]*)\]",line)
        require(match is not None,'unrecognized axiom output')
        found.append(match[1])
        require(set(filter(None,match[2].split(', ')))<={'propext','Classical.choice','Quot.sound'},'nonstandard axiom')
    require(found==requested,'missing, reordered, duplicated or foreign axiom declaration')
    return len(found)

def static(root):
    zen=json.loads(bounded(root/'.zenodo.json'))
    cff=bounded(root/'CITATION.cff')
    require('37 selected' in zen['description'] and 'complete analytic proof is not formalized' in zen['description'],'formal scope disclosure missing')
    require('for all sufficiently small' in zen['description'] and 'for all sufficiently small' in cff,'eventual coefficient qualifier missing')
    require('whether the Pal-Vertesi family converges to S' not in zen['description'],'stale globally-open claim')
    require('2608.29734' in zen['description'] and '2609.06038' in zen['description'],'concurrent citation missing')
    names=re.findall(r'^#print axioms (\S+)$',bounded(root/'lean/I3322Kernel/AxiomCheck.lean'),re.M)
    require(len(names)==37 and len(set(names))==37,'axiom target list changed')
    for p in (root/'lean/I3322Kernel/I3322Kernel').glob('*.lean'):
        source=re.sub(r'--[^\n]*','',bounded(p))
        require(not re.search(r'\b(?:sorry|admit)\b|^\s*(?:axiom|unsafe)\b',source,re.M),'admission in Lean source')
    manifest=json.loads(bounded(root/'lean/I3322Kernel/lake-manifest.json'))
    require(len(manifest['packages'])==9,'dependency count changed')
    require(all(re.fullmatch('[0-9a-f]{40}',p['rev']) for p in manifest['packages']),'unpinned dependency')
    print('PASS: metadata scope, eventual qualifier, concurrency, selected Lean source hygiene and nine full dependency pins. No theorem approval.')

def approval(root,tag,approved_manifest,approved_decisions):
    path=root/'release/SOURCE-MANIFEST.json'
    decision_path=root/'release/RELEASE-DECISIONS.json'
    d=json.loads(bounded(decision_path))
    require(d.get('status')=='APPROVED-FOR-RELEASE','release metadata not approved')
    require(re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+',d.get('version') or '') is not None,'version pending')
    require(tag=='v'+d['version'],'tag/version mismatch')
    doi=d.get('version_doi')
    mode=d.get('doi_mode')
    release_url='https://github.com/Apsiape/i3322-exact-wall/releases/tag/'+tag
    require(mode in {'reserved-before-release','zenodo-after-github-release'},'DOI workflow not declared')
    if mode=='reserved-before-release':
        require(re.fullmatch(r'10\.5281/zenodo\.[0-9]+',doi or '') is not None,'version DOI pending')
        require(doi not in {'10.5281/zenodo.21782008','10.5281/zenodo.22099128'},'concept or historical DOI substituted for new version')
    else:
        require(doi is None,'automatic mint must not claim a preassigned DOI')
        require(d.get('release_url')==release_url,'versioned release URL missing or mismatched')
    for field in ['proof_review_approval','public_release_approval','public_inventory_approval']:
        value=d.get(field)
        require(isinstance(value,dict) and bool(value.get('approved_by')) and bool(value.get('approved_at')) and value.get('source_manifest_sha256')==sha(path),field+' missing or for different bytes')
    require(approved_manifest==sha(path),'protected human-approved source hash missing or mismatched')
    require(approved_decisions==sha(decision_path),'protected human-approved decisions hash missing or mismatched')
    cff=bounded(root/'CITATION.cff'); zen=json.loads(bounded(root/'.zenodo.json')); tex=bounded(root/'paper/resolution.tex')
    require(zen.get('version')==d['version'] and re.search(r'^version: '+re.escape(d['version'])+r'$',cff,re.M),'public version mismatch')
    if mode=='reserved-before-release':
        require(doi in cff and doi in tex,'version DOI absent from citation or source')
    else:
        require(re.search(r'^url: "'+re.escape(release_url)+r'"$',cff,re.M) is not None,'citation does not identify tagged snapshot')
        require(re.search(r'^doi:',cff,re.M) is None and not zen.get('doi'),'automatic mint metadata supplies a DOI')
    require('Internal review draft' not in tex and 'No new public archive identifier' not in tex and 'in this internal revision' not in tex,'pending manuscript release fields')
    require('UNRELEASED' not in zen['description'],'archive description remains unreleased')
    require('UNRELEASED' not in cff,'citation remains unreleased')
    static(root)
    return integrity(root,path)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['static','integrity','axioms','release'])
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--log',type=Path);parser.add_argument('--tag')
    parser.add_argument('--approved-manifest-sha256');parser.add_argument('--approved-decisions-sha256')
    a=parser.parse_args();root=a.root.resolve()
    if a.mode=='static':static(root)
    elif a.mode=='axioms':print('PASS:',axioms(a.log,root),'selected standard-axiom declarations; complete paper not formalized.')
    elif a.mode=='integrity':print('PASS:',integrity(root,root/'release/SOURCE-MANIFEST.json'),'raw source files; custody only.')
    else:print('PASS:',approval(root,a.tag,a.approved_manifest_sha256,a.approved_decisions_sha256),'source files and separately approved prepublication metadata. This does not publish a release or verify a Zenodo DOI/archive; automated checks do not confer proof approval.')

if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,FileNotFoundError) as e:
        print('FAIL-CLOSED:',e,file=sys.stderr);raise SystemExit(1)
