// Generic subjects for qualifying the v7 recipe tests. Not panel code.
// Lines tagged FIX are removed or replaced to make the defect variant.
import AVFoundation
import SwiftUI
#if canImport(UIKit)
import UIKit

@MainActor public final class Binder {
    private var generation = 0
    private var handler: () -> Void = {}
    private weak var button: UIButton?
    public init() {}
    public func bind(_ button: UIButton, handler: @escaping () -> Void) {
        generation += 1
        self.button = button
        self.handler = handler
        button.removeAction(identifiedBy: .init("primary"), for: .primaryActionTriggered)
        let callback = makeCallback()
        button.addAction(UIAction(identifier: .init("primary")) { _ in callback() }, for: .primaryActionTriggered)
    }
    public func makeCallback() -> () -> Void {
        let ticket = generation
        return { [weak self] in
            guard let self else { return }
            guard self.generation == ticket else { return } // FIX:callbacks
            self.handler()
        }
    }
    public func stop() {
        generation += 1
        button?.removeAction(identifiedBy: .init("primary"), for: .primaryActionTriggered)
        handler = {}
    }
}

@MainActor public final class SignupForm {
    public enum Failure: Error { case taken }
    public let field: UITextField
    public private(set) var error: Failure?
    public private(set) var isBusy = false
    public private(set) var accepted: String?
    private var generation = 0
    public init(field: UITextField) { self.field = field }
    public func submit() -> (Result<Void, Failure>) -> Void {
        generation += 1
        let ticket = generation, input = field.text ?? ""
        isBusy = true; error = nil
        return { [weak self] result in
            guard let self, self.generation == ticket else { return }
            self.isBusy = false
            guard input == (self.field.text ?? "") else { return } // FIX:late
            switch result {
            case .success: self.accepted = input
            case .failure(let failure): self.error = failure
            }
        }
    }
}
#endif

@MainActor public final class FakePreferenceSource {
    public var value = false
    public var deliver: (() -> Void)?
    private var pending: [() -> Void] = []
    public init() {}
    public func queue() { if let deliver { pending.append(deliver) } }
    public func drainFirst() { if !pending.isEmpty { pending.removeFirst()() } }
    public func drainAll() { while !pending.isEmpty { pending.removeFirst()() } }
}

@MainActor public final class PreferenceScreen {
    public let source: FakePreferenceSource
    public private(set) var applied: [Bool] = []
    private var generation = 0
    private var last: Bool?
    public init(source: FakePreferenceSource) { self.source = source }
    public func start() {
        generation += 1
        let ticket = generation
        last = source.value                       // restart reads and caches the current value
        source.deliver = { [weak self] in
            guard let self else { return }
            guard self.generation == ticket else { return } // FIX:observer
            let value = self.source.value
            guard value != self.last else { return } // deduplicate
            self.last = value
            self.applied.append(value)
        }
    }
    public func stop() { generation += 1; source.deliver = nil }
}

#if !os(tvOS)
@MainActor public final class CaptionStore {
    public struct Choice { public let id: String; public let option: AVMediaSelectionOption }
    public let player: AVPlayer
    public private(set) var choices: [Choice] = []
    public private(set) var selectedID: String?
    private var group: AVMediaSelectionGroup?
    private var generation = 0
    public init(player: AVPlayer) { self.player = player }
    public func load() async throws {
        generation += 1
        guard let item = player.currentItem else { group = nil; choices = []; return }
        let loaded = try await item.asset.loadMediaSelectionGroup(for: .legible)
        group = loaded
        choices = (loaded?.options ?? []).enumerated().map { Choice(id: "\($0.offset)", option: $0.element) }
    }
    public var selection: Binding<String?> {
        let ticket = generation, owner = player.currentItem
        return Binding(get: { self.selectedID }, set: { id in
            guard self.generation == ticket, self.player.currentItem === owner else { return }
            self.choose(id)
        })
    }
    public func choose(_ id: String?) {
        guard let item = player.currentItem, let group else { return }
        if let id {
            guard let choice = choices.first(where: { $0.id == id }) else { return }
            item.select(choice.option, in: group) // FIX:media
        } else {
            guard group.allowsEmptySelection else { return }
            item.select(nil, in: group) // FIX:media
        }
        selectedID = id
    }
}
#endif
