"""Stage immutable offline cells and run the host's native XCTest adapter."""
import csv, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path
from zipfile import ZipFile

D = Path(__file__).resolve().parent
R = D.parents[2]
EX = R/'code-examples'
SHEET = R/'evals/native-calibration/sheet-dismissal'
H = lambda b: hashlib.sha256(b).hexdigest()
def read(path): return path.read_text()
def change(s,a,b):
    assert s.count(a)==1, a
    return s.replace(a,b)
def main(bundle, patches=False, cache=None):
    base=Path(tempfile.mkdtemp(prefix='callbacks18-',dir=R/'evals/results'))
    if patches and cache is None:
        # Only reuse compiler intermediates, never a first log, manifest or result.
        complete=[b.parent for b in base.parent.glob('callbacks18-*/results.json')
                  if 'iOS-answer' in json.loads(b.read_bytes())]
        if complete:cache=max(complete,key=lambda b:b.stat().st_mtime)
    print(base,flush=True)
    z=ZipFile(bundle); sub=ZipFile(D.parent/'subjects.zip')
    rows=list(csv.DictReader((D.parent/'grade350/grades.csv').open()))
    def answer(prefix):
        r,=[r for r in rows if r['id'].startswith('Q-'+prefix)]
        b=z.read('raw/'+r['id']+'/answer.txt');assert H(b)==r['answerSHA256']
        return re.findall(r'```swift\n(.*?)```',b.decode(),re.S)
    def starter(prefix,typ):
        r,=[r for r in rows if r['id'].startswith('Q-'+prefix)]
        p=sub.read('questions/'+r['id']+'.md');assert H(p)==r['promptSHA256']
        return next(b for b in re.findall(r'```swift\n(.*?)```',p.decode(),re.S) if 'class '+typ in b)
    x=lambda *args:subprocess.check_output(args,text=True).strip()
    pkg='''// swift-tools-version: 5.9
import PackageDescription
let package=Package(name:"AccessibilityExamples",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"AccessibilityExamples",targets:["AccessibilityExamples"])],targets:[.target(name:"AccessibilityExamples",path:"Sources"),.testTarget(name:"Checks",dependencies:["AccessibilityExamples"],path:"Tests")])
'''
    devices=json.loads(x('xcrun','simctl','list','devices','available','-j'))['devices']
    report={}
    for plat in ['macOS','tvOS','iOS']:
        sdk={'macOS':'macosx','tvOS':'appletvsimulator','iOS':'iphonesimulator'}[plat]
        dest='platform=macOS,arch=arm64';runtime=x('sw_vers','-productVersion');build=x('sw_vers','-buildVersion')
        if plat!='macOS':
            runtime,device=next((k,v) for k,vs in devices.items() if k.endswith(plat+'-26-5') for v in vs if v['name']=='SwiftAccessibility-OS26-Unit-'+plat)
            dest='id='+device['udid'];build=next(r['buildversion'] for r in json.loads(x('xcrun','simctl','list','runtimes','-j'))['runtimes'] if r['identifier']==runtime)
        for v in (['patch'] if patches else ['working','alternative','defect','answer']):
            w=base/(plat+'-'+v);(w/'Sources').mkdir(parents=True);(w/'Tests').mkdir()
            (w/'Package.swift').write_text(pkg)
            (w/'Tests/Contract.swift').write_bytes((D/'ContractTests.swift').read_bytes())
            def source(name,s): (w/'Sources'/(name+'.swift')).write_text(s)
            if plat=='macOS':
                doc=read(EX/'swiftui/macos-v1/Sources/Documents.swift')
                if v=='alternative':
                    doc=doc.replace('private var revision = 0','private final class Lease {}\n    private var revision = Lease()').replace('revision += 1','revision = Lease()').replace('revision == generation','revision === generation')
                if v=='defect':doc=change(doc,'self.revision == generation,','')
                if v=='answer':doc=answer('f32498')[-1]
                if patches:
                    doc=starter('62bbd5','DocumentState')
                    a=doc.index('func action(for'); b=doc.index('\n}',a)
                    doc=doc[:a]+answer('62bbd5')[1]+doc[b:]
                source('Documents',doc)
                if v=='answer':
                    source('Presentation',answer('c6f0a2')[-1]+read(SHEET/'answers/Registration.swift'))
                    test=read(SHEET/'answers/Hosted.swift')
                else:
                    sheet=read(R/'research/evaluation/signal-panel-v3/Presentation.swift')
                    if v=='alternative':
                        sheet=sheet.replace('private var active: UUID?', 'private final class Session {}\n    private var active: Session?').replace('let id = UUID()', 'let id = Session()').replace('self.active == id','self.active === id')
                    if v=='defect':
                        sheet=sheet.replace('private var active: UUID?', 'private var active: UUID?\n    private var latest: (UUID, String)?').replace('active = id','active = id\n        latest = (id, origin)').replace('guard let self, self.active == id','guard let self, let (id, origin) = self.latest, self.active == id')
                    source('Presentation',sheet);test=read(SHEET/'CallbackTests.swift')
                (w/'Tests/Sheet.swift').write_text(test.replace('@testable import Presentation','@testable import AccessibilityExamples'))
            else:
                root=EX/('platforms/'+plat.lower()+'-closure-v1')
                val=read(root/'Sources/AsyncOwnership.swift')
                if v=='alternative':val=change(val,'self.snapshot == input','input.allSatisfy { entry in self.fields[entry.key]?.text == entry.value }'.replace('allSatisfy {','allSatisfy({').replace('value }','value })'))
                if v=='defect':val=read(root/'NegativeFixtures/validation_snapshot.swift')
                if v=='answer':val=starter('1b1d51' if plat=='iOS' else '8b494a','ValidationOwner')
                source('Validation',val)
                if plat=='tvOS':
                    root=EX/'platforms/tvos-results-v1'
                    s=read(root/'Sources/TelevisionResults.swift')
                    if v=='alternative':s=change(s,'self.generation == revision','self.buttons.contains(where: { $0 === button })')
                    if v=='defect':s=read(root/'NegativeFixtures/StaleButton.swift')
                    if v=='answer':s=answer('61e7b4')[-1]
                    if patches:
                        s=starter('20d89c','TelevisionResults')
                        a=s.index('button.addAction('); b=s.index('}, for: .primaryActionTriggered)',a)+len('}, for: .primaryActionTriggered)')
                        s=s[:a]+answer('20d89c')[1]+s[b:]
                    source('Shelf',s)
                else:
                    root=EX/'pilots/uikit-modal-v1'
                    s=read(root/'Sources/ModalUIKit.swift')
                    if v=='alternative':
                        s=change(s,'private var generation = 0','private final class Session {}\n    private var generation = Session()').replace('generation += 1','generation = Session()').replace('generation == token','generation === token')
                    if v=='defect':s=read(root/'NegativeFixtures/EarlyNotification.swift')
                    if v=='answer':s=answer('5376a3')[-1]
                    if patches:
                        s=starter('015170','RestoringPanel')
                        a=s.index('@discardableResult',s.index('return true',s.index('func open(')))
                        b=s.index('private func finish',a)
                        s=s[:a]+answer('015170')[1]+s[b:]
                    source('Panel',s)
                    if v!='answer' and not patches:
                        for prefix in ['c13f93','015170']:
                            text=answer(prefix)[-1]
                            (w/'Tests'/('Submitted'+prefix+'.swift')).write_text('import UIKit\nimport XCTest\n@testable import AccessibilityExamples\n@MainActor final class Submitted'+prefix+': XCTestCase {\n'+text+'\n}\n')
            inputs={str(p.relative_to(w)):H(p.read_bytes()) for p in w.rglob('*.swift')}
            env=dict(platform=plat,runtime=runtime,runtimeBuild=build,sdk=x('xcrun','--sdk',sdk,'--show-sdk-version'),sdkBuild=x('xcrun','--sdk',sdk,'--show-sdk-build-version'),xcode=x('xcodebuild','-version'),deployment='26.0')
            (w/'manifest.json').write_text(json.dumps(dict(inputs=inputs,environment=env),indent=2))
            args=['xcodebuild','test','-scheme','AccessibilityExamples','-jobs','3','-destination',dest,'-derivedDataPath',str((cache or base)/('dd-'+plat)),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']
            with (w/'first.log').open('xb') as f:
                try:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=240).returncode
                except subprocess.TimeoutExpired:rc=124
            data=(w/'first.log').read_bytes();log=data.decode(errors='replace')
            events=re.findall(r"Test Case '-\[([^\]]+)\]' (passed|failed|skipped)",log)
            errors=[line.split(str(w)+'/')[-1][:400] for line in log.splitlines() if 'error:' in line and not line.startswith('    ')]
            record=dict(inputs=inputs,environment=env,rc=rc,events=events,errors=errors,logSHA256=H(data))
            report[w.name]=record;(base/'results.json').write_text(json.dumps(report,indent=2))
            print(w.name,rc,events,errors[:1],flush=True)
            if rc==124 or (rc and not events and (not errors or "xcodebuild: error:" in log)):raise RuntimeError('infrastructure failure; see first.log')
if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle',type=Path)
    parser.add_argument('--patches',action='store_true')
    parser.add_argument('--cache-from',type=Path,help='Reuse only disposable derived data from a completed main batch')
    args=parser.parse_args()
    cache=args.cache_from.resolve() if args.cache_from else None
    if cache:
        assert args.patches and cache.parent == R/'evals/results' and (cache/'results.json').is_file()
    main(args.bundle,args.patches,cache)
