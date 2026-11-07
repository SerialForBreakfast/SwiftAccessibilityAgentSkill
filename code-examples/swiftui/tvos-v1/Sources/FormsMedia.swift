import SwiftUI
import Observation
import AVKit

@MainActor @Observable
final class FormMediaState {
    var text = ""
    private(set) var error: String?
    private(set) var busy = false
    private var generation = 0
    private var active: Int?
    var accepted: (String) -> Void = { _ in }
    var validate: (String, @escaping @MainActor (String?) -> Void) -> Void = { _, reply in reply(nil) }
    var input: Binding<String> {
        Binding(get: { self.text }, set: { value in self.text = value; self.cancel() })
    }
    func cancel() { generation += 1; active = nil; busy = false; error = nil }
    func submit() {
        generation += 1; let ticket = generation, snapshot = text
        active = ticket; busy = true; error = nil
        validate(snapshot) { [weak self] message in
            guard let self, self.active == ticket else { return }
            guard self.text == snapshot else { self.cancel(); return }
            self.active = nil; self.busy = false
            if let message { self.error = message.isEmpty ? "Validation unavailable" : message }
            else { self.accepted(snapshot) }
        }
    }
}

struct TrackChoice: Identifiable, Equatable {
    let id: String
    let name: String
    let descriptive: Bool
}

@MainActor @Observable
final class MediaState {
    let player: AVPlayer
    private(set) var tracks: [TrackChoice] = []
    private(set) var selected: String?
    private(set) var loaded = false
    private var generation = 0
    private var active: Int?
    init(player: AVPlayer = AVPlayer()) { self.player = player }
    var status: String { !loaded ? "Options unavailable" : tracks.isEmpty ? "No caption options" : "\(tracks.count) caption options" }
    func load(_ loader: (@escaping @MainActor ([TrackChoice]) -> Void) -> Void) {
        generation += 1; let ticket = generation; active = ticket; loaded = false
        loader { [weak self] tracks in
            guard let self, self.active == ticket else { return }
            self.active = nil
            guard Set(tracks.map(\.id)).count == tracks.count else { return }
            self.tracks = tracks; self.loaded = true
            if let selected = self.selected, !tracks.contains(where: { $0.id == selected }) { self.selected = nil }
        }
    }
    func choose(_ id: String?) {
        guard loaded, id == nil || tracks.contains(where: { $0.id == id }) else { return }
        selected = id
    }
}

struct FormMediaExample: View {
    @Bindable var form: FormMediaState
    @Bindable var media: MediaState
    var body: some View {
        VStack {
            TextField("Email", text: form.input)
            if let error = form.error { Text(error).accessibilityLabel("Error: \(error)") }
            Button("Save", action: form.submit).disabled(form.busy)
            VideoPlayer(player: media.player)
            Text(media.status)
            ForEach(media.tracks) { track in
                Button(track.name) { media.choose(track.id) }
                    .accessibilityValue(media.selected == track.id ? "Selected" : "Not selected")
            }
        }
    }
}
