# D01 · UILabel accessibility

[← Dashboard](../README.md) · [All cases](../README.md#browse-the-cases)

**Initial smoke · OS context 26 · 8 responses · quality not independently graded**

## Exact user prompt

```text
Tell me about UILabel accessibility.
Deployment context: uikit OS version 26. Clarify platform if needed.
```

## Expected answer criteria

Explain meaningful labels without claiming visual truncation necessarily truncates spoken text.

These are the original scenario rubric, **not a validated gold answer**. They were not appended to the model question. No retrospective gold answer has been invented.

Source for review: [references/uikit/guidelines/u-001-labels-meaningful-names.md](../../../../references/uikit/guidelines/u-001-labels-meaningful-names.md).

Critical-error checks: Invented API or unsupported availability; Hiding required independent actions; Claiming evidence that was not supplied or read.

Display formatting removes trailing spaces only; exact response strings and hashes remain in [dashboard data](../data.json).

## Compare responses

| Variant | Output cap | Finish | Time (s) | Reference contents | Response |
| --- | --- | --- | --- | --- | --- |
| candidate / C0 | 1024 | length | 49.00 | 0 unavailable | [Read ↓](#response-1) |
| candidate / C1 | 1024 | stop | 6.17 | 0 unavailable | [Read ↓](#response-2) |
| candidate / C2 | 1024 | stop | 6.10 | 1 injected | [Read ↓](#response-3) |
| candidate / C3 | 1024 | stop | 4.75 | 0 model-read | [Read ↓](#response-4) |
| baseline / C0 | 1024 | length | 5.96 | 0 unavailable | [Read ↓](#response-5) |
| baseline / C1 | 1024 | stop | 3.95 | 0 unavailable | [Read ↓](#response-6) |
| baseline / C2 | 1024 | length | 6.38 | 1 injected | [Read ↓](#response-7) |
| baseline / C3 | 1024 | length | 6.61 | 0 model-read | [Read ↓](#response-8) |

Times include request processing; first-request warmup effects are not separated here. A normal finish is not a correctness score. C2 reference counts are harness injection, not model tool use.

## Response excerpts

Opening prose excerpts for quick comparison; ellipses mark omitted text. Full original wording is preserved below. These excerpts are not grades.

| Variant | Original response excerpt |
| --- | --- |
| [C0 · candidate · 1024](#response-1) | Clarification: You mentioned "uikit OS version 26." This is likely a confusion between two different Apple frameworks: 1.  UIKit: The framework for building user interfaces (UI). 2.  iOS 16: The operating sys … |
| [C1 · candidate · 1024](#response-2) | Platform: uikit Framework: uikit Task type: Review / Implementation guidance You are asking about the accessibility implications of UILabel within the UIKit framework on iOS 26. Important Clar … |
| [C2 · candidate · 1024](#response-3) | UILabel is a core UIKit component used to display text on a screen. Its accessibility behavior is governed by the U-001: Labels and Meaningful Names guideline, which mandates that every meaningful interactive ele … |
| [C3 · candidate · 1024](#response-4) | To provide guidance on UILabel accessibility, I have selected the uikit platform and the u-001-labels-meaningful-names.md guideline.    Platform: iOS (UIKit)    OS Version: 26 (iOS 17)    Framework:  … |
| [C0 · baseline · 1024](#response-5) | Clarification: You mentioned "uikit OS version 26." This is likely a confusion between two different Apple frameworks: 1.  UIKit: The framework for building user interfaces (UI). 2.  iOS 16: The operating sys … |
| [C1 · baseline · 1024](#response-6) | Platform: uikit Framework: uikit Task Type: Review / Implementation Guidance UILabel is a core UIKit component used to display text. Its accessibility behavior is governed by the Accessibility Inspect … |
| [C2 · baseline · 1024](#response-7) | UILabel is a core UIKit control used to display text on a screen. It is the standard way to present textual information in an iOS application. Accessibility Context:    Platform: iOS (macOS uses UILabel as … |
| [C3 · baseline · 1024](#response-8) | To provide guidance on UILabel accessibility, I have selected the platform and framework as specified in your request: iOS (UIKit) and SwiftUI.    Platform: iOS (UIKit)    Framework: UIKit (SwiftUI) … |

## Response 1

**C0 · candidate · 1,024-token cap** — length; 49.00s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/cb2a45b991efe4c0.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
### Platform Clarification
**Clarification:** You mentioned "uikit OS version 26." This is likely a confusion between two different Apple frameworks:
1.  **UIKit:** The framework for building user interfaces (UI).
2.  **iOS 16:** The operating system version number.

**Assumption:** Based on the phrasing "uikit OS version 26," you are likely asking about **iOS 16** (released in 2023) or perhaps a specific **iOS 16** build context where the UIKit is the primary focus. However, if you are strictly referring to **iOS 16**, the accessibility features for `UILabel` have evolved significantly since iOS 13.

If you meant **iOS 16** specifically, here is the breakdown of `UILabel` accessibility in that context.

---

### Accessibility Overview for `UILabel` (iOS 16 Context)

In iOS 16, `UILabel` is fully integrated into the **Accessibility Framework** (specifically the `UIAccessibility` and `UIAccessibilityManager` APIs). It is no longer just a visual label; it is a semantic component that can be queried, tested, and controlled programmatically.

#### 1. Semantic Roles
`UILabel` can be assigned specific accessibility roles depending on its content and context. In iOS 16, the system provides a more robust set of roles compared to earlier versions.
*   **`UIAccessibilityLabel`**: The primary role for displaying text.
*   **`UIAccessibilityValue`**: Used when the label contains a value (e.g., a price, a score, or a count).
*   **`UIAccessibilityHint`**: Used for visual cues (e.g., "Tap to edit").
*   **`UIAccessibilityLabel` with `UIAccessibilityValue`**: Often used for dynamic content like "Current Balance: $100".

#### 2. `UIAccessibility` API Integration
You can query the accessibility state of a `UILabel` using the `UIAccessibility` framework:

```swift
import UIKit

// Example: Check if the label has a label role
let accessibilityLabel = UILabel()
accessibilityLabel.text = "Hello World"

let accessibilityInfo = UIAccessibility.accessibilityInfo(for: accessibilityLabel)
let role = accessibilityInfo.role

// Check if it is a label role
if role == .label {
    // You can now programmatically change the text or color
    accessibilityLabel.text = "Hello World" // This might trigger a change if the system allows it
}
```

#### 3. `UIAccessibilityManager` for Dynamic Updates
In iOS 16, `UIAccessibilityManager` is the recommended way to manage accessibility properties dynamically. This is crucial for scenarios where the text content changes (e.g., a dynamic progress bar or a list of items).

```swift
import UIKit

let accessibilityManager = UIAccessibilityManager()

// Set the accessibility label
accessibilityManager.setAccessibilityLabel(for: accessibilityLabel, with: "Hello World")

// Set the accessibility value (e.g., for a dynamic list)
accessibilityManager.setAccessibilityValue(for: accessibilityLabel, with: "Item 1")

// Set the accessibility hint
accessibilityManager.setAccessibilityHint(for: accessibilityLabel, with: "Tap to edit")
```

#### 4. Testing and Debugging
*   **Accessibility Inspector:** You can use the built-in **Accessibility Inspector** (accessible via the Accessibility icon in the toolbar) to inspect the role, label, and value of your `UILabel` in real-time.
*   **Automated Testing:** In iOS 16, you can use the `UIAccessibility` framework within XCTest to verify that a `UILabel` renders correctly and that its role is accessible to screen readers.

#### 5. Important Considerations for iOS 16
*   **Dynamic Content:** If your `UILabel` contains dynamic content (e.g., a list of users), ensure you are using `UIAccessibilityManager` to update the `value` property. Simply changing the text string might not trigger a re-render if the system doesn't know the new value.
*   **Color Contrast:** While `UILabel` itself doesn't enforce contrast rules, the system will adjust the text color based on the background to ensure WCAG compliance. If you manually set a color that violates contrast ratios, the system may revert it or warn you during testing.
*   **Keyboard Navigation:** In iOS 16, `UILabel` is fully keyboard navigable. Users can tap the label to focus it, and the system will automatically focus the first child view (if any) or the text itself depending on the role.

### Summary
In **iOS 16**, `UILabel` is a **semantic component** with full accessibility support. It is not just a visual element; it can be queried
````

</details>

Reference evidence: none.

## Response 2

**C1 · candidate · 1,024-token cap** — stop; 6.17s; 1015 output tokens.

[Exact system/user messages and tool schema](../prompts/0ef2dcc1e2786460.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [uikit:u-005-labels.md]

**Swift Accessibility Agent (v0.2.2)**

**Platform:** `uikit`
**Framework:** `uikit`
**Task type:** Review / Implementation guidance

### Analysis
You are asking about the accessibility implications of `UILabel` within the **UIKit** framework on **iOS 26**.

**Important Clarification on OS Version:**
As of my current knowledge cutoff, **iOS 26 does not exist**. The current latest major iOS version is **iOS 17** (released in 2023). iOS 26 is a hypothetical or future version.

However, `UILabel` accessibility guidelines are **stable and consistent** across all supported iOS versions (iOS 14+). The behavior regarding labels, labels with text, and labels with accessibility properties (like `accessibilityLabel`, `accessibilityHint`, `accessibilityValue`) remains the same.

### Accessibility Guidance for `UILabel`

#### 1. Basic Label Behavior
*   **Role:** `UILabel` is a standard text label.
*   **Semantic Role:** It is a `UILabel` with a `UIAccessibilityRole` of `UIAccessibilityLabel`.
*   **Text:** The text content is the primary semantic value.
*   **Accessibility Properties:**
    *   `accessibilityLabel`: Sets the text to read by VoiceOver.
    *   `accessibilityHint`: Sets a hint for VoiceOver (e.g., "This is a button").
    *   `accessibilityValue`: Sets the value for the `accessibilityValue` property (e.g., for a toggle switch).
    *   `accessibilityIdentifier`: Sets a unique identifier for the label.

#### 2. Common Pitfalls & Fixes
*   **Missing `accessibilityLabel` on Text:** If a `UILabel` contains text but lacks an `accessibilityLabel`, VoiceOver will read the text as a regular label (e.g., "Hello World") rather than a button or specific UI element.
    *   *Fix:* Explicitly set `accessibilityLabel` to the desired text.
*   **Confusing `accessibilityValue` vs `accessibilityLabel`:**
    *   `accessibilityLabel` is for the *text* content.
    *   `accessibilityValue` is for the *value* of the control (e.g., the value of a toggle switch).
    *   *Fix:* Use `accessibilityLabel` for the text description and `accessibilityValue` for the control's value.
*   **Mixed Frameworks:** If you are using `UILabel` in a mixed SwiftUI/UIKit/AppKit stack, ensure the `accessibilityLabel` is set on the `UILabel` instance itself, not just the SwiftUI view that hosts it.

#### 3. Implementation Example (UIKit)
```swift
let label = UILabel()
label.text = "This is a button"
label.accessibilityLabel = "This is a button" // Critical for VoiceOver
label.accessibilityValue = "active" // If this is a toggle
label.accessibilityIdentifier = "myButton"
```

### Verification Steps
To verify this implementation works correctly on your target platform (iOS 17+):

1.  **Visual Inspection:** Open the app in Xcode and run it on a device.
2.  **VoiceOver:**
    *   Press `Cmd + Cmd + V` (or `Cmd + Cmd + Space` on some devices) to activate VoiceOver.
    *   Navigate to the `UILabel`.
    *   **Expected Behavior:** VoiceOver should read the text set in `accessibilityLabel` (e.g., "This is a button"), not the raw text content of the label.
3.  **Inspector:**
    *   Open the Accessibility Inspector (Cmd + Option + I).
    *   Navigate to the `UILabel`.
    *   **Expected Findings:**
        *   `Role`: `UIAccessibilityLabel`
        *   `Value`: `UIAccessibilityLabel`
        *   `Text`: "This is a button" (or the value of `accessibilityLabel`)
        *   `Hint`: (If set, should be present)
        *   `Identifier`: `myButton`

### Trust Footer
**Sources:** `references/uikit/guidelines/topic-backlog.md` (iOS 14+ guidelines), `references/uikit/guidelines/topic-backlog.md` (iOS 17+ guidelines)
**Freshness:** `HIGH` (Guidelines are stable across iOS 14+; specific OS version behavior is consistent)
**Assumptions:** `none` (Assumes standard iOS 17+ environment with UIKit)
````

</details>

Reference evidence: none.

## Response 3

**C2 · candidate · 1,024-token cap** — stop; 6.10s; 975 output tokens.

[Exact system/user messages and tool schema](../prompts/717a76a05dcfe728.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [uikit:u-001-labels-meaningful-names.md]

## Swift Accessibility Agent (v0.2.2)

### Overview

**UILabel** is a core UIKit component used to display text on a screen. Its accessibility behavior is governed by the **U-001: Labels and Meaningful Names** guideline, which mandates that every meaningful interactive element must have a clear, unique, and user-centered accessibility label.

In the context of **iOS 26** (a hypothetical future OS version), the implementation of `UILabel` accessibility will follow the same core principles as current iOS versions, with potential enhancements for future OS capabilities (e.g., dynamic type, voice control support, or new semantic APIs).

### Key Accessibility Rules for `UILabel`

1.  **Meaningful Labels**: Every `UILabel` must have a non-empty `accessibilityLabel` property. This label must reflect the user's intent (e.g., "Submit", "Delete", "Price: $10.99") rather than implementation details (e.g., "Button 1", "Label 1").
2.  **Icon-Only Controls**: If a `UILabel` is used as an icon-only control (e.g., a trash icon), it must still have a meaningful label that describes the action (e.g., "Delete", "Remove").
3.  **Semantic Controls**: Prefer using semantic controls (`UIButton`, `UISwitch`, `UITextField`) over generic views with `UILabel` for better accessibility and performance.
4.  **Decorative Elements**: If a `UILabel` is purely decorative (e.g., a background label with no text or no semantic meaning), it should not be focusable or announceable.

### Implementation Guidelines

#### UIKit Implementation

```swift
// Example: A meaningful label for a button
let label = UILabel()
label.text = "Submit"
label.accessibilityLabel = "Submit" // Explicitly set the label
label.accessibilityHint = "Submit the form" // Optional hint for context
label.accessibilityTraits = [.active, .button] // Optional traits for focus states

// Example: An icon-only label
let iconLabel = UILabel()
iconLabel.text = "✕"
iconLabel.accessibilityLabel = "Delete" // Clear semantic meaning
iconLabel.accessibilityTraits = [.button, .icon]
```

#### SwiftUI Interop Notes

When mixing SwiftUI and UIKit, ensure that the SwiftUI view's accessibility properties are correctly propagated to the underlying UIKit `UILabel` or `UIButton` if used for text display.

```swift
// SwiftUI View
struct MyView: View {
    var body: some View {
        Button("Submit") {
            // Ensure the button has a meaningful label
            Button("Submit") {
                // ...
            }
            .accessibilityLabel("Submit") // SwiftUI button label
        }
        .accessibilityLabel("Submit") // SwiftUI button label
    }
}
```

### Testing and Verification

To verify the accessibility of `UILabel` implementations:

1.  **Accessibility Inspector**:
    *   Navigate to the **Accessibility Inspector** in Xcode.
    *   Check that the `accessibilityLabel` property is set for all meaningful controls.
    *   Verify that the label text is unique and does not duplicate other controls.

2.  **VoiceOver Walkthrough**:
    *   Open the app in a simulator or device.
    *   Use **VoiceOver** to navigate the screen.
    *   Confirm that each meaningful control is announced with a clear, descriptive name.
    *   Test icon-only controls to ensure they announce user intent (e.g., "Delete", "Remove").

3.  **Optional XCUITest Hook**:
    *   Use XCUITest to verify the existence of critical controls and their accessibility properties programmatically.

### Citations

- [APPLE-AX-HUB] https://developer.apple.com/documentation/accessibility
- [APPLE-HIG-ACCESSIBILITY] https://developer.apple.com/design/human-interface-guidelines/accessibility
- [APPLE-WWDC23-SWIFTUI-UIKIT] https://developer.apple.com/videos/play/wwdc2023/10036/

### Trust Footer

**Sources:** `references/uikit/guidelines/u-001-labels-meaningful-names.md`
**Freshness:** `HIGH` (Guideline is current and supported by Apple documentation)
**Assumptions:** `none` (Assumes standard iOS 26 environment with UIKit and SwiftUI interop)
````

</details>

Reference evidence: references/uikit/guidelines/u-001-labels-meaningful-names.md.

## Response 4

**C3 · candidate · 1,024-token cap** — stop; 4.75s; 694 output tokens.

[Exact system/user messages and tool schema](../prompts/903d54d036521c4f.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

```text
ROUTING: [uikit:u-001-labels-meaningful-names.md]

**Swift Accessibility Agent (v0.2.2)**

To provide guidance on `UILabel` accessibility, I have selected the `uikit` platform and the `u-001-labels-meaningful-names.md` guideline.

### Platform & Framework Context
*   **Platform:** iOS (UIKit)
*   **OS Version:** 26 (iOS 17)
*   **Framework:** UIKit (SwiftUI is not applicable here as `UILabel` is a UIKit class)

### Guideline Findings
The `u-001-labels-meaningful-names.md` guideline establishes that `UILabel` must have a **label** (text content) and a **value** (accessibility text) to be considered accessible.

#### Key Requirements for `UILabel`
1.  **Label (Text Content):** The visible text displayed on the screen.
2.  **Value (Accessibility Text):** The text used by the system for screen readers (e.g., VoiceOver).
    *   **Default Behavior:** On iOS 17+, `UILabel` defaults to using the `text` property as the accessibility value.
    *   **Customization:** You can override this by setting the `accessibilityValue` property.
    *   **Fallback:** If `accessibilityValue` is not set, the system may fall back to the `text` property or the `accessibilityLabel` property (if available).

#### Implementation Considerations
*   **SwiftUI Interop:** If you are using SwiftUI, you must explicitly set the `accessibilityValue` property on the `UILabel` view model or the `Text` view to ensure the correct text is read.
*   **Semantic Equivalence:** Ensure the accessibility value is semantically equivalent to the label text. For example, if the label says "Submit", the accessibility value should ideally be "Submit" or "Button" depending on the specific accessibility role.
*   **Dynamic Type:** Ensure the accessibility value is not truncated or modified by Dynamic Type settings (e.g., font size, color) unless explicitly intended.

#### Verification Steps
1.  **Inspector Audit:** Use the Accessibility Inspector to verify that the `accessibilityValue` property matches the intended text.
2.  **Manual Flow:** Perform a VoiceOver or TalkBack test to confirm the screen reader reads the correct text.
3.  **Dynamic Type Check:** Verify that the accessibility value is not affected by Dynamic Type font size or color changes.

### Sources
*   `references/uikit/guidelines/u-001-labels-meaningful-names.md`
*   `references/uikit/README.md`

**Freshness:** `HIGH`

**Assumptions:**
*   The user is using iOS 17 (OS 26) or later.
*   The user is using UIKit or SwiftUI with explicit accessibility configuration.

---
**Note:** This answer relies on the `uikit` platform and the `u-001-labels-meaningful-names.md` guideline. If you are using SwiftUI, please note that SwiftUI does not support `UILabel` directly; you must use `Text` with `accessibilityValue` set.
```

</details>

Reference evidence: none.

## Response 5

**C0 · baseline · 1,024-token cap** — length; 5.96s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/cb2a45b991efe4c0.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
### Platform Clarification
**Clarification:** You mentioned "uikit OS version 26." This is likely a confusion between two different Apple frameworks:
1.  **UIKit:** The framework for building user interfaces (UI).
2.  **iOS 16:** The operating system version number.

**Assumption:** Based on the phrasing "uikit OS version 26," you are likely asking about **iOS 16** (released in 2023) or perhaps a specific **iOS 16** build context where the UIKit is the primary focus. However, if you are strictly referring to **iOS 16**, the accessibility features for `UILabel` have evolved significantly since iOS 13.

If you meant **iOS 16** specifically, here is the breakdown of `UILabel` accessibility in that context.

---

### Accessibility Overview for `UILabel` (iOS 16 Context)

In iOS 16, `UILabel` is fully integrated into the **Accessibility Framework** (specifically the `UIAccessibility` and `UIAccessibilityManager` APIs). It is no longer just a visual label; it is a semantic component that can be queried, tested, and controlled programmatically.

#### 1. Semantic Roles
`UILabel` can be assigned specific accessibility roles depending on its content and context. In iOS 16, the system provides a more robust set of roles compared to earlier versions.
*   **`UIAccessibilityLabel`**: The primary role for displaying text.
*   **`UIAccessibilityValue`**: Used when the label contains a value (e.g., a price, a score, or a count).
*   **`UIAccessibilityHint`**: Used for visual cues (e.g., "Tap to edit").
*   **`UIAccessibilityLabel` with `UIAccessibilityValue`**: Often used for dynamic content like "Current Balance: $100".

#### 2. `UIAccessibility` API Integration
You can query the accessibility state of a `UILabel` using the `UIAccessibility` framework:

```swift
import UIKit

// Example: Check if the label has a label role
let accessibilityLabel = UILabel()
accessibilityLabel.text = "Hello World"

let accessibilityInfo = UIAccessibility.accessibilityInfo(for: accessibilityLabel)
let role = accessibilityInfo.role

// Check if it is a label role
if role == .label {
    // You can now programmatically change the text or color
    accessibilityLabel.text = "Hello World" // This might trigger a change if the system allows it
}
```

#### 3. `UIAccessibilityManager` for Dynamic Updates
In iOS 16, `UIAccessibilityManager` is the recommended way to manage accessibility properties dynamically. This is crucial for scenarios where the text content changes (e.g., a dynamic progress bar or a list of items).

```swift
import UIKit

let accessibilityManager = UIAccessibilityManager()

// Set the accessibility label
accessibilityManager.setAccessibilityLabel(for: accessibilityLabel, with: "Hello World")

// Set the accessibility value (e.g., for a dynamic list)
accessibilityManager.setAccessibilityValue(for: accessibilityLabel, with: "Item 1")

// Set the accessibility hint
accessibilityManager.setAccessibilityHint(for: accessibilityLabel, with: "Tap to edit")
```

#### 4. Testing and Debugging
*   **Accessibility Inspector:** You can use the built-in **Accessibility Inspector** (accessible via the Accessibility icon in the toolbar) to inspect the role, label, and value of your `UILabel` in real-time.
*   **Automated Testing:** In iOS 16, you can use the `UIAccessibility` framework within XCTest to verify that a `UILabel` renders correctly and that its role is accessible to screen readers.

#### 5. Important Considerations for iOS 16
*   **Dynamic Content:** If your `UILabel` contains dynamic content (e.g., a list of users), ensure you are using `UIAccessibilityManager` to update the `value` property. Simply changing the text string might not trigger a re-render if the system doesn't know the new value.
*   **Color Contrast:** While `UILabel` itself doesn't enforce contrast rules, the system will adjust the text color based on the background to ensure WCAG compliance. If you manually set a color that violates contrast ratios, the system may revert it or warn you during testing.
*   **Keyboard Navigation:** In iOS 16, `UILabel` is fully keyboard navigable. Users can tap the label to focus it, and the system will automatically focus the first child view (if any) or the text itself depending on the role.

### Summary
In **iOS 16**, `UILabel` is a **semantic component** with full accessibility support. It is not just a visual element; it can be queried
````

</details>

Reference evidence: none.

## Response 6

**C1 · baseline · 1,024-token cap** — stop; 3.95s; 614 output tokens.

[Exact system/user messages and tool schema](../prompts/84900557eaaf5783.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

```text
ROUTING: [uikit:u-005-labels.md]

**Swift Accessibility Agent (v0.2.2)**

**Platform:** `uikit`
**Framework:** `uikit`
**Task Type:** Review / Implementation Guidance

### Overview
`UILabel` is a core UIKit component used to display text. Its accessibility behavior is governed by the **Accessibility Inspector** and the **Accessibility Guidelines**.

### Key Accessibility Behaviors
1.  **Default State:** By default, `UILabel` is **not** an accessible UI element. It does not have a `role`, `label`, or `value` set.
2.  **Interaction:** It is **not** focusable by default. Users cannot tap it to navigate or interact with the app.
3.  **Semantic Role:** To make it accessible, it must be assigned a semantic role (e.g., `label`, `button`, `text`) and a value (the text content).
4.  **Focus Management:** If the label is part of a group or container, focus must be managed correctly (e.g., using `accessibilityElements` or `accessibilityTraits`).

### Implementation Guidelines
To ensure `UILabel` is accessible:
*   **Assign Role:** Use `accessibilityLabel` (or `accessibilityValue` in older contexts) to set the text.
*   **Assign Value:** Use `accessibilityValue` to set the text content.
*   **Traits:** Consider using `accessibilityTraits` (e.g., `accessibilityTraits` with `accessibilityLabel` or `accessibilityValue`) to ensure the label is recognized as a text element.
*   **Grouping:** If the label is inside a group, ensure the group has the correct `accessibilityElements` to contain the label.

### Verification Steps
1.  **Inspector Audit:** Open the Accessibility Inspector in Xcode.
    *   Check if the `UILabel` has a `role` set.
    *   Check if the `label` and `value` properties are populated.
    *   Check if the `accessibilityTraits` include `accessibilityLabel` or `accessibilityValue`.
2.  **Manual Flow:**
    *   Navigate to the app.
    *   Tap the `UILabel`.
    *   Verify that the text is visible and that the label is part of the navigation flow (e.g., tapping it moves focus to the next element or the app exits).

### Trust Footer
**Sources:** `references/uikit/guidelines/topic-backlog.md`, `references/uikit/guidelines/labels.md`
**Freshness:** `HIGH`
**Assumptions:** `none`

---
*Note: This guidance assumes standard UIKit usage. If you are using SwiftUI, the implementation differs significantly (using `Text` with `accessibilityLabel` and `accessibilityValue` properties).*
```

</details>

Reference evidence: none.

## Response 7

**C2 · baseline · 1,024-token cap** — length; 6.38s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/cf0aca43717faaf5.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

```text
ROUTING: [uikit:u-001-labels-meaningful-names.md]

## Swift Accessibility Agent (v0.2.2)

### Overview

**UILabel** is a core UIKit control used to display text on a screen. It is the standard way to present textual information in an iOS application.

**Accessibility Context:**
*   **Platform:** iOS (macOS uses `UILabel` as well, but the context here is iOS).
*   **Framework:** UIKit
*   **OS Version:** 26 (iOS 16)
*   **Primary Role:** Semantic labeling for VoiceOver and VoiceOver TalkBack.

### Core Accessibility Concepts

#### 1. The `accessibilityLabel` Property
This is the most critical property for accessibility.
*   **Function:** It provides the text that VoiceOver reads aloud.
*   **Requirement:** It must be **non-empty** for the control to be announced.
*   **Behavior:**
    *   If the text is empty, VoiceOver will not announce the control at all.
    *   If the text is empty, the control is often treated as "non-interactive" or "non-accessible" in strict audits.
    *   **Important:** Do not rely on the text content of the label itself for accessibility purposes (e.g., do not use `label.text` as the accessibility label). Instead, use a separate `accessibilityLabel` property or a `Text` view with a specific `accessibilityLabel`.

#### 2. `accessibilityHint`
*   **Function:** Provides additional context that VoiceOver reads *after* the main label.
*   **Use Case:** Useful for clarifying the purpose of the label, especially when the label text is long or ambiguous.
*   **Example:**
    *   Label: "Delete message"
    *   Hint: "Press to delete"

#### 3. `accessibilityValue`
*   **Function:** Provides the value associated with the control.
*   **Use Case:** Often used for numeric inputs, sliders, or custom controls where the text is not the primary identifier.

#### 4. `accessibilityTraits`
*   **Function:** Defines how the control behaves for assistive technologies.
*   **Common Values:**
    *   `UITraitContentEditable`: Allows the user to edit the text (e.g., in a `UITextField`).
    *   `UITraitScrollable`: Allows the control to scroll when the text is too long.
    *   `UITraitHidden`: Hides the control from the screen but keeps it accessible (e.g., for a button that is visually hidden but functional).

### Implementation Guidelines for iOS 16

When implementing or reviewing a `UILabel` in iOS 16:

1.  **Ensure Non-Empty Label:**
    *   If the label is intended to be announced, ensure `label.text` is not empty.
    *   If the label is decorative (e.g., a button icon), ensure `label.text` is empty and `accessibilityLabel` is set to `nil` or a non-announced value.

2.  **Semantic Control Selection:**
    *   Prefer using `UIButton` or `UISwitch` over `UILabel` for icon-only controls.
    *   Use `UILabel` primarily for text content.

3.  **Mixed Frameworks (SwiftUI):**
    *   If using SwiftUI, ensure the `UIHostingController` or `UIHostingView` does not override the accessibility behavior of the underlying UIKit `UILabel`.
    *   Ensure the SwiftUI view has an explicit `accessibilityLabel` property set to the text you want VoiceOver to read.

### Testing & Verification

To verify accessibility for a `UILabel` in iOS 16:

1.  **Accessibility Inspector:**
    *   Open the Inspector in Xcode.
    *   Navigate to the `Accessibility` tab.
    *   Check the `Label` property. It should contain the expected text.
    *   Check the `Traits` property to ensure it matches the intended behavior (e.g., `UITraitContentEditable` for a text field).

2.  **VoiceOver Walkthrough:**
    *   Open VoiceOver.
    *   Navigate to the screen containing the `UILabel`.
    *   Verify that the control is announced with the correct text.
    *   Verify that the control is focusable and responds to keyboard interactions.

3.  **XCUITest (Optional):**
    *   Use XCUITest to programmatically verify the text content of the label and its accessibility properties.

### Citations

*   [APPLE-AX-HUB] https://developer.apple.com/documentation/accessibility
*   [APPLE-HIG-ACCESS
```

</details>

Reference evidence: references/uikit/guidelines/u-001-labels-meaningful-names.md.

## Response 8

**C3 · baseline · 1,024-token cap** — length; 6.61s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/b4dae95bdfbc5128.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [uikit:u-001-labels-meaningful-names.md]

**Swift Accessibility Agent (v0.2.2)**

To provide guidance on `UILabel` accessibility, I have selected the platform and framework as specified in your request: **iOS (UIKit)** and **SwiftUI**.

### Platform & Framework
*   **Platform:** iOS (UIKit)
*   **Framework:** `UIKit` (SwiftUI)
*   **OS Version:** 26 (iOS 16)

### Core Accessibility Guidance for `UILabel`

`UILabel` is a fundamental control for displaying text. Its accessibility behavior is governed by the following principles:

1.  **Semantic Role:** By default, `UILabel` has the `UITextLabel` role. This role is the correct semantic choice for displaying text content.
2.  **Label vs. Text:**
    *   **Label:** The container for the text. It has a `label` property (or `text` in SwiftUI). It is the primary semantic element.
    *   **Text:** The actual content. In SwiftUI, `text` is the property. In UIKit, `text` is the property.
    *   **Rule:** Do not use `UILabel` for the text content itself. Use `UILabel` for the container and `UILabel` (or `UILabel` in SwiftUI) for the text.
3.  **Accessibility Properties:**
    *   **`label` (UIKit):** The text content.
    *   **`text` (SwiftUI):** The text content.
    *   **`hint` (UIKit):** Optional text that appears below the label when the label is not visible (e.g., in a scrollable list).
    *   **`value` (UIKit):** The value of a `UISwitch` or `UISlider` control.
    *   **`role` (UIKit):** The semantic role of the control. For `UILabel`, the role is `UITextLabel`.
4.  **Focus Management:**
    *   `UILabel` is a standard text control. It does not inherently manage focus.
    *   **Action:** If you need to manage focus (e.g., moving focus to the label when the user taps a button), you must explicitly add an `accessibilityAction` to the label or the button.
    *   **Default Behavior:** If the label is not visible, the focus may not be on the label. This is a common accessibility issue.
5.  **Dynamic Type:**
    *   `UILabel` supports Dynamic Type (System Text Size).
    *   **Requirement:** Ensure the font size is set to a value that is accessible (e.g., `16pt` or larger) and that the text is not truncated.
    *   **Hint:** Use `accessibilityHint` to provide a hint about the text size or font family if the default size is not appropriate.
6.  **Contrast:**
    *   Ensure the text color has sufficient contrast against the background color.
    *   **Rule:** Do not use `UILabel` with a background color that is too light or transparent.
7.  **Grouping:**
    *   `UILabel` is a single-line control.
    *   **Rule:** Do not group multiple `UILabel` controls together. If you need to group multiple controls, use a container view (e.g., `UILabel` with `text` property set to a container view, or a `UITabView` with `UILabel` children).

### Implementation Example (SwiftUI)

```swift
// Correct: Label for container, Label for text
struct MyView: View {
    var body: some View {
        VStack {
            // Label for the container
            let label = UILabel()
            label.text = "Hello"
            label.accessibilityLabel = "Hello"
            label.accessibilityHint = "This is a hint"

            // Text for the content
            let text = UILabel()
            text.text = "Hello"

            // Optional: Add a hint for the hint
            let hint = UILabel()
            hint.text = "This is a hint"
            hint.accessibilityHint = "This is a hint"

            label
                .accessibilityLabel("Hello")
                .accessibilityHint("This is a hint")
                .accessibilityTraits(.accessibilityLabel)

            text
                .accessibilityLabel("Hello")
                .accessibilityTraits(.accessibilityLabel)

            hint
                .accessibilityLabel("This is a hint")
                .accessibilityTraits(.accessibilityHint)
        }
        .accessibilityLabel("My App")
    }
}
```

### Verification Steps

1.  **Inspector Audit:**

````

</details>

Reference evidence: none.
