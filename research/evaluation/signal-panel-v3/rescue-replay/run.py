"""Offline first attempts only. No rewriting diagnostics or returned Swift."""
import hashlib,json,re,subprocess,tempfile,sys
from pathlib import Path
from zipfile import ZipFile
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
H=lambda b:hashlib.sha256(b).hexdigest()
base=ROOT/'evals/results/nine-rescues';base.mkdir(exist_ok=True)
run=Path(tempfile.mkdtemp(dir=base));print(run,flush=True)
def sealed(path,seal):
    assert H(path.read_bytes())==seal
    return ZipFile(path)
ret=sealed(ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip','9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368')
pkt=sealed(D.parents[1]/'signal-panel-v2/held.zip','51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd')
panel={r['id']:r for r in json.loads(pkt.read('controller/panel.json'))}
cases=[r for r in json.loads(ret.read('transitions.json')) if r['transitions']['whole']=='rescue']
assert len(cases)==9
def blocks(s):return re.findall(r'(?ms)^`{3}(swift|diff)\n(.*?)^`{3}[ \t]*$',s)
def method(s,name):
    m=re.search(r'(?m)^.*?func '+name+r'\(',s);assert m,name
    start=m.start();depth=1
    for end in range(m.end(),len(s)):
        depth+=(s[end]=='(')-(s[end]==')')
        if not depth:break
    n=s.index('{',end);depth=1
    for j in range(n+1,len(s)):
        depth+=(s[j]=='{')-(s[j]=='}')
        if not depth:return s[start:j+1]
    raise ValueError(name)
def cmd(*a):return subprocess.check_output(a,text=True).strip()
devices=json.loads(cmd('xcrun','simctl','list','devices','booted','-j'))['devices']
dests={'macOS':'platform=macOS,arch=arm64'}
for platform in ('iOS','tvOS'):
    d,=[d for d in devices['com.apple.CoreSimulator.SimRuntime.'+platform+'-26-5'] if d['name']=='SwiftAccessibility-OS26-Unit-'+platform]
    dests[platform]='id='+d['udid']
for r in cases:
 if len(sys.argv)>1 and r['id'][2:6] not in sys.argv[1:]:continue
 for arm in ('unaided','skill'):
    i=r['id']; k=i[2:6];platform=r['platform'];p=run/(i+'.'+arm);p.mkdir()
    ans=ret.read(f'records/{i}.{arm}/answer.txt'); (p/'answer.txt').write_bytes(ans)
    question=pkt.read('subjects/'+i+'.txt');(p/'question.txt').write_bytes(question)
    meta=dict(id=i,arm=arm,family=r['family'],platform=platform,answer=H(ans),question=H(question),binding=panel[i]['assertions'],runtime=cmd('sw_vers','-productVersion') if platform=='macOS' else '26.5',xcode=cmd('xcodebuild','-version'),sdk=cmd('xcrun','--sdk',{'macOS':'macosx','iOS':'iphonesimulator','tvOS':'appletvsimulator'}[platform],'--show-sdk-version'),deployment='26.0')
    save=lambda:(p/'receipt.json').write_text(json.dumps(meta,indent=2))
    if k=='e56a':
        meta.update(result='source-only',reason='Product layout and OS availability; no executable starter or named native assertion.');save();continue
    a=[b for _,b in blocks(ans.decode())];q=blocks(question.decode());s=q[0][1] if q else ''
    note='Retain supplied starter as recommended'
    if k in ('a5c8','4328','76d9','b435') and (arm=='unaided' or k=='b435'):
        s=a[0 if k=='a5c8' or arm=='skill' else 1];note='Integrate full returned implementation'
    if k=='9ae5':
        s=s[:s.index('@MainActor public enum EditActionFactory')]+a[int(arm=='skill')];note='Replace starter factory with returned declaration'
    if k=='d2dd':
        if arm=='unaided':
            line=next(l[1:] for l in a[0].splitlines(True) if l.startswith('- ') );assert s.count(line)==1;s=s.replace(line,'')
        else:
            old='    @discardableResult\n'+method(s,'dismiss');assert s.count(old)==1;s=s.replace(old,a[0].rstrip('\n'))
        note='Apply supplied one-line diff or exact replacement method'
    if k=='b12c':s='\n'.join(a);note='Compile supplied Swift fences in order; no native assertion is registered'
    src=p/'Sources/AccessibilityExamples/Implementation.swift';src.parent.mkdir(parents=True);src.write_text(s)
    tests=p/'Tests/ReplayTests/Contract.swift';tests.parent.mkdir(parents=True)
    check='';extras=''
    if meta['binding']:
        cls,name=meta['binding'][0].split('/')
        file=ROOT/Path(panel[i]['source']).parent/'Tests'/(cls+'.swift')
        history=file.read_text()
        helpers={'4328':['row','configure'],'d2dd':['open'],'7d27':['setup','hint']}.get(k,[])
        check=(' private var testOwners: [SurfaceOwner] = []\n' if k=='7d27' else '')+'\n'.join(method(history,x) for x in helpers+[name])
        meta.update(oracleFile=str(file.relative_to(ROOT)),oracleHash=H(file.read_bytes()),assertionHash=H(method(history,name).encode()))
        if k=='9ae5':
            extras='func testRequestedStates() { for grouped in [false,true] { let a = EditActionFactory.make(title:NSAttributedString(string:"Rename"),grouped:grouped){ _ in true }; XCTAssertEqual(a.category, grouped ? UIAccessibilityCustomAction.editCategory : nil) } }'
        if k in ('b435','76d9'):
            extras='func testLiveDispatch() { let r=DesktopRow(); var ids=[String](); r.choose={ids.append($0)}; for b in [true,false] {r.configure(id:b ? "A":"B",title:"Open",selected:b,expanded:b); XCTAssertEqual(r.isAccessibilitySelected(),b); r.open.performClick(nil)}; XCTAssertEqual(ids,["A","B"]) }'
    tests.write_text('import XCTest\nimport '+('AppKit' if platform=='macOS' else 'UIKit')+'\n@testable import AccessibilityExamples\n@MainActor final class ReplayTests: XCTestCase {\n'+check+'\n'+extras+'\n}\n')
    (p/'Package.swift').write_text('// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"Replay",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"Replay",targets:["AccessibilityExamples"])],targets:[.target(name:"AccessibilityExamples"),.testTarget(name:"ReplayTests",dependencies:["AccessibilityExamples"])])\n')
    args=['xcodebuild','test' if check else 'build','-scheme','Replay','-destination',dests[platform],'-derivedDataPath',str(p/'build'),'-resultBundlePath',str(p/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','CODE_SIGNING_ALLOWED=NO']
    meta.update(integration=note,source=H(src.read_bytes()),tests=H(tests.read_bytes()),command=args)
    (p/'intent.json').write_text(json.dumps(meta,indent=2))
    with (p/'first.log').open('xb') as log:
        rc=subprocess.run(args,cwd=p,stdout=log,stderr=subprocess.STDOUT,timeout=600).returncode
    log=(p/'first.log').read_bytes();txt=log.decode(errors='replace')
    methods=dict(re.findall(r"Test Case '.*? (test\w+)\]' (passed|failed)",txt))
    errors=[l.replace(str(p),'<stage>') for l in txt.splitlines() if 'error:' in l]
    result='assertion-fail' if 'failed' in methods.values() else 'unit-pass' if methods and not rc else 'compile-pass' if not rc and not check else 'compile-error' if errors else 'harness-gap'
    meta.update(result=result,methods=methods,exit=rc,log=H(log),diagnostics=errors);save();print(k,arm,result,methods,errors[:1],flush=True)
    if result=='harness-gap':raise RuntimeError('Unclassified infrastructure outcome')
