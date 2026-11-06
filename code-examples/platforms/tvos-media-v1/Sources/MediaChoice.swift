import AVFoundation

@MainActor
public enum MediaChoice {
    // Explicit user choice only. The group must come from this item's asset.
    @discardableResult
    public static func select(language: String, requiresDescription: Bool = false,
                              in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
        guard let option = group.options.first(where: {
            $0.locale?.language.languageCode?.identifier == language &&
            !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) &&
            (!requiresDescription || $0.hasMediaCharacteristic(.describesVideoForAccessibility))
        }) else { return false }
        item.select(option, in: group)
        return true
    }
    @discardableResult
    public static func turnOff(in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
        return requestOff(allowed: group.allowsEmptySelection) { item.select(nil, in: group) }
    }
    // Separate application-policy seam; tests do not invent native group permissions.
    static func requestOff(allowed: Bool, clear: () -> Void) -> Bool {
        guard allowed else { return false }
        clear()
        return true
    }
}
