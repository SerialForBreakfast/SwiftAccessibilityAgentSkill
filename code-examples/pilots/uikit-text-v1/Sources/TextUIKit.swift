import UIKit

@MainActor public final class TextMatchRotor: UIView {
    public let textView = UITextView()
    private var matches: [NSRange] = []
    public override init(frame: CGRect) {
        super.init(frame: frame)
        addSubview(textView)
        isAccessibilityElement = false
        textView.accessibilityCustomRotors = [UIAccessibilityCustomRotor(name: "Matches") { [weak self] predicate in
            guard let self, !self.matches.isEmpty else { return nil }
            let item: UIAccessibilityCustomRotorItemResult? = predicate.currentItem
            let current: Int?
            if item?.targetElement === self.textView, let range = item?.targetRange {
                let offset = self.textView.offset(from: self.textView.beginningOfDocument, to: range.start)
                current = self.matches.firstIndex { $0.location == offset }
            } else { current = nil }
            let index = predicate.searchDirection == .next
                ? current.map { $0 + 1 } ?? 0
                : current.map { $0 - 1 } ?? self.matches.count - 1
            guard self.matches.indices.contains(index) else { return nil }
            let match = self.matches[index]
            guard let start = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location),
                  let end = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location + match.length),
                  let range = self.textView.textRange(from: start, to: end) else { return nil }
            return UIAccessibilityCustomRotorItemResult(targetElement: self.textView, targetRange: range)
        }]
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    @discardableResult public func replace(text: String, query: String) -> Bool {
        guard !query.isEmpty else { return false }
        textView.text = text
        matches.removeAll()
        let document = text as NSString
        var offset = 0
        while offset < document.length {
            let found = document.range(of: query, options: .literal, range: NSRange(location: offset, length: document.length - offset))
            guard found.location != NSNotFound else { break }
            matches.append(found)
            offset = NSMaxRange(found)
        }
        return true
    }
}

@MainActor public enum EditActionFactory {
    public static func make(title: NSAttributedString, handler: @escaping UIAccessibilityCustomAction.Handler) -> UIAccessibilityCustomAction {
        let action = UIAccessibilityCustomAction(attributedName: title, actionHandler: handler)
        action.category = UIAccessibilityCustomAction.editCategory
        return action
    }
}
