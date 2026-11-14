import XCTest
@testable import AccessibilityExamples
#if os(macOS)
import SwiftUI
#else
import UIKit
#endif

@MainActor final class ContractTests: XCTestCase {
#if os(macOS)
    func testDocument() {
        let s = DocumentState()
        var selected = [String](), deleted = [String]()
        s.chosen = { selected.append($0) }; s.deleted = { deleted.append($0) }
        s.replace([Article(id: "x", title: "A", important: false)])
        let old = s.action(for: "x", remove: true)
        s.replace([Article(id: "x", title: "B", important: true)])
        old()
        XCTAssertEqual(s.entries.map(\.title), ["B"], "retired delete removed B")
        s.action(for: "x")()
        s.action(for: "x", remove: true)()
        XCTAssertEqual(selected, ["x"]); XCTAssertEqual(deleted, ["x"])
    }
#else
    func testLiveEdit() {
        var replies = [@MainActor ([String:String]) -> Void]()
        var accepted = [String](), focus = 0
        let s = ValidationOwner(validate: { _, reply in replies.append(reply) },
                                request: { _ in focus += 1 },
                                accept: { accepted.append($0["name"] ?? "") })
        s.edit("name", "A"); s.submit()
        s.fields["name"]!.text = "B"
        replies[0](["name":"bad A"])
        XCTAssertEqual(s.errors, [:], "obsolete error reached current field")
        XCTAssertEqual(focus, 0); XCTAssertFalse(s.busy)
        XCTAssertEqual(s.fields["name"]?.text, "B")
        s.submit()
        replies[0]([:]); XCTAssertTrue(s.busy); XCTAssertEqual(accepted, [])
        replies[1]([:]); XCTAssertEqual(accepted, ["B"]); XCTAssertFalse(s.busy)
    }
#if os(tvOS)
    func testShelf() throws {
        let s = TelevisionResults()
        s.apply([.init(id:"x", title:"A", actionName:"Open A")])
        let retired = s.buttons[0]
        var installed: UIAction?
        retired.enumerateEventHandlers { action, _, events, _ in if events.contains(.primaryActionTriggered) { installed = action } }
        let oldAction = try XCTUnwrap(installed)
        s.apply([.init(id:"x", title:"B", actionName:"Open B")])
        retired.sendAction(oldAction)
        XCTAssertNil(s.selectedID, "retired control selected replacement")
        s.buttons[0].sendActions(for:.primaryActionTriggered)
        XCTAssertEqual(s.selectedID, "x")
    }
#else
    func testPanel() {
        let s = RestoringPanel(), bg = UIView(), target = UIButton()
        bg.addSubview(target)
        func open() { XCTAssertTrue(s.open(background:bg, target:target, title:"T", primaryTitle:"Go", closeTitle:"Close")) }
        var pending: (() -> Void)?, count = 0
        s.performDismissal = { pending = $0 }
        s.post = { _, arg in
            count += 1
            XCTAssertTrue((arg as? UIView) === target)
            if s.state == .closed { open() }
        }
        open(); s.canDismiss = false
        s.close.sendActions(for:.touchUpInside)
        XCTAssertEqual(s.state,.open); XCTAssertNil(pending)
        s.canDismiss = true
        XCTAssertTrue(s.accessibilityPerformEscape())
        XCTAssertEqual(count,0,"restored before completion")
        XCTAssertTrue(bg.accessibilityElementsHidden)
        let cancelled = pending; s.tearDown(); cancelled?()
        XCTAssertEqual(count,0); XCTAssertFalse(bg.accessibilityElementsHidden)
        open(); s.close.sendActions(for:.touchUpInside)
        let done = pending; done?(); done?()
        XCTAssertEqual(count,1); XCTAssertEqual(s.state,.open)
        XCTAssertTrue(bg.accessibilityElementsHidden)
        s.tearDown(); bg.accessibilityElementsHidden = true; open(); s.tearDown()
        XCTAssertTrue(bg.accessibilityElementsHidden)
    }
#endif
#endif
}
