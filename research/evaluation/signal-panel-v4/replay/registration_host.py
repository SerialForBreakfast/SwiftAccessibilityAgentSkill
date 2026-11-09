"""Include the submitted identifier extension in the same integration as its BridgeOwner."""
from prepare import ROOT,H,blocks
from pathlib import Path
import json,sys,tempfile
base=ROOT/'evals/results/persistent-replay'
old,=(base/sys.argv[1]).glob('P-a00e*.signal-v2')
out=Path(tempfile.mkdtemp(prefix='v4-registration-',dir=base))
cell=out/old.name;cell.mkdir()
code=blocks((old/'answer.txt').read_text())[1].split('@MainActor')[0]
assert code.strip().startswith('#if !os(macOS)') and 'static let bridgeAction' in code
(cell/'Subject.swift').write_bytes((old/'Subject.swift').read_bytes()+b'\n'+code.encode())
for f in [old/'Contract.swift',*old.glob('Proof*.swift')]:(cell/f.name).write_bytes(f.read_bytes())
r=json.loads((old/'input.json').read_bytes())
r.update(selection='include verbatim submitted extension',inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()})
(cell/'input.json').write_text(json.dumps(r,indent=2));print(out.name)
