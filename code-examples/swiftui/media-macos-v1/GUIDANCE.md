# SwiftUI media selection: macOS

Use this example only for explicit media choices and asynchronous item ownership.
Read Sources/MediaSelection.swift on request; tests are opt-in. It uses a real
AVPlayerItem group and does not infer accessibility semantics from view construction.
Reload explicitly after replacing the player item. Current selection is read from
AVFoundation; do not silently disable automatic media preferences.
