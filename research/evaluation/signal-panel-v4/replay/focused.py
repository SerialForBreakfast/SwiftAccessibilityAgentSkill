"""Additional controller checks, separate from original-contract and submitted-proof lanes."""
from prepare import ROOT,H,declaration
import base64,json,re,sys,tempfile
from pathlib import Path
base=ROOT/'evals/results/persistent-replay'
first=base/sys.argv[1];out=Path(tempfile.mkdtemp(prefix='v4-focused-',dir=base))
for old in sorted(first.glob('P-*')):
    k=old.name[2:6];v4=old.name.endswith('v4')
    if k not in ('0a2c','be25','d4bd','dc1e','852a') or k=='852a' and not v4:continue
    c=out/old.name;c.mkdir()
    meta=json.loads((old/'input.json').read_bytes());mod=meta['module']
    src=(old/'Subject.swift').read_bytes();(c/'Subject.swift').write_bytes(src)
    header=f'import XCTest\nimport SwiftUI\nimport AVFoundation\n@testable import {mod}\n'
    if k=='0a2c':
        t=(old/'Contract.swift').read_text()
        ref=(ROOT/'code-examples/platforms/tvos-lifecycle-v1/Tests/TelevisionLifecycleTests.swift').read_text()
        t+='\n@MainActor\n'+declaration(ref,'private final class PreferenceHarness')+'\n'
    elif k=='852a':
        # The submitted function has no test prefix. Register it without changing the check.
        t=(old/'Proof0.swift').read_text()+'\n@MainActor final class Host: XCTestCase { func testSubmittedCheck() { checkRetainedActionVersusCurrentControls() } }\n'
    elif k=='be25':
        t=header+'''
import AppKit
@MainActor final class Refusal: XCTestCase {
    func testRejectedRequestFallsBack() {
        _ = NSApplication.shared
        let root=NSView(), primary=NSButton(), fallback=NSButton()
        root.addSubview(primary);root.addSubview(fallback)
        var requests=[NSButton]()
        let owner=DesktopModalRestore(root:root) { requests.append($0); return $0 === fallback }
        XCTAssertTrue(owner.finish(owner.begin(primary:primary,fallback:fallback)))
        XCTAssertEqual(requests,[primary,fallback],"refused request must advance")
    }
}
'''
    else:
        # Use an already qualified movie; no network, external file write, or production patch.
        fixture=ROOT/f"code-examples/swiftui/media-{meta['platform'].lower()}-v2/Tests/DescriptionFixture.swift"
        data=base64.b64decode(re.search(r'let positive = """(.*?)"""',fixture.read_text(),re.S)[1])
        assert H(data)=='c08c9e5d23f035221aedfd9004dde8873a1b9edeff1d21b45a73a4b5626f76f3'
        (c/'sample.mov').write_bytes(data)
        drive='''
        var chosen: String?
        for _ in 0..<200 {
            if case .loaded(let options) = state.loadState { chosen=options.first(where: { $0.option == caption })?.id; break }
            try await Task.sleep(nanoseconds:10_000_000)
        }
        let id = try XCTUnwrap(chosen,"fixture was not loaded")
        state.BINDING.wrappedValue=id
        '''.replace('BINDING','selectionBinding' if k=='d4bd' else 'pickerBinding') if v4 else '''
        let choice=TrackChoice(id:"fixture",name:caption.displayName,descriptive:false)
        state.load { done in done(.success([choice])) }
        state.choose(choice.id)
        XCTAssertEqual(state.selected,choice.id)
        '''
        t=header+'''
@MainActor final class MediaWrite: XCTestCase {
    func testNativeCaptionAndAudio() async throws {
        let item=AVPlayerItem(url:URL(fileURLWithPath:"FIXTURE"))
        let cg=try await item.asset.loadMediaSelectionGroup(for:.legible)
        let ag=try await item.asset.loadMediaSelectionGroup(for:.audible)
        let text=try XCTUnwrap(cg),audio=try XCTUnwrap(ag)
        let caption=try XCTUnwrap(text.options.first)
        let audioOption=try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        item.select(audioOption,in:audio); item.select(nil,in:text)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in:text))
        let state=MediaState(player:AVPlayer(playerItem:item))
DRIVE
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:text),caption,"actual caption write")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:audio),audioOption,"preserve audio")
    }
}
'''.replace('FIXTURE',str(c/'sample.mov')).replace('DRIVE',drive)
    (c/'Contract.swift').write_text(t)
    meta.update(selection='additional probe, not original grade',inputs={p.name:H(p.read_bytes()) for p in c.iterdir()})
    (c/'input.json').write_text(json.dumps(meta,indent=2))
print(out.name)
