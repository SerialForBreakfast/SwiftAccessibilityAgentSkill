iOS 26.0, UIKit.

QA found two VoiceOver complaints on the Library sync strip. After a failed sync recovers, Retry still talks about the old error. And after pulling to refresh a couple of times in a row, the strip sometimes settles on a result that is older than what the server last said. Can you fix `SyncStatusView`?

Keep `SyncResult`, `SyncStatusView`, `Fetch`, `init(fetch:)`, `statusLabel`, `retryButton`, `retryCount`, `refresh()` and `retry()` with their current names and signatures.
