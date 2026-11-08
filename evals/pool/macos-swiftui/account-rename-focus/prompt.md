macOS 26, SwiftUI.

When someone renames an account from the sidebar's context menu, the popover closes after the server answers but keyboard focus goes nowhere, and VoiceOver users end up back at the top of the window. After a rename is saved or cancelled, focus should go back to that account's row. If a server refresh removed the account in the meantime, the account list itself is fine.

Saves can take several seconds. People sometimes cancel the popover and start renaming a different account before the first save has answered.

Keep `AccountsModel`, `Account`, `SidebarFocus`, `init(accounts:save:)`, `accounts`, `renamingID` (which account's popover is open), `draftName`, `focus`, `beginRename(_:)`, `commitRename()`, `cancelRename()` and `refresh(_:)` with their current names and types.
