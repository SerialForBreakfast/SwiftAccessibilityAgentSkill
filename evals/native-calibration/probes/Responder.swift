import AppKit
import XCTest
@testable import Probe

@MainActor private final class Button: NSButton {
    var eligible = true
    override var acceptsFirstResponder: Bool { eligible }
}

@MainActor final class ResponderTests: XCTestCase {
    func testAttachedRefusal() {
        _ = NSApplication.shared
        let root = NSView(), primary = Button(), fallback = Button()
        root.addSubview(primary)
        root.addSubview(fallback)
        var requests: [NSButton] = []
        let owner = DesktopModalRestore(root: root) { requests.append($0); return true }
        for accepts in [true, false] {
            let ticket = owner.begin(primary: primary, fallback: fallback)
            primary.eligible = accepts
            XCTAssertTrue(owner.finish(ticket))
        }
        XCTAssertEqual(requests, [primary, fallback], "attached ineligible origin must yield to fallback")
    }
}
