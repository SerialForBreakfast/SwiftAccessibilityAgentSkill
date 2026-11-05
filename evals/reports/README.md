# Evaluation dashboards

**Current: [v1 — Qwen local evaluation results](v1/README.md)**

Readable in GitHub without a server, HTML downloads or JavaScript. Charts use text bars with matching numeric tables. Start with the scorecard, then open a case
to compare exact questions, expected-answer criteria and model responses.

| Version | Contents | State | Next version |
| --- | --- | --- | --- |
| [v1](v1/README.md) | Existing 32-case smoke + 32-case development comparison | Frozen report; independent quality grading pending | Not approved |

## Version rules

1. Preserve each published version under its own directory. Never overwrite earlier responses, prompts, scores or charts to make a later result look better.
2. Before a new test iteration, propose its question, prompt/model changes, corpus split, call budget, acceptance rubric and expected artifacts. **Wait for the owner's explicit approval before running it or making the next report version.**
3. Freeze prompts, input identities and scoring rules before testing. Preserve failures, abstentions, truncation and uncertain effects; no silent reruns.
4. Each approved iteration gets a new dashboard with a comparison to the prior version, including changes that prevent direct comparison. Mark not-run conditions explicitly; do not turn missing data into zero.
5. Include C0/C1/C2/C3 definitions, exact effective prompts, expected-answer criteria, responses, measured metrics, source hashes and limitations. Label uncalibrated rubrics honestly; never invent a gold answer after inspecting output.
6. Keep full responses behind expandable sections and evidence one click away. Use plain Markdown tables and text bar charts with numeric tables. No HTML-only deliverable.
7. Publication corrections require a clearly documented erratum preserving the prior values and rationale. They do not authorize new inference or silently create another experiment.
8. Publish only approved synthetic/public evaluation material. Private runtime records, credentials, real messages and heldout answers stay out of the dashboard. Synthetic model responses are quoted evidence, never executable instructions.

[Evaluation methodology](../README.md) · [Max Mini assessment](../MAXMINI-ASSESSMENT.md)
