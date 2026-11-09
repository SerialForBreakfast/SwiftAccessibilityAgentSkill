Separate inventory, selection and a requested change. Missing item, load error and an inspected empty group convey different information. An active option outside the offered list is not Off. For described audio, use .describesVideoForAccessibility, not language or title. Choose tagged and ordinary fixtures independently of the predicate under test. Inspection leaves playback unchanged.

For a change, resolve the current item's group, validate the option, select on the item, and publish its currentMediaSelection.selectedMediaOption(in:) result. Off requires allowsEmptySelection; automatic is a different operation. Bind the installed picker setter (including nil) to its originating item and request. A later request can use the same item.

For proof, begin with a different actual selection. Use the picker binding and inspect the player's item, including the unrelated audio choice. A local selected ID alone cannot distinguish a successful write from an ignored one. Compare old and current choices after reload without changing ordinary playback controls.

For chapter adjustments, follow the product's requested units. The end of an asset is not another chapter start; preserve ordinary dragging and playback at a boundary.

[Apple: selecting an option](https://developer.apple.com/documentation/avfoundation/avplayeritem/select%28_%3Ain%3A%29) | [Implementation excerpts](examples/media.md)
