# SwiftUI macos-focus-requests

## Platforms

macOS; deployment target 26.0. Source: installed public SDK27 declarations.

Focus-state modifier availability on macOS; requests are not proof that focus was delivered.

## Declared APIs

- View.accessibilityFocused(_:equals:): SDK @available annotation includes macOS 12.0.

```text
@available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
extension SwiftUICore.View {
  nonisolated public func accessibilityFocused<Value>(_ binding: SwiftUI.AccessibilityFocusState<Value>.Binding, equals value: Value) -> some SwiftUICore.View where Value : Swift.Hashable
```

Source: SwiftUI/arm64e-apple-macos.swiftinterface:27979; full-interface SHA256 155b00c7d8fa9e9696b96b4bd3291b4c910207b480025d13ba6482f7b9940d38.

## Evidence scope

These are declaration/availability excerpts, not application snippets. Module migration annotations are not introduction dates. API availability does not establish rendered layout, generated semantics, automatic environment propagation, spoken output or delivered focus.
