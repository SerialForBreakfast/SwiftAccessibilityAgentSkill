"""Materialize clean standalone developer packages or a batch linkage suite (no controller content)."""
from common import *
import argparse,subprocess,tempfile
SHARED='// swift-tools-version: 5.9\nimport PackageDescription\n'
SDK={'iOS':'.iOS','tvOS':'.tvOS','macOS':'.macOS'}
def sources():
    with questions() as q:
        for r in PANEL:
            i=r['id']; raw=q.read('subjects/'+i+'.txt')
            assert H(raw)==r['questionSHA256']
            s=blocks(raw.decode())
            scaffold=D/'scaffolds'/(i[2:6]+'.swift')
            if not s and not scaffold.exists():continue
            assert len(s)<=1 and not (s and scaffold.exists())
            yield r,raw,s[0].encode() if s else scaffold.read_bytes()
def make(w,rows):
    targets=[]; deps=[]; imports=[];plat=rows[0][0]['platform']
    for r,q,data in rows:
        mod='Starter'+r['id'][2:]; deps.append('"'+mod+'"'); imports.append('import '+mod)
        p=w/'Sources'/mod;p.mkdir(parents=True)
        (p/'Starter.swift').write_bytes(data)
        targets.append('.target(name: "'+mod+'")')
        if len(rows)==1:(w/'QUESTION.md').write_bytes(q)
    targets.append('.testTarget(name:"Linkage",dependencies:['+','.join(deps)+'])')
    (w/'Package.swift').write_text(SHARED+f'let package=Package(name:"Starters",platforms:[{SDK[plat]}("26.0")],products:[.library(name:"Starters",targets:['+','.join(deps)+'])],targets:['+','.join(targets)+'])\n')
    t=w/'Tests/Linkage';t.mkdir(parents=True)
    (t/'Linkage.swift').write_text('\n'.join(imports)+'\nimport XCTest\nfinal class Linkage: XCTestCase { func testModulesLoad() {} }\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--case');a=ap.parse_args()
    base=ROOT/'evals/results/qualification-56';base.mkdir(exist_ok=True)
    out=Path(tempfile.mkdtemp(prefix='starters-',dir=base));print(out.name,flush=True)
    if a.case:
        row,=[v for v in sources() if v[0]['id']==a.case];make(out,[row]);return
    env=json.loads((BASE/'v4-paired-jwlc74x4/environment.json').read_bytes())
    for plat in SDK:
        rows=[x for x in sources() if x[0]['platform']==plat];w=out/plat;make(w,rows)
        args=['xcodebuild','test','-scheme','Starters','-destination',env[plat]['destination'],'-derivedDataPath',str(w/'dd'),'-resultBundlePath',str(w/'result.xcresult'),'-parallel-testing-enabled','NO','CODE_SIGNING_ALLOWED=NO']
        inputs={str(p.relative_to(w)):H(p.read_bytes()) for p in w.rglob('*') if p.is_file()}
        intent=dict(args=args,inputs=inputs,xcode=subprocess.check_output(['xcodebuild','-version'],text=True))
        (w/'intent.json').write_text(json.dumps(intent,indent=2))
        with (w/'native.log').open('xb') as f: rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=300).returncode
        data=(w/'native.log').read_bytes()
        (w/'receipt.json').write_text(json.dumps(dict(exit=rc,log=H(data),intent=H((w/'intent.json').read_bytes())),indent=2))
        print(plat,len(rows),rc,flush=True)
if __name__=='__main__':main()
