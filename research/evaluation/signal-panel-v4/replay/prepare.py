"""Freeze v4 head-to-head replay inputs. S=starter; integers=answer fences, not repaired code."""
import sys,json,re,tempfile
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
OLD=D.parents[1]/'signal-panel-v3/persistent-replay'
sys.path.insert(0,str(OLD))
from stage import blocks,oracle,packet,H,declaration
# C/F replace exactly one named declaration in the starter. X=partial platform branch.
modes={'d76c':('S','S'),'0a2c':('F1:start','F1:start'),'f28c':('1','1'),
'7622':('S','C0:BridgeOwner'),'f93b':('0','0'),'7d27':('S','X'),'f6c7':('S','1'),
'db32':('S','C1:SavedItemCell'),'51e9':('F0:perform','C0:ReusableMessageActions'),
'852a':('0','1'),'5d12':('0','0'),'a12b':('3','2'),'6bfe':('N','0'),
'6d2d':('0','0'),'7cc5':('diff','0'),'a00e':('C1:BridgeOwner','C1:BridgeOwner'),
'89b1':('S','S'),'a32f':('0','S'),'be25':('F1:finish','S'),'d4bd':('0','0'),
'9ae5':('E0:EditActionFactory','E1:EditActionFactory'),'dc1e':('0','0'),'f776':('0','0')}

def main():
    ret=packet(ROOT/'evals/results/signal-v4-review/signal-v4-return.zip','f14305f1ff84de8bd03a79752e70e15e51b0fe8e5f70008b3be855a8bfb7ff09')
    pkt=packet(D.parent/'readiness/held.zip','5e73c208ef105df6a93364a7925363178dd527b3b7d5c8e7cbd5ed1c9180f103')
    panel={r['id']:r for r in json.loads((D.parent/'controller.json').read_bytes())}
    cells=json.loads(ret.read('return.json'))['cells']
    out=Path(tempfile.mkdtemp(prefix='v4-paired-',dir=ROOT/'evals/results/persistent-replay'))
    selected=set()
    for i,row in panel.items():
        pair=sorted([c for c in cells if c['id']==i],key=lambda c:c['arm']);b,v=pair
        failures=[k for k,g in v['grade'].items() if k!='whole' and g['verdict']=='fail']
        if not (failures==['verification'] or b['grade']['whole']['verdict']!=v['grade']['whole']['verdict'] or v['critical'] and not b['critical']):continue
        k=i[2:6]; selected.add(k)
        q=pkt.read('subjects/'+i+'.txt');orig=blocks(q.decode())
        check,oh=oracle(dict(row,criterion=row['originalCriterion']))
        for c,mode in zip(pair,modes[k]):
            folder=out/(i+'.'+c['arm']);folder.mkdir()
            ans=ret.read(c['answer']['path']); assert H(ans)==c['answer']['sha256']
            a=blocks(ans.decode());src='';fw='AppKit' if row['platform']=='macOS' else 'UIKit'
            if mode=='S':src=orig[0]
            elif mode=='N':pass
            elif mode=='X':
                pat=r'#if os\(macOS\)\s*view.setAccessibilityLabel\(snapshot.title\).*?#else'
                src,n=re.subn(pat,lambda _:a[0].strip(),orig[0],count=1,flags=re.S);assert n==1
            elif mode=='diff':
                patch=re.search(r'(?ms)^```diff\n(.*?)^```',ans.decode())[1]
                minus=[l[1:] for l in patch.splitlines() if l.startswith('-') and not l.startswith('---')]
                plus=[l[1:] for l in patch.splitlines() if l.startswith('+') and not l.startswith('+++')]
                old='\n'.join(minus);assert orig[0].count(old)==1
                src=orig[0].replace(old,'\n'.join(plus))
            elif ':' in mode:
                n,name=mode[1:].split(':');kind={'F':'func','C':'class','E':'enum'}[mode[0]]
                pat=kind+' '+name+(r'\(' if kind=='func' else r'\b')
                old,new=[declaration(s,pat) for s in (orig[0],a[int(n)])]
                src=orig[0].replace(old,new)
            else:src=a[int(mode)]
            proof=[t for t in a if re.search(r'\bfunc test\w*\s*\(|@Test\b|:\s*XCTestCase\b',t)]
            if k=='852a' and c==v:proof=[a[0]]
            module=next((m[1] for t in proof for m in re.finditer(r'@testable import (\w+)',t)),'YourAppModule')
            (folder/'answer.txt').write_bytes(ans);(folder/'question.txt').write_bytes(q)
            if src:(folder/'Subject.swift').write_text(src)
            if check:(folder/'Contract.swift').write_text(f'import XCTest\nimport SwiftUI\nimport AVFoundation\nimport {fw}\n@testable import {module}\n'+check)
            for n,t in enumerate(proof):
                wrap='XCTestCase' not in t and '@Test' not in t and re.search(r'\bfunc test',t)
                host=(f'import XCTest\nimport {fw}\n@testable import {module}\n')
                if wrap:host+='@MainActor final class Submitted: XCTestCase {\n'
                (folder/f'Proof{n}.swift').write_text(host+t+('}\n' if wrap else ''))
            meta=dict(id=i,arm=c['arm'],platform=row['platform'],module=module,selection=mode,oracle=oh,bindings=row['assertions'],proofFences=list(map(lambda t:H(t.encode()),proof)),inputs={p.name:H(p.read_bytes()) for p in folder.iterdir()})
            (folder/'input.json').write_text(json.dumps(meta,indent=2))
    assert selected==set(modes)
    print(out.name)
if __name__=='__main__':main()
