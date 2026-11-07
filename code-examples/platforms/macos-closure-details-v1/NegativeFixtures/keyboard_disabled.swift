import AppKit
import AVKit

@MainActor
final class SemanticToggle: NSControl {
    let status = NSTextField(labelWithString: "Off")
    private(set) var on = false
    var changed: (Bool) -> Void = { _ in }
    override init(frame: NSRect) { super.init(frame: frame); addSubview(status); status.setAccessibilityElement(false); setAccessibilityElement(true) }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    override var acceptsFirstResponder: Bool { isEnabled }
    override func accessibilityRole() -> NSAccessibility.Role? { .checkBox }
    override func accessibilityLabel() -> String? { "Notifications" }
    override func accessibilityValue() -> Any? { NSNumber(value: on) }
    override func isAccessibilityEnabled() -> Bool { isEnabled }
    override func accessibilityPerformPress() -> Bool { activate() }
    @discardableResult func activate() -> Bool {
        // Deliberate mutant: disabled ordinary activation accepted.
        on.toggle(); status.stringValue = on ? "On" : "Off"; changed(on); return true
    }
    override func mouseDown(with event: NSEvent) { _ = activate() }
    override func keyDown(with event: NSEvent) {
        if event.modifierFlags.intersection([.command, .control, .option]).isEmpty,
           [" ", "\r"].contains(event.charactersIgnoringModifiers ?? "") { _ = activate() }
        else { super.keyDown(with: event) }
    }
}

@MainActor
final class RegionState: NSView {
    let button = NSButton(title: "Open", target: nil, action: nil)
    let status = NSTextField(labelWithString: "")
    let backdrop = NSVisualEffectView()
    override init(frame: NSRect) {
        super.init(frame: frame); [backdrop, button, status].forEach { addSubview($0) }
        setAccessibilityElement(true); setAccessibilityRole(.group); setAccessibilityLabel("Downloads")
        setAccessibilityChildren([button, status]); status.textColor = .labelColor
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func configure(name: String, selected: Bool, reduceTransparency: Bool) {
        button.title = name; button.setAccessibilityLabel(name)
        status.stringValue = selected ? "Selected" : "Not selected"
        button.setAccessibilityValue(status.stringValue)
        backdrop.isHidden = reduceTransparency
    }
    static func player(_ player: AVPlayer) -> AVPlayerView {
        let view = AVPlayerView(); view.player = player; view.controlsStyle = .floating; return view
    }
}

@MainActor
final class ModalFlag {
    let view: NSView
    private var prior: Bool?
    init(_ view: NSView) { self.view = view }
    func begin() { guard prior == nil else { return }; prior = view.isAccessibilityModal(); view.setAccessibilityModal(true) }
    func end() { guard let prior else { return }; view.setAccessibilityModal(prior); self.prior = nil }
}
