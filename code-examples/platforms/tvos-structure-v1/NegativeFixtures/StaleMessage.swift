import UIKit

@MainActor
final class TelevisionForm: UIView {
    let field = UITextField()
    let errorLabel = UILabel()
    let submitButton = UIButton(type: .system)
    private let originalHint: String?
    private let validate: (String) -> String?
    private let save: (String) -> Void
    private var submitting = false
    init(hint: String? = nil, validate: @escaping (String) -> String?, save: @escaping (String) -> Void) {
        originalHint = hint; self.validate = validate; self.save = save
        super.init(frame: .zero)
        [field, errorLabel, submitButton].forEach { addSubview($0) }
        isAccessibilityElement = false
        field.addAction(UIAction { [weak self] _ in self?.edited() }, for: .editingChanged)
        field.accessibilityLabel = "Email"
        field.accessibilityHint = hint
        errorLabel.isHidden = true; errorLabel.isAccessibilityElement = false
        submitButton.setTitle("Save", for: .normal)
        submitButton.addAction(UIAction { [weak self] _ in self?.submit() }, for: .primaryActionTriggered)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func edited() {}
    private func show(_ message: String?) {
        errorLabel.text = message ?? ""
        errorLabel.isHidden = message == nil
        errorLabel.isAccessibilityElement = message != nil
        field.accessibilityHint = message.map { [originalHint, $0].compactMap { $0 }.joined(separator: ". ") } ?? originalHint
    }
    func submit() {
        guard submitButton.isEnabled, !submitting else { return }
        let input = field.text ?? ""
        let error = validate(input)
        show(error)
        guard error == nil else { return }
        submitting = true; defer { submitting = false }
        save(input)
    }
}
