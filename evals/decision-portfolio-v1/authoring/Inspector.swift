import AVFoundation

struct Entry { let title: String }
enum AudioInventory { case waiting, empty, entries([Entry]) }

func inventory(for item: AVPlayerItem?) async throws -> AudioInventory {
    guard let item else { return .waiting }
    guard let group = try await item.asset.loadMediaSelectionGroup(for: .audible)
    else { return .empty }
    return .entries(group.options.map { Entry(title: $0.displayName) })
}
