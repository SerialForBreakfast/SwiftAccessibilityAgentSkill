import XCTest
import SwiftUI
#if os(macOS)
import AppKit
#else
import UIKit
#endif
@testable import AccessibilityExamples

@MainActor final class InteropTests: XCTestCase {
    func button() -> BridgeButton {
        #if os(macOS)
        NSButton(title: "", target: nil, action: nil)
        #else
        UIButton(type: .system)
        #endif
    }
    func label(_ button: BridgeButton) -> String? {
        #if os(macOS)
        button.accessibilityLabel()
        #else
        button.accessibilityLabel
        #endif
    }
    func testCoordinatorUpdatesCurrentNameAndEnabledState() { let c = BridgeOwner(), b = button(); c.configure(b, title: "One", enabled: false, handler: {}); c.configure(b, title: "Two", enabled: true, handler: {}); XCTAssertEqual(label(b), "Two"); XCTAssertTrue(b.isEnabled) }
    func testCoordinatorReplacesOldCallback() { let c = BridgeOwner(), b = button(); var values: [String] = []; c.configure(b, title: "One", enabled: true, handler: { values.append("old") }); let old = c.action(); c.configure(b, title: "Two", enabled: true, handler: { values.append("new") }); old(); c.action()(); XCTAssertEqual(values, ["new"]) }
    func testNativeActionDispatchUsesCurrentHandlerOnce() { let c = BridgeOwner(), b = button(); var n = 0; for _ in 0..<3 { c.configure(b, title: "Open", enabled: true, handler: { n += 1 }) }
        #if os(macOS)
        b.performClick(nil)
        #else
        b.sendActions(for: .primaryActionTriggered)
        #endif
        XCTAssertEqual(n, 1)
    }
    func testOldNativeViewCannotDispatchAfterRebind() { let c = BridgeOwner(), old = button(), current = button(); var n = 0; c.configure(old, title: "Old", enabled: true, handler: {}); c.configure(current, title: "Current", enabled: true, handler: { n += 1 });
        #if os(macOS)
        old.performClick(nil)
        #else
        old.sendActions(for: .primaryActionTriggered)
        #endif
        XCTAssertEqual(n, 0)
    }
    func testExternallyDisabledButtonRejectsCallback() { let c = BridgeOwner(), b = button(); var n = 0; c.configure(b, title: "Open", enabled: true, handler: { n += 1 }); b.isEnabled = false; c.action()(); XCTAssertEqual(n, 0) }
    func testDismantleRejectsRetainedAction() { let c = BridgeOwner(), b = button(); var n = 0; c.configure(b, title: "Open", enabled: true, handler: { n += 1 }); let action = c.action(); c.stop(); action(); XCTAssertEqual(n, 0) }
    func testRetainedCallbackDoesNotRetainCoordinator() { var c: BridgeOwner? = BridgeOwner(); let b = button(); c!.configure(b, title: "Open", enabled: true, handler: {}); weak var owner = c; let action = c!.action(); c = nil; action(); XCTAssertNil(owner) }
    func testCoordinatorDoesNotRetainNativeView() {
        let c = BridgeOwner(); weak var view: BridgeButton?
        autoreleasepool {
            let b = button(); view = b
            c.configure(b, title: "Open", enabled: true, handler: {})
        }
        XCTAssertNil(view)
    }
    func testUnownedNativeViewLifetimeAfterAutoreleasePool() {
        weak var view: BridgeButton?
        autoreleasepool { let b = button(); view = b }
        XCTAssertNil(view)
    }
    func testPublicDismantleStopsCoordinator() { let c = BridgeOwner(), b = button(); var n = 0; c.configure(b, title: "Open", enabled: true, handler: { n += 1 });
        #if os(macOS)
        NativeButtonExample.dismantleNSView(b, coordinator: c)
        #else
        NativeButtonExample.dismantleUIView(b, coordinator: c)
        #endif
        c.action()(); XCTAssertEqual(n, 0)
    }
}
