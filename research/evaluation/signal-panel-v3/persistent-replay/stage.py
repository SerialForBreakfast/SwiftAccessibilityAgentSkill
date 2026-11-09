"""Create a new immutable native-replay input directory for every frozen persistent pair."""
import hashlib,json,re,tempfile
from pathlib import Path
from zipfile import ZipFile
D=Path(__file__).resolve().parent; ROOT=D.parents[3]
H=lambda b:hashlib.sha256(b).hexdigest()
def packet(p,expected):
    assert H(p.read_bytes())==expected
    return ZipFile(p)
def blocks(s):return re.findall(r'(?ms)^`{3}swift[ \t]*\r?\n(.*?)^`{3}[ \t]*$',s)
def declaration(s,pattern):
    m=re.search(r'(?m)^.*?'+pattern,s);assert m,pattern
    j=m.end()
    if s[j-1]=='(':
        depth=1
        while depth:
            depth+=(s[j]=='(')-(s[j]==')');j+=1
    j=s.index('{',j)+1;depth=1
    while depth:
        depth+=(s[j]=='{')-(s[j]=='}');j+=1
    return s[m.start():j]
# Numbers index verbatim Swift fences. S = retain starter as primary recommendation.
# C = replace just the matching class in starter; G = incomplete patch lacking a unique integration.
selections={
'7d8c':('C0:BridgeOwner','G'),'d76c':('1','S'),'f28c':('3','2'),'7622':('1','G'),
'4840':('C1:PresentationState','1'),'f93b':('0','0'),'2865':('0','0'),'db6a':('S','S'),
'f6c7':('S','S'),'3454':('0','0'),'35ee':('0','0'),'db32':('1','0'),
'51e9':('C4:ReusableMessageActions','1'),'3f81':('0','0'),'852a':('1','1'),'777d':('1','S'),
'4ec9':('0','0'),'7766':('1','2'),'4099':('S','S'),'5d12':('0','0'),
'a12b':('S','S'),'6bfe':('0+1','1'),'6d2d':('0','0'),'da78':('1','1'),
'7cc5':('0','0'),'a00e':('C1:BridgeOwner','C1:BridgeOwner'),'9062':('0+1','0'),
'89b1':('S','S'),'a32f':('0','1'),'be25':('S','S'),'c04c':('0','0'),
'c556':('T','T'),'c6b2':('0','0'),'d4bd':('0','0'),'d82c':('N','N'),
'dc1e':('0','0'),'dd7e':('0','0'),'ddf8':('0','0'),'e505':('0','0'),'f483':('0','0')}
def oracle(row):
    if not row['assertions']:return '',{}
    cls,meth=row['assertions'][0].split('/')
    td=ROOT/Path(row['source']).parent/'Tests'
    f,=[f for f in td.glob('*.swift') if 'func '+meth+'(' in f.read_text()]
    s=f.read_text();body=declaration(s,'func '+meth+r'\(')
    start=s.index('class '+cls+': XCTestCase {')+len('class '+cls+': XCTestCase {')
    pre=s[start:re.search(r'(?m)^.*?func test',s[start:]).start()+start]
    # Interop contains additional unrelated helpers. Only button() is required.
    if cls=='InteropTests':pre=declaration(pre,r'func button\(')
    outside=''
    if cls=='DesktopLifecycleTests':
        outside='@MainActor\n'+declaration(s,'private final class ModalHarness')+'\n'+declaration(s,'private final class TestButton')
    if 'DescriptionFixture' in pre+body:outside+='\n'+(td/'DescriptionFixture.swift').read_text()
    return (outside+'\n@MainActor final class OriginalTests: XCTestCase {\n'+pre+'\n'+body+'\n}\n'),{str(f.relative_to(ROOT)):H(f.read_bytes()),'method':H(body.encode())}
def main():
    ret=packet(ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip','9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368')
    pkt=packet(D.parents[1]/'signal-panel-v2/held.zip','51bf28327715ad63929a107b9c8b3e3c364669916e3f2c0107f61b6300b45acd')
    panel={r['id']:r for r in json.loads(pkt.read('controller/panel.json'))}
    pairs=[r for r in json.loads(ret.read('transitions.json')) if r['transitions']['whole']=='persistent']
    assert len(pairs)==40 and set(selections)=={r['id'][2:6] for r in pairs}
    base=ROOT/'evals/results/persistent-replay';base.mkdir(exist_ok=True)
    out=Path(tempfile.mkdtemp(dir=base))
    for row in pairs:
        i=row['id'];k=i[2:6];q=pkt.read('subjects/'+i+'.txt'); orig=blocks(q.decode())
        check,oracle_hash=oracle(panel[i])
        for j,arm in enumerate(('unaided','skill')):
            cell=out/(i+'.'+arm);cell.mkdir()
            ans=ret.read(f'records/{i}.{arm}/answer.txt');a=blocks(ans.decode())
            (cell/'answer.txt').write_bytes(ans);(cell/'question.txt').write_bytes(q)
            mode=selections[k][j];src=''
            if mode=='S':src=orig[0]
            elif mode.startswith('C'):
                n,name=mode[1:].split(':');pat='class '+name+r'\b';old=declaration(orig[0],pat);new=declaration(a[int(n)],pat)
                src=orig[0].replace(old,new)
            elif mode not in ('G','N','T'):src='\n'.join(a[int(n)] for n in mode.split('+'))
            proof=[b for b in a if re.search(r'\bfunc test\w*\s*\(|@Test\b|:\s*XCTestCase\b',b)]
            if mode=='T': proof=a
            chosen=check
            if k in ('3454','9062') and arm=='skill':
                chosen=(D.parent/'offline-pass'/('panel.swift' if k=='3454' else 'sheet.swift')).read_text()
            plat=row['platform'];fw='AppKit' if plat=='macOS' else 'UIKit'
            # Provide a host for free XCTest functions. Swift Testing free functions are already tests.
            imp=next((m[1] for b in proof for m in re.finditer(r'@testable import (\w+)',b)),'YourAppModule')
            proof_bytes=[]
            for b in proof:
                if b==src and mode!='T':continue
                wrap='XCTestCase' not in b and '@Test' not in b and re.search(r'\bfunc test',b)
                proof_bytes.append('import XCTest\nimport '+fw+'\n@testable import '+imp+'\n'+('@MainActor final class Submitted: XCTestCase {\n' if wrap else '')+b+('}\n' if wrap else ''))
            if mode=='T':src='// Submitted example and proof are colocated in the test target.\n'
            if src:(cell/'Subject.swift').write_text(src)
            if chosen:(cell/'Contract.swift').write_text('import XCTest\nimport SwiftUI\nimport AVFoundation\nimport '+fw+'\n@testable import '+imp+'\n'+chosen)
            for n,b in enumerate(proof_bytes):(cell/f'Proof{n}.swift').write_text(b)
            meta=dict(id=i,arm=arm,platform=plat,family=row['family'],selection=mode,module=imp,bindings=panel[i]['assertions'],criterion=panel[i]['criterion'],oracle=oracle_hash,returnedProofFences=[H(b.encode()) for b in proof],inputs={f.name:H(f.read_bytes()) for f in sorted(cell.iterdir())})
            (cell/'input.json').write_text(json.dumps(meta,indent=2))
    print(out)
if __name__=='__main__':main()
