# OS 27 research corpus

Research snapshot: 2026-11-05. Status: **third-pass corpus, dated 2026-11-05**. It is not a
benchmark-approved guidance update. No skill, routing, source-registry, rubric, scenario or
release-version changes are part of this work.

## Browse

Platform pages (curated accessibility and interaction claims):
[iOS](ios.md) · [iPadOS](ipados.md) · [macOS](macos.md) · [tvOS](tvos.md) ·
[watchOS](watchos.md) · [visionOS](visionos.md) · [Safari/WebKit](safari-webkit.md) ·
[Xcode tooling](xcode-tooling.md) · [Cross-platform](cross-platform.md)

Full release-note inventories (one row per Apple entry; 27.3 beta separated):
[iOS/iPadOS](inventory/ios-ipados.md) · [macOS](inventory/macos.md) ·
[tvOS](inventory/tvos.md) · [watchOS](inventory/watchos.md) · [visionOS](inventory/visionos.md) ·
[Safari](inventory/safari.md) (accessibility-scoped) · [Xcode](inventory/xcode.md)
(accessibility-scoped). Extraction script: [inventory/build_inventory.py](inventory/build_inventory.py).

Cross-cutting records:
[Releases and builds](releases.md) · [API availability](api-availability.md) ·
[Announced versus shipped](shipping-constraints.md) · [WWDC26 index](wwdc.md) ·
[Community evidence](community.md) · [Conflicts](conflicts.md) ·
[Source ledger](sources.md) · [Backlog](backlog.md)

Earlier-pass records kept as history: [all-framework topic inventory](coverage.md) (pass 1),
[pass-2 retrieval records](pass-2-sources.md).

## What the third pass added

- Entry-by-entry inventories: iOS/iPadOS 322, macOS 296, visionOS 168, tvOS 68 and watchOS
  73 release-note entries, transferred mechanically from the notes.
- Claim ID ranges: IOS-101+, IPAD-101+, MAC-101+, TV-101+, WATCH-101+, VISION-101+,
  WEB-101+, XCODE-101+, API-101+, SHIP-101+, PEND-01+, WWDC-101+, COMM-101+, C-01+.
  Pass-1 and pass-2 IDs (IOS-01..06, IPAD-01..03, MAC-01..06, TV-01..04, WATCH-01..04,
  VISION-01..06, WEB-01..06, CROSS-01..05, ANN-01..07, API-01..05, SHIP-01..06) are
  preserved and cross-referenced, never renumbered.
- 27.1 scope: only iOS 27.1 for iPhone Duo and Xcode 27.1 shipped ([releases.md](releases.md)).

## Scope and completeness

The goal is a traceable OS-27-family change corpus across Apple platforms, emphasizing
accessibility and adjacent interaction. A topic indexed is discovered; an extracted claim
with its supporting passage is reviewed; symbol availability and shipping constraints need
their own review. The OS inventories are complete for the retrieved 27.0, 27.2 and 27.3 beta
documents. Safari and Xcode inventories cover the accessibility subset only. Remaining gaps
are in [backlog.md](backlog.md).

Apple announced 27.3 betas on November 3; keep that track separate from stable features.
[Apple beta announcement](https://developer.apple.com/news/?id=6gpufove)

## Evidence tiers

| Tier | Supports | Examples |
| --- | --- | --- |
| Tier-1 | Apple platform contracts, documented behavior and first-party release status | Developer API docs and DocC, release notes, WWDC transcripts, Support pages and guides, feature-availability tables, Newsroom (for "announced" only), WebKit team posts for engine behavior |
| Tier-2 | Implementation practice and editorially reviewed user experience | AppleVis editorial, named practitioner articles, press with hands-on testing |
| Tier-3 | Discovery and narrowly scoped observations | Forum posts (including Apple Developer Forums), reader comments, search snippets, uncorroborated blogs |

Evidence type is recorded separately from tier: **announcement**, **API declaration**,
**release note**, **transcript**, **support guide** or Support release note,
**feature-availability table**, **WebKit post**. An announcement supports only that a feature
was announced. An API declaration supports symbol availability. A release note supports the
described version-specific behavior. Forum posts keep their author and scope; Apple hosting
does not make them platform contracts.

### Tier normalization from the pass-3 notes

The notes used inconsistent schemes (see [conflicts.md](conflicts.md) C-32). Mapping applied:

| Notes file | Notes tier | Corpus tier and evidence type |
| --- | --- | --- |
| shipped_features | T1 Support release notes or guides | Tier-1, Support release note / support guide |
| shipped_features | T2 feature-availability page | Tier-1, feature-availability table |
| shipped_features | T3 Newsroom | Tier-1, announcement (announced only) |
| shipped_features | T4 press; T4-snippet | Tier-2 if editorial with testing, else Tier-3; snippets Tier-3 |
| wwdc_api_availability | T1 DocC field or transcript | Tier-1, API declaration / transcript |
| wwdc_api_availability | T2 lab remark, code sample, listing category | Tier-1, transcript (informal) or code sample; weaker than release notes |
| wwdc_api_availability | T3 inference | Research inference, untiered |
| visionos | T1 Apple docs and Support | Tier-1 |
| visionos | T2 Newsroom, WWDC transcripts | Tier-1, announcement / transcript |
| visionos | T3 press | Tier-3 (snippets) or Tier-2 |
| safari_webkit_xcode | T1 release notes, DocC, WebKit posts | Tier-1 |
| safari_webkit_xcode | T2 WWDC sessions; T3 group-lab Q&A | Tier-1, transcript (lab answers informal) |
| ios_ipados, macos, tvos_watchos, community_evidence | Tier-1/2/3 or T1/T2/T3 | Same tiers; editorial summaries seen only as snippets are Tier-3 |

Sources read through a summarizing fetch tool are marked "quote needs verification against
live page" in [sources.md](sources.md).

## Thorough research procedure

1. Inventory every platform release index, major and minor release note, relevant WWDC
   session, API symbol, HIG change and Support feature guide, including SDK tools and WebKit.
   Record retrieval failures as research tasks.
2. Review every section, not just matches for "accessibility". Navigation, layout, text,
   media, lifecycle, keyboard, input and window changes can affect usability.
3. Create atomic claims with stable IDs. Record locator, retrieval date and hash, release,
   status, runtime minimum, SDK-link requirement, hardware, language and region limits, and
   gaps. Keep unknown availability explicitly pending.
4. Cross-check API declarations against behavioral notes. A WWDC demonstration does not mean
   the API was newly introduced. Shared framework notes need per-platform availability.
5. Layer Tier-2 and Tier-3 user evidence onto claims with assistive technology, task,
   settings, device and build, and outcome.
6. Reconcile duplicates by issue ID or symbol and preserve conflicts. Historical beta issues
   stay historical; announce-to-ship promotion requires shipping evidence.
7. Have a further pass review claim and source pairing and the missing-platform matrix.
8. After benchmark baselines are achieved, propose small guidance changes linked to claim IDs
   and new development cases. Evaluate each candidate before promotion. Do not inject this
   corpus into baseline, C2 or C3 inputs or tune heldout questions.

## Claim record for deeper follow-up

```text
ID / platform / topic:
Change and practical user task:
Type: API | behavior | SDK-linked | system feature | resolved | known | deprecation
Documented release / stable or beta / build:
Runtime minimum / linked SDK / hardware / language / region:
Tier / evidence type / URL / section or timestamp / retrieval date / content hash:
Tier-2 or Tier-3 corroboration, author and scope:
Old behavior / changed behavior / fallback:
Evidence-supported statement:
Research inference and unresolved questions:
Proposed future development test (not added to evaluation):
Review status / reviewer:
```

## Isolation

This folder is research-only and deliberately outside `references/`, `docs/` mirrors,
`evals/` and `SKILL.md`. Do not route the installed skill to it. No baseline content,
candidate runtime fingerprint or evaluation expectation is changed by collecting research.

## Promotion

Research stays isolated until the agreed benchmark baselines exist. Promotion then requires
a small source-backed candidate change linked to claim IDs, affected development cases, a
frontier-agent evaluation of quality and efficiency, and a regression review before any
released skill guidance changes. See [backlog.md](backlog.md).
