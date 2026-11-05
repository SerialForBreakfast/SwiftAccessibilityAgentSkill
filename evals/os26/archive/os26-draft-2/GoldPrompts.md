# Gold prompts — OS 26 first

**Draft revision2 · 6 registered development cases · 0 validated gold fixtures · no new inference.**

**Current historical pilot:** Gemini3.8Flash-low / skill0.2.2 · W/T/L **1/4/1** (6 pairs) · C2 tokens **1.89×** · suspected API errors **1** · compile/device **not run**. Single-reviewer static results, not scores for the revised prompts below.

[How drafts become runnable](evals/os26/README.md) · [Methodology decisions and corrections](evals/METHODOLOGY-DECISIONS-2026-11-05.md) · [Historical pilot](evals/evidence/pilots/bigdog/developer-code-20261105/README.md)

## Prompts at a glance

| ID | Actual request (code below) | Cohort | Status |
|---|---|---|---|
| [GP26-01](#gp26-01) | VoiceOver only stops on “Downloads” in this settings row. People cannot change the setting or open Help. The existing callbacks are already wired. Can you fix it? | representative | Oracle evidence pending |
| [GP26-02](#gp26-02) | After scrolling and refreshing orders, a cell sometimes announces the previous customer or status. Here is its configuration code; the model has customer/status strings and an isPriority flag, and titleLabel is already laid out. What should change? | representative | Oracle evidence pending |
| [GP26-03](#gp26-03) | Customers using larger text cannot read the complete checkout total. The container fills the safe-area width, and formattedTotal can be a long localized currency value. The Pay button already works and its appearance should stay the same. Can you fix this layout? | representative | Oracle evidence pending |
| [GP26-04](#gp26-04) | Our message row can only delete by swiping. Add an on-screen way to delete that works with VoiceOver and with Full Keyboard Access plus a hardware keyboard. Keep swipe deletion working. onDelete must delete the chosen message once after explicit activation; do not add a confirmation or undo policy. Message has a stable id and subject. | regression | Oracle evidence pending |
| [GP26-05](#gp26-05) | Testers cannot reliably reach and select all the movie tiles with the remote. VoiceOver users also need to identify the movie they are opening. Movie is Identifiable with title and posterName; open(movie) opens its detail screen. Please fix the interaction. | representative | Oracle evidence pending |
| [GP26-06](#gp26-06) | Please review the accessibility of this notification settings view and make any changes that are needed. The binding is connected to the existing preference store. | Correct-code control | Oracle evidence pending |

The authoritative model inputs are in [prompts.json](evals/os26/prompts.json); evaluator assertions are separate in [acceptance.json](evals/os26/acceptance.json). Never send this entire catalog to a model. These revised synthetic cases are not fresh heldout data. GP26-04 is a known regression. No previous output can be regraded as an answer to these changed prompts.

Promotion requires a compiled fixture, independently reviewed sources/criteria, a known-good patch, two rejected error mutations, and evidence for each required interaction. Native tests are pending. The offline gate verifies evidence completeness/hashes; it does not execute tests or prove supplied reports true.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Hide interactive descendants |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Drop Help callback |
| switch-state | manual | pass | VoiceOver reaches Downloads switch, announces its current state, and activation changes only that setting. |
| help-action | manual | pass | VoiceOver reaches Help separately and activation invokes its existing callback once without toggling Downloads. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Skip normal-order label reset |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Leave status from previous order |
| reconfiguration | unit | pass | Configure priority Alice/shipped, then nonpriority Bob/processing on the SAME instance without prepareForReuse: label names Bob without stale priority and value reports processing; reverse ordering also works. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Keep fixed container height |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Disable live text scaling |
| live-resize | manual | pass | At 320pt and 375pt safe-area widths, change from default to largest accessibility text size while screen stays open: full long currency amount remains readable and Pay visible/operable without overlap. |
| payment-action | unit | pass | Existing payment handler is preserved and invoked exactly once per explicit activation; unrelated button appearance is preserved. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Delete on focus |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Remove ordinary keyboard affordance |
| explicit-delete | unit | pass | Each supported explicit activation deletes the selected ID once; focus/navigation causes zero deletions; original swipe still dispatches one deletion. |
| voiceover-delete | manual | pass | VoiceOver user can discover and activate deletion and still read the subject. |
| keyboard-delete | manual | pass | With Full Keyboard Access enabled, hardware-keyboard focus can reach the visible deletion affordance and activate it; navigation alone never deletes. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Remove activation handler |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Reset focus on every update |
| remote-activation | manual | pass | On the tvOS26 fixture shelf, navigate to first/middle/last tiles and activate each using Select: correct movie callback once, no forced reset or trap. |
| voiceover-name | manual | pass | VoiceOver identifies each movie by meaningful title; separately record remote focus results rather than treating VoiceOver order as remote navigation proof. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

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

### Evaluator only — not sent to model

| Gate | Method | Expected result | Assertion |
|---|---|---|---|
| source-review | review | pass | Independent reviewer confirms primary-source sections, API availability and accepted alternatives for the stated26target; fixture author is not sole reviewer. |
| compile-host | compile | pass | Complete fixture host builds with pinned Apple SDK/build and deployment target. |
| known-good | oracle | pass | Reviewed known-good patch passes required atomic checks in the fixture host. |
| mutation-1 | oracle | fail | The oracle rejects this single-error mutation: Break bound state update |
| mutation-2 | oracle | fail | The oracle rejects this single-error mutation: Hide the toggle from accessibility |
| native-toggle | manual | pass | VoiceOver exposes Notifications purpose/current state, explicit activation updates binding once, and no required behavior is lost. |
| scope-control | review | pass | No demonstrated defect is fabricated; valid equivalent implementations are allowed but unnecessary semantic overrides count as review burden, not automatic critical errors. |

Status: all evidence pending. A rejected mutation is an expected fail, not a failing good implementation.

## Coverage before baseline freeze

Retain representative tasks and correct-code controls. Add independently reviewed interop ownership, asynchronous updates/errors, modal focus and adjustable-control families before treating this as broad coverage. Headroom-screened failures form a separately reported stratum; do not remove every baseline success. OS27-specific tests follow OS26 adoption.

## Simple performance line

`Model / skill / corpus | W/T/L x/y/z of N | accepted fixes x/N or unknown | critical confirmed/suspected x/y | tokens vs baseline x.xx× | compile x/N; device x/N or not_run`

W/T/L uses paired frozen criteria and reports reviewer status. Accepted fixes require all applicable checks; unknown/unrun cannot be passes. Token ratio uses the same completed paired subset and client-reported input+output; report excluded failures/missing telemetry separately. Correction time is unknown unless measured. Suspected defects are not compiler-confirmed failures. These six-case judgments are not a population accuracy estimate.

## Offline readiness

```sh
node evals/runner/os26.mjs status
node evals/runner/os26.mjs plan /path/to/private-evidence.json
```

The second command refuses a runnable plan until required evidence is present. Even a successful plan grants no model execution. Further subscription runs require a separately approved bounded batch.
