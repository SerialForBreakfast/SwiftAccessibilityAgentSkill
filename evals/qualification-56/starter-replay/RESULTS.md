# Frozen starter-interface replay

All are signal-v6, trial 1, receipt 1507. Outcomes below are for the submitted proof, not the whole answer. Ref and alt are valid implementations; mut is the deliberately defective one.

| Case | Reference | Defect | Alternative | Interpretation |
|---|---|---|---|---|
| 4840 | pass | pass | pass | Accepts both valid variants but misses the defect. Direct ticket helper, not installed A/B closure. First attempt lacked macro visibility; separate test support file fixed discovery. |
| 4ec9 | assertion-failure | assertion-failure | assertion-failure | Rejects the reference; a mutant failure does not establish discrimination. The nil-item subtest passes only the defective phase. On all variants replacement expected nil although the local fixture auto-selected a forced track; unknown-ID subtest passed. |
| 5d12 | compile-error | compile-error | compile-error | No behavioral grade: compile diagnostic remains. Proof calls AVMediaSelectionOption.unicodeLanguageIdentifier, unavailable in the target SDK. No fabricated extension. |
| 6d2d | compile-only | compile-only | compile-only | Remote URLs: compiled only; runtime discrimination unmeasured. Remote HLS URL in the submitted load. All three variants typecheck; no assertion executed. |
| c04c | compile-only | compile-only | compile-only | Remote URLs: compiled only; runtime discrimination unmeasured. Remote player-item URLs in the suite; unchanged proof compiled on all variants, no behavioral verdict. |
| c6b2 | compile-only | compile-only | compile-only | Remote URLs: compiled only; runtime discrimination unmeasured. Remote item URLs in the submitted tests; async loader type bound on all variants, no behavioral verdict. |
| da78 | pass | pass | pass | Accepts both valid variants but misses the defect. Direct ticket helper, not installed closure; duplicate B check passes even on shared-ticket wiring. |
| f483 | pass | assertion-failure | pass | Distinguishes the defect; accepts the alternative (see failing assertion). Injected string-option state only; does not inspect native legible selection. |
