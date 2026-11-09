"""Run independent lanes in sequence with disposable staging and immutable first receipts."""
import json,re,sys,subprocess,shutil,hashlib,os
from pathlib import Path
from stage import D,ROOT,H
run=ROOT/'evals/results/persistent-replay'/sys.argv[1]
def read(*a):return subprocess.check_output(a,text=True).strip()
devices=json.loads(read('xcrun','simctl','list','devices','booted','-j'))['devices']
env={}
for plat,sdk in [('macOS','macosx'),('iOS','iphonesimulator'),('tvOS','appletvsimulator')]:
    dest='platform=macOS,arch=arm64'
    if plat!='macOS':
        d,=[d for d in devices['com.apple.CoreSimulator.SimRuntime.'+plat+'-26-5'] if d['name']=='SwiftAccessibility-OS26-Unit-'+plat]
        dest='id='+d['udid']
    env[plat]=dict(xcode=read('xcodebuild','-version'),sdk=read('xcrun','--sdk',sdk,'--show-sdk-version'),destination=dest,deployment='26.0',runtime=read('sw_vers','-productVersion') if plat=='macOS' else '26.5')
def save(path,r):
    with path.open('x') as f:json.dump(r,f,indent=2)
if (run/'environment.json').exists():
    assert json.loads((run/'environment.json').read_text())==env
else:save(run/'environment.json',env)
for c in sorted(run.glob('P-*')):
    r=json.loads((c/'input.json').read_text());plat=r['platform'];module=r['module']
    assert all(H((c/n).read_bytes())==v for n,v in r['inputs'].items())
    for lane in ['contract','proof']:
        target=c/(lane+'.json')
        if target.exists():continue
        if (c/(lane+'-intent.json')).exists():
            log=c/(lane+'.log')
            save(target,dict(lane=lane,environment=plat,status='orchestrator-interrupted',log=H(log.read_bytes())))
            continue
        files=([c/'Contract.swift'] if (c/'Contract.swift').exists() else []) if lane=='contract' else sorted(c.glob('Proof*.swift'))
        result=dict(lane=lane,environment=plat)
        if not (c/'Subject.swift').exists(): reason={'G':'ambiguous-partial-patch','N':'source-only'}[r['selection']]
        elif lane=='proof' and not files:reason='no-executable-proof'
        elif lane=='proof' and json.loads((c/'contract.json').read_text())['status']=='subject-compile-failure':reason='blocked-by-identical-subject'
        elif lane=='contract' and r['selection']=='T':reason='no-bound-assertion'
        else:reason=None
        if reason:save(target,dict(**result,status=reason));continue
        w=run/'work'/plat;w.mkdir(parents=True,exist_ok=True)
        src=w/'Sources'/module;tests=w/'Tests/Checks'
        # Working directories only. The input and both first receipts stay outside work/.
        for d in (w/'Sources',w/'Tests'):
            if d.exists():shutil.rmtree(d)
        src.mkdir(parents=True);tests.mkdir(parents=True)
        shutil.copyfile(c/'Subject.swift',src/'Subject.swift')
        for f in files:shutil.copyfile(f,tests/f.name)
        (tests/'Empty.swift').write_text('')
        manifest=f'// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"Replay",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"Replay",targets:["{module}"])],targets:[.target(name:"{module}"),.testTarget(name:"Checks",dependencies:["{module}"])])\n'
        (w/'Package.swift').write_text(manifest)
        args=['xcodebuild','test' if files else 'build','-scheme','Replay','-destination',env[plat]['destination'],'-derivedDataPath',str(w/'dd'),'-resultBundlePath',str(c/(lane+'.xcresult')),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','CODE_SIGNING_ALLOWED=NO']
        offline_only=files and any(re.search(r'URL\s*\(\s*string:|URLSession|https?://',f.read_text()) for f in [c/'Subject.swift',*files])
        if offline_only:args[1]='build-for-testing'
        save(c/(lane+'-intent.json'),dict(command=args,manifest=manifest,source=H((src/'Subject.swift').read_bytes()),checks=[H(f.read_bytes()) for f in files]))
        logpath=c/(lane+'.log')
        with logpath.open('xb') as log:
            try:rc=subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=240).returncode
            except subprocess.TimeoutExpired:rc=124
        data=logpath.read_bytes();s=data.decode(errors='replace')
        errors=[l.replace(str(w),'<work>') for l in s.splitlines() if ': error:' in l and ('/Tests/' in l or '/Sources/' in l)]
        ran=bool(re.search(r"Test Case '.*?' (passed|failed)|Test .+ (passed|failed) after",s))
        trap=bool(re.search(r'(?m)^.*?(?:Assertion failed|Fatal error):?',s)) and 'Restarting after unexpected exit' in s
        if rc==124:status='harness-timeout'
        elif rc==0:status='offline-build-only' if offline_only else 'unit-pass' if ran else 'compile-only' if not files else 'no-tests-discovered'
        elif any('/Sources/' in l for l in errors):status='subject-compile-failure'
        elif ran or trap:status='unit-failure'
        elif errors:status='test-compile-failure'
        else:status='harness-error'
        save(target,dict(**result,status=status,exit=rc,log=H(data),diagnostics=list(dict.fromkeys(errors))[:6]))
        print(c.name,lane,status,flush=True)
        if status=='harness-error' and ('Unable to find a destination' in s or 'No space left on device' in s):raise RuntimeError(status)
