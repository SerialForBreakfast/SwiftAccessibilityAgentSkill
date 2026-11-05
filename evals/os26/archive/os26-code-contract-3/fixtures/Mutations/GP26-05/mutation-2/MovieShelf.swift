#if os(tvOS)
import SwiftUI
public struct Movie: Identifiable {
    public let id: String
    public let title: String
    public let posterName: String
    public init(id: String, title: String, posterName: String) {
        self.id = id; self.title = title; self.posterName = posterName
    }
}
public struct MovieShelf: View {
    @FocusState private var focusedMovie: String?
    let movies: [Movie]
    let open: (Movie) -> Void
    public init(movies: [Movie], open: @escaping (Movie) -> Void) {
        self.movies = movies; self.open = open
    }
    // PATCH BEGIN GP26-05
    public var body: some View {
        ScrollView(.horizontal) {
            HStack {
                ForEach(movies) { movie in
                    Button { open(movie) } label: {
                        VStack {
                            Image(movie.posterName).accessibilityHidden(true)
                            Text(movie.title)
                        }.frame(width: 240, height: 360)
                    }
                    .accessibilityLabel(movie.title)
                    .focused($focusedMovie, equals: movie.id)
                }
            }.padding()
            .onChange(of: UUID()) { _, _ in focusedMovie = movies.first?.id }
        }
    }
    // PATCH END GP26-05
}
#endif
