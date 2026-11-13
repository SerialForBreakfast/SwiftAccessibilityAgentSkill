import AVKit
import SwiftUI

struct CaptionOption: Identifiable, Equatable {
    let id: String
    let name: String
    var mediaOption: AVMediaSelectionOption? = nil
}

@MainActor @Observable final class CaptionState {
    enum Status { case idle, loading, missingItem, noOptions, failed, ready, changedItem }
    let player: AVPlayer
    private let store: MediaSelectionStore
    private(set) var legibleGroup: AVMediaSelectionGroup?
    init(player: AVPlayer) { self.player = player; self.store = MediaSelectionStore(player: player) }
    var state: Status { status }
    var status: Status {
        switch store.phase {
        case .idle: .idle
        case .loading: .loading
        case .noItem: .missingItem
        case .absent: .noOptions
        case .failed: .failed
        case .ready: .ready
        case .changedItem: .changedItem
        }
    }
    private var injected: [CaptionOption]?
    private var injectedSelection: String?
    private var loadingInjected = false
    private var revision = 0
    func nextRevision() { revision += 1 }
    var options: [CaptionOption] {
        if let injected { return injected }
        return store.choices.map { CaptionOption(id: $0.id, name: $0.name, mediaOption: $0.option) }
    }
    var selectedOptionID: String? { store.selectedID }
    var selected: String? { injected == nil ? store.selectedID : injectedSelection }
    var loading: Bool { loadingInjected || store.phase == .loading }
    var captionBinding: Binding<String?> { store.selection }
    var selectionBinding: Binding<String?> {
        guard injected != nil || loadingInjected else { return store.selection }
        let ticket = revision, owner = player.currentItem
        return Binding(get: { self.selected }, set: { id in
            guard ticket == self.revision, self.player.currentItem === owner else { return }
            self.choose(id)
        })
    }
    func scopedSelectionBinding() -> Binding<String?> { selectionBinding }
    func choose(_ id: String?) {
        if let injected {
            guard id == nil || injected.contains(where: { $0.id == id }) else { return }
            injectedSelection = id
        } else { _ = store.choose(id) }
    }
    func choose(_ id: String?, for item: AVPlayerItem) {
        guard player.currentItem === item else { return }
        choose(id)
    }
    func handleItemChange(to item: AVPlayerItem) { playerItemDidChange(to: item) }
    func playerItemDidChange(to item: AVPlayerItem) { cancelLoading() }
    func cancelLoading() { nextRevision(); injected = nil; injectedSelection = nil; loadingInjected = false; store.cancel(); legibleGroup = nil }
    func loadCaptions() async { await loadOptions() }
    func load() async { await loadOptions() }
    func loadOptions() async {
        let ticket = store.beginLoad()
        guard let item = player.currentItem else { return }
        do {
            let group = try await item.asset.loadMediaSelectionGroup(for: .legible)
            store.complete(ticket, result: .success(group))
            if store.isCurrent { legibleGroup = group }
        } catch { store.complete(ticket, result: .failure(error)) }
    }
    // Injected String options exercise starter state, not a native media selection.
    func load(using loader: (@escaping @MainActor ([CaptionOption]) -> Void) -> Void) {
        nextRevision()
        let ticket = revision, item = player.currentItem
        loadingInjected = true
        loader { options in
            guard self.revision == ticket, self.player.currentItem === item else { return }
            self.injected = options
            self.loadingInjected = false
        }
    }
    func load(for item: AVPlayerItem, using loader: @escaping (AVPlayerItem) async -> [CaptionOption]) {
        guard item === player.currentItem else { return }
        load { complete in Task { complete(await loader(item)) } }
    }
}
