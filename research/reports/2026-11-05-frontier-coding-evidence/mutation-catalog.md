# Deliberate mutation catalog

These29 intentionally broken variants are test-sensitivity evidence, not spontaneous model mistakes. Patches show the exact difference from the current tested source. Full failing assertions remain in the linked native reports. A passing negative check means its specified failure occurred.

## uikit-pilot: row-actions-negative

Mutant: [code-examples/pilots/uikit-v1/NegativeFixtures/SettingsRow.swift](../../../code-examples/pilots/uikit-v1/NegativeFixtures/SettingsRow.swift). Evidence: [native report](../../../code-examples/pilots/uikit-v1/validation/pilot-r2-results.json).

Selected tests: UIKitTests/testSettingsCallbacksAndExposedControls.

```diff
--- tested-source
+++ intentional-mutant
@@ -17,7 +17,7 @@
         helpButton.addAction(UIAction { _ in onHelp() }, for: .touchUpInside)
         // PATCH BEGIN GP26-01
         isAccessibilityElement = false
-        accessibilityElementsHidden = false
+        accessibilityElementsHidden = true
         titleLabel.isAccessibilityElement = false
         downloadSwitch.accessibilityLabel = "Downloads"
         // PATCH END GP26-01
```

## uikit-pilot: cell-state-negative

Mutant: [code-examples/pilots/uikit-v1/NegativeFixtures/OrderCell.swift](../../../code-examples/pilots/uikit-v1/NegativeFixtures/OrderCell.swift). Evidence: [native report](../../../code-examples/pilots/uikit-v1/validation/pilot-r2-results.json).

Selected tests: UIKitTests/testReconfigurationWithoutPrepareForReuse.

```diff
--- tested-source
+++ intentional-mutant
@@ -28,7 +28,7 @@
         titleLabel.text = order.customer
         isAccessibilityElement = true
         accessibilityLabel = order.isPriority ? "Priority order for \(order.customer)" : order.customer
-        accessibilityValue = order.status
+        if order.isPriority { accessibilityValue = order.status }
     }
     // PATCH END GP26-02
 }
```

## uikit-pilot: text-scaling-negative

Mutant: [code-examples/pilots/uikit-v1/NegativeFixtures/CheckoutSummary.swift](../../../code-examples/pilots/uikit-v1/NegativeFixtures/CheckoutSummary.swift). Evidence: [native report](../../../code-examples/pilots/uikit-v1/validation/pilot-r2-results.json).

Selected tests: UIKitTests/testCheckoutCallbackAndResizePrerequisites.

```diff
--- tested-source
+++ intentional-mutant
@@ -12,7 +12,7 @@
         [totalLabel, payButton].forEach(addArrangedSubview)
         // PATCH BEGIN GP26-03
         totalLabel.font = .preferredFont(forTextStyle: .body)
-        totalLabel.adjustsFontForContentSizeCategory = true
+        totalLabel.adjustsFontForContentSizeCategory = false
         totalLabel.numberOfLines = 0
         axis = .vertical
         distribution = .fill
```

## uikit-pilot: compile-label-type-negative

Mutant: [code-examples/pilots/uikit-v1/NegativeFixtures/WrongLabelType.swift](../../../code-examples/pilots/uikit-v1/NegativeFixtures/WrongLabelType.swift). Evidence: [native report](../../../code-examples/pilots/uikit-v1/validation/pilot-r2-results.json).

Selected tests: Compiler diagnostic: label-type-mismatch.

```swift
import UIKit

// Intentional compiler rejection: accessibilityLabel accepts String?, not Int.
@MainActor func invalidLabelType() {
    UILabel().accessibilityLabel = 42
}
```

## uikit-semantics: droppedaction-negative

Mutant: [code-examples/pilots/uikit-semantics-v1/NegativeFixtures/DroppedAction.swift](../../../code-examples/pilots/uikit-semantics-v1/NegativeFixtures/DroppedAction.swift). Evidence: [native report](../../../code-examples/pilots/uikit-semantics-v1/validation/revision-2.json).

Selected tests: UIKitSemanticsTests/testCustomActionHasNameAndInvokesOneCallback.

```diff
--- tested-source
+++ intentional-mutant
@@ -55,7 +55,7 @@
     private func performArchive() -> Bool {
         guard !archived else { return false }
         archived = true
-        onArchive()
+        // Intentional defect: callback omitted.
         return true
     }
 }
```

## uikit-semantics: wrongrotordirection-negative

Mutant: [code-examples/pilots/uikit-semantics-v1/NegativeFixtures/WrongRotorDirection.swift](../../../code-examples/pilots/uikit-semantics-v1/NegativeFixtures/WrongRotorDirection.swift). Evidence: [native report](../../../code-examples/pilots/uikit-semantics-v1/validation/revision-2.json).

Selected tests: UIKitSemanticsTests/testRotorNextAndPreviousReturnCorrectIdentity.

```diff
--- tested-source
+++ intentional-mutant
@@ -79,7 +79,7 @@
             let item: UIAccessibilityCustomRotorItemResult? = predicate.currentItem
             let current = self.sections.firstIndex { $0 === item?.targetElement }
             let index: Int
-            if predicate.searchDirection == .next { index = current.map { $0 + 1 } ?? 0 }
+            if predicate.searchDirection == .next { index = current.map { $0 - 1 } ?? 0 }
             else { index = current.map { $0 - 1 } ?? self.sections.count - 1 }
             guard self.sections.indices.contains(index) else { return nil }
             return UIAccessibilityCustomRotorItemResult(targetElement: self.sections[index], targetRange: nil)
```

## uikit-semantics: losttraits-negative

Mutant: [code-examples/pilots/uikit-semantics-v1/NegativeFixtures/LostTraits.swift](../../../code-examples/pilots/uikit-semantics-v1/NegativeFixtures/LostTraits.swift). Evidence: [native report](../../../code-examples/pilots/uikit-semantics-v1/validation/revision-2.json).

Selected tests: UIKitSemanticsTests/testSelectedTraitPreservesOtherTraits.

```diff
--- tested-source
+++ intentional-mutant
@@ -5,7 +5,7 @@
         button.accessibilityLabel = "Bookmark"
         button.accessibilityHint = hint
         button.accessibilityValue = selected ? "Saved" : "Not saved"
-        if selected { button.accessibilityTraits.insert(.selected) }
+        if selected { button.accessibilityTraits = .selected }
         else { button.accessibilityTraits.remove(.selected) }
     }
```

## uikit-dynamic: staleaction-negative

Mutant: [code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/StaleAction.swift](../../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/StaleAction.swift). Evidence: [native report](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json).

Selected tests: DynamicUIKitTests/testRetainedOldActionCannotAffectReusedView.

```diff
--- tested-source
+++ intentional-mutant
@@ -88,7 +88,7 @@
         }
     }
     private func perform(token: Int, id: String, operation: MessageOperation) -> Bool {
-        guard token == revision, active else { return false }
+        guard active else { return false }
         onAction(id, operation)
         return true
     }
```

## uikit-dynamic: duplicatecallback-negative

Mutant: [code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/DuplicateCallback.swift](../../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/DuplicateCallback.swift). Evidence: [native report](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json).

Selected tests: DynamicUIKitTests/testCustomActionsAreIndependentAndNamed.

```diff
--- tested-source
+++ intentional-mutant
@@ -90,6 +90,7 @@
     private func perform(token: Int, id: String, operation: MessageOperation) -> Bool {
         guard token == revision, active else { return false }
         onAction(id, operation)
+        onAction(id, operation)
         return true
     }
 }
```

## uikit-dynamic: missingelements-negative

Mutant: [code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/MissingElements.swift](../../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/MissingElements.swift). Evidence: [native report](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json).

Selected tests: DynamicUIKitTests/testReorderPreservesIdentityAndChangesSearchOrder.

```diff
--- tested-source
+++ intentional-mutant
@@ -40,7 +40,7 @@
         ordered.forEach(addSubview)
         byID = next
         labels = ordered
-        accessibilityElements = ordered
+        accessibilityElements = []
         return true
     }
 }
```

## uikit-dynamic: retainedremoved-negative

Mutant: [code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/RetainedRemoved.swift](../../../code-examples/pilots/uikit-dynamic-v1/NegativeFixtures/RetainedRemoved.swift). Evidence: [native report](../../../code-examples/pilots/uikit-dynamic-v1/validation/revision-2.json).

Selected tests: DynamicUIKitTests/testRemovedElementIsNotRetainedByIndexOrContainer.

```diff
--- tested-source
+++ intentional-mutant
@@ -38,7 +38,7 @@
         }
         labels.forEach { $0.removeFromSuperview() }
         ordered.forEach(addSubview)
-        byID = next
+        byID.merge(next) { _, new in new }
         labels = ordered
         accessibilityElements = ordered
         return true
```

## uikit-text: wrongrange-negative

Mutant: [code-examples/pilots/uikit-text-v1/NegativeFixtures/WrongRange.swift](../../../code-examples/pilots/uikit-text-v1/NegativeFixtures/WrongRange.swift). Evidence: [native report](../../../code-examples/pilots/uikit-text-v1/validation/revision-1.json).

Selected tests: TextUIKitTests/testUnicodePrefixProducesExactSelectedText.

```diff
--- tested-source
+++ intentional-mutant
@@ -20,7 +20,7 @@
                 : current.map { $0 - 1 } ?? self.matches.count - 1
             guard self.matches.indices.contains(index) else { return nil }
             let match = self.matches[index]
-            guard let start = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location),
+            guard let start = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location + 1),
                   let end = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location + match.length),
                   let range = self.textView.textRange(from: start, to: end) else { return nil }
             return UIAccessibilityCustomRotorItemResult(targetElement: self.textView, targetRange: range)
```

## uikit-text: stalematches-negative

Mutant: [code-examples/pilots/uikit-text-v1/NegativeFixtures/StaleMatches.swift](../../../code-examples/pilots/uikit-text-v1/NegativeFixtures/StaleMatches.swift). Evidence: [native report](../../../code-examples/pilots/uikit-text-v1/validation/revision-1.json).

Selected tests: TextUIKitTests/testReplacingTextDiscardsOldMatches.

```diff
--- tested-source
+++ intentional-mutant
@@ -30,7 +30,7 @@
     @discardableResult public func replace(text: String, query: String) -> Bool {
         guard !query.isEmpty else { return false }
         textView.text = text
-        matches.removeAll()
+        // Intentional defect: previous matches retained.
         let document = text as NSString
         var offset = 0
         while offset < document.length {
```

## uikit-text: missingcategory-negative

Mutant: [code-examples/pilots/uikit-text-v1/NegativeFixtures/MissingCategory.swift](../../../code-examples/pilots/uikit-text-v1/NegativeFixtures/MissingCategory.swift). Evidence: [native report](../../../code-examples/pilots/uikit-text-v1/validation/revision-1.json).

Selected tests: TextUIKitTests/testEditCategoryConfigurationAndDefault.

```diff
--- tested-source
+++ intentional-mutant
@@ -46,7 +46,7 @@
 @MainActor public enum EditActionFactory {
     public static func make(title: NSAttributedString, handler: @escaping UIAccessibilityCustomAction.Handler) -> UIAccessibilityCustomAction {
         let action = UIAccessibilityCustomAction(attributedName: title, actionHandler: handler)
-        action.category = UIAccessibilityCustomAction.editCategory
+        action.category = nil
         return action
     }
 }
```

## uikit-preferences: ignoredmotion-negative

Mutant: [code-examples/pilots/uikit-preferences-v1/NegativeFixtures/IgnoredMotion.swift](../../../code-examples/pilots/uikit-preferences-v1/NegativeFixtures/IgnoredMotion.swift). Evidence: [native report](../../../code-examples/pilots/uikit-preferences-v1/validation/revision-1.json).

Selected tests: PreferenceUIKitTests/testReducedMotionUsesImmediateTransition.

```diff
--- tested-source
+++ intentional-mutant
@@ -3,7 +3,7 @@
 @MainActor
 public enum MotionPolicy {
     public static func duration(reduceMotion: Bool) -> TimeInterval {
-        reduceMotion ? 0 : 0.25
+        reduceMotion ? 0.25 : 0.25
     }
 
     public static func currentDuration() -> TimeInterval {
```

## uikit-preferences: stalehint-negative

Mutant: [code-examples/pilots/uikit-preferences-v1/NegativeFixtures/StaleHint.swift](../../../code-examples/pilots/uikit-preferences-v1/NegativeFixtures/StaleHint.swift). Evidence: [native report](../../../code-examples/pilots/uikit-preferences-v1/validation/revision-1.json).

Selected tests: PreferenceUIKitTests/testRecoveryRemovesStaleErrorAndHint.

```diff
--- tested-source
+++ intentional-mutant
@@ -32,6 +32,7 @@
         message.text = error.map { "Error: \($0)" } ?? "Ready to submit"
         message.accessibilityLabel = message.text
         submit.isEnabled = error == nil
+        if error == nil { return }
         submit.accessibilityHint = error.map { "Correct the error before submitting: \($0)" }
     }
```

## uikit-containers: wrongspan-negative

Mutant: [code-examples/pilots/uikit-containers-v1/NegativeFixtures/WrongSpan.swift](../../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/WrongSpan.swift). Evidence: [native report](../../../code-examples/pilots/uikit-containers-v1/validation/revision-2.json).

Selected tests: ContainerUIKitTests/testSpanningCellResolvesEveryCoveredCoordinate.

```diff
--- tested-source
+++ intentional-mutant
@@ -64,7 +64,7 @@
         guard row >= 0, row < rows, column >= 0, column < columns else { return nil }
         return cells.first {
             NSLocationInRange(row, $0.accessibilityRowRange()) &&
-            NSLocationInRange(column, $0.accessibilityColumnRange())
+            column == $0.accessibilityColumnRange().location
         }
     }
```

## uikit-containers: stalemodal-negative

Mutant: [code-examples/pilots/uikit-containers-v1/NegativeFixtures/StaleModal.swift](../../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/StaleModal.swift). Evidence: [native report](../../../code-examples/pilots/uikit-containers-v1/validation/revision-2.json).

Selected tests: ContainerUIKitTests/testEscapeDismissesAndClearsModalState.

```diff
--- tested-source
+++ intentional-mutant
@@ -109,7 +109,7 @@
         isOpen = false
         isHidden = true
         accessibilityElementsHidden = true
-        accessibilityViewIsModal = false
+        accessibilityViewIsModal = true
         onDismiss()
         return true
     }
```

## uikit-containers: ignoredenabled-negative

Mutant: [code-examples/pilots/uikit-containers-v1/NegativeFixtures/IgnoredEnabled.swift](../../../code-examples/pilots/uikit-containers-v1/NegativeFixtures/IgnoredEnabled.swift). Evidence: [native report](../../../code-examples/pilots/uikit-containers-v1/validation/revision-2.json).

Selected tests: ContainerUIKitTests/testDisabledActivationDoesNotInvokeHandler.

```diff
--- tested-source
+++ intentional-mutant
@@ -131,7 +131,7 @@
     public required init?(coder: NSCoder) { fatalError("Programmatic example") }
 
     public override func accessibilityActivate() -> Bool {
-        guard isEnabled else { return false }
+        // Deliberately omit enabled guard.
         return perform()
     }
 }
```

## uikit-reuse: staleselection-negative

Mutant: [code-examples/pilots/uikit-reuse-v1/NegativeFixtures/StaleSelection.swift](../../../code-examples/pilots/uikit-reuse-v1/NegativeFixtures/StaleSelection.swift). Evidence: [native report](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-3.json).

Selected tests: ReuseUIKitTests/testReconfigureClearsSelectedStateWithoutLosingOtherTraits.

```diff
--- tested-source
+++ intentional-mutant
@@ -22,7 +22,7 @@
         accessibilityAttributedLabel = NSAttributedString(string: title, attributes: [.accessibilitySpeechLanguage: language])
         accessibilityValue = saved ? "Saved" : "Not saved"
         if saved { accessibilityTraits.insert(.selected) }
-        else { accessibilityTraits.remove(.selected) }
+        else { accessibilityTraits.insert(.selected) }
         accessibilityHint = removable ? "Remove is available in actions" : nil
         accessibilityCustomActions = removable ? [UIAccessibilityCustomAction(name: "Remove") { [weak self] _ in
             guard let self, self.generation == token, let remove = self.onRemove else { return false }
```

## uikit-reuse: staleidentity-negative

Mutant: [code-examples/pilots/uikit-reuse-v1/NegativeFixtures/StaleIdentity.swift](../../../code-examples/pilots/uikit-reuse-v1/NegativeFixtures/StaleIdentity.swift). Evidence: [native report](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-3.json).

Selected tests: ReuseUIKitTests/testRetainedActionRejectsReconfiguredIdentity.

```diff
--- tested-source
+++ intentional-mutant
@@ -25,7 +25,7 @@
         else { accessibilityTraits.remove(.selected) }
         accessibilityHint = removable ? "Remove is available in actions" : nil
         accessibilityCustomActions = removable ? [UIAccessibilityCustomAction(name: "Remove") { [weak self] _ in
-            guard let self, self.generation == token, let remove = self.onRemove else { return false }
+            guard let self, let remove = self.onRemove else { return false }
             remove(id)
             return true
         }] : []
```

## uikit-reuse: wrongnotification-negative

Mutant: [code-examples/pilots/uikit-reuse-v1/NegativeFixtures/WrongNotification.swift](../../../code-examples/pilots/uikit-reuse-v1/NegativeFixtures/WrongNotification.swift). Evidence: [native report](../../../code-examples/pilots/uikit-reuse-v1/validation/revision-3.json).

Selected tests: ReuseUIKitTests/testLayoutUpdatePreservesTargetIdentity.

```diff
--- tested-source
+++ intentional-mutant
@@ -85,7 +85,7 @@
     public let target: UIView?
 
     public static func layout(target: UIView?) -> Self {
-        Self(notification: .layoutChanged, target: target)
+        Self(notification: .screenChanged, target: target)
     }
 
     public static func screen(target: UIView?) -> Self {
```

## uikit-media: hiddencontrols-negative

Mutant: [code-examples/pilots/uikit-media-v1/NegativeFixtures/HiddenControls.swift](../../../code-examples/pilots/uikit-media-v1/NegativeFixtures/HiddenControls.swift). Evidence: [native report](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

Selected tests: MediaUIKitTests/testNativeControllerPreservesControlsAndAutomaticSelection.

```diff
--- tested-source
+++ intentional-mutant
@@ -7,7 +7,7 @@
     public static func controller(player: AVPlayer) -> AVPlayerViewController {
         let controller = AVPlayerViewController()
         controller.player = player
-        controller.showsPlaybackControls = true
+        controller.showsPlaybackControls = false
         controller.requiresLinearPlayback = false
         return controller
     }
```

## uikit-media: wronglanguage-negative

Mutant: [code-examples/pilots/uikit-media-v1/NegativeFixtures/WrongLanguage.swift](../../../code-examples/pilots/uikit-media-v1/NegativeFixtures/WrongLanguage.swift). Evidence: [native report](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

Selected tests: MediaUIKitTests/testSubtitleSelectionAndOffState.

```diff
--- tested-source
+++ intentional-mutant
@@ -40,7 +40,7 @@
     @discardableResult
     public static func select(language: String, in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
         guard let option = group.options.first(where: {
-            $0.locale?.languageCode == language && !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
+            $0.locale?.languageCode == "en" && !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
         }) else { return false }
         item.select(option, in: group)
         return true
```

## uikit-media: staleposition-negative

Mutant: [code-examples/pilots/uikit-media-v1/NegativeFixtures/StalePosition.swift](../../../code-examples/pilots/uikit-media-v1/NegativeFixtures/StalePosition.swift). Evidence: [native report](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

Selected tests: MediaUIKitTests/testUnavailableTimelineResetsPreviousState.

```diff
--- tested-source
+++ intentional-mutant
@@ -26,7 +26,7 @@
             slider.minimumValue = 0
             slider.maximumValue = 1
             slider.value = 0
-            slider.accessibilityValue = "Position unavailable"
+            // Deliberately retain previous position.
             return
         }
         let value = min(max(elapsed, 0), duration)
```

## uikit-media: forcedonly-negative

Mutant: [code-examples/pilots/uikit-media-v1/NegativeFixtures/ForcedOnly.swift](../../../code-examples/pilots/uikit-media-v1/NegativeFixtures/ForcedOnly.swift). Evidence: [native report](../../../code-examples/pilots/uikit-media-v1/validation/revision-3.json).

Selected tests: MediaUIKitTests/testSubtitleSelectionAndOffState.

```diff
--- tested-source
+++ intentional-mutant
@@ -40,7 +40,7 @@
     @discardableResult
     public static func select(language: String, in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
         guard let option = group.options.first(where: {
-            $0.locale?.languageCode == language && !$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
+            $0.locale?.languageCode == language && $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
         }) else { return false }
         item.select(option, in: group)
         return true
```

## uikit-lifecycle: wrongnotification-negative

Mutant: [code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/WrongNotification.swift](../../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/WrongNotification.swift). Evidence: [native report](../../../code-examples/pilots/uikit-lifecycle-v1/validation/revision-2.json).

Selected tests: LifecycleUIKitTests/testInitialMotionReadAndNotificationRefresh.

```diff
--- tested-source
+++ intentional-mutant
@@ -27,7 +27,7 @@
     public func start() {
         guard observation == nil else { return }
         reduceMotion = read()
-        let token = center.addObserver(forName: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil, queue: .main) { [weak self] _ in
+        let token = center.addObserver(forName: UIAccessibility.voiceOverStatusDidChangeNotification, object: nil, queue: .main) { [weak self] _ in
             // The explicit main operation queue is the isolation boundary.
             MainActor.assumeIsolated { self?.refresh() }
         }
```

## uikit-lifecycle: unstopped-negative

Mutant: [code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/UnstoppedObserver.swift](../../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/UnstoppedObserver.swift). Evidence: [native report](../../../code-examples/pilots/uikit-lifecycle-v1/validation/revision-2.json).

Selected tests: LifecycleUIKitTests/testStopRemovesObserverAndRestartRefreshes.

```diff
--- tested-source
+++ intentional-mutant
@@ -34,7 +34,7 @@
         observation = Observation(center: center, token: token)
     }
 
-    public func stop() { observation = nil }
+    public func stop() { }
     private func refresh() { reduceMotion = read() }
 }
```

## uikit-lifecycle: staleedit-negative

Mutant: [code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/StaleEditAction.swift](../../../code-examples/pilots/uikit-lifecycle-v1/NegativeFixtures/StaleEditAction.swift). Evidence: [native report](../../../code-examples/pilots/uikit-lifecycle-v1/validation/revision-2.json).

Selected tests: LifecycleUIKitTests/testReadOnlyStateRemovesEditCategoryAndHint.

```diff
--- tested-source
+++ intentional-mutant
@@ -55,7 +55,7 @@
             button.accessibilityCustomActions = [action]
             button.accessibilityHint = "Edit is available in actions"
         } else {
-            button.accessibilityCustomActions = []
+            // Deliberately retain edit actions.
             button.accessibilityHint = nil
         }
     }
```
