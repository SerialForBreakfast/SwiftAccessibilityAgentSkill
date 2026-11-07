import XCTest
import SwiftUI
import AVFoundation
@testable import AccessibilityExamples

@MainActor
final class ReviewRegressionTests: XCTestCase {
    private func fixture(_ body: @MainActor (MediaSelectionStore, AVPlayerItem, AVMediaSelectionGroup) async throws -> Void) async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let item = AVPlayerItem(url: url)
        let loaded = try await item.asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        let store = MediaSelectionStore(player: AVPlayer(playerItem: item))
        store.complete(store.beginLoad(), result: .success(group))
        try await body(store, item, group)
    }

    func testStaleOffCannotClearReloadedSelection() async throws {
        try await fixture { store, item, group in
            let old = store.selection
            store.complete(store.beginLoad(), result: .success(group))
            let choice = try XCTUnwrap(store.choices.first)
            XCTAssertTrue(store.choose(choice.id))
            old.wrappedValue = nil
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
        }
    }

    func testStaleOffCannotClearReplacementSelection() async throws {
        try await fixture { store, item, group in
            let old = store.selection
            let replacement = AVPlayerItem(asset: item.asset)
            store.player.replaceCurrentItem(with: replacement)
            store.complete(store.beginLoad(), result: .success(group))
            let choice = try XCTUnwrap(store.choices.first)
            XCTAssertTrue(store.choose(choice.id))
            old.wrappedValue = nil
            XCTAssertEqual(replacement.currentMediaSelection.selectedMediaOption(in: group), choice.option)
        }
    }

    func testForcedSelectionIsNotOff() async throws {
        try await fixture { store, item, group in
            let forced = try XCTUnwrap(group.options.first { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) })
            item.select(forced, in: group)
            XCTAssertNotNil(store.selection.wrappedValue)
        }
    }
}
