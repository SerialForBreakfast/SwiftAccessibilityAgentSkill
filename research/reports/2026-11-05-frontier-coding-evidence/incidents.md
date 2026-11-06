# Exact incident record

Generated from preserved files on2026-11-05. Snippets are exact source extracts, not reconstructed pseudocode. Paths and file hashes accompany each extract. Read the [scope and interpretation](README.md) before using these as evaluation cases.

## F01: Compiler diagnostic wording guessed from property optionality

Classification: Model-authored oracle / harness contract.

The invalid assignment was intentional. The unexpected failure was the matcher expecting String? while the compiler emitted String; the intended failure did not qualify until the matcher was versioned.

### Original code / expectation

Source: [code-examples/pilots/uikit-v1/history/manifest-revision-1.json:187](../../../code-examples/pilots/uikit-v1/history/manifest-revision-1.json#L187); SHA-256 `19d09c36d8258989e3bc0d805b3c1e64e38bfd7b12d64225fa6647c63d732f26`.

```json
"diagnostics": [
        {
          "id": "label-type-mismatch",
          "contains": "cannot assign value of type 'Int' to type 'String?'"
        }
      ]
    }
  ]
}
```

Source: [code-examples/pilots/uikit-v1/NegativeFixtures/WrongLabelType.swift:4](../../../code-examples/pilots/uikit-v1/NegativeFixtures/WrongLabelType.swift#L4); SHA-256 `e9123c7aef47a7e3e47465786093b0399c96ec5da843cfa33b2bdfae76a4a920`.

```swift
@MainActor func invalidLabelType() {
    UILabel().accessibilityLabel = 42
}
```

### Correction

Source: [code-examples/pilots/uikit-v1/manifest.json:187](../../../code-examples/pilots/uikit-v1/manifest.json#L187); SHA-256 `609af86e4ee70b60c177ea0b3b9901557b83db7117d3fb6e72ab618dbb89199c`.

```json
"diagnostics": [
        {
          "id": "label-type-mismatch",
          "contains": "cannot assign value of type 'Int' to type 'String'"
        }
      ]
    }
  ]
}
```

### Observed diagnostics

```text
error: cannot assign value of type 'Int' to type 'String'
```

Reports: [code-examples/pilots/uikit-v1/validation/pilot-r2-results.json](../../../code-examples/pilots/uikit-v1/validation/pilot-r2-results.json).

### Candidate skill lesson

Derive diagnostic expectations from captured compiler output. Property declaration optionality does not guarantee diagnostic wording. Keep exact toolchain and fail closed for unknown diagnostics.

### Proposed evaluation

Ask a model to design a compiler-negative check without supplying the exact message. Score whether it captures and versions actual output rather than guessing or accepting every nonzero exit.

## F02: Autorelease timing mistaken for persistent retention

Classification: Model-authored lifetime-test setup.

The first positive suite passed14/15; a weak UILabel reference was still non-nil before draining temporary Objective-C references. Source code did not change. An explicit autorelease boundary made the intended ownership assertion meaningful, and a deliberate retained-element mutant still failed.

### Original code / expectation

Source: [code-examples/pilots/uikit-dynamic-v1/history/revision-1/Tests/DynamicUIKitTests.swift:67](../../../code-examples/pilots/uikit-dynamic-v1/history/revision-1/Tests/DynamicUIKitTests.swift#L67); SHA-256 `b9947a7976508984ecbd3e05ff30506f4557ccd2833ed3267b1ffbe31b6eeb84`.

```swift
    @MainActor func testRemovedElementIsNotRetainedByIndexOrContainer() {
        let view = DynamicSections(frame: .zero)
        view.replace(records)
        weak var removed = view.labels[0]
        view.replace([records[1]])
        XCTAssertNil(removed)
    }
```

### Correction

Source: [code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift:67](../../../code-examples/pilots/uikit-dynamic-v1/Tests/DynamicUIKitTests.swift#L67); SHA-256 `5fcffc72fab4f66e2e36973100f43771eb3e31b532973eb43d301d73bca9935b`.

```swift
    @MainActor func testRemovedElementIsNotRetainedByIndexOrContainer() {
        let view = DynamicSections(frame: .zero)
        weak var removed: UILabel?
        // Observe persistent ownership after temporary Objective-C references drain.
        autoreleasepool {
            view.replace(records)
            removed = view.labels[0]
            view.replace([records[1]])
        }
        XCTAssertNil(removed)
    }
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.DynamicUIKitTests testRemovedElementIsNotRetainedByIndexOrContainer] : XCTAssertNil failed: "<UILabel: <address>; frame = (0 0; 0 0); text = 'A...a' (length = 5); userInteractionEnabled = NO; backgroundColor = UIExtendedGrayColorSpace 0 0; layer = <_UILabelLayer: <address>>>"
```

Reports: [code-examples/pilots/uikit-dynamic-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-1.json), [code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json).

### Candidate skill lesson

Separate temporary autorelease lifetime from persistent ownership. A weak-reference assertion needs a controlled observation boundary and a mutation that proves it still detects retained ownership.

### Proposed evaluation

Give a failing weak UILabel lifetime assertion and ask for a diagnosis. Penalize claiming an Apple leak, changing production ownership without evidence, or deleting the assertion.

## F03: XCTFail was incompatible with the adapter assertion whitelist

Classification: Test/adapter representation mismatch.

The mutant did invoke the forbidden callback. XCTest summarized XCTFail as "failed - ...", not "XCTAssert...". The conservative adapter therefore returned error/not-assessed. The correction recorded call count and asserted zero; it did not widen the adapter to accept arbitrary failures.

### Original code / expectation

Source: [code-examples/pilots/uikit-containers-v1/history/revision-1/Tests/ContainerUIKitTests.swift:146](../../../code-examples/pilots/uikit-containers-v1/history/revision-1/Tests/ContainerUIKitTests.swift#L146); SHA-256 `a7d30db378c69352ab35e0f8c21f69e6b8466f225d77a7069d26db1d9eab147f`.

```swift
    func testDisabledActivationDoesNotInvokeHandler() {
        let control = ActivationControl()
        control.perform = { XCTFail("Disabled control invoked callback"); return true }
        control.isEnabled = false
        XCTAssertFalse(control.accessibilityActivate())
    }
```

### Correction

Source: [code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift:146](../../../code-examples/pilots/uikit-containers-v1/Tests/ContainerUIKitTests.swift#L146); SHA-256 `ab22df52dd5b7b048155718b593b2089cdf005de35266d2015481ae5cb629982`.

```swift
    func testDisabledActivationDoesNotInvokeHandler() {
        let control = ActivationControl()
        var calls = 0
        control.perform = { calls += 1; return true }
        control.isEnabled = false
        XCTAssertFalse(control.accessibilityActivate())
        XCTAssertEqual(calls, 0)
    }
```

Source: [code-examples/tools/native-core.mjs:59](../../../code-examples/tools/native-core.mjs#L59); SHA-256 `10709e14acd380a18a805858b4881956a512f674e66c7cfbedd54c2303d03346`.

```javascript
  if (failedTestIds.length) {
    const failures = summary.testFailures;
    if (!failures?.length || failures.some(f => !f.failureText?.startsWith('XCTAssert') ||
        !failedTestIds.includes(f.testIdentifierString?.replace(/\(\)$/, '')))) throw Error('Non-assertion or unrelated test failure');
  }
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.ContainerUIKitTests testDisabledActivationDoesNotInvokeHandler] : failed - Disabled control invoked callback
error: -[AccessibilityExamplesTests.ContainerUIKitTests testDisabledActivationDoesNotInvokeHandler] : XCTAssertFalse failed
```

Reports: [code-examples/pilots/uikit-containers-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-containers-v1/validation/revision-1.json), [code-examples/pilots/uikit-containers-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-containers-v1/validation/revision-2.json).

### Candidate skill lesson

Understand the grading contract before authoring assertions. An unclassified failure is not a successful mutant kill. Explicit state/count assertions can be clearer and more machine-verifiable.

### Proposed evaluation

Supply the log and whitelist. Require preserving error status and proposing a precise counted assertion; reject counting the original adapter error as a passing check.

## F04: Detached font traits disagreed with the receiving label environment

Classification: Model-authored configuration/test mismatch.

The suite passed10/11. With automatic font adjustment enabled, observed sizes included17 rather than53,17 rather than15,12 rather than43, and12 rather than11. Passing a separate trait collection to font creation had not configured the receiving label environment.

### Original code / expectation

Source: [code-examples/pilots/uikit-reuse-v1/history/revision-1/Sources/ReuseUIKit.swift:48](../../../code-examples/pilots/uikit-reuse-v1/history/revision-1/Sources/ReuseUIKit.swift#L48); SHA-256 `745cde77056a2cb8bfa42b3943fa7f85c34b38825155e495d90e70fdda96ea24`.

```swift
public enum ReusableTypography {
    public static func configure(_ label: UILabel, style: UIFont.TextStyle, traits: UITraitCollection) {
        label.font = .preferredFont(forTextStyle: style, compatibleWith: traits)
        label.adjustsFontForContentSizeCategory = true
        label.numberOfLines = 0
    }
}
```

Source: [code-examples/pilots/uikit-reuse-v1/history/revision-1/Tests/ReuseUIKitTests.swift:105](../../../code-examples/pilots/uikit-reuse-v1/history/revision-1/Tests/ReuseUIKitTests.swift#L105); SHA-256 `e80f60e88330ce8fad323adaba5dbdfe1b7f10647d2b3b67a31597677be9f229`.

```swift
    func testTypographyReconfigurationReplacesStyleAndSizePolicy() {
        let label = UILabel()
        for style: UIFont.TextStyle in [.headline, .caption1, .body] {
            for category: UIContentSizeCategory in [.large, .accessibilityExtraExtraExtraLarge, .small] {
                let traits = UITraitCollection(preferredContentSizeCategory: category)
                label.numberOfLines = 1
                label.adjustsFontForContentSizeCategory = false
                ReusableTypography.configure(label, style: style, traits: traits)
                XCTAssertEqual(label.font.pointSize, UIFont.preferredFont(forTextStyle: style, compatibleWith: traits).pointSize)
                XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, style.rawValue)
                XCTAssertTrue(label.adjustsFontForContentSizeCategory)
                XCTAssertEqual(label.numberOfLines, 0)
            }
        }
    }
```

### Correction

Source: [code-examples/pilots/uikit-reuse-v1/Sources/ReuseUIKit.swift:48](../../../code-examples/pilots/uikit-reuse-v1/Sources/ReuseUIKit.swift#L48); SHA-256 `4dfd9e59adafda3abca189c95aa885ce1cd31704e4a25cad61be455539fd1bbb`.

```swift
public enum ReusableTypography {
    public static func configure(_ label: UILabel, style: UIFont.TextStyle) {
        label.font = .preferredFont(forTextStyle: style, compatibleWith: label.traitCollection)
        label.adjustsFontForContentSizeCategory = true
        label.numberOfLines = 0
    }
}
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("17.0") is not equal to ("53.0")
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("17.0") is not equal to ("15.0")
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("12.0") is not equal to ("43.0")
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("12.0") is not equal to ("11.0")
```

Reports: [code-examples/pilots/uikit-reuse-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-1.json), [code-examples/pilots/uikit-reuse-v1/validation/revision-3.json](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-3.json).

### Candidate skill lesson

Reason about the receiving UIKit trait environment and automatic adjustment together, not just preferredFont in isolation. Retain exact requested categories and style checks.

### Proposed evaluation

Ask for a reusable Dynamic Type label test across categories. Check that it sets and verifies effective traits rather than comparing a detached font against a differently configured label.

## F05: Trait override assumed to propagate synchronously

Classification: Model-authored lifecycle/test setup; second attempt in same family.

After assigning traitOverrides, the new effective-category assertion still read large instead of accessibilityXXXL or small. Calling updateTraitsIfNeeded after assignment resolved the setup. All nine style/category combinations remained asserted.

### Original code / expectation

Source: [code-examples/pilots/uikit-reuse-v1/history/revision-2/Tests/ReuseUIKitTests.swift:105](../../../code-examples/pilots/uikit-reuse-v1/history/revision-2/Tests/ReuseUIKitTests.swift#L105); SHA-256 `aad7a318c7c3d70eb110359c99915267652ac83137ca71a55202afedee1e8406`.

```swift
    func testTypographyReconfigurationReplacesStyleAndSizePolicy() {
        let label = UILabel()
        for style: UIFont.TextStyle in [.headline, .caption1, .body] {
            for category: UIContentSizeCategory in [.large, .accessibilityExtraExtraExtraLarge, .small] {
                label.traitOverrides.preferredContentSizeCategory = category
                let traits = label.traitCollection
                XCTAssertEqual(traits.preferredContentSizeCategory, category)
                label.numberOfLines = 1
                label.adjustsFontForContentSizeCategory = false
                ReusableTypography.configure(label, style: style)
                XCTAssertEqual(label.font.pointSize, UIFont.preferredFont(forTextStyle: style, compatibleWith: traits).pointSize)
                XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, style.rawValue)
                XCTAssertTrue(label.adjustsFontForContentSizeCategory)
                XCTAssertEqual(label.numberOfLines, 0)
            }
        }
    }
```

### Correction

Source: [code-examples/pilots/uikit-reuse-v1/Tests/ReuseUIKitTests.swift:105](../../../code-examples/pilots/uikit-reuse-v1/Tests/ReuseUIKitTests.swift#L105); SHA-256 `46d3ab83dddce83d6dc6b5944c3fbf1c70e25e7428f4bdb7ba8e24eae82e280b`.

```swift
    func testTypographyReconfigurationReplacesStyleAndSizePolicy() {
        let label = UILabel()
        for style: UIFont.TextStyle in [.headline, .caption1, .body] {
            for category: UIContentSizeCategory in [.large, .accessibilityExtraExtraExtraLarge, .small] {
                label.traitOverrides.preferredContentSizeCategory = category
                label.updateTraitsIfNeeded()
                let traits = label.traitCollection
                XCTAssertEqual(traits.preferredContentSizeCategory, category)
                label.numberOfLines = 1
                label.adjustsFontForContentSizeCategory = false
                ReusableTypography.configure(label, style: style)
                XCTAssertEqual(label.font.pointSize, UIFont.preferredFont(forTextStyle: style, compatibleWith: traits).pointSize)
                XCTAssertEqual(label.font.fontDescriptor.object(forKey: .textStyle) as? String, style.rawValue)
                XCTAssertTrue(label.adjustsFontForContentSizeCategory)
                XCTAssertEqual(label.numberOfLines, 0)
            }
        }
    }
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("UIContentSizeCategory(_rawValue: UICTContentSizeCategoryL)") is not equal to ("UIContentSizeCategory(_rawValue: UICTContentSizeCategoryAccessibilityXXXL)")
error: -[AccessibilityExamplesTests.ReuseUIKitTests testTypographyReconfigurationReplacesStyleAndSizePolicy] : XCTAssertEqual failed: ("UIContentSizeCategory(_rawValue: UICTContentSizeCategoryL)") is not equal to ("UIContentSizeCategory(_rawValue: UICTContentSizeCategoryS)")
```

Reports: [code-examples/pilots/uikit-reuse-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-2.json), [code-examples/pilots/uikit-reuse-v1/validation/revision-3.json](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-3.json).

### Candidate skill lesson

Configuration assignment and effective state are different steps. Use the documented synchronous trait update boundary when a deterministic unit assertion requires it; do not add arbitrary sleeps.

### Proposed evaluation

Present the failed effective-category assertion. Require a documented update boundary, no UI automation or global preference mutation, and preservation of the expected large/small categories.

## F06: Native UIButton role assumed to appear in a headless property getter

Classification: Unsupported oracle about test environment; native observation.

The direct getter did not contain .button in this headless run. The example now explicitly inserts the trait, so the passing test proves explicit configuration. It does NOT explain the native getter observation or prove a displayed UIButton lacks a button role.

### Original code / expectation

Source: [code-examples/pilots/uikit-media-v1/history/revision-1/Sources/MediaUIKit.swift:15](../../../code-examples/pilots/uikit-media-v1/history/revision-1/Sources/MediaUIKit.swift#L15); SHA-256 `f6c7ac23f751eefdbfea39c0854ef49ae2d7ffefa54520d3eb781f8508a561bd`.

```swift
    public static func configure(_ button: UIButton, playing: Bool) {
        button.setTitle(playing ? "Pause" : "Play", for: .normal)
        button.accessibilityLabel = playing ? "Pause" : "Play"
        button.accessibilityValue = playing ? "Playing" : "Paused"
    }
```

Source: [code-examples/pilots/uikit-media-v1/history/revision-1/Tests/MediaUIKitTests.swift:19](../../../code-examples/pilots/uikit-media-v1/history/revision-1/Tests/MediaUIKitTests.swift#L19); SHA-256 `cf91e7a08771df9f99587b4b3f2ddbf45708ff2443b48fea74a864a98104f6bb`.

```swift
    func testPlayPauseControlMetadataTransitions() {
        let button = UIButton(type: .system)
        MediaConfiguration.configure(button, playing: false)
        XCTAssertEqual(button.title(for: .normal), "Play")
        XCTAssertEqual(button.accessibilityLabel, "Play")
        XCTAssertEqual(button.accessibilityValue, "Paused")
        MediaConfiguration.configure(button, playing: true)
        XCTAssertEqual(button.title(for: .normal), "Pause")
        XCTAssertEqual(button.accessibilityLabel, "Pause")
        XCTAssertEqual(button.accessibilityValue, "Playing")
        XCTAssertTrue(button.accessibilityTraits.contains(.button))
    }
```

### Correction

Source: [code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift:15](../../../code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift#L15); SHA-256 `7fd55e418c7253dadb42c1917471513ef75cb5af4a20e47c90b8c3968b0ed3f6`.

```swift
    public static func configure(_ button: UIButton, playing: Bool) {
        button.accessibilityTraits.insert(.button)
        button.setTitle(playing ? "Pause" : "Play", for: .normal)
        button.accessibilityLabel = playing ? "Pause" : "Play"
        button.accessibilityValue = playing ? "Playing" : "Paused"
    }
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.MediaUIKitTests testPlayPauseControlMetadataTransitions] : XCTAssertTrue failed
```

Reports: [code-examples/pilots/uikit-media-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-1.json), [code-examples/pilots/uikit-media-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-2.json), [code-examples/pilots/uikit-media-v1/validation/revision-3.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

### Candidate skill lesson

Do not equate a headless getter with the assistive-technology representation. Label the correction as a change from an assumed default to an explicit configuration contract; native-default behavior remains a bounded unresolved observation.

### Proposed evaluation

Ask why a native UIButton trait assertion fails in a logic test. Reward scope discipline; reject claiming VoiceOver announces no role or that every UIButton must have its role manually added.

## F07: Two authored subtitle tracks assumed to mean two selection options

Classification: Model-authored data-model assumption with framework metadata evidence.

AVFoundation returned English, English Forced, Spanish and Spanish Forced. The original count assertion failed4 versus2, including on a diagnostic second run. The final test checks two full and two forced-only variants and both language sets for this pinned fixture. A new forced-only mutant proves language alone is insufficient.

### Original code / expectation

Source: [code-examples/pilots/uikit-media-v1/history/revision-1/Tests/MediaUIKitTests.swift:58](../../../code-examples/pilots/uikit-media-v1/history/revision-1/Tests/MediaUIKitTests.swift#L58); SHA-256 `cf91e7a08771df9f99587b4b3f2ddbf45708ff2443b48fea74a864a98104f6bb`.

```swift
    func testSubtitleOptionsExposeBothAuthoredLanguages() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        XCTAssertEqual(Set(group.options.compactMap { $0.locale?.languageCode }), ["en", "es"])
        XCTAssertEqual(group.options.count, 2)
        XCTAssertTrue(group.options.allSatisfy { !$0.displayName.isEmpty })
        XCTAssertTrue(group.allowsEmptySelection)
    }
```

Source: [code-examples/pilots/uikit-media-v1/history/revision-1/Sources/MediaUIKit.swift:40](../../../code-examples/pilots/uikit-media-v1/history/revision-1/Sources/MediaUIKit.swift#L40); SHA-256 `f6c7ac23f751eefdbfea39c0854ef49ae2d7ffefa54520d3eb781f8508a561bd`.

```swift
    public static func select(language: String, in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
        guard let option = group.options.first(where: { $0.locale?.languageCode == language }) else { return false }
        item.select(option, in: group)
        return true
    }
```

### Correction

Source: [code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift:58](../../../code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift#L58); SHA-256 `1e1fa737af60adfc64f3a3e3fce99735c4c06a9e343d72315d75a8447b80902e`.

```swift
    func testSubtitleOptionsExposeBothAuthoredLanguages() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        for option in group.options {
            print("MEDIA_OPTION name=\(option.displayName) language=\(option.locale?.languageCode ?? "nil") forced=\(option.hasMediaCharacteristic(.containsOnlyForcedSubtitles)) type=\(option.mediaType.rawValue)")
        }
        XCTAssertEqual(Set(group.options.compactMap { $0.locale?.languageCode }), ["en", "es"])
        let full = group.options.filter { !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) }
        let forced = group.options.filter { $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles) }
        XCTAssertEqual(full.count, 2)
        XCTAssertEqual(forced.count, 2)
        XCTAssertEqual(Set(full.compactMap { $0.locale?.languageCode }), ["en", "es"])
        XCTAssertEqual(Set(forced.compactMap { $0.locale?.languageCode }), ["en", "es"])
        XCTAssertTrue(group.options.allSatisfy { !$0.displayName.isEmpty })
        XCTAssertTrue(group.allowsEmptySelection)
    }
```

Source: [code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift:41](../../../code-examples/pilots/uikit-media-v1/Sources/MediaUIKit.swift#L41); SHA-256 `7fd55e418c7253dadb42c1917471513ef75cb5af4a20e47c90b8c3968b0ed3f6`.

```swift
    public static func select(language: String, in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
        guard let option = group.options.first(where: {
            $0.locale?.languageCode == language && !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
        }) else { return false }
        item.select(option, in: group)
        return true
    }
```

Source: [code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift:78](../../../code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift#L78); SHA-256 `1e1fa737af60adfc64f3a3e3fce99735c4c06a9e343d72315d75a8447b80902e`.

```swift
    func testSubtitleSelectionAndOffState() async throws {
        let url = try MediaFixture.write()
        defer { try? FileManager.default.removeItem(at: url) }
        let asset = AVURLAsset(url: url)
        let loaded = try await asset.loadMediaSelectionGroup(for: .legible)
        let group = try XCTUnwrap(loaded)
        let item = AVPlayerItem(asset: asset)
        XCTAssertTrue(MediaConfiguration.select(language: "es", in: group, item: item))
        XCTAssertEqual(MediaConfiguration.selectedLanguage(in: group, item: item), "es")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: group)?.hasMediaCharacteristic(.containsOnlyForcedSubtitles), false)
        item.select(nil, in: group)
        XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: group))
    }
```

### Observed diagnostics

```text
error: -[AccessibilityExamplesTests.MediaUIKitTests testSubtitleOptionsExposeBothAuthoredLanguages] : XCTAssertEqual failed: ("4") is not equal to ("2")
```

Reports: [code-examples/pilots/uikit-media-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-1.json), [code-examples/pilots/uikit-media-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-2.json), [code-examples/pilots/uikit-media-v1/validation/revision-3.json](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

### Candidate skill lesson

Inspect actual options and characteristics. Do not infer one option per authored track or select solely by language. Exact option counts are fixture/runtime observations, not general API guarantees.

### Proposed evaluation

Use a natural question about Spanish subtitles selecting incomplete content. Evaluate distinction between full and forced-only options and preserve authored content. Include assets with different option cardinalities so memorizing four does not pass.

## F08: Object identity used for a String-valued action category

Classification: Model-authored Swift type error in test code.

Library type-check passed, but the XCTest target did not compile: argument type String expected to be an instance of a class or class-constrained type. Zero tests executed. Replacing === with XCTAssertEqual fixed the authored test; production code was unchanged.

### Original code / expectation

Source: [code-examples/pilots/uikit-lifecycle-v1/history/revision-1/Tests/LifecycleUIKitTests.swift:83](../../../code-examples/pilots/uikit-lifecycle-v1/history/revision-1/Tests/LifecycleUIKitTests.swift#L83); SHA-256 `a0f9cb6ebf0182c459a45c719faaf1c0c49980a90635505e1ede2704e6c5e8cd`.

```swift
    func testReadOnlyStateRemovesEditCategoryAndHint() {
        let button = UIButton(type: .system)
        ContextActions.configure(button, editable: true) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 1)
        XCTAssertTrue(button.accessibilityCustomActions?.first?.category === UIAccessibilityCustomAction.editCategory)
        ContextActions.configure(button, editable: false) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 0)
        XCTAssertNil(button.accessibilityHint)
    }
```

### Correction

Source: [code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift:83](../../../code-examples/pilots/uikit-lifecycle-v1/Tests/LifecycleUIKitTests.swift#L83); SHA-256 `5a829cf732a2b099a39c243a834d63f1e9e32eb9a45a7c7318616203a55a0db5`.

```swift
    func testReadOnlyStateRemovesEditCategoryAndHint() {
        let button = UIButton(type: .system)
        ContextActions.configure(button, editable: true) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 1)
        XCTAssertEqual(button.accessibilityCustomActions?.first?.category, UIAccessibilityCustomAction.editCategory)
        ContextActions.configure(button, editable: false) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 0)
        XCTAssertNil(button.accessibilityHint)
    }
```

### Observed diagnostics

```text
error: argument type 'String' expected to be an instance of a class or class-constrained type
```

Reports: [code-examples/pilots/uikit-lifecycle-v1/validation/revision-1.json](../../../code-examples/pilots/uikit-lifecycle-v1/validation/revision-1.json), [code-examples/pilots/uikit-lifecycle-v1/validation/revision-2.json](../../../code-examples/pilots/uikit-lifecycle-v1/validation/revision-2.json).

### Candidate skill lesson

Inspect the actual declaration and compile the test target, not just library code. A successful source type-check cannot establish a runnable test suite.

### Proposed evaluation

Ask for an edit-category assertion. Check correct value equality and require evidence that tests were discovered and executed.

## C01: Initial rotor search missing from a green suite

Revision1 passed22 positive tests. Revision2 added initial/default-predicate coverage and optional handling;23 passed. Do not invent a pre-fix crash that the preserved run did not execute.

Before:

Source: [code-examples/pilots/uikit-semantics-v1/history/revision-1/Sources/UIKitSemantics.swift:79](../../../code-examples/pilots/uikit-semantics-v1/history/revision-1/Sources/UIKitSemantics.swift#L79); SHA-256 `e946914c1988cf8f3596965e85a20f0743f06a45fc02b502d658ba34bd361769`.

```swift
            let current = self.sections.firstIndex { $0 === predicate.currentItem.targetElement }
```

After:

Source: [code-examples/pilots/uikit-semantics-v1/Sources/UIKitSemantics.swift:79](../../../code-examples/pilots/uikit-semantics-v1/Sources/UIKitSemantics.swift#L79); SHA-256 `3e32ee71d21fccc4c074fff4916c4dfebbe7791c0842bdf8d463757337a238e0`.

```swift
            let item: UIAccessibilityCustomRotorItemResult? = predicate.currentItem
            let current = self.sections.firstIndex { $0 === item?.targetElement }
```

Added test:

Source: [code-examples/pilots/uikit-semantics-v1/Tests/UIKitSemanticsTests.swift:151](../../../code-examples/pilots/uikit-semantics-v1/Tests/UIKitSemanticsTests.swift#L151); SHA-256 `65fe2963785845dd5c95160b1e4652285fa9664ab555d219cbe73fdf296a8d37`.

```swift
    @MainActor func testRotorInitialSearchReturnsFirstOrLast() throws {
        let root = SectionRotor(names: ["One", "Two"])
        let rotor = try XCTUnwrap(root.accessibilityCustomRotors?.first)
        let predicate = UIAccessibilityCustomRotorSearchPredicate()
        predicate.searchDirection = .next
        XCTAssertTrue(rotor.itemSearchBlock(predicate)?.targetElement === root.sections[0])
        predicate.searchDirection = .previous
        XCTAssertTrue(rotor.itemSearchBlock(predicate)?.targetElement === root.sections[1])
    }
```
