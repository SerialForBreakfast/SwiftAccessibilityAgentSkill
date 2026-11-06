# Deliberate Mutation Diffs

Manufactured sensitivity checks, not spontaneous model errors. Zero-context display diffs; full inputs are pinned in manifest.json.

## nolinearization-negative

Selected assertion: `ContrastUIKitTests/testUIKitGrayConversionUsesLinearLuminance`.

```diff
--- code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift	2026-11-05 20:26:59
+++ code-examples/pilots/uikit-contrast-v1/NegativeFixtures/NoLinearization.swift	2026-11-05 20:27:42
@@ -25 +25 @@
-        value <= 0.04045 ? value / 12.92 : pow((value + 0.055) / 1.055, 2.4)
+        value
```

## wrongcolorspace-negative

Selected assertion: `ContrastUIKitTests/testLinearColorSpaceIsConvertedBeforeFormula`.

```diff
--- code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift	2026-11-05 20:26:59
+++ code-examples/pilots/uikit-contrast-v1/NegativeFixtures/WrongColorSpace.swift	2026-11-05 20:27:42
@@ -51 +51 @@
-              let space = CGColorSpace(name: CGColorSpace.sRGB),
+              let space = CGColorSpace(name: CGColorSpace.linearSRGB),
```

## ignoredtraits-negative

Selected assertion: `ContrastUIKitTests/testDynamicColorsUseExplicitStyleAndContrast`.

```diff
--- code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift	2026-11-05 20:26:59
+++ code-examples/pilots/uikit-contrast-v1/NegativeFixtures/IgnoredTraits.swift	2026-11-05 20:27:42
@@ -48 +48 @@
-        let original = color.resolvedColor(with: traits).cgColor
+        let original = color.resolvedColor(with: UITraitCollection(userInterfaceStyle: .light)).cgColor
```

## ignoredalpha-negative

Selected assertion: `ContrastUIKitTests/testTranslucentForegroundAndBackgroundAreRejected`.

```diff
--- code-examples/pilots/uikit-contrast-v1/Sources/ContrastUIKit.swift	2026-11-05 20:26:59
+++ code-examples/pilots/uikit-contrast-v1/NegativeFixtures/IgnoredAlpha.swift	2026-11-05 20:27:42
@@ -49 +49 @@
-        guard original.alpha == 1 else { throw ContrastError.translucent }
+        // Deliberate defect: ignore alpha.
```
