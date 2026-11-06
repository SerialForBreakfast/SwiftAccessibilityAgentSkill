# Deliberate Mutation Diffs

Five current sensitivity checks, separate from the observed revision2 regression. Zero-context diffs; full inputs are pinned by manifest.json.

## lostbackground-negative

Selected assertion: `ModalUIKitTests/testBackgroundRestoresBothOriginalValues`.

```diff
--- code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift	2026-11-05 20:44:00
+++ code-examples/pilots/uikit-modal-v1/NegativeFixtures/LostBackground.swift	2026-11-05 20:44:00
@@ -76 +76 @@
-        background?.accessibilityElementsHidden = priorHidden
+        background?.accessibilityElementsHidden = false
```

## earlynotification-negative

Selected assertion: `ModalUIKitTests/testNotificationWaitsForCompletionAndUsesCurrentTarget`.

```diff
--- code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift	2026-11-05 20:44:00
+++ code-examples/pilots/uikit-modal-v1/NegativeFixtures/EarlyNotification.swift	2026-11-05 20:44:00
@@ -62,0 +63 @@
+        post(.screenChanged, returnTarget)
```

## stalecompletion-negative

Selected assertion: `ModalUIKitTests/testOldCompletionCannotCloseReopenedPanel`.

```diff
--- code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift	2026-11-05 20:44:00
+++ code-examples/pilots/uikit-modal-v1/NegativeFixtures/StaleCompletion.swift	2026-11-05 20:44:00
@@ -65 +65 @@
-            guard let self, self.state == .closing, self.generation == token else { return }
+            guard let self, self.state == .closing else { return }
```

## ignoreddismissguard-negative

Selected assertion: `ModalUIKitTests/testOrdinaryCloseAndEscapeShareDismissalGuard`.

```diff
--- code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift	2026-11-05 20:44:00
+++ code-examples/pilots/uikit-modal-v1/NegativeFixtures/IgnoredDismissGuard.swift	2026-11-05 20:44:00
@@ -61 +61 @@
-        guard state == .open, canDismiss else { return false }
+        guard state == .open else { return false }
```

## detachedtarget-negative

Selected assertion: `ModalUIKitTests/testRetainedButRemovedTargetPostsNil`.

```diff
--- code-examples/pilots/uikit-modal-v1/Sources/ModalUIKit.swift	2026-11-05 20:44:00
+++ code-examples/pilots/uikit-modal-v1/NegativeFixtures/DetachedTarget.swift	2026-11-05 20:44:00
@@ -72,4 +72 @@
-        let target = returnTarget.flatMap { candidate -> UIView? in
-            guard let background, !priorHidden, candidate.isDescendant(of: background) else { return nil }
-            return candidate
-        }
+        let target = returnTarget
```
