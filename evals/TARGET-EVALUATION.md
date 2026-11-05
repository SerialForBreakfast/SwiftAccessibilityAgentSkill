# Evaluate for the intended user

## Product hypothesis

The intended user is a Swift developer using a capable frontier coding agent to
review or modify Apple-platform UI. The skill supplies specialized accessibility
guidance, source-backed availability distinctions and efficient reference lookup.
It is not intended to turn a weak general model into a production Swift engineer.

Our hypothesis is that the skill improves an already-capable agent's accessibility
decisions without harming ordinary Swift work. Current small-model reports do not
establish or disprove that hypothesis. Frontier effectiveness remains unmeasured.

## Three separate lanes

| Lane | Purpose | How results influence the skill |
| --- | --- | --- |
| Frontier coding agent, primary | Realistic code review, editing, retrieval and OS migration | Primary product and eventual release evidence |
| Independent comparator/judge | Check generalization and grading reliability | Detect provider-specific overfitting and grading errors |
| Local small model, diagnostic | Harness validation, protocol failures, capacity boundaries | Fix general defects; do not simplify away useful guidance solely to make this lane pass |

BigDog and MaxMini remain useful for offline validation, artifact processing, privacy-
preserving diagnostics and native SDK checks. They need not host a frontier-sized
model to contribute. New local-model sweeps are secondary to exporting and grading
existing evidence. Compact/lite variants require a distinct user need and experiment;
they are not the default optimization target.

## Feasibility gates

1. Establish that the selected agent can handle representative Swift tasks without
   the skill: compile-ready fixes, ordinary framework use and basic tool operation.
   Report failures rather than filtering them out of the test population.
2. Compare C0/C1/C2/C3 on identical realistic development fixtures. Include working
   code with independent controls, focus restoration, availability guards and media
   semantics. C2 isolates supplied knowledge; C3 tests actual retrieval.
3. Add a separately labeled installed-agent lane for multi-file edits and tool use.
   The current text-generation harness is not an IDE or full agent evaluation.
   Keep tool access, starting repository and budgets matched between arms.
4. Grade functional preservation and accessibility correctness before formatting.
   Check code with pinned SDKs where appropriate. Assess source honesty and routing
   separately. Human usability claims require user evidence beyond prompt scores.
5. Report gains, unchanged competent answers and regressions. Easy C0 successes
   belong in non-regression coverage; do not remove them to inflate skill benefit.
6. Optimize reference loading only after quality is established. Measure real input
   tokens and reads; useful detail is not waste merely because a tiny model overflows.

## Next frontier experiment

Choose one owner-approved frontier coding deployment and an independent grader,
then freeze exact accessible model identities, reasoning settings, tool contract,
context/output budgets, provider API and spend ceiling. Do not assume a model name,
subscription or local hardware inventory establishes API access or budget approval.
No provider is silently substituted. No paid calls are authorized by this document.

Start with a small development pilot spanning code fixes, OS-sensitive advice,
independent actions, missing evidence and irrelevant triggers. Retain the original
60-family suite; develop richer atomic cases under a new catalog revision. Keep
heldout frozen. Calibrate the grader using correct answers and known-error mutations
before trusting semantic scores. Reuse exact-context duplicate grades, not just
identical token counts. Choose the release design before inspecting candidate results.

The existing frozen release gates remain unchanged. A future frontier-focused
protocol revision must name its primary comparisons and separately report local
diagnostics, C0 A/A noise, platform regressions and uncertainty. Do not pool weak
local and frontier model scores into one release headline.
