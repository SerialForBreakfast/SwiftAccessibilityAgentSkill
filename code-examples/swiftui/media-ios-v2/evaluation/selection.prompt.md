# iOS developer question

My SwiftUI video screen only changes a local selected value when someone chooses captions. Connect the choices to the real media item without resetting audio or playback settings. Offer complete captions rather than tracks with just occasional translated lines. Preserve a current choice outside that list without pretending it is Off. Include focused unit tests. Target iOS26 or later. Here is the complete current file:

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
