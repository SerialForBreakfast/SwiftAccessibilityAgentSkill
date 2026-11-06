# Preserved difficulties

These are author/harness observations, not a ranking of models and not automatically
accessibility recommendations. First input snapshots and diagnostics precede repairs.

| ID | Classification | First observation | Repair and evaluation implication |
| --- | --- | --- | --- |
| platform-path-01 | Harness test defect | Using URL.pathname left `%20` in the repository path; two manifest tests failed ENOENT | Use fileURLToPath. Preserve [first test](incidents/encoded-path-first.test.txt) and [diagnostic](incidents/encoded-path-diagnostic.txt). A separate tooling diagnostic, not accessibility guidance |
| platform-mac-01 | Harness preflight defect | Node architecture arm64 did not exactly match xcdevice arm64e; no tests executed | Accept this specific compatible host pair, still reject x86_64 mismatch/ambiguous destinations. [First adapter](incidents/mac-preflight-first.mjs.txt). No capability conclusion from a blocked run |
| platform-mac-02 | Test oracle lifetime defect | First native run: testShortcutDoesNotRetainRow asserted nil before an explicit autorelease-pool drain; 19 other methods passed | [First test](incidents/mac-lifetime-first.swift.txt). Add autoreleasepool around construction/destruction, retain action outside it, preserve weak-row and action-result assertions. Test ownership after framework temporary lifetime, not immediate destruction timing. Revised 20-method suite passed; see results ledger |

| platform-tv-01 | Author defect and coverage gap | First source set accessible names but left ordinary button titles empty; original 20-method suite passed | Preserve [first source](incidents/tv-visible-titles-first.swift.txt) and [first manifest](incidents/tv-first-manifest.json.txt). Set caller-provided names as visible titles, add title/reuse tests, and execute original source as a regression fixture. This is an actual example defect, not a deliberate mutant or measured model-comparison result |

Exact native first inputs, logs and test summaries remain in the immutable private
run directories recorded in the results index. Sanitized excerpts may remove host
paths and addresses, but not code, failing test identity or assertion meaning.
Do not replace first-attempt evidence with repaired outputs.

## Diagnostic questions (controller only until separate subject packaging)

- A local test helper uses new URL(relative, import.meta.url).pathname and fails
  when the checkout directory contains spaces. What should be inspected?
- A Mac preflight reports Node arm64 versus xcdevice arm64e. How can compatibility
  be checked without accepting arbitrary destination mismatches?
- An AppKit ownership test holds an action after releasing a view. How should the
  test distinguish a strong callback cycle from temporary autoreleased objects?

These tooling/oracle topics are not additional accessibility gold families. The
five platform developer prompts stay isolated from these known incidents.
