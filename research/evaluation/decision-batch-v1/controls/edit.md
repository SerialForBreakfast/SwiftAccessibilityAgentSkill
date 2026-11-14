iOS 26 / UIKit

Our editor keeps this Rename command while the document is open. Opening the menu doesn't change permissions, but another part of the app can change them. Should we replace the command to keep Rename usable and respect permission changes? Explain using the code as supplied.

```swift
import UIKit

@MainActor final class Editor {
    var editable = true
    var names: [String] = []
    func installRename() -> (String) -> Bool {
        { [weak self] name in
            guard let self, self.editable else { return false }
            self.names.append(name)
            return true
        }
    }
}
```
