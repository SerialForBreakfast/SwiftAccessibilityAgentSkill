import SwiftUI
#if os(macOS)
import AppKit
typealias SurfaceButton = NSButton
final class NativeSurface: NSView {
    let heading = NSTextField(labelWithString: "")
    let status = NSTextField(wrappingLabelWithString: "")
    let primary = NSButton(title: "", target: nil, action: nil)
    let details = NSButton(title: "", target: nil, action: nil)
    override init(frame: NSRect) {
        super.init(frame: frame)
        [heading, primary, details, status].forEach { addSubview($0) }
        setAccessibilityElement(true); setAccessibilityRole(.group)
        setAccessibilityChildren([heading, primary, details, status])
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
}
#else
import UIKit
typealias SurfaceButton = UIButton
final class NativeSurface: UIView {
    let heading = UILabel()
    let status = UILabel()
    let primary = UIButton(type: .system)
    let details = UIButton(type: .system)
    override init(frame: CGRect) {
        super.init(frame: frame)
        [heading, primary, details, status].forEach { addSubview($0) }
        isAccessibilityElement = false
        accessibilityElements = [heading, primary, details, status]
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
}
#endif

struct SurfaceSnapshot: Equatable {
    var id = "one"
    var title = "Report"
    var status: String? = "Ready"
    var hint: String? = nil
    var selected = false
    var enabled = true
    var landmark = true
    var value: String { [status, selected ? "Selected" : "Not selected"].compactMap { $0 }.filter { !$0.isEmpty }.joined(separator: ", ") }
}

@MainActor final class SurfaceOwner: NSObject {
    private weak var surface: NativeSurface?
    private var generation = 0
    private var snapshot = SurfaceSnapshot()
    private var perform: (String, Bool) -> Void = { _,_ in }
    func configure(_ view: NativeSurface, snapshot: SurfaceSnapshot, perform: @escaping (String, Bool) -> Void) {
        if let old = surface, old !== view { detach(old) }
        generation += 1; surface = view; self.snapshot = snapshot; self.perform = perform
        #if os(macOS)
        view.setAccessibilityLabel(snapshot.title)
        view.heading.stringValue = snapshot.title
        view.heading.setAccessibilityRole(snapshot.landmark ? .headingRole : .staticText)
        view.primary.title = "Open \(snapshot.title)"; view.details.title = "Details \(snapshot.title)"
        view.primary.setAccessibilityLabel(view.primary.title); view.details.setAccessibilityLabel(view.details.title)
        view.primary.setAccessibilityValue(snapshot.value); view.primary.setAccessibilityHelp(snapshot.hint)
        view.primary.setAccessibilitySelected(snapshot.selected)
        view.status.stringValue = snapshot.value; view.status.setAccessibilityValue(snapshot.value)
        view.status.font = .preferredFont(forTextStyle: .body)
        view.status.usesSingleLineMode = false
        view.primary.target = self; view.primary.action = #selector(open(_:))
        view.details.target = self; view.details.action = #selector(detail(_:))
        let shortcut = action(view, secondary: true)
        view.primary.setAccessibilityCustomActions([NSAccessibilityCustomAction(name: view.details.title) { shortcut() }])
        #else
        view.accessibilityLabel = snapshot.title; view.heading.text = snapshot.title
        if snapshot.landmark { view.heading.accessibilityTraits.insert(.header) } else { view.heading.accessibilityTraits.remove(.header) }
        view.primary.setTitle("Open \(snapshot.title)", for: .normal); view.details.setTitle("Details \(snapshot.title)", for: .normal)
        view.primary.accessibilityLabel = view.primary.title(for: .normal); view.details.accessibilityLabel = view.details.title(for: .normal)
        view.primary.accessibilityValue = snapshot.value; view.primary.accessibilityHint = snapshot.hint
        if snapshot.selected { view.primary.accessibilityTraits.insert(.selected) } else { view.primary.accessibilityTraits.remove(.selected) }
        view.status.text = snapshot.value; view.status.accessibilityLabel = nil
        view.status.font = .preferredFont(forTextStyle: .body); view.status.adjustsFontForContentSizeCategory = true
        view.status.numberOfLines = 0; view.status.lineBreakMode = .byWordWrapping
        for (button, secondary) in [(view.primary, false), (view.details, true)] {
            button.removeAction(identifiedBy: UIAction.Identifier("surface"), for: .primaryActionTriggered)
            let callback = action(view, secondary: secondary)
            button.addAction(UIAction(identifier: UIAction.Identifier("surface")) { _ in _ = callback() }, for: .primaryActionTriggered)
        }
        let shortcut = action(view, secondary: true)
        view.primary.accessibilityCustomActions = [UIAccessibilityCustomAction(name: "Details \(snapshot.title)") { _ in shortcut() }]
        #endif
        view.primary.isEnabled = snapshot.enabled; view.details.isEnabled = snapshot.enabled
    }
    func action(_ view: NativeSurface, secondary: Bool) -> () -> Bool {
        let ticket = generation
        return { [weak self, weak view] in
            guard let self, let view, self.surface === view, 
                  self.snapshot.enabled, (secondary ? view.details : view.primary).isEnabled else { return false }
            self.perform(self.snapshot.id, secondary); return true
        }
    }
    #if os(macOS)
    @objc private func open(_ sender: NSButton) { guard let view = surface, sender === view.primary else { return }; _ = action(view, secondary: false)() }
    @objc private func detail(_ sender: NSButton) { guard let view = surface, sender === view.details else { return }; _ = action(view, secondary: true)() }
    #endif
    private func detach(_ view: NativeSurface) {
        #if os(macOS)
        view.primary.target = nil; view.primary.action = nil; view.details.target = nil; view.details.action = nil
        view.primary.setAccessibilityCustomActions([])
        #else
        for button in [view.primary, view.details] { button.removeAction(identifiedBy: UIAction.Identifier("surface"), for: .primaryActionTriggered) }
        view.primary.accessibilityCustomActions = []
        #endif
    }
    func stop() { generation += 1; if let view = surface { detach(view) }; surface = nil; perform = { _,_ in } }
}

#if os(macOS)
struct SurfaceExample: NSViewRepresentable {
    let snapshot: SurfaceSnapshot
    let perform: (String, Bool) -> Void
    func makeCoordinator() -> SurfaceOwner { SurfaceOwner() }
    func makeNSView(context: Context) -> NativeSurface { NativeSurface() }
    func updateNSView(_ view: NativeSurface, context: Context) { context.coordinator.configure(view, snapshot: snapshot, perform: perform) }
    static func dismantleNSView(_ view: NativeSurface, coordinator: SurfaceOwner) { coordinator.stop() }
}
#else
struct SurfaceExample: UIViewRepresentable {
    let snapshot: SurfaceSnapshot
    let perform: (String, Bool) -> Void
    func makeCoordinator() -> SurfaceOwner { SurfaceOwner() }
    func makeUIView(context: Context) -> NativeSurface { NativeSurface() }
    func updateUIView(_ view: NativeSurface, context: Context) { context.coordinator.configure(view, snapshot: snapshot, perform: perform) }
    static func dismantleUIView(_ view: NativeSurface, coordinator: SurfaceOwner) { coordinator.stop() }
}
#endif
