"""Inventory original answer bytes and map submitted Swift blocks to production types."""
import hashlib,json,re,zipfile
from pathlib import Path
from collections import defaultdict
R=Path(__file__).resolve().parents[3]; D=R/'evals/results/proof-repair-preserved-r1'
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:json.dumps(x,indent=1)+'\n'
base=R/'evals/results/proof-repair-1544-v2'
types={}
for f in sorted(base.glob('Q*/case.json')):
    src=(f.parent/'working'/json.loads(f.read_text())['replacementTarget']).read_text()
    types[f.parent.name]=set(re.findall(r'^(?:(?:@MainActor|public|private|final|internal)\s+)*(?:class|struct|enum)\s+(\w+)',src,re.M))
answers={}; origins=defaultdict(list); archives={}
def add(b,n):
    h=H(b);answers[h]=b;origins[h].append(n)
share=R.parent/'SharedStatusFile/joe-big-dog'
for p in sorted(share.glob('*.zip')):
    if not re.search('return|swift-disputed|checkout-first-review|agy-native-validation',p.name) or p.name.startswith('accessibility-repair-100'):continue
    z=zipfile.ZipFile(p);before=sum(map(len,origins.values()))
    for n in z.namelist():
        if re.search(r'(?:^|/)(?:answer\.(?:txt|md)|answers/R\d+\.md)$',n): add(z.read(n),[p.name,n])
        if n=='answers-and-grades.json':
            for a in json.loads(z.read(n)):add(a['original_answer'].encode(),[p.name,n+':'+a['id']])
    archives[p.name]=sum(map(len,origins.values()))-before
files={};blocks={}
for a,b in answers.items():
    s=b.decode(errors='replace')
    matches=[]; opened=None
    for mark in re.finditer(rb'(?m)^[ \t]*(`{3,})([^\r\n]*)\r?$',b):
        fence,lang=mark[1],mark[2].strip().lower()
        if opened is None:opened=(len(fence),lang,mark.end()+1)
        elif not lang and len(fence)>=opened[0]:
            _,tag,start=opened
            if tag in (b'',b'swift'):matches.append((start,b[start:mark.start()]))
            opened=None
    if not matches and s.lstrip().startswith(('import ','@testable import ')): matches=[(0,b)]
    for offset,body in matches:
        if not re.search(rb'XCTAssert|XCTUnwrap|XCTestCase|@Test\b|#expect\(|func test\w+',body):continue
        h=H(body);files[h]=body
        x=blocks.setdefault(h,dict(hash=h,answers=[],cases=[],symbols={}))
        x['answers'].append([a,offset])
        for i,names in types.items():
            hits=sorted(n for n in names if re.search(rb'\b'+n.encode()+rb'\b',body))
            if hits and i not in x['cases']:x['cases'].append(i);x['symbols'][i]=hits
(D/'blocks').mkdir(exist_ok=True)
for h,b in files.items():(D/'blocks'/(h+'.swift')).write_bytes(b)
(D/'inventory.json').write_text(J(dict(archives=archives,origins=origins,types={i:sorted(ns) for i,ns in types.items()},blocks=list(blocks.values()))))
if __name__=='__main__':
    print(archives,len(answers),len(blocks))
    for i in types:print(i,types[i],sum(i in x['cases'] for x in blocks.values()))
