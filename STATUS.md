# Current release decision

**0.2.2 is released. 0.3.0-rc.1 is the one installable candidate.** SwiftUI development is open on iOS, macOS and tvOS. iPadOS-specific expansion, watchOS and visionOS are deferred. Existing historical material stays in place.

| Question | Current evidence |
|---|---|
| Can a user install the RC without switching the default release? | Yes: [archive and local install instructions](evals/rc1/README.md). Project-local copy installed with the existing skills CLI; compared to all archive files. No model session used. |
| Can we grade code without an LLM reviewer? | [Twelve bounded development tasks](evals/rc1/RUBRIC.md) check executable Swift contracts across six cells. The [fixture scorecard](evals/rc1/scorecard.json) separates compilation from the expected runtime verdict. One qualified target per task is not a platform support matrix. |
| Does the installed RC activate or improve answers? | Unknown. Offline qualification covers neither. No model calls, quota grants, paid runs or release promotion. |

**Next decision:** qualify the disposable offline submission worker before using third-party answers. Then separately authorize one bounded comparison with released 0.2.2, including repeated baseline observations and explicit versus automatic native invocation. Keep known development cases separate from holdouts.
