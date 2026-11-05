import XCTest
import SwiftUI
@testable import OS26Fixtures

final class SwiftUIContractTests: XCTestCase {
    #if os(iOS)
    @MainActor func testMessageActions() {
        var deleted: [String] = []
        let first = MessageRow(message: Message(id: "a", subject: "Alpha")) { deleted.append($0.id) }
        let second = MessageRow(message: Message(id: "b", subject: "Bravo")) { deleted.append($0.id) }
        XCTAssertEqual(deleted, [])
        first.handleSwipe(translation: 0)
        first.handleSwipe(translation: -80)
        first.handleSwipe(translation: 100)
        XCTAssertEqual(deleted, [])
        first.deleteMessage()
        second.deleteMessage()
        first.handleSwipe(translation: -81)
        second.handleSwipe(translation: -100)
        XCTAssertEqual(deleted, ["a", "b", "a", "b"])
    }

    @MainActor func testNotificationBinding() {
        var stored = false
        var writes: [Bool] = []
        let binding = Binding<Bool>(get: { stored }, set: { stored = $0; writes.append($0) })
        let settings = NotificationSettings(notificationsEnabled: binding)
        XCTAssertFalse(settings.toggleBinding.wrappedValue)
        XCTAssertTrue(writes.isEmpty)
        settings.toggleBinding.wrappedValue = true
        XCTAssertTrue(stored)
        XCTAssertTrue(settings.toggleBinding.wrappedValue)
        settings.toggleBinding.wrappedValue = false
        XCTAssertFalse(stored)
        XCTAssertEqual(writes, [true, false])
    }
    #endif

    #if os(tvOS)
    @MainActor func testMovieActivation() {
        let movies = ["first", "middle", "last"].map { Movie(id: $0, title: $0, posterName: "Poster") }
        var opened: [String] = []
        let shelf = MovieShelf(movies: movies) { opened.append($0.id) }
        XCTAssertTrue(opened.isEmpty)
        for movie in movies { shelf.activate(movie) }
        XCTAssertEqual(opened, ["first", "middle", "last"])
    }
    #endif
}
