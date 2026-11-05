# Changelog

All notable changes to this documentation project are tracked here.

## [Unreleased]

### Portable worker evaluation requirements

- Reviewed pinned upstream BigDog smoke/development summaries and MaxMini peer assessment without merging over local rubric changes. Preserved failures as ungraded historical observations.
- Added L1-L4 task complexity, four independent context/output budgets, an offline full-corpus campaign planner and worker receipt/coverage checks for BigDog or MaxMini.
- Added independent MaxMini provider settings; preserved finish reasons/truncation and excluded .DS_Store from live content hashes without changing baseline snapshots.
- Documented worker token-preflight, failure accounting, TDD/OS-maintenance comparisons and follow-up context-stress work. No local inference, live dispatch or remote execution performed.

### Gold-prompt and rubric review

- Added anchored, weighted grading for all 60 scenarios, critical-error evidence requirements, a frozen grading reference bundle and independent calibration protocol.
- Preserved held-out questions; repaired development conversations and separated framework/OS context.
- Paired judges receive actual user context and identical reference evidence; imports reject ungradable or unanchored grades.
- Fingerprint rubric/evidence with run inputs; no model results or calibration success is claimed.

### Evaluation-backed 0.2.3 candidate

- Captured pre-update v0.2.2 working-tree baseline with file hashes; released version unchanged.
- Added provider-neutral C0-C3 evaluation, BigDog/comparator configuration, 40 development and 20 held-out families, traced reads, blinded grading and paired statistical reporting.
- Added reviewed tvOS Larger Text, reading-content, and subtitle guidance with a claim-level source audit ledger.
- Made testing/reference loading conditional and clarified evidence honesty and freshness.
- Completed the 63-entry scoped source audit, repaired SwiftUI/AppKit source mappings, corrected linked-group symbol versus behavior availability, narrowed historical issue ranges and updated resolved Xcode issue status.
- Added source/citation/mirror checks and a BigDog deployment handoff; 20 offline tests pass.
- Model quality, native-host discovery, dependency installation and grading calibration remain pending; no effectiveness claim is made.

### Added

- `docs/core/apple-beta-release-readiness-2026.md` and mirrored `references/core/apple-beta-release-readiness-2026.md` to track Apple beta/release-note signals affecting tvOS Larger Text, generated subtitles, custom controls, reading apps, TextKit, Xcode agent support, and evaluation planning.
- `docs/core/adr/ADR-002-context-budget-and-routing.md` and mirrored `references/core/adr/ADR-002-context-budget-and-routing.md` to define route-first progressive loading and prevent context bloat.
- `evals/promptfoo/context-budget-gold-prompts.md` to make context-bloat and over-routing behavior measurable in future promptfoo coverage.
- `docs/core/adr/ADR-001-robust-evaluation-methodology.md` and mirrored `references/core/adr/ADR-001-robust-evaluation-methodology.md` to define layered release-gated evaluation across package integrity, promptfoo, source governance, optional ViewLens runtime evidence, and human/user validation.
- `docs/core/viewlens-evaluation-integration.md`, mirrored `references/core/viewlens-evaluation-integration.md`, and `evals/promptfoo/viewlens-gold-prompts.md` to define optional ViewLens runtime-evidence evaluation for accessibility hierarchy, focus graphs, Dynamic Type reflow, and before/after fix verification.
- `docs/core/wwdc-2026-accessibility-watchlist.md` and mirrored `references/core/wwdc-2026-accessibility-watchlist.md` to track newly previewed Apple accessibility features, agent support implications, and promptfoo coverage candidates.
- `docs/tvos/README.md`
- `docs/tvos/guidelines/topic-backlog.md`
- `docs/macos/README.md`
- `docs/macos/guidelines/topic-backlog.md`
- `docs/tvos/guidelines/t-001-focus-order-directional-navigation.md`
- `docs/tvos/guidelines/t-002-initial-focus-modal-restoration.md`
- `docs/tvos/guidelines/t-003-labels-values-traits-focused-controls.md`
- `docs/tvos/guidelines/t-009-contrast-non-color-cues.md`
- `docs/tvos/guidelines/t-007-media-playback-controls.md`
- `docs/tvos/guidelines/t-008-reduce-motion-focus-animations.md`
- `docs/tvos/guidelines/t-004-grouping-containment-shelves-grids.md`
- `docs/tvos/guidelines/t-005-custom-actions-remote-first.md`
- `docs/tvos/guidelines/t-006-search-filter-collection-semantics.md`
- `docs/tvos/guidelines/t-010-xcuitest-focus-regression-hooks.md`
- `docs/macos/guidelines/m-001-nsaccessibility-roles-labels-values-actions.md`
- `docs/macos/guidelines/m-002-keyboard-focus-order.md`
- `docs/macos/guidelines/m-007-modal-window-focus-containment.md`
- `docs/macos/guidelines/m-009-contrast-reduced-transparency.md`
- `docs/macos/guidelines/m-010-testing-workflow.md`
- `docs/macos/guidelines/m-008-voice-control-naming-disambiguation.md`
- `docs/macos/guidelines/m-003-grouping-hierarchy-desktop-layouts.md`
- `docs/macos/guidelines/m-004-announcements-state-change-notifications.md`
- `docs/macos/guidelines/m-005-swiftui-appkit-interop-forwarding.md`
- `docs/macos/guidelines/m-006-table-outline-list-semantics.md`
- `docs/testing/manual-test-scripts.md`
- `docs/testing/inspector-audit-checklist.md`
- `docs/testing/xcuitest-hooks.md`
- `skill/manifests/README.md`
- `skill/manifests/axes.json`
- `skill/manifests/core.json`
- `skill/manifests/routes.json`
- `skill/manifests/task-presets.json`
- `skill/manifests/platform-presets.json`
- `docs/testing/tvos-manual-test-scripts.md`
- `docs/testing/macos-manual-test-scripts.md`
- `docs/testing/platform-coverage-matrix.md`
- `docs/testing/regression-triage-playbook.md`
- `AGENT.md`
- `docs/core/architecture/architecture-principles.md`
- `docs/core/decision-matrix.md`
- `docs/core/external-landscape.md`
- `docs/core/pattern-review-rubric.md`
- `docs/core/cookbook/semantics-cookbook.md`
- `docs/core/known-os-issues.md`
- `docs/core/known-os-issues-index.json`
- `docs/core/known-os-issues-workflow.md`
- `docs/core/version-matrix.md`
- `docs/core/templates/component-contract-template.md`
- `docs/core/templates/interop-boundary-contract-template.md`
- `SKILL.md` agent packaging document.
- `docs/visionos/README.md`
- `docs/visionos/guidelines/topic-backlog.md`
- `skill/manifests/select-example.json`
- `skill/manifests/decision-rules.json`
- `skill/manifests/security-policy.json`
- `skill/manifests/pattern-signals.json`
- UIKit P0 guideline drafts:
  - `docs/uikit/guidelines/u-001-labels-meaningful-names.md`
  - `docs/uikit/guidelines/u-002-hints-when-to-use.md`
  - `docs/uikit/guidelines/u-003-values-stateful-controls.md`
  - `docs/uikit/guidelines/u-004-traits-roles.md`
  - `docs/uikit/guidelines/u-005-grouping-containment.md`
  - `docs/uikit/guidelines/u-006-focus-reading-order.md`
  - `docs/uikit/guidelines/u-010-dynamic-type-layout-resilience.md`
  - `docs/uikit/guidelines/u-011-color-contrast-non-color-cues.md`
- UIKit remaining guideline drafts:
  - `docs/uikit/guidelines/u-007-accessibility-custom-actions.md`
  - `docs/uikit/guidelines/u-008-custom-controls-semantic-equivalence.md`
  - `docs/uikit/guidelines/u-009-rotor-friendly-structure.md`
  - `docs/uikit/guidelines/u-012-reduced-motion.md`
  - `docs/uikit/guidelines/u-013-modal-focus-containment.md`
  - `docs/uikit/guidelines/u-014-table-collection-form-semantics.md`
  - `docs/uikit/guidelines/u-015-media-captions-descriptions-controls.md`

### Changed

- Reduced runtime manifest default loading by keeping long core, testing, source-registry, evaluation, ViewLens, and watchlist documents on-demand instead of always loaded.
- Expanded top-level track coverage in `README.md` to include tvOS and macOS backlogs.
- Expanded `SKILL.md` to include tvOS/macOS canonical inputs and explicit platform-target selection rules.
- Extended `docs/core/sources/registry.md` with Tier-1 tvOS/macOS sources (`Accessibility for UIKit`, tvOS focus interactions, `NSAccessibility`, WWDC25 macOS accessibility) and Tier-2 automation reference (`AccessibilitySnapshot`).
- Expanded `docs/core/technology-map.md` with tvOS focus-engine and macOS keyboard/AppKit risk sections.
- Added Workstream `H` and Milestone `M6` for platform expansion in `Tasks.txt`.
- Updated tvOS and macOS backlogs to mark `T-001` and `M-001` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-002` and `M-002` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-003` and `M-007` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-009` and `M-009` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-007` and `M-010` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-008` and `M-008` as drafted with Tier-1 citation evidence.
- Updated tvOS and macOS backlogs to mark `T-004`, `T-005`, `T-006`, `T-010`, `M-003`, `M-004`, `M-005`, and `M-006` as drafted with citation evidence.
- Updated tvOS and macOS track README files to reflect complete drafted sets (`T-001`..`T-010`, `M-001`..`M-010`).
- Corrected SwiftUI backlog guideline paths and core reference links in `docs/swiftui/guidelines/topic-backlog.md`.
- Updated UIKit backlog statuses and file links for drafted P0 topics in `docs/uikit/guidelines/topic-backlog.md`.
- Completed structured guideline QA pass across SwiftUI and UIKit sets (sections, metadata, citation counts, and source-ID integrity).
- Strengthened reviewer execution readiness in `docs/testing/manual-test-scripts.md` with preconditions and minimum PR evidence requirements.
- Expanded `SKILL.md` canonical inputs to reference explicit testing artifact files.
- Added actionable stale-source downgrade workflow to `docs/core/sources/registry.md`.
- Marked core workstreams A/B/C as complete in `Tasks.txt` after artifact and consistency verification scans.
- Added `acceptance_status` and `review_evidence` tracking columns to SwiftUI and UIKit topic backlogs using tier-based positive evidence language, and marked topics as `Tier-Validated`.
- Promoted all SwiftUI and UIKit guidelines to `Status: Accepted` and aligned backlog `status`/`acceptance_status` entries to `Accepted`.
- Updated top-level and track README files to reflect accepted guideline baseline and tier-based backlog evidence fields.
- Added skills.sh install command and publish-readiness checklist to `README.md`.
- Added `agents/openai.yaml`, created a skill-facing `references/` tree, and simplified `SKILL.md` for progressive-loading runtime behavior.
- Updated README with install verification steps, expected install path, session refresh guidance, and a validation checklist.
- Clarified local vs global Codex install commands in README and added dual-scope install verification.
- Updated `SKILL.md` to lead with task-first workflows (review, improve, implement) before internal manifest routing details.
- Refined README install guidance to use a provider-agnostic default command first, with Codex-specific scope flags moved to optional troubleshooting.
- Added runtime manifest layer under `skill/manifests/` to support low-token platform/framework/task-based document loading.
- Updated `SKILL.md` with a manifest-first runtime load protocol and explicit token policy behavior.
- Updated `README.md` AI-agent workflow to resolve runtime manifests before loading long-form docs.
- Added platform-specific runtime presets so agents load tvOS/macOS-specific test scripts automatically.
- Expanded `SKILL.md` and `README.md` to include platform coverage matrix and platform-specific test artifacts.
- Added architecture-principles layer, component/interop contract templates, semantics cookbook, and OS issue tracker scaffold.
- Extended source registry with additional Tier-1 API/session anchors and Tier-2 code-heavy references from the architecture guide.
- Added strict-mode agent rules aligned to architecture-guide recommendations.
- Replaced `docs/core/known-os-issues.md` placeholder with a structured regression catalog including symptom classes, detection signals, mitigations, and source-backed entries.
- Expanded source registry with Apple forum threads, release-note anchors, and community trend links used for regression tracking context.
- Updated runtime task presets so `regression_triage` requires the known-issues catalog and regression triage playbook.
- Added visionOS track scaffolding (`README` + backlog) and manifest route/axis support.
- Added machine-readable known-issues index for low-token symptom-to-bug lookup.
- Added manifest selection examples (`skill/manifests/select-example.json`) for common runtime resolution scenarios.
- Tightened task presets so `code_review` and `test_plan` require the platform coverage matrix.
- Added known-issues maintenance workflow doc with add/verify/retire criteria.
- Added explicit `Interop Ownership` sections to key tvOS/macOS focus/modal/media/table-list guidelines.
- Added alternatives decision matrix and machine-readable decision rules so agents can choose between valid implementations deterministically.
- Updated skill runtime/task presets to require decision matrix usage in review/guideline/architecture tasks.
- Added repository-level secure prompting policy (`AGENT.md`) with explicit prohibition on arbitrary code execution.
- Added machine-readable security manifest and wired it into always-load runtime documents.
- Updated `SKILL.md` and `README.md` to require security-policy-first loading in agent workflows.
- Added curated external accessibility landscape document covering lauded projects, strong voices, and conference/transcript resources.
- Extended source registry with landscape source IDs (Apple Design Awards pages, AppleVis Hall of Fame, and conference-resource links).
- Updated architecture task preset to load external landscape references for discovery and pattern selection.
- Expanded known-issues catalog with explicit version status fields (`introduced_in`, `affected_range`, `fixed_in`, `status`, `evidence_confidence`).
- Added accessibility version matrix to centralize per-issue OS-range status and confidence.
- Updated triage/runtime docs so regression triage loads both known-issues catalog and version matrix.
- Added accessibility pattern review rubric to classify implementations as good/risky/bad with category-based scoring and auto-fail conditions.
- Added machine-readable pattern signal definitions and integrated them into runtime task presets and skill requirements.
- Rewrote `README.md` for public-facing use by removing internal development-status/task-progress sections and keeping user-focused usage guidance.
