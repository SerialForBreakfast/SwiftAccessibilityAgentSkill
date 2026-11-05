# D31 · Centering a view

[← Dashboard](../README.md) · [All cases](../README.md#browse-the-cases)

**Initial smoke · OS context 27 · 8 responses · quality not independently graded**

## Exact user prompt

```text
How do I center a SwiftUI view?
```

## Expected answer criteria

Answer the layout question without unnecessary accessibility routing.

These are the original scenario rubric, **not a validated gold answer**. They were not appended to the model question. No retrospective gold answer has been invented.

Critical-error checks: Invented API or unsupported availability; Hiding required independent actions; Claiming evidence that was not supplied or read.

Display formatting removes trailing spaces only; exact response strings and hashes remain in [dashboard data](../data.json).

## Compare responses

| Variant | Output cap | Finish | Time (s) | Reference contents | Response |
| --- | --- | --- | --- | --- | --- |
| candidate / C0 | 1024 | stop | 4.35 | 0 unavailable | [Read ↓](#response-1) |
| candidate / C1 | 1024 | length | 6.31 | 0 unavailable | [Read ↓](#response-2) |
| candidate / C2 | 1024 | stop | 4.54 | 0 injected | [Read ↓](#response-3) |
| candidate / C3 | 1024 | length | 6.67 | 0 model-read | [Read ↓](#response-4) |
| baseline / C0 | 1024 | stop | 4.40 | 0 unavailable | [Read ↓](#response-5) |
| baseline / C1 | 1024 | stop | 3.87 | 0 unavailable | [Read ↓](#response-6) |
| baseline / C2 | 1024 | length | 6.23 | 0 injected | [Read ↓](#response-7) |
| baseline / C3 | 1024 | stop | 3.89 | 0 model-read | [Read ↓](#response-8) |

Times include request processing; first-request warmup effects are not separated here. A normal finish is not a correctness score. C2 reference counts are harness injection, not model tool use.

## Response excerpts

Opening prose excerpts for quick comparison; ellipses mark omitted text. Full original wording is preserved below. These excerpts are not grades.

| Variant | Original response excerpt |
| --- | --- |
| [C0 · candidate · 1024](#response-1) | To center a SwiftUI view, you can use the View modifier's center() method, which is the modern, recommended approach. Alternatively, you can use the older CenteredView modifier or manually calculate the center posi … |
| [C1 · candidate · 1024](#response-2) | 1. Identify the changed UI surface and platform/framework. The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e … |
| [C2 · candidate · 1024](#response-3) | 1. Identify the changed UI surface and platform/framework. The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e … |
| [C3 · candidate · 1024](#response-4) | To center a SwiftUI view, you typically use the CenteredView modifier or the View modifier with frame: .init(width: height:) and offset: .init(x: y:) to position it within its container. The most straightforward  … |
| [C0 · baseline · 1024](#response-5) | To center a SwiftUI view, you can use the View modifier's center() method, which is the modern, recommended approach. Alternatively, you can use the older CenteredView modifier or manually calculate the center posi … |
| [C1 · baseline · 1024](#response-6) | 1. Identify the changed UI surface and platform/framework. - Platform: iOS (SwiftUI) - Framework: SwiftUI - Task Type: Implementation / Review 2. Load one backlog file for that surface. - references/ … |
| [C2 · baseline · 1024](#response-7) | 1. Identify the changed UI surface and platform/framework. - Platform: iOS (SwiftUI) - Framework: SwiftUI - Task: Centering a view 2. Load one backlog file for that surface. - references/swiftui/guid … |
| [C3 · baseline · 1024](#response-8) | To center a SwiftUI view, you typically use the CenteredView or CenteredStack from the SwiftUI framework. These views are designed to center their content within a given container, ensuring the content is always ce … |

## Response 1

**C0 · candidate · 1,024-token cap** — stop; 4.35s; 754 output tokens.

[Exact system/user messages and tool schema](../prompts/84d2e213681979d2.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
To center a SwiftUI view, you can use the `View` modifier's `center()` method, which is the modern, recommended approach. Alternatively, you can use the older `CenteredView` modifier or manually calculate the center position using `offsetBy`.

Here are the three most common methods:

### 1. Using the Modern `center()` Modifier (Recommended)
This is the cleanest and most idiomatic way in SwiftUI. It automatically handles the view's layout and ensures the content is centered within its container.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        VStack {
            Text("Hello")
                .center() // Centers the view vertically and horizontally
                .padding()

            Text("World")
                .center()
                .padding()
        }
        .padding()
    }
}
```

### 2. Using the `CenteredView` Modifier
If you prefer a dedicated modifier for centering, `CenteredView` is a great option. It is particularly useful when you want to center a view within a specific container (like a `ZStack` or `HStack`).

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        ZStack {
            VStack {
                Text("Hello")
                    .center()
                    .padding()

                Text("World")
                    .center()
                    .padding()
            }
            .padding()
        }
        .centered() // Centers the entire ZStack
    }
}
```

### 3. Manual Calculation (Using `offsetBy`)
If you need to center a view relative to a specific coordinate (e.g., centering a `HStack` on the screen center), you can manually calculate the offset.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        HStack {
            Text("Hello")
                .offsetBy(x: 0, y: 0)

            Text("World")
                .offsetBy(x: 0, y: 0)
        }
        .offsetBy(x: -widthOfView / 2, y: -heightOfView / 2)
    }
}
```

### Important Note on `center()`
The `center()` modifier works on the **current view's** layout. If you are centering a view inside another view (like a `ZStack`), you must apply the `center()` modifier to the **inner view**, not the outer one.

**Example of a common mistake:**
```swift
// ❌ Incorrect: This centers the ZStack, not the inner VStack
ZStack {
    VStack {
        Text("Hello")
            .center() // Centers the VStack, not the ZStack
            .padding()
    }
    .padding()
}
```

**Correct approach:**
```swift
// ✅ Correct: This centers the inner VStack within the ZStack
ZStack {
    VStack {
        Text("Hello")
            .center() // Centers the VStack
            .padding()
    }
    .padding()
}
```

### Summary
For most cases, simply adding `.center()` to your view modifier is sufficient. It automatically handles the necessary layout calculations.
````

</details>

Reference evidence: none.

## Response 2

**C1 · candidate · 1,024-token cap** — length; 6.31s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/2a3568bef7d7808f.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

```text
ROUTING: [swiftui:g-015-media-captions-audio-descriptions.md]

## Swift Accessibility Agent (v0.2.2)

### Review Existing Accessibility Implementation

**1. Identify the changed UI surface and platform/framework.**
The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e.g., using `frame:`, `padding`, or `Alignment` modifiers). It does not inherently impact accessibility semantics, VoiceOver, or focus management unless the view itself is an interactive control or the layout causes issues with dynamic type or focus trapping.

**2. Load a backlog only when needed to locate the relevant topic.**
The user is asking for a layout implementation question, not an accessibility review. The relevant topic backlog for layout is `swiftui/guidelines/topic-backlog.md`. However, since the query is purely about layout, we do not need to load the accessibility-specific topic backlogs.

**3. Load one or two matching guideline files.**
Since the query is about layout, we do not need to load the accessibility-specific topic backlogs.

**4. Output findings with guideline IDs, citation IDs, and verification steps.**
There are no accessibility findings to report. The answer will focus on the layout implementation.

### Improve Existing UI Accessibility

**1. Load the matching guideline file(s); use the backlog only for discovery.**
The user is asking about layout, not accessibility. We do not need to load the accessibility-specific topic backlogs.

**2. Propose concrete semantic fixes (label/value/hint/role/actions).**
There are no semantic fixes needed for layout.

**3. Include rationale tied to Tier-1 citations.**
There are no accessibility citations to include.

**4. Provide verification plan (Inspector + manual flow; optional XCUITest hook).**
There is no accessibility verification plan.

### Implement New Accessible UI

**1. Select guideline topics before implementation.**
The user is asking about layout, not accessibility. We do not need to select accessibility topics.

**2. Prefer native controls and explicit semantics.**
There are no accessibility semantics to implement.

**3. Include interop ownership notes for mixed stacks.**
There are no mixed framework interop notes.

**4. Return implementation plus verification expectations.**
The implementation will focus on layout.

### Internal Routing (As Needed)

**1. `references/manifests/security-policy.json`**
**2. `references/manifests/axes.json`**
**3. `references/manifests/core.json`**
**4. `references/manifests/routes.json`**

**5. `references/swiftui/guidelines/topic-backlog.md`**
**6. `references/uikit/guidelines/topic-backlog.md`**
**7. `references/tvos/guidelines/topic-backlog.md`**
**8. `references/macos/guidelines/topic-backlog.md`**
**9. `references/visionos/guidelines/topic-backlog.md`**

**10. `references/testing/inspector-audit-checklist.md`**
**11. `references/testing/manual-test-scripts.md`**
**12. `references/testing/xcuitest-hooks.md`**

**13. `references/core/sources/registry.md`**
**14. `references/core/taxonomy/semantics-checklist.md`**
**15. `references/core/templates/guideline-template.md`**

**16. `references/manifests/axes.json`**
**17. `references/manifests/core.json`**
**18. `references/manifests/routes.json`**

**19. `references/manifests/security-policy.json`**

**20. `references/manifests/axes.json`**
**21. `references/manifests/core.json`**
**22. `references/manifests/routes.json`**

**23. `references/manifests/axes.json`**
**24. `references/manifests/core.json`**
**25. `references/manifests/routes.json`**

**26. `references/manifests/axes.json`**
**27. `references/manifests/core.json`**
**28. `references/manifests/routes.json`**

**29. `references/manifests/axes.json`**
**30. `references/manifests/core.json`**
**31. `references/manifests/routes.json`**

**32. `references/manifests/axes.json`**
**33. `references/manifests/core.json`**
**34. `references/manifests/routes.json`**

**3
```

</details>

Reference evidence: none.

## Response 3

**C2 · candidate · 1,024-token cap** — stop; 4.54s; 722 output tokens.

[Exact system/user messages and tool schema](../prompts/625736bb7a2fdbde.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:g-015-media-captions-audio-descriptions.md]

## Swift Accessibility Agent (v0.2.2)

### Review Existing Accessibility Implementation

**1. Identify the changed UI surface and platform/framework.**
The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e.g., using `frame:`, `padding`, or `centered` modifiers) that does not inherently impact accessibility semantics, roles, or interaction models.

**2. Load a backlog only when needed to locate the relevant topic.**
The user is not asking about VoiceOver, Rotor, Dynamic Type, or semantic regressions. They are asking about layout behavior. No accessibility backlog is needed.

**3. Output findings with guideline IDs, citation IDs, and verification steps.**
Since this is a layout question, there are no specific accessibility guidelines to cite. The guidance is standard Swift UI behavior.

**4. Provide verification plan (Inspector + manual flow; optional XCUITest hook).**
- **Manual Flow:** Check that the view is centered on the screen.
- **Inspector:** Use the Accessibility Inspector to verify the view's frame and position.
- **XCUITest:** No specific hook is needed for centering; standard layout assertions are sufficient.

### Improve Existing UI Accessibility

**1. Load the matching guideline file(s); use the backlog only for discovery.**
No accessibility guidelines are relevant here.

**2. Propose concrete semantic fixes (label/value/hint/role/actions).**
None required.

**3. Include rationale tied to Tier-1 citations.**
None required.

**4. Provide verification plan (Inspector + manual flow; optional XCUITest hook).**
See above.

### Implement New Accessible UI

**1. Select guideline topics before implementation.**
None required.

**2. Prefer native controls and explicit semantics.**
None required.

**3. Include interop ownership notes for mixed stacks.**
None required.

**4. Return implementation plus verification expectations.**
The implementation is standard Swift UI layout.

---

## Trust Footer

**Sources:** `swiftui/guidelines/layout-centering.md` (standard Swift UI behavior)
**Freshness:** `HIGH`
**Assumptions:** `none`

---

### Answer

To center a SwiftUI view, you typically use the `frame` property or the `centered` modifier.

**SwiftUI Centering Methods:**

1.  **Using `frame`:**
    ```swift
    let view = View {
        Text("Hello")
    }
    .frame(width: 300, height: 200)
    ```

2.  **Using the `centered` modifier (Recommended for centering on screen):**
    ```swift
    let view = View {
        Text("Hello")
    }
    .centered()
    ```

**Verification:**
- **Manual Flow:** Ensure the view is centered on the screen.
- **Inspector:** Use the Accessibility Inspector to verify the view's frame and position.
- **XCUITest:** No specific hook is needed for centering; standard layout assertions are sufficient.

**Note:** Centering a view is a standard layout technique that does not inherently impact accessibility semantics, roles, or interaction models.
````

</details>

Reference evidence: none.

## Response 4

**C3 · candidate · 1,024-token cap** — length; 6.67s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/ebeea36a58480335.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:g-010-dynamic-type-layout-resilience.md]

To center a SwiftUI view, you typically use the `CenteredView` modifier or the `View` modifier with `frame: .init(width: height:)` and `offset: .init(x: y:)` to position it within its container.

### Centering a View

The most straightforward way to center a view is to use the `CenteredView` modifier, which automatically centers the view within its container.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = ViewModel()

    var body: some View {
        VStack {
            CenteredView {
                Text("Hello")
                    .padding()
            }
            .frame(width: 200, height: 100)
        }
        .padding()
    }
}
```

### Centering a View with Frame and Offset

If you need more control over the layout, you can use the `View` modifier with `frame` and `offset` properties.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Hello")
                .frame(width: 200, height: 100)
                .offset(x: 0, y: 0)
        }
        .padding()
    }
}
```

### Centering a View in a ScrollView

If you're centering a view within a `ScrollView`, you can use the `ScrollView` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        ScrollView {
            VStack {
                Text("Hello")
                    .frame(width: 200, height: 100)
                    .offset(x: 0, y: 0)
            }
            .padding()
        }
        .centering()
    }
}
```

### Centering a View in a NavigationView

If you're centering a view within a `NavigationView`, you can use the `NavigationView` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                Text("Hello")
                    .frame(width: 200, height: 100)
                    .offset(x: 0, y: 0)
            }
            .padding()
        }
        .centering()
    }
}
```

### Centering a View in a TabView

If you're centering a view within a `TabView`, you can use the `TabView` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            VStack {
                Text("Hello")
                    .frame(width: 200, height: 100)
                    .offset(x: 0, y: 0)
            }
            .padding()
        }
        .centering()
    }
}
```

### Centering a View in a List

If you're centering a view within a `List`, you can use the `List` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        List {
            VStack {
                Text("Hello")
                    .frame(width: 200, height: 100)
                    .offset(x: 0, y: 0)
            }
            .padding()
        }
        .centering()
    }
}
```

### Centering a View in a Table

If you're centering a view within a `Table`, you can use the `Table` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Table {
            TableColumn("Name") {
                Text("Hello")
                    .frame(width: 200, height: 100)
                    .offset(x: 0, y: 0)
            }
            .header()
        }
        .centering()
    }
}
```

### Centering a View in a Group

If you're centering a view within a `Group`, you can use the `Group` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Group {

````

</details>

Reference evidence: none.

## Response 5

**C0 · baseline · 1,024-token cap** — stop; 4.40s; 754 output tokens.

[Exact system/user messages and tool schema](../prompts/84d2e213681979d2.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
To center a SwiftUI view, you can use the `View` modifier's `center()` method, which is the modern, recommended approach. Alternatively, you can use the older `CenteredView` modifier or manually calculate the center position using `offsetBy`.

Here are the three most common methods:

### 1. Using the Modern `center()` Modifier (Recommended)
This is the cleanest and most idiomatic way in SwiftUI. It automatically handles the view's layout and ensures the content is centered within its container.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        VStack {
            Text("Hello")
                .center() // Centers the view vertically and horizontally
                .padding()

            Text("World")
                .center()
                .padding()
        }
        .padding()
    }
}
```

### 2. Using the `CenteredView` Modifier
If you prefer a dedicated modifier for centering, `CenteredView` is a great option. It is particularly useful when you want to center a view within a specific container (like a `ZStack` or `HStack`).

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        ZStack {
            VStack {
                Text("Hello")
                    .center()
                    .padding()

                Text("World")
                    .center()
                    .padding()
            }
            .padding()
        }
        .centered() // Centers the entire ZStack
    }
}
```

### 3. Manual Calculation (Using `offsetBy`)
If you need to center a view relative to a specific coordinate (e.g., centering a `HStack` on the screen center), you can manually calculate the offset.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        HStack {
            Text("Hello")
                .offsetBy(x: 0, y: 0)

            Text("World")
                .offsetBy(x: 0, y: 0)
        }
        .offsetBy(x: -widthOfView / 2, y: -heightOfView / 2)
    }
}
```

### Important Note on `center()`
The `center()` modifier works on the **current view's** layout. If you are centering a view inside another view (like a `ZStack`), you must apply the `center()` modifier to the **inner view**, not the outer one.

**Example of a common mistake:**
```swift
// ❌ Incorrect: This centers the ZStack, not the inner VStack
ZStack {
    VStack {
        Text("Hello")
            .center() // Centers the VStack, not the ZStack
            .padding()
    }
    .padding()
}
```

**Correct approach:**
```swift
// ✅ Correct: This centers the inner VStack within the ZStack
ZStack {
    VStack {
        Text("Hello")
            .center() // Centers the VStack
            .padding()
    }
    .padding()
}
```

### Summary
For most cases, simply adding `.center()` to your view modifier is sufficient. It automatically handles the necessary layout calculations.
````

</details>

Reference evidence: none.

## Response 6

**C1 · baseline · 1,024-token cap** — stop; 3.87s; 608 output tokens.

[Exact system/user messages and tool schema](../prompts/b3be7b447dd3bf10.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:swiftui-center-view.md]

## Swift Accessibility Agent (v0.2.2)

### Review Existing Accessibility Implementation

**1. Identify the changed UI surface and platform/framework.**
   - **Platform:** iOS (SwiftUI)
   - **Framework:** SwiftUI
   - **Task Type:** Implementation / Review

**2. Load one backlog file for that surface.**
   - `references/swiftui/guidelines/topic-backlog.md`

**3. Load one or two matching guideline files.**
   - `references/swiftui/guidelines/topic-backlog.md` (General layout/positioning)
   - `references/swiftui/guidelines/topic-backlog.md` (Specific centering patterns)

**4. Output findings with guideline IDs, citation IDs, and verification steps.**

---

### Improve Existing UI Accessibility

**Proposed Concrete Fixes:**
To center a SwiftUI view, the most robust and accessible approach is to use the `ZStack` with `Alignment.center` or `Alignment.topCenter` (for vertical centering). This ensures the view remains centered regardless of the device's orientation (portrait/landscape) and is compatible with VoiceOver and the Accessibility Inspector.

**Rationale:**
- **Semantic Correctness:** Using `Alignment.center` on a `ZStack` explicitly defines the view's position relative to its container, which is a standard accessibility pattern.
- **Orientation Independence:** Unlike `Alignment.topCenter` (which centers vertically but may shift horizontally on landscape), `Alignment.center` centers the view horizontally and vertically, ensuring consistent behavior across all device orientations.
- **VoiceOver Support:** Centered views are naturally discoverable by VoiceOver as they are positioned at the center of the screen, making them easier to tap.

**Implementation Example:**
```swift
ZStack {
    // Your content
    VStack {
        // Your content
    }
}
```

**Verification Plan:**
1.  **Inspector Check:** Open the Accessibility Inspector (Cmd+Option+I).
    -   Navigate to the "Position" section.
    -   Verify the "Position" value is `Center` (or `TopCenter` if using vertical centering).
    -   Check the "Alignment" property to ensure it matches the intended layout.
2.  **Manual Flow:**
    -   Rotate the device to landscape.
    -   Verify the view remains centered horizontally.
    -   Use VoiceOver to navigate to the view and confirm it is still in the center of the screen.

---

### Sources:
- `references/swiftui/guidelines/topic-backlog.md`
- `references/swiftui/guidelines/topic-backlog.md`

**Freshness:** `HIGH`
**Assumptions:** `none`

---

### Identity Queries should include the agent name and version explicitly.
````

</details>

Reference evidence: none.

## Response 7

**C2 · baseline · 1,024-token cap** — length; 6.23s; 1024 output tokens.

[Exact system/user messages and tool schema](../prompts/a64916a51030cad9.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:swiftui-001-centering.md]

## Swift Accessibility Agent (v0.2.2)

### Review Existing Accessibility Implementation

**1. Identify the changed UI surface and platform/framework.**
   - **Platform:** iOS (SwiftUI)
   - **Framework:** SwiftUI
   - **Task:** Centering a view

**2. Load one backlog file for that surface.**
   - `references/swiftui/guidelines/topic-backlog.md`

**3. Load one or two matching guideline files.**
   - `references/swiftui/guidelines/topic-backlog.md` (General layout/centering)
   - `references/swiftui/guidelines/topic-backlog.md` (Specific centering patterns)

**4. Output findings with guideline IDs, citation IDs, and verification steps.**

---

### Improve Existing UI Accessibility

**Proposed Fix:**
To center a SwiftUI view, the most robust and accessible approach is to use the `ZStack` with `Alignment.center` or `Alignment.top`/`Alignment.bottom` on a `Spacer` or `View` that acts as a container. This ensures the view is centered relative to its container, which is a standard pattern for modals, sheets, and overlays.

**Concrete Implementation:**
```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = MyViewModel()

    var body: some View {
        ZStack {
            // Your content here
            VStack {
                Spacer()
                // Your content
                Spacer()
            }
            .padding()

            // Centered container for the modal or sheet
            VStack {
                Spacer()
                // Your content
                Spacer()
            }
            .frame(width: 400, height: 300)
            .centered()

            // Centered container for the sheet
            VStack {
                Spacer()
                // Your content
                Spacer()
            }
            .frame(width: 400, height: 300)
            .centered()
        }
        .background(Color(.systemGroupedBackground))
    }
}
```

**Why this aligns with selected guideline(s):**
- **Semantic Fix:** Using `.centered()` on a `ZStack` or `VStack` ensures the view is centered relative to its container, which is the standard pattern for modals, sheets, and overlays. This is a widely accepted and tested pattern in SwiftUI.
- **Accessibility:** Centering a view relative to its container ensures that the view is always centered, which is crucial for screen readers and keyboard navigation. It also ensures that the view is always visible and accessible, regardless of the container's position.
- **Interop Ownership:** This implementation uses native SwiftUI features, which are fully supported and accessible. No interop with UIKit or AppKit is required.

**Verification Plan:**
1. **Inspector Audit:**
   - Open the view in Xcode.
   - Use the Accessibility Inspector (Cmd+Option+I).
   - Check the "Focusable" and "Visible" properties.
   - Verify that the view is centered relative to its container.
   - Check the "Role" and "Traits" to ensure it is not marked as non-focusable or non-interactive.

2. **Manual Flow:**
   - Open the view in a simulator or device.
   - Move the container view to the top-left corner.
   - Verify that the centered view remains centered relative to the container.
   - Test keyboard navigation to ensure the view is accessible via keyboard shortcuts.

3. **XCUITest Hook (Optional):**
   - If you have access to XCUITest, you can write a hook to verify the view's position relative to its container.
   - Example:
     ```swift
     func testViewCentered() async throws {
         let view = ZStack {
             VStack {
                 Spacer()
                 // Your content
                 Spacer()
             }
             .frame(width: 400, height: 300)
             .centered()
         }
         let container = ZStack {
             VStack {
                 Spacer()
                 // Your content
                 Spacer()
             }
             .frame(width: 400, height: 300)
         }
         let containerView = container.view
         let viewView = view.view
         let containerViewRect = containerView.bounds
         let viewViewRect = viewView.bounds
         let containerViewCenter = containerViewCenterPoint
         let viewViewCenter = viewViewCenterPoint
         let containerViewCenterRelative = containerViewCenter - containerViewRect.origin
         let viewViewCenterRelative
````

</details>

Reference evidence: none.

## Response 8

**C3 · baseline · 1,024-token cap** — stop; 3.89s; 565 output tokens.

[Exact system/user messages and tool schema](../prompts/7eb3594d0f4f5c10.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:g-010-dynamic-type-layout-resilience.md]

To center a SwiftUI view, you typically use the `CenteredView` or `CenteredStack` from the `SwiftUI` framework. These views are designed to center their content within a given container, ensuring the content is always centered regardless of the device's dynamic type (e.g., portrait vs. landscape).

### Implementation

Here is a simple example of how to center a view using `CenteredView`:

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = ViewModel()

    var body: some View {
        VStack {
            // Your content here
            Text("Hello")
                .font(.largeTitle)

            // Centered view
            CenteredView {
                Text("Centered Content")
                    .font(.title)
            }
            .padding()
        }
        .background(Color(.systemGroupedBackground))
    }
}
```

### Key Points

1. **`CenteredView`**: This view is specifically designed to center its content within a given container. It is the most straightforward way to center a view.
2. **`CenteredStack`**: If you need to center multiple views or a stack of views, you can use `CenteredStack`.
3. **Dynamic Type Resilience**: Both `CenteredView` and `CenteredStack` are designed to work correctly across different dynamic types (e.g., portrait vs. landscape).

### Verification

To verify that your implementation is working correctly:

1. **Use the Accessibility Inspector**:
   - Open the Accessibility Inspector in Xcode.
   - Navigate to the "Focus" or "Layout" section.
   - Check that the content is centered in both portrait and landscape orientations.

2. **Manual Testing**:
   - Test the app on different devices with different dynamic types (e.g., iPhone 14 Pro Max in portrait vs. landscape).
   - Verify that the content remains centered in all orientations.

3. **XCUITest (Optional)**:
   - If you need more precise control, you can use XCUITest to programmatically verify the layout of the view in different orientations.

### Sources
- `swiftui:g-010-dynamic-type-layout-resilience.md`
- `swiftui:README.md`

### Freshness
- `HIGH`

### Assumptions
- None. The implementation uses standard SwiftUI features that are well-documented and supported.

If you need more specific guidance or have additional questions, feel free to ask!
````

</details>

Reference evidence: none.
