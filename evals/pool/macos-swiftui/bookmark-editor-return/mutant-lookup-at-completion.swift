import SwiftUI
import Observation

struct Bookmark: Identifiable, Equatable {
    let id: String
    var title: String
    var url: String
}

struct EditRequest: Identifiable, Equatable {
    let id = UUID()
    let bookmarkID: String
}

enum BookmarkFocus: Hashable {
    case addButton
    case editButton(String)
}

@MainActor @Observable
final class BookmarksModel {
    var bookmarks: [Bookmark]
    var editing: EditRequest?
    var focus: BookmarkFocus?
    private var currentOrigin: String?

    init(bookmarks: [Bookmark]) { self.bookmarks = bookmarks }

    func edit(_ id: String) {
        currentOrigin = id
        editing = EditRequest(bookmarkID: id)
    }

    func duplicateAndEdit(_ id: String) {
        guard let original = bookmarks.first(where: { $0.id == id }) else { return }
        let copy = Bookmark(id: original.id + "-copy", title: original.title + " copy", url: original.url)
        bookmarks.append(copy)
        currentOrigin = copy.id
        editing = EditRequest(bookmarkID: copy.id)
    }

    // Also called by iCloud sync when a bookmark is deleted on another Mac.
    func remove(_ id: String) {
        bookmarks.removeAll { $0.id == id }
    }

    func rename(_ id: String, to title: String) {
        guard let index = bookmarks.firstIndex(where: { $0.id == id }) else { return }
        bookmarks[index].title = title
    }

    func sheetDismissed() {
        guard let id = currentOrigin else { return }
        focus = bookmarks.contains(where: { $0.id == id }) ? .editButton(id) : .addButton
    }
}

struct BookmarkEditor: View {
    @Bindable var model: BookmarksModel
    let request: EditRequest
    @State private var title = ""
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Form {
            TextField("Title", text: $title)
            HStack {
                Button("Duplicate") { model.duplicateAndEdit(request.bookmarkID) }
                Spacer()
                Button("Cancel", role: .cancel) { dismiss() }
                    .keyboardShortcut(.cancelAction)
                Button("Save") {
                    model.rename(request.bookmarkID, to: title)
                    dismiss()
                }
                .keyboardShortcut(.defaultAction)
            }
        }
        .padding()
        .frame(minWidth: 360)
        .onAppear { title = model.bookmarks.first { $0.id == request.bookmarkID }?.title ?? "" }
    }
}

struct BookmarksView: View {
    @Bindable var model: BookmarksModel
    @FocusState private var focused: BookmarkFocus?

    var body: some View {
        VStack(alignment: .leading) {
            List(model.bookmarks) { bookmark in
                HStack {
                    Text(bookmark.title)
                    Spacer()
                    Button("Edit…") { model.edit(bookmark.id) }
                        .focused($focused, equals: .editButton(bookmark.id))
                }
            }
            Button("Add Bookmark") {
                let id = UUID().uuidString
                model.bookmarks.append(Bookmark(id: id, title: "New Bookmark", url: ""))
                model.edit(id)
            }
            .focused($focused, equals: .addButton)
            .padding()
        }
        .sheet(item: $model.editing, onDismiss: { model.sheetDismissed() }) { request in
            BookmarkEditor(model: model, request: request)
        }
        .onChange(of: model.focus) { _, target in focused = target }
    }
}
