"""Regenerate the public projection, verifying first private sources, receipts and logs."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
base=ROOT/'evals/results/nine-rescues'
first=base/'tmpp8sh46t7'; repair=base/'tmpqgwq724j'; proofs=first/'proofs-3h61qpit'
h=lambda b:hashlib.sha256(b).hexdigest()
records=[]
def get(p):return json.loads(p.read_bytes())
def contract(cell,kind):
    r=get(cell/'receipt.json')
    assert r['answer']==h((cell/'answer.txt').read_bytes())
    assert r['question']==h((cell/'question.txt').read_bytes())
    fields=('id','arm','answer','question','family','platform','runtime','sdk','xcode','deployment','result','reason','binding','source','tests','oracleFile','oracleHash','assertionHash','integration','exit','log','methods')
    row={k:r[k] for k in fields if k in r}
    if r['result']!='source-only':
        assert r['source']==h((cell/'Sources/AccessibilityExamples/Implementation.swift').read_bytes())
        assert r['tests']==h((cell/'Tests/ReplayTests/Contract.swift').read_bytes())
        assert r['log']==h((cell/'first.log').read_bytes())
        if 'oracleFile' in r: assert h((ROOT/r['oracleFile']).read_bytes())==r['oracleHash']
        row['diagnostics']=list(dict.fromkeys(l for l in r['diagnostics'] if l.startswith('<stage>/') and ': error:' in l))[:4]
    row['lane']=kind
    if kind=='first' and cell.name.startswith('P-4328'):row['classification']='oracle-helper extraction error'
    if kind=='adapter-repair':assert r['source']==get(first/cell.name/'receipt.json')['source']
    return row

ret=ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip'
assert h(ret.read_bytes())=='9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368'
with ZipFile(ret) as z:
    expected={r['id']+'.'+arm for r in json.loads(z.read('transitions.json')) if r['transitions']['whole']=='rescue' for arm in ('unaided','skill')}
    assert expected=={p.name for p in first.glob('P-*')}
    for idarm in sorted(expected):
        cell=first/idarm;row=contract(cell,'first')
        assert row['answer']==h(z.read('records/'+idarm+'/answer.txt'))
        records.append(row)
        if (repair/idarm).exists():records.append(contract(repair/idarm,'adapter-repair'))
        tests=[b for b in re.findall(rb'(?ms)^`{3}swift\n(.*?)^`{3}[ \t]*$',(cell/'answer.txt').read_bytes()) if re.search(rb'func test|@Test\b',b)]
        if tests:
            p=proofs/idarm;r=get(p/'receipt.json');intent=get(p/'intent.json')
            assert len(tests)==1 and r['fence']==h(tests[0]) and r['log']==h((p/'first.log').read_bytes())
            assert tests[0] in (p/'Tests/ReplayTests/Submitted.swift').read_bytes()
            assert intent['staged']==h((p/'Tests/ReplayTests/Submitted.swift').read_bytes())
            assert (p/'Sources/YourAppModule/Implementation.swift').read_bytes()==(cell/'Sources/AccessibilityExamples/Implementation.swift').read_bytes()
            proof=dict(**r,lane='submitted-proof')
            # Swift assert traps before XCTest can print its normal case-failed line.
            log=(p/'first.log').read_text(errors='replace')
            trap=re.search(r'(?m)^ReplayTests/Submitted.swift:(\d+): Assertion failed$',log)
            if trap and r['exit'] and '** TEST FAILED **' in log:
                proof.update(classification='submitted-assertion-trap',line=int(trap[1]))
            records.append(proof)
assert len(records)==34
data=(json.dumps(records,indent=2)+'\n').encode()
if '--check' in sys.argv:assert (D/'evidence.json').read_bytes()==data
else:
    with (D/'evidence.json').open('xb') as f:f.write(data)
print('Verified 18 arm dispositions, 2 adapter repairs, 14 submitted proof records.')
