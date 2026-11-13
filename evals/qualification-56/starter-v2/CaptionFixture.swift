import AVFoundation
import Foundation

@MainActor
struct CaptionFixture {
    let item: AVPlayerItem
    let legible: AVMediaSelectionGroup
    let audible: AVMediaSelectionGroup
    let ordinary: AVMediaSelectionOption
    let forced: AVMediaSelectionOption
    let audio: AVMediaSelectionOption

    enum Initial { case ordinary, forced }
    enum FixtureError: Error { case missingMovie, missingGroup, unexpectedTracks, selectionFailed }

    static func open(selected initial: Initial) async throws -> Self {
        guard let url = Bundle.module.url(forResource: "Captions", withExtension: "mov")
        else { throw FixtureError.missingMovie }
        let asset = AVURLAsset(url: url)
        let item = AVPlayerItem(asset: asset)
        guard let legible = try await asset.loadMediaSelectionGroup(for: .legible),
              let audible = try await asset.loadMediaSelectionGroup(for: .audible)
        else { throw FixtureError.missingGroup }
        // Ordinals are an inventory of this pinned movie, not a selection policy
        // for arbitrary assets. AVFoundation offers a forced-only variant of
        // each subtitle track. Validate language and flags independently below.
        guard legible.options.count == 4, audible.options.count == 2 else { throw FixtureError.unexpectedTracks }
        let ordinary = legible.options[2], forced = legible.options[1], audio = audible.options[1]
        guard ordinary.extendedLanguageTag == "es", forced.extendedLanguageTag == "en",
              audio.extendedLanguageTag == "es", legible.allowsEmptySelection,
              !ordinary.hasMediaCharacteristic(.containsOnlyForcedSubtitles),
              forced.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
        else { throw FixtureError.unexpectedTracks }
        let choice = initial == .ordinary ? ordinary : forced
        item.select(audio, in: audible)
        item.select(choice, in: legible)
        guard item.currentMediaSelection.selectedMediaOption(in: legible) == choice,
              item.currentMediaSelection.selectedMediaOption(in: audible) == audio
        else { throw FixtureError.selectionFailed }
        return Self(item: item, legible: legible, audible: audible, ordinary: ordinary,
                    forced: forced, audio: audio)
    }
}
