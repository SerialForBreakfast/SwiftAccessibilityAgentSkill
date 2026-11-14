"""Replay unchanged iOS production bytes with the answer's Bool completion interface."""
import json,re,shutil,subprocess,sys
from pathlib import Path
from run import H,change
base=Path(sys.argv[1]).resolve()
old=base/'iOS-answer'
w=base/'iOS-answer-hook-repair'
w.mkdir()
for name in ('Sources','Tests'):shutil.copytree(old/name,w/name)
shutil.copyfile(old/'Package.swift',w/'Package.swift')
p=w/'Tests/Contract.swift'
s=change(p.read_text(),'var pending: (() -> Void)?, count = 0','var pending: (@MainActor (Bool) -> Void)?, count = 0')
s=change(s,'let cancelled = pending; s.tearDown(); cancelled?()', 'let cancelled = pending; cancelled?(false); XCTAssertEqual(s.state,.open); s.tearDown(); cancelled?(true)')
p.write_text(change(s,'done?(); done?()','done?(true); done?(true)'))
r=json.loads((old/'manifest.json').read_text())
r['inputs']['Tests/Contract.swift']=H(p.read_bytes())
assert all(H((w/name).read_bytes())==h for name,h in r['inputs'].items())
(w/'manifest.json').write_text(json.dumps(r,indent=2))
devices=json.loads(subprocess.check_output(['xcrun','simctl','list','devices','available','-j']))['devices']
device,=[v for k,vs in devices.items() if k.endswith('iOS-26-5') for v in vs if v['name']=='SwiftAccessibility-OS26-Unit-iOS']
args=['xcodebuild','test','-scheme','AccessibilityExamples','-jobs','3','-destination','id='+device['udid'],'-derivedDataPath',str(base/'dd-iOS'),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']
with (w/'first.log').open('xb') as f:
    try:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=240).returncode
    except subprocess.TimeoutExpired:rc=124
b=(w/'first.log').read_bytes();log=b.decode(errors='replace')
r.update(rc=rc,events=re.findall(r"Test Case '-\[([^\]]+)\]' (passed|failed|skipped)",log),
         errors=[line.split(str(w)+'/')[-1][:400] for line in log.splitlines() if 'error:' in line and not line.startswith('    ')],logSHA256=H(b))
(w/'result.json').write_text(json.dumps(r,indent=2));print(r['events'],r['errors'][:2])
