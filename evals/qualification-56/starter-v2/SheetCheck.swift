import SwiftUI
import XCTest
@testable import Starter

final class InstalledTests: XCTestCase {
    @MainActor func testRetiredAndRepeatedDismissal() throws {
        let state = PresentationState()
        state.eligible = ["A", "B"]
        var requests: [String] = []
        state.request = { requests.append($0) }
        let host = SheetHost(state: state)
        host.present(from: "A", showing: .constant(true))
        let old = try XCTUnwrap(host.installed).onDismiss
        host.present(from: "B", showing: .constant(true))
        let current = try XCTUnwrap(host.installed).onDismiss
        old()
        XCTAssertEqual(requests, [], "retired callback")
        XCTAssertTrue(state.showing)
        XCTAssertEqual(state.focus, "close")
        current()
        XCTAssertEqual(requests, ["B"])
        current()
        XCTAssertEqual(requests, ["B"], "duplicate restoration")
    }
}
