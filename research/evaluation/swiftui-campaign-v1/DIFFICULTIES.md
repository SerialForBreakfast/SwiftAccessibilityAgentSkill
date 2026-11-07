# Failure and gap analysis

## SUI-01: Old AppKit target dispatches into the new binding

Classification: accidental implementation defect, found during review and reproduced
by the first complete macOS unit suite. The initial coordinator replaced its current
button/handler but left the old button's target/action attached. A retained closure
had a generation check; the native selector called a newly created closure, so the
old control could invoke the new handler despite those closure tests.

Exact first source, test and manifest are in incidents/mac-first-*. Raw inputs,
commands, diagnostics and result bundles remain immutable in the private archive.
Repair1 detaches target/action from the previous AppKit button when rebinding to a
different view. The native old-view dispatch assertion passes after repair. This is
an actual native-entry-point test, not a SwiftUI accessibility-tree assertion.

Candidate skill lesson: test the real native entry point as well as captured closure
ownership. Platform-specific dispatch differences matter; a UIKit UIAction already
captures its generation, whereas the AppKit selector reads current coordinator state.
No released guidance changes follow automatically from this development incident.

## SUI-02: Weak lifetime assertion ignored autorelease timing

Classification: test-oracle lifetime defect, not a demonstrated coordinator leak.
The initial assertion expected a native button to disappear immediately after a local
optional was cleared. The coordinator's view reference was already weak. Repair1
scopes allocation/configuration in autoreleasepool and asserts after draining; a
separate native-view control without a coordinator uses the same pool boundary.
Both pass. The original failure is retained rather than rewritten as a successful
leak rejection. Compiler addresses are sanitized publicly; exact raw diagnostics
remain private. Do not transfer this oracle mistake into accessibility guidance.

## SUI-03: Source review found gaps that model units could not establish

Before final freeze, the native Toggle title did not consume the tested contextual
name, and a representation-only Circle lacked an ordinary activation path. These
were source-audit findings, not recorded compiler/unit failures. The final source
uses current name/status, and an ordinary Button shares the Toggle binding with its
accessibility representation. No fictitious failed test or runtime tree observation
is claimed. Future prompt/rubric review must inspect integration, not merely praise
green extracted-state tests.

## Scope and remaining gaps

- Real SwiftUI modifier composition is compiled, but no private reflection or generated
  accessibility-tree inspection is used. Unit models alone cannot prove modifier
  attachment, role output, rotor discoverability, environment propagation or focus.
- Direct public coordinator/update-helper calls and dismantle are tested. Broader
  interop container semantics and automatic hosting propagation remain unresolved.
- Media option state is synthetic and explicitly not AVMediaSelection application,
  captions rendering or audio-description-content validation.
- First Mac compile covers the initial source set (52 methods listed, no unit run).
  The first complete suite selects61 methods; repaired final suites select62,
  including the oracle's additional lifetime control. These are not 62 independent
  accessibility behaviors or three independent sets of knowledge.
- Shared-policy mutants run on Mac; the platform-specific coordinator mutant runs
  on all three anchors. Do not describe unexecuted mutants as runtime rejections.

Known incidents are development cases. Original source grades/baselines are not
changed, no model ranking is inferred, and no mandatory manual/UI test gate is added.

## SUI-04: First inventory missed the appended OS27 media requirement

Classification: coverage-scanner gap, found in the final section-header audit, not
an accessibility implementation defect. The first whitelist captured implementation,
testing, do/dont and interaction refinement, but skipped the appended OS27 media
update paragraph. Its216-clause inventory is preserved in
incidents/requirements-first-inventory.json.txt. The corrected inventory accounts
for217 requirements and explicitly leaves that version-scoped generation/style
selection claim unresolved. No guideline, frozen baseline or OS27 implementation
was changed to manufacture coverage. Do not turn this parser defect into SwiftUI
accessibility guidance.
