import UIKit

enum ContrastError: Error, Equatable {
    case invalidComponent
    case translucent
    case unsupportedColor
    case invalidThreshold
}

struct OpaqueSRGB {
    let red: Double
    let green: Double
    let blue: Double

    init(red: Double, green: Double, blue: Double) throws {
        guard [red, green, blue].allSatisfy({ $0.isFinite && (0...1).contains($0) }) else {
            throw ContrastError.invalidComponent
        }
        self.red = red
        self.green = green
        self.blue = blue
    }

    private static func linear(_ value: Double) -> Double {
        value <= 0.04045 ? value / 12.92 : pow((value + 0.055) / 1.055, 2.4)
    }

    var luminance: Double {
        0.2126 * Self.linear(red) + 0.7152 * Self.linear(green) + 0.0722 * Self.linear(blue)
    }

    func contrast(with other: Self) -> Double {
        let a = luminance, b = other.luminance
        return (max(a, b) + 0.05) / (min(a, b) + 0.05)
    }

    func meets(_ threshold: Double, against other: Self) throws -> Bool {
        guard threshold.isFinite && (1...21).contains(threshold) else {
            throw ContrastError.invalidThreshold
        }
        return contrast(with: other) >= threshold
    }
}

@MainActor
enum ConfiguredContrast {
    static func resolve(_ color: UIColor, traits: UITraitCollection) throws -> OpaqueSRGB {
        let original = color.resolvedColor(with: traits).cgColor
        guard original.alpha == 1 else { throw ContrastError.translucent }
        guard original.colorSpace?.model != .pattern,
              let space = CGColorSpace(name: CGColorSpace.sRGB),
              let converted = original.converted(to: space, intent: .relativeColorimetric, options: nil),
              let values = converted.components, values.count == 4 else {
            throw ContrastError.unsupportedColor
        }
        return try OpaqueSRGB(red: Double(values[0]), green: Double(values[1]), blue: Double(values[2]))
    }

    static func ratio(foreground: UIColor, background: UIColor, traits: UITraitCollection) throws -> Double {
        let foreground = try resolve(foreground, traits: traits)
        let background = try resolve(background, traits: traits)
        return foreground.contrast(with: background)
    }
}
