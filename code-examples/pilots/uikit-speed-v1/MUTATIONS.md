# Deliberate Speed-Control Mutations

Manufactured faults, not spontaneous model failures.

## StaleMetadata

```diff
--- code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift	2026-11-06 07:08:48
+++ code-examples/pilots/uikit-speed-v1/NegativeFixtures/StaleMetadata.swift	2026-11-06 07:08:48
@@ -38 +37,0 @@
-        render()
```

## RepeatedChange

```diff
--- code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift	2026-11-06 07:08:48
+++ code-examples/pilots/uikit-speed-v1/NegativeFixtures/RepeatedChange.swift	2026-11-06 07:08:48
@@ -36 +36 @@
-        guard rate != selectedRate else { return true }
+        // Deliberately emit duplicate changes.
```

## IgnoredDisabled

```diff
--- code-examples/pilots/uikit-speed-v1/Sources/PlaybackSpeed.swift	2026-11-06 07:08:48
+++ code-examples/pilots/uikit-speed-v1/NegativeFixtures/IgnoredDisabled.swift	2026-11-06 07:08:48
@@ -35 +35 @@
-        guard controlsEnabled, Self.rates.contains(rate) else { return false }
+        guard Self.rates.contains(rate) else { return false }
```
