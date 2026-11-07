import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
private final class ModalHarness {
    let root: TelevisionFocusRoot
    let primary: UIButton
    let fallback: UIButton
    var seen: [UIButton] = []
    var accepted = true
    lazy var restore = TelevisionModalRestore(root: root) { [weak self] target in
        guard let self else { return false }; self.seen.append(target); return self.accepted
    }
    init() {
        
        root = TelevisionFocusRoot(); primary = UIButton(type: .system); fallback = UIButton(type: .system)
        root.addSubview(primary); root.addSubview(fallback)
    }
    func begin() -> Int { restore.begin(primary: primary, fallback: fallback) }
}

@MainActor
private final class PreferenceHarness {
    let center = NotificationCenter()
    var snapshot = DisplayPreferences()
    var applied: [DisplayPreferences] = []
    var reads = 0
    var jobs: [@MainActor @Sendable () -> Void] = []
    lazy var observer = TelevisionPreferences(center: center, read: { [unowned self] in
        reads += 1; return snapshot
    }, enqueue: { [weak self] action in
        MainActor.assumeIsolated { self?.jobs.append(action) }
    }, apply: { [unowned self] value in applied.append(value) })
    func post(_ index: Int = 0) { center.post(name: TelevisionPreferences.names[index], object: nil) }
    func drain() { let pending = jobs; jobs = []; pending.forEach { $0() } }
}

@MainActor
final class TelevisionLifecycleTests: XCTestCase {
    func testBeginDoesNotRequestFocus() { let h = ModalHarness(); _ = h.begin(); XCTAssertTrue(h.seen.isEmpty) }
    func testCompletedModalRequestsOriginal() { let h = ModalHarness(); XCTAssertTrue(h.restore.finish(h.begin())); XCTAssertTrue(h.seen.first === h.primary) }
    func testRemovedOriginalUsesFallback() { let h = ModalHarness(); let token = h.begin(); h.primary.removeFromSuperview(); XCTAssertTrue(h.restore.finish(token)); XCTAssertTrue(h.seen.first === h.fallback) }
    func testHiddenAncestorUsesFallback() { let h = ModalHarness(); let group = UIView(); h.root.addSubview(group); group.addSubview(h.primary); let token = h.begin(); group.isHidden = true; XCTAssertTrue(h.restore.finish(token)); XCTAssertTrue(h.seen.first === h.fallback) }
    func testDisabledOriginalUsesFallback() { let h = ModalHarness(); let token = h.begin(); h.primary.isEnabled = false; XCTAssertTrue(h.restore.finish(token)); XCTAssertTrue(h.seen.first === h.fallback) }
    func testForeignOriginalUsesFallback() { let h = ModalHarness(); let token = h.begin(); let other = UIView(); other.addSubview(h.primary); XCTAssertTrue(h.restore.finish(token)); XCTAssertTrue(h.seen.first === h.fallback) }
    func testOldCompletionCannotConsumeNewSession() { let h = ModalHarness(); let old = h.begin(); let current = h.restore.begin(primary: h.fallback, fallback: nil); XCTAssertFalse(h.restore.finish(old)); XCTAssertTrue(h.seen.isEmpty); XCTAssertTrue(h.restore.finish(current)); XCTAssertTrue(h.seen.first === h.fallback) }
    func testDuplicateCompletionIsQuiet() { let h = ModalHarness(); let token = h.begin(); XCTAssertTrue(h.restore.finish(token)); XCTAssertFalse(h.restore.finish(token)); XCTAssertEqual(h.seen.count, 1) }
    func testCancellationRejectsLateCompletion() { let h = ModalHarness(); let token = h.begin(); h.restore.cancel(token); XCTAssertFalse(h.restore.finish(token)); XCTAssertTrue(h.seen.isEmpty) }
    func testOldCancellationPreservesCurrentSession() { let h = ModalHarness(); let old = h.begin(), current = h.begin(); h.restore.cancel(old); XCTAssertTrue(h.restore.finish(current)) }
    func testNoEligibleTargetDoesNotRequest() { let h = ModalHarness(); let token = h.begin(); h.primary.isHidden = true; h.fallback.isEnabled = false; XCTAssertFalse(h.restore.finish(token)); XCTAssertTrue(h.seen.isEmpty) }
    func testRequestRejectionIsReturned() { let h = ModalHarness(); h.accepted = false; XCTAssertFalse(h.restore.finish(h.begin())); XCTAssertEqual(h.seen.count, 1) }
    func testReentrantRequestPreservesNewSession() {
        let h = ModalHarness(); var next: Int?, calls = 0; var r: TelevisionModalRestore!
        r = TelevisionModalRestore(root: h.root) { _ in calls += 1; if next == nil { next = r.begin(primary: h.fallback, fallback: nil) }; return true }
        let first = r.begin(primary: h.primary, fallback: nil)
        XCTAssertTrue(r.finish(first)); XCTAssertNotNil(next); XCTAssertTrue(r.finish(next!)); XCTAssertEqual(calls, 2); r = nil
    }
    func testHiddenRootPreventsRequest() { let h = ModalHarness(); let token = h.begin(); h.root.isHidden = true; XCTAssertFalse(h.restore.finish(token)); XCTAssertTrue(h.seen.isEmpty) }
    func testPreferenceInitialSnapshot() { let h = PreferenceHarness(); h.snapshot.reduceMotion = true; h.observer.start(); XCTAssertEqual(h.applied, [h.snapshot]); XCTAssertEqual(h.reads, 1) }
    func testPreferenceStartIsIdempotent() { let h = PreferenceHarness(); h.observer.start(); h.observer.start(); h.post(); XCTAssertEqual(h.jobs.count, 1); XCTAssertEqual(h.reads, 1) }
    func testPreferenceIdenticalValuesAreDeduplicated() { let h = PreferenceHarness(); h.observer.start(); h.post(); h.drain(); XCTAssertEqual(h.applied.count, 1); XCTAssertEqual(h.reads, 2) }
    func testPreferenceMotionChange() { let h = PreferenceHarness(); h.observer.start(); h.snapshot.reduceMotion = true; h.post(); h.drain(); XCTAssertTrue(h.applied.last!.reduceMotion) }
    func testPreferenceTransparencyChange() { let h = PreferenceHarness(); h.observer.start(); h.snapshot.reduceTransparency = true; h.post(1); h.drain(); XCTAssertTrue(h.applied.last!.reduceTransparency); XCTAssertFalse(h.applied.last!.reduceMotion) }
    func testPreferenceContrastChange() { let h = PreferenceHarness(); h.observer.start(); h.snapshot.increaseContrast = true; h.post(2); h.drain(); XCTAssertTrue(h.applied.last!.increaseContrast) }
    func testPreferenceStoppedQueuedWorkIgnored() { let h = PreferenceHarness(); h.observer.start(); h.post(); h.observer.stop(); h.snapshot.reduceMotion = true; h.drain(); XCTAssertEqual(h.reads, 1); XCTAssertEqual(h.applied.count, 1) }
    func testPreferenceStopRemovesObservers() { let h = PreferenceHarness(); h.observer.start(); h.observer.stop(); for name in TelevisionPreferences.names { h.center.post(name: name, object: nil) }; XCTAssertTrue(h.jobs.isEmpty) }
    func testPreferenceRestartRefreshesSnapshot() { let h = PreferenceHarness(); h.observer.start(); h.observer.stop(); h.snapshot.reduceTransparency = true; h.observer.start(); XCTAssertEqual(h.reads, 2); XCTAssertTrue(h.applied.last!.reduceTransparency) }
    func testPreferenceOldGenerationIgnoredAfterRestart() { let h = PreferenceHarness(); h.observer.start(); h.post(); h.observer.stop(); h.observer.start(); h.drain(); XCTAssertEqual(h.reads, 2) }
    func testPreferenceOtherCenterIgnored() { let h = PreferenceHarness(); h.observer.start(); NotificationCenter().post(name: TelevisionPreferences.names[0], object: nil); XCTAssertTrue(h.jobs.isEmpty) }
    func testPreferenceDeinitRemovesObservers() {
        let center = NotificationCenter(); let queue = PreferenceHarness(); weak var weakObserver: TelevisionPreferences?
        autoreleasepool {
            let observer = TelevisionPreferences(center: center, read: {DisplayPreferences()}, enqueue: { action in MainActor.assumeIsolated { queue.jobs.append(action) } }, apply: {_ in})
            weakObserver = observer; observer.start()
        }
        XCTAssertNil(weakObserver); for name in TelevisionPreferences.names { center.post(name: name, object: nil) }; XCTAssertTrue(queue.jobs.isEmpty)
    }
    func testTransparentAncestorUsesFallback() { let h = ModalHarness(); let group = UIView(); h.root.addSubview(group); group.addSubview(h.primary); group.alpha = 0; XCTAssertTrue(h.restore.finish(h.begin())); XCTAssertTrue(h.seen.first === h.fallback) }
    func testDefaultRequestUpdatesPreferredTarget() { let root = FocusSpyRoot(); let button = UIButton(type: .system); root.addSubview(button); let r = TelevisionModalRestore(root: root); XCTAssertTrue(r.finish(r.begin(primary: button, fallback: nil))); XCTAssertEqual(root.requests, 1); XCTAssertTrue(root.preferredFocusEnvironments.first === button) }
    func testPreferredTargetRevalidatedAfterRemoval() { let root = FocusSpyRoot(); let button = UIButton(type: .system); root.addSubview(button); root.restorationTarget = button; button.removeFromSuperview(); XCTAssertTrue(root.preferredFocusEnvironments.isEmpty) }
}

@MainActor
private final class FocusSpyRoot: TelevisionFocusRoot {
    var requests = 0
    override func setNeedsFocusUpdate() { requests += 1 }
}
