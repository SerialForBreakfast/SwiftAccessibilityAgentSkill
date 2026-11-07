import SwiftUI
import Observation

struct Article: Identifiable, Equatable {
    let id: String
    var title: String
    var important: Bool
}

@MainActor @Observable
final class DocumentState {
    private(set) var entries: [Article] = []
    private(set) var selected: String?
    private var revision = 0
    var chosen: (String) -> Void = { _ in }
    var deleted: (String) -> Void = { _ in }
    var landmarks: [Article] { entries.filter(\.important) }
    @discardableResult func replace(_ next: [Article]) -> Bool {
        guard Set(next.map(\.id)).count == next.count else { return false }
        revision += 1; entries = next
        if let selected, !next.contains(where: { $0.id == selected }) { self.selected = nil }
        return true
    }
    func action(for id: String, remove: Bool = false) -> () -> Void {
        let generation = revision
        return { [weak self] in
            guard let self, self.revision == generation,
                  self.entries.contains(where: { $0.id == id }) else { return }
            if remove {
                self.entries.removeAll { $0.id == id }; self.revision += 1
                if self.selected == id { self.selected = nil }
                self.deleted(id)
            } else { self.selected = id; self.chosen(id) }
        }
    }
}

struct DocumentExample: View {
    @Bindable var state: DocumentState
    var body: some View {
        List {
            Section {
                ForEach(state.entries) { article in
                    VStack(alignment: .leading) {
                        Button(article.title, action: state.action(for: article.id))
                            .id(article.id)
                        Button("Delete \(article.title)", action: state.action(for: article.id, remove: true))
                    }
                    .accessibilityElement(children: .contain)
                    .accessibilityActions {
                        Button("Delete \(article.title)", action: state.action(for: article.id, remove: true))
                    }
                }
            } header: {
                Text("Articles").accessibilityAddTraits(.isHeader)
            }
        }
        .accessibilityRotor("Important articles", entries: state.landmarks, entryLabel: \.title)
    }
}
