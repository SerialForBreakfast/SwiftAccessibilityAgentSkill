# Controller difficulties and refinements

No observed subject-model failures or new native errors occurred. These are local
review/validation refinements, not accessibility guidance or independent gold cases.

## Source anchor initially captured only a heading

The first builder used this line-ending search for every anchor:

```js
let end = text.indexOf('\n', start + needle.length);
```

For `## Rule`, that would retain the heading but omit its substantive rule. Author
inspection changed section anchors to run to the next heading (with a size bound).
Regression checks require rule anchors to contain body text, not merely the heading.
Original full raw authoring transcript is not exported; this is an exact code excerpt
plus separate analysis, not a reconstructed full failed execution.

## Review identity initially lacked the rubric revision

Subject and answer hashes alone cannot distinguish a later controller revision
whose criterion IDs stay the same. The first schema required:

```json
["schema", "caseId", "subjectSha256", "answer", "review"]
```

The final schema also requires `rubricSha256`. The validator compares it to the
current corpus digest, and a stale-rubric mutation is rejected. This is a review-
record integrity safeguard, not semantic proof that a reviewer made the right call.
The original 278 tests passed; the added stale-rubric check brings this suite to 279.

## Nearby evidence is not interchangeable

Checkout evidence uses a research-local `validation.json` row format, not the older
code-example validation directory format. The supplemental adapter reads that exact
record and matches revision 2, source hashes, test selection and environment. It
never promotes revision-1 oracle failures, adds callbacks to submitted answers or
transfers native UIKit evidence to SwiftUI/AppKit/tvOS. No execution was repeated.
