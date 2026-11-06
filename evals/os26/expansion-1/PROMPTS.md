# Expansion prompts — draft 1

**Six proposed code cases · 0/6 gold-ready · no inference.** IDs07–12 are isolated from the existing frozen01–06 catalog. Acceptance keys are in a separate evaluator file.

## GP26-07 — Return to the current payment origin

iOS 26.0, UIKit.

Rows may be refreshed or removed while this payment panel is open. `rowButtons` always maps stable IDs to the current attached, visible, enabled buttons; `payButton` is a persistent fallback. All calls happen on the main thread, and only one panel is open at a time. After dismissal, attention should return to the originating row if it still exists, otherwise to `payButton`. The current code sometimes targets an old row before the panel has closed. Fix the code without adding a guessed delay or changing the payment operation.

```swift
import UIKit

final class PaymentPresenter {
    let host: UIViewController
    let payButton: UIButton
    var rowButtons: [UUID: UIButton] = [:]

    init(host: UIViewController, payButton: UIButton) {
        self.host = host
        self.payButton = payButton
    }

    func open(from id: UUID, panel: UIViewController) {
        let originalButton = rowButtons[id]
        host.present(panel, animated: true)
        // The panel's existing Done action calls this closure once.
        onDone = {
            UIAccessibility.post(notification: .layoutChanged,
                                 argument: originalButton)
            panel.dismiss(animated: true)
        }
    }

    var onDone: (() -> Void)?
}
```

## GP26-08 — Contain a custom popup and restore background state

iOS 26.0, UIKit.

This custom popup and `content` are siblings under `root`. `popup` is a container, not a single accessibility element; it contains a labeled Close button with its callback already wired. Both views already have valid layout. VoiceOver can reach background controls while the popup is open, and some screens remain inaccessible after closing it. Fix show/close behavior, preserving the value of `content.accessibilityElementsHidden` that existed before each opening. Repeated show or close calls must be harmless; assume no other component changes that flag while this popup is open. Do not replace the Close action or turn the whole popup into one leaf element.

```swift
import UIKit

final class PopupPresenter {
    let root: UIView
    let content: UIView
    let popup: UIView

    init(root: UIView, content: UIView, popup: UIView) {
        self.root = root
        self.content = content
        self.popup = popup
    }

    func show() {
        root.addSubview(popup)
        popup.accessibilityViewIsModal = false
    }

    func close() {
        popup.removeFromSuperview()
        content.accessibilityElementsHidden = true
    }
}
```

## GP26-09 — Make a custom volume knob adjustable

iOS 26.0, UIKit.

This knob is drawn elsewhere and the existing drag recognizer calls `dragChanged(to:)` with an integer percentage. It currently has no usable accessibility adjustment. Make its purpose, current value and adjustments accessible. The product step is 5 percentage points, the range is 0…100, and one real value change must call `onChange` exactly once. Clamped requests that leave the value unchanged must not call it. Preserve the drag path and do not add automatic announcements for every change.

```swift
import UIKit

final class VolumeKnob: UIView {
    private(set) var volume = 50
    var onChange: ((Int) -> Void)?

    func dragChanged(to requested: Int) {
        setVolume(requested)
    }

    private func setVolume(_ requested: Int) {
        let next = min(100, max(0, requested))
        guard next != volume else { return }
        volume = next
        onChange?(next)
        setNeedsDisplay()
    }
}
```

## GP26-10 — Report download progress without repeated announcements

iOS 26.0, UIKit.

The main-thread download callback reports integer percentages (display clamped to 0…100) and may repeat its terminal event. Only one download is active; `begin(id:)` starts a fresh unique ID. Late callbacks from an older ID and progress callbacks after the current operation has finished must be ignored. Keep the current percentage available as the label’s accessibility value without announcing every tick. Announce the first completion or failure once per ID; preserve its terminal state on duplicates. A later download must be able to announce its own outcome. Fix this implementation; no network code needs changing.

```swift
import UIKit

enum DownloadUpdate {
    case progress(Int)
    case completed
    case failed(String)
}

final class DownloadStatus {
    let label: UILabel
    private var activeID: UUID?

    init(label: UILabel) {
        self.label = label
        label.isAccessibilityElement = true
        label.accessibilityLabel = "Download"
    }

    func begin(id: UUID) {
        activeID = id
        label.text = "0%"
        label.accessibilityValue = "0%"
    }

    func receive(id: UUID, update: DownloadUpdate) {
        let text: String
        switch update {
        case .progress(let value): text = "\(value)%"
        case .completed: text = "Download complete"
        case .failed(let reason): text = "Download failed: \(reason)"
        }
        label.text = text
        label.accessibilityValue = text
        UIAccessibility.post(notification: .announcement, argument: text)
    }
}
```

## GP26-11 — Review a native volume slider

iOS 26.0, SwiftUI.

Review this volume setting for a concrete accessibility problem. Its parent owns a persisted volume value in 0…100 and supplies a working two-way binding. Keep that binding, the allowed range and one-point increments. Explain any change you recommend; do not change unrelated settings.

```swift
import SwiftUI

struct VolumeSettings: View {
    @Binding var volume: Double

    var body: some View {
        Form {
            Slider(value: $volume, in: 0...100, step: 1) {
                Text("Volume")
            }
        }
    }
}
```

## GP26-12 — Review a reduced-motion transition

iOS 26.0, SwiftUI.

Review this three-page view for a concrete accessibility problem. The user can change Reduce Motion while it is open; the next page change should follow the current preference without resetting the selected page. Content and next-page behavior must stay the same. No other animations or parent transactions are applied. Explain any change you recommend.

```swift
import SwiftUI

enum PageMotionPolicy {
    static func shouldAnimate(reduceMotion: Bool) -> Bool {
        !reduceMotion
    }
}

struct PageView: View {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var page = 0
    private let pages = ["Account", "Playback", "Downloads"]

    var body: some View {
        VStack {
            Text(pages[page])
                .id(page)
                .transition(.slide)
            Button("Next page") {
                page = (page + 1) % pages.count
            }
        }
        .animation(
            PageMotionPolicy.shouldAnimate(reduceMotion: reduceMotion)
                ? .easeInOut(duration: 0.2) : nil,
            value: page
        )
    }
}
```

