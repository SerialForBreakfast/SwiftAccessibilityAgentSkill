# Captions, audio and described video

## Decide

- **A picker that only changes a local value changes nothing on screen.** The fix must write the playing item:
  - `item.select(option, in: group)` to choose;
  - `item.select(nil, in: group)` for Off, only when `group.allowsEmptySelection`.
  - Then read back with `item.currentMediaSelection.selectedMediaOption(in: group)`.
- **Changing captions keeps the audio choice.** Never reset the other group or player settings.
- **Keep the option, not a made-up ID.** `AVMediaSelectionOption` has no persistent ID member. Keep the option object, or derive IDs from its index in `group.options`.
  - Language and `displayName` describe an option but need not be unique.
  - Identify described audio with `option.hasMediaCharacteristic(.describesVideoForAccessibility)`, never by name or language.
- **Distinct states:**
  - no current item;
  - loading;
  - failed load (allow retry);
  - loaded with no such group;
  - loaded with options.
  - Report each separately. A current choice that is not in your list is "other", not Off.
  - Inspecting options is read-only: it never calls `select`.
- **Validate before writing.** An unknown or retired choice leaves the current selection unchanged.
- **Every setter belongs to the item and load that produced it.**
  - A reload of the same item, a cancellation, or a replaced item retires earlier bindings and completions.
  - An old Off, choice, success or error must not change newer state. Capture `let ticket = generation, owner = item` when you build the binding or start the load, and check both when it fires.
- **Chapters:**
  - adjust moves to the neighbouring chapter start;
  - at the first or last chapter stay put; with no chapters do nothing;
  - ordinary tap-to-play stays wired separately; accessibility activation is not a replacement for it.

## Test fixture: real selection groups without a media file (iOS and macOS)

An in-memory movie with empty tracks has real `AVMediaSelectionGroup`s that `AVPlayerItem` can select and read back:

```swift
import AVFoundation

/// Legible: "eng", "fra". Audible: "eng" ordinary, "eng" described.
func makeMediaItem() async throws -> (AVPlayerItem, legible: AVMediaSelectionGroup, audible: AVMediaSelectionGroup) {
    let movie = AVMutableMovie()
    for code in ["eng", "fra"] {
        let track = movie.addMutableTrack(withMediaType: .subtitle, copySettingsFrom: nil, options: nil)!
        track.languageCode = code; track.alternateGroupID = 1      // ISO 639-2 codes
    }
    for described in [false, true] {
        let track = movie.addMutableTrack(withMediaType: .audio, copySettingsFrom: nil, options: nil)!
        track.languageCode = "eng"; track.alternateGroupID = 2
        if described {
            let tag = AVMutableMetadataItem()
            tag.keySpace = .quickTimeUserData; tag.key = "tagc" as NSString
            tag.value = "public.accessibility.describes-video" as NSString
            track.metadata = [tag]
        }
    }
    let legible = try await movie.loadMediaSelectionGroup(for: .legible)
    let audible = try await movie.loadMediaSelectionGroup(for: .audible)
    return (AVPlayerItem(asset: movie), try XCTUnwrap(legible), try XCTUnwrap(audible))
}
```

- **Which fixture is which:** you built the tracks, so you know their order. `audible.options[0]` is ordinary and `audible.options[1]` is described. Expect results from that independent knowledge. Never pick the "described" fixture with the predicate you are testing.
- **tvOS:** `AVMutableMovie` is unavailable. Use a supplied asset, or wrap the production write behind a small seam that records the chosen option. Say that native readback is untested on tvOS.

## Test: read the player item, not the picker

**The wrong test:** set the picker or binding, then assert the store's `selected` value. Deleting the `item.select` line leaves that assertion unchanged.

```swift
@MainActor func testChoosingCaptionsWritesThePlayingItem() async throws {
    let (item, legible, audible) = try await makeMediaItem()
    item.select(audible.options[1], in: audible)                       // existing audio choice
    let store = CaptionStore(player: AVPlayer(playerItem: item))
    try await store.load()                                             // production load path
    store.selection.wrappedValue = store.choices[1].id                 // drive the binding the picker uses
    XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: legible), legible.options[1])
    XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in: audible), audible.options[1]) // audio kept
    store.selection.wrappedValue = nil                                 // Off
    XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: legible))
}
// Without item.select(...): the legible readback stays at its starting value, not legible.options[1].
```

**More cases:**

- **Old binding after reload or replacement:**
  1. Keep the binding with `let old = store.selection`.
  2. Reload, or replace the item.
  3. Choose a new option through the current binding.
  4. Set `old.wrappedValue = nil` and then to another ID.
  5. Assert that the *current* item still has the new option.
- **Missing item vs no group:**
  - build the store with no current item, and separately with an asset that has no tracks of that kind (`AVMutableMovie()` with no subtitle tracks);
  - compare the two reported states;
  - pattern-match enum cases rather than requiring `Equatable` on payloads that are not `Equatable`.
- **Late completion:**
  1. Start load A and keep its completion.
  2. Start load B and finish it.
  3. Deliver A's success and its error.
  4. Assert that B's options and state are unchanged.
- **Failed load:** assert the failed state, then that a retry succeeds.
