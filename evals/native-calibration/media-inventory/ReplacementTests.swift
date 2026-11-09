import AVFoundation
import SwiftUI
import XCTest
@testable import YourAppModule

@MainActor final class ReplacementTests: XCTestCase {
    func testRetainedPickerAfterReplacement() async throws {
        let url = URL(fileURLWithPath: "FIXTURE_PATH")
        let a = AVPlayerItem(url: url), b = AVPlayerItem(url: url)
        let player = AVPlayer(playerItem: a)
        let state = MediaState(player: player)
        func bind(_ item: AVPlayerItem) async throws -> (Binding<String?>, AVMediaSelectionGroup) {
            let loaded = try await item.asset.loadMediaSelectionGroup(for: .legible)
            let text = try XCTUnwrap(loaded)
            let rows = text.options.enumerated().map { i, option in
                TrackChoice(id: String(i), name: option.displayName, descriptive: false, option: option)
            }
            XCTAssertTrue(text.allowsEmptySelection)
            guard rows.count >= 2 else { throw XCTSkip("fixture needs two caption options") }
            #if os(iOS)
            state.syncWithPlayerItem()
            state.loadOptions(for: item) { _, done in done(.success((rows, text))) }
            #else
            state.loadOptions { _ in (text, rows) }
            #endif
            for _ in 0..<500 {
                if case .loaded = state.loadState {
                    #if os(iOS)
                    return (state.selectionBinding, text)
                    #else
                    return (state.pickerBinding, text)
                    #endif
                }
                try await Task.sleep(nanoseconds: 10_000_000)
            }
            throw XCTSkip("injected load did not settle")
        }
        let (old, aText) = try await bind(a)
        old.wrappedValue = "0"
        XCTAssertEqual(a.currentMediaSelection.selectedMediaOption(in: aText), aText.options[0])
        player.replaceCurrentItem(with: b)
        let (current, text) = try await bind(b)
        let audible = try await b.asset.loadMediaSelectionGroup(for: .audible)
        let audio = try XCTUnwrap(audible)
        let described = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        b.select(described, in: audio)
        current.wrappedValue = "1"
        func check(_ option: AVMediaSelectionOption?, _ message: String) {
            XCTAssertEqual(b.currentMediaSelection.selectedMediaOption(in: text), option, message)
            XCTAssertEqual(b.currentMediaSelection.selectedMediaOption(in: audio), described, "preserve described audio")
        }
        check(text.options[1], "establish replacement selection")
        old.wrappedValue = nil
        check(text.options[1], "retired Off altered replacement")
        old.wrappedValue = "0"
        check(text.options[1], "retired option altered replacement")
        current.wrappedValue = nil
        check(nil, "current Off")
        current.wrappedValue = "0"
        check(text.options[0], "current option")
    }
}
