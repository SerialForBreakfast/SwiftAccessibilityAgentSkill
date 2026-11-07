import XCTest
import SwiftUI
import AVFoundation
import Observation
@testable import AccessibilityExamples

@MainActor
final class MediaSelectionTests: XCTestCase {
    enum LoadError: Error { case unavailable }
    private func fixture(_ body: @MainActor (MediaSelectionStore, AVPlayerItem, AVMediaSelectionGroup, AVMediaSelectionGroup) async throws -> Void) async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let item = AVPlayerItem(url: url)
        let loadedAudio = try await item.asset.loadMediaSelectionGroup(for: .audible)
        let loadedText = try await item.asset.loadMediaSelectionGroup(for: .legible)
        let audio = try XCTUnwrap(loadedAudio)
        let text = try XCTUnwrap(loadedText)
        let store = MediaSelectionStore(player: AVPlayer(playerItem: item))
        store.complete(store.beginLoad(), result: .success(text))
        try await body(store, item, audio, text)
    }

    func testNativeRefreshLoadsActualGroup() async throws {
        try await fixture { store, _, _, _ in
            await store.refresh()
            XCTAssertEqual(store.phase, .ready)
            XCTAssertFalse(store.choices.isEmpty)
        }
    }
    func testFullSubtitleChoicesExcludeForcedOnly() async throws {
        try await fixture { store, _, _, group in
            XCTAssertTrue(group.options.contains { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) })
            XCTAssertTrue(store.choices.allSatisfy { !$0.option.hasMediaCharacteristic(.containsOnlyForcedSubtitles) })
            XCTAssertEqual(store.choices.count, group.options.filter { !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) }.count)
        }
    }
    func testBindingWritesNativeSelection() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            store.selection.wrappedValue = choice.id
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
            XCTAssertEqual(store.selection.wrappedValue, choice.id)
        }
    }
    func testBindingReadsExternalSelection() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.last)
            item.select(choice.option, in: group)
            XCTAssertEqual(store.selection.wrappedValue, choice.id)
        }
    }
    func testUnknownChoicePreservesSelection() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            item.select(choice.option, in: group)
            XCTAssertFalse(store.choose("not-an-option"))
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
        }
    }
    func testOffClearsOnlyPermittedGroup() async throws {
        try await fixture { store, item, _, group in
            XCTAssertTrue(group.allowsEmptySelection)
            _ = store.choose(try XCTUnwrap(store.choices.first).id)
            store.selection.wrappedValue = nil
            XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: group))
        }
    }
    func testSubtitleChangePreservesDescriptiveAudio() async throws {
        try await fixture { store, item, audio, _ in
            let described = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
            item.select(described, in: audio)
            _ = store.choose(try XCTUnwrap(store.choices.first).id)
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), described)
        }
    }
    func testOffPreservesAudio() async throws {
        try await fixture { store, item, audio, _ in
            let chosen = try XCTUnwrap(audio.options.first)
            item.select(chosen, in: audio)
            XCTAssertTrue(store.choose(nil))
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), chosen)
        }
    }
    func testAudioStoreReadsDescriptionTag() async throws {
        try await fixture { store, item, audio, _ in
            let audioStore = MediaSelectionStore(player: store.player, characteristic: .audible)
            await audioStore.refresh()
            let choice = try XCTUnwrap(audioStore.choices.first { $0.option.hasMediaCharacteristic(.describesVideoForAccessibility) })
            XCTAssertTrue(audioStore.choose(choice.id))
            XCTAssertTrue(try XCTUnwrap(item.currentMediaSelection.selectedMediaOption(in: audio)).hasMediaCharacteristic(.describesVideoForAccessibility))
        }
    }
    func testAudioOffMatchesActualGroupPermission() async throws {
        try await fixture { store, _, audio, _ in
            let audioStore = MediaSelectionStore(player: store.player, characteristic: .audible)
            audioStore.complete(audioStore.beginLoad(), result: .success(audio))
            XCTAssertEqual(audioStore.allowsOff, audio.allowsEmptySelection)
            XCTAssertEqual(audioStore.choose(nil), audio.allowsEmptySelection)
        }
    }
    func testLoadingDoesNotChangeNativeChoice() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            item.select(choice.option, in: group)
            _ = store.beginLoad()
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
            XCTAssertTrue(store.choices.isEmpty)
            XCTAssertFalse(store.choose(nil))
        }
    }
    func testReloadRecoversNativeChoiceWithNewIDs() async throws {
        try await fixture { store, _, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            _ = store.choose(choice.id)
            store.complete(store.beginLoad(), result: .success(group))
            XCTAssertNotEqual(store.selectedID, choice.id)
            XCTAssertEqual(store.choices.first { $0.id == store.selectedID }?.option, choice.option)
        }
    }
    func testOldOptionIDCannotSelectAfterReload() async throws {
        try await fixture { store, _, _, group in
            let id = try XCTUnwrap(store.choices.first).id
            store.complete(store.beginLoad(), result: .success(group))
            XCTAssertFalse(store.choose(id))
        }
    }
    func testDuplicateCompletionCannotOverwriteSuccess() async throws {
        try await fixture { store, _, _, group in
            let ticket = store.beginLoad()
            store.complete(ticket, result: .success(group))
            store.complete(ticket, result: .failure(LoadError.unavailable))
            XCTAssertEqual(store.phase, .ready)
        }
    }
    func testOldCompletionCannotOverwriteNewLoad() async throws {
        try await fixture { store, _, audio, text in
            let old = store.beginLoad(), current = store.beginLoad()
            store.complete(current, result: .success(text))
            let ids = store.choices.map(\.id)
            store.complete(old, result: .success(audio))
            XCTAssertEqual(store.choices.map(\.id), ids)
        }
    }
    func testOldErrorCannotOverwriteNewSuccess() async throws {
        try await fixture { store, _, _, group in
            let old = store.beginLoad(), current = store.beginLoad()
            store.complete(current, result: .success(group))
            store.complete(old, result: .failure(LoadError.unavailable))
            XCTAssertEqual(store.phase, .ready)
        }
    }
    func testCancelRejectsLateCompletion() async throws {
        try await fixture { store, _, _, group in
            let ticket = store.beginLoad()
            store.cancel()
            store.complete(ticket, result: .success(group))
            XCTAssertEqual(store.phase, .idle)
            XCTAssertTrue(store.choices.isEmpty)
        }
    }
    func testCancelDoesNotClearNativeSelection() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            _ = store.choose(choice.id)
            store.cancel()
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), choice.option)
        }
    }
    func testReplacedItemRejectsOldChoice() async throws {
        try await fixture { store, item, _, group in
            let choice = try XCTUnwrap(store.choices.first)
            let before = item.currentMediaSelection.selectedMediaOption(in: group)
            store.player.replaceCurrentItem(with: AVPlayerItem(asset: AVMutableComposition()))
            XCTAssertFalse(store.choose(choice.id))
            XCTAssertNil(store.selectedID)
            XCTAssertFalse(store.allowsOff)
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group), before)
        }
    }
    func testReplacedItemRejectsOldCompletion() async throws {
        try await fixture { store, _, _, group in
            let ticket = store.beginLoad()
            store.player.replaceCurrentItem(with: AVPlayerItem(asset: AVMutableComposition()))
            store.complete(ticket, result: .success(group))
            XCTAssertTrue(store.choices.isEmpty)
            XCTAssertFalse(store.isCurrent)
        }
    }
    func testNoItemIsNotAbsentGroup() async {
        let store = MediaSelectionStore(player: AVPlayer())
        await store.refresh()
        XCTAssertEqual(store.phase, .noItem)
        XCTAssertEqual(store.status, "No media item")
    }
    func testAbsentGroupIsNotFailure() {
        let store = MediaSelectionStore(player: AVPlayer(playerItem: AVPlayerItem(asset: AVMutableComposition())))
        store.complete(store.beginLoad(), result: .success(nil))
        XCTAssertEqual(store.phase, .absent)
        XCTAssertFalse(store.choose(nil))
    }
    func testLoadFailureIsNotEmptySuccess() {
        let store = MediaSelectionStore(player: AVPlayer(playerItem: AVPlayerItem(asset: AVMutableComposition())))
        store.complete(store.beginLoad(), result: .failure(LoadError.unavailable))
        XCTAssertEqual(store.phase, .failed)
        XCTAssertFalse(store.isCurrent)
    }
    func testErrorThenReloadRecovers() async throws {
        try await fixture { store, _, _, group in
            store.complete(store.beginLoad(), result: .failure(LoadError.unavailable))
            store.complete(store.beginLoad(), result: .success(group))
            XCTAssertTrue(store.isCurrent)
        }
    }
    func testSelectionPreservesPlayerSettingsAndIdentity() async throws {
        try await fixture { store, item, _, _ in
            store.player.isMuted = true
            store.player.volume = 0.3
            _ = store.choose(try XCTUnwrap(store.choices.first).id)
            XCTAssertTrue(store.player.currentItem === item)
            XCTAssertTrue(store.player.isMuted)
            XCTAssertEqual(store.player.volume, 0.3)
            XCTAssertEqual(store.player.rate, 0)
        }
    }
    func testChoiceIDsUniqueWithinSnapshot() async throws {
        try await fixture { store, _, _, _ in
            XCTAssertEqual(Set(store.choices.map(\.id)).count, store.choices.count)
            XCTAssertTrue(store.choices.allSatisfy { !$0.name.isEmpty })
        }
    }
    func testViewRetainsSameStoreAndPlayer() {
        let player = AVPlayer(), store = MediaSelectionStore(player: AVPlayer())
        let view = MediaSelectionExample(store: store)
        XCTAssertTrue(view.store === store)
        XCTAssertTrue(view.store.player === store.player)
        XCTAssertFalse(view.store.player === player)
    }
    func testCapturedBindingRejectsAfterCancellation() async throws {
        try await fixture { store, _, _, _ in
            let binding = store.selection, id = try XCTUnwrap(store.choices.first).id
            store.cancel()
            binding.wrappedValue = id
            XCTAssertNil(binding.wrappedValue)
            XCTAssertEqual(store.phase, .idle)
        }
    }
    func testActualRefreshPassesItemAndCharacteristicToLoader() async throws {
        try await fixture { store, item, _, group in
            var calls = 0
            await store.refresh { actual, characteristic in
                calls += 1
                XCTAssertTrue(actual === item)
                XCTAssertEqual(characteristic, .legible)
                return group
            }
            XCTAssertEqual(calls, 1)
            XCTAssertTrue(store.isCurrent)
        }
    }
    func testActualRefreshErrorSetsFailedPhase() async throws {
        try await fixture { store, _, _, _ in
            await store.refresh { _, _ in throw LoadError.unavailable }
            XCTAssertEqual(store.phase, .failed)
        }
    }
    func testActualRefreshAbsentSetsAbsentPhase() async throws {
        try await fixture { store, _, _, _ in
            await store.refresh { _, _ in nil }
            XCTAssertEqual(store.phase, .absent)
        }
    }
    func testCancelledOldTaskCannotCancelNewerLoad() async throws {
        try await fixture { store, _, _, group in
            var continuation: CheckedContinuation<Void, Never>?
            let task = Task { @MainActor in
                await store.refresh { _, _ in
                    await withCheckedContinuation { continuation = $0 }
                    return group
                }
            }
            while continuation == nil { await Task.yield() }
            task.cancel()
            let newer = store.beginLoad()
            continuation?.resume()
            await task.value
            store.complete(newer, result: .success(group))
            XCTAssertTrue(store.isCurrent)
        }
    }
    func testCancelledCurrentTaskDoesNotPublishResult() async throws {
        try await fixture { store, _, _, group in
            var continuation: CheckedContinuation<Void, Never>?
            let task = Task { @MainActor in
                await store.refresh { _, _ in
                    await withCheckedContinuation { continuation = $0 }
                    return group
                }
            }
            while continuation == nil { await Task.yield() }
            task.cancel()
            continuation?.resume()
            await task.value
            XCTAssertEqual(store.phase, .idle)
            XCTAssertTrue(store.choices.isEmpty)
        }
    }

    func testBindingWriteInvalidatesObservableSelection() async throws {
        try await fixture { store, _, _, _ in
            let flag = ObservationFlag()
            withObservationTracking { _ = store.selectedID } onChange: { flag.set() }
            store.selection.wrappedValue = try XCTUnwrap(store.choices.first).id
            XCTAssertTrue(flag.value)
        }
    }

    func testInvalidChoiceDoesNotInvalidateObservableSelection() async throws {
        try await fixture { store, _, _, _ in
            let flag = ObservationFlag()
            withObservationTracking { _ = store.selectedID } onChange: { flag.set() }
            XCTAssertFalse(store.choose("unknown"))
            XCTAssertFalse(flag.value)
        }
    }

    func testAlreadyCancelledTaskCannotStartLoad() async throws {
        try await fixture { store, _, _, group in
            var gate: CheckedContinuation<Void, Never>?
            var calls = 0
            let task = Task { @MainActor in
                await withCheckedContinuation { gate = $0 }
                await store.refresh { _, _ in calls += 1; return group }
            }
            while gate == nil { await Task.yield() }
            task.cancel()
            let ids = store.choices.map(\.id)
            gate?.resume()
            await task.value
            XCTAssertEqual(calls, 0)
            XCTAssertEqual(store.phase, .ready)
            XCTAssertEqual(store.choices.map(\.id), ids)
        }
    }
}

private final class ObservationFlag: @unchecked Sendable {
    private let lock = NSLock()
    private var changed = false
    func set() { lock.lock(); defer { lock.unlock() }; changed = true }
    var value: Bool { lock.lock(); defer { lock.unlock() }; return changed }
}
