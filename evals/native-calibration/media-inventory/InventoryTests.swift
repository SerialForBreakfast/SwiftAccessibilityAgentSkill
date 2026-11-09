import XCTest
import AVFoundation
@testable import Inventory

@MainActor final class InventoryTests: XCTestCase {
    func testLoadAndChooseEveryNativeOption() async throws {
        let url = URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("sample.mov")
        let item = AVPlayerItem(url: url)
        let captions = try await item.asset.loadMediaSelectionGroup(for: .legible)
        let audible = try await item.asset.loadMediaSelectionGroup(for: .audible)
        let text = try XCTUnwrap(captions), audio = try XCTUnwrap(audible)
        let options = text.options
        XCTAssertGreaterThan(options.count, 1, "fixture must expose multiple native options")
        let labels = options.map { $0.extendedLanguageTag ?? $0.displayName }
        XCTAssertLessThan(Set(labels).count, options.count, "fixture must expose colliding native keys")
        let track = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        XCTAssertTrue(text.allowsEmptySelection)
        item.select(track, in: audio)
        item.select(nil, in: text)
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), track)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text))

        let store = MediaSelectionStore(player: AVPlayer(playerItem: item))
        await store.refresh()
        XCTAssertEqual(store.phase, .ready, "inventory must load despite language collision")
        XCTAssertEqual(store.choices.count, options.count, "retain all requested options")
        XCTAssertEqual(Set(store.choices.map(\.id)).count, options.count, "independently addressable options")
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text), "inspection is read-only")
        for option in options {
            let choice = try XCTUnwrap(store.choices.first { $0.option == option })
            store.selection.wrappedValue = choice.id
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: text), option, "real caption write")
            XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), track, "preserve audio")
        }
    }
}
