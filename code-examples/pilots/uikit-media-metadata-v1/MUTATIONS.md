# Intentional Metadata Mutations

Manufactured defects, not accidental model failures.

## AllAudioDescribed

```diff
--- code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift	2026-11-05 22:58:52
+++ code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/AllAudioDescribed.swift	2026-11-05 22:58:52
@@ -30 +30 @@
-                describesVideo: option.hasMediaCharacteristic(.describesVideoForAccessibility),
+                describesVideo: true,
```

## NoItemAbsent

```diff
--- code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift	2026-11-05 22:58:52
+++ code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/NoItemAbsent.swift	2026-11-05 22:58:52
@@ -22 +22 @@
-        guard let item else { return .unavailable }
+        guard let item else { return .absent }
```

## SelectionLost

```diff
--- code-examples/pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift	2026-11-05 22:58:52
+++ code-examples/pilots/uikit-media-metadata-v1/NegativeFixtures/SelectionLost.swift	2026-11-05 22:58:52
@@ -32 +32 @@
-                selected: option == selected)
+                selected: false)
```
