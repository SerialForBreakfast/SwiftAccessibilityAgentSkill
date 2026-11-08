macOS 26.0, AppKit.

Our VoiceOver testers want Remove in the Actions menu (VO-Command-Space) on the attachment chip itself, so they don't have to hunt for the tiny x button. Can you add that to `AttachmentChipView`?

Some context: the attachment strip reuses chips when attachments are added or removed, and when someone pops a draft out into its own window we move the existing chips over and set `delegate` to the new window's controller. Read-only messages set `isEditable = false`.

Keep `Attachment`, `AttachmentChipDelegate`, `AttachmentChipView`, `delegate`, `attachment`, `isEditable`, `previewButton` and `removeButton` as they are.
