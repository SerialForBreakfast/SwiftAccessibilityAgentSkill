import XCTest
import UIKit
import AVKit
import AVFoundation
@testable import AccessibilityExamples

@MainActor
final class MediaUIKitTests: XCTestCase {
    func testNativeControllerPreservesControlsAndAutomaticSelection() {
        let player = AVPlayer()
        let controller = MediaConfiguration.controller(player: player)
        XCTAssertTrue(controller.player === player)
        XCTAssertTrue(controller.showsPlaybackControls)
        XCTAssertFalse(controller.requiresLinearPlayback)
        XCTAssertTrue(player.appliesMediaSelectionCriteriaAutomatically)
        XCTAssertEqual(player.rate, 0)
    }

    func testPlayPauseControlMetadataTransitions() {
        let button = UIButton(type: .system)
        MediaConfiguration.configure(button, playing: false)
        XCTAssertEqual(button.title(for: .normal), "Play")
        XCTAssertEqual(button.accessibilityLabel, "Play")
        XCTAssertEqual(button.accessibilityValue, "Paused")
        MediaConfiguration.configure(button, playing: true)
        XCTAssertEqual(button.title(for: .normal), "Pause")
        XCTAssertEqual(button.accessibilityLabel, "Pause")
        XCTAssertEqual(button.accessibilityValue, "Playing")
        XCTAssertTrue(button.accessibilityTraits.contains(.button))
    }

    func testTimelineValueAndBounds() {
        let slider = UISlider()
        MediaConfiguration.configureTimeline(slider, elapsed: 30, duration: 120)
        XCTAssertTrue(slider.isEnabled)
        XCTAssertEqual(slider.value, 0.25)
        XCTAssertEqual(slider.accessibilityLabel, "Playback position")
        XCTAssertEqual(slider.accessibilityValue, "30 of 120 seconds")
        for (elapsed, expected) in [(-4.0, Float(0)), (140.0, Float(1))] {
            MediaConfiguration.configureTimeline(slider, elapsed: elapsed, duration: 120)
            XCTAssertEqual(slider.value, expected)
        }
    }

    func testUnavailableTimelineResetsPreviousState() {
        let slider = UISlider()
        for duration: Double? in [nil, 0, -1, .infinity, .nan, .greatestFiniteMagnitude] {
            MediaConfiguration.configureTimeline(slider, elapsed: 30, duration: 120)
            MediaConfiguration.configureTimeline(slider, elapsed: 30, duration: duration)
            XCTAssertFalse(slider.isEnabled)
            XCTAssertEqual(slider.value, 0)
            XCTAssertEqual(slider.accessibilityValue, "Position unavailable")
        }
        MediaConfiguration.configureTimeline(slider, elapsed: .nan, duration: 120)
        XCTAssertFalse(slider.isEnabled)
    }

    func testSubtitleOptionsExposeBothAuthoredLanguages() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        for option in group.options {
            print("MEDIA_OPTION name=\(option.displayName) language=\(option.locale?.languageCode ?? "nil") forced=\(option.hasMediaCharacteristic(.containsOnlyForcedSubtitles)) type=\(option.mediaType.rawValue)")
        }
        XCTAssertEqual(Set(group.options.compactMap { $0.locale?.languageCode }), ["en", "es"])
        XCTAssertEqual(group.options.count, 2)
        XCTAssertTrue(group.options.allSatisfy { !$0.displayName.isEmpty })
        XCTAssertTrue(group.allowsEmptySelection)
    }

    func testSubtitleSelectionAndOffState() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        let item = AVPlayerItem(asset: asset)
        XCTAssertTrue(MediaConfiguration.select(language: "es", in: group, item: item))
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: group, item: item), "es")
        item.select(nil, in: group)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: group))
    }

    func testMissingSubtitleLanguagePreservesSelection() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        let item = AVPlayerItem(asset: asset)
        XCTAssertTrue(MediaConfiguration.select(language: "en", in: group, item: item))
        XCTAssertFalse(MediaConfiguration.select(language: "de", in: group, item: item))
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: group, item: item), "en")
    }

    func testAlternateAudioDoesNotReplaceSubtitleSelection() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loadedAudio = try await asset.loadMediaSelectionGroup(for: .audible)
        let loadedText = try await asset.loadMediaSelectionGroup(for: .legible)
        let audio = try XCTUnwrap(loadedAudio), text = try XCTUnwrap(loadedText)
        XCTAssertEqual(Set(audio.options.compactMap { $0.locale?.languageCode }), ["en", "es"])
        let item = AVPlayerItem(asset: asset)
        XCTAssertTrue(MediaConfiguration.select(language: "es", in: text, item: item))
        XCTAssertTrue(MediaConfiguration.select(language: "en", in: audio, item: item))
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: text, item: item), "es")
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: audio, item: item), "en")
    }
}
