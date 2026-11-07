import SwiftUI
import Observation
import AVKit

struct MediaOption: Identifiable {
    let id: String
    let name: String
    let option: AVMediaSelectionOption
}

@MainActor @Observable
final class MediaSelectionStore {
    enum Phase: Equatable { case idle, loading, noItem, absent, failed, ready }
    let player: AVPlayer
    let characteristic: AVMediaCharacteristic
    private(set) var phase: Phase = .idle
    private(set) var choices: [MediaOption] = []
    private var group: AVMediaSelectionGroup?
    private var item: AVPlayerItem?
    private var generation = 0
    private var active: Int?
    private var selectionRevision = 0

    init(player: AVPlayer, characteristic: AVMediaCharacteristic = .legible) {
        self.player = player
        self.characteristic = characteristic
    }

    var isCurrent: Bool { phase == .ready && item != nil && player.currentItem === item }
    var allowsOff: Bool { isCurrent && group?.allowsEmptySelection == true }
    var selectedID: String? {
        _ = selectionRevision
        guard isCurrent, let item, let group,
              let selected = item.currentMediaSelection.selectedMediaOption(in: group) else { return nil }
        return choices.first { $0.option == selected }?.id
    }
    var selection: Binding<String?> {
        Binding(get: { self.selectedID }, set: { _ = self.choose($0) })
    }
    var status: String {
        switch phase {
        case .idle: return "Options not loaded"
        case .loading: return "Loading options"
        case .noItem: return "No media item"
        case .absent: return "No options available"
        case .failed: return "Options could not be loaded"
        case .ready: return isCurrent ? "\(choices.count) options" : "Media item changed; reload options"
        }
    }

    // Each completion belongs to one item and one load. Cancellation invalidates
    // ownership even when an injected loader does not cooperate with cancellation.
    func beginLoad() -> Int {
        generation += 1
        active = generation
        item = player.currentItem
        group = nil
        choices = []
        phase = item == nil ? .noItem : .loading
        if item == nil { active = nil }
        return generation
    }

    func complete(_ ticket: Int, result: Result<AVMediaSelectionGroup?, Error>) {
        guard active == ticket, let item, player.currentItem === item else { return }
        active = nil
        switch result {
        case .failure: phase = .failed
        case .success(nil): phase = .absent
        case .success(let loaded?):
            group = loaded
            choices = loaded.options.enumerated().compactMap { index, option in
                guard !option.hasMediaCharacteristic(.containsOnlyForcedSubtitles) else { return nil }
                return MediaOption(id: "\(ticket):\(index)", name: option.displayName, option: option)
            }
            phase = .ready
        }
    }

    func refresh(using loader: @MainActor (AVPlayerItem, AVMediaCharacteristic) async throws -> AVMediaSelectionGroup? = { item, characteristic in
        try await item.asset.loadMediaSelectionGroup(for: characteristic)
    }) async {
        guard !Task.isCancelled else { return }
        let ticket = beginLoad()
        guard let item else { return }
        do {
            let loaded = try await loader(item, characteristic)
            guard !Task.isCancelled else { cancel(ticket: ticket); return }
            complete(ticket, result: .success(loaded))
        } catch {
            guard !Task.isCancelled else { cancel(ticket: ticket); return }
            complete(ticket, result: .failure(error))
        }
    }

    private func cancel(ticket: Int) {
        // MUTANT: old cancellation clears newer ownership
        cancel()
    }

    func cancel() {
        generation += 1
        active = nil
        group = nil
        choices = []
        item = nil
        phase = .idle
    }

    @discardableResult
    func choose(_ id: String?) -> Bool {
        guard isCurrent, let group, let item else { return false }
        if let id {
            guard let choice = choices.first(where: { $0.id == id }) else { return false }
            item.select(choice.option, in: group)
        } else {
            guard allowsOff else { return false }
            item.select(nil, in: group)
        }
        selectionRevision += 1
        return true
    }
}

struct MediaSelectionExample: View {
    @Bindable var store: MediaSelectionStore
    @State private var reloadID = 0
    var body: some View {
        VStack {
            VideoPlayer(player: store.player)
            Text(store.status)
            Button("Reload options") { reloadID += 1 }
            Picker("Media options", selection: store.selection) {
                if store.allowsOff { Text("Off").tag(nil as String?) }
                ForEach(store.choices) { choice in
                    Text(choice.name).tag(Optional(choice.id))
                }
            }
            .disabled(!store.isCurrent)
        }
        .task(id: reloadID) { await store.refresh() }
        .onDisappear { store.cancel() }
    }
}
