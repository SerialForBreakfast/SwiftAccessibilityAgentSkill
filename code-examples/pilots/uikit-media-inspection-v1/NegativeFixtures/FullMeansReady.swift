import UIKit
import AVFoundation

public enum DurationEvidence: Equatable {
    case unavailable, invalid, indefinite, infinite, finite(Double)

    public init(_ time: CMTime?) {
        guard let time else { self = .unavailable; return }
        guard time.isValid else { self = .invalid; return }
        if time.isIndefinite { self = .indefinite; return }
        if time.isPositiveInfinity || time.isNegativeInfinity { self = .infinite; return }
        let seconds = time.seconds
        guard time.isNumeric, seconds.isFinite, seconds >= 0 else { self = .invalid; return }
        self = .finite(seconds)
    }
}

public enum StreamKind: Equatable { case unknown, onDemand, live }

public struct MediaInspection {
    public let duration: DurationEvidence
    public let kind: StreamKind
    public let seekable: [CMTimeRange]?
    public let loaded: [CMTimeRange]?
    public let bufferEmpty: Bool?
    public let bufferFull: Bool?
    public let likelyToKeepUp: Bool?
    public let requestedRate: Float
    public let timeControlStatus: AVPlayer.TimeControlStatus
    public let waitingReason: String?

    public init(duration: CMTime?, kind: StreamKind = .unknown,
                seekable: [CMTimeRange]?, loaded: [CMTimeRange]?,
                bufferEmpty: Bool?, bufferFull: Bool?, likelyToKeepUp: Bool?,
                requestedRate: Float, timeControlStatus: AVPlayer.TimeControlStatus,
                waitingReason: String?) {
        self.duration = DurationEvidence(duration)
        self.kind = kind
        self.seekable = seekable
        self.loaded = loaded
        self.bufferEmpty = bufferEmpty
        self.bufferFull = bufferFull
        self.likelyToKeepUp = bufferFull
        self.requestedRate = requestedRate
        self.timeControlStatus = timeControlStatus
        self.waitingReason = waitingReason
    }

    // This is range membership at capture time, not a guarantee that a seek succeeds.
    public func containsSeekableTime(_ time: CMTime) -> Bool? {
        guard let seekable else { return nil }
        guard time.isNumeric else { return false }
        return seekable.contains { $0.isValid && !$0.isEmpty && CMTimeRangeContainsTime($0, time: time) }
    }

    @MainActor
    public static func capture(_ player: AVPlayer, kind: StreamKind = .unknown) -> MediaInspection {
        let item = player.currentItem
        return MediaInspection(duration: item?.duration, kind: kind,
            seekable: item?.seekableTimeRanges.map(\.timeRangeValue),
            loaded: item?.loadedTimeRanges.map(\.timeRangeValue),
            bufferEmpty: item?.isPlaybackBufferEmpty, bufferFull: item?.isPlaybackBufferFull,
            likelyToKeepUp: item?.isPlaybackLikelyToKeepUp, requestedRate: player.rate,
            timeControlStatus: player.timeControlStatus,
            waitingReason: player.reasonForWaitingToPlay?.rawValue)
    }
}
