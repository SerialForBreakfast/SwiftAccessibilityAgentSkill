# Proposed controlled skill-lift milestone package

Offline preparation, not an approved evaluation. The prior operational-rubric and
skill-lift checkpoint is committed locally as **fd31933**, not pushed. This package
is the uncommitted continuation. Released skill and frozen baselines are unchanged.

## Selection at a glance

| Inventory | Count | Meaning |
| --- | ---: | --- |
| Original development questions | 60 | Original subject bytes retained |
| Proposed selection | 24 | 18 domain applications plus six controls |
| Domain lanes | 6 | Three questions per platform/framework lane |
| Topics represented | 8 | All current task topics |
| Related families | 12 | Platform variants are not independent families |
| Proposed message payloads | 48 | Two per question; not a call allocation |
| Quarantined | 4 | Three primary-source mappings plus one ambiguous native-control premise |
| Deferred development cases | 32 | Not holdouts and not silently discarded |
| Approved calls / new model runs / spend | 0 / 0 / $0 | No provider or execution path |

[Selection](selection.json), [manifest](manifest.json) and the [review packet](REVIEW.md)
are controller-only. Do not give the subject agent this directory or the repository.
Only a single approved payload's `messages` belong in an isolated subject invocation.

## What would be compared

The initial design measures **generic assistance versus candidate-controlled context**:

- Generic arm: C0, a generic Swift assistant and the same user request, no skill text,
  reference injection, branding or protocol expectations.
- Candidate domain arm: C2, exact dev.5 subject body plus one task note and one routed
  guideline supplied inline. File names are supplied evidence, not tool reads.
- Candidate control arm: C1, the same candidate instructions with no references.
  These questions probe no-change, ownership, source absence or version boundaries.

All cells share text-only/no-tools boundaries. Candidate source content is the
intended variable; user request bytes and common host constraints match. Protocol
is scored separately; a C0 answer is not penalized for missing skill branding.

This does not isolate instructions from references on every task, compare against
the released skill, demonstrate C3 autonomous lookup, or test installed discovery.
Those require separately scoped conditions. The design avoids automatically
multiplying all questions by every possible arm or repetition. Report C1/C2 strata
and scenario-family uncertainty, not 48 independent questions.

## Payload and review integrity

Files under `payloads/` contain only structured system/user messages. Expected routes,
accepted alternatives, family IDs, assertion evidence, grades and review status stay
in the manifest/controller records. Every serialized payload, original question,
rubric corpus, candidate body and selected reference has an identity/hash. Tokens
remain unavailable; the proposed 24,000-byte input ceiling is not a token estimate.

A real harness must disable tools and isolate every subject from repository files,
other arm outputs, previous sessions, auto-loaded project instructions and global
skills. Declaring no tools in a prompt is not proof the harness enforced it.
Isolation is an explicit pending preflight item, not an accomplished setup.

## New prompt issue found before a model run

The original tvOS/UIKit semantics draft describes a standard switch. The installed
AppleTVSimulator27 SDK declares `UISwitch` unavailable on tvOS. Since a custom on/off
control is possible but unspecified, this is **premise ambiguity**, not proof every
interpretation is impossible and not a model failure. The original question and SDK
excerpt/hash are preserved in [the quarantine record](prompt-quarantine.json).

A [separate draft replacement](repairs/tvos-uikit-semantics-v2.prompt.md) uses a
supplied working UIButton and explicit title/callback facts. Its rubric is separate,
review is pending, and it has not been silently substituted into the selected run.
No original prompt, historical grade or candidate snapshot was repaired in place.

## Offline checks and execution boundaries

```sh
node research/evaluation/milestone-package-v1/package.mjs check
node --test research/evaluation/milestone-package-v1/integrity.test.mjs
```

`check` reports integrity separately from pending review/approval. A successful exit
means package integrity only; it does not mean evaluation is approved. Corrupted
inputs/payloads fail integrity. `build` refuses to overwrite the sealed package;
selection/payload changes require a new package revision. There is no execute mode,
provider import, remote setup, worker message or model API client in this package.

Live execution remains blocked on independent prompt/oracle review, source
applicability, actual harness isolation, model/provider identity, explicit call/quota
allocation, output/total-token and time ceilings, and owner approval. These are run
prerequisites, not mandatory manual accessibility/UI verification. Editing a manifest
approval flag cannot activate this offline module.

The 48 cells are a proposed reviewable design, not an approved budget. Review may
reduce or change the design before a new revision is sealed. The existing frozen
held-out set is neither copied nor promoted into this development package.

## Validation checkpoint

The full offline suite passes 1,300 checks, including 34 package checks. Exact output
is preserved in [offline-checks.log](offline-checks.log), preflight results in
[preflight.json](preflight.json), and artifact identities in [checkpoint.json](checkpoint.json).
The existing baseline verifier still validates 210 files and the historical verifier
validates 87 pins. Protected sources match fd31933; whitespace and scoped Markdown
checks pass. Counts validate machinery, not new accessibility or model behavior.
