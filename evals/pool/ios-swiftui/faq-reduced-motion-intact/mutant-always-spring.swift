import SwiftUI
import Observation

struct FAQEntry: Identifiable, Equatable {
    let id: String
    let question: String
    let answer: String
}

@MainActor @Observable
final class FAQModel {
    let entries: [FAQEntry]
    private(set) var expandedID: String?
    /// Analytics: which answers people read.
    var didExpand: (String) -> Void = { _ in }

    init(entries: [FAQEntry]) { self.entries = entries }

    func toggle(_ id: String) {
        guard entries.contains(where: { $0.id == id }) else { return }
        if expandedID == id {
            expandedID = nil
        } else {
            expandedID = id
            didExpand(id)
        }
    }

    func isExpanded(_ id: String) -> Bool { expandedID == id }

    /// Expanding springs the answer open; with Reduce Motion the answer simply appears.
    static func expansionAnimation(reduceMotion: Bool) -> Animation? {
        // A hard cut is disorienting; always give the answer a visible transition.
        .spring(duration: 0.45, bounce: 0.3)
    }
}

struct FAQView: View {
    let model: FAQModel
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        List(model.entries) { entry in
            VStack(alignment: .leading, spacing: 8) {
                Button {
                    withAnimation(FAQModel.expansionAnimation(reduceMotion: reduceMotion)) {
                        model.toggle(entry.id)
                    }
                } label: {
                    HStack {
                        Text(entry.question).font(.headline)
                        Spacer()
                        Image(systemName: "chevron.down")
                            .rotationEffect(.degrees(model.isExpanded(entry.id) ? 180 : 0))
                            .accessibilityHidden(true)
                    }
                }
                .accessibilityValue(model.isExpanded(entry.id) ? "Expanded" : "Collapsed")

                if model.isExpanded(entry.id) {
                    Text(entry.answer)
                        .transition(.move(edge: .top).combined(with: .opacity))
                }
            }
        }
        .navigationTitle("Help")
    }
}
