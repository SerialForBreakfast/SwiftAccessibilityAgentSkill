Inspection is read-only: report available options and the actual current selection without changing playback. A forced-only option omitted by a full-subtitles picker may still be active; that is not Off. Identify described audio by its media characteristic, not the language or title.

For an explicit choice, resolve the current player item and its asset's group. In Swift, use item.select(option, in: group); Off uses item.select(nil, in: group) only when group.allowsEmptySelection. A foreign option does not change playback. Do not publish the requested ID as confirmed selection; inspect the item's selection in the intended group. Automatic selection is a different choice from Off.

A delayed menu action must still own the choice when invoked, including an Off action with no option ID. Item identity catches replacement but not a newer menu request on the same item. Preserve unrelated audio or subtitle selections.

[Apple: selecting an option](https://developer.apple.com/documentation/avfoundation/avplayeritem/select%28_%3Ain%3A%29)
