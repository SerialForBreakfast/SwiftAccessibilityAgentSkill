// swift-tools-version: 6.0
import PackageDescription
let package = Package(name: "AccessibilityExamples", platforms: [.iOS("26.0")], products: [.library(name: "AccessibilityExamples", targets: ["AccessibilityExamples"])], targets: [.target(name: "AccessibilityExamples"), .testTarget(name: "AccessibilityExamplesTests", dependencies: ["AccessibilityExamples"])])
