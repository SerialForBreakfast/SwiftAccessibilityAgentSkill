Current status: all twelve scored Haiku sessions completed under the approved subscription-percentage budget. Displayed usage remained0% five-hour/18% weekly; actual consumption is unresolved by rounded readings. Neither skill version was invoked or read in any of six relevant guided sessions. Independent source-quality grading is complete: accessibility tasks meet2/3 generic,1/3 released-available and2/3 candidate-available. No native answer tests ran. See the [executed report](../../../evals/reports/native-activation-lift-20261106/README.md).

The explicit-invocation continuation is [held by the owner](../explicit-invocation-v1/STATUS.json). See the [current reconciliation](../RECONCILIATION-20261107.md) for remote developments and distinct execution lanes.

## Historical initial proposal

The following initial design/limits are preserved as history. The executed percentage-budget run and corrected turn accounting are documented in the current report linked above; these earlier tables are not current run authorization.

> Current outcome: the initial counted probe stopped at startup. No scored sessions
> ran. See [qualification result](QUALIFICATION-RESULT.md) and the separately gated
> [repair proposal](REPAIR-PROPOSAL.json). The original plan below remains frozen.

# Native activation and skill-lift pilot

Status: owner approved the exact 13-session/52-turn allocation. Independent question
review and eight offline executor tests passed. No inference started yet; a fresh
subscription check and one counted native qualification probe remain.

## Bounded scope

| Item | Proposed bound |
| --- | --- |
| Model | Claude Haiku `claude-haiku-5-5`, subscription only |
| Scored work | Four questions × generic / released 0.2.2 / candidate 0.3.0-dev.2 =12 sessions |
| Qualification | One counted synthetic native-skill + file-read/isolation session |
| Total ceiling | **13 CLI sessions**, maximum **4 agentic turns/session**, **52 exposed turns** |
| Runtime | 180 seconds/session, 60-minute batch, serial |
| Tokens | 200,000 reported-total stop threshold; may overshoot by one session; hard token/internal-request caps unavailable |
| Tools | Native Skill and Read only; no commands, writes, network, MCP, delegation or repairs |
| Capture | 2 MiB stream/session; 8 tool calls/session; 64 KiB returned-reference-byte stop threshold, possibly one-read overshoot |
| Retries/fallback | Zero; preserve all unsuccessful/unattempted cells |

The three conditions receive identical natural developer requests. Skill bodies and
references are **not injected** into user/system messages. Released/candidate skills
are assembled only in isolated private workspaces and invoked through actual native
discovery. Reference snapshots are identical between guided conditions. Generic has
no accessibility skill. This compares installed workflows, not only body length.

Questions: one existing UIKit cell-reconfiguration smoke control, two harder native
validation/media ownership tasks with explicit accessibility product context, and
one general Swift sorting negative-trigger control. The two ownership context
revisions and negative control received independent provisional contract review. All are
**development cases**, not fresh independent holdouts. The general Swift case is not
an accessibility-effectiveness score.

## What success means

Record separately: skill advertised, intended skill body actually loaded, reference
files actually read with hashes/bytes, correct identity/version, truthful ROUTING,
false activation on the unrelated task, task quality and critical defects. Naming a
file or announcing the skill is not retrieval evidence. No trace means unproven, not
an invented read. Failure to activate stays visible even when a generic answer works.

Source quality uses an independent alternative-aware controller and preserves
inconclusive outcomes. No generated answer is executed; native compile/unit checking
requires its separate scope. One small pilot cannot meet release statistics or prove
population-wide gains. Do not pool it with earlier injected-context scores.

## Qualification findings

The installed CLI is 2.1.319. Its local help says safe-mode disables skills; earlier
injected tests therefore never exercised installed activation. Observed restricted mode suppressed the target project skill. An explicit session-local plugin advertised the target skill while restricted mode remained enabled; actual invocation still needs the counted probe. `--max-turns 4 --version` is accepted without inference even though max-turns
is absent from local help. A live counted probe must still qualify runtime behavior.

Installed bare mode requires API-key/helper authentication and is excluded under the
subscription-only policy, regardless of differences in current web documentation.
No account credential copying, global skill/settings edits or new trust grant.
Global synced skill metadata must be hidden for the isolated test; unexpected
catalog items, hooks, tools, body selection or traces stop qualification.

Primary references: [CLI reference](https://code.claude.com/docs/en/cli-reference),
[skill discovery](https://code.claude.com/docs/en/skills), and
[settings](https://code.claude.com/docs/en/settings). Installed behavior/version
controls execution; web descriptions are not runtime proof.

## Preservation and remaining work

Released 0.2.2 means the current root snapshot at the pinned commit, whose SKILL hash
differs from the older archived 0.2.2 evaluation fixture. Both original artifacts
stay unchanged; identify this new baseline by version, commit and exact hashes.
Candidate 0.3.0-dev.2 body remains immutable. Native packaging does not create a new
candidate body or a second maintainer skill in this repository.

[PROPOSAL.json](PROPOSAL.json) contains case/source hashes and exact session order;
private case files contain the complete subject text. Exact workspaces/controller are frozen and offline executor tests pass. Live native
catalog isolation/trace behavior still requires the counted probe. No live grant
exists until fresh subscription checks pass. AGY is excluded from this first native pilot because
its bounded tool-loop/trace behavior has not yet been qualified; no silent substitution.

Reviewer clarifications: external-player inspection is valid without owning player
replacement; documented edit/event APIs are valid without hidden direct-field/ABA
requirements. Missing callback/binding signatures remain integration limits.
