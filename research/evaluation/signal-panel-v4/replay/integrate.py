"""Repeat only the iOS media cell with its untouched starter dependency present."""
from prepare import ROOT,H,blocks
import json,sys,tempfile
from pathlib import Path
base=ROOT/'evals/results/persistent-replay'
out=Path(tempfile.mkdtemp(prefix='v4-integrated-',dir=base))
first,focused=[base/x for x in sys.argv[1:]]
old,=first.glob('P-d4bd*.signal-v4');cell=out/old.name;cell.mkdir()
prefix=blocks((old/'question.txt').read_text())[0].split('struct TrackChoice:')[0]
(cell/'Subject.swift').write_bytes(prefix.encode()+(old/'Subject.swift').read_bytes())
# Leave the original example media and path intact.
(cell/'Contract.swift').write_bytes((focused/old.name/'Contract.swift').read_bytes())
for proof in old.glob('Proof*.swift'):(cell/proof.name).write_bytes(proof.read_bytes())
meta=json.loads((old/'input.json').read_bytes())
meta.update(selection='verbatim starter prefix plus verbatim answer',inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()})
(cell/'input.json').write_text(json.dumps(meta,indent=2))
print(out.name)
