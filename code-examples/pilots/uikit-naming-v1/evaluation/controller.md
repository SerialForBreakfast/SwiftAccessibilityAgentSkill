# UPAIR-01 Controller Case: Naming and Independent Controls

Status: draft; independent source/oracle/prompt review pending. Split: development.
Requirement links: FR-01/02/03/07/10 in the failure-driven PRD. Do not inject this
file, the implementation, tests, mutation variants or incident ledger into subjects.

## Task Contract

The question supplies the visible card contents and desired ordinary operations.
It requests Swift configuration and unit tests, not pixel layout or a runnable app.
There is no requirement to match `ItemActionCard` or any exact method name.
The plain prompt is the complete proposed subject input. Environment: iOS26 minimum,
UIKit; selected SDK/runtime must be supplied by the worker, not inferred from this prose.

## Atomic Rubric

| Criterion | Weight | Executable example contract / acceptable alternatives |
| --- | --- | --- |
| Decorative mark excluded while meaningful title remains | 1 | `testDecorationIsExplicitlyExcluded`; omitting a decorative accessibility element is also valid |
| Independent Open and Save controls remain available | 2 | `testContainerPreservesIndependentControls`; alternative container layouts allowed, collapsing into a single actionless element is critical lost functionality |
| Contextual names identify each item and operation | 1 | `testRepeatedVisibleTitlesHaveContextualNames`; equivalent localized wording or appropriately demonstrated context accepted |
| Same-instance reconfiguration replaces item names | 1 | `testReconfigurationReplacesNamesWithoutReuseCallback`; no dependency on a reuse callback absent from the task |
| Complete localized names are supported | 1 | `testCompleteLocalizedNamesArePreserved`; valid localization APIs accepted, exact French strings not required |
| Ordinary actions remain independent and current | 2 | `testOrdinaryActionsRemainIndependent`, `testReconfigurationReplacesHandlersWithoutDuplicates`; target/action, UIAction or other correct wiring accepted |
| Unit assertions are bounded and defensible | 1 | No claim property tests prove speech/navigation/layout; meaningful assertions rather than mocks of the asserted implementation |

Normalize earned weights to the existing 0-4 task-success scale; grade correctness,
calibration and relevance separately using evals/GRADING.md. Record critical API,
availability, fabricated-evidence and lost-functionality errors independently of
the numerical total. Wrong callback identity or duplicate operations is substantive.

`testReconfigurationResetsOwnedContainerState` is additional resilience evidence,
not a hidden requirement to repair arbitrary external mutations in every solution.
The selected example owns these properties. Do not reject an otherwise valid answer
solely because it does not reset state that the prompt never assigns to it.

## Oracle and Mutation Review

- ExposedDecoration deliberately changes the decorative flag to true.
- HiddenControls deliberately sets the descendant-hidden flag to true.
- StaleNames deliberately assigns the Open name only when it is initially nil.

The corresponding selected test must fail with its intended assertion. Compiler,
simulator and harness failures are not successful mutation kills. These mutations
are manufactured sensitivity checks, not model-generated failures.

Review must confirm test evidence and API source scope, score one alternate valid
implementation, and inspect the neutral prompt for ambiguity before freezing.
No actual model output, cross-model failure or skill gain has been observed here.

## Experiment Plan

New overlay only, never change frozen OS26 prompts in place. After independent
review, propose one approved frontier model with C0/C2, clean isolated contexts,
identical user task, first attempt preserved, zero-spend quota ceiling. C1/C3 and
other models follow separately qualified plans. This document authorizes no runs.

Candidate skill opportunities if failures reproduce: preserve independent controls,
refresh metadata during reconfiguration, distinguish decorative from meaningful
content, and avoid claiming assistive-technology behavior from property assertions.
The unit fixture is evidence, not proof that any model needs all these instructions.
