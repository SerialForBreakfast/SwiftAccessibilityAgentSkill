import AppKit

@MainActor
final class DesktopActions: NSStackView {
    let title = NSTextField(labelWithString: "")
    let open = NSButton(title: "Open", target: nil, action: nil)
    let save = NSButton(title: "Save", target: nil, action: nil)
    private var generation = 0
    private var onOpen: () -> Void = {}
    private var onSave: () -> Void = {}

    init() {
        super.init(frame: .zero)
        [title, open, save].forEach { addArrangedSubview($0) }
        open.target = self; open.action = #selector(openItem)
        save.target = self; save.action = #selector(saveItem)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }

    func configure(title text: String, openName: String, saveName: String,
                   onOpen: @escaping () -> Void, onSave: @escaping () -> Void) {
        generation += 1
        let revision = generation
        self.onOpen = onOpen; self.onSave = onSave
        title.stringValue = text
        setAccessibilityElement(false)
        title.setAccessibilityElement(true)
        open.setAccessibilityElement(true); save.setAccessibilityElement(true)
        open.setAccessibilityLabel(openName); save.setAccessibilityLabel(saveName)
        open.setAccessibilityValue(nil); save.setAccessibilityValue(nil)
        // An optional shortcut supplements, rather than replaces, the ordinary Save button.
        open.setAccessibilityCustomActions([NSAccessibilityCustomAction(name: saveName) { [weak self] in
            guard let self, self.save.isEnabled else { return false }
            self.onSave()
            return true
        }])
    }
    @objc private func openItem() { guard open.isEnabled else { return }; onOpen() }
    @objc private func saveItem() { guard save.isEnabled else { return }; onSave() }
}

@MainActor
final class DesktopStatus {
    let label = NSTextField(labelWithString: "")
    private let post: (Any, NSAccessibility.Notification) -> Void
    init(post: @escaping (Any, NSAccessibility.Notification) -> Void = {
        NSAccessibility.post(element: $0, notification: $1)
    }) { self.post = post }
    func update(_ value: String) {
        guard value != label.stringValue else { return }
        label.stringValue = value
        post(label, .valueChanged)
    }
}
