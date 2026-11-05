// swift-tools-version: 6.0
import PackageDescription
let package = Package(
    name: "OS26Fixtures",
    platforms: [.iOS("26.0"), .tvOS("26.0")],
    products: [.library(name: "OS26Fixtures", targets: ["OS26Fixtures"])],
    targets: [
        .target(name: "OS26Fixtures"),
        .testTarget(name: "OS26FixturesTests", dependencies: ["OS26Fixtures"])
    ]
)
