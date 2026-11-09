"""Resolve first-pass integration gaps and execute additional original behavioral requirements.
Authoring here changes test hosts only, never subject logic or previous receipts.
"""
from stage import ROOT,D,H,blocks,declaration
import json,shutil,tempfile
from pathlib import Path
base=ROOT/'evals/results/persistent-replay';first=base/'tmp6xijam9k'
out=Path(tempfile.mkdtemp(prefix='adapters-',dir=base))
for c in sorted(first.glob('P-*')):
    k=c.name[2:6];arm=c.name.split('.')[1]
    if k not in ('7d8c','7622','e505','6bfe','7766','3f81','ddf8','d4bd','dc1e'):continue
    if k in ('7d8c','7622','3f81') and arm=='unaided' or k=='7766' and arm=='skill':continue
    p=out/c.name;p.mkdir();meta=json.loads((c/'input.json').read_bytes());mod=meta['module']
    for n in ('answer.txt','question.txt'):shutil.copyfile(c/n,p/n)
    q=blocks((c/'question.txt').read_text());a=blocks((c/'answer.txt').read_text())
    s=(c/'Subject.swift').read_text() if (c/'Subject.swift').exists() else ''
    t=(c/'Contract.swift').read_text() if (c/'Contract.swift').exists() else ''
    repeatproof=False
    if k=='7d8c':
        old=q[0].index('        #if !os(macOS)\n        button.removeAction')
        end=q[0].index('#endif',old)+6
        s=q[0][:old]+a[2]+q[0][end:];repeatproof=True
    if k=='7622':
        s=q[0];pat=r'class BridgeOwner\b'
        s=s.replace(declaration(s,pat),declaration(a[2],pat))
        for n in ('dismantleNSView','dismantleUIView'):
            pat=r'func '+n+r'\(';s=s.replace(declaration(s,pat),declaration(a[3],pat))
        repeatproof=True
    if k=='7766':
        s=q[0].split('@MainActor')[0]+a[1];repeatproof=True
    if k=='6bfe':s='import AppKit\n'+s
    if k=='e505':
        f=ROOT/meta['criterion']
        t='func testFrozenBindingContract() { func exercise() -> Bool {\n'+f.read_text()+'\n}; XCTAssertTrue(exercise()) }'
        meta['oracle']={str(f.relative_to(ROOT)):H(f.read_bytes())}
    if k=='3f81':
        t='''func testOrdinaryAndInstalledShortcut() throws {
         let r=InvoiceRowView(frame:.zero); var calls=[String]()
         func bind(_ id:String,_ enabled:Bool) {r.configure(with:.init(title:id,openTitle:"Open",saveTitle:"Save",isSaveEnabled:enabled,onOpen:{calls.append("open"+id)},onSave:{calls.append("save"+id)}))}
         bind("A",true); bind("B",true)
         let b=r.arrangedSubviews.compactMap{$0 as? NSButton}
         let open=try XCTUnwrap(b.first{$0.title=="Open"}),save=try XCTUnwrap(b.first{$0.title=="Save"})
         let action=try XCTUnwrap(open.accessibilityCustomActions()?.first)
         XCTAssertEqual(action.name,"Save")
         let target=try XCTUnwrap(action.target),sel=try XCTUnwrap(action.selector)
         open.performClick(nil);save.performClick(nil);NSApplication.shared.sendAction(sel,to:target,from:nil)
         XCTAssertEqual(calls,["openB","saveB","saveB"])
         bind("B",false); NSApplication.shared.sendAction(sel,to:target,from:nil)
         XCTAssertEqual(calls.count,3)
        }'''
    if k=='ddf8':
        setup=('let cell=FileRowCell(frame:.zero); cell.onDelete={ _ in hits += 1 }; func bind(_ id:UUID,_ enabled:Bool) {cell.configure(with:FileItem(id:id,name:"File",isEnabled:enabled,canDelete:enabled))}' if arm=='skill' else 'let cell=FileRowCell(style:.default,reuseIdentifier:nil); func bind(_ id:UUID,_ enabled:Bool) {cell.configure(with:FileItem(id:id,name:"File",isEnabled:enabled),onOpen:{},onDelete:{hits += 1})}')
        t='''func testRetiredAndDisabledCommands() throws {
         var hits=0; let a=UUID(), b=UUID(); '''+setup+'''
         bind(a,true); let retired=try XCTUnwrap(cell.accessibilityCustomActions?.first)
         bind(b,true); XCTAssertEqual(retired.actionHandler?(retired),false,"old registration"); XCTAssertEqual(hits,0)
         let current=try XCTUnwrap(cell.accessibilityCustomActions?.first)
         let before=hits; XCTAssertEqual(current.actionHandler?(current),true); XCTAssertEqual(hits,before+1)
         bind(b,false); let previous=hits; XCTAssertEqual(current.actionHandler?(current),false,"permission changed"); XCTAssertEqual(hits,previous)
        }'''
    if k in ('dc1e','d4bd'):
        if k=='d4bd' and arm=='unaided':
            s=q[0].split('struct TrackChoice')[0]+s;repeatproof=True
        td=ROOT/('code-examples/swiftui/media-'+meta['platform'].lower()+'-v2/Tests/DescriptionFixture.swift')
        load='await state.loadOptions { [choice] }' if k=='dc1e' and arm=='unaided' else 'state.load { $0(.success([choice])) }'
        t='''func testChangeReachesActualItem() async throws {
        let url=try DescriptionFixture.write(tagged:true); defer {try? FileManager.default.removeItem(at:url)}
        let item=AVPlayerItem(url:url), player=AVPlayer(playerItem:item)
        let loaded=try await item.asset.loadMediaSelectionGroup(for:.legible)
        let group=try XCTUnwrap(loaded), opt=try XCTUnwrap(group.options.first)
        item.select(nil,in:group); XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in:group))
        let state=MediaState(player:player), choice=TrackChoice(id:"test-caption",name:opt.displayName,descriptive:false)
        '''+load+'''
        state.choose(choice.id)
        XCTAssertEqual(state.selected,choice.id,"local selection")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:group),opt,"actual player selection")
        }'''
        meta['fixture']=H(td.read_bytes())
    if k in ('3f81','ddf8','dc1e','d4bd','e505'):
        t='import XCTest\nimport SwiftUI\nimport AVFoundation\n@testable import '+mod+'\n@MainActor final class Contract: XCTestCase {\n'+t+'\n}\n'
        if k in ('dc1e','d4bd'):t+=td.read_text()
    if repeatproof:
        for f in c.glob('Proof*.swift'):shutil.copyfile(f,p/f.name)
    (p/'Subject.swift').write_text(s)
    if t:(p/'Contract.swift').write_text(t)
    meta.update(selection='hosted',followup=True,repeatproof=repeatproof,inputs={f.name:H(f.read_bytes()) for f in p.iterdir()})
    (p/'input.json').write_text(json.dumps(meta,indent=2))
print(out)
