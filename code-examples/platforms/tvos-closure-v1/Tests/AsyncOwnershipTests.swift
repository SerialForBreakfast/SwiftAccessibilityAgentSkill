import XCTest
import UIKit
import AVFoundation
@testable import AccessibilityExamples

@MainActor
final class AsyncOwnershipTests: XCTestCase {
    typealias Reply = @MainActor ([String: String]) -> Void
    private var replies: [Reply] = []
    private func owner(request: @escaping (UITextField) -> Void = { _ in }, accept: @escaping ([String:String]) -> Void = { _ in }) -> ValidationOwner {
        ValidationOwner(validate: { [weak self] _, reply in self?.replies.append(reply) }, request: request, accept: accept)
    }
    func testPendingStateAndSnapshotPreserveInput() {
        let o = owner(); o.edit("name", "  Name  "); o.submit()
        XCTAssertTrue(o.busy); XCTAssertEqual(o.snapshot["name"], "  Name  ")
        XCTAssertEqual(o.status.text, "Checking")
    }
    func testOutOfOrderReplyCannotReplaceLatestErrors() {
        let o = owner(); o.submit(); o.submit()
        replies[1](["email":"Current"]); replies[0](["name":"Old"])
        XCTAssertEqual(o.errors, ["email":"Current"]); XCTAssertFalse(o.busy)
    }
    func testEditInvalidatesInFlightResult() {
        var accepted = 0; let o = owner(accept: { _ in accepted += 1 })
        o.submit(); o.edit("email", "new"); replies[0]([:])
        XCTAssertEqual(accepted, 0); XCTAssertFalse(o.busy); XCTAssertEqual(o.snapshot["email"], "new")
    }
    func testCancelRejectsLateReply() {
        let o = owner(); o.submit(); o.cancel(); replies[0](["name":"Late"])
        XCTAssertTrue(o.errors.isEmpty); XCTAssertEqual(o.status.text, "")
    }
    func testNativeFieldMutationCannotApplyOldSnapshot() {
        var accepted = 0; let o = owner(accept: { _ in accepted += 1 }); o.submit()
        o.fields["name"]?.text = "Changed outside adapter"; replies[0]([:])
        XCTAssertEqual(accepted, 0); XCTAssertFalse(o.busy)
    }
    func testFirstInvalidUsesDeclaredFieldOrder() {
        var target: UITextField?; let o = owner(request: { target = $0 }); o.submit()
        replies[0](["email":"Email issue", "name":"Name issue"])
        XCTAssertTrue(target === o.fields["name"]); XCTAssertEqual(o.status.text, "Name issue")
    }
    func testDuplicateReplyCannotAcceptTwice() {
        var count = 0; let o = owner(accept: { _ in count += 1 }); o.submit()
        replies[0]([:]); replies[0]([:]); XCTAssertEqual(count, 1)
    }
    func testUnknownFieldAndEmptyErrorAreNotSuccess() {
        var count = 0; let o = owner(accept: { _ in count += 1 })
        o.submit(); replies[0](["unknown":"Error"])
        XCTAssertEqual(o.status.text, "Validation unavailable")
        o.submit(); replies[1](["name":""]); XCTAssertEqual(count, 0)
        XCTAssertEqual(o.status.text, "Validation unavailable")
    }
    func testSynchronousCompletionWorks() {
        var count = 0; let o = ValidationOwner(validate: { _, done in done([:]) }, accept: { _ in count += 1 })
        o.submit(); XCTAssertFalse(o.busy); XCTAssertEqual(count, 1)
    }
    func testReentrantAcceptancePreservesNewRequest() {
        var o: ValidationOwner!; var count = 0
        o = owner(accept: { _ in count += 1; if count == 1 { o.submit() } })
        o.submit(); replies[0]([:]); XCTAssertTrue(o.busy); XCTAssertEqual(replies.count, 2)
        replies[0](["name":"stale"]); XCTAssertTrue(o.busy); o = nil
    }
    func testRetainedReplyDoesNotRetainForm() {
        var o: ValidationOwner? = owner(); weak var weakOwner = o
        o?.submit(); o = nil; XCTAssertNil(weakOwner); replies[0]([:])
    }
    func testSuccessRecoversAfterErrorAndKeepsFieldIdentity() {
        var count = 0; let o = owner(accept: { _ in count += 1 }); let field = o.fields["name"]
        o.submit(); replies[0](["name":"Error"]); o.edit("name", "Fixed")
        o.submit(); replies[1]([:]); XCTAssertEqual(count, 1); XCTAssertTrue(o.fields["name"] === field)
        XCTAssertTrue(o.errors.isEmpty); XCTAssertEqual(o.status.text, "Ready")
    }
}

@MainActor
final class MediaLoadOwnerTests: XCTestCase {
    typealias Reply = @MainActor (Result<String, Error>) -> Void
    enum Failure: Error { case sample }
    private func item() -> AVPlayerItem { AVPlayerItem(asset: AVMutableComposition()) }
    func testNilItemDoesNotInvokeLoader() {
        let o = MediaLoadOwner(); var calls = 0
        o.replace(nil) { _, _ in calls += 1 }; XCTAssertEqual(calls, 0); XCTAssertEqual(o.state, "unavailable")
    }
    func testReplacementRejectsOldItemCompletion() {
        let o = MediaLoadOwner(); var a: Reply!, b: Reply!
        o.replace(item()) { _, reply in a = reply }; o.replace(item()) { _, reply in b = reply }
        b(.success("new")); a(.success("old")); XCTAssertEqual(o.value, "new")
    }
    func testSameItemNewRequestRejectsOldGeneration() {
        let o = MediaLoadOwner(), i = item(); var a: Reply!, b: Reply!
        o.replace(i) { _, r in a = r }; o.replace(i) { _, r in b = r }
        a(.success("old")); XCTAssertNil(o.value); XCTAssertEqual(o.state, "loading")
        b(.success("new")); XCTAssertEqual(o.value, "new")
    }
    func testExternalReplacementRejectsOldResult() {
        let o = MediaLoadOwner(); var done: Reply!
        let original = item(); o.replace(original) { _, r in done = r }; o.player.replaceCurrentItem(with: item())
        withExtendedLifetime(original) { done(.success("old")) }; XCTAssertNil(o.value); XCTAssertEqual(o.state, "superseded")
    }
    func testCancellationRejectsLateSuccess() {
        let o = MediaLoadOwner(); var done: Reply!
        o.replace(item()) { _, r in done = r }; o.cancel(); done(.success("late"))
        XCTAssertNil(o.value); XCTAssertEqual(o.state, "cancelled")
    }
    func testErrorIsNotMissingOrSuccessfulMetadata() {
        let o = MediaLoadOwner(); o.replace(item()) { _, done in done(.failure(Failure.sample)) }
        XCTAssertEqual(o.state, "failed"); XCTAssertNil(o.value)
    }
    func testDuplicateCallbackCannotOverwriteFirstResult() {
        let o = MediaLoadOwner(); o.replace(item()) { _, done in done(.success("first")); done(.success("second")) }
        XCTAssertEqual(o.value, "first")
    }
    func testInspectionDoesNotChangePlayerPreferences() {
        let o = MediaLoadOwner(); o.player.volume = 0.3; o.player.isMuted = true
        o.replace(item()) { _, done in done(.success("snapshot")) }
        XCTAssertEqual(o.player.volume, 0.3, accuracy: 0.001); XCTAssertTrue(o.player.isMuted); XCTAssertEqual(o.player.rate, 0)
    }
    func testRetainedLoaderReplyDoesNotRetainOwner() {
        var o: MediaLoadOwner? = MediaLoadOwner(); weak var weakOwner = o; var done: Reply!
        o?.replace(item()) { _, r in done = r }; o = nil; XCTAssertNil(weakOwner); done(.success("late"))
    }
}
