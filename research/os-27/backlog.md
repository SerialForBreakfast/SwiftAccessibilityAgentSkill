# Research completion backlog

These are research tasks only. No skill changes or benchmark mutations are authorized.

## Second-pass progress

- Five symbols reviewed in [API availability](api-availability.md); full symbol audit remains open.
- iPhone/Mac media constraints established in [shipping constraints](shipping-constraints.md);
  iPad/tvOS/visionOS-specific tables remain open.
- watchOS Sound Recognition and visionOS Dwell Control/Look to Drive now have
  user-facing shipping evidence. FaceTime interpreter/live-captioner support is
  documented for visionOS 27.2; exact developer integration remains open.
- Managed-device accessibility policy added as a deployment constraint.
- Eleven raw-response fingerprints recorded in [pass-2 sources](pass-2-sources.md).
- AppKit toolbar-role metadata has unexpected iOS/iPadOS entries; retain for targeted
  declaration/variant review. No implementation conclusion is inferred from them.
- Release/build reconciliation and exhaustive section-by-section extraction remain
  open. These targeted findings do not establish complete OS coverage.

| Priority | Work | Completion evidence |
| --- | --- | --- |
| P0 | Reconcile exact stable/beta releases and builds from Apple indexes | Per-platform dated release map, including 27.1 retrieval gaps |
| P0 | Review API declarations for every extracted symbol | Platform minima, linked-SDK requirements, availability/deprecation metadata |
| P0 | Extract TV Larger Text and media hardware/language limits | Specific transcript tables/support footnotes, scoped claims |
| P0 | Expand watchOS and visionOS research | Reviewed platform sessions, Support changes and user-task coverage |
| P1 | Walk every section of the release inventory | Each topic marked relevant/excluded/pending with rationale; individual change IDs |
| P1 | Audit 27.2 and 27.3 SDK behavior separately | Stable versus beta claim records, exact issue IDs |
| P1 | Follow WWDC session resource links and API changes | Session index reconciled with symbols and sample-code scope |
| P1 | Complete Apple announcement shipping reconciliation | Announced features matched to shipped Support/API evidence or pending status |
| P1 | Retrieve full AppleVis articles and individual bugs | Full-text-reviewed user-impact records with device/build context |
| P1 | Seek practitioner analysis by topic and named author | Relevant reviewed articles, not author reputation alone |
| P1 | Cover HomePod/audioOS and CarPlay dependencies | Dedicated support/release evidence; clarify app-development relevance |
| P1 | Expand Safari/WebKit fix inventory and SDK tools | Atomic web/inspector changes with host/version scope |
| P2 | Independent corpus review | Every reviewed claim checked against supporting passage; conflicts retained |
| Later | Propose development tests after baselines | Separate proposed cases; no heldout tuning or baseline rewriting |

## Current delivery boundary

This pass provides five release-note families across three releases, six platform
files, selected reviewed claims, WWDC and WebKit evidence, a source fingerprint ledger,
and a complete topic inventory for the retrieved documents. It does not yet provide
an exhaustive atomic inventory of all OS-27 changes. Keywords were used to select
accessibility/interaction passages; all other topics remain indexed for deeper review.

## Promotion gate

Research stays isolated until the agreed benchmark baselines exist. Then choose a
small source-backed candidate change, identify affected development cases, evaluate
frontier-agent quality and efficiency, and review regressions before touching released
skill guidance. Documentation evidence does not require mandatory manual verification;
user studies and runtime tests answer separate implementation/outcome questions.
