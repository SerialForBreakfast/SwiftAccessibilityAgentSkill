iOS 26.0, UIKit.

VoiceOver testers say the Now Playing screen sometimes announces the wrong episode: the title shows an episode that isn't the one playing. Title lookups can be slow. The player is shared with our Up Next queue and CarPlay, so episodes can change without this screen being involved. Can you fix `NowPlayingViewController`?

Keep `NowPlayingViewController`, `MetadataLoader`, `init(player:loadTitle:)`, `player`, `titleLabel`, `playPauseButton`, `play(_:)` and `togglePlayback()` with their current names and signatures.
