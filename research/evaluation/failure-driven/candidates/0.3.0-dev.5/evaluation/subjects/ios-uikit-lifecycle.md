I am using UIKit on iOS 26 deployment target; available validation anchor iOS 26.5.

Closing a details panel should return attention to the item that opened it. The list may reorder or delete that item while the panel is open. Dismissal completion can arrive twice, and a new panel can open before an old completion runs. Describe the ownership and restoration-request logic and focused unit tests. Do not require UI automation.

This is a design/debugging question; no existing project or omitted source files are available. If code is useful, supply a self-contained minimal example and state material assumptions. Do not execute anything.
