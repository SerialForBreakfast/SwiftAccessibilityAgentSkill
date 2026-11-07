# SwiftUI media selection: macOS

This revision binds every choice, including Off, to the displayed item/snapshot.
Keep existing filtered native selections distinct from Off. Use explicit reload
after external item changes; no automatic native observation is claimed. Task
cancellation is cooperative; explicit store.cancel() invalidates ownership now.
SwiftUI task identity includes the store. Examples/contracts are opt-in.
