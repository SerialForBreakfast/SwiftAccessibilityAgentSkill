# Consolidated independent review request

Prepared for BigDog; this document is not a sent message or accepted assignment.
No model runs or quota expansion are authorized by it. The existing nine-case
Gemini plan and frozen skill/baseline remain unchanged.

## One review, organized by workstream

1. **Ownership:** iOS/UIKit, tvOS/UIKit and macOS/AppKit form completion ownership and
   AVPlayer current-item loading. Audit synchronous/reentrant/duplicate callback
   contracts, field snapshot comparisons, actual item identity and retained-owner tests.
2. **Native text:** AppKit delegate and UIKit search-block rotors; inspect UTF16 and
   composed-character ranges, stale text/query sessions, boundary behavior and ordinary
   selection preservation. Review platform-specific imported API names, not just the
   matching algorithm.
3. **State and native controls:** explicit names/roles, non-color state, AVKit controls,
   query/filter state, modal flag restoration and disabled actions. Audit transitions
   across methods, particularly search followed by selection configuration.
4. **Desktop entry points:** explicit row-state metadata and direct synthetic NSEvent
   keyDown calls. Distinguish direct dispatch from delivered keyboard traversal.
5. **Coverage and evidence:** all507 clauses/36 rules, earlier iOS bindings, source
   hashes, first failures, intended mutants, exact execution receipts and scope limits.

## Required return

Return one sanitized report tied to the exact reviewed commit/content hashes:
- accepted, change requested, or disputed per behavioral family;
- clause mappings that overstate their assertions;
- rubric alternatives the current question may unfairly exclude;
- unresolved API-availability annotations;
- oracle defects separately from implementation defects;
- whether each development question is ready for baseline eligibility.

Review source and assertion validity without silently repairing subject answers.
No manual accessibility testing or UI automation is a prerequisite. No extra human
approval is needed for ordinary technical findings; escalate only disputed product
requirements, new spend/scope, or release decisions.

Unit acceptance does not establish measured skill improvement. After review, propose
an explicit, bounded zero-additional-spend frontier evaluation rather than silently
adding these development questions to a frozen baseline or held-out set.
