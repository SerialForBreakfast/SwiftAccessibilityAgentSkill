# Media source evidence

Reviewed November 6, 2026. [Source index](source-index.json) pins actual retrieved
Apple markdown and SDK27 AVFoundation headers separately for Mac and TV.

| Source | Supporting section and use |
| --- | --- |
| [AVPlayerItem.select](https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:in:)) | Parameters/Discussion: option and group relationship, current item asset, empty-selection permission and choice among matching options |
| [Description characteristic](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/describesvideoforaccessibility) | Characteristic meaning; AVMediaFormat.h explicitly documents tagging for MOV/M4V |
| [Seekable ranges](https://developer.apple.com/documentation/avfoundation/avplayeritem/seekabletimeranges) | Discussion: discrete ranges can be discontinuous, not equivalent to loaded ranges |
| Installed AVAsset.h | Async group loading returns a group, nil or error; Swift deprecation guidance points away from synchronous access |
| Installed AVMediaSelectionGroup.h / AVMediaSelection.h | Empty-selection permission, option characteristics and selected option query |
| Installed AVPlayerItem.h / AVPlayer.h | Item ranges/buffer properties and player rate/time-control/waiting state |

The requested async Swift-loader markdown URL returned HTTP404. No page content
was inferred; AVAsset.h supplied the scoped declaration/behavior evidence instead.
This is an access gap, not a claim that the API is missing.

## Availability

The async group loader declaration is macOS12/tvOS15; its synchronous Swift
predecessor is deprecated from macOS13/tvOS16. The description characteristic
has explicit macOS10.8/tvOS9 annotations. Target26 compilation with SDK27 is
recorded separately from actual Mac27.0 and TV26.5 execution. Unannotated member
introductions are not invented. This is not a complete framework availability map.

## Policy and observation

Selecting full rather than forced-only subtitles, requiring description on an
explicit request, and preserving selection when no match exists are application
policies. Native APIs supply actual options, characteristics and selection state.
The off decision uses each group's reported permission, not its media type.
Inspection is observational and must not silently override user selection.

The fixture's tagged track is silent. It is suitable for testing tag extraction
and option selection, not description quality. Readiness, streaming, rendered
controls and actual assistive-tool delivery are separate from these unit contracts.
