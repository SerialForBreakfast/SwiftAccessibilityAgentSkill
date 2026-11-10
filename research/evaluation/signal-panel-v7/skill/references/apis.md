# Verified APIs

These forms typecheck against the iOS, macOS and tvOS 26 SDKs, except where a line names its platforms. Prefer them over guessed members. If something you need is not here or in the supplied code, say what you need instead of inventing it.

## AVFoundation (all three platforms)

```swift
let group: AVMediaSelectionGroup? = try await asset.loadMediaSelectionGroup(for: .legible)   // also .audible
group.options                                   // [AVMediaSelectionOption]
group.allowsEmptySelection                      // Bool; Off is valid only when true
group.defaultOption                             // AVMediaSelectionOption?
AVMediaSelectionGroup.mediaSelectionOptions(from: group.options, filteredAndSortedAccordingToPreferredLanguages: Locale.preferredLanguages)
AVMediaSelectionGroup.mediaSelectionOptions(from: group.options, withoutMediaCharacteristics: [.containsOnlyForcedSubtitles])
option.displayName                              // String, not unique
option.extendedLanguageTag                      // String?, e.g. "en"
option.locale                                   // Locale?
option.mediaType                                // AVMediaType
option.hasMediaCharacteristic(.describesVideoForAccessibility)  // also .containsOnlyForcedSubtitles, .transcribesSpokenDialogForAccessibility
option.isPlayable
item.select(option, in: group)                  // nil option = Off
item.selectMediaOptionAutomatically(in: group)
item.currentMediaSelection.selectedMediaOption(in: group)       // AVMediaSelectionOption?
player.currentItem                              // AVPlayerItem?
player.replaceCurrentItem(with: newItem)
```

There is no `persistentID`, `identifier`, `unicodeLanguageIdentifier` or `isDescribed` on `AVMediaSelectionOption`. `AVMutableMovie` and `AVMutableMovieTrack` are iOS and macOS only (see [media](media.md)).

## UIKit (iOS and tvOS)

```swift
button.addAction(UIAction(identifier: .init("primary")) { _ in }, for: .primaryActionTriggered)
button.removeAction(identifiedBy: .init("primary"), for: .primaryActionTriggered)
button.sendActions(for: .primaryActionTriggered)     // also .touchUpInside
button.actions(forTarget: target, forControlEvent: .touchUpInside)   // [String]? selector names; not UIActions
button.setTitle("Play", for: .normal); button.title(for: .normal)
let action = UIAccessibilityCustomAction(name: "Archive") { _ in true }
action.actionHandler?(action)                        // invoke a retained closure-based action
action.category = UIAccessibilityCustomAction.editCategory   // String?; nil clears
view.accessibilityCustomActions = [action]
view.accessibilityTraits.insert(.selected); view.accessibilityTraits.remove(.selected)
UIAccessibility.post(notification: .screenChanged, argument: target)
```

## AppKit (macOS)

```swift
button.setAccessibilityLabel("Save"); _ = button.accessibilityLabel()
button.setAccessibilityHelp(nil)
view.setAccessibilityCustomActions([NSAccessibilityCustomAction(name: "Archive") { true }])
let custom = view.accessibilityCustomActions()?.first; _ = custom?.handler?()
NSAccessibilityCustomAction(name: "Archive", target: self, selector: #selector(archive))
button.target = self; button.action = #selector(activate); button.performClick(nil)
let accepted: Bool = window.makeFirstResponder(view)   // false = refused
view.window; view.acceptsFirstResponder
```

## SwiftUI

```swift
.sheet(item: $presented, onDismiss: { … }) { item in … }   // item: Identifiable
.sheet(isPresented: $showing, onDismiss: { … }) { … }
@Environment(\.accessibilityReduceMotion) var reduceMotion
.accessibilityAction(named: "Archive") { … }
.accessibilityAdjustableAction { direction in … }        // .increment / .decrement
```

## XCTest and concurrency

- Mark test classes or methods `@MainActor` when they touch `@MainActor` types. Do not read main-actor state from a `nonisolated` context or a detached task.
- Async tests use `func test…() async throws`.
- Use `throw XCTSkip("needs …")` for a missing fixture.
- Use `try XCTUnwrap(x)` instead of `guard … else { return }`.
- An enum with a non-`Equatable` payload cannot synthesize `Equatable`. Match it with `if case .noGroup = state {} else { XCTFail() }`.
