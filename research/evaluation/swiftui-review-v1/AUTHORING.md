# Authoring And Review Capture

Exact owner continuation: `Ok do that`, accepting the prior recommendation to
independently review the consolidated batch and combine accepted findings into a
later candidate without changing BigDog's sealed comparison.

One fresh-context review agent was used for source/oracle/prompt review. The first
response is retained in `original-review.json`. After new examples and questions
were authored, the exact `followup-request.json` was sent to the same reviewer; its
original response is `followup-review.json`. Author adjudication is a separate file.
The agent was closed after each completed pass. The reviewer edited no files and
ran no native, provider, network, installation or Git operations.

The initial detailed reviewer request remains available in the current chat's tool
record but is not independently exported as a complete provider request here. It
scoped review to the original shared source/tests, three platforms' questions and
rubrics, coverage ledger and reported results, and explicitly prohibited execution
or edits. Unexposed system instructions, hidden reasoning, exact provider revision
and usage telemetry are unavailable; this record does not reconstruct them.

The original batch is pinned by `prior-batch-pins.json`. Corrected source is under
`code-examples/swiftui/media-shared-v2/`, with deterministic packaging in `prepare.mjs`.
The first review-defect repro uses unchanged v1 production source and three new
assertions; the corresponding receipt is distinct from intentional mutation checks.
Original native input/diagnostic/XCTest artifacts remain privately archived, with
explicitly derived, redacted public copies and original hashes in the results index.

The nine expanded developer questions and independent rubrics are retained in
`prompt-records.json`. They have no independent subject answers. Author source,
review-agent text and native tool outputs are not relabeled as those answers.
Controller records and prior incident narratives are excluded from ordinary
candidate retrieval. Review-informed changes remain research-only.

The dev.6 candidate inherits dev.5 for unchanged topics and declares its focused
media extension and inherited limitations. Candidate input/output bytes and hashes
are measurable; model quality, token use and cost comparisons were not run.
Two source-review turns are not counted as frontier benchmark cells. No paid API,
model substitution, provider batch, worker message or Git publication was invoked.
