# BigDog: one handoff, one return

The local team prepares the candidate, questions and scoring rules, then analyzes
the result. BigDog executes only the authorized job and delivers the evidence
for that analysis in its first and only response. This also applies to requests
to export existing evidence, which authorize no inference or regrading.

## One outbound handoff

Before sending, include the job ID, exact revision and seal, cases and arms,
rubric, approved model and quota, attempt/cost limits, stop conditions, permitted
grading, and a **single return destination readable by the local team**. For an
export, specify the existing run and cases instead. Include the checklist below
or pin this document in the packet. Resolve missing authorization or delivery
access locally before dispatch. No acknowledgement, capability survey, progress
message, permission negotiation, or second start signal is required.

## One inbound response

Return one bundle (or one message pointing to the entire accessible bundle)
with status **complete**, **partial**, or **blocked**. A Git return can itself
be the response; no duplicate coordinator message is needed. Storage receipts
are transport metadata, not a result. Keep raw records controller-only, out
of model inputs and public Git when sensitive.

| Include in the return | BigDog checks before sending |
|---|---|
| Scope and outcomes | Match revision, seal, provider, case and arm to every planned cell. Report first attempts, unattempted cells, stops, reservations and actual usage, separately per provider. |
| Answer and grading evidence | Deliver exact available inputs, original first answers/errors, grading prompts, original reviewer outputs and the arm-to-masked-ID mapping through the approved controller destination. Supply relative paths and hashes; worker-local paths and hashes alone are not delivery. |
| Why the grade changed | For each graded criterion, identify the verdict and rationale. Index every regression, critical flag, persistent gap and gain by case, criterion and arm. Include the decisive verbatim passages on **both** sides of an attempted pair with enough surrounding context and the reviewer rationale. For an alleged omission, include the relevant complete implementation path. Label an absent or unassessable side rather than inventing a quote. |
| Integrity and usability | From the actual return bundle, without the worker's private checkout, resolve each artifact, verify its hash and match quoted spans to the correct answer. Check coverage against the sealed case list. Report redactions and their effect on interpretation. |

Package or index already-captured evidence locally before sending; that is not
permission to call a model again. If evidence is missing, cannot safely be
shared, or quota or transport prevents completion, return **partial** with
usable evidence and precise gaps, or **blocked** if nothing can be delivered.
The local team records what can and cannot be concluded and closes the job.
Do not automatically resend, rerun, ask for missing exhibits, or promote a
summary-only result to complete. A separately authorized future job is distinct.

**Current Flash excerpt request:** receipt 1445 is already the one outbound
request. Do not send this policy as a second message. Use its single return to
review the three regressions; leave unsupported conclusions open.
