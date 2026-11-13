import AVFoundation
import XCTest
@testable import Feature

final class InventoryTests: XCTestCase {
    func testBeforeAndAfterItemAssignment() async throws {
        let before = try await inventory(for: nil)
        let after = try await inventory(for: AVPlayerItem(asset: AVMutableComposition()))
        guard case .waiting = before else { return XCTFail("before assignment") }
        guard case .empty = after else { return XCTFail("after assignment") }
    }
}
