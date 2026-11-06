import XCTest
import AVFoundation
@testable import AccessibilityExamples

@MainActor
final class MediaMetadataTests: XCTestCase {
    private func options(_ evidence: GroupEvidence) -> [MediaOptionEvidence] {
        if case .loaded(let options) = evidence { return options }
        return []
    }

    func testTaggedOptionIsRecognizedWithoutInferringOtherAudio() async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let result = try await MediaMetadata.group(.audible, item: AVPlayerItem(url: url))
        let rows = options(result)
        XCTAssertEqual(rows.count, 2)
        XCTAssertEqual(rows.filter(\.describesVideo).count, 1)
        XCTAssertEqual(rows.first(where: { $0.describesVideo })?.language, "es")
        XCTAssertEqual(rows.first(where: { $0.language == "en" })?.describesVideo, false)
        XCTAssertTrue(rows.allSatisfy { !$0.name.isEmpty })
    }

    func testUntaggedAlternateAudioIsNotDescription() async throws {
        let url = try DescriptionFixture.write(tagged: false)
        defer { try? FileManager.default.removeItem(at: url) }
        let rows = options(try await MediaMetadata.group(.audible, item: AVPlayerItem(url: url)))
        XCTAssertEqual(rows.count, 2)
        XCTAssertTrue(rows.allSatisfy { !$0.describesVideo })
    }

    func testInspectionPreservesChosenAudioAndSubtitleOff() async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loadedAudio = try await asset.loadMediaSelectionGroup(for: .audible)
        let loadedText = try await asset.loadMediaSelectionGroup(for: .legible)
        let audio = try XCTUnwrap(loadedAudio)
        let text = try XCTUnwrap(loadedText)
        let chosen = try XCTUnwrap(audio.options.first { $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        let item = AVPlayerItem(asset: asset)
        item.select(chosen, in: audio)
        item.select(nil, in: text)
        let rows = options(try await MediaMetadata.group(.audible, item: item))
        let captions = options(try await MediaMetadata.group(.legible, item: item))
        XCTAssertEqual(rows.filter(\.selected).count, 1)
        XCTAssertEqual(rows.first(where: { $0.selected })?.describesVideo, true)
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audio), chosen)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: text))
        XCTAssertFalse(captions.contains(where: { $0.selected }))
    }

    func testLoadedItemDurationAndSubtitleVariants() async throws {
        let url = try DescriptionFixture.write(tagged: true)
        defer { try? FileManager.default.removeItem(at: url) }
        let item = AVPlayerItem(url: url)
        let duration = try await MediaMetadata.duration(item: item)
        XCTAssertTrue(duration.isNumeric)
        XCTAssertEqual(duration.seconds, 1, accuracy: 0.05)
        let rows = options(try await MediaMetadata.group(.legible, item: item))
        XCTAssertEqual(rows.filter { !$0.forcedOnly }.count, 2)
        XCTAssertEqual(rows.filter(\.forcedOnly).count, 2)
        XCTAssertEqual(Set(rows.compactMap(\.language)), ["en", "es"])
    }

    func testMissingItemIsUnavailableRatherThanAbsent() async throws {
        let result = try await MediaMetadata.group(.audible, item: nil)
        let unavailable: Bool
        if case .unavailable = result { unavailable = true } else { unavailable = false }
        XCTAssertTrue(unavailable)
    }

    func testKnownMissingGroupIsAbsent() async throws {
        let item = AVPlayerItem(asset: AVMutableComposition())
        let result = try await MediaMetadata.group(.audible, item: item)
        let absent: Bool
        if case .absent = result { absent = true } else { absent = false }
        XCTAssertTrue(absent)
    }

    func testUnreadableLocalAssetPropagatesError() async throws {
        let url = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString).appendingPathExtension("mov")
        let item = AVPlayerItem(url: url)
        var threw = false
        do { _ = try await MediaMetadata.group(.audible, item: item) } catch { threw = true }
        XCTAssertTrue(threw)
    }
}
