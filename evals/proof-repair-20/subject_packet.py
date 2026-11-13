"""Create a subject-only local ZIP and a separate controller-side seal."""
import json,sys,zipfile
from pathlib import Path
from prepare import H,J
base=Path(sys.argv[1]).resolve(); entries={};index={}
for folder in sorted(base.glob('Q*/subject')):
    i=folder.parent.name
    files={p.relative_to(folder).as_posix():p.read_bytes() for p in folder.rglob('*') if p.is_file()}
    assert set(files)=={'QUESTION.md','Tests/CurrentTests.swift',*(k for k in files if k.startswith('Sources/') and k.endswith('.swift'))}
    assert H(files['Tests/CurrentTests.swift'])==json.loads((folder.parent/'case.json').read_bytes())['weakSHA256']
    index[i]={k:H(b) for k,b in files.items()}
    entries.update({i+'/'+k:b for k,b in files.items()})
assert len(index)==20
path=base/'subject-only.zip'
with zipfile.ZipFile(path,'x') as z:
    for key,b in sorted(entries.items()):
        z.writestr(zipfile.ZipInfo(key,(2026,1,1,0,0,0)),b,compress_type=zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(path) as z:assert {k:z.read(k) for k in z.namelist()}==entries
(base/'subject-seal.json').write_text(J(dict(zipSHA256=H(path.read_bytes()),cases=index)))
print(len(index),'complete subject inputs sealed:',H(path.read_bytes()))
