import SwiftUI
struct DetailsScreen: View {
    @State private var presented = false
    var body: some View {
        Button("Open") { presented = true }
            .sheet(isPresented: $presented) {
                Button("Close") { presented = false }
            }
    }
}
