import AppKit
@MainActor final class InvoiceRow: NSStackView {
    let name = NSTextField(labelWithString: "")
    let open = NSButton(title: "Open", target: nil, action: nil)
    let save = NSButton(title: "Save", target: nil, action: nil)
    override init(frame: NSRect) {
        super.init(frame: frame)
        [name, open, save].forEach { addArrangedSubview($0) }
    }
    required init?(coder: NSCoder) { nil }
}
