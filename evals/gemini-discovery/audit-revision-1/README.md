# Revised developer questions and skill contributions

This development overlay contains 17 revised prompts from 14 audited answers. Each entry in the [controller](cases.json) pins the exact original question, revised question and observable grading criterion. Export one subject with `python3 -B evals/gemini-discovery/audit-revision-1/export.py current-order` from the repository root. The calibrated exporter preserves the original Swift and supplies neutral review instructions. [Independent calibration and subscription estimate](CALIBRATION.md) All 17 revised questions now have fresh first answers in all four conditions. [Matched results](RESULTS.md) The original 384 grades describe the original questions.

## What changed

| Concern | Revised scoring decision |
|---|---|
| Dismissal | Separate duplicate completion from permission to dismiss. Exercise ordinary Close and Escape for the latter. |
| Stale handles | Test direct detachment and reparenting separately; distinguish deletion from reusing an ID for a different object. |
| Reused cell | Ask for both current name and order status. Score an unnecessary focus move separately. |
| Chapter control | Use uneven starts, an episode end beyond the final start, and the empty list. Preserve tap and drag. |
| Product scope | Specify full-only subtitles, exactly which selection cues matter, and whether Pay styling may change. |
| Weak evidence | Invoke retained production handlers, exercise a positive media fixture, and assert the actual selected substring. |

In each review record the requested behavior, any damage to existing behavior, unnecessary changes and strength of the proposed test separately. A harmless equivalent can earn a behavior pass. A test that never exercises the relevant path provides insufficient evidence. Two independent reviewers calibrated the primary behavior offline. Native execution remains unmeasured.

## Minimal experimental content

Use these two standalone additions as independently removable content. Use the same neutral envelope in all four content conditions. Normal announcements and read attribution apply in a later installed-skill comparison. The three text-range cases share the same opening but supply different original code, including both broken and working examples.

**Review instruction**
“Trace the reported symptom through the supplied code. If the current path already satisfies the request, show the decisive path and leave it in place.”

**On-demand UIKit text note**
“When an NSString search supplies an NSRange for a UITextView, keep its UTF-16 offsets when constructing positions in that document. Swift Character counts can diverge after emoji. Read the text in the returned UITextRange and check it against the expected search word.” [Local text-range contract](../../../code-examples/pilots/uikit-edited-rotor-v1/evaluation/controller.md)

Compare unaided, review instruction alone, text note alone and both on the same inputs and permissions. Report working/broken pairs both correct, whole-task gains and regressions, irrelevant reads, token use and first-answer repair needs. Presence in supplied context measures exposure. An installed follow-up needs actual body/reference reads and an equally tool-enabled control. The accepted outcome would be a reproducible improvement on an untouched developer task without a new critical loss; these development examples alone cannot establish transfer. [Audit and pruning decisions](../BLIND-AUDIT-V1.md)
