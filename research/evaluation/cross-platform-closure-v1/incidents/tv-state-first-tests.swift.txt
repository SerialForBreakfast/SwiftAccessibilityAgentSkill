import XCTest
import UIKit
import AVKit
@testable import AccessibilityExamples

@MainActor
final class StateContractTests: XCTestCase {
    func testSearchThenSelectionDoesNotLeaveStaleLabel() {
        let r = RegionState(); r.search("report", count: 3)
        r.configure(name: "Report", selected: true, reduceTransparency: false)
        XCTAssertEqual(r.status.text, "Selected")
        XCTAssertEqual(r.status.accessibilityLabel ?? r.status.text, "Selected")
    }
    func testRepeatedSearchAndSelectionKeepCurrentStatus() {
        let r = RegionState(); r.configure(name: "Report", selected: true, reduceTransparency: false)
        r.search("", count: 0)
        XCTAssertEqual(r.status.accessibilityLabel ?? r.status.text, "0 results")
        r.configure(name: "Other", selected: false, reduceTransparency: true)
        XCTAssertEqual(r.status.accessibilityLabel ?? r.status.text, "Not selected")
    }
    func testRegionPreservesOrdinaryControlAndNamedBoundary() {
        let r = RegionState(); r.configure(name: "Open report", selected: false, reduceTransparency: false)
        XCTAssertTrue(r.button.superview === r)
        XCTAssertEqual(r.accessibilityLabel, "Downloads")
        XCTAssertEqual(r.button.accessibilityLabel, "Open report")
        XCTAssertEqual(r.accessibilityElements?.count, 3)
    }
    func testSelectedStateHasNonColorTextAndValue() {
        let r = RegionState(); r.configure(name: "Report", selected: true, reduceTransparency: false)
        XCTAssertEqual(r.status.text, "Selected")
        XCTAssertEqual(r.button.accessibilityValue, "Selected")
    }
    func testReconfigureClearsStaleSelectionText() {
        let r = RegionState(); r.configure(name: "First", selected: true, reduceTransparency: false)
        r.configure(name: "Second", selected: false, reduceTransparency: false)
        XCTAssertEqual(r.button.accessibilityLabel, "Second")
        XCTAssertEqual(r.status.text, "Not selected")
    }
    func testReducedTransparencyDoesNotRemoveContent() {
        let r = RegionState(); r.configure(name: "Report", selected: false, reduceTransparency: true)
        XCTAssertTrue(r.backdrop.isHidden); XCTAssertFalse(r.button.isHidden); XCTAssertFalse(r.status.isHidden)
        r.configure(name: "Report", selected: false, reduceTransparency: false); XCTAssertFalse(r.backdrop.isHidden)
    }
    func testNativePlayerControlsAndPlayerArePreserved() {
        let p = AVPlayer(), view = RegionState.player(p)
        XCTAssertTrue(view.player === p)
        XCTAssertTrue(view.showsPlaybackControls)
    }
    func testModalFlagRestoresOriginalFalse() {
        let view = UIView(), scope = ModalFlag(UIView())
        let s = ModalFlag(view); s.begin(); XCTAssertTrue(view.accessibilityViewIsModal)
        s.end(); XCTAssertFalse(view.accessibilityViewIsModal); scope.end()
    }
    func testRepeatedModalBeginRestoresOriginalTrue() {
        let view = UIView(); view.accessibilityViewIsModal = true
        let s = ModalFlag(view); s.begin(); s.begin(); s.end(); s.end()
        XCTAssertTrue(view.accessibilityViewIsModal)
    }
    func testSearchQueryAndResultCountRemainVisible() {
        let r = RegionState(); r.search("cats", count: 4)
        XCTAssertEqual(r.query.text, "cats"); XCTAssertEqual(r.query.accessibilityLabel, "Search downloads")
        XCTAssertEqual(r.status.text, "4 results"); XCTAssertEqual(r.status.accessibilityLabel, "4 results")
    }
    func testSelectionPreservesUnrelatedTraits() {
        let r = RegionState(); r.button.accessibilityTraits.insert(.startsMediaSession)
        r.configure(name: "X", selected: true, reduceTransparency: false)
        r.configure(name: "X", selected: false, reduceTransparency: false)
        XCTAssertTrue(r.button.accessibilityTraits.contains(.startsMediaSession)); XCTAssertFalse(r.button.accessibilityTraits.contains(.selected))
    }
    func testTextUsesFlexibleSemanticConfigurationWithoutOS27Claim() {
        let r = RegionState(); XCTAssertEqual(r.status.numberOfLines, 0)
        XCTAssertEqual(r.status.lineBreakMode, .byWordWrapping); XCTAssertTrue(r.status.adjustsFontForContentSizeCategory)
        XCTAssertNotNil(r.status.font)
    }
}
