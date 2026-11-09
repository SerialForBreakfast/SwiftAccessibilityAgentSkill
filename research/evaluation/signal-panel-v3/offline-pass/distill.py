"""Build an isolated archive and a controller-side decision board from pinned inputs."""
from pathlib import Path
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
from io import BytesIO
import hashlib,json,re,sys,posixpath
D=Path(__file__).resolve().parent
parent=D.parent/'feedback-review/candidate.zip'
assert hashlib.sha256(parent.read_bytes()).hexdigest()=='f59e0cbdd2ffd48778b9ff74a16e64eea5c0ead4f5a31b2507324c05cebef19a'
prefix='swift-accessibility-agent/'
with ZipFile(parent) as z: original={k:z.read(k) for k in z.namelist()}
files=original.copy()
entry=prefix+'SKILL.md'
files[entry]=original[entry].split(b'# Swift Accessibility Agent\n',1)[0].replace(b'signal-v3-review.1',b'signal-v3-distilled.1')+b'# Swift Accessibility Agent\n\n'+(D/'guide.md').read_bytes()
for n in ['actions','media','return','validation']:
    files[prefix+'references/'+n+'.md']=(D/(n+'.md')).read_bytes()
for path,data in files.items():
    for target in re.findall(rb'\]\(([^)]+)\)',data):
        if not target.startswith(b'https:'):
            assert posixpath.normpath(posixpath.join(posixpath.dirname(path),target.decode())) in files
assert len(files[entry])<len(original[entry]) and sum(map(len,files.values()))<sum(map(len,original.values()))
out=BytesIO()
with ZipFile(out,'w') as z:
    for n,b in sorted(files.items()): z.writestr(ZipInfo(n,(2026,1,1,0,0,0)),b,compress_type=ZIP_DEFLATED)
root=D.parents[3]
def packet(path,seal):
    data=path.read_bytes();assert hashlib.sha256(data).hexdigest()==seal
    return ZipFile(BytesIO(data))
with packet(root/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip','9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368') as z, packet(D.parents[1]/'signal-panel-v2/held.zip','51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd') as inputs:
    panel={r['id']:r for r in json.loads(inputs.read('controller/panel.json'))}
    transitions=json.loads(z.read('transitions.json'))
    assert len(panel)==len(transitions)==56 and set(panel)=={r['id'] for r in transitions}
    board=['| Case | Platform/framework | Family | Whole transition | Installed axes still failing | Next offline check (controller only) |','|---|---|---|---|---|---|']
    grades={(r['id'],r['arm']):r for r in json.loads(z.read('grades.json'))}
    for r in transitions:
        i=r['id'];g=grades.get((i,'skill'));whole=r['transitions']['whole']
        failed=', '.join(k for k in ('primary','integration','verification','preservation','rework') if g and g[k]=='fail')
        recommendation=panel[i]['reviewProposal']
        if whole in ('preserved','rescue'): recommendation='Protect as regression control. '+recommendation
        if whole=='inconclusive': recommendation='Keep unpaired; exclude from lift. '+recommendation
        board.append('| '+' | '.join([i,r['platform']+'/'+r['framework'],r['family'],whole,failed or ('none' if g else 'unavailable'),recommendation.replace('|','/')])+' |')
for n,data in [('candidate.zip',out.getvalue()),('portfolio.md',('\n'.join(board)+'\n').encode())]:
    if '--check' in sys.argv:assert (D/n).read_bytes()==data
    else:(D/n).write_bytes(data)
print('Entry bytes:',len(original[entry]),'->',len(files[entry]),'; all uncompressed bytes:',sum(map(len,original.values())),'->',sum(map(len,files.values())))
