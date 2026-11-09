import XCTest
import AVFoundation
import SwiftUI
@testable import Contracts

@MainActor final class ContractTests: XCTestCase {
#if os(iOS)
    func testPanelReopen() throws {
        for initial in [false, true] {
            let bg = UIView(), panel = RestoringPanel(), a = UIButton(), b = UIButton()
            bg.addSubview(a); bg.addSubview(b); bg.accessibilityElementsHidden = initial
            var pending: [@MainActor () -> Void] = [], posted: [Any?] = []
            panel.performDismissal = { pending.append($0) }
            panel.post = { _, target in posted.append(target) }
            func open(_ target: UIButton) -> Bool {
                panel.open(background: bg, target: target, title: "Order", primaryTitle: "Apply", closeTitle: "Close")
            }
            XCTAssertTrue(open(a)); XCTAssertTrue(panel.accessibilityPerformEscape())
            let first = try XCTUnwrap(pending.first)
            panel.tearDown()
            XCTAssertEqual(bg.accessibilityElementsHidden, initial)
            XCTAssertTrue(open(b)); XCTAssertTrue(panel.primary.isDescendant(of: panel))
            var applied = 0
            panel.onPrimary = { applied += 1 }
            panel.primary.sendActions(for: .touchUpInside)
            XCTAssertEqual(applied, 1)
            XCTAssertTrue(panel.accessibilityPerformEscape())
            XCTAssertEqual(pending.count, 2)
            first()
            XCTAssertEqual(panel.state, .closing); XCTAssertTrue(bg.accessibilityElementsHidden)
            XCTAssertTrue(posted.isEmpty)
            let second = try XCTUnwrap(pending.last)
            second(); second()
            XCTAssertEqual(panel.state, .closed)
            XCTAssertEqual(bg.accessibilityElementsHidden, initial, "final background snapshot")
            XCTAssertEqual(posted.count, 1)
            if initial { XCTAssertNil(posted.first ?? nil) }
            else { XCTAssertTrue((posted.first as? UIView) === b) }
        }
    }

    func testSheetCallback() {
        var restored: [String] = []
        let owner = SheetOwner { restored.append($0) }
        let a = owner.presentation(origin: "A", showing: .constant(true))
        let b = owner.presentation(origin: "B", showing: .constant(true))
        _ = Text("presenter").modifier(b)
        a.onDismiss()
        XCTAssertTrue(restored.isEmpty, "obsolete modifier callback")
        b.onDismiss(); a.onDismiss(); b.onDismiss()
        XCTAssertEqual(restored, ["B"])
    }

    func testRetainedWrapperAction() throws {
        let view = NativeSurface(), wrapper = SurfaceExample(snapshot: SurfaceSnapshot(), perform: { _,_ in })
        let owner = wrapper.makeCoordinator()
        var events: [String] = []
        func bind(_ id: String) {
            var s = SurfaceSnapshot(); s.id = id
            owner.configure(view, snapshot: s) { key, detail in events.append(key + (detail ? ":details" : ":open")) }
        }
        bind("A")
        let old = try XCTUnwrap(view.primary.accessibilityCustomActions?.first)
        bind("B")
        XCTAssertEqual(old.actionHandler?(old), false, "old installed action")
        let current = try XCTUnwrap(view.primary.accessibilityCustomActions?.first)
        XCTAssertEqual(current.actionHandler?(current), true)
        view.primary.sendActions(for: .primaryActionTriggered)
        view.details.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(events, ["B:details","B:open","B:details"])
        SurfaceExample.dismantleUIView(view, coordinator: owner)
        XCTAssertEqual(current.actionHandler?(current), false)
    }
#endif

    func testPickerWritesPlayerItem() async throws {
        let url = URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("sample.mov")
        let item = AVPlayerItem(url: url)
        let store = MediaSelectionStore(player: AVPlayer(playerItem: item))
        let audioGroup = try await item.asset.loadMediaSelectionGroup(for: .audible)
        let textGroup = try await item.asset.loadMediaSelectionGroup(for: .legible)
        let audio = try XCTUnwrap(audioGroup), text = try XCTUnwrap(textGroup)
        let described = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        item.select(described, in: audio)
        XCTAssertTrue(text.allowsEmptySelection)
        item.select(nil, in: text)
        await store.refresh()
        let choice = try XCTUnwrap(store.choices.first)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text))
        let old = store.selection
        old.wrappedValue = choice.id
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: text), choice.option, "native caption write")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), described)
        await store.refresh()
        old.wrappedValue = nil
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: text), choice.option)
        store.selection.wrappedValue = nil
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text))
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), described)
    }
}
