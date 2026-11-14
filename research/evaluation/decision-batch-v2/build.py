"""Bounded edits to the frozen measured skill; no second discoverable entry point."""
import base64,csv,hashlib,io,re,sys
from pathlib import Path
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
D=Path(__file__).resolve().parent; P=D.parent/'decision-batch-v1'
def table(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def build():
    base=(P/'candidate.zip').read_bytes()
    assert hashlib.sha256(base).hexdigest()=='aa23b85f2235f1eb74f7738c8541529950b44b9a048fdf38f2660024ceed7b5c'
    with ZipFile(io.BytesIO(base)) as z: files={k:z.read(k) for k in z.namelist()}
    root='swift-accessibility-agent/'; entry=root+'SKILL.md'
    files[entry]=files[entry].replace(b'decision-batch-v1',b'decision-batch-v2')
    rows={r['family']:r for r in table(P/'decisions.tsv')}
    fixes=table(D/'fixes.tsv')
    assert len({i for r in fixes for i in r['cases'].split(',')})==8
    for f in fixes:
        r=rows[f['family']];key=root+'references/'+r['route']+'.md'
        before=r['guidance'].encode(); assert files[key].count(before)==1
        files[key]=files[key].replace(before,f['replacement'].encode())
    for family in ('native-slider','visible-title','input-snapshot','dismissal-completion'):
        r=rows[family];assert r['guidance'].encode() in files[root+'references/'+r['route']+'.md']
    # Supply concrete, pre-authored silent sample assets only for fixture requests.
    fixture=(D.parents[2]/'code-examples/platforms/macos-media-v1/Tests/DescriptionFixture.swift').read_text()
    for name,body in re.findall(r'private static let (positive|control) = """(.*?)"""',fixture,re.S):
        path='fixtures/'+name+'.mov';files[root+path]=base64.b64decode(body)
        files[root+'references/media.md']+=f'\n- On request: [local {name} movie](../{path})'.encode()
    assert sum(k.endswith('.mov') for k in files)==2
    files[root+'references/media.md']+=b'\nUse these silent assets for metadata and selection, not narration quality.\n'
    out=io.BytesIO()
    with ZipFile(out,'w') as z:
        for k,v in sorted(files.items()):
            info=ZipInfo(k);info.external_attr=0o100644<<16
            z.writestr(info,v,compress_type=ZIP_DEFLATED)
    return out.getvalue()
if __name__=='__main__':
    b=build();p=D/'candidate.zip'
    if '--check' in sys.argv:assert p.read_bytes()==b
    else:p.write_bytes(b)
    print(hashlib.sha256(b).hexdigest())
