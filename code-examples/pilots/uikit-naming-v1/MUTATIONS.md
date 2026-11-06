# Deliberate Mutation Diffs

These are intentional sensitivity checks, not spontaneous model failures. Original and mutated files are pinned by manifest.json.

## exposeddecoration-negative

Selected assertion: `NamingUIKitTests/testDecorationIsExplicitlyExcluded`.

```diff
--- code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift	2026-11-05 19:59:14
+++ code-examples/pilots/uikit-naming-v1/NegativeFixtures/ExposedDecoration.swift	2026-11-05 19:59:44
@@ -26,7 +26,7 @@
         isAccessibilityElement = false
         accessibilityElementsHidden = false
         decoration.text = "*"
-        decoration.isAccessibilityElement = false
+        decoration.isAccessibilityElement = true
         titleLabel.text = title
         titleLabel.isAccessibilityElement = true
         titleLabel.accessibilityLabel = nil
```

## hiddencontrols-negative

Selected assertion: `NamingUIKitTests/testContainerPreservesIndependentControls`.

```diff
--- code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift	2026-11-05 19:59:14
+++ code-examples/pilots/uikit-naming-v1/NegativeFixtures/HiddenControls.swift	2026-11-05 19:59:44
@@ -24,7 +24,7 @@
                    onOpen: @escaping () -> Void, onSave: @escaping () -> Void) {
         // This example owns these properties; it never collapses its action subtree.
         isAccessibilityElement = false
-        accessibilityElementsHidden = false
+        accessibilityElementsHidden = true
         decoration.text = "*"
         decoration.isAccessibilityElement = false
         titleLabel.text = title
```

## stalenames-negative

Selected assertion: `NamingUIKitTests/testReconfigurationReplacesNamesWithoutReuseCallback`.

```diff
--- code-examples/pilots/uikit-naming-v1/Sources/NamingUIKit.swift	2026-11-05 19:59:14
+++ code-examples/pilots/uikit-naming-v1/NegativeFixtures/StaleNames.swift	2026-11-05 19:59:44
@@ -34,7 +34,7 @@
         saveButton.isAccessibilityElement = true
         openButton.setTitle(openTitle, for: .normal)
         saveButton.setTitle(saveTitle, for: .normal)
-        openButton.accessibilityLabel = openName
+        if openButton.accessibilityLabel == nil { openButton.accessibilityLabel = openName }
         saveButton.accessibilityLabel = saveName
         openHandler = onOpen
         saveHandler = onSave
```
