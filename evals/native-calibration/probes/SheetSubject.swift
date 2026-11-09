@MainActor final class Sheet {
    private(set) var visible: String?
    private var session: (id: Int, origin: String)?
    private var next = 0
    func open(_ origin: String) -> Int {
        next += 1
        visible = origin
        session = (next, origin)
        return next
    }
    func close() { visible = nil }
    func finish(_ id: Int, _ available: [String], _ request: (String) -> Void) {
        guard let pending = session, pending.id == id else { return }
        session = nil
        request(available.contains(pending.origin) ? pending.origin : "fallback")
    }
}
