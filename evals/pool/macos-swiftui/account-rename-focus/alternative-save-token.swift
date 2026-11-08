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
    private var activeSave: UUID?
    private let save: @MainActor (String, String, @escaping @MainActor (Bool) -> Void) -> Void

    init(accounts: [Account], save: @escaping @MainActor (String, String, @escaping @MainActor (Bool) -> Void) -> Void) {
        self.accounts = accounts
        self.save = save
    }

    func beginRename(_ id: String) {
        guard let account = accounts.first(where: { $0.id == id }) else { return }
        activeSave = nil
        draftName = account.name
        renamingID = id
    }

    func commitRename() {
        guard let id = renamingID else { return }
        let name = draftName.trimmingCharacters(in: .whitespaces)
        guard !name.isEmpty else { return }
        let token = UUID()
        activeSave = token
        saving = true
        save(id, name) { [weak self] ok in
            guard let self else { return }
            if ok { self.applyName(name, to: id) }
            guard self.activeSave == token else { return }
            self.activeSave = nil
            self.saving = false
            self.renamingID = nil
            self.focus = self.target(for: id)
        }
    }

    private func applyName(_ name: String, to id: String) {
        guard let index = accounts.firstIndex(where: { $0.id == id }) else { return }
        accounts[index].name = name
    }

    private func target(for id: String) -> SidebarFocus {
        accounts.first(where: { $0.id == id }) == nil ? .accountList : .account(id)
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
