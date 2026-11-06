# Campaign Results

Status: executed-with-expected-outcomes; independent review pending. Not baseline promotion.

| Measure | Result |
| --- | ---: |
| Packages | 19 |
| Native checks | 104 |
| Positive unit checks | 21 |
| Unique selected positive unit methods | 202 |
| Negative controls, including compile negatives | 66 |
| Compile checks, including compile negatives | 18 |
| All method executions, including negative reruns | 355 |
| Unexpected outcomes | 0 |

New development: three behavioral families, 17 positive methods and five deliberate mutants. Existing pilot and checkout methods are reruns, not newly discovered independent behaviors. Compile and negative categories overlap.

Anchor: SDK 27.0 (24A430); runtime 26.5 (23F77); arm64. Deployment target 26.0. Exact compiler/Xcode identifiers are retained in execution.json.

## Coverage

- partially-covered: 123 clauses.
- covered: 22 clauses.
- swiftui-deferred: 31 clauses.
- documentation-supported/outside-unit-scope: 33 clauses.

All 15 guideline rules have partial dispositions with bounded assertions. This is accounting closure, not a claim that all accessibility behavior is unit-tested.

## First Attempts and Repairs

The original checkout oracle failure and correction remain in the checkout package. The new quantity pre-execution coverage defect and declaration-scanner scope defect retain first sources, findings and repair records. Neither authoring incident is a controlled model failure. Native first outcomes are in the table below; any later repair must use a separate revision/export.

## Per-Check Outcomes

| Package | Check | Lane | Outcome |
| --- | --- | --- | --- |
| uikit-choice-v1 | compile-choice | compile | positive-pass |
| uikit-choice-v1 | choice-unit | unit | positive-pass |
| uikit-choice-v1 | singleline-negative | unit | intended-negative-rejection |
| uikit-choice-v1 | fixedfont-negative | unit | intended-negative-rejection |
| uikit-choice-v1 | staleselection-negative | unit | intended-negative-rejection |
| uikit-choice-v1 | clobberedtraits-negative | unit | intended-negative-rejection |
| uikit-containers-v1 | compile-containers | compile | positive-pass |
| uikit-containers-v1 | containers-unit | unit | positive-pass |
| uikit-containers-v1 | wrongspan-negative | unit | intended-negative-rejection |
| uikit-containers-v1 | stalemodal-negative | unit | intended-negative-rejection |
| uikit-containers-v1 | ignoredenabled-negative | unit | intended-negative-rejection |
| uikit-contrast-v1 | compile-contrast | compile | positive-pass |
| uikit-contrast-v1 | contrast-unit | unit | positive-pass |
| uikit-contrast-v1 | nolinearization-negative | unit | intended-negative-rejection |
| uikit-contrast-v1 | wrongcolorspace-negative | unit | intended-negative-rejection |
| uikit-contrast-v1 | ignoredtraits-negative | unit | intended-negative-rejection |
| uikit-contrast-v1 | ignoredalpha-negative | unit | intended-negative-rejection |
| uikit-dynamic-v1 | compile-dynamic | compile | positive-pass |
| uikit-dynamic-v1 | dynamic-unit | unit | positive-pass |
| uikit-dynamic-v1 | staleaction-negative | unit | intended-negative-rejection |
| uikit-dynamic-v1 | duplicatecallback-negative | unit | intended-negative-rejection |
| uikit-dynamic-v1 | missingelements-negative | unit | intended-negative-rejection |
| uikit-dynamic-v1 | retainedremoved-negative | unit | intended-negative-rejection |
| uikit-edited-rotor-v1 | compile-edited-rotor | compile | positive-pass |
| uikit-edited-rotor-v1 | edited-rotor-unit | unit | positive-pass |
| uikit-edited-rotor-v1 | characteroffsets-negative | unit | intended-negative-rejection |
| uikit-edited-rotor-v1 | ignoredoverlap-negative | unit | intended-negative-rejection |
| uikit-edited-rotor-v1 | missingrestart-negative | unit | intended-negative-rejection |
| uikit-edited-rotor-v1 | oldrotor-negative | unit | intended-negative-rejection |
| uikit-edited-rotor-v1 | staletext-negative | unit | intended-negative-rejection |
| uikit-lifecycle-v1 | compile-lifecycle | compile | positive-pass |
| uikit-lifecycle-v1 | lifecycle-unit | unit | positive-pass |
| uikit-lifecycle-v1 | wrongnotification-negative | unit | intended-negative-rejection |
| uikit-lifecycle-v1 | unstopped-negative | unit | intended-negative-rejection |
| uikit-lifecycle-v1 | staleedit-negative | unit | intended-negative-rejection |
| uikit-media-inspection-v1 | compile-inspection | compile | positive-pass |
| uikit-media-inspection-v1 | inspection-unit | unit | positive-pass |
| uikit-media-inspection-v1 | loadedasseekable-negative | unit | intended-negative-rejection |
| uikit-media-inspection-v1 | fullmeansready-negative | unit | intended-negative-rejection |
| uikit-media-inspection-v1 | inferredlive-negative | unit | intended-negative-rejection |
| uikit-media-metadata-v1 | compile-metadata | compile | positive-pass |
| uikit-media-metadata-v1 | metadata-unit | unit | positive-pass |
| uikit-media-metadata-v1 | allaudiodescribed-negative | unit | intended-negative-rejection |
| uikit-media-metadata-v1 | noitemabsent-negative | unit | intended-negative-rejection |
| uikit-media-metadata-v1 | selectionlost-negative | unit | intended-negative-rejection |
| uikit-media-v1 | compile-media | compile | positive-pass |
| uikit-media-v1 | media-unit | unit | positive-pass |
| uikit-media-v1 | hiddencontrols-negative | unit | intended-negative-rejection |
| uikit-media-v1 | wronglanguage-negative | unit | intended-negative-rejection |
| uikit-media-v1 | staleposition-negative | unit | intended-negative-rejection |
| uikit-media-v1 | forcedonly-negative | unit | intended-negative-rejection |
| uikit-modal-v1 | compile-modal | compile | positive-pass |
| uikit-modal-v1 | modal-unit | unit | positive-pass |
| uikit-modal-v1 | lostbackground-negative | unit | intended-negative-rejection |
| uikit-modal-v1 | earlynotification-negative | unit | intended-negative-rejection |
| uikit-modal-v1 | stalecompletion-negative | unit | intended-negative-rejection |
| uikit-modal-v1 | ignoreddismissguard-negative | unit | intended-negative-rejection |
| uikit-modal-v1 | detachedtarget-negative | unit | intended-negative-rejection |
| uikit-naming-v1 | compile-naming | compile | positive-pass |
| uikit-naming-v1 | naming-unit | unit | positive-pass |
| uikit-naming-v1 | exposeddecoration-negative | unit | intended-negative-rejection |
| uikit-naming-v1 | hiddencontrols-negative | unit | intended-negative-rejection |
| uikit-naming-v1 | stalenames-negative | unit | intended-negative-rejection |
| uikit-preferences-v1 | compile-preferences | compile | positive-pass |
| uikit-preferences-v1 | preferences-unit | unit | positive-pass |
| uikit-preferences-v1 | ignoredmotion-negative | unit | intended-negative-rejection |
| uikit-preferences-v1 | stalehint-negative | unit | intended-negative-rejection |
| uikit-reuse-v1 | compile-reuse | compile | positive-pass |
| uikit-reuse-v1 | reuse-unit | unit | positive-pass |
| uikit-reuse-v1 | staleselection-negative | unit | intended-negative-rejection |
| uikit-reuse-v1 | staleidentity-negative | unit | intended-negative-rejection |
| uikit-reuse-v1 | wrongnotification-negative | unit | intended-negative-rejection |
| uikit-semantics-v1 | compile-semantics | compile | positive-pass |
| uikit-semantics-v1 | semantics-unit | unit | positive-pass |
| uikit-semantics-v1 | droppedaction-negative | unit | intended-negative-rejection |
| uikit-semantics-v1 | wrongrotordirection-negative | unit | intended-negative-rejection |
| uikit-semantics-v1 | losttraits-negative | unit | intended-negative-rejection |
| uikit-speed-v1 | compile-speed | compile | positive-pass |
| uikit-speed-v1 | speed-unit | unit | positive-pass |
| uikit-speed-v1 | stalemetadata-negative | unit | intended-negative-rejection |
| uikit-speed-v1 | repeatedchange-negative | unit | intended-negative-rejection |
| uikit-speed-v1 | ignoreddisabled-negative | unit | intended-negative-rejection |
| uikit-text-v1 | compile-text | compile | positive-pass |
| uikit-text-v1 | text-unit | unit | positive-pass |
| uikit-text-v1 | wrongrange-negative | unit | intended-negative-rejection |
| uikit-text-v1 | stalematches-negative | unit | intended-negative-rejection |
| uikit-text-v1 | missingcategory-negative | unit | intended-negative-rejection |
| uikit-v1 | compile-pilot | compile | positive-pass |
| uikit-v1 | row-actions-unit | unit | positive-pass |
| uikit-v1 | row-actions-negative | unit | intended-negative-rejection |
| uikit-v1 | cell-state-unit | unit | positive-pass |
| uikit-v1 | cell-state-negative | unit | intended-negative-rejection |
| uikit-v1 | text-scaling-unit | unit | positive-pass |
| uikit-v1 | text-scaling-negative | unit | intended-negative-rejection |
| uikit-v1 | compile-label-type-negative | compile | intended-negative-rejection |
| checkout-contract-v1 | checkout-unit | unit | positive-pass |
| checkout-contract-v1 | changed-font | unit | intended-negative-rejection |
| checkout-contract-v1 | fixed-height | unit | intended-negative-rejection |
| gap-contracts | gap-unit | unit | positive-pass |
| gap-contracts | summary-name | unit | intended-negative-rejection |
| gap-contracts | ordinary-quantity | unit | intended-negative-rejection |
| gap-contracts | disabled-quantity | unit | intended-negative-rejection |
| gap-contracts | motion-feedback | unit | intended-negative-rejection |
| gap-contracts | disabled-metadata | unit | intended-negative-rejection |

## Preservation

246 offline checks passed. All 210 frozen files and 87 historical pins verified unchanged. Durable private archives preserve raw receipts, first failures, source snapshots and xcresults; hashes and recovery location are in preservation.json. Git publication was not performed.

## Remaining Review

Independent clause/oracle/rubric acceptance is pending. The availability matrix preserves unresolved introduction dates and overlay/type interpretation limits. No new development cases are baseline-eligible yet. No models, UI tests or mandatory manual checks were run; no skill or frozen-baseline updates were made.
