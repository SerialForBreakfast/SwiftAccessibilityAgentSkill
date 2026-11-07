import AppKit

@MainActor
final class DesktopModalRestore {
    private weak var root: NSView?
    private weak var primary: NSButton?
    private weak var fallback: NSButton?
    private var nextID = 0
    private var active: Int?
    private let request: (NSButton) -> Bool
    init(root: NSView, request: @escaping (NSButton) -> Bool = {
        $0.window?.makeFirstResponder($0) ?? false
    }) { self.root = root; self.request = request }
    func begin(primary: NSButton?, fallback: NSButton?) -> Int {
        nextID += 1; active = nextID
        self.primary = primary; self.fallback = fallback
        return nextID
    }
    func cancel(_ token: Int) {
        guard active == token else { return }
        active = nil; primary = nil; fallback = nil
    }
    func finish(_ token: Int) -> Bool {
        guard active == token else { return false }
        active = nil
        let target = eligible(primary) ? primary : eligible(fallback) ? fallback : nil
        primary = nil; fallback = nil
        guard let target else { return false }
        return request(target)
    }
    private func eligible(_ target: NSButton?) -> Bool {
        guard let target, let root else { return false }
        return target.isDescendant(of: root) && target.isEnabled && !target.isHiddenOrHasHiddenAncestor
    }
}

struct DisplayPreferences: Equatable, Sendable {
    var reduceMotion = false
    var reduceTransparency = false
    var increaseContrast = false
}

// Immutable ownership of Foundation tokens; cleanup can occur on any thread.
private final class Observations: @unchecked Sendable {
    let center: NotificationCenter
    let tokens: [NSObjectProtocol]
    init(center: NotificationCenter, tokens: [NSObjectProtocol]) { self.center = center; self.tokens = tokens }
    deinit { tokens.forEach { center.removeObserver($0) } }
}

@MainActor
final class DesktopPreferences {
    static let names = [NSWorkspace.accessibilityDisplayOptionsDidChangeNotification]
    private let center: NotificationCenter
    private let read: () -> DisplayPreferences
    private let apply: (DisplayPreferences) -> Void
    private let enqueue: @Sendable (@escaping @MainActor @Sendable () -> Void) -> Void
    private var observations: Observations?
    private var generation = 0
    private var last: DisplayPreferences?
    init(center: NotificationCenter = NSWorkspace.shared.notificationCenter,
         read: @escaping () -> DisplayPreferences = {
             let w = NSWorkspace.shared
             return DisplayPreferences(reduceMotion: w.accessibilityDisplayShouldReduceMotion,
                 reduceTransparency: w.accessibilityDisplayShouldReduceTransparency,
                 increaseContrast: w.accessibilityDisplayShouldIncreaseContrast)
         }, enqueue: @escaping @Sendable (@escaping @MainActor @Sendable () -> Void) -> Void = {
             action in Task { @MainActor in action() }
         }, apply: @escaping (DisplayPreferences) -> Void) {
        self.center = center; self.read = read; self.enqueue = enqueue; self.apply = apply
    }
    func start() {
        guard observations == nil else { return }
        generation += 1
        let revision = generation, schedule = enqueue
        let tokens = Self.names.map { name in
            center.addObserver(forName: name, object: nil, queue: nil) { [weak self] _ in
                schedule { [weak self] in
                    guard let self, self.observations != nil, self.generation == revision else { return }
                    self.refresh()
                }
            }
        }
        observations = Observations(center: center, tokens: tokens)
        refresh()
    }
    func stop() { generation += 1; observations = nil; last = nil }
    private func refresh() {
        let value = read()
        guard value != last else { return }
        last = value
        apply(value)
    }
}
