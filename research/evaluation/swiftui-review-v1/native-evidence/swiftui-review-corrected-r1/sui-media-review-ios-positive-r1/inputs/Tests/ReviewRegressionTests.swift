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

    func testUnlistedChoicePreservesNativeSelection() async throws {
        try await fixture { store, item, group in
            let forced = try XCTUnwrap(group.options.first { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) })
            item.select(forced, in: group)
            XCTAssertEqual(store.selectedID, store.unlistedSelectionID)
            XCTAssertEqual(store.unlistedSelectionName, forced.displayName)
            XCTAssertTrue(store.choose(store.unlistedSelectionID))
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), forced)
        }
    }

    func testExplicitOffIsDistinctFromUnlistedSelection() async throws {
        try await fixture { store, item, group in
            XCTAssertTrue(group.allowsEmptySelection)
            item.select(nil, in: group)
            XCTAssertNil(store.selectedID)
            XCTAssertNil(store.unlistedSelectionName)
        }
    }

    func testOldCompletionLeavesLoadingOnItemChange() async throws {
        try await fixture { store, _, group in
            let ticket = store.beginLoad()
            store.player.replaceCurrentItem(with: AVPlayerItem(asset: AVMutableComposition()))
            store.complete(ticket, result: .success(group))
            XCTAssertEqual(store.phase, .changedItem)
            XCTAssertFalse(store.isCurrent)
        }
    }

    func testViewLoadKeyIncludesStoreIdentity() {
        let a = MediaSelectionExample(store: MediaSelectionStore(player: AVPlayer()))
        let b = MediaSelectionExample(store: MediaSelectionStore(player: AVPlayer()))
        XCTAssertNotEqual(a.loadKey, b.loadKey)
        XCTAssertEqual(a.loadKey, a.loadKey)
    }

    func testExplicitCancelInvalidatesWhileLoaderIsSuspended() async throws {
        try await fixture { store, _, group in
            var gate: CheckedContinuation<Void, Never>?
            let task = Task { @MainActor in
                await store.refresh { _, _ in
                    await withCheckedContinuation { gate = $0 }
                    return group
                }
            }
            while gate == nil { await Task.yield() }
            task.cancel()
            // Task cancellation alone is cooperative; explicit owner cleanup is immediate.
            XCTAssertEqual(store.phase, .loading)
            store.cancel()
            XCTAssertEqual(store.phase, .idle)
            let next = store.beginLoad()
            gate?.resume()
            await task.value
            store.complete(next, result: .success(group))
            XCTAssertTrue(store.isCurrent)
        }
    }
}
