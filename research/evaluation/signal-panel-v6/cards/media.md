Inspection does not change playback. Missing item, loading, failed load, a loaded item without the group, and an active selection are distinct states; report each, and allow retry after a failed load. An unlisted selection is not Off. For described audio use .describesVideoForAccessibility, not language or title.

Load options from the current item's group. Language and display name describe an option; neither necessarily identifies it uniquely. Keep choices associated with their actual options. Validate membership before writing: an unknown or retired ID leaves the current selection unchanged. Write with item.select(_:in:), then read currentMediaSelection.selectedMediaOption(in:). Off requires allowsEmptySelection; automatic is different. Changing captions must keep the audio selection.

Every setter, including Off, belongs to the item and request that produced it. A new load on the same item, a cancellation or a replaced item retires earlier bindings and completions: an old Off, choice, success or error must not change newer state, and a duplicate completion must not overwrite a result. Cancellation can save work; ownership checks must still reject late delivery.

For proof, use a supplied local asset. Start from a different selection, load through the production path, drive the binding, and check caption and audio. For reload or replacement, drive Off and a choice through the retained old binding and read back the current item. Injected options test the setter, not inventory.

For chapter-based adjustment, move to the neighboring chapter start. At the first or last chapter stay put; with no chapters do nothing rather than jumping by time, unless the product asks for that. Keep ordinary tap-to-play wired separately from drag-to-seek: an accessibility activation is not an ordinary tap handler.

[Apple: selecting an option](https://developer.apple.com/documentation/avfoundation/avplayeritem/select%28_%3Ain%3A%29) | [Implementation excerpts](examples/media.md)
