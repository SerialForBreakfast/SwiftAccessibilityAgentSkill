# SwiftUI macos-values

## Platforms

macOS; deployment target 26.0. Source: installed public SDK27 declarations.

Value-description modifier availability on macOS; application update/ownership policy remains separate.

## Declared APIs

- View.accessibilityValue(Text): SDK @available annotation includes macOS 11.0.

```text
@available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
extension SwiftUICore.View {
  nonisolated public func accessibilityValue(_ valueDescription: SwiftUICore.Text) -> SwiftUICore.ModifiedContent<Self, SwiftUI.AccessibilityAttachmentModifier>
```

Source: SwiftUI/arm64e-apple-macos.swiftinterface:60; full-interface SHA256 155b00c7d8fa9e9696b96b4bd3291b4c910207b480025d13ba6482f7b9940d38.

## Evidence scope

These are declaration/availability excerpts, not application snippets. Module migration annotations are not introduction dates. API availability does not establish rendered layout, generated semantics, automatic environment propagation, spoken output or delivered focus.
