# macOS media selection declarations

Installed public SDK27; deployment26. These excerpts describe native AVFoundation
selection APIs. They do not establish SwiftUI-generated accessibility semantics.

## AVPlayerItem.select

```objc
- (void)selectMediaOption:(nullable AVMediaSelectionOption *)mediaSelectionOption inMediaSelectionGroup:(AVMediaSelectionGroup *)mediaSelectionGroup
#if AVF_DEPLOYING_TO_2022_RELEASES_AND_LATER
NS_SWIFT_NONISOLATED
#endif
API_AVAILABLE(macos(10.8), ios(5.0), tvos(9.0), watchos(1.0), visionos(1.0));
```

Source: AVPlayerItem.h:612; header SHA256 002344cd17c89bf2127a61d229ac63e0c59792809f0dda0e4927e0d5939c89e6.
Exact declaration annotations retained; no nearby-comment inference.

## AVPlayerItem.currentMediaSelection

```objc
@property (readonly) AVMediaSelection *currentMediaSelection NS_SWIFT_NONISOLATED API_AVAILABLE(macos(10.11), ios(9.0), tvos(9.0), watchos(2.0), visionos(1.0));
```

Source: AVPlayerItem.h:632; header SHA256 002344cd17c89bf2127a61d229ac63e0c59792809f0dda0e4927e0d5939c89e6.
Exact declaration annotations retained; no nearby-comment inference.

## AVAsset.loadMediaSelectionGroup

```objc
- (void)loadMediaSelectionGroupForMediaCharacteristic:(AVMediaCharacteristic)mediaCharacteristic completionHandler:(void (^ NS_SWIFT_SENDABLE)(AVMediaSelectionGroup * _Nullable_result, NSError * _Nullable))completionHandler API_AVAILABLE(macos(12.0), ios(15.0), tvos(15.0), watchos(8.0), visionos(1.0));
```

Source: AVAsset.h:412; header SHA256 78f593df2b6bcaa0103a0b3f4f53e5ddd61edde1b83d69267298a0370a43e742.
Exact declaration annotations retained; no nearby-comment inference.

## AVMediaSelectionGroup.allowsEmptySelection

```objc
@property (nonatomic, readonly) BOOL allowsEmptySelection;
```

Source: AVMediaSelectionGroup.h:44; header SHA256 ae5c280e4d1d342bba4b3eebf40487818e87753bdb79793333c4942b1b8cdb59.
No member-level annotation; enclosing declaration introduction not resolved in this capture.

## forced-only characteristic

```objc
AVF_EXPORT AVMediaCharacteristic const AVMediaCharacteristicContainsOnlyForcedSubtitles API_AVAILABLE(macos(10.8), ios(5.0), tvos(9.0), watchos(1.0), visionos(1.0));
```

Source: AVMediaFormat.h:152; header SHA256 5a85f66c94ff9425ea7848f9230ef15d2b1f8e597ea89ed36e8ac69ce92d8c2d.
Exact declaration annotations retained; no nearby-comment inference.

Example policies, snapshot ownership and observable notification are application
contracts. Actual compile/unit receipts are an optional companion, not proof of
spoken output, rendered captions, streaming metadata or universal OS coverage.
