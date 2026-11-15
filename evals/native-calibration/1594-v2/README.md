# Receipt 1594: macOS controller erratum v2

Use this additive specification instead of the literal Q070 wording checks and the ambiguous Q082 question **in the next development packet**. The original packet, XCTest fixtures and grades remain historical records. Use [the subject questions](subject/questions.json) with the original case's unchanged starter files; do not send controller material to subjects.

## Q070: grade meaning on both transitions

Use [the component grader](controller/grade.py) on observations from configuring the **same** region selected, then deselected. Both the visible non-color status and the button's accessibility value must express the current state. Accept “Selected” followed by either “Not selected” or “Unselected”, including different equivalent strings on the two channels. Route unfamiliar nonempty wording to semantic review; register confirmed equivalents with their state rather than accepting arbitrary distinct strings. Reject blank values, reversed meanings and stale state. Score unchanged ordinary button naming and transparency behavior separately using the existing controls. An answer's own proof that rejects a valid alternative is still over-specific even when its product is correct.

## Q082: grade two different decisions

| Case | Arrange | Required observable | Negative control |
|---|---|---|---|
| Q082-A: eligibility | Attached, enabled, visible original reports that it cannot accept first responder; fallback is eligible and accepts the request. | Only the fallback receives a request; finish returns true. | Removing the eligibility check requests the original. |
| Q082-B: rejection | Both targets are eligible. Record the requested targets. The request callback returns false for the original. | Only the original receives a request; finish returns false. | Trying fallback after rejection violates the one-request policy, even if the final Boolean is false. |

For both, independently score the ordinary case: an eligible original accepts, is the only target requested, and finish returns true. Use a fresh presentation ticket per scenario. Either direct branching or an injected selector is fine: judge the installed finish path, not helper names or implementation order. One request is **this fixture's product policy**, not a general AppKit rule. These tests observe requests, not delivered focus.

## Saved evidence and limits

Receipt 1598's graded archive SHA-256 is `461d08925e686966dd9ae90c4a07fabe482ebd778989b3e02da5616b85c7a6ee`. [The controller index](controller/evidence.json) identifies both masked submissions per original case, all four first-result lanes, and the failed method names (exact messages remain in the private archive). It does not contain revised whole-answer grades.

- Q070: both products use meaningful synchronized state strings. Accept their wording on source review; retain both original literal mismatches and both proofs' rejection of the working reference. Blank mutant status remains defective.
- Q082-A: both products requested an ineligible original first. Q082-B: both issued two requests when the first was rejected. These are observed violations in two submissions, not four independent model failures. The original controller checked the first target for A and the request count and Boolean for B; do not infer unrecorded trace details from a passing assertion.
- The ordinary return-to-primary method passed for both submitted products in the saved suites. The submitted proofs modeled request refusal, not eligibility, and expected fallback after refusal. Their native results stay unchanged.
- Neither split question was asked in the original run. They are development cases with retrospectively mapped evidence, not fresh model scores. No code or model execution is needed to inspect the saved records.
