import SwiftUI
import Observation

struct Account: Identifiable, Equatable {
    let id: String
    var name: String
}

enum SidebarFocus: Hashable {
    case accountList
    case account(String)
}

@MainActor @Observable
final class AccountsModel {
    var accounts: [Account]
    var renamingID: String?
    var draftName = ""
    var focus: SidebarFocus?
    private(set) var saving = false
    private let save: @MainActor (String, String, @escaping @MainActor (Bool) -> Void) -> Void

    init(accounts: [Account], save: @escaping @MainActor (String, String, @escaping @MainActor (Bool) -> Void) -> Void) {
        self.accounts = accounts
        self.save = save
    }

    func beginRename(_ id: String) {
        guard let account = accounts.first(where: { $0.id == id }) else { return }
        draftName = account.name
        renamingID = id
    }

    func commitRename() {
        guard let id = renamingID else { return }
        let name = draftName.trimmingCharacters(in: .whitespaces)
        guard !name.isEmpty else { return }
        saving = true
        save(id, name) { ok in
            self.saving = false
            if ok, let index = self.accounts.firstIndex(where: { $0.id == id }) {
                self.accounts[index].name = name
            }
            self.renamingID = nil
        }
    }

    func cancelRename() {
        guard renamingID != nil else { return }
        renamingID = nil
        saving = false
    }

    // Server push: the account list can change at any time.
    func refresh(_ latest: [Account]) {
        accounts = latest
    }
}

struct AccountsSidebar: View {
    @Bindable var model: AccountsModel
    @FocusState private var focused: SidebarFocus?

    var body: some View {
        List {
            ForEach(model.accounts) { account in
                Text(account.name)
                    .focusable()
                    .focused($focused, equals: .account(account.id))
                    .contextMenu {
                        Button("Rename…") { model.beginRename(account.id) }
                    }
                    .popover(isPresented: Binding(
                        get: { model.renamingID == account.id },
                        set: { if !$0 { model.cancelRename() } })) {
                        VStack(alignment: .trailing) {
                            TextField("Account name", text: $model.draftName)
                                .onSubmit { model.commitRename() }
                            HStack {
                                if model.saving { ProgressView().controlSize(.small) }
                                Button("Cancel") { model.cancelRename() }
                                    .keyboardShortcut(.cancelAction)
                                Button("Rename") { model.commitRename() }
                                    .keyboardShortcut(.defaultAction)
                                    .disabled(model.saving)
                            }
                        }
                        .padding()
                        .frame(width: 260)
                    }
            }
        }
        .focused($focused, equals: .accountList)
        .onChange(of: model.focus) { _, target in focused = target }
    }
}
