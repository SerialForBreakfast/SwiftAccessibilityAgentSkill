"""Separate default enumeration from binding writes with native, independently identified options."""
from prepare import ROOT,H
import json,sys,tempfile
from pathlib import Path
base=ROOT/'evals/results/persistent-replay'
out=Path(tempfile.mkdtemp(prefix='v4-binding-',dir=base))
for name in sys.argv[1:]:
    for old in sorted((base/name).glob('P-d*.signal-v4')):
        k=old.name[2:6]
        if k!='dc1e' and not (k=='d4bd' and name.startswith('v4-integrated')):continue
        cell=out/old.name;cell.mkdir()
        r=json.loads((old/'input.json').read_bytes());src=(old/'Subject.swift').read_bytes()
        (cell/'Subject.swift').write_bytes(src)
        first=(old/'Contract.swift').read_text()
        trigger='state.loadOptions()' if k=='dc1e' else '// Initialization already calls loadOptions.'
        end='let id = try XCTUnwrap(chosen,"fixture was not loaded")'
        check='if case .failed(let message) = state.loadState { XCTFail("native enumeration: "+message); return }'
        default=first.replace('var chosen: String?',trigger+'\n        var chosen: String?').replace('try await Task.sleep',check+'\n            try await Task.sleep')
        loader=('state.loadOptions { _ in (text,[choice]) }' if k=='dc1e' else
                'state.loadOptions(for:item) { _,done in done(.success(([choice],text))) }')
        inject=first[first.index('    func testNative'):first.rfind('}')].replace('testNativeCaptionAndAudio','testBindingWithRealPreloadedOption')
        inject=inject.replace('var chosen: String?', 'let choice = TrackChoice(id:"known-caption",name:caption.displayName,descriptive:false,option:caption)\n        '+loader+'\n        var chosen: String?')
        assert end in inject
        (cell/'Contract.swift').write_text(default[:default.rfind('}')]+inject+'\n}\n')
        r.update(selection='native enumeration and isolated binding contrast',inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()})
        (cell/'input.json').write_text(json.dumps(r,indent=2))
print(out.name)
