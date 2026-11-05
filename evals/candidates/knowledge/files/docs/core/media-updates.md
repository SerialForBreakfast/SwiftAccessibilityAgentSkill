# Generated Subtitles and Style Selection

Reviewed: 2026-11-04. Evidence: Tier-1 Apple WWDC26 session 256,
Media authoring, Availability and support, Presenting subtitles, Style preview.
Status: source-supported candidate update.

Keep authored subtitle tracks. Generated subtitles supplement missing supported
languages; they do not justify removing authored accessibility content.

The session describes English transcription starting in OS 27 across iOS,
macOS, tvOS, and visionOS; translation support differs by platform. Check device,
language, and individual API availability rather than promising universal support.

Expose subtitle selection and selected state during playback. Standard AVKit
players provide selection and styling behavior. Custom player interfaces should
consider supported media-option menus and style previews, keeping controls
reachable and restoring playback presentation after a preview ends.

Source: [Discover generated subtitles and subtitle styles](https://developer.apple.com/videos/play/wwdc2026/256/).
