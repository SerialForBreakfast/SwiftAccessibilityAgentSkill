# Independent review packet: AppKit and tvOS first batch

Status: prepared locally; not sent, accepted or independently reviewed.

## Inputs

- [Scope, families and reproduction](README.md)
- [Executed results](RESULTS.md) and [machine-readable attempts](results-index.json)
- [Apple sources](SOURCES.md), [coverage queue](COVERAGE.md)
- [Preserved difficulties](DIFFICULTIES.md)
- [Candidate read traces](retrieval-measurements.json)

## Review priorities

1. Audit each of the five prompt/rubric pairs for neutral language, enough developer
   context and valid alternative implementations. Preserve original answers if a
   later model run is authorized; this packet does not authorize one.
2. Verify ordinary actions remain available alongside shortcuts on both platforms.
   Inspect stale action ownership, disabled-state behavior and visible labels.
3. Audit the Mac autorelease-pool oracle correction, distinguishing framework
   temporary lifetime from a callback cycle. Keep first failure intact.
4. Verify exact intended assertion failures for ten mutants and the separate
   original-title-defect regression. Do not classify infrastructure failures as rejection.
5. Audit source/member availability, keeping unresolved dates explicit. SDK27 with
   target26 and Mac27 host evidence must not be represented as Mac26 runtime evidence.
6. Inspect routing selection and actual reads: no AppKit/UIKit/SwiftUI conflation,
   no iOS-only fallback into tvOS, no source/test archive in default context.

Return findings by family, severity, source/test IDs and accepted alternatives.
Separate factual corrections, oracle defects, coverage gaps and optional preferences.
Report review as draft/reviewed/accepted explicitly. Do not modify the released
skill, frozen baselines or existing UIKit evidence as part of this review.

## Later evaluation gate

After review, freeze this development overlay and request bounded frontier-model
quota/scope approval. Use the same developer questions across C0-C3, retain actual
lookup traces and score correctness separately from routing/identity. Compare
bytes/tokens only where observed; these offline traces are not model benchmarks.
