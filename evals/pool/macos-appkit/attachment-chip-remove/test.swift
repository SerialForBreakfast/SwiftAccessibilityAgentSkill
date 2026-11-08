_ = NSApplication.shared
let first = Owner(), second = Owner()
let chip = AttachmentChipView(frame: NSRect(x: 0, y: 0, width: 220, height: 22))
let invoice = Attachment(id: 1, filename: "Invoice-0425.pdf", byteCount: 182_000)
let photo = Attachment(id: 2, filename: "Site photo.heic", byteCount: 2_400_000)
func removeActions() -> [NSAccessibilityCustomAction] {
    (chip.accessibilityCustomActions() ?? []).filter { $0.name.localizedCaseInsensitiveContains("remove") }
}

chip.delegate = first
chip.attachment = invoice
guard let earlier = removeActions().first else { return false }

// The strip reuses the chip for another attachment, then the draft pops out into a new window.
chip.attachment = photo
chip.delegate = second
guard removeActions().count == 1, fire(removeActions()[0]) else { return false }
guard second.removed == [2], first.removed.isEmpty else { return false }
// An action object kept from before never reaches the old window or removes the old attachment.
_ = fire(earlier)
guard first.removed.isEmpty, !second.removed.contains(1), second.removed.count <= 2 else { return false }

// The ordinary buttons stay reachable and reach the current owner once.
second.removed = []
for button in [chip.previewButton, chip.removeButton] {
    guard reachable(button, from: chip), button.isEnabled else { return false }
}
guard chip.removeButton.accessibilityLabel() == "Remove Site photo.heic",
      chip.previewButton.accessibilityLabel() == "Quick Look Site photo.heic" else { return false }
guard press(chip.previewButton), second.previewed == [2], second.removed.isEmpty else { return false }
guard press(chip.removeButton), second.removed == [2], first.previewed.isEmpty, first.removed.isEmpty else { return false }

// Read-only messages: no removal by any route, Quick Look still works.
chip.isEditable = false
second.removed = []; second.previewed = []
guard removeActions().count <= 1 else { return false }
for action in removeActions() { _ = fire(action) }
_ = fire(earlier)
guard second.removed.isEmpty, first.removed.isEmpty else { return false }
guard reachable(chip.previewButton, from: chip), press(chip.previewButton), second.previewed == [2] else { return false }

// Editable again: the action is back and works.
chip.isEditable = true
guard removeActions().count == 1, fire(removeActions()[0]), second.removed == [2] else { return false }
return true
