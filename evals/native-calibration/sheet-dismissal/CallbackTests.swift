import SwiftUI
import XCTest
@testable import Presentation

@MainActor final class CallbackTests: XCTestCase {
    func testLateAThenBTwice() {
        var requests: [String] = []
        var caller = "opening"
        let owner = SheetOwner { requests.append("\(caller):\($0)") }
        let a = owner.presentation(origin: "row-A", showing: .constant(true))
        let b = owner.presentation(origin: "row-B", showing: .constant(true))
        XCTAssertEqual(requests, [], "opening must not restore")
        caller = "late-A"
        a.onDismiss()
        XCTAssertEqual(requests, [], "late A must not consume B")
        caller = "first-B"
        b.onDismiss()
        XCTAssertEqual(requests, ["first-B:row-B"], "B must restore its own origin")
        caller = "repeat-B"
        b.onDismiss()
        XCTAssertEqual(requests, ["first-B:row-B"], "B may restore only once")
    }
}
