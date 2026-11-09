Inspection does not change playback. Distinguish missing item, failed load, inspected empty group, and active selection. An unlisted selection is not Off. For described audio use .describesVideoForAccessibility, not language or title.

Load options from the current item's group. Language and display name describe an option; neither necessarily identifies it uniquely. Keep choices associated with their actual options. Bind each setter, including Off, to the originating item and request. Validate membership, write with item.select(_:in:), then read currentMediaSelection.selectedMediaOption(in:). Off requires allowsEmptySelection; automatic is different.

For requested proof, use a supplied local asset with independently identifiable options, not an invented bundle resource. Start with a different selection; load through the production path, drive the binding, and check the item's caption and unrelated audio. For replacement, retain the old binding; reuse option IDs on the new item. Try Off and a choice through both bindings and read back the replacement. Injecting options isolates the setter, not inventory. If the fixture is unavailable, say which claim remains untested.

For chapter-based adjustment, resolve a neighboring chapter start. At an outward boundary or with no chapters, do not substitute a time jump unless the product asks for one. Keep ordinary tap-to-play wired separately from drag-to-seek: an accessibility activation is not an ordinary tap handler.

[Apple: selecting an option](https://developer.apple.com/documentation/avfoundation/avplayeritem/select%28_%3Ain%3A%29) | [Implementation excerpts](examples/media.md)
