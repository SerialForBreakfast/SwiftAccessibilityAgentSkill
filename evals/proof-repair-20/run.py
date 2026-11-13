"""Run a prepared triplet without overwriting trials; preserve its native diagnostics."""
import json,re,subprocess,sys
from pathlib import Path
from prepare import H,J
base=Path(sys.argv[1]).resolve()
anchors=json.loads(subprocess.check_output(['xcrun','simctl','list','devices','available','-j']))['devices']
rt={r['identifier']:r['buildversion'] for r in json.loads(subprocess.check_output(['xcrun','simctl','list','runtimes','-j']))['runtimes']}
version=subprocess.check_output(['xcodebuild','-version'],text=True).strip()
for case in sorted(base.glob('Q*/case.json')):
    if len(sys.argv)>2 and case.parent.name not in sys.argv[2:]:continue
    a=json.loads(case.read_bytes());p=a['platform'];runtime=subprocess.check_output(['sw_vers','-productVersion'],text=True).strip()
    build=subprocess.check_output(['sw_vers','-buildVersion'],text=True).strip();dest='platform=macOS,arch=arm64'
    if p!='macOS':
        [(runtime,device)]=[(k,v) for k,vs in anchors.items() if k.endswith(p+'-26-5') for v in vs if v['name']==f'SwiftAccessibility-OS26-Unit-{p}']
        dest='id='+device['udid'];build=rt[runtime]
    sdk={'macOS':'macosx','tvOS':'appletvsimulator','iOS':'iphonesimulator'}[p]
    for v in ('working','alternative','defect'):
        w=case.parent/v;files={str(f.relative_to(w)):H(f.read_bytes()) for f in [w/'Package.swift',*w.glob('Sources/*.swift'),*w.glob('Tests/*.swift')]}
        assert files['Tests/CurrentTests.swift']==a['proofSHA256']
        args=['xcodebuild','test','-jobs','3','-scheme','AccessibilityExamples','-destination',dest,'-derivedDataPath',str(base/('dd-'+p)),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']
        with (w/'first.log').open('xb') as log:
            try:rc=subprocess.run(args,cwd=w,stdout=log,stderr=subprocess.STDOUT,timeout=240).returncode
            except subprocess.TimeoutExpired:rc=124
        data=(w/'first.log').read_bytes();s=data.decode(errors='replace');events=re.findall(r"Test Case '[^'\n]* testCurrentBehavior\]' (passed|failed|skipped)",s)
        errors=[l.split('CurrentTests.swift:',1)[1] for l in s.splitlines() if 'CurrentTests.swift:' in l and 'error:' in l and 'testCurrentBehavior]' in l]
        lines=(w/'Tests/CurrentTests.swift').read_text().splitlines()
        witness=[lines[int(m[1])-1].strip() for l in errors if (m:=re.match(r'(\d+):',l))]
        record=dict(id=a['id'],variant=v,exit=rc,events=events,witness=witness,diagnostics=errors,inputHashes=files,logSHA256=H(data),platform=p,runtime=runtime,runtimeBuild=build,deployment=a['deploymentTarget'],sdk=subprocess.check_output(['xcrun','--sdk',sdk,'--show-sdk-version'],text=True).strip(),sdkBuild=subprocess.check_output(['xcrun','--sdk',sdk,'--show-sdk-build-version'],text=True).strip(),xcode=version)
        (w/'result.json').write_text(J(record));print(a['id'],v,rc,events,witness[:1],flush=True)
