"""Preflight standalone tests and method fragments before grouping native executions."""
import subprocess,re,json,hashlib,sys,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[3]; D=R/'evals/results/proof-repair-preserved-r1'
base=R/'evals/results/proof-repair-1544-v2'
owners='SemanticConfiguration DynamicSections OpaqueSRGB SavedItemCell ValidationOwner DataGrid RestoringPanel MotionPreference ItemActionCard PlaybackSpeedChoices AccessibleChoiceCell DesktopActions DesktopResults DesktopModalRestore DesktopOutline DesktopRow TelevisionStatus TelevisionActions MotionPolicy TelevisionShelves'.split()
def call(args):return subprocess.run(args,capture_output=True)
def main():
 inv=json.loads((D/'inventory.json').read_text()); results=[]
 for i,owner in zip(sorted(inv['types']),owners,strict=True):
    a=json.loads((base/i/'case.json').read_text());platform=a['platform']
    sdk,trip={'macOS':('macosx','macos26.0'),'iOS':('iphonesimulator','ios26.0-simulator'),'tvOS':('appletvsimulator','tvos26.0-simulator')}[platform]
    dev=Path(subprocess.check_output(['xcrun','--sdk',sdk,'--show-sdk-platform-path'],text=True).strip())/'Developer'
    cmd=['xcrun','--sdk',sdk,'swiftc','-swift-version','5','-target','arm64-apple-'+trip,'-module-cache-path',str(D/'cache'),'-F',str(dev/'Library/Frameworks'),'-I',str(dev/'usr/lib')]
    prod='Prod'+i; w=D/'preflight'/i;w.mkdir(parents=True,exist_ok=False)
    src=list((base/i/'working/Sources').glob('*.swift'))
    p=call(cmd+['-emit-module','-enable-testing','-module-name',prod,'-emit-module-path',str(w/(prod+'.swiftmodule'))]+list(map(str,src)))
    if p.returncode:raise RuntimeError(p.stderr.decode())
    for x in inv['blocks']:
        if owner not in x['symbols'].get(i,[]):continue
        h=x['hash'];b=(D/'blocks'/(h+'.swift')).read_bytes();s=b.decode();assert hashlib.sha256(b).hexdigest()==h
        row={'case':i,'hash':h,'platform':platform,'answerCount':len(x['answers'])};results.append(row)
        methods=re.findall(r'\bfunc\s+(test\w+)\s*\(|@Test\b[^\n]*?\bfunc\s+(\w+)',s)
        if not methods:row['status']='no discoverable method';continue
        if re.search(r'\b(?:class|struct|enum|typealias)\s+'+owner+r'\b',s):row['status']='redeclares production owner';continue
        imports=re.findall(r'(?m)^\s*(?:@testable\s+)?import\s+(\w+)',s)
        aliases=set(imports)-{'XCTest','Testing','UIKit','AppKit','SwiftUI','Foundation','AVFoundation','CoreGraphics'}
        if len(aliases)>1:row['status']='multiple product modules';continue
        alias=next(iter(aliases),prod);row['alias']=alias
        pre=('import XCTest\nimport '+('AppKit' if platform=='macOS' else 'UIKit')+'\n@testable import '+alias+'\n').encode()
        full=bool(re.search(r':\s*(?:XCTest\.)?XCTestCase|@Test\b',s))
        if not full and imports: # import declarations must stay at file scope
            row['status']='method fragment with file-level imports';continue
        row['wrapper']='file' if full else 'method fragment'
        code=pre+(b if full else b'@MainActor final class Submitted: XCTestCase {\n'+b+b'\n}\n')
        path=w/(h+'.swift');path.write_bytes(code);assert b in code
        cmd2=cmd+['-typecheck','-I',str(w)]+(['-module-alias',alias+'='+prod] if alias!=prod else [])+[str(path)]
        p=call(cmd2);(w/(h+'.log')).write_bytes(p.stderr)
        row['status']='ready' if p.returncode==0 else 'compile gap';row['error']=next((l.split('error: ',1)[1] for l in p.stderr.decode().splitlines() if 'error: ' in l),None)
    (D/'preflight.json').write_text(json.dumps(results,indent=1));print(i,sum(x['status']=='ready' for x in results if x['case']==i),flush=True)
if __name__=='__main__':main()
