import AVFoundation

public struct MediaOptionEvidence {
    public let name: String
    public let language: String?
    public let describesVideo: Bool
    public let forcedOnly: Bool
    public let selected: Bool
}

public enum GroupEvidence {
    case unavailable
    case absent
    case loaded([MediaOptionEvidence])
}

@MainActor
public enum MediaMetadata {
    // A completed load establishes asset metadata, not player readiness or content quality.
    public static func group(_ characteristic: AVMediaCharacteristic,
                             item: AVPlayerItem?) async throws -> GroupEvidence {
        guard let item else { return .unavailable }
        guard let group = try await item.asset.loadMediaSelectionGroup(for: characteristic) else {
            return .absent
        }
        let selected = item.currentMediaSelection.selectedMediaOption(in: group)
        return .loaded(group.options.map { option in
            MediaOptionEvidence(name: option.displayName,
                language: option.locale?.languageCode,
                describesVideo: true,
                forcedOnly: option.hasMediaCharacteristic(.containsOnlyForcedSubtitles),
                selected: option == selected)
        })
    }

    public static func duration(item: AVPlayerItem) async throws -> CMTime {
        try await item.asset.load(.duration)
    }
}
