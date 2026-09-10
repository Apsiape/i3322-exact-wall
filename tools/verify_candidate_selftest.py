"""Adversarial engineering controls in a disposable directory, no publication."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import copy, importlib.util, json

spec=importlib.util.spec_from_file_location('verify',Path(__file__).with_name('verify_candidate.py'))
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

def rejected(f):
    try:f()
    except (ValueError,FileNotFoundError):return
    raise AssertionError('invalid candidate accepted')

def main():
    with TemporaryDirectory(prefix='i3322-gate-') as td:
        root=Path(td);(root/'release').mkdir();(root/'paper').mkdir();(root/'lean/I3322Kernel').mkdir(parents=True)
        source=root/'paper/resolution.tex';source.write_text('reviewed version DOI 10.5281/zenodo.99999999',encoding='utf-8')
        (root/'CITATION.cff').write_text('version: 4.1.0\ndoi: 10.5281/zenodo.99999999\n',encoding='utf-8')
        (root/'.zenodo.json').write_text(json.dumps({'version':'4.1.0','description':'fixture only'}),encoding='utf-8')
        ax=root/'lean/I3322Kernel/AxiomCheck.lean'; ax.write_bytes((v.ROOT/'lean/I3322Kernel/AxiomCheck.lean').read_bytes())
        m={'schema':'i3322-source-manifest-v1','hash_mode':'raw-sha256','files':[dict(path=p,bytes=(root/p).stat().st_size,sha256=v.sha(root/p)) for p in v.expected_inventory(root)]}
        manifest=root/'release/SOURCE-MANIFEST.json';manifest.write_text(json.dumps(m),encoding='utf-8')
        assert v.integrity(root,manifest)==4
        for mutate in [lambda x:x['files'].pop(),lambda x:x['files'].append(x['files'][0]),lambda x:x['files'][0].update(sha256='0'*64),lambda x:x['files'][0].update(path='../escape')]:
            bad=copy.deepcopy(m);mutate(bad);manifest.write_text(json.dumps(bad),encoding='utf-8');rejected(lambda:v.integrity(root,manifest))
        manifest.write_text(json.dumps(m),encoding='utf-8')
        source.write_text('tampered',encoding='utf-8');rejected(lambda:v.integrity(root,manifest))
        source.write_text('reviewed version DOI 10.5281/zenodo.99999999',encoding='utf-8')
        approved={'approved_by':'TEST FIXTURE ONLY','approved_at':'TEST','source_manifest_sha256':v.sha(manifest)}
        d={'status':'APPROVED-FOR-RELEASE','version':'4.1.0','doi_mode':'reserved-before-release','version_doi':'10.5281/zenodo.99999999','proof_review_approval':approved,'public_release_approval':approved,'public_inventory_approval':approved}
        decision=root/'release/RELEASE-DECISIONS.json'
        def write(x):decision.write_text(json.dumps(x),encoding='utf-8')
        def check():return v.approval(root,'v4.1.0',v.sha(manifest),v.sha(decision))
        # A fabricated identifier is confined to this disposable test fixture.
        with patch.object(v,'static'):
            write(d);assert check()==4
            rejected(lambda:v.approval(root,'v4.1.0',None,None))
            rejected(lambda:v.approval(root,'v4.0.0',v.sha(manifest),v.sha(decision)))
            for key,value in [('status','UNRELEASED'),('version',None),('version_doi',None),('version_doi','10.5281/zenodo.21782008'),('version_doi','10.5281/zenodo.22099128'),('proof_review_approval',None),('public_release_approval',None)]:
                bad=copy.deepcopy(d);bad[key]=value;write(bad);rejected(check)
            bad=copy.deepcopy(d);bad['proof_review_approval']['source_manifest_sha256']='0'*64;write(bad);rejected(check)
            # Automatic Zenodo mint: no invented DOI; protected approvals and
            # exact source custody remain mandatory before release publication.
            url='https://github.com/Apsiape/i3322-exact-wall/releases/tag/v4.1.0'
            (root/'CITATION.cff').write_text('version: 4.1.0\nurl: "'+url+'"\n',encoding='utf-8')
            m['files']=[dict(path=p,bytes=(root/p).stat().st_size,sha256=v.sha(root/p)) for p in v.expected_inventory(root)]
            manifest.write_text(json.dumps(m),encoding='utf-8')
            auto=copy.deepcopy(d);auto.update(doi_mode='zenodo-after-github-release',version_doi=None,release_url=url)
            for field in ['proof_review_approval','public_release_approval','public_inventory_approval']:
                auto[field]['source_manifest_sha256']=v.sha(manifest)
            write(auto);assert check()==4
            rejected(lambda:v.approval(root,'v4.1.0',None,None))
            for key,value in [('doi_mode',None),('version_doi','10.5281/zenodo.21782008'),('version_doi','10.5281/zenodo.99999999'),('release_url',url.replace('4.1.0','4.0.0')),('status','UNRELEASED'),('public_release_approval',None),('public_inventory_approval',None)]:
                bad=copy.deepcopy(auto);bad[key]=value;write(bad);rejected(check)
            write(auto)
            (root/'CITATION.cff').write_text('version: 4.1.0\nurl: "'+url+'"\ndoi: 10.5281/zenodo.21782008\n',encoding='utf-8')
            rejected(check)
        names=[line.split()[-1] for line in ax.read_text().splitlines() if line.startswith('#print axioms ')]
        log=root/'axioms.txt';text='\n'.join("'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"%n for n in names)
        log.write_text(text,encoding='utf-8');assert v.axioms(log,root)==37
        for bad in [text.replace('Quot.sound','sorryAx',1),'\n'.join(text.splitlines()[:-1]),text+'\n'+text.splitlines()[0],text.replace(names[0],'Wrong.name',1)]:
            log.write_text(bad,encoding='utf-8');rejected(lambda:v.axioms(log,root))
    print('PASS: complete raw inventory and tamper/path controls; missing/unapproved/stale metadata and protected approval hashes; exact named axiom inventory and sorryAx rejection. Fixture approval is not real approval.')

if __name__=='__main__':main()
