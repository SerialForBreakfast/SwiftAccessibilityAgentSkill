My SwiftUI player has a subtitle menu on iPhone and Apple TV. Some files offer two English options. Both should appear in this menu, even if the names or languages match. Choosing either should change the subtitles on the playing video without switching the viewer's audio track. What would you change in the code below, and how would you check that it works with the player rather than just the menu?

The caller has already loaded the legible group from the current item. This example only needs choices for the current load; selections aren't saved between launches.

```swift
import AVFoundation

@MainActor
final class SubtitleMenu {
    struct Choice: Identifiable {
        let id: String
        let option: AVMediaSelectionOption
    }

    let player: AVPlayer
    private var owner: AVPlayerItem?
    private var group: AVMediaSelectionGroup?
    private(set) var choices: [Choice] = []
    private(set) var selected: String?

    init(player: AVPlayer) { self.player = player }

    func load(item: AVPlayerItem, group: AVMediaSelectionGroup) {
        owner = item
        self.group = group
        choices = group.options.map {
            Choice(id: $0.extendedLanguageTag ?? $0.displayName, option: $0)
        }
        selected = nil
    }

    func choose(_ id: String) {
        guard choices.contains(where: { $0.id == id }) else { return }
        selected = id
    }
}
```
