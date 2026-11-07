# Candidate 0.3.0-dev.5: target-complete development questions

Research only. Released 0.2.2, frozen baselines and previous candidates are unchanged.
This is a substantial offline iteration, not a model-evaluation or publication trigger.

## Coverage at a glance

| Target / owning framework | Topic applications | Qualification |
| --- | ---: | --- |
| iOS / UIKit | 8 | Draft |
| iOS / SwiftUI | 8 | Draft |
| macOS / AppKit | 8 | Draft |
| macOS / SwiftUI | 8 | Draft |
| tvOS / UIKit | 8 | Draft |
| tvOS / SwiftUI | 8 | Draft |
| Preservation, ownership, scope and evidence controls | 12 | Draft |

Eight related topic families: semantics, state, actions, structure/rotors, text,
lifecycle, media and testing. Sixty applications are not sixty independent families.
Platform variants share scenarios and must not be treated as independent statistical
samples. WatchOS and visionOS have explicit scope questions, not tested companion
coverage. Other frameworks and platforms have not been silently included.

## Read the questions without seeing the answers

[Subjects](evaluation/subjects/) contain only the natural developer request and
necessary scenario constraints. These are design/debugging tasks, not patch tasks
with missing source attachments. An implementation answer must supply its own minimal
complete example. A separate [controller catalog](evaluation/controller.json) contains
criteria, valid alternatives, expected references and evidence leads. Never give that
catalog to a subject model or make it available in the subject workspace.

No new answers have been generated. Empty attempts and unavailable outputs mean
unrun, not failed or successful. Existing evidence is a research lead; a new question
is not independently qualified merely because a related native fixture passed.

## Candidate improvements

Each topic note now explicitly addresses the corresponding failure traps. The
entrypoint distinguishes shared principles from framework defaults and asks about
actual ownership before prescribing cross-framework fixes. Preserve ordinary controls,
current callback ownership and user media selection; do not turn missing evidence
into a platform guarantee. Source gaps remain explicit: AppKit text/media and UIKit
on tvOS text. These require source review before their API claims can be qualified.

Examples remain opt-in. The router reads only the selected note and guideline; it
does not load subject questions, rubrics or the incident archive. Additional note
bytes are intentional; no token-efficiency improvement is claimed for this iteration.

## Qualification and next evaluation

Independent review must check realistic language, sufficient inputs, platform-specific
correctness, alternative acceptance and links to exact assertion/execution evidence.
Reviewers must tighten generic criteria where a particular API or code outcome matters.
Then freeze approved inputs and controls before a single explicitly approved milestone
batch. Keep known incidents in development; reserve holdouts outside this matrix.

No automatic run follows this candidate. No model calls, installs, native execution,
messages or Git publication are authorized by these files. Claude remains pending.

## Offline checks

`node --test research/evaluation/failure-driven/candidates/0.3.0-dev.5/integrity.test.mjs`

111 checks cover 60 separate subject records, 48 route/topic matches, evidence hashes,
source gaps, context boundaries, unsupported targets and unrun status. They do not
establish answer quality, natural-language routing accuracy or accessibility behavior.
