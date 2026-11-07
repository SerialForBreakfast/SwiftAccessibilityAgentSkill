import SwiftUI

#if os(macOS)
import AppKit
typealias BridgeButton = NSButton
#else
import UIKit
typealias BridgeButton = UIButton
#endif

@MainActor
final class BridgeOwner: NSObject {
    private var generation = 0
    private weak var button: BridgeButton?
    private var handler: () -> Void = {}
    private var enabled = false
    func configure(_ button: BridgeButton, title: String, enabled: Bool, handler: @escaping () -> Void) {
        generation += 1; self.button = button; self.enabled = enabled; self.handler = handler
        #if os(macOS)
        button.title = title; button.setAccessibilityLabel(title)
        button.target = self; button.action = #selector(activate)
        #else
        button.setTitle(title, for: .normal); button.accessibilityLabel = title
        #endif
        button.isEnabled = enabled
        #if !os(macOS)
        button.removeAction(identifiedBy: UIAction.Identifier("bridge"), for: .primaryActionTriggered)
        let callback = action()
        button.addAction(UIAction(identifier: UIAction.Identifier("bridge")) { _ in callback() }, for: .primaryActionTriggered)
        #endif
    }
    @objc func activate() { action()() }
    func action() -> () -> Void {
        let ticket = generation
        return { [weak self] in
            guard let self, self.generation == ticket, self.enabled, self.button?.isEnabled == true else { return }
            self.handler()
        }
    }
    func stop() {
        generation += 1
        #if os(macOS)
        button?.target = nil; button?.action = nil
        #else
        button?.removeAction(identifiedBy: UIAction.Identifier("bridge"), for: .primaryActionTriggered)
        #endif
        button = nil; handler = {}; enabled = false
    }
}

#if os(macOS)
struct NativeButtonExample: NSViewRepresentable {
    let title: String
    let enabled: Bool
    let action: () -> Void
    func makeCoordinator() -> BridgeOwner { BridgeOwner() }
    func makeNSView(context: Context) -> NSButton { NSButton(title: "", target: nil, action: nil) }
    func updateNSView(_ view: NSButton, context: Context) { context.coordinator.configure(view, title: title, enabled: enabled, handler: action) }
    static func dismantleNSView(_ view: NSButton, coordinator: BridgeOwner) { coordinator.stop() }
}
#else
struct NativeButtonExample: UIViewRepresentable {
    let title: String
    let enabled: Bool
    let action: () -> Void
    func makeCoordinator() -> BridgeOwner { BridgeOwner() }
    func makeUIView(context: Context) -> UIButton { UIButton(type: .system) }
    func updateUIView(_ view: UIButton, context: Context) { context.coordinator.configure(view, title: title, enabled: enabled, handler: action) }
    static func dismantleUIView(_ view: UIButton, coordinator: BridgeOwner) { coordinator.stop() }
}
#endif
