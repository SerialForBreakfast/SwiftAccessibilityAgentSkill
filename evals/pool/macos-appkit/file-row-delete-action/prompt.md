macOS 26.0, AppKit.

In our Files table, VoiceOver users have to interact with each row and arrow over to the Delete button to delete a file. Can you add Delete to the row's VoiceOver Actions menu (VO-Command-Space) on `FileRowView`, so it's available as soon as they land on the row? Mouse and keyboard users use the buttons, and the table reuses rows as the list refreshes.

Keep `FileItem`, `FileRowView`, `configure(with:onOpen:onDelete:)`, `openButton` and `deleteButton` with their current names, types and behavior.
