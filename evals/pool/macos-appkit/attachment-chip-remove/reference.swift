import AppKit

struct Attachment: Equatable {
    let id: Int
    var filename: String
    var byteCount: Int
}

@MainActor
protocol AttachmentChipDelegate: AnyObject {
    func chipDidRequestPreview(_ attachment: Attachment)
    func chipDidRequestRemoval(_ attachment: Attachment)
}

/// A pill-shaped attachment chip in the compose window's attachment strip.
final class AttachmentChipView: NSView {
    weak var delegate: AttachmentChipDelegate?
    var attachment: Attachment? { didSet { refresh() } }
    /// Sent and scheduled messages show attachments read-only.
    var isEditable = true { didSet { removeButton.isHidden = !isEditable } }

    let titleField = NSTextField(labelWithString: "")
    let previewButton = NSButton(image: NSImage(systemSymbolName: "eye", accessibilityDescription: "Quick Look")!,
                                 target: nil, action: nil)
    let removeButton = NSButton(image: NSImage(systemSymbolName: "xmark.circle.fill", accessibilityDescription: "Remove")!,
                                target: nil, action: nil)
    private let sizeFormatter = ByteCountFormatter()

    override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
        wantsLayer = true
        layer?.cornerRadius = 11
        layer?.backgroundColor = NSColor.quaternaryLabelColor.cgColor
        titleField.lineBreakMode = .byTruncatingMiddle
        for button in [previewButton, removeButton] {
            button.isBordered = false
            button.imagePosition = .imageOnly
            button.target = self
        }
        previewButton.action = #selector(previewPressed(_:))
        removeButton.action = #selector(removePressed(_:))

        let stack = NSStackView(views: [titleField, previewButton, removeButton])
        stack.spacing = 4
        stack.edgeInsets = NSEdgeInsets(top: 2, left: 8, bottom: 2, right: 4)
        stack.translatesAutoresizingMaskIntoConstraints = false
        addSubview(stack)
        // One action for the chip's lifetime; it resolves the attachment and owner when it runs.
        setAccessibilityCustomActions([NSAccessibilityCustomAction(name: "Remove") { [weak self] in
            guard let self, self.isEditable, let attachment = self.attachment, let delegate = self.delegate else { return false }
            delegate.chipDidRequestRemoval(attachment)
            return true
        }])
        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: leadingAnchor),
            stack.trailingAnchor.constraint(equalTo: trailingAnchor),
            stack.topAnchor.constraint(equalTo: topAnchor),
            stack.bottomAnchor.constraint(equalTo: bottomAnchor),
        ])
    }

    required init?(coder: NSCoder) { fatalError("AttachmentChipView is created in code") }

    private func refresh() {
        guard let attachment else { titleField.stringValue = ""; return }
        let size = sizeFormatter.string(fromByteCount: Int64(attachment.byteCount))
        titleField.stringValue = "\(attachment.filename) (\(size))"
        previewButton.setAccessibilityLabel("Quick Look \(attachment.filename)")
        removeButton.setAccessibilityLabel("Remove \(attachment.filename)")
    }

    @objc private func previewPressed(_ sender: NSButton) {
        guard let attachment else { return }
        delegate?.chipDidRequestPreview(attachment)
    }

    @objc private func removePressed(_ sender: NSButton) {
        guard let attachment, isEditable else { return }
        delegate?.chipDidRequestRemoval(attachment)
    }
}
