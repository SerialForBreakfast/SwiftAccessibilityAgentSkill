import AVFoundation
import XCTest
@testable import Starter

final class FixtureTests: XCTestCase {
    @MainActor func testLocalSelection() async throws {
        let a = try await CaptionFixture.open(selected: .forced)
        let b = try await CaptionFixture.open(selected: .ordinary)
        XCTAssertFalse(a.item === b.item)
        XCTAssertEqual(a.item.currentMediaSelection.selectedMediaOption(in: a.legible), a.forced)
        XCTAssertEqual(b.item.currentMediaSelection.selectedMediaOption(in: b.legible), b.ordinary)
        b.item.select(nil, in: b.legible)
        XCTAssertNil(b.item.currentMediaSelection.selectedMediaOption(in: b.legible))
        XCTAssertEqual(b.item.currentMediaSelection.selectedMediaOption(in: b.audible), b.audio)
        XCTAssertEqual(a.item.currentMediaSelection.selectedMediaOption(in: a.legible), a.forced)
    }
}
