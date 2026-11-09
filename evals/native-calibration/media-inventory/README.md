# Qualified controller: native subtitle inventory and selection

The same XCTest on iOS and tvOS accepts two different ways to identify native subtitle options, and rejects three independent defects. It is a code-contract oracle for a menu that offers **all** options in the current legible group; it is not a rule about filtering forced subtitles or stable IDs across launches.

| Control | iOS 26.5 | tvOS 26.5 | Interpretation |
|---|---|---|---|
| Load-scoped ordinal IDs | Pass | Pass | Every option remains addressable. |
| Per-option opaque UUIDs | Pass | Pass | Same result without relying on ordinal identity. |
| Language tag or display name as sole key; reject duplicates | Intended fail | Intended fail | Native inventory rejected the asset before the picker could select anything. |
| Remove the actual caption write | Intended fail | Intended fail | Inventory succeeds; changing the binding leaves the actual caption Off. |
| Select the caption and also switch audio | Intended fail | Intended fail | Caption readback succeeds, but the viewer loses the preselected described audio option. |

One test method, five implementations, ten first executions, no retries. Both correct variants share the tested store's native AVAsset loader and writer, but construct identity differently. A native load is essential here: injected choices with unique IDs sidestep the original failure. AVFoundation exposed four legible options on this fixture; the test verifies a collision in the native language/display keys before it assesses a loader. It starts with captions Off, preselects described audio and writes **each** option via the binding before reading both native groups. It does not drive a UI or measure spoken output.

[Subject question](question.md) and [controller rubric](rubric.md) are separate development artifacts. [Evidence index](evidence.json) records both anchors, immutable input hashes and native receipt hashes. [Test](InventoryTests.swift) and [runner](qualify.py) reproduce the comparisons. The exact file is the previously qualified positive movie embedded in the two platform example packages. No network media, new dependency or provider is involved.

Run `python3 -B evals/native-calibration/media-inventory/verify.py` on the evidence host to verify against private first receipts. `test_outcomes.py` checks classification safeguards. A new native run via `qualify.py` stages a new private batch under evals/results/media-inventory; never replace the recorded batch. Xcode 27.0 (27A266a), SDK 27.0, deployment 26.0, iOS/tvOS simulator 26.5. A stronger oracle does not regrade frozen answers and does not establish that signal-v5 improves model output.

## Preserved-answer replay

Eight first answers to the same two picker questions were screened across the original unaided/skill comparison and the later signal-v2/v4 comparison. Six accept externally loaded rows without a default native inventory path. Supplying that implementation from the controller would test the controller, so they have no grade under this oracle; their historical results stand.

The two signal-v4 answers expose native discovery and a binding. The controller uses each answer's own load lifecycle and binding names, retaining the fixture and all-option assertions. The iOS assembly includes its unchanged starter dependency. A separate method injects native option objects with distinct load-scoped IDs to isolate writing from discovery; it cannot rescue the production path.

| Platform | Native inventory | Binding with supplied native options |
|---|---|---|
| iOS 26.5 | Rejected duplicate identifiers before a choice was available | Selected every caption and kept described audio |
| tvOS 26.5 | Rejected duplicate identifiers before a choice was available | Selected every caption and kept described audio |

This extends earlier single-option write evidence, not the count of model failures. Two answer implementations, four method outcomes, two native invocations, zero retries. These are supplemental development checks rather than revised whole-answer grades. Neither the complete-caption filtering policy nor selection after replacing a player item was graded here.

[Receipt index](answer-receipts.json) binds the answers, staged sources and native logs. Run `python3 -B evals/native-calibration/media-inventory/verify_replay.py` to verify the retained evidence. For a fresh offline run, `replay_answers.py` stages a new private batch; pass the printed batch name to the v4 replay's `native.py`.

## Replacement ownership

[Native unit](ReplacementTests.swift) | [first execution records](replacement-receipts.json) | [stage](replacement.py) | [verify](verify_replacement.py).
Both preserved v4 picker implementations passed after A was replaced and B's options loaded. The isolated negative controls remove only the ownership check in the returned setter; both failed on retired Off and retired selection, without breaking current selection. Same asset, distinct player items, shared option IDs, described audio preselected. The test drives retained bindings with supplied native groups; it does not exercise default inventory discovery, SwiftUI event delivery, or the interval before B has loaded.

Developer question: Our player switches videos while a captions menu is open. The next video also has choices 0 and 1. What should happen if the earlier menu sends Off or 0 after the new menu is ready? How could we check that without driving the UI?

Controller rubric: establish B on choice 1 and its independent audio track. Retain A's actual setter across replacement; stale Off and 0 must leave both B groups unchanged. Use B's setter to clear and then select 0, reading back both groups after each operation. Accept any ownership mechanism satisfying those observations. A fresh binding used for both calls, different IDs hiding a stale write, or checking a local selected ID does not establish this contract. Known development case; no new gold grade.
