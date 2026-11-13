"""Join XCTest's per-target events to immutable proof hashes; never grade by process exit alone."""
import json, re, collections, csv
from pathlib import Path
from stage import D, R
HERE=Path(__file__).resolve().parent
def walk(n):
    yield n
    for c in n.get('children',[]):yield from walk(c)
def events(report,t,w):
    found=[]
    for root in report.get('testNodes',[]):
        for b in walk(root):
            if b.get('nodeType')!='Unit test bundle' or b['name']!=t:continue
            for n in walk(b):
                if n.get('nodeType') not in ('Test Case','Test case'):continue
                fails=[]
                for c in walk(n):
                    if c.get('nodeType')!='Failure Message':continue
                    loc=c.get('sourceLocation',{});ln=loc.get('lineNumber');file=w/'Tests'/t/'Submission.swift'
                    text=file.read_text().splitlines()
                    fails.append({'message':c['name'],'line':ln,'assertion':text[ln-1].strip() if ln and 0<ln<=len(text) and Path(loc['filePath']).name=='Submission.swift' else None})
                found.append(dict(method=n['name'],status=n['result'],failures=fails))
    return found
def main():
    board=[]
    extra={r['hash']:r for r in json.loads((D/'extra.json').read_bytes())}
    for r in json.loads((D/'preflight.json').read_bytes()):
        r=extra.get(r['hash'],r);i,h=r['case'],r['hash'];t='T'+h[:12]
        record=dict(case=i,hash=h,source_answers=r['answerCount'],preflight=r['status'],detail=r.get('error'))
        board.append(record)
        if r['status']!='ready':record['outcome']='interface/discovery gap';continue
        vs={}
        for v in ('working','alternative','defect'):
            w=D/'native'/i/v
            if (D/'native-extra'/i/v/'native.json').exists() and h in json.loads((D/'native-extra'/i/v/'native.json').read_bytes())['ids']:w=D/'native-extra'/i/v
            if not (w/'native.json').exists():continue
            n=json.loads((w/'native.json').read_bytes());vs[v]=events(n['report'],t,w)
        record['arms']=vs
        def allpass(x):return bool(x) and all(e['status']=='Passed' for e in x)
        if len(vs)!=3 or any(not vs[k] for k in vs):verdict='execution gap'
        elif any(e['status'] not in ('Passed','Failed') for es in vs.values() for e in es):verdict='skip or incomplete'
        elif any(re.search(r'crash:|crashed with signal', f['message'], re.I) for k in vs for e in vs[k] for f in e['failures']):verdict='runtime crash (not a catch)'
        elif any(not allpass(vs[k]) for k in ('working','alternative')):verdict='rejects valid code'
        elif {e['method'] for e in vs['working']}!={e['method'] for e in vs['defect']} or {e['method'] for e in vs['working']}!={e['method'] for e in vs['alternative']}:verdict='execution gap'
        elif allpass(vs['defect']):verdict='misses defect'
        elif any(f['assertion'] and re.search(r'XCTAssert|XCTUnwrap|Expectation failed|failed -',f['message']) for e in vs['defect'] for f in e['failures']):verdict='differential assertion'
        else:verdict='failure needs attribution'
        record['outcome']=verdict
    (D/'board.json').write_text(json.dumps(board,indent=1))
    print(collections.Counter(r['outcome'] for r in board))
if __name__=='__main__':main()
