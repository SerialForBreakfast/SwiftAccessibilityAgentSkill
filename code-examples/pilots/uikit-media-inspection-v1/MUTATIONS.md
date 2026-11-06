# Deliberate Media Inspection Mutations

These are manufactured defects, not spontaneous model failures.

## LoadedAsSeekable

```diff
--- code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift	2026-11-05 21:50:23
+++ code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/LoadedAsSeekable.swift	2026-11-05 21:50:57
@@ -39 +39 @@
-        self.seekable = seekable
+        self.seekable = loaded
```

## FullMeansReady

```diff
--- code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift	2026-11-05 21:50:23
+++ code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/FullMeansReady.swift	2026-11-05 21:50:57
@@ -43 +43 @@
-        self.likelyToKeepUp = likelyToKeepUp
+        self.likelyToKeepUp = bufferFull
```

## InferredLive

```diff
--- code-examples/pilots/uikit-media-inspection-v1/Sources/MediaInspection.swift	2026-11-05 21:50:23
+++ code-examples/pilots/uikit-media-inspection-v1/NegativeFixtures/InferredLive.swift	2026-11-05 21:50:57
@@ -38 +38 @@
-        self.kind = kind
+        self.kind = duration?.isIndefinite == true ? .live : kind
```
