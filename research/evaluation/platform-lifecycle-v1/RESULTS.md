# Lifecycle results

Status: executed, author-checked; independent review pending.

| Measurement | Result |
| --- | --- |
| Current revision positive methods | 57 (28 Mac, 29 TV) |
| Current checks | 15: two compile, two positive, eleven negative |
| Negative checks | Ten deliberate mutants and one preserved original Mac defect; all rejected by intended assertions |
| Preserved attempts | 19, including initial compile/positive attempts on both platforms |
| Method executions including reruns/negatives | 124; not 124 unique behaviors |
| Unexpected native failures | 0; source-audit findings described separately |
| New draft developer questions/rubrics | 4; no independent model responses yet |

The exact test IDs, hashes, outcomes, diagnostics and environment are in
[results-index.json](results-index.json). Each current check has a matching
manifest-hash receipt. First green versions remain distinguishable from revised
ones. Negative `status: passed` means `observed: failure` with the expected test ID,
not successful execution of a defective implementation.

## Environment

| Lane | Runtime | SDK | Deployment target |
| --- | --- | --- | --- |
| macOS | 27.0, 26A428 (host) | 27.0, 26A425 | 26.0 |
| tvOS | 26.5, 23L470 (simulator) | 27.0, 24J360 | 26.0 |

Xcode 27.0 (27A266a), Swift 6.4, arm64 targets. Mac compilation for 26 does not
establish Mac26 runtime behavior. Annual anchors and release promotion are separate.

## What is established

Completion requests select a currently eligible owned target, preserve newer
sessions, handle cancellation/duplicates and consume state before reentrant callbacks.
Preference tests inject current values and controlled scheduling, use platform
notification names, assert cleanup, and reject callbacks from stopped/old sessions.
The TV default requester is checked through a request spy and preferred-target state.
The Mac default requester is checked without an attached window for rejection.

Apple's focus-system preconditions remain part of the integration contract. These
assertions establish request/configuration behavior, not delivered focus or actual
system-preference notification timing. No UI tests or manual verification required.

## Cumulative companion counts

AppKit/macOS now has 66 positive methods; UIKit/tvOS has 67. UIKit/iOS remains202.
These 335 methods are not independent scenarios or platform coverage percentages.
The new contracts complement the earlier names/actions and navigation/results
packages. All older records remain unchanged.

## Offline verification

The combined companion, native-adapter, evaluation-runner and research integrity
suite passed 296 checks, with no failures or skips. The baseline checker verified
all 210 frozen files and the same baseline content hash:
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
The earlier development archive verifier passed 87 pins, 26 exact snippets, 17 reports,
eight incidents and29 mutants. These checks did not rerun older native suites.

[Archive receipt](archive-receipt.json) identifies the durable private archive of
all 19 native attempts and retrieved Apple markdown. Regenerable build caches are
excluded; original selected inputs, commands, diagnostics and xcresult evidence
are retained. Original raw logs are private; the public index is sanitized.

The original nine-case prompt index is unchanged. Its inventory test now checks
its declared package scope; the new lifecycle integrity test checks the union of
those nine cases and the four new ones against all platform prompt files. This
avoids silently expanding the already prepared Gemini baseline.

Publication formatting exception: TelevisionLifecycleTests.swift line16 contains
spaces on an otherwise blank line. Staged whitespace checking identifies exactly
this line. Its validated source hash is preserved rather than rewriting native
inputs for a cosmetic edit; no semantic or execution change is involved.
