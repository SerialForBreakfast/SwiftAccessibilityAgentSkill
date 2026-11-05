# D31 · Centering a view

[← Dashboard](../README.md) · [All cases](../README.md#browse-the-cases)

**Development comparison · OS context 26 · 8 responses · quality not independently graded**

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
| C0 | 1024 | stop | 4.36 | 0 unavailable | [Read ↓](#response-1) |
| C2 | 1024 | stop | 4.54 | 0 injected | [Read ↓](#response-2) |
| C3-original | 1024 | length | 6.59 | 0 model-read | [Read ↓](#response-3) |
| C3-explicit | 1024 | stop | 3.45 | 0 model-read | [Read ↓](#response-4) |
| C0 | 2048 | stop | 4.37 | 0 unavailable | [Read ↓](#response-5) |
| C2 | 2048 | stop | 4.63 | 0 injected | [Read ↓](#response-6) |
| C3-original | 2048 | length | 12.75 | 0 model-read | [Read ↓](#response-7) |
| C3-explicit | 2048 | stop | 3.36 | 0 model-read | [Read ↓](#response-8) |

Times include request processing; first-request warmup effects are not separated here. A normal finish is not a correctness score. C2 reference counts are harness injection, not model tool use.

## Response excerpts

Opening prose excerpts for quick comparison; ellipses mark omitted text. Full original wording is preserved below. These excerpts are not grades.

| Variant | Original response excerpt |
| --- | --- |
| [C0 · candidate · 1024](#response-1) | To center a SwiftUI view, you can use the View modifier's center() method, which is the modern, recommended approach. Alternatively, you can use the older CenteredView modifier or manually calculate the center posi … |
| [C2 · candidate · 1024](#response-2) | 1. Identify the changed UI surface and platform/framework. The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e … |
| [C3-original · candidate · 1024](#response-3) | To center a SwiftUI view, you typically use the CenteredView modifier or the View modifier with frame: .init(width: height:) and offset: .init(x: y:) to position it within its container. The most straightforward  … |
| [C3-explicit · candidate · 1024](#response-4) | To center a SwiftUI view, you generally use the Center modifier. This is the standard approach for views that need to be centered on the screen. SwiftUI: import SwiftUI struct ContentView: View { @StateObject priva … |
| [C0 · candidate · 2048](#response-5) | To center a SwiftUI view, you can use the View modifier's center() method, which is the modern, recommended approach. Alternatively, you can use the older CenteredView modifier or manually calculate the center posi … |
| [C2 · candidate · 2048](#response-6) | 1. Identify the changed UI surface and platform/framework. The user is asking about centering a SwiftUI view. This is a layout concern, not an accessibility concern. Centering a view is a standard layout technique (e … |
| [C3-original · candidate · 2048](#response-7) | To center a SwiftUI view, you typically use the CenteredView modifier or the View modifier with frame: .init(width: height:) and offset: .init(x: y:) to position it within its container. The most straightforward  … |
| [C3-explicit · candidate · 2048](#response-8) | To center a SwiftUI view, you generally use the Center modifier. This is the standard approach for views that need to be centered on the screen. SwiftUI: import SwiftUI struct ContentView: View { @StateObject priva … |

## Response 1

**C0 · candidate · 1,024-token cap** — stop; 4.36s; 754 output tokens.

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

## Response 3

**C3-original · candidate · 1,024-token cap** — length; 6.59s; 1024 output tokens.

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

## Response 4

**C3-explicit · candidate · 1,024-token cap** — stop; 3.45s; 460 output tokens.

[Exact system/user messages and tool schema](../prompts/54205a37c6178100.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:g-010-dynamic-type-layout-resilience.md]

To center a SwiftUI view, you generally use the `Center` modifier. This is the standard approach for views that need to be centered on the screen.

**SwiftUI:**
```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = ViewModel()

    var body: some View {
        VStack {
            // Your content
            Text("Hello")
        }
        .padding()
        .center()
    }
}
```

**UIKit:**
```swift
import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        // Center the view
        view.center()
    }
}
```

**Important Note:**
The `center()` modifier in SwiftUI is a convenience wrapper around the `LayoutConstraint` system. It automatically applies the appropriate layout constraints (like `CenterContentLayoutGuide`) to ensure the view is centered.

For more complex scenarios, such as centering a view within a specific container or managing dynamic type (dynamic font size), you might need to combine this with other modifiers or use the `LayoutGuide` system directly.

**Verification Steps:**
1.  **Inspector:** Open the Inspector in Xcode. Check the "Layout" section to ensure the view has a `CenterContentLayoutGuide` or similar constraint applied.
2.  **Manual Flow:** Place the view on the screen and drag it to the center. The view should remain centered even if the screen size changes.
3.  **Dynamic Type:** Test with different font sizes (e.g., 12pt, 14pt, 16pt) to ensure the view remains centered and does not overflow or become misaligned.

**Assumptions:**
- The view is placed within a `VStack`, `HStack`, or `ZStack` container.
- The device supports dynamic type (iOS 13+).

**Sources:**
- `swiftui:g-010-dynamic-type-layout-resilience.md`
- `swiftui:README.md`
````

</details>

Reference evidence: none.

## Response 5

**C0 · candidate · 2,048-token cap** — stop; 4.37s; 754 output tokens.

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

**C2 · candidate · 2,048-token cap** — stop; 4.63s; 722 output tokens.

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

## Response 7

**C3-original · candidate · 2,048-token cap** — length; 12.75s; 2048 output tokens.

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

### Centering a View in a Stack

If you're centering a view within a `Stack`, you can use the `Stack` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Stack {
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

### Centering a View in a HStack

If you're centering a view within a `HStack`, you can use the `HStack` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        HStack {
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

### Centering a View in a Row

If you're centering a view within a `Row`, you can use the `Row` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Row {
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

### Centering a View in a Column

If you're centering a view within a `Column`, you can use the `Column` modifier with the `centering` property.

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Column {
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
    var body
````

</details>

Reference evidence: none.

## Response 8

**C3-explicit · candidate · 2,048-token cap** — stop; 3.36s; 460 output tokens.

[Exact system/user messages and tool schema](../prompts/54205a37c6178100.json) · [Back to comparison](#compare-responses)

<details>
<summary>Show complete original model response</summary>

````text
ROUTING: [swiftui:g-010-dynamic-type-layout-resilience.md]

To center a SwiftUI view, you generally use the `Center` modifier. This is the standard approach for views that need to be centered on the screen.

**SwiftUI:**
```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = ViewModel()

    var body: some View {
        VStack {
            // Your content
            Text("Hello")
        }
        .padding()
        .center()
    }
}
```

**UIKit:**
```swift
import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        // Center the view
        view.center()
    }
}
```

**Important Note:**
The `center()` modifier in SwiftUI is a convenience wrapper around the `LayoutConstraint` system. It automatically applies the appropriate layout constraints (like `CenterContentLayoutGuide`) to ensure the view is centered.

For more complex scenarios, such as centering a view within a specific container or managing dynamic type (dynamic font size), you might need to combine this with other modifiers or use the `LayoutGuide` system directly.

**Verification Steps:**
1.  **Inspector:** Open the Inspector in Xcode. Check the "Layout" section to ensure the view has a `CenterContentLayoutGuide` or similar constraint applied.
2.  **Manual Flow:** Place the view on the screen and drag it to the center. The view should remain centered even if the screen size changes.
3.  **Dynamic Type:** Test with different font sizes (e.g., 12pt, 14pt, 16pt) to ensure the view remains centered and does not overflow or become misaligned.

**Assumptions:**
- The view is placed within a `VStack`, `HStack`, or `ZStack` container.
- The device supports dynamic type (iOS 13+).

**Sources:**
- `swiftui:g-010-dynamic-type-layout-resilience.md`
- `swiftui:README.md`
````

</details>

Reference evidence: none.
