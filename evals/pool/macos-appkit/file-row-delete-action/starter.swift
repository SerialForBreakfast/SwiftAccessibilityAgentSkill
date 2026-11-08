import AppKit

struct FileItem: Equatable {
    let id: String
    var name: String
    var modified: String
    var isLocked: Bool
}

/// One row in the Files table. The table reuses rows as the list scrolls and refreshes.
final class FileRowView: NSTableCellView {
    let nameField = NSTextField(labelWithString: "")
    let modifiedField = NSTextField(labelWithString: "")
    let openButton = NSButton(title: "Open", target: nil, action: nil)
    let deleteButton = NSButton(title: "Delete", target: nil, action: nil)

    private(set) var file: FileItem?
    private var onOpen: (FileItem) -> Void = { _ in }
    private var onDelete: (FileItem) -> Void = { _ in }

    override init(frame frameRect: NSRect) {
        super.init(frame: frameRect)
        modifiedField.textColor = .secondaryLabelColor
        openButton.bezelStyle = .push
        deleteButton.bezelStyle = .push
        openButton.target = self
        openButton.action = #selector(openPressed(_:))
        deleteButton.target = self
        deleteButton.action = #selector(deletePressed(_:))

        let stack = NSStackView(views: [nameField, modifiedField, openButton, deleteButton])
        stack.orientation = .horizontal
        stack.spacing = 8
        stack.translatesAutoresizingMaskIntoConstraints = false
        addSubview(stack)
        textField = nameField
        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: leadingAnchor, constant: 8),
            stack.trailingAnchor.constraint(lessThanOrEqualTo: trailingAnchor, constant: -8),
            stack.centerYAnchor.constraint(equalTo: centerYAnchor),
        ])
    }

    required init?(coder: NSCoder) { fatalError("FileRowView is created in code") }

    func configure(with file: FileItem,
                   onOpen: @escaping (FileItem) -> Void,
                   onDelete: @escaping (FileItem) -> Void) {
        self.file = file
        self.onOpen = onOpen
        self.onDelete = onDelete
        nameField.stringValue = file.name
        modifiedField.stringValue = file.modified
        openButton.setAccessibilityLabel("Open \(file.name)")
        deleteButton.setAccessibilityLabel("Delete \(file.name)")
        deleteButton.isEnabled = !file.isLocked
        deleteButton.toolTip = file.isLocked ? "\(file.name) is locked" : nil
    }

    @objc private func openPressed(_ sender: NSButton) {
        guard let file else { return }
        onOpen(file)
    }

    @objc private func deletePressed(_ sender: NSButton) {
        guard let file, deleteButton.isEnabled else { return }
        onDelete(file)
    }
}
