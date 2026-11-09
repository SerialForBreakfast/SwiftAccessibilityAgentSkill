import XCTest
@testable import Probe

@MainActor final class SheetTests: XCTestCase {
    func testSurvivingOrigin() {
        let owner = Sheet()
        for ids in [["other", "origin"], ["other"]] {
            let ticket = owner.open("origin")
            owner.close()
            XCTAssertNil(owner.visible)
            var requests: [String] = []
            owner.finish(ticket, ids) { requests.append($0) }
            XCTAssertEqual(requests, [ids.contains("origin") ? "origin" : "fallback"],
                           "eligible origin survives close")
        }
    }
}
