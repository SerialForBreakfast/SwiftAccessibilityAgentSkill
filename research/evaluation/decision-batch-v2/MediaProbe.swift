import Foundation
import AVFoundation

@main struct MediaProbe {
    @MainActor static func main() async throws {
        let item = AVPlayerItem(url: URL(fileURLWithPath: CommandLine.arguments[1]))
        guard let group = try await item.asset.loadMediaSelectionGroup(for: .legible) else { throw ProbeError.noFixture }
        let options = group.options.filter { $0.locale?.language.languageCode?.identifier == "en" }
        let forced: (AVMediaSelectionOption) -> Bool = { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) }
        print("English forced flags in native order:", options.map(forced))
        guard let f = options.first(where: forced), let full = options.first(where: { !forced($0) }) else { throw ProbeError.noFixture }
        // Isolate the ordering hazard without faking either native option or the group.
        for choices in [[f, full], [full, f]] {
            guard let choice = choices.first(where: { !forced($0) }) else { throw ProbeError.noFixture }
            item.select(choice, in: group)
            guard item.currentMediaSelection.selectedMediaOption(in: group) == full else { throw ProbeError.wrongSelection }
        }
        item.select([f,full][0], in: group)
        guard item.currentMediaSelection.selectedMediaOption(in: group) == f else { throw ProbeError.wrongSelection }
        print("Both input orders selected full; language-only first-match selected forced.")
    }
    enum ProbeError: Error { case noFixture, wrongSelection }
}
