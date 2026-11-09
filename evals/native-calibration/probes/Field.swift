import XCTest
import UIKit
@testable import Probe

@MainActor final class FieldTests: XCTestCase {
    func testLiveEdit() {
        var replies: [@MainActor ([String: String]) -> Void] = []
        var accepted: [String] = []
        let owner = ValidationOwner(validate: { _, reply in replies.append(reply) },
                                    accept: { accepted.append($0["name"] ?? "") })
        owner.edit("name", "first")
        owner.submit()
        owner.fields["name"]!.text = "second"
        replies[0]([:])
        XCTAssertEqual(accepted, [], "obsolete field reply accepted")
        XCTAssertFalse(owner.busy)
        owner.submit()
        replies[1]([:])
        XCTAssertEqual(accepted, ["second"])
        XCTAssertFalse(owner.busy)
    }
}
