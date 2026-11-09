"""Complete the host repair with the installed Swift overlay and two proof-host prerequisites."""
import runpy,shutil,json
from stage import D,H,blocks
g=runpy.run_path(str(D/'registration.py'))
out,first=g['out'],g['first']
for c in first.glob('P-*'):
    k=c.name[2:6];arm=c.name.split('.')[1]
    if (k,arm) not in [('db32','skill'),('da78','unaided'),('f6c7','unaided')]:continue
    p=out/c.name;p.mkdir()
    r=json.loads((c/'input.json').read_text())
    for f in c.iterdir():
        if f.name in ('answer.txt','question.txt','Subject.swift','Contract.swift') or f.match('Proof*.swift'):shutil.copyfile(f,p/f.name)
    if k=='db32':
        # Integrated replacement of the class leaves the rest of the supplied source in place.
        starter=blocks((p/'question.txt').read_text())[0];pos=starter.index('public enum ReusableTypography')
        with (p/'Subject.swift').open('a') as f:f.write('\n'+starter[pos:])
    else:
        proof=p/'Proof0.swift';proof.write_text('import Testing\n'+proof.read_text())
    r.update(selection='unchanged fences in supplied starter/test host',repeatproof=True,inputs={f.name:H(f.read_bytes()) for f in p.iterdir()})
    (p/'input.json').write_text(json.dumps(r,indent=2))
