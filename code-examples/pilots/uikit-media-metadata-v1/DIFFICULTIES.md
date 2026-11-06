# UPAIR-06B Difficulty and Repair Record

Work date November5,2026. Assisted authoring, not a controlled model comparison.
Exact serving revision/context are unavailable. Preserve failures and warnings
separately from intentional mutation defects and anticipated risks.

| ID | Classification | Observation |
| --- | --- | --- |
| MM01 | Source-access limitation | Apple web result was an HTML shell. Installed SDK AVMediaFormat.h describes explicit track tagging; record header hashes rather than claim a web-body review. |
| MM02 | Fixture design risk | Ordinary alternate-language silent audio is not an audio-description fixture. Create a matched tagged/untagged pair and explicitly scope the positive claim to metadata recognition. |
| MM03 | Fixture integrity risk | Adding metadata before media payload shifts chunk offsets. Remux to MOV with moov last, reject other layouts in the builder, and preserve media offsets. |
| MM04 | Native compiler warning | First attempt used the older locale languageCode accessor. Compiler identifies its iOS16 deprecation; preserved source and diagnostics before replacing it in revision2. |
| MM05 | Lifecycle boundary | Loader accepts an item, not an atomic live player snapshot. Callers must reject obsolete results after item replacement; this packet does not test a live subscription. |

## MM04 Exact Warning and Repair

First-attempt source:

```swift
language: option.locale?.languageCode,
```

Compiler diagnostic (source line29):

```text
warning: 'languageCode' was deprecated in iOS 16: renamed to 'language.languageCode.identifier' [#DeprecatedDeclaration]
note: use 'language.languageCode.identifier' instead
```

Executed repair in revision2 of the new tranche only:

```swift
language: option.locale?.language.languageCode?.identifier,
```

This is a deprecation warning, not a failed compilation or an observed accessibility
failure. The old media fixture remains historical evidence. Independent prompts
should ask for supported APIs naturally rather than reveal this exact repair.

## Final Native Outcome

Seven positive methods passed in both revisions. Revision2 compile output contains
no warning; three manufactured defects were caught by their selected assertions.
No unexpected assertion failure occurred. Preserve MM04 as a warning/repair, not a
failed test. See validation/revision-1.json and validation/revision-2.json.
