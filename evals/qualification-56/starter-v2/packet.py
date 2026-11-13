"""Export an isolated subject package or qualify copies with controller-only checks."""
import argparse, hashlib, json, re, subprocess, sys, tempfile, zipfile
from pathlib import Path

D = Path(__file__).resolve().parent
R = D.parents[2]
OUT = R/'evals/results'
sys.path.insert(0, str(D.parent))
from common import questions, blocks

CASES = {'4ec9':'iOS','5d12':'tvOS','6d2d':'iOS','c04c':'iOS','c6b2':'tvOS','f483':'macOS',
         '4840':'macOS','da78':'macOS'}
H = lambda b: hashlib.sha256(b).hexdigest()
def files(k):
    sheet = k in ('4840','da78')
    with questions() as z:
        name, = [n for n in z.namelist() if n.startswith('subjects/P-'+k)]
        raw = z.read(name); source, = blocks(raw.decode())
    assert H(raw)[:16] in name
    prompt=raw.decode().split('```')[0].rstrip()
    # The complete current file is supplied as a package member, not a dangling inline fence.
    if sheet:
        prompt=prompt.split('Interop.swift:')[0].split('Presentation.swift:')[0].rstrip()
        prompt=re.sub(r'\n[\w]+\.swift:$','',prompt)
        source = source.split('struct SheetExample: View {')[0]+(D/'SheetSurface.swift').read_text()
        extra='Use the callbacks on the registrations actually installed by the host: deliver an earlier dismissal after a replacement opens, then deliver the replacement dismissal twice.'
    else:
        prompt=re.sub(r'Here is the complete current (?:implementation|file):\s*$','',prompt)
        extra='Use the supplied local CaptionFixture instead of remote URLs. Open independent items with selected: .ordinary or .forced. Inspect the item’s native legible and audible selections before and after the interaction.'
    data={'QUESTION.md':(prompt+'\n\n'+extra+' The complete starter is in Sources/Starter. Put your focused unit checks in Tests/Checks.\n').encode(),
          'Sources/Starter/Starter.swift':source.encode(),
          'Tests/Checks/Checks.swift':b'import XCTest\n@testable import Starter\n'}
    resource=''
    if not sheet:
        movie=(D/'Captions.mov').read_bytes()
        assert H(movie)=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3'
        data.update({'Sources/Starter/Captions.mov':movie,'Sources/Starter/CaptionFixture.swift':(D/'CaptionFixture.swift').read_bytes()})
        resource=', resources: [.copy("Captions.mov")]'
    data['Package.swift']=('''// swift-tools-version: 5.9
import PackageDescription
let package = Package(name: "Starter", platforms: [.macOS("26.0"), .iOS("26.0"), .tvOS("26.0")],
    products: [.library(name: "Starter", targets: ["Starter"])],
    targets: [.target(name: "Starter"'''+resource+'''), .testTarget(name: "Checks", dependencies: ["Starter"])])
''').encode()
    return name, data

def build(check=False):
    manifest={}
    for k in CASES:
        name,data=files(k)
        from io import BytesIO
        stream=BytesIO()
        with zipfile.ZipFile(stream,'w') as z:
            for n,b in sorted(data.items()):
                info=zipfile.ZipInfo(n,(2026,1,1,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
                z.writestr(info,b,compress_type=zipfile.ZIP_DEFLATED)
        dest=D/'subjects'/(k+'.zip'); content=stream.getvalue()
        if check:assert dest.read_bytes()==content
        else:dest.parent.mkdir(exist_ok=True);dest.write_bytes(content)
        manifest[k]=dict(original=Path(name).stem,platform=CASES[k],archive=H(content),members={n:H(b) for n,b in data.items()})
    raw=(json.dumps(manifest,indent=2)+'\n').encode();path=D/'manifest.json'
    if check:assert path.read_bytes()==raw
    else:path.write_bytes(raw)

def qualify():
    build(True)
    batch=Path(tempfile.mkdtemp(prefix='starter-v2-',dir=OUT));print(batch,flush=True)
    devices=json.loads(subprocess.check_output(['xcrun','simctl','list','devices','booted','-j']))['devices']
    dest={'macOS':'platform=macOS,arch=arm64'}
    for p in ('iOS','tvOS'):
        device,=[d for d in devices.get('com.apple.CoreSimulator.SimRuntime.'+p+'-26-5',[]) if d['name']=='SwiftAccessibility-OS26-Unit-'+p]
        dest[p]='id='+device['udid']
    rows=[]
    for k,p in CASES.items():
        sheet=k in ('4840','da78')
        for variant in (('starter','capture','token') if sheet else ('fixture',)):
            w=batch/(k+'-'+variant);w.mkdir()
            with zipfile.ZipFile(D/'subjects'/(k+'.zip')) as z:z.extractall(w)
            src=w/'Sources/Starter/Starter.swift';s=src.read_text()
            if sheet and variant!='starter':
                old='guard let self, let closingTicket = self.currentTicket else { return }'
                assert s.count(old)==1
                new=('guard let self else { return }; let closingTicket = ticket' if variant=='capture' else
                     'guard let self, self.currentTicket == ticket else { return }; let closingTicket = ticket')
                s=s.replace(old,new)
                if variant=='capture':s=s.replace('guard showing else','guard showing, ticket == generation else')
                src.write_text(s)
            (w/'Tests/Checks/Checks.swift').write_bytes((D/('SheetCheck.swift' if sheet else 'CaptionCheck.swift')).read_bytes())
            cache=OUT/'starter-v2-build-cache'/p
            cache.mkdir(parents=True,exist_ok=True)
            args=['xcodebuild','-jobs','3','test','-scheme','Starter','-destination',dest[p],'-derivedDataPath',str(cache),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','SWIFT_ENABLE_EXPLICIT_MODULES=NO','CODE_SIGNING_ALLOWED=NO']
            with (w/'first.log').open('xb') as f:
                try:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=240).returncode
                except subprocess.TimeoutExpired:rc=124
            b=(w/'first.log').read_bytes();log=b.decode(errors='replace')
            method='testRetiredAndRepeatedDismissal' if sheet else 'testLocalSelection'
            expected='failed' if variant=='starter' else 'passed'
            ok=bool(re.search(r"Test Case '[^']*"+method+r"\]' "+expected,log)) and (rc==65 and 'retired callback' in log if expected=='failed' else rc==0)
            rows.append(dict(case=k,platform=p,variant=variant,method=method,expected=expected,verified=ok,exit=rc,log=H(b),source=H(src.read_bytes()),package=H((D/'subjects'/(k+'.zip')).read_bytes())))
            (batch/'results.json').write_text(json.dumps(rows,indent=2));print(k,variant,rc,ok,flush=True)
            if not ok:raise RuntimeError(str(w/'first.log'))
    return batch

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('command',choices=['build','check','qualify']);args=a.parse_args()
    if args.command=='qualify':qualify()
    else:build(args.command=='check')
