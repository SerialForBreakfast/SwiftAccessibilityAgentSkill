var pending: [(id: String, name: String, reply: @MainActor (Bool) -> Void)] = []
let model = AccountsModel(
    accounts: [Account(id: "work", name: "Work"), Account(id: "home", name: "Home"), Account(id: "news", name: "News")],
    save: { id, name, reply in pending.append((id, name, reply)) })

// A saved rename closes the popover, keeps the new name and returns to the row.
model.beginRename("work")
model.draftName = "Work Mail"
model.commitRename()
guard pending.count == 1, pending[0].id == "work", pending[0].name == "Work Mail" else { return false }
pending[0].reply(true)
guard model.renamingID == nil, model.accounts.first(where: { $0.id == "work" })?.name == "Work Mail",
      model.focus == .account("work") else { return false }

// Cancelling also returns to the row.
model.focus = nil
model.beginRename("news")
model.cancelRename()
guard model.renamingID == nil, model.focus == .account("news") else { return false }

// The account disappears while its save is in flight: the list receives focus.
model.focus = nil
model.beginRename("home")
model.draftName = "House"
model.commitRename()
guard pending.count == 2 else { return false }
model.refresh([Account(id: "work", name: "Work Mail"), Account(id: "news", name: "News")])
pending[1].reply(true)
guard model.renamingID == nil, model.focus == .accountList else { return false }

// A slow save answers after the person cancelled and opened another account's popover.
model.focus = nil
model.beginRename("work")
model.draftName = "Office"
model.commitRename()
guard pending.count == 3 else { return false }
model.cancelRename()
guard model.focus == .account("work") else { return false }
model.focus = nil
model.beginRename("news")
let before = model.focus
pending[2].reply(true)
guard model.renamingID == "news", model.focus == before else { return false }

// The current rename still completes normally.
model.draftName = "Headlines"
model.commitRename()
guard pending.count == 4, pending[3].id == "news" else { return false }
pending[3].reply(true)
return model.renamingID == nil && model.focus == .account("news")
    && model.accounts.first(where: { $0.id == "news" })?.name == "Headlines"
