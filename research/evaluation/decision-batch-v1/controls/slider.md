iOS 26 / SwiftUI

This preview-volume row writes to the parent's persisted setting. Product wants a named adjustable control, integer steps from 0 to 100, and no extra stop for the title. Is there a change you would make before shipping this row? Explain what the code tells you.

```swift
import SwiftUI

struct PreviewVolume: View {
    @Binding var level: Double
    var body: some View {
        Slider(value: $level, in: 0...100, step: 1) { Text("Preview volume") }
    }
}
```
