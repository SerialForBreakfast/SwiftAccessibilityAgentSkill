"""Replay the eight frozen v6 trial-1 proofs. Never change Proof0.swift."""
import hashlib,json,re,shutil,subprocess,sys,tempfile,os
from pathlib import Path
D=Path(__file__).resolve().parent; R=D.parents[2]; E=R/'evals/results'
M=E/'mutation-grade-calibration/trial1'
sys.path.insert(0,str(D.parent))
from mutation_grade import controls
KEYS={'4840','da78','4ec9','5d12','6d2d','c04c','c6b2','f483'}
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,obj):p.write_text(json.dumps(obj,indent=2)+'\n')
def replace(s,a,b):
    assert s.count(a)==1,a
    return s.replace(a,b)
def main():
    batch=Path(tempfile.mkdtemp(prefix='starter-eight-',dir=E));print(batch,flush=True)
    import platform
    write(batch/'host.json',dict(xcode=subprocess.check_output(['xcodebuild','-version'],text=True).strip(),
         host=platform.mac_ver()[0],platforms=json.loads(subprocess.check_output(['xcrun','simctl','list','devices','booted','-j']))['devices']))
    specs=controls(); env=json.loads((M/'environment.json').read_bytes())
    rows=[v for v in json.loads((M/'verdicts.json').read_bytes()) if v['arm']=='signal-v6' and v['id'][2:6] in KEYS]
    assert len(rows)==8 and all(r['reason'].startswith('control-api-mismatch:') for r in rows)
    movie,=(E/'media-inventory').glob('batch-7l479_zv/iOS/ordinal/Tests/InventoryTests/sample.mov')
    assert h(movie)=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3'
    results=[]
    for r in rows:
        if sys.argv[1:] and r["id"][2:6] not in sys.argv[1:]:continue
        k=r['id'][2:6]; p=r['platform']; old=M/(r['key']+'.ref')
        mod=json.loads((old/'input.json').read_bytes())['module']
        proof=old/'Proof0.swift'; assert h(proof)==json.loads((old/'input.json').read_bytes())['inputs']['Proof0.swift']
        if k in ('4840','da78'): adapter=(D/'Sheet.swift').read_text()
        else:
            starter,=(E/'qualification-56').glob('starters-*/'+p+'/Sources/Starter'+r['id'][2:]+'/Starter.swift')
            adapter=(D/'Captions.swift').read_text()+'\nstruct CaptionScreen:'+starter.read_text().split('struct CaptionScreen:')[1]
        for label,src in zip(('ref','alt','mut'),specs[k]['src']):
            w=batch/(r['key']+'.'+label);w.mkdir();(w/'Subject').mkdir();(w/'Tests').mkdir()
            api=adapter
            if k in ('c04c','c6b2','f483'):
                # A loader returning string fixtures has no AVMediaSelectionGroup. Apply
                # the same registration-lifetime contrast in this separate state lane.
                if label=='mut':api=replace(api,'guard ticket == self.revision, self.player.currentItem === owner else { return }','_ = (ticket, owner)')
                if label=='alt':api=replace(replace(api,'private var revision = 0','private var revision = UUID()'),'revision += 1','revision = UUID()')
            (w/'Subject/Core.swift').write_text(src);(w/'Subject/Starter.swift').write_text(api)
            shutil.copyfile(proof,w/'Tests/Proof0.swift')
            assert h(w/'Tests/Proof0.swift')==h(proof)
            # The legacy wrapper imported XCTest for a bare test method even if it used
            # Swift Testing macros. Supply module visibility outside the frozen file.
            if k=='4840':
                (w/'Tests/MacroSupport.swift').write_text('@_exported import Testing\n')
            extras=[]
            if k in ('4ec9','5d12'):
                resource=('sample_with_captions' if k=='4ec9' else 'test_media')+'.mp4'
                shutil.copyfile(movie,w/resource);extras=[resource]
                if k=='4ec9':(w/'Tests/Resources.swift').write_text('import Foundation\nprivate final class TestBundleMarker {}\nextension Bundle { static var module: Bundle { Bundle(for: TestBundleMarker.self) } }\n')
            subprocess.run(['ruby',str(D/'project.rb'),str(w),mod,{'iOS':'ios','tvOS':'tvos','macOS':'osx'}[p],'26.0',*extras],check=True)
            offline=bool(re.search(r'URL\(string:|https?://',proof.read_text()))
            args=['xcodebuild','build-for-testing' if offline else 'test','-scheme','Replay','-destination',env[p]['destination'],'-derivedDataPath',str(w/'dd'),'-resultBundlePath',str(w/'first.xcresult'),'-parallel-testing-enabled','NO','-collect-test-diagnostics','never','CODE_SIGNING_ALLOWED=NO']
            write(w/'intent.json',dict(command=args,proof=h(proof),sources={f.name:h(f) for f in (w/'Subject').glob('*.swift')},resource=h(movie) if extras else None))
            with (w/'first.log').open('xb') as f:
                try:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=150).returncode
                except subprocess.TimeoutExpired:rc=124
            log=(w/'first.log').read_text(errors='replace')
            tests=re.findall(r"Test Case '([^']+)' (passed|failed|skipped)",log)
            swift=re.findall(r'Test (.+?) (passed|failed) after',log)
            errors=[line.split(': error: ')[-1][:240] for line in log.splitlines() if ': error: ' in line]
            status=('compile-only' if offline else 'pass' if tests or swift else 'no-tests') if rc==0 else 'assertion-failure' if any(t[1]=='failed' for t in tests+swift) else 'compile-error' if errors else 'harness-error'
            res=dict(id=k,variant=label,status=status,tests=tests+swift,errors=errors[:5],proof=h(proof),exit=rc,log=h(w/'first.log'))
            write(w/'receipt.json',res);results.append(res);write(batch/'results.json',results)
            print(k,label,status,errors[:1],flush=True)
            if status=='harness-error':raise RuntimeError('Inspect preserved infrastructure failure: '+str(w))
if __name__=='__main__':main()
