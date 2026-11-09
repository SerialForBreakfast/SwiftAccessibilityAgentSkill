"""Drive an installed registration instead of requiring a reference-only action() helper."""
from pathlib import Path
from stage import ROOT,H
import json,shutil,tempfile
base=ROOT/'evals/results/persistent-replay';first=base/'tmp6xijam9k';second=base/'adapters-o1xp27st'
out=Path(tempfile.mkdtemp(prefix='registrations-',dir=base))
for f in first.glob('P-*/input.json'):
    c=f.parent
    if c.name[2:6] not in ('7d8c','7622','7766','a00e'):continue
    src=second/c.name if (second/c.name).is_dir() else c
    r=json.loads((src/'input.json').read_text());p=out/c.name;p.mkdir()
    for n in ('answer.txt','question.txt','Subject.swift'):shutil.copyfile(src/n,p/n)
    extra='owner.attach(to:b)' if c.name.startswith('P-7766') and r['arm']=='unaided' else ''
    t='''import XCTest
import UIKit
@testable import MODULE
@MainActor final class Registration: XCTestCase {
    func testInstalledRegistration() throws {
        let owner=BridgeOwner(), b=UIButton(type:.system)
        var events=[String]()
        EXTRA
        owner.configure(b,title:"A",enabled:true){events.append("A")}
        var held:UIAction?
        b.enumerateEventHandlers { action, _, mask, _ in
            if mask.contains(.primaryActionTriggered), let action { held=action }
        }
        let first=try XCTUnwrap(held)
        owner.configure(b,title:"B",enabled:true){events.append("B")}
        b.sendAction(first)
        XCTAssertEqual(events,[],"retired registration must not dispatch for B")
        events.removeAll()
        b.sendActions(for:.primaryActionTriggered)
        XCTAssertEqual(events,["B"],"current ordinary action must work")
        owner.stop();b.sendActions(for:.primaryActionTriggered)
        XCTAssertEqual(events,["B"],"teardown must retire the ordinary action")
    }
}
'''.replace('MODULE',r['module']).replace('EXTRA',extra)
    (p/'Contract.swift').write_text(t)
    r.update(selection='same submitted implementation; retained installed UIAction probe',repeatproof=False,inputs={f.name:H(f.read_bytes()) for f in p.iterdir()})
    (p/'input.json').write_text(json.dumps(r,indent=2))
print(out)
