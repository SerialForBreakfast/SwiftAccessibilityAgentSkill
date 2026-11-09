@MainActor final class Sheet {
    private(set) var visible: String?
    private var next = 0
    private var resolver: (([String]) -> String)?
    func open(_ origin: String) -> Int {
        next += 1
        visible = origin
        resolver = { $0.first(where: { $0 == origin }) ?? "fallback" }
        return next
    }
    func close() { visible = nil }
    func finish(_ id: Int, _ available: [String], _ request: (String) -> Void) {
        guard id == next, let resolve = resolver else { return }
        resolver = nil
        request(resolve(available))
    }
}
