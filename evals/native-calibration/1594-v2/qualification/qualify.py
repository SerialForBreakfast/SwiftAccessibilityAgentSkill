"""One immutable first attempt per controller-authored Q082-B fixture."""
from pathlib import Path
import hashlib, io, json, subprocess, sys, zipfile

here = Path(__file__).resolve().parent
root = here.parents[3]
held = root / 'evals/results/1594-v2-held'
out = root / 'evals/results/1594-q082b-qualification'
sha = lambda data: hashlib.sha256(data).hexdigest()
def checked(name, seal):
    raw = (held / name).read_bytes()
    assert sha(raw) == seal
    return zipfile.ZipFile(io.BytesIO(raw))

ctrl = checked('controller.zip', '7fc8785e3780c107f1acbe3441a0000b4814251955eff7f63d760af7cc743df5')
subjects = checked('subjects.zip', '14f6c34034e3be6757928311aa7e30e962708c5af054603fec7679c900acd84b')
subject = zipfile.ZipFile(io.BytesIO(subjects.read('Q082-B.zip')))
def source(role):
    return ctrl.read(f'Q082-B/{role}/Sources/DesktopLifecycle.swift')
ref = source('reference')
before = b'let target = eligible(primary) ? primary : eligible(fallback) ? fallback : nil'
after = b'let target = [primary, fallback].compactMap { $0 }.first(where: { eligible($0) })'
assert ref.count(before) == 1
test = (here / 'RejectionTests.swift').read_bytes()
out.mkdir(exist_ok=False)
env = {k:subprocess.check_output(v,text=True).strip() for k,v in
       {'macOS':['sw_vers','-productVersion'], 'runtimeBuild':['sw_vers','-buildVersion'],
        'xcode':['xcodebuild','-version'], 'sdk':['xcrun','--show-sdk-version'],
        'swift':['swift','--version']}.items()}
results = {}
for role, code in [('reference',ref), ('alternative',ref.replace(before,after)), ('defect',source('defect'))]:
    w = out / role
    for name, data in [('Package.swift',subject.read('Package.swift')),
                       ('Sources/DesktopLifecycle.swift',code), ('Tests/RejectionTests.swift',test)]:
        path = w / name
        path.parent.mkdir(exist_ok=True,parents=True)
        path.write_bytes(data)
    cmd = ['swift','test','--disable-automatic-resolution','--jobs','2','--filter','RejectionTests']
    attempt = dict(role=role,command=cmd,sourceSHA=sha(code),testSHA=sha(test),environment=env)
    (w/'attempt.json').write_text(json.dumps(attempt,indent=2))
    with (w/'first.log').open('xb') as f:
        try: rc = subprocess.run(cmd,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=240).returncode
        except subprocess.TimeoutExpired: rc = 124
    raw = (w/'first.log').read_bytes()
    lines = raw.decode(errors='replace').splitlines()
    traces = [l.strip() for l in lines if l.startswith('Q082B ')]
    expected = ['Q082B primaryAccepts=true requests=primary result=true',
                'Q082B primaryAccepts=false requests=' + ('primary,fallback result=true' if role=='defect' else 'primary result=false')]
    events = [l for l in lines if "Test Case '-[" in l and (' passed (' in l or ' failed (' in l)]
    errors = [l for l in lines if 'error:' in l]
    matches = (sorted(traces)==sorted(expected) and len(events)==2 and
               any('testOrdinaryAcceptance]' in l and ' passed (' in l for l in events) and
               any('testRejectedPrimary]' in l and (' failed (' if role=='defect' else ' passed (') in l for l in events) and
               (rc==1 and len(errors)==2 and all('testRejectedPrimary' in l for l in errors)
                if role=='defect' else rc==0 and not errors))
    results[role]=dict(**attempt,exit=rc,logSHA=sha(raw),traces=traces,events=events,errors=errors,matches=matches)
    (w/'result.json').write_text(json.dumps(results[role],indent=2))
    print(role, rc, traces, matches,flush=True)
(out/'results.json').write_text(json.dumps(results,indent=2))
sys.exit(not all(r['matches'] for r in results.values()))
