import UIKit
import SwiftUI
import XCTest
@testable import Presentation

@MainActor final class Hosted: XCTestCase {
    func testRetainedRegistrations() async throws {
        var calls = [String]()
        var caller = "setup"
        let bID = UUID()
        let state = SheetPresentationCoordinator(eligibilityResolver: { _ in true }, onRestoration: {
            calls.append(caller + ($0 == .item(bID) ? ":B" : ":other"))
        })
        let host = UIHostingController(rootView: DetailsSheetContainerView(coordinator: state))
        let window = UIWindow(frame: CGRect(x: 0, y: 0, width: 400, height: 800))
        window.rootViewController = host
        window.isHidden = false
        defer { window.isHidden = true; window.rootViewController = nil; Registrations.shown = nil }
        func callback(after rev: Int, shown: Bool) async throws -> () -> Void {
            for _ in 0..<100 {
                host.view.layoutIfNeeded()
                if Registrations.revision > rev, let pair = Registrations.shown, pair.0.wrappedValue == shown { return pair.1 }
                try await Task.sleep(nanoseconds: 10_000_000)
            }
            throw XCTSkip("host gap: registration did not update")
        }
        _ = try await callback(after: 0, shown: false)
        var rev = Registrations.revision
        state.open(from: .item(UUID()))
        let a = try await callback(after: rev, shown: true)
        rev = Registrations.revision
        state.close()
        _ = try await callback(after: rev, shown: false)
        rev = Registrations.revision
        state.open(from: .item(bID))
        let b = try await callback(after: rev, shown: true)
        state.close()
        XCTAssertEqual(calls, [])
        caller = "late-A"; a()
        XCTAssertEqual(calls, [], "late A must not restore")
        caller = "first-B"; b()
        XCTAssertEqual(calls, ["first-B:B"], "first B owns restoration")
        caller = "repeat-B"; b()
        XCTAssertEqual(calls, ["first-B:B"], "repeat B must be quiet")
    }
}
