import UIKit

enum LiteralMatches {
    static func ranges(in text: String, query: String, allowOverlaps: Bool) -> [NSRange] {
        guard !query.isEmpty else { return [] }
        var boundaries = [0], offset = 0
        for character in text {
            offset += String(character).utf16.count
            boundaries.append(offset)
        }
        let boundarySet = Set(boundaries), document = text as NSString
        var cursor = 0, boundaryIndex = 0, result: [NSRange] = []
        while cursor < document.length {
            let found = document.range(of: query, options: .literal,
                                       range: NSRange(location: cursor, length: document.length - cursor))
            guard found.location != NSNotFound, found.length > 0 else { break }
            let end = NSMaxRange(found)
            let valid = boundarySet.contains(found.location) && boundarySet.contains(end)
            if valid { result.append(found) }
            while boundaryIndex < boundaries.count && boundaries[boundaryIndex] <= found.location {
                boundaryIndex += 1
            }
            let next = boundaryIndex < boundaries.count ? boundaries[boundaryIndex] : document.length
            cursor = valid && !allowOverlaps ? end : next
        }
        return result
    }
}

@MainActor
final class EditedMatchReader: UIView {
    let textView = UITextView()
    private(set) var matches: [NSRange] = []
    private var revision = 0

    override init(frame: CGRect) {
        super.init(frame: frame)
        addSubview(textView)
        isAccessibilityElement = false
        textView.isEditable = false
        textView.isSelectable = true
        textView.isAccessibilityElement = true
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) is not supported") }

    func replace(text: String, query: String, allowOverlaps: Bool = false) {
        revision += 1
        let epoch = revision
        textView.text = text
        matches = LiteralMatches.ranges(in: text, query: query, allowOverlaps: allowOverlaps)
        textView.accessibilityCustomRotors = []
        guard !matches.isEmpty else { return }
        var restart = true
        textView.accessibilityCustomRotors = [UIAccessibilityCustomRotor(name: "Matches") { [weak self] predicate in
            guard let self, self.revision == epoch else { return nil }
            let item: UIAccessibilityCustomRotorItemResult? = predicate.currentItem
            var current: Int?
            if !restart, item?.targetElement === self.textView, let range = item?.targetRange {
                let start = self.textView.offset(from: self.textView.beginningOfDocument, to: range.start)
                let end = self.textView.offset(from: self.textView.beginningOfDocument, to: range.end)
                if start >= 0 && end >= start {
                    current = self.matches.firstIndex(of: NSRange(location: start, length: end - start))
                }
            }
            restart = false
            let index = predicate.searchDirection == .next
                ? current.map { $0 + 1 } ?? 0
                : current.map { $0 - 1 } ?? self.matches.count - 1
            guard self.matches.indices.contains(index) else { return nil }
            let match = self.matches[index]
            guard let start = self.textView.position(from: self.textView.beginningOfDocument, offset: match.location),
                  let end = self.textView.position(from: start, offset: match.length),
                  let range = self.textView.textRange(from: start, to: end) else { return nil }
            return UIAccessibilityCustomRotorItemResult(targetElement: self.textView, targetRange: range)
        }]
    }
}
