# Deliberate Mutation Diffs

Manufactured sensitivity checks, not spontaneous model errors. Zero-context diffs avoid whitespace-only context lines; full files are pinned by manifest.json.

## singleline-negative

Selected assertion: `ChoiceUIKitTests/testMultilinePolicyReplacesShrinkToFit`.

```diff
--- code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift	2026-11-05 20:18:46
+++ code-examples/pilots/uikit-choice-v1/NegativeFixtures/SingleLine.swift	2026-11-05 20:19:21
@@ -31 +31 @@
-            label.numberOfLines = 0
+            label.numberOfLines = 1
```

## fixedfont-negative

Selected assertion: `ChoiceUIKitTests/testFontsMatchEffectiveLargeTextEnvironment`.

```diff
--- code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift	2026-11-05 20:18:46
+++ code-examples/pilots/uikit-choice-v1/NegativeFixtures/FixedFont.swift	2026-11-05 20:19:21
@@ -35 +35 @@
-            label.font = .preferredFont(forTextStyle: .body, compatibleWith: label.traitCollection)
+            label.font = .systemFont(ofSize: 17)
```

## staleselection-negative

Selected assertion: `ChoiceUIKitTests/testDeselectionClearsEveryOwnedSelectionCue`.

```diff
--- code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift	2026-11-05 20:18:46
+++ code-examples/pilots/uikit-choice-v1/NegativeFixtures/StaleSelection.swift	2026-11-05 20:19:21
@@ -43 +43 @@
-        else { accessibilityTraits.remove(.selected) }
+        else { /* deliberate stale selected trait */ }
```

## clobberedtraits-negative

Selected assertion: `ChoiceUIKitTests/testSelectionUpdatesPreserveUnrelatedTraits`.

```diff
--- code-examples/pilots/uikit-choice-v1/Sources/ChoiceUIKit.swift	2026-11-05 20:18:46
+++ code-examples/pilots/uikit-choice-v1/NegativeFixtures/ClobberedTraits.swift	2026-11-05 20:19:21
@@ -42 +42 @@
-        if chosen { accessibilityTraits.insert(.selected) }
+        if chosen { accessibilityTraits = .selected }
```
