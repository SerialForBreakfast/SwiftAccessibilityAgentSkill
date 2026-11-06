import UIKit

// Intentional compiler rejection: accessibilityLabel accepts String?, not Int.
@MainActor func invalidLabelType() {
    UILabel().accessibilityLabel = 42
}
