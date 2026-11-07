# iOS developer question

Build a SwiftUI media-option picker using the same player as the video view. It should show the real selection, distinguish loading, absent options and failure, and allow retry. Keep normal player controls. Include focused unit tests and state which external changes require an explicit reload. Target iOS26 or later. Here is the complete current file:

```swift
import SwiftUI
import Observation
import AVKit

struct CaptionOption: Identifiable {
    let id: String
    let name: String
}

@MainActor @Observable
final class CaptionState {
    let player: AVPlayer
    var options: [CaptionOption] = []
    var selected: String?
    var loading = false
    init(player: AVPlayer) { self.player = player }
    func load(using loader: (@escaping @MainActor ([CaptionOption]) -> Void) -> Void) {
        loading = true
        loader { options in self.options = options; self.loading = false }
    }
    func choose(_ id: String?) { selected = id }
}

struct CaptionScreen: View {
    @Bindable var state: CaptionState
    var body: some View {
        VStack {
            VideoPlayer(player: state.player)
            Picker("Captions", selection: Binding(get: { state.selected }, set: { state.choose($0) })) {
                Text("Off").tag(nil as String?)
                ForEach(state.options) { option in Text(option.name).tag(Optional(option.id)) }
            }
        }
    }
}
```
