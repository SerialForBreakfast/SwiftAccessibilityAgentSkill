"""Sequential XCTest replay. Snapshot inputs and diagnostics in a fresh private attempt."""
import base64, hashlib, json, os, re, subprocess, sys, tempfile
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
platform, mode=sys.argv[1:]
assert platform in ('iOS','tvOS') and mode in ('positive','alternative','mutant')
def cmd(*args):return subprocess.check_output(args,text=True).strip()
devices=json.loads(cmd('xcrun','simctl','list','devices','booted','-j'))['devices']
device,=[d for d in devices['com.apple.CoreSimulator.SimRuntime.'+platform+'-26-5'] if d['name']=='SwiftAccessibility-OS26-Unit-'+platform and d['state']=='Booted']
base=ROOT/'evals/results/signal-v3-native';base.mkdir(exist_ok=True)
out=Path(tempfile.mkdtemp(prefix=platform+'-'+mode+'-',dir=base))
src=out/'Sources/Contracts';tests=out/'Tests/ContractsTests'
src.mkdir(parents=True);tests.mkdir(parents=True)
examples=ROOT/'code-examples'
paths=[examples/f'swiftui/media-{platform.lower()}-v2/Sources/MediaSelection.swift']
if platform=='iOS': paths += [D/'Presentation.swift',examples/'pilots/uikit-modal-v1/Sources/ModalUIKit.swift',examples/'swiftui/forwarding-ios-v1/Sources/NativeSurface.swift']
mutants={'ModalUIKit.swift':('background?.accessibilityElementsHidden = priorHidden','if notify { background?.accessibilityElementsHidden = true } else { background?.accessibilityElementsHidden = priorHidden }'),
'Presentation.swift':('self.active == id','self.active != nil'),
'NativeSurface.swift':('self.generation == ticket,',''),
'MediaSelection.swift':('item.select(choice.option, in: group)','_ = choice.option')}
for p in paths:
    s=p.read_text()
    if mode=="alternative":
        from alternatives import apply
        s=apply(p.name,s)
    if mode=='mutant':
        old,new=mutants[p.name];assert s.count(old)==1;s=s.replace(old,new)
    (src/p.name).write_text(s)
(tests/'ContractTests.swift').write_bytes((D/'ContractTests.swift').read_bytes())
fixture=examples/f'swiftui/media-{platform.lower()}-v2/Tests/DescriptionFixture.swift'
(tests/'sample.mov').write_bytes(base64.b64decode(re.search(r'let positive = """(.*?)"""',fixture.read_text(),re.S)[1]))
(out/'Package.swift').write_text('// swift-tools-version: 6.0\nimport PackageDescription\nlet package = Package(name:"Contracts", platforms:[.iOS("26.0"), .tvOS("26.0")], products:[.library(name:"Contracts",targets:["Contracts"])], targets:[.target(name:"Contracts"), .testTarget(name:"ContractsTests",dependencies:["Contracts"],exclude:["sample.mov"])])\n')
names=['testPickerWritesPlayerItem']+(['testPanelReopen','testSheetCallback','testRetainedWrapperAction'] if platform=='iOS' else [])
args=['xcodebuild','test','-scheme','Contracts','-destination','id='+device['udid'],'-derivedDataPath',str(out/'build'),'-resultBundlePath',str(out/'tests.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','CODE_SIGNING_ALLOWED=NO']
summary=dict(platform=platform,mode=mode,destination=device['name'],runtime='26.5',deployment='26.0',xcode=cmd('xcodebuild','-version'),sdk=cmd('xcrun','--sdk','iphonesimulator' if platform=='iOS' else 'appletvsimulator','--show-sdk-version'),inputs={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob('*') if p.is_file()},command=args)
(out/'intent.json').write_text(json.dumps(summary,indent=2))
with (out/'native.log').open('w') as log:
    run=subprocess.run(args,cwd=out,stdout=log,stderr=subprocess.STDOUT,timeout=600)
log=(out/'native.log').read_text()
status={n:re.findall(r"Test Case '[^'\n]*"+n+r"\]' (passed|failed)",log) for n in names}
expected='failed' if mode=='mutant' else 'passed'
ok=all(v==[expected] for v in status.values()) and run.returncode==(65 if mode=='mutant' else 0)
if mode=='mutant':
    for n,msg in zip(['testPickerWritesPlayerItem','testPanelReopen','testSheetCallback','testRetainedWrapperAction'],['native caption write','final background snapshot','obsolete modifier callback','old installed action']):
        if n in names: ok &= any(n in line and msg in line for line in log.splitlines())
summary.update(tests=status,exit=run.returncode,accepted=ok,artifacts=str(out.relative_to(ROOT)))
(out/'receipt.json').write_text(json.dumps(summary,indent=2));print(out,status,ok,flush=True)
sys.exit(0 if ok else 1)
