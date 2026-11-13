import XCTest
@testable import Feature

@MainActor final class TransportTests: XCTestCase {
    func testStepDoesNotPlay() {
        let transport = Transport()
        transport.step(.increment)
        XCTAssertEqual(transport.cue, 1)
        XCTAssertFalse(transport.playing)
    }
}
