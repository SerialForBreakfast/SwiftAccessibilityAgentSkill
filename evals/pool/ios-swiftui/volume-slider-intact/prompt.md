iOS 26.0, SwiftUI.

Our release checklist has an accessibility pass for every settings screen, and the Listening screen is next. Can you go over the volume slider for VoiceOver and make whatever changes it needs? It saves to the listener's profile through `save`, and the visible percentage next to "Volume" is what support tells customers to read back.

Keep `ListeningSettings`, `volume`, `range`, `step`, `volumeBinding`, `setVolume(_:)`, `volumeText`, `save` and `ListeningSettingsView(settings:)` with their current names and types.
