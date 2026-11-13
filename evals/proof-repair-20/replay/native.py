"""One independent test target per submission, identical test bytes in three builds."""
import json,re,subprocess,sys,time,shutil,hashlib
from pathlib import Path
from stage import D,base,owners,R
H=lambda b:hashlib.sha256(b).hexdigest()
def main():
 extra='--extra' in sys.argv
 for i in sorted(json.loads((D/'inventory.json').read_text())['types']):
    while True:
        rows=json.loads((D/('extra.json' if extra else 'preflight.json')).read_text())
        if extra:break
        if any(x['case']==i for x in rows):break
        time.sleep(3)
    rows=[x for x in rows if x['case']==i and x['status']=='ready']
    if not rows:continue
    for v in ('working','alternative','defect'):
        w=D/('native-extra' if extra else 'native')/i/v;w.mkdir(parents=True,exist_ok=False)
        platform=rows[0]['platform']; targets=[]; prod=base/i/v/'Sources'
        rec=next(x for x in json.loads((R/'evals/proof-repair-20/evidence.json').read_text()) if x['id']==i)
        orig=json.loads((base/i/'case.json').read_text());assert H((base/i/v/orig['replacementTarget']).read_bytes())==rec['variants'][v]
        for alias in sorted({x['alias'] for x in rows}):
            shutil.copytree(prod,w/'Sources'/alias)
            targets.append('.target(name:"'+alias+'")')
        for x in rows:
            h=x['hash'];t='T'+h[:12]; alias=x['alias']
            dest=w/'Tests'/t;dest.mkdir(parents=True)
            b=(D/'blocks'/(h+'.swift')).read_bytes();file=(D/'preflight'/i/(h+'.swift')).read_bytes(); assert b in file and H(b)==h
            (dest/'Submission.swift').write_bytes(file)
            targets.append('.testTarget(name:"'+t+'",dependencies:["'+alias+'"])')
        (w/'Package.swift').write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"Replay",platforms:[.iOS("26.0"),.macOS("26.0"),.tvOS("26.0")],targets:['+','.join(targets)+'])\n')
        dest={'iOS':'id=2B4E2AF3-2753-4B30-B312-01FE20E5F462','tvOS':'id=E4B1D7C1-467B-4B09-991B-4D9E500CC26D','macOS':'platform=macOS,arch=arm64'}[platform]
        # Multi-product SwiftPM packages expose a package-wide scheme.
        schemes=json.loads(subprocess.check_output(['xcodebuild','-list','-json'],cwd=w,stderr=subprocess.DEVNULL))['workspace']['schemes']
        scheme='Replay-Package' if 'Replay-Package' in schemes else ('Replay' if 'Replay' in schemes else rows[0]['alias'])
        args=['xcodebuild','test','-scheme',scheme,'-destination',dest,'-jobs','4','-derivedDataPath',str(D/(('dd-extra-' if extra else 'dd-')+platform)),'-resultBundlePath',str(w/'native.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']
        with (w/'native.log').open('xb') as log:
            try:rc=subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=500).returncode
            except subprocess.TimeoutExpired:rc=124
        out=call_report(w)
        (w/'native.json').write_text(json.dumps(dict(rc=rc,scheme=scheme,schemes=schemes,ids=[x['hash'] for x in rows],report=out),indent=1))
        print(i,v,len(rows),rc,scheme,len(out.get('testNodes',[])),flush=True)
def call_report(w):
    p=subprocess.run(['xcrun','xcresulttool','get','test-results','tests','--compact','--path',str(w/'native.xcresult')],capture_output=True)
    return json.loads(p.stdout) if not p.returncode else {}
if __name__=='__main__':main()
