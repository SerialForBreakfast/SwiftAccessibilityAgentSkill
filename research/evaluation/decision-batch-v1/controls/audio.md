tvOS 26 / SwiftUI

Our audio menu lets someone pick a specific track. Its other command, Follow System, hands track choice back to the player for the audio group currently being displayed. The player is configured to apply automatic media-selection criteria, and the user previously selected a specific option in this same item's audio group. The menu is discarded when the item changes. Would this command implement that policy, or would you change it? What outcome can the code guarantee?

```swift
import AVFoundation
import SwiftUI

@MainActor func followSystem(_ automatic: @escaping () -> Void) -> () -> Void {
    { automatic() }
}

@MainActor func audioCommand(item: AVPlayerItem, group: AVMediaSelectionGroup) -> some View {
    Button("Follow System", action: followSystem {
        item.selectMediaOptionAutomatically(in: group)
    })
}
```
