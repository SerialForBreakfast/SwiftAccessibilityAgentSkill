import SwiftUI
import XCTest
@testable import Presentation

@MainActor final class ItemTests: XCTestCase {
    func testRegisteredItems() async throws {
        #if os(iOS)
        let first = Item(id: UUID(), name: "first"), second = Item(id: UUID(), name: "second")
        let model = DetailsCoordinator(items: [first, second])
        let host = UIHostingController(rootView: ItemListView(coordinator: model))
        let window = UIWindow(frame: CGRect(x: 0, y: 0, width: 400, height: 800))
        window.rootViewController = host; window.isHidden = false
        defer { window.isHidden = true; window.rootViewController = nil }
        #else
        let model = BookmarksModel(bookmarks: [Bookmark(id: "first", title: "A", url: "")])
        let host = NSHostingView(rootView: BookmarksView(model: model))
        host.frame = NSRect(x: 0, y: 0, width: 400, height: 200)
        let window = NSWindow(contentRect: host.frame, styleMask: .borderless, backing: .buffered, defer: false)
        window.contentView = host
        defer { window.contentView = nil }
        #endif
        defer { ItemRegistration.byID.removeAll() }
        func retained(_ id: UUID) async throws -> () -> Void {
            for _ in 0..<150 {
                #if os(iOS)
                host.view.layoutIfNeeded()
                #else
                host.layoutSubtreeIfNeeded()
                #endif
                if let callback = ItemRegistration.byID[id] { return callback }
                try await Task.sleep(nanoseconds: 10_000_000)
            }
            throw XCTSkip("item registration not observed")
        }
        #if os(iOS)
        model.presentDetails(for: first.id)
        let a = try await retained(XCTUnwrap(model.activeSession).token)
        model.presentDetails(for: second.id)
        let b = try await retained(XCTUnwrap(model.activeSession).token)
        a(); XCTAssertEqual(model.focusRequestCount, 0, "late A")
        b(); XCTAssertEqual(model.focusRequestCount, 1, "first B")
        XCTAssertEqual(model.requestedFocusID, second.id)
        b(); XCTAssertEqual(model.focusRequestCount, 1, "repeat B")
        #else
        model.edit("first")
        let a = try await retained(XCTUnwrap(model.editing).id)
        model.duplicateAndEdit("first")
        let b = try await retained(XCTUnwrap(model.editing).id)
        model.editing = nil
        a(); XCTAssertNil(model.focus, "late A")
        b(); XCTAssertEqual(model.focus, .editButton("first-copy"), "first B")
        b(); XCTAssertEqual(model.focus, .editButton("first-copy"), "repeat B")
        #endif
    }
}
