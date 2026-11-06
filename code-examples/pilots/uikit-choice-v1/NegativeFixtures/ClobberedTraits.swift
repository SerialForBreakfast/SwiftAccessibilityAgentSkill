import UIKit

@MainActor
final class AccessibleChoiceCell: UITableViewCell {
    let nameLabel = UILabel()
    let stateLabel = UILabel()
    let textStack = UIStackView()

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        textStack.axis = .vertical
        textStack.spacing = 4
        textStack.translatesAutoresizingMaskIntoConstraints = false
        textStack.addArrangedSubview(nameLabel)
        textStack.addArrangedSubview(stateLabel)
        contentView.addSubview(textStack)
        NSLayoutConstraint.activate([
            textStack.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 12),
            textStack.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -12),
            textStack.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 12),
            textStack.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -12)
        ])
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) is not supported") }

    func configure(name: String, chosen: Bool, selectedText: String, unselectedText: String) {
        nameLabel.text = name
        stateLabel.text = chosen ? selectedText : unselectedText
        for label in [nameLabel, stateLabel] {
            label.numberOfLines = 0
            label.lineBreakMode = .byWordWrapping
            label.adjustsFontSizeToFitWidth = false
            label.adjustsFontForContentSizeCategory = true
            label.font = .preferredFont(forTextStyle: .body, compatibleWith: label.traitCollection)
            label.textColor = .label
            label.isAccessibilityElement = false
        }
        isAccessibilityElement = true
        accessibilityLabel = name
        accessibilityValue = stateLabel.text
        if chosen { accessibilityTraits = .selected }
        else { accessibilityTraits.remove(.selected) }
        accessoryType = chosen ? .checkmark : .none
    }

    static func configureSizing(_ table: UITableView) {
        table.rowHeight = UITableView.automaticDimension
        table.estimatedRowHeight = 60
    }
}
