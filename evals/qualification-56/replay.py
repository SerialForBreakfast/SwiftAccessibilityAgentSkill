"""Stage only cells absent from the first native v4 batch. Never guess a patch."""
from common import *
import tempfile,re
# Primary answer fences, starter retention, verbatim declaration splice, or unresolved integration.
selection={'1046':('0','1'),'1079':('0','0'),'2865':('0','0'),'3454':('0','0'),
'35ee':('0','0'),'3f81':('0','0'),'4099':('S','G'),'4328':('S','1'),'4840':('1','0'),
'4ec9':('0','0'),'76d9':('S','S'),'7766':('1','G'),'777d':('S','1'),'7b8c':('F:configure','F:configure'),
'7d8c':('1','0'),'9062':('0+1','0'),'9c45':('E:MediaMetadata','E:MediaMetadata'),
'a5c8':('0','0'),'b12c':('0','0+1'),'b435':('0','0'),'c04c':('0','0'),'c556':('N','N'),
'c6b2':('0','0'),'d2dd':('S','G'),'d82c':('N','N'),'da78':('S','0'),'db6a':('S','S'),
'dd7e':('0','0'),'ddf8':('0','0'),'debf':('0','0'),'e505':('0','0'),'e56a':('N','N'),'f483':('0','0')}
def stage():
    batch=Path(tempfile.mkdtemp(prefix='panel56-',dir=BASE))
    with answers() as ret,questions() as qs:
        cells=json.loads(ret.read('return.json'))['cells']
        for r in PANEL:
            i=r['id'];k=i[2:6]
            if k in modes:continue
            q=qs.read('subjects/'+i+'.txt');assert H(q)==r['questionSHA256']
            for c in [x for x in cells if x['id']==i]:
                arm=c['arm']; mode=selection[k][arm=='signal-v4']
                cell=batch/(i+'.'+arm);cell.mkdir()
                a=ret.read(c['answer']['path']);assert H(a)==c['answer']['sha256']
                (cell/'answer.txt').write_bytes(a);(cell/'question.txt').write_bytes(q)
                parts=blocks(a.decode()); orig=blocks(q.decode()); src=''
                if mode=='S':src=orig[0]
                elif ':' in mode:
                    typ,name=mode.split(':'); pat=('enum ' if typ=='E' else 'func ')+name+(r'\b' if typ=='E' else r'\(')
                    src=orig[0].replace(declaration(orig[0],pat),declaration(parts[0],pat))
                elif mode not in ('G','N'):src='\n'.join(parts[int(n)] for n in mode.split('+'))
                if src:(cell/'Subject.swift').write_text(src)
                proofs=[s for s in parts if re.search(r'\bfunc test\w*\s*\(|@Test\b|:\s*XCTestCase\b',s) and s not in [src]]
                module=next((m[1] for s in proofs for m in re.finditer(r'@testable import (\w+)',s)),'YourAppModule')
                imports='import XCTest\nimport SwiftUI\nimport AVFoundation\nimport '+('AppKit' if r['platform']=='macOS' else 'UIKit')+'\n@testable import '+module+'\n'
                check,hashes=oracle(dict(r,criterion=r['originalCriterion']))
                if check:(cell/'Contract.swift').write_text(imports+check)
                for n,s in enumerate(proofs):
                    if 'XCTestCase' not in s and '@Test' not in s and re.search(r'\bfunc test',s):
                        pre,sep,body=s.partition('@MainActor')
                        if sep and 'func test' in body and 'func ' not in pre:s=pre+'@MainActor final class Submitted: XCTestCase {\n'+body+'\n}'
                    (cell/f'Proof{n}.swift').write_text(imports+s)
                meta=dict(id=i,arm=arm,platform=r['platform'],module=module,selection=mode,oracle=hashes,inputs={p.name:H(p.read_bytes()) for p in cell.iterdir()})
                (cell/'input.json').write_text(json.dumps(meta,indent=2))
    assert len(list(batch.glob('P-*')))==66
    print(batch.name)
if __name__=='__main__':stage()
