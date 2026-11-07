# tvOS developer question

People can change videos or reload caption choices while this SwiftUI screen is open. Old callbacks sometimes affect the new selection, including turning captions off. Make these operations belong to the right item and request, and include focused unit tests. Explain how the screen should react when the player item changes and what cancellation does. Target tvOS26 or later. Here is the complete current file:

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
