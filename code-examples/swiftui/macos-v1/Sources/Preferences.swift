import SwiftUI

struct PresentationPolicy: Equatable {
    var reduceMotion = false
    var reduceTransparency = false
    var differentiateWithoutColor = false
    var expandedText = false
    var animate: Bool { !reduceMotion }
    var selectedText: String { "Selected" }
    var opaqueBackground: Bool { reduceTransparency }
    var vertical: Bool { expandedText }
}

@MainActor
struct TextPreferenceExample: View {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @Environment(\.accessibilityReduceTransparency) private var reduceTransparency
    @Environment(\.accessibilityDifferentiateWithoutColor) private var differentiate
    #if !os(tvOS)
    @Environment(\.dynamicTypeSize) private var typeSize
    @ScaledMetric(relativeTo: .body) private var spacing = 12.0
    #endif
    let title: String
    let selected: Bool
    private var policy: PresentationPolicy {
        #if os(tvOS)
        PresentationPolicy(reduceMotion: reduceMotion, reduceTransparency: reduceTransparency, differentiateWithoutColor: differentiate)
        #else
        PresentationPolicy(reduceMotion: reduceMotion, reduceTransparency: reduceTransparency, differentiateWithoutColor: differentiate, expandedText: typeSize.isAccessibilitySize)
        #endif
    }
    var body: some View {
        let layout = policy.vertical ? AnyLayout(VStackLayout(alignment: .leading)) : AnyLayout(HStackLayout())
        layout {
            Text(title).font(.body).fixedSize(horizontal: false, vertical: true)
            Text(selected ? "Selected" : "Not selected")
            if policy.differentiateWithoutColor && selected { Image(systemName: "checkmark").accessibilityHidden(true) }
        }
        #if !os(tvOS)
        .padding(spacing)
        #endif
        .background(policy.opaqueBackground ? Color.primary.opacity(0.1) : Color.clear)
        .animation(policy.animate ? .default : nil, value: selected)
    }
}
