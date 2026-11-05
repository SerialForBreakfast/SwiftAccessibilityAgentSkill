# ADR-001: Robust Evaluation Methodology for Swift Accessibility Agent

- Status: Accepted
- Date: 2026-09-01
- Deciders: Swift Accessibility Agent maintainers
- Tags: `evaluation`, `promptfoo`, `viewlens`, `source-governance`, `versioning`, `accessibility-research`

## Context

Swift Accessibility Agent is both a human-readable accessibility reference and an installable AI-agent skill. It will evolve as Apple platforms change, new assistive-technology behavior appears, ViewLens matures, and users discover gaps in real projects.

Without a durable evaluation method, the project risks drifting in several ways:

- The agent may answer as a generic Swift assistant instead of the versioned accessibility skill.
- The agent may skip visible routing and make repo-backed claims without naming consulted guidance.
- New documentation may improve breadth while making answers slower, less precise, or less usable.
- Prompt changes may accidentally over-trigger on generic Swift questions.
- Runtime claims may be made from screenshots or source code when accessibility hierarchy evidence is unavailable.
- The project may optimize for developer assumptions instead of real accessibility-tool users and disabled developers.

Evaluation must therefore measure behavior over time, not only validate files exist.

## Decision

Adopt a layered evaluation methodology with explicit release gates. Each layer measures a different risk and has a clear owner, cadence, and failure response.

| Layer | Name | Primary Tooling | Purpose | Release Role |
| --- | --- | --- | --- | --- |
| E0 | Package integrity | File checks, skill validation, reference-path checks | Confirm the skill is installable and discoverable. | Required for every release. |
| E1 | Prompt contract | promptfoo `C0` / `C1` / `C2` | Confirm identity, routing, source disclosure, assumptions, negative cases, and answer quality. | Required for every prompt/reference release. |
| E2 | Reference governance | Source registry review, version matrix, source freshness checks | Confirm guidance remains source-backed and Apple-first. | Required when guidance or platform claims change. |
| E3 | Runtime evidence | Optional ViewLens CLI/MCP fixtures | Confirm UI evidence can support or challenge the agent's guidance. | Required only for runtime-backed claims or ViewLens-integrated releases. |
| E4 | Closed-loop fix verification | ViewLens before/after evidence, app fixtures, regression prompts | Confirm agent-suggested fixes improve evidence without obvious regressions. | Required before claiming fix-verification capability. |
| E5 | Human/user validation | Interviews, usability sessions, accessibility review partners | Confirm the agent addresses real user workflows, pain points, and adoption barriers. | Required before broad claims about user impact. |

The default automated baseline is E0 + E1 + applicable E2. ViewLens is valuable but optional; it should not become a hard dependency for installing or using the skill.

## Evaluation Principles

1. Measure the agent as users experience it.
2. Use user-like prompts, not repo-internal phrasing.
3. Keep negative cases as first-class tests.
4. Treat routing and source disclosure as observable behavior.
5. Separate source-backed guidance from runtime evidence.
6. Treat unavailable evidence as unavailable, not as passing.
7. Version the prompt, references, and eval baseline together while the project is pre-1.0.
8. Add regression prompts for real failures discovered in usage.
9. Include disabled users and assistive-technology users in research, not only developer-maintainer judgment.
10. Prefer small, repeatable evals over occasional large audits.

## Promptfoo Methodology

Keep the existing three-config model:

- `C0`: bare model baseline.
- `C1`: agent identity and routing protocol without injected reference excerpts.
- `C2`: agent identity, routing protocol, and selected reference excerpts.

Use this comparison to answer two questions:

- Does the skill prompt improve routing and answer behavior over a generic Swift assistant?
- Do repo references measurably improve the response beyond the identity/routing protocol alone?

Minimum assertions:

- Identity probes include `Swift Accessibility Agent` and the active version.
- Repository-guided answers include `ROUTING:`.
- Routing names the expected repo documents.
- Repository-guided answers include `Sources:`, `Freshness:`, and `Assumptions:`.
- `Assumptions: none` appears only when the answer is directly supported and the user context is specific enough.
- Generic Swift questions do not trigger routing or trust footer output.
- The first response may include the identity line; later substantive answers should not repeatedly announce identity unless asked.

## Gold Prompt Design

Gold prompts must resemble real Swift developer questions.

Prompt sources:

- User questions from real usage.
- Common framework vocabulary developers use naturally, such as `UILabel`, `UITableView`, `NSWindow`, `SwiftUI`, `VoiceOver`, `Dynamic Type`, `tvOS`, and `NSHostingView`.
- Bug symptoms, such as focus loss, repeated labels, clipped text, ambiguous grouping, inaccessible custom controls, missing captions, and OS-version regressions.
- Assistive-technology workflows, such as VoiceOver rotor use, keyboard navigation, Voice Control, Switch Control, captions, braille, and Larger Text.

Prompt rules:

- Do not copy repo guideline titles into the prompt unless a user would naturally say them.
- Do not reveal expected routing in the user prompt.
- Include broad, ambiguous, and bug-like prompts.
- Include cross-platform prompts where real projects are likely to mix SwiftUI, UIKit, AppKit, or tvOS behavior.
- Include prompts from less-expert users who know the symptom but not the accessibility term.

Coverage targets:

- One identity probe.
- At least one positive prompt per accepted topic cluster.
- At least one negative prompt per common over-trigger surface.
- At least one multi-domain prompt per platform track.
- At least one assumptions/freshness prompt.
- At least one runtime-evidence prompt.
- At least one user-impact prompt grounded in assistive-technology use.

## Runtime Evidence Methodology

Use ViewLens as an optional E3/E4 evidence provider when evaluating actual UI behavior.

ViewLens evidence should be categorized as:

- `measured`: captured from platform APIs or runtime hierarchy introspection.
- `derived`: deterministic computation from measured facts.
- `inferred`: heuristic or ML-based finding.
- `unavailable`: requested evidence could not be captured.

Runtime evaluation should verify:

- accessibility names, roles, values, states, actions, hints, and grouping
- reading order and focus traversal where platform evidence permits
- rotor candidates and custom actions where evidence is available
- Dynamic Type or Larger Text layout resilience
- contrast and non-color cues
- target sizing and activation points
- visual-semantic mismatch
- modal focus containment and restoration
- before/after evidence for proposed fixes

Do not claim a screen is accessible from screenshot-only evidence. Screenshot evidence can support visual, contrast, clipping, and layout findings, but semantic accessibility needs platform or hierarchy evidence.

## Human/User Validation Methodology

Automated evaluation is necessary but insufficient. The project should maintain a lightweight research loop with people who use accessibility tools and people who build accessible Apple-platform software.

Research should include:

- blind and low-vision developers
- VoiceOver users with different rotor familiarity levels
- keyboard-only and switch-control users where possible
- Deaf and hard-of-hearing users for media/caption workflows
- low-vision users who rely on Dynamic Type, Larger Text, contrast, or Magnifier
- developers who are new to accessibility
- developers who are experienced accessibility reviewers

Research questions:

- Does the agent explain tradeoffs in terms of user outcomes?
- Does the agent help developers choose practical fixes?
- Does routing help users trust and inspect the supporting docs?
- Does the agent over-assume VoiceOver expertise, rotor fluency, or Apple-framework defaults?
- Does the agent support progressive adoption without hiding primary tasks behind advanced assistive-technology features?
- Does the agent help teams discover where runtime evidence is needed?

Research outputs should become:

- new gold prompts
- updated guideline examples
- new negative cases
- source-registry additions
- backlog topics
- release notes when behavior changes

## Release Gates

Before any release:

1. Confirm `VERSION`, `SKILL.md`, README, changelog, and promptfoo baseline agree.
2. Confirm root `SKILL.md`, `agents/openai.yaml`, and `references/` are present.
3. Confirm referenced paths resolve.
4. Run promptfoo baseline or document why it was not run.
5. Review failures as either release-blocking, expected baseline differences, or new backlog items.
6. Confirm new guidance cites appropriate source tiers.
7. Add at least one gold prompt for any meaningful new guidance behavior.
8. Add a negative case when a new trigger could over-match generic Swift questions.

Before claiming runtime verification support:

1. Capture before/after evidence with ViewLens or equivalent tooling.
2. Identify which evidence is measured, derived, inferred, or unavailable.
3. Confirm the agent does not convert unavailable evidence into a pass.
4. Preserve a short fixture or summary suitable for promptfoo regression testing.

Before claiming user-impact improvement:

1. Collect feedback from relevant users or accessibility practitioners.
2. Translate feedback into measurable prompts, docs, or backlog items.
3. Avoid broad claims such as "accessible to all" unless scoped to verified outcomes.

## Failure Triage

Classify evaluation failures as:

- `contract_failure`: missing identity, routing, trust footer, version, or assumptions behavior.
- `routing_failure`: wrong domain or missing expected source.
- `overtrigger_failure`: routing appears for generic Swift questions.
- `undertrigger_failure`: accessibility question does not trigger repo guidance.
- `source_failure`: answer makes a claim unsupported by routed docs.
- `freshness_failure`: answer treats stale or preview-only information as current.
- `runtime_overclaim`: answer claims verification without runtime evidence.
- `user_outcome_failure`: answer is technically correct but impractical, confusing, or dismissive of real assistive-technology workflows.

Each failure should produce one of:

- prompt change
- reference-doc change
- routing-table or manifest change
- new gold prompt
- new negative case
- source-registry update
- backlog item

## Versioning Policy

Evaluation changes affect versioning:

- Patch bump: new prompts, wording clarifications, or eval coverage that does not materially change runtime behavior.
- Minor bump: changed output contract, routing behavior, assumptions policy, source governance, or platform coverage.
- Major bump: stable public contract after pre-1.0.

Each promptfoo run should record:

- agent version
- prompt/config version
- reference-set version
- model/provider used
- date
- pass/fail summary
- known accepted failures

## Consequences

Positive consequences:

- Regressions become visible and actionable.
- Users can inspect which docs shaped an answer.
- ViewLens can add runtime confidence without making the skill harder to install.
- Human feedback becomes part of the measurable improvement loop.
- Versioned evals make behavior changes easier to debug.

Tradeoffs:

- Maintaining gold prompts adds overhead.
- Some failures will require judgment rather than binary pass/fail decisions.
- Runtime evidence requires fixtures and tooling discipline.
- Human research cannot be fully automated and must be scheduled intentionally.

## Follow-Up Actions

1. Add a release checklist script or documented command sequence for E0 checks.
2. Expand promptfoo tests from the gold prompt catalog.
3. Add optional ViewLens fixture excerpts under `evals/fixtures/viewlens/` when stable.
4. Add an evaluation-results template under `evals/`.
5. Add a research-notes template for converting user feedback into prompts and docs.

