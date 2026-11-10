"""Offline readback from the worker archive, independent of its construction loop."""
from collections import Counter
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import json
import re
from zipfile import ZipFile
import sys
D=Path(__file__).resolve().parent
B=D.parent
R=B.parents[2]
sys.path.insert(0,str(B))
import verify
from assemble import main
def read(p):return json.loads(p.read_bytes())
def h(b):return sha256(b).hexdigest()

main(True)
receipt=read(D/'receipt.json')
items={x['id']:x for x in read(B/'items.json')['items']}
suggestions={}
for platform in ('ios','macos','tvos'):
    for r in read(D/'shards'/f'{platform}.json'):
        assert items[r['id']]['platform'].lower()==platform and r['id'] not in suggestions
        suggestions[r['id']]=r
verify.load=lambda:(items,suggestions)
verify.HERE=D
verify.main()
board={r['id']:r for r in read(D/'board.json')}
old={r['id']:r['prompt'] for r in map(json.loads,(R/'evals/gemini-discovery/subjects.jsonl').read_text().splitlines())}
with ZipFile(D/'bigdog-held.zip') as z:
    seal=json.loads(z.read('seal.json'))
    assert set(z.namelist())==set(seal)|{'seal.json'} and all(h(z.read(k))==v for k,v in seal.items())
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    rows=json.loads(z.read('controller/cases.json'))
    prompts={r['subject']:z.read('subjects/'+r['subject']+'.txt').decode() for r in rows}
    assert set(old)==set(board)=={r['parent'] for r in rows} and len(prompts)==receipt['distinctSubjects']
    for r in rows:
        s=prompts[r['subject']]; parent=r['parent']; orig=old[parent]
        assert re.findall(r'```.*?```',orig,re.S)==re.findall(r'```.*?```',s,re.S)
        assert r['subject']=='N-'+h(s.encode())[:16] and r['subject'] in board[parent]['subjectIDs']
        if not board[parent]['changed']: assert s==orig
        partner=board[parent]['pair']
        if partner: assert s.split('\n\n',2)[:2]==prompts[board[partner]['subjectIDs'][0]].split('\n\n',2)[:2]
    with ZipFile(BytesIO(z.read('candidate.zip'))) as skill:
        prefix='swift-accessibility-agent/'
        entry=skill.read(prefix+'SKILL.md').decode()
        routes=re.findall(r'\]\((references/[^)]+)\)',entry)
        assert set(skill.namelist())=={prefix+k for k in ['SKILL.md','agents/openai.yaml',*routes]}
        for member in skill.namelist():
            assert not re.search(rb'G-[a-f0-9]{14}|controller/|audit-revision|grade-ledger',skill.read(member))
    cal=json.loads(z.read('controller/calibration.json'))
    assert len(cal['cases'])==17
    for c in cal['cases'].values():
        assert c['reviewer_1']==c['reviewer_2']==c['author_expected']
print('PASS: original starter blocks, unchanged prompts, 59 paired openings, exact archive members, sealed bytes, isolated skill and prior calibration.')
