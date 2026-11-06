# Configured UIKit Color Contrast

UPAIR-03 candidate: nine unit tests and four deliberate defects. This is a numerical
check of configured opaque colors, not a screenshot audit or accessibility certification.
The skill, frozen baselines and existing evidence-tier system remain unchanged.

## Evidence Sources

[Apple color resolution](https://developer.apple.com/documentation/uikit/uicolor/resolvedcolor(with:))
and [Core Graphics conversion](https://developer.apple.com/documentation/coregraphics/cgcolor/converted(to:intent:options:))
support obtaining components in a specified color space for explicit traits.
Installed header hashes are recorded in [Apple source provenance](apple-sdk-sources.json).

The [W3C luminance and ratio definitions](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)
supply the sRGB calculation. [Threshold guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
supports comparing an unrounded result. Their distinct provenance is in
[supplemental sources](supplemental-sources.json). These are not Apple API claims.
Pure numerical tests link to W3C sources or project validation policy; integrated
checks also link to Apple APIs. The existing Apple-only manifest validator is unchanged.

## Bounded Contract

- Resolve both colors using explicit light/dark and normal/high contrast traits.
- Convert to sRGB with relative-colorimetric intent before interpreting components.
- Reject nonfinite/out-of-range numerical inputs and invalid thresholds.
- Reject translucent colors: this fixture has no compositing/backdrop model.
- Record the configured `.label`/`.systemBackground` pair in four trait contexts.
  Its chosen4.5 threshold is a project check at the tested anchor, not a guarantee
  for all semantic colors, platforms, backgrounds or OS releases.

Conversion selects an sRGB representation; it does not simulate a display, HDR,
materials, blending, antialiasing or actual pixel output. Pattern colors are rejected
by implementation, but this tranche does not independently exercise that branch.
Wider-gamut conversion behavior is not exhaustively covered; the known linear-sRGB
fixture exercises a concrete source-space conversion with a numerical oracle.

## Reproduce and Review

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-contrast-v1/manifest.json contrast-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-contrast-v1/manifest.json contrast-unit \
  /private/tmp/uikit-contrast-new IOS26_SIMULATOR_UUID
```

Other checks: `compile-contrast`, `nolinearization-negative`, `wrongcolorspace-negative`,
`ignoredtraits-negative`, `ignoredalpha-negative`. Use fresh private output directories.
See [coverage](coverage.json), [mutations](MUTATIONS.md), [difficulties](DIFFICULTIES.md)
and [native results](validation/README.md). The [developer question](evaluation/prompt.json)
and [controller rubric](evaluation/controller.md) remain separate development drafts;
independent review and model evaluation are not implied by native passes.
