"""Run independent Swift control triplets in one XCTest package per platform."""
from native_controls import *
from starters import SHARED, SDK
import base64,re,subprocess,tempfile

def run():
    base=ROOT/'evals/results/qualification-56';base.mkdir(exist_ok=True)
    out=Path(tempfile.mkdtemp(prefix='controls-',dir=base))
    print(out.name,flush=True)
    env=json.loads((BASE/'v4-paired-jwlc74x4/environment.json').read_bytes())
    from more_controls import specs
    from final_controls import specs as final_specs
    selected=final_specs() if '--last' in sys.argv else specs() if "--more" in sys.argv else suites()
    movie=out/"sample.mov"
    fixture=load('swiftui/media-ios-v2/Tests/DescriptionFixture.swift')
    movie.write_bytes(base64.b64decode(re.search(r'let positive = """(.*?)"""',fixture,re.S)[1]))
    assert H(movie.read_bytes())=="c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3"
    for plat in SDK:
        if "--platform" in sys.argv and sys.argv[sys.argv.index("--platform")+1]!=plat:continue
        cases=[s for s in selected if s['platform']==plat]
        if not cases:continue
        w=out/plat; targets=[];libs=[]; methods={}
        for s in cases:
            for variant,src in zip(('Reference','Alternative','Mutant'),s['src']):
                stem='C'+s['ids'][0]+variant
                t=stem+'Tests';name='test'+stem
                targets.extend([f'.target(name:"{stem}")',f'.testTarget(name:"{t}",dependencies:["{stem}"])']);libs.append('"'+stem+'"')
                p=w/'Sources'/stem;p.mkdir(parents=True);(p/'Subject.swift').write_text(src)
                q=w/'Tests'/t;q.mkdir(parents=True)
                code='import XCTest\nimport SwiftUI\nimport AVFoundation\nimport '+('AppKit' if plat=='macOS' else 'UIKit')+'\n@testable import '+stem+'\n@MainActor final class Probe: XCTestCase { func '+name+'() async throws {\n'+s['body']+'\n} }\n'
                (q/'Probe.swift').write_text(code.replace('MOVIE',str(movie)));methods[name]=dict(cases=s['ids'],variant=variant)
        (w/'Package.swift').write_text(SHARED+f'let package=Package(name:"ControlSuite",platforms:[{SDK[plat]}("26.0")],products:[.library(name:"ControlSuite",targets:['+','.join(libs)+'])],targets:['+','.join(targets)+'])\n')
        args=['xcodebuild','test','-scheme','ControlSuite','-destination',env[plat]['destination'],'-collect-test-diagnostics','never','-jobs','3','-derivedDataPath',str(w/'dd'),'-resultBundlePath',str(w/'result.xcresult'),'-parallel-testing-enabled','NO','CODE_SIGNING_ALLOWED=NO']
        inputs={str(p.relative_to(w)):H(p.read_bytes()) for p in w.rglob('*') if p.is_file()}
        (w/'intent.json').write_text(json.dumps(dict(args=args,inputs=inputs,methods=methods,anchor=env[plat]),indent=2))
        with (w/'native.log').open('xb') as f:
            try:rc=subprocess.run(args,cwd=w,stdout=f,stderr=subprocess.STDOUT,timeout=480).returncode
            except subprocess.TimeoutExpired:rc=124
        (w/'receipt.json').write_text(json.dumps(dict(exit=rc,log=H((w/'native.log').read_bytes()),intent=H((w/'intent.json').read_bytes())),indent=2))
        print(plat,rc,flush=True)
        if rc not in (0,65):break
if __name__=='__main__':run()
