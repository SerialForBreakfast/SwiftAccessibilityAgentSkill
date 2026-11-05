# Gold prompts - OS26 code-contract baseline

Revision `os26-code-contract-4`. Six development cases; zero validated gold fixtures.

Owner decision: compile checks and unit tests, with independent source review. No mandatory manual verification or UI tests. VoiceOver traversal/speech, remote or keyboard navigation and rendered layout are not measured outcomes. The prior catalog is preserved under `evals/os26/archive/os26-draft-2/`. User questions are unchanged; only the measured acceptance scope changed.

[Promotion protocol](evals/os26/README.md). Do not send evaluator gates, candidate fixes or mutation sources to the model. Historical outputs are not new baseline results.

## GP26-01

### Exact model input

iOS 26.0, UIKit.

VoiceOver only stops on “Downloads” in this settings row. People cannot change the setting or open Help. The existing callbacks are already wired. Can you fix it?

```swift
let row = UIStackView(arrangedSubviews: [titleLabel, downloadSwitch, helpButton])
titleLabel.text = "Downloads"
helpButton.setTitle("Help", for: .normal)
row.isAccessibilityElement = true
row.accessibilityLabel = titleLabel.text
row.accessibilityElementsHidden = true
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | The oracle rejects this single-error mutation: Hide interactive descendants Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| mutation-2 | unit oracle | fail | The oracle rejects this single-error mutation: Drop Help callback Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| switch-state | unit | pass | Unit test public row/child accessibility configuration and directly dispatch switch value-change events; assert current switch state and only the setting callback changes. This does not assert VoiceOver traversal. |
| help-action | unit | pass | Directly dispatch Help activation and assert one Help callback with no switch-state or setting-callback change. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.

## GP26-02

### Exact model input

iOS 26.0, UIKit.

After scrolling and refreshing orders, a cell sometimes announces the previous customer or status. Here is its configuration code; the model has customer/status strings and an isPriority flag, and titleLabel is already laid out. What should change?

```swift
final class OrderCell: UITableViewCell {
    let titleLabel = UILabel()
    func configure(_ order: Order) {
        titleLabel.text = order.customer
        isAccessibilityElement = true
        if order.isPriority {
            accessibilityLabel = "Priority order for \(order.customer)"
            accessibilityValue = order.status
        }
    }
}
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | The oracle rejects this single-error mutation: Skip normal-order label reset Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| mutation-2 | unit oracle | fail | The oracle rejects this single-error mutation: Leave status from previous order Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| reconfiguration | unit | pass | Configure priority Alice/shipped, then nonpriority Bob/processing on the SAME instance without prepareForReuse: label names Bob without stale priority and value reports processing; reverse ordering also works. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.

## GP26-03

### Exact model input

iOS 26.0, UIKit.

Customers using larger text cannot read the complete checkout total. The container fills the safe-area width, and formattedTotal can be a long localized currency value. The Pay button already works and its appearance should stay the same. Can you fix this layout?

```swift
totalLabel.text = formattedTotal
totalLabel.font = .systemFont(ofSize: 17)
totalLabel.numberOfLines = 1
payButton.setTitle("Pay now", for: .normal)
let summary = UIStackView(arrangedSubviews: [totalLabel, payButton])
summary.axis = .horizontal
summary.distribution = .fillEqually
summary.heightAnchor.constraint(equalToConstant: 44).isActive = true
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | The oracle rejects this single-error mutation: Keep fixed container height Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| mutation-2 | unit oracle | fail | The oracle rejects this single-error mutation: Disable live text scaling Require an executed focused unit assertion against this exact variant; source inspection alone is not a mutation kill. |
| live-resize | unit | pass | Assert text-scaling configuration and layout-policy prerequisites for long localized totals, including multiline text and absence of a fixed enclosing height. This does not assert rendered layout or readability. |
| payment-action | unit | pass | Directly dispatch payment activation and assert one existing callback; compare exposed button configuration before/after rather than visual appearance. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.

## GP26-04

### Exact model input

iPadOS 26.0, SwiftUI.

Our message row can only delete by swiping. Add an on-screen way to delete that works with VoiceOver and with Full Keyboard Access plus a hardware keyboard. Keep swipe deletion working. onDelete must delete the chosen message once after explicit activation; do not add a confirmation or undo policy. Message has a stable id and subject.

```swift
struct MessageRow: View {
    let message: Message
    let onDelete: (Message) -> Void
    var body: some View {
        Text(message.subject)
            .padding()
            .contentShape(Rectangle())
            .gesture(DragGesture().onEnded { value in
                if value.translation.width < -80 { onDelete(message) }
            })
    }
}
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | An executed unit assertion rejects the dropped-delete variant; same test selection as known-good. Source inspection is not a mutation kill. |
| mutation-2 | unit oracle | fail | An executed unit assertion rejects the duplicate-delete variant; same test selection as known-good. Source inspection is not a mutation kill. |
| explicit-delete | unit | pass | Directly exercise production explicit-delete and swipe-handler paths for two message IDs; each invocation dispatches the chosen ID exactly once. Construction and nonactivation state transitions dispatch nothing. This does not prove input delivery. |
| voiceover-delete | review | pass | Review supplied source against Apple native-control documentation: visible named deletion control and subject content remain present. Do not claim observed VoiceOver interaction. |
| keyboard-delete | review | pass | Review native-control and handler wiring for keyboard-compatible activation without deletion on focus. Actual Full Keyboard Access navigation is outside this endpoint. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.

## GP26-05

### Exact model input

tvOS 26.0, SwiftUI.

Testers cannot reliably reach and select all the movie tiles with the remote. VoiceOver users also need to identify the movie they are opening. Movie is Identifiable with title and posterName; open(movie) opens its detail screen. Please fix the interaction.

```swift
ScrollView(.horizontal) {
    HStack {
        ForEach(movies) { movie in
            VStack {
                Image(movie.posterName)
                Text(movie.title)
            }
            .frame(width: 240, height: 360)
            .onTapGesture { open(movie) }
        }
    }
}
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | An executed unit assertion rejects the dropped-open variant; same test selection as known-good. Source inspection is not a mutation kill. |
| mutation-2 | unit oracle | fail | An executed unit assertion rejects the wrong-movie variant; same test selection as known-good. Source inspection is not a mutation kill. |
| remote-activation | unit | pass | Directly invoke the production activation path for first/middle/last movie IDs and assert one correct callback per invocation. No remote focus or Select delivery claim follows. |
| voiceover-name | review | pass | Review source for meaningful movie titles and native control semantics against documented contracts; no spoken output assertion. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.

## GP26-06

### Exact model input

iOS 26.0, SwiftUI.

Please review the accessibility of this notification settings view and make any changes that are needed. The binding is connected to the existing preference store.

```swift
struct NotificationSettings: View {
    @Binding var notificationsEnabled: Bool
    var body: some View {
        Form {
            Toggle("Notifications", isOn: $notificationsEnabled)
        }
    }
}
```

### Evaluator only

| Gate | Method | Expected | Assertion |
| --- | --- | --- | --- |
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Fixture and required unit-test host build with pinned Apple SDK/build and deployment target; no UI-test target is required. |
| known-good | unit oracle | pass | Reviewed known-good implementation passes the scoped compile/unit assertions. No interaction outcome is implied. |
| mutation-1 | unit oracle | fail | An executed unit assertion rejects the constant-binding variant; same test selection as known-good. Source inspection is not a mutation kill. |
| mutation-2 | unit oracle | fail | An executed unit assertion rejects the inverted-binding variant; same test selection as known-good. Source inspection is not a mutation kill. |
| native-toggle | unit | pass | Exercise the production binding/state path in both directions and assert backing state changes correctly. Source review separately checks native Toggle wiring; unit state checks do not prove VoiceOver activation. |
| scope-control | review | pass | No demonstrated defect is fabricated; valid equivalent implementations are allowed but unnecessary semantic overrides count as review burden, not automatic critical errors. |

Status: evidence pending. Code-contract acceptance is not complete interaction validation.
