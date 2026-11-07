# Were the candidate instructions present and announced?

**Yes: all 28 captured requests contain the exact intended candidate body, and all 28
answers announce the correct skill/version on their first nonempty line, exactly once.**
This is a post-run audit of existing artifacts, not new inference or a rerun.

| Check | AGY | Claude |
| --- | ---: | ---: |
| Exact body present once in sent prompt | 14/14 | 14/14 |
| Sent-prompt hash matches persisted intention | 14/14 | 14/14 |
| Raw output hash matches execution receipt | 14/14 | 14/14 |
| Correct identity/version on first nonempty line | 14/14 | 14/14 |
| Identity appears exactly once | 14/14 | 14/14 |
| ROUTING present and names supplied reference ID | 14/14 | 14/14 |

Example identity format: `Swift Accessibility Agent (v0.3.0-dev.2, development candidate)`.
No original answer text, account identifiers or private transcript is published here.
[Machine-readable audit](PAYLOAD-ANNOUNCEMENT-AUDIT-20261106.json) contains per-cell checks.

## What this proves and does not prove

The harness explicitly supplies the candidate body and selected reference bytes.
That checks behavior with supplied guidance; it bypasses automatic skill discovery
and reference selection. Announcements are evidence that the reporting instruction
was followed, not proof of autonomous loading/reading. A separate instrumented
activation/retrieval lane is needed to test the installed workflow.

Reporting is not perfect: four Claude ROUTING lines use only a guideline ID instead
of a filename; two AGY lines omit explicit supplied-content provenance. All match the
reference IDs actually injected. Also, frozen GP26-10 is a UIKit task but receives
SwiftUI G-003 state/value guidance. Both versions receive identical bytes; this is a
harness reference-selection limitation, not an autonomous routing decision. Preserve
this run and qualify a separate corrected context revision rather than silently
changing inputs or rewriting grades.

## Why no new-candidate gain does not mean no skill benefit

The completed 28-cell study compares two skill versions, both receiving guidance.
It has no generic or released-skill control. Therefore it cannot estimate skill lift
against no skill. The supported conclusion is narrower: dev.2 did not demonstrate
an efficiency gain over dev.1 on these seven known cases; source-grade differences
are met versus inconclusive, not an established correction rate.

These cases also have little observed headroom: in the older 18-case source review,
the same seven cases already scored 7/7 without skill on AGY and 6/7 on Claude.
Those are historical, unblinded source grades, not a current matched baseline.
They explain why this subset is a weak test of overall benefit; they do not prove
that the current skill helps or harms. Native checks of exact answers remain separate.

The earlier 18-case comparison did show a preliminary signal with the historical
compact-only draft: AGY 13→15 and Claude 15→17 contracts met out of 18 versus no skill.
That is one unblinded development sample with different candidate bytes and mixed
frameworks. Do not relabel it as measured performance of 0.3.0-dev.1/dev.2 or as a
release-qualified improvement.

Next evidence should separate generic/released/candidate quality on eligible,
independently reviewed cases from actual installed activation/retrieval. New runs,
changed case contexts and candidate text need their own bounded approval/freeze.
No subject text, original answers, historical grades or frozen pins changed here.
