"""Check six frozen source/test pairs against real SDKs; do not execute model code."""
import json,re,subprocess,tempfile,zipfile
from pathlib import Path
from build import D,R,H,build
outputs=build()
board=json.loads(outputs['controller/board.json']);out=Path(tempfile.mkdtemp(dir=R/'evals/results',prefix='rc2-direct-'))
print(out,flush=True)
rows=[]
for r in board:
    if r['lane']!='rc2-direct':continue
    case=r['id'];w=out/case;w.mkdir();file=D/'subjects'/(case+'.zip');assert H(file.read_bytes())==r['sha256']
    with zipfile.ZipFile(file) as z:z.extractall(w)
    mac=r['platform']=='macOS';sdk='macosx' if mac else 'iphonesimulator'
    dev=Path(subprocess.check_output(['xcrun','--sdk',sdk,'--show-sdk-platform-path'],text=True).strip())/'Developer'
    args=['xcrun','--sdk',sdk,'swiftc','-swift-version','5','-target','arm64-apple-'+('macos26.0' if mac else 'ios26.0-simulator'),'-module-cache-path',str(out/'cache'),'-F',str(dev/'Library/Frameworks'),'-I',str(dev/'usr/lib')]
    src=w/'Sources/Feature/Feature.swift';test=w/'Tests/Checks/Checks.swift'
    for lane,cmd in [('source',['-emit-module','-enable-testing','-module-name','Feature','-emit-module-path',str(w/'Feature.swiftmodule'),str(src)]),('tests',['-typecheck','-I',str(w),str(test)])]:
        proc=subprocess.run(args+cmd,capture_output=True,timeout=150);log=proc.stdout+proc.stderr;(w/(lane+'.log')).write_bytes(log)
        bad=(r['family'],r['mode'],lane)==('Inspector','repair','tests')
        assert (proc.returncode!=0)==bad and (not bad or b'Equatable' in log),(case,lane,log[-1000:])
        rows.append(dict(id=case,archive=r['sha256'],family=r['family'],variant=r['mode'],lane=lane,exit=proc.returncode,diagnostic=next(iter(re.findall(r': error: ([^\n]+)',log.decode())),None)))
    print(r['family'],r['mode'],'verified',flush=True)
(out/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
