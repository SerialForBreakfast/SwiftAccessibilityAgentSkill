"""Local sequential XCTest jobs; preserve independent first attempts under evals/results."""
import hashlib,json,re,subprocess,sys,tempfile
from pathlib import Path
D=Path(__file__).resolve().parent; R=D.parents[2]; E=R/'code-examples'
out=Path(tempfile.mkdtemp(prefix='decision-v2-',dir=R/'evals/results'))
print(out,flush=True)
def get(*args): return subprocess.check_output(args,text=True).strip()
def h(data): return hashlib.sha256(data).hexdigest()
pkg='// swift-tools-version: 5.9\nimport PackageDescription\nlet package=Package(name:"AccessibilityExamples",platforms:[.macOS("26.0"),.iOS("26.0"),.tvOS("26.0")],products:[.library(name:"AccessibilityExamples",targets:["AccessibilityExamples"])],targets:[.target(name:"AccessibilityExamples",path:"Sources"),.testTarget(name:"Checks",dependencies:["AccessibilityExamples"],path:"Tests")])\n'
dev=json.loads(get('xcrun','simctl','list','devices','available','-j'))['devices']
records=[]
for platform,variant in [('tvOS','working'),('tvOS','missing-enabled'),('macOS','working'),('macOS','id-only'),('iOS','working')]:
    w=out/(platform+'-'+variant);w.mkdir()
    for sub in ['Sources','Tests']: (w/sub).mkdir()
    (w/'Package.swift').write_text(pkg)
    def stage(src,sub,edit=None):
        data=src.read_text()
        if edit:
            old,new=edit;assert data.count(old)==1
            data=data.replace(old,new)
        (w/sub/src.name).write_text(data)
    methods=[]
    if platform!='iOS':stage(D/'FocusTests.swift','Tests')
    if platform=='tvOS':
        stage(E/'platforms/tvos-results-v1/Sources/TelevisionResults.swift','Sources',(', button.isEnabled else',' else') if variant!='working' else None)
        methods=['ShelfChecks/testInstalledActionNeedsCurrentBindingAndEnabledButton']
    elif platform=='macOS':
        stage(E/'swiftui/macos-v1/Sources/Documents.swift','Sources',('self.revision == generation,','') if variant!='working' else None)
        stage(E/'platforms/macos-closure-details-v1/Sources/DesktopRow.swift','Sources')
        reference=(R/'evals/rc2/checks/Contracts.swift').read_text()
        (w/'Sources/Search.swift').write_text(reference[:reference.index('\n@MainActor\nfinal class PlayerControls')])
        methods=['DesktopChecks/testIdenticalValueReplacementRetiresDelete']
        if variant=='working':
            methods+=['DesktopChecks/testConfiguredRowAndIndependentChild','DesktopChecks/testNativeSearchOwner']
            base=E/'platforms/macos-media-v1'
            for file in (base/'Sources').glob('*.swift'):stage(file,'Sources')
            for f in ['MediaMetadataTests.swift','MediaChoiceTests.swift','DescriptionFixture.swift']:
                # Keep generated synthetic clips inside this run.
                stage(base/'Tests'/f,'Tests',('FileManager.default.temporaryDirectory','URL(fileURLWithPath: '+json.dumps(str(w))+')') if f=='DescriptionFixture.swift' else None)
            methods+=['MediaChoiceTests/testSelectFullEnglishSubtitle','MediaChoiceTests/testSubtitleChoiceLeavesAudioUntouched','MediaMetadataTests/testTaggedOptionIsRecognizedWithoutInferringOtherAudio','MediaMetadataTests/testUntaggedAlternateAudioIsNotDescription']
    else:
        base=E/'pilots/uikit-text-v1'
        for sub in ['Sources','Tests']:
            for file in (base/sub).glob('*.swift'):stage(file,sub)
        methods=['TextUIKitTests/testUnicodePrefixProducesExactSelectedText']
    sdk={'iOS':'iphonesimulator','tvOS':'appletvsimulator','macOS':'macosx'}[platform]
    dest='platform=macOS,arch=arm64';runtime=get('sw_vers','-productVersion');build=get('sw_vers','-buildVersion')
    if platform!='macOS':
        (runtime,v),=[(k,v) for k,vs in dev.items() if k.endswith(platform+'-26-5') for v in vs if v['name']=='SwiftAccessibility-OS26-Unit-'+platform]
        dest='id='+v['udid'];build=next(r['buildversion'] for r in json.loads(get('xcrun','simctl','list','runtimes','-j'))['runtimes'] if r['identifier']==runtime)
    args=['xcodebuild','test','-jobs','3','-scheme','AccessibilityExamples','-destination',dest,'-derivedDataPath',str(out/('dd-'+platform)),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']+['-only-testing:Checks/'+m for m in methods]
    rec=dict(platform=platform,variant=variant,methods=methods,runtime=runtime,runtimeBuild=build,sdk=get('xcrun','--sdk',sdk,'--show-sdk-build-version'),xcode=get('xcodebuild','-version'),deployment='26.0',inputs={str(p.relative_to(w)):h(p.read_bytes()) for p in w.rglob('*.swift')})
    (w/'attempt.json').write_text(json.dumps(dict(**rec,command=args),indent=2))
    with (w/'first.log').open('xb') as log:
        try: rc=subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=240).returncode
        except subprocess.TimeoutExpired:rc=124
    data=(w/'first.log').read_bytes();text=data.decode(errors='replace')
    events={s.split('.')[-1]+'/'+m:v for s,m,v in re.findall(r"Test Case '-\[([^ ]+) (\w+)\]' (passed|failed|skipped)",text)}
    diagnostics=[l.split(' : ')[-1] for l in text.splitlines() if ' : XCTAssert' in l and 'failed' in l]
    witness={'missing-enabled':'disabled registration dispatched','id-only':'value equality did not retire old Delete'}.get(variant)
    ok=set(events)==set(methods) and ((rc==0 and set(events.values())=={'passed'}) if not witness else (rc==65 and set(events.values())=={'failed'} and any(witness in l for l in diagnostics)))
    records.append(dict(**rec,exit=rc,events=events,qualified=ok,diagnostics=diagnostics,logSHA256=h(data)))
    (out/'report.json').write_text(json.dumps(records,indent=2)+'\n');print(platform,variant,rc,events,ok,flush=True)
sys.exit(not all(x['qualified'] for x in records))
