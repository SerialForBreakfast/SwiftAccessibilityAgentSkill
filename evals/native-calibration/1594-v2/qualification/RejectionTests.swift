import AppKit
import XCTest
@testable import AccessibilityExamples

private final class EligibleButton: NSButton {
    override var acceptsFirstResponder: Bool { true }
}

final class RejectionTests: XCTestCase {
    @MainActor
    private func observe(primaryAccepts: Bool) -> ([String], Bool) {
        let root = NSView(), primary = EligibleButton(), fallback = EligibleButton()
        root.addSubview(primary)
        root.addSubview(fallback)
        var seen: [String] = []
        let restore = DesktopModalRestore(root: root) { target in
            seen.append(target === primary ? "primary" : target === fallback ? "fallback" : "other")
            return target === primary ? primaryAccepts : target === fallback
        }
        let ticket = restore.begin(primary: primary, fallback: fallback)
        let result = restore.finish(ticket)
        print("Q082B primaryAccepts=\(primaryAccepts) requests=\(seen.joined(separator: ",")) result=\(result)")
        return (seen, result)
    }

    @MainActor func testOrdinaryAcceptance() {
        let (requests, result) = observe(primaryAccepts: true)
        XCTAssertEqual(requests, ["primary"])
        XCTAssertTrue(result)
    }

    @MainActor func testRejectedPrimary() {
        let (requests, result) = observe(primaryAccepts: false)
        XCTAssertEqual(requests, ["primary"])
        XCTAssertFalse(result)
    }
}
