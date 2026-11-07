# Visible owner request

The following is the visible implementation request, quoted without claiming access
to provider-internal context:

```text
PLEASE IMPLEMENT THIS PLAN:
# SwiftUI Failure-Driven Unit-Test Campaign

## Summary
Build one consolidated SwiftUI campaign across **iOS, macOS and tvOS**, covering all 15 existing SwiftUI guidelines. Deliver one review checkpoint, not small successive tranches.

Keep released skill files, frozen baselines and existing UIKit/AppKit evidence unchanged. No UI tests, mandatory manual verification, new model runs or paid dependencies.

## Implementation
- Inventory every guideline’s requirements. Classify each as directly unit-testable, compile-checkable, documentation-supported outside unit scope, or unresolved.
- Separate shared accessibility principles, SwiftUI-specific APIs and platform-specific behavior. Do not import UIKit defaults as SwiftUI expectations.
- Group implementation into semantics and native controls; containers/actions/rotors; text and preferences; lifecycle/focus requests; lists/forms/media.
- Build complete SwiftUI examples with focused units for observable bindings, state transitions, action handlers, identity, asynchronous ownership and configuration policies. Add targeted negative controls where meaningful.
- Compile actual SwiftUI modifier compositions for each platform. Do not describe testing an extracted model or constructing a view as proof of generated accessibility semantics.
- Use public APIs and existing native adapters. Hosting is permitted for in-process units where public behavior is observable; private view-tree introspection, reflection-based semantics assertions and new inspection dependencies are excluded.

## Failure Evidence and Evaluation Pairs
- Preserve each first source snapshot, diagnostics, environment and outcome before repair. Record implementation defects, oracle defects, harness errors and coverage gaps separately.
- Allow at most two documented repairs per failing contract; retain unresolved outcomes visibly.
- Pair each behavioral family with a natural developer question, complete starter inputs and an independent rubric accepting valid alternatives.
- Capture available authoring prompts, original outputs and separate analysis. Mark missing history explicitly.
- Record potential skill improvements as research findings linked to evidence, not immediate runtime guidance changes. Known incidents remain development cases, not holdouts.

## Execution and Acceptance
- Use installed SDKs and existing runtime anchors: iOS 26.5, tvOS 26.5 and macOS 27.0, subject to preflight verification. Record deployment targets separately.
- Run platform suites sequentially with immutable manifests and artifacts. Continue independent assertion checks; stop on infrastructure failures.
- Acceptance requires every inventoried requirement to have an explicit disposition, every claimed unit contract to link to matching execution evidence, and every new family to have its prompt/rubric pair.
- Report unique contracts, platform repetitions, methods, mutants and executions separately. Compilation does not establish spoken output, delivered focus, rendered layout or rotor discoverability.
- Finish with one consolidated coverage ledger, failure analysis, results report and independent-review packet. Git publication and worker messaging remain separately authorized; Claude stays pending.
```
