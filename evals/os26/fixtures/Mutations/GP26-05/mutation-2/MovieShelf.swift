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
    let movies: [Movie]
    let open: (Movie) -> Void
    public init(movies: [Movie], open: @escaping (Movie) -> Void) {
        self.movies = movies; self.open = open
    }
    // PATCH BEGIN GP26-05
    func activate(_ movie: Movie) { open(movies[0]) }
    public var body: some View {
        ScrollView(.horizontal) {
            HStack {
                ForEach(movies) { movie in
                    Button { activate(movie) } label: {
                        VStack {
                            Image(movie.posterName).accessibilityHidden(true)
                            Text(movie.title)
                        }.frame(width: 240, height: 360)
                    }
                    .accessibilityLabel(movie.title)
                }
            }.padding()
        }
    }
    // PATCH END GP26-05
}
#endif
