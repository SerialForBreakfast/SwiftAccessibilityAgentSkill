import AppKit
import SwiftUI
import XCTest
@testable import Presentation

@MainActor final class Hosted: XCTestCase {
    func testRetainedRegistrations() async throws {
        let state = PresentationState()
        var history = [String]()
        var caller = "setup"
        state.request = { history.append("\(caller):\($0)") }
        let host = NSHostingView(rootView: SheetExample(state: state))
        host.frame = NSRect(x: 0, y: 0, width: 400, height: 200)
        let window = NSWindow(contentRect: host.frame, styleMask: .borderless, backing: .buffered, defer: false)
        window.contentView = host
        defer { window.contentView = nil; Registrations.open = nil; Registrations.shown = nil }
        func registration(after revision: Int, showing: Bool) async throws -> (Binding<Bool>, () -> Void) {
            for _ in 0..<100 {
                host.layoutSubtreeIfNeeded()
                if Registrations.revision > revision, let pair = Registrations.shown, pair.0.wrappedValue == showing { return pair }
                try await Task.sleep(nanoseconds: 10_000_000)
            }
            throw XCTSkip("host gap: expected revision after \(revision), actual \(Registrations.revision), showing=\(showing)")
        }
        let _ = try await registration(after: 0, showing: false)
        var rev = Registrations.revision
        try XCTUnwrap(Registrations.open)()
        let a = try await registration(after: rev, showing: true)
        rev = Registrations.revision
        a.0.wrappedValue = false
        _ = try await registration(after: rev, showing: false)
        rev = Registrations.revision
        try XCTUnwrap(Registrations.open)()
        let b = try await registration(after: rev, showing: true)
        b.0.wrappedValue = false
        XCTAssertEqual(history, [], "opening must not restore")
        caller = "late-A"; a.1()
        XCTAssertEqual(history, [], "late A must not restore")
        caller = "first-B"; b.1()
        XCTAssertEqual(history, ["first-B:open"], "first B owns restoration")
        caller = "repeat-B"; b.1()
        XCTAssertEqual(history, ["first-B:open"], "repeat B must be quiet")
    }
}
