"""Replay first-answer bytes, never repair subject code. Each invocation creates a new attempt."""
from pathlib import Path
import hashlib, json, re, subprocess, tempfile, sys
from zipfile import ZipFile

D = Path(__file__).resolve().parent
root = D.parents[3]
base = root/'evals/results/signal-dismissal-replay'
base.mkdir(exist_ok=True)
out = Path(tempfile.mkdtemp(dir=base))
sha = lambda b: hashlib.sha256(b).hexdigest()
raw = root/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip'
assert sha(raw.read_bytes()) == '9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368'
dest = sys.argv[1]
for case, ident in [('panel','P-34541ce79ee3d519'), ('sheet','P-90629dd9d60ff906')]:
    with ZipFile(raw) as z:
        answer = z.read(f'records/{ident}.skill/answer.txt')
    blocks = re.findall(rb'(?m)^\x60{3}swift\r?\n(.*?)^\x60{3}\s*$', answer, re.S)
    assert len(blocks) == 2
    (out/(case+'.txt')).write_bytes(answer)
    for mode in ['submitted','contract']:
        p = out/case/mode
        source = p/'Sources/YourAppModule/Answer.swift'
        test = p/'Tests/ReplayTests/Tests.swift'
        source.parent.mkdir(parents=True); test.parent.mkdir(parents=True)
        source.write_bytes(blocks[0])
        test.write_bytes(blocks[1] if mode=='submitted' else (D/(case+'.swift')).read_bytes())
        (p/'Package.swift').write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package = Package(name:"Replay",platforms:[.iOS("26.0")],products:[.library(name:"Replay",targets:["YourAppModule"])],targets:[.target(name:"YourAppModule"),.testTarget(name:"ReplayTests",dependencies:["YourAppModule"])])\n')
        args = ['xcodebuild','test','-scheme','Replay','-destination','id='+dest,'-derivedDataPath',str(p/'build'),'-resultBundlePath',str(p/'result.xcresult'),'-parallel-testing-enabled','NO','CODE_SIGNING_ALLOWED=NO']
        meta = dict(case=ident,mode=mode,answer=sha(answer),source=sha(source.read_bytes()),tests=sha(test.read_bytes()),command=args,xcode=subprocess.check_output(['xcodebuild','-version'],text=True).strip(),sdk=subprocess.check_output(['xcrun','--sdk','iphonesimulator','--show-sdk-version'],text=True).strip())
        (p/'intent.json').write_text(json.dumps(meta,indent=2))
        with (p/'first.log').open('xb') as log:
            rc=subprocess.run(args,cwd=p,stdout=log,stderr=subprocess.STDOUT,timeout=600).returncode
        text=(p/'first.log').read_bytes()
        meta.update(exit=rc,log=sha(text),errors=[line.replace(str(p),'<attempt>') for line in text.decode(errors='replace').splitlines() if 'error:' in line][:25])
        (p/'receipt.json').write_text(json.dumps(meta,indent=2))
        print(case,mode,rc,meta['errors'][:2],flush=True)
        if rc and not meta['errors']: raise SystemExit('Unclassified failure; inspect first.log')
print(out)
