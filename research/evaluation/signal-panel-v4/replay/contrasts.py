"""Bind the existing named font criterion, saved-state distinction and local media fixtures."""
from prepare import ROOT,H,declaration
from pathlib import Path
import base64,json,re,sys,tempfile
base=ROOT/'evals/results/persistent-replay';first=base/sys.argv[1]
out=Path(tempfile.mkdtemp(prefix='v4-contrasts-',dir=base))
for old in sorted(first.glob('P-*')):
    k=old.name[2:6]
    if k not in ('db32','f776','d76c','f28c','7cc5'):continue
    c=out/old.name;c.mkdir()
    meta=json.loads((old/'input.json').read_bytes())
    (c/'Subject.swift').write_bytes((old/'Subject.swift').read_bytes())
    header=f'import UIKit\nimport XCTest\n@testable import {meta["module"]}\n@MainActor final class Contract: XCTestCase {{\n'
    if k=='f776':
        original=(ROOT/'evals/pool/ios-uikit/receipt-font-traits/test.swift').read_text()
        test=header+'func testOriginalFontCriterion() { func check() -> Bool {\n'+original+'\n}; XCTAssertTrue(check()) }\n}'
    elif k=='db32':
        test=header+'''func testNativeSelectionDoesNotRewriteSavedValue() {
            let cell=SavedItemCell(frame:.zero)
            cell.configure(id:"A",title:"Order",saved:true,removable:false,language:"en")
            XCTAssertEqual(cell.accessibilityValue,"Saved")
            cell.isSelected=true; cell.isSelected=false
            XCTAssertEqual(cell.accessibilityValue,"Saved","native selection changed independent saved state")
        }
        }'''
    else:
        test=(old/'Contract.swift').read_text()
        # Replace fixture plumbing only: never let the original cleanup remove a retained snapshot.
        for label in ('positive','control'):
            data=base64.b64decode(re.search('let '+label+' = """(.*?)"""',test,re.S)[1])
            (c/(label+'.mov')).write_bytes(data)
        prior=declaration(test,r'static func write\(')
        test=test.replace(prior,'    static func write(tagged: Bool) throws -> URL { URL(fileURLWithPath:"'+str(c)+'").appendingPathComponent(tagged ? "positive.mov" : "control.mov") }')
        test=test.replace('defer { try? FileManager.default.removeItem(at: url) }','')
        assert 'temporaryDirectory' not in test and 'removeItem' not in test
    (c/'Contract.swift').write_text(test)
    meta.update(selection='controller contrast',inputs={p.name:H(p.read_bytes()) for p in c.iterdir()})
    (c/'input.json').write_text(json.dumps(meta,indent=2))
print(out.name)
