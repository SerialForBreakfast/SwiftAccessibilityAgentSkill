# Deliberate Mutation Diffs

Manufactured sensitivity checks, not spontaneous model failures. Zero-context diffs; full files are pinned by manifest.json.

## characteroffsets-negative

Selected assertion: `EditedRotorUIKitTests/testUnicodePrefixProducesCorrectNativeRange`.

```diff
--- code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift	2026-11-05 20:54:09
+++ code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/CharacterOffsets.swift	2026-11-05 20:54:57
@@ -8 +8 @@
-            offset += String(character).utf16.count
+            offset += 1
```

## ignoredoverlap-negative

Selected assertion: `EditedRotorUIKitTests/testOverlapPolicyIsExplicit`.

```diff
--- code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift	2026-11-05 20:54:09
+++ code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/IgnoredOverlap.swift	2026-11-05 20:54:57
@@ -24 +24 @@
-            cursor = valid && !allowOverlaps ? end : next
+            cursor = valid ? end : next
```

## missingrestart-negative

Selected assertion: `EditedRotorUIKitTests/testNewRevisionRestartsRetainedResult`.

```diff
--- code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift	2026-11-05 20:54:09
+++ code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/MissingRestart.swift	2026-11-05 20:54:57
@@ -59 +59 @@
-            if !restart, item?.targetElement === self.textView, let range = item?.targetRange {
+            if item?.targetElement === self.textView, let range = item?.targetRange {
```

## oldrotor-negative

Selected assertion: `EditedRotorUIKitTests/testRetainedOldRotorIsInvalidAfterQueryChange`.

```diff
--- code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift	2026-11-05 20:54:09
+++ code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/OldRotor.swift	2026-11-05 20:54:57
@@ -56 +56 @@
-            guard let self, self.revision == epoch, self.textView.text == text else { return nil }
+            guard let self, self.textView.text == text else { return nil }
```

## staletext-negative

Selected assertion: `EditedRotorUIKitTests/testUnannouncedTextChangeRejectsCachedSearch`.

```diff
--- code-examples/pilots/uikit-edited-rotor-v1/Sources/EditedRotorUIKit.swift	2026-11-05 20:54:09
+++ code-examples/pilots/uikit-edited-rotor-v1/NegativeFixtures/StaleText.swift	2026-11-05 20:54:57
@@ -56 +56 @@
-            guard let self, self.revision == epoch, self.textView.text == text else { return nil }
+            guard let self, self.revision == epoch else { return nil }
```
