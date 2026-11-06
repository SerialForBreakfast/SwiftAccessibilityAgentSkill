import AppKit

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
final class DesktopText: NSView {
    let textView = NSTextView()
    private(set) var matches: [NSRange] = []
    private var session: SearchSession?
    override init(frame: NSRect) {
        super.init(frame: frame); addSubview(textView)
        setAccessibilityElement(false); textView.isEditable = false; textView.isSelectable = true
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func replace(text: String, query: String, allowOverlaps: Bool = false) {
        session = nil; textView.setAccessibilityCustomRotors([]); textView.string = text
        matches = LiteralMatches.ranges(in: text, query: query, allowOverlaps: allowOverlaps)
        guard !matches.isEmpty else { return }
        let next = SearchSession(owner: self, text: text)
        session = next
        textView.setAccessibilityCustomRotors([NSAccessibilityCustomRotor(label: "Matches", itemSearchDelegate: next)])
    }
    @MainActor
    private final class SearchSession: NSObject, @MainActor NSAccessibilityCustomRotorItemSearchDelegate {
        weak var owner: DesktopText?
        let text: String
        var restart = true
        init(owner: DesktopText, text: String) { self.owner = owner; self.text = text }
        func rotor(_ rotor: NSAccessibilityCustomRotor, resultFor searchParameters: NSAccessibilityCustomRotor.SearchParameters) -> NSAccessibilityCustomRotor.ItemResult? {
            guard let owner, owner.session === self, owner.textView.string == text else { return nil }
            let filter = searchParameters.filterString
            let ranges = owner.matches.filter { filter.isEmpty || (text as NSString).substring(with: $0).localizedCaseInsensitiveContains(filter) }
            var current: Int?
            if !restart, (searchParameters.currentItem?.targetElement as? NSTextView) === owner.textView,
               let range = searchParameters.currentItem?.targetRange { current = ranges.firstIndex(of: range) }
            restart = false
            let next = searchParameters.searchDirection == .next ? current.map { $0 + 1 } ?? 0 : current.map { $0 - 1 } ?? ranges.count - 1
            guard ranges.indices.contains(next) else { return nil }
            let result = NSAccessibilityCustomRotor.ItemResult(targetElement: owner.textView)
            result.targetRange = ranges[next]
            return result
        }
    }
}
