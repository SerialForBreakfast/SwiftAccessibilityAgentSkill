"""Separate lane: do the submitted verification examples themselves compile and pass?"""
from pathlib import Path
import hashlib,json,re,subprocess,sys,tempfile
D=Path(__file__).resolve().parent
base=D.parents[3]/'evals/results/nine-rescues'
run=base/sys.argv[1]; assert run.parent==base
out=Path(tempfile.mkdtemp(prefix='proofs-',dir=run));print(out,flush=True)
h=lambda b:hashlib.sha256(b).hexdigest()
assert len(list(run.glob("P-*/receipt.json"))) == 18, "contract batch incomplete"
for cell in sorted(run.glob('P-*')):
    a=(cell/'answer.txt').read_bytes()
    matches=[b for b in re.findall(rb'(?ms)^`{3}swift\n(.*?)^`{3}[ \t]*$',a) if re.search(rb'func test|@Test\b',b)]
    if not matches:continue
    block,=matches
    p=out/cell.name;p.mkdir()
    intent=json.loads((cell/'intent.json').read_bytes())
    plat=intent['platform'];sdk='AppKit' if plat=='macOS' else 'UIKit'
    src=p/'Sources/YourAppModule/Implementation.swift';src.parent.mkdir(parents=True)
    src.write_bytes((cell/'Sources/AccessibilityExamples/Implementation.swift').read_bytes())
    t=p/'Tests/ReplayTests/Submitted.swift';t.parent.mkdir(parents=True)
    host=('import XCTest\nimport '+sdk+'\n@testable import YourAppModule\n').encode()
    wrapped=not any(x in block for x in (b'XCTestCase',b'@Suite'))
    t.write_bytes(host+(b'@MainActor final class Submitted: XCTestCase {\n' if wrapped else b'')+block+(b'}\n' if wrapped else b''))
    (p/'Package.swift').write_bytes((cell/'Package.swift').read_bytes().replace(b'AccessibilityExamples',b'YourAppModule'))
    args=list(intent['command']);args[args.index('-derivedDataPath')+1]=str(out/('build-'+plat));args[args.index('-resultBundlePath')+1]=str(p/'first.xcresult')
    (p/'intent.json').write_text(json.dumps(dict(answer=intent['answer'],fence=h(block),staged=h(t.read_bytes()),wrapped=wrapped,command=args),indent=2))
    with (p/'first.log').open('xb') as log:
        rc=subprocess.run(args,cwd=p,stdout=log,stderr=subprocess.STDOUT,timeout=360).returncode
    log=(p/'first.log').read_bytes();txt=log.decode(errors='replace')
    ran=bool(re.search(r"Test Case '.*? (test\w+)\]' (passed|failed)|Test .*? (passed|failed) after",txt))
    errors=list(dict.fromkeys(l.replace(str(p),'<stage>') for l in txt.splitlines() if ': error:' in l))
    result=('unit-pass' if not rc else 'assertion-fail') if ran else 'compile-error' if errors else 'harness-gap'
    rec=dict(id=intent['id'],arm=intent['arm'],result=result,exit=rc,fence=h(block),log=h(log),diagnostics=errors[:12])
    (p/'receipt.json').write_text(json.dumps(rec,indent=2)); print(cell.name,result,errors[:1],flush=True)
