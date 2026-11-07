# SwiftUI macos-text-sizing

## Platforms

macOS; deployment target 26.0. Source: installed public SDK27 declarations.

Explicit DynamicTypeSize environment and ScaledMetric declarations on macOS. These declarations do not establish a system settings source or automatic settings propagation; that integration is application-dependent.

## Declared APIs

- EnvironmentValues.dynamicTypeSize: SDK @available annotation includes macOS 12.0.

```text
@available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
@_originallyDefinedIn(module: "SwiftUI", iOS 18.0)
@_originallyDefinedIn(module: "SwiftUI", macOS 15.0)
@_originallyDefinedIn(module: "SwiftUI", tvOS 18.0)
@_originallyDefinedIn(module: "SwiftUI", watchOS 11.0)
extension SwiftUICore::EnvironmentValues {
  public var dynamicTypeSize: SwiftUICore::DynamicTypeSize {
```

Source: SwiftUICore/arm64e-apple-macos.swiftinterface:14783; full-interface SHA256 4fb89ff3d972d507faee2bde0a7e81761a2cb9c744eaf94df810235918c7ac13.

- ScaledMetric: SDK @available annotation includes macOS 11.0.

```text
@available(iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, *)
@_originallyDefinedIn(module: "SwiftUI", iOS 18.0)
@_originallyDefinedIn(module: "SwiftUI", macOS 15.0)
@_originallyDefinedIn(module: "SwiftUI", tvOS 18.0)
@_originallyDefinedIn(module: "SwiftUI", watchOS 11.0)
@propertyWrapper public struct ScaledMetric<Value> : SwiftUICore::DynamicProperty where Value : Swift::BinaryFloatingPoint {
```

Source: SwiftUICore/arm64e-apple-macos.swiftinterface:15035; full-interface SHA256 4fb89ff3d972d507faee2bde0a7e81761a2cb9c744eaf94df810235918c7ac13.

## Evidence scope

These are declaration/availability excerpts, not application snippets. Module migration annotations are not introduction dates. API availability does not establish rendered layout, generated semantics, automatic environment propagation, spoken output or delivered focus.
