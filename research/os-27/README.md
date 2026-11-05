# OS 27 research corpus

Research snapshot: 2026-11-05. Status: second-pass corpus, not an exhaustive or
benchmark-approved guidance update. No skill, routing, source-registry, rubric,
scenario or release-version changes are part of this work.

## Browse by platform

[iOS](ios.md) · [iPadOS](ipados.md) · [macOS](macos.md) · [tvOS](tvos.md) ·
[visionOS](visionos.md) · [watchOS](watchos.md) · [Cross-platform](cross-platform.md) ·
[Safari/WebKit](safari-webkit.md) · [User evidence](community.md)

[Primary-source ledger](sources.md) · [All-framework topic inventory](coverage.md) ·
[Research backlog](backlog.md)

Second pass: [API availability](api-availability.md), [shipping constraints](shipping-constraints.md),
and [11 additional retrieval records](pass-2-sources.md). Five symbols now have
reviewed availability metadata. Support pages clarify iPhone/Mac subtitle hardware,
watchOS Sound Recognition, visionOS shipping features and managed-device policy.

## Scope and completeness

The goal is a traceable OS-27-family change corpus across Apple platforms. The
all-framework inventory indexes every top-level section in 15 retrieved Apple
release-note documents: 27.0, 27.2 and 27.3 beta for five platform families (iOS and
iPadOS share notes). The platform claim tables prioritize accessibility and adjacent
interaction changes. They are not a claim-by-claim summary of every OS change.

Separate breadth from depth: a topic indexed is discovered; an extracted claim with
its supporting passage is reviewed; symbol availability and shipping constraints
require their own review. Exact build reconciliation, 27.1 notes, support guides,
full WWDC session coverage and per-symbol API deltas are continuing work.

Apple announced 27.3 betas on November 3; keep this track separate from stable
features. [Apple beta announcement](https://developer.apple.com/news/?id=6gpufove)

## Evidence tiers

| Tier | Supports | Examples |
| --- | --- | --- |
| Tier-1 | Apple platform contracts, documented behavior and first-party release status | Developer API docs, release notes, WWDC transcripts, Support; WebKit team for engine behavior |
| Tier-2 | Implementation practice and editorially reviewed user experience | AppleVis editorial investigations, named expert technical articles |
| Tier-3 | Discovery and narrowly scoped observations | Individual forum reports, unverified workarounds, commentary awaiting primary-source confirmation |

An Apple announcement supports that a feature was announced. An API declaration
supports symbol availability. A release note supports the described version-specific
behavior. These are distinct evidence types even within Tier-1. Forum posts, including
posts on Apple-hosted forums, retain their author and evidential scope; hosting alone
does not turn a report into a platform contract. Populate tiers where evidence exists,
without empty boilerplate sections on every platform page.

## Thorough research procedure

1. Inventory every platform release index, major/minor release note, relevant WWDC
   session, API symbol, HIG change and Support feature guide. Include SDK tools and
   WebKit dependencies. Record retrieval failures as research tasks.
2. Review every section, not just matches for “accessibility.” Navigation, layout,
   text, media, lifecycle, keyboard, input and window changes can affect usability.
   Keyword screening helps triage; it does not establish exhaustive coverage.
3. Create atomic claims with stable IDs. Record source/section or timestamp, retrieval
   date/hash, documented release, new/changed/fixed/deprecated/known status, runtime
   minimum, SDK-link requirement, hardware/language/region restrictions and confidence
   gaps in natural language. Keep unknown availability explicitly pending.
4. Cross-check the API declaration against behavioral notes. A WWDC demonstration
   does not mean the demonstrated API was newly introduced. Shared framework notes
   need per-platform symbol availability, especially watchOS and visionOS.
5. Layer Tier-2/3 user evidence onto the claims. Record assistive technology, task,
   settings, device/build and user-reported outcome. Preserve novice ordinary
   navigation as well as experienced rotor/action shortcuts.
6. Reconcile duplicates by issue ID/symbol and preserve conflicts. Historical beta
   issues stay historical; announce-to-ship promotion requires shipping evidence.
   Maintain separate resolved and known-issue records, not generic OS bug claims.
7. Have a second research pass review the claim/source pairing and missing-platform
   matrix. Apple documentation is sufficient evidence for documented behavior;
   device tests are optional implementation/user-outcome evidence.
8. After benchmark baselines are achieved, propose small guidance changes linked to
   claim IDs and new development cases. Evaluate each candidate before promotion.
   Do not inject this corpus into baseline/C2/C3 inputs or tune heldout questions.

## Claim record for deeper follow-up

```text
ID / platform / topic:
Change and practical user task:
Type: API | behavior | SDK-linked | system feature | resolved | known | deprecation
Documented release / stable or beta / build:
Runtime minimum / linked SDK / hardware / language / region:
Tier-1 URL / section or timestamp / retrieval date / content hash:
Tier-2 or Tier-3 corroboration, author and scope:
Old behavior / changed behavior / fallback:
Evidence-supported statement:
Research inference and unresolved questions:
Proposed future development test (not added to evaluation):
Review status / reviewer:
```

## Isolation

This folder is research-only and deliberately outside `references/`, `docs/` mirrors
and `evals/`. Do not route the installed skill to it. No baseline content, candidate
runtime fingerprint or evaluation expectation is changed by collecting research.
