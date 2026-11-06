import XCTest
import UIKit
import AVFoundation
@testable import AccessibilityExamples

@MainActor
final class MediaInspectionTests: XCTestCase {
    private func time(_ seconds: Int64) -> CMTime { CMTime(value: seconds, timescale: 1) }
    private func range(_ start: Int64, _ length: Int64) -> CMTimeRange {
        CMTimeRange(start: time(start), duration: time(length))
    }
    private func snapshot(duration: CMTime? = nil, kind: StreamKind = .unknown,
                          seekable: [CMTimeRange]? = nil, loaded: [CMTimeRange]? = nil,
                          full: Bool? = nil, likely: Bool? = nil,
                          rate: Float = 0, status: AVPlayer.TimeControlStatus = .paused) -> MediaInspection {
        MediaInspection(duration: duration, kind: kind, seekable: seekable, loaded: loaded,
            bufferEmpty: nil, bufferFull: full, likelyToKeepUp: likely,
            requestedRate: rate, timeControlStatus: status, waitingReason: nil)
    }

    func testDurationCategoriesRemainDistinct() {
        XCTAssertEqual(DurationEvidence(nil), .unavailable)
        XCTAssertEqual(DurationEvidence(.invalid), .invalid)
        XCTAssertEqual(DurationEvidence(.indefinite), .indefinite)
        XCTAssertEqual(DurationEvidence(.positiveInfinity), .infinite)
        XCTAssertEqual(DurationEvidence(.negativeInfinity), .infinite)
        XCTAssertEqual(DurationEvidence(time(-1)), .invalid)
        XCTAssertEqual(DurationEvidence(.zero), .finite(0))
        XCTAssertEqual(DurationEvidence(CMTime(value: 3, timescale: 2)), .finite(1.5))
    }

    func testIndefiniteDoesNotInventLiveClassification() {
        XCTAssertEqual(snapshot(duration: .indefinite).kind, .unknown)
        XCTAssertEqual(snapshot(duration: time(60), kind: .live).kind, .live)
        XCTAssertEqual(snapshot(duration: .indefinite, kind: .onDemand).kind, .onDemand)
    }

    func testLoadedRangesDoNotAuthorizeSeeking() {
        let value = snapshot(duration: time(100), seekable: [range(20, 10)], loaded: [range(0, 100)])
        XCTAssertEqual(value.containsSeekableTime(time(5)), false)
        XCTAssertEqual(value.containsSeekableTime(time(25)), true)
        XCTAssertEqual(value.loaded?.count, 1)
        XCTAssertEqual(value.loaded?.first?.duration, time(100))
    }

    func testDiscontinuousRangesPreserveGapsAndHalfOpenEnds() {
        let value = snapshot(seekable: [range(10, 5), range(30, 5)])
        XCTAssertEqual(value.containsSeekableTime(time(10)), true)
        XCTAssertEqual(value.containsSeekableTime(time(15)), false)
        XCTAssertEqual(value.containsSeekableTime(time(20)), false)
        XCTAssertEqual(value.containsSeekableTime(time(30)), true)
        XCTAssertEqual(value.containsSeekableTime(time(35)), false)
    }

    func testUnavailableAndEmptyRangesDiffer() {
        XCTAssertNil(snapshot().containsSeekableTime(time(0)))
        XCTAssertEqual(snapshot(seekable: []).containsSeekableTime(time(0)), false)
        XCTAssertEqual(snapshot(seekable: [range(0, 10)]).containsSeekableTime(.indefinite), false)
        XCTAssertEqual(snapshot(seekable: [.invalid, range(0, 0)]).containsSeekableTime(time(0)), false)
    }

    func testFullBufferDoesNotImplyLikelyToKeepUp() {
        let value = snapshot(full: true, likely: false)
        XCTAssertEqual(value.bufferFull, true)
        XCTAssertEqual(value.likelyToKeepUp, false)
        XCTAssertNil(value.bufferEmpty)
    }

    func testWaitingStatusDoesNotBecomePlayingFromRate() {
        let value = snapshot(rate: 1, status: .waitingToPlayAtSpecifiedRate)
        XCTAssertEqual(value.requestedRate, 1)
        XCTAssertEqual(value.timeControlStatus, .waitingToPlayAtSpecifiedRate)
    }

    func testWaitingReasonAndIndependentFlagsArePreserved() {
        let value = MediaInspection(duration: .invalid, seekable: [], loaded: [],
            bufferEmpty: true, bufferFull: false, likelyToKeepUp: false, requestedRate: 1,
            timeControlStatus: .waitingToPlayAtSpecifiedRate, waitingReason: "future-reason")
        XCTAssertEqual(value.waitingReason, "future-reason")
        XCTAssertEqual(value.bufferEmpty, true)
        XCTAssertEqual(value.bufferFull, false)
        XCTAssertEqual(value.likelyToKeepUp, false)
    }

    func testEmptyNativePlayerCaptureAndControlMetadataRemainUnchanged() {
        let player = AVPlayer()
        let button = UIButton(type: .system)
        button.accessibilityLabel = "Play"
        button.accessibilityValue = "Paused"
        let value = MediaInspection.capture(player)
        XCTAssertEqual(value.duration, .unavailable)
        XCTAssertNil(value.seekable)
        XCTAssertNil(value.loaded)
        XCTAssertNil(value.bufferFull)
        XCTAssertEqual(value.requestedRate, 0)
        XCTAssertEqual(value.timeControlStatus, .paused)
        XCTAssertNil(player.currentItem)
        XCTAssertEqual(button.accessibilityLabel, "Play")
        XCTAssertEqual(button.accessibilityValue, "Paused")
    }
}
