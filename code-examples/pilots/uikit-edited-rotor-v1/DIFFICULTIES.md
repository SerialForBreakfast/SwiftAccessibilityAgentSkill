# UPAIR-05 Difficulty Ledger

Local date2026-11-05. Assisted development, not a controlled model comparison.
Exact serving revision and full context are unavailable. Preserve accidental
failures separately from deliberate mutants and anticipated design risks.

| ID | Difficulty | Treatment and evaluation implication |
| --- | --- | --- |
| R01 | Header currentItem has a nonnull annotation while search comments describe nil initial items | Read it into an optional and test initial search explicitly; do not assume annotation alone proves runtime non-nil. This was known from earlier evidence, not a new crash. |
| R02 | Swift Character counts differ from UITextInput/Foundation offsets | Build UTF16 boundary offsets and test emoji plus decomposed accents with native targetRange text. |
| R03 | Literal substring matches may split a composed character | Filter against complete Character boundaries; test a combining mark and a joined emoji. Policy is explicit rather than presented as a UIKit requirement. |
| R04 | Stale results cannot reliably be identified using object identity alone | Invalidate old rotor callbacks by revision; restart the first new-revision request; subsequently validate full current ranges. Avoid an undocumented assumption that UIKit preserves result object identity. |
| R05 | Different matching and empty-query policies are legitimate | Document exact literal/overlap/empty-query behavior; rubric accepts valid alternatives. Do not overwrite the older text pilot's distinct empty-query contract. |
| R06 | Ordinary reading must not depend on rotor adoption | Preserve the accessible selectable text view in empty/no-match cases. Direct range selection proves compatibility, not gesture delivery. |
| R07 | Apple web pages returned HTML shells | Installed headers and comments are reviewed and hashed; API web bodies are not claimed as reviewed. |

R01-R06 are design/oracle issues addressed before execution, not spontaneous failures.
If native execution fails unexpectedly, keep the exact source/test revision and
diagnostics before repair. Full deliberate diffs are recorded in MUTATIONS.md.

## Executed outcome

Revision1 compiled and all12 positive methods passed on iOS26.5 with SDK27.0.
All five deliberate mutants failed only their selected assertions. No unexpected
native failure occurred in this tranche. These are first-attempt unit outcomes,
not independent prompt review or evidence of model improvement. See
[immutable sanitized results](validation/revision-1.json).
