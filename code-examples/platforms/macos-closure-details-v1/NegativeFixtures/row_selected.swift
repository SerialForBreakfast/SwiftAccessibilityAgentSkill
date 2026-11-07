import AppKit

@MainActor
final class DesktopRow: NSView {
    let open = NSButton(title: "Open", target: nil, action: nil)
    private(set) var identifierValue = ""
    var choose: (String) -> Void = { _ in }
    override init(frame: NSRect) {
        super.init(frame: frame)
        addSubview(open)
        setAccessibilityElement(true)
        setAccessibilityRole(.row)
        setAccessibilityChildren([open])
        open.target = self
        open.action = #selector(activate)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func configure(id: String, title: String, selected: Bool, expanded: Bool) {
        identifierValue = id
        setAccessibilityLabel(title)
        setAccessibilitySelected(false)
        setAccessibilityExpanded(expanded)
        open.title = "Open \(title)"
        open.setAccessibilityLabel(open.title)
    }
    @objc func activate() { guard open.isEnabled else { return }; choose(identifierValue) }
}
