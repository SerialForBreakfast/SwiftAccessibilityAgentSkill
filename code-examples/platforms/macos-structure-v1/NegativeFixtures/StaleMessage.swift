import AppKit

@MainActor
final class DesktopForm: NSView, NSTextFieldDelegate {
    let field = NSTextField()
    let errorLabel = NSTextField(labelWithString: "")
    let submitButton = NSButton(title: "Save", target: nil, action: nil)
    private let originalHelp: String?
    private let validate: (String) -> String?
    private let save: (String) -> Void
    private var submitting = false
    init(help: String? = nil, validate: @escaping (String) -> String?, save: @escaping (String) -> Void) {
        originalHelp = help; self.validate = validate; self.save = save
        super.init(frame: .zero)
        [field, errorLabel, submitButton].forEach { addSubview($0) }
        setAccessibilityElement(false)
        field.delegate = self
        field.setAccessibilityLabel("Email")
        field.setAccessibilityHelp(help)
        errorLabel.isHidden = true
        errorLabel.setAccessibilityElement(false)
        submitButton.target = self; submitButton.action = #selector(submit)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func controlTextDidChange(_ notification: Notification) {
        guard let sender = notification.object as? NSTextField, sender === field else { return }
        edited()
    }
    func edited() {}
    private func show(_ message: String?) {
        errorLabel.stringValue = message ?? ""
        errorLabel.isHidden = message == nil
        errorLabel.setAccessibilityElement(message != nil)
        field.setAccessibilityHelp(message.map { [originalHelp, $0].compactMap { $0 }.joined(separator: ". ") } ?? originalHelp)
    }
    @objc func submit() {
        guard submitButton.isEnabled, !submitting else { return }
        let input = field.stringValue
        let error = validate(input)
        show(error)
        guard error == nil else { return }
        submitting = true; defer { submitting = false }
        save(input)
    }
}
