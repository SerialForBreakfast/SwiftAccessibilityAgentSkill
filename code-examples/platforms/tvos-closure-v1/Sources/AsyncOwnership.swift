import UIKit
import AVFoundation

@MainActor
final class ValidationOwner {
    typealias Validator = ([String: String], @escaping @MainActor ([String: String]) -> Void) -> Void
    let order = ["name", "email"]
    let fields: [String: UITextField] = ["name": UITextField(), "email": UITextField()]
    let status = UILabel()
    private(set) var errors: [String: String] = [:]
    private(set) var busy = false
    private var generation = 0
    private var active: Int?
    private let validate: Validator
    private let request: (UITextField) -> Void
    private let accept: ([String: String]) -> Void
    init(validate: @escaping Validator, request: @escaping (UITextField) -> Void = { _ in }, accept: @escaping ([String: String]) -> Void = { _ in }) {
        self.validate = validate; self.request = request; self.accept = accept
        for id in order { fields[id]?.accessibilityLabel = id }
    }
    var snapshot: [String: String] { fields.mapValues { $0.text ?? "" } }
    func edit(_ id: String, _ text: String) {
        guard let field = fields[id] else { return }
        field.text = text; cancel()
    }
    func cancel() {
        generation += 1; active = nil; busy = false; errors = [:]; status.text = ""
    }
    func submit() {
        generation += 1
        let ticket = generation, input = snapshot
        active = ticket; busy = true; errors = [:]; status.text = "Checking"
        validate(input) { [weak self] result in
            guard let self, self.active == ticket else { return }
            guard self.snapshot == input else { self.cancel(); return }
            // Consume before calling client code that can begin another request.
            self.active = nil; self.busy = false
            guard result.keys.allSatisfy({ self.fields[$0] != nil }), result.values.allSatisfy({ !$0.isEmpty }) else {
                self.status.text = "Validation unavailable"; return
            }
            self.errors = result
            if let id = self.order.first(where: { result[$0] != nil }), let field = self.fields[id] {
                self.status.text = result[id]!
                self.request(field)
            } else {
                self.status.text = "Ready"; self.accept(input)
            }
        }
    }
}

@MainActor
final class MediaLoadOwner {
    typealias Loader = (AVPlayerItem, @escaping @MainActor (Result<String, Error>) -> Void) -> Void
    let player = AVPlayer()
    private(set) var value: String?
    private(set) var state = "unavailable"
    private var generation = 0
    private var active: Int?
    func replace(_ item: AVPlayerItem?, load: Loader) {
        generation += 1; let ticket = generation
        active = nil; value = nil
        player.replaceCurrentItem(with: item)
        guard let item else { state = "unavailable"; return }
        active = ticket; state = "loading"
        load(item) { [weak self, weak item] result in
            guard let self, self.active == ticket else { return }
            guard let item, self.player.currentItem === item else {
                self.active = nil; self.state = "superseded"; return
            }
            self.active = nil
            switch result {
            case .success(let value): self.value = value; self.state = "loaded"
            case .failure: self.value = nil; self.state = "failed"
            }
        }
    }
    func cancel() { generation += 1; active = nil; value = nil; state = "cancelled" }
}
