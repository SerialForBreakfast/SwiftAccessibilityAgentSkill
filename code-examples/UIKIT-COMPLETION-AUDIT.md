# UIKit completion audit: in progress

Scope: the UIKit code-contract assertions in the fifteen existing U-001 through
U-015 guidelines, plus the explicitly recorded gaps in [the coverage ledger](UIKIT-COVERAGE.md).
The source implementation sections were reread on2026-11-05. This audit does not
promote the skill, replace Apple documentation or require UI/manual verification.
Native evidence currently uses SDK27 with actual iOS26.5, as recorded per package.

## Remaining evidence work

| Work | Basis | Required completion evidence |
| --- | --- | --- |
| Decorative/sibling semantics and native-default boundaries | U-001, U-004, U-005; prior headless button observation | Assert explicit decorative flags and distinct ordinary control names; distinguish configured metadata from defaults exposed through assistive technology. Preserve observed defaults without turning unsupported assumptions into contracts. |
| Long text and non-color selection | U-010, U-011 | Reconfigure long/localized strings under large effective traits; assert flexible text/row configuration and text/symbol/selected-state cues. Rendered clipping remains outside unit evidence. |
| Contrast calculation | U-011 | Verify color-space conversion and formula independently, then measure the selected semantic foreground/background combinations in supported light/dark and contrast trait configurations. Report numeric configured-color evidence, not rendered-pixel guarantees. |
| Modal content and restoration request | U-013 | Explicit title, primary and dismissal controls, inactive-background configuration and captured restoration target; verify teardown/reopen. Do not claim actual focus delivery from an argument assertion. |
| Edited rotor documents | Existing coverage ledger | Exercise retained range results after edits, overlap policy and Unicode boundaries. Keep ordinary document access intact. Preserve any failing earlier implementation as evidence. |
| Media description/inspection | U-015 and existing ledger | Source-bound description-tag metadata and separate inspection fields for stream kind, seekability, buffering/rate/selected options; validate unavailable/indefinite inputs and keep diagnostic detail out of spoken labels. |
| Availability/fallback audit | Existing ledger and ADR-003 | Verify public declarations for every selected API against deployment26.0; identify any actual guarded branch rather than inventing a fallback just to add a test. Tested SDK/runtime are recorded separately. |
| Final source-to-test audit | All15 guidelines | Link each code-contract requirement to current tests and manifest-bound passing evidence; identify documentation-supported behaviors outside the agreed unit-test boundary. Verify historical records, negative checks, offline integrity and frozen baseline hashes. |

## Evidence already available

The indexed pilots cover labels/hints/values, traits, independent actions, dynamic
containers/rotors, text ranges, typography, color/error policy, table metadata,
activation/escape, collection reuse, media selection and preference lifecycle.
Per-test claim maps and native records are under each pilot. A passing method count
is not a substitute for the final requirement-by-requirement review.

## Boundaries retained

- Unit tests can inspect configuration, direct callbacks, framework metadata and
  local computations. They do not prove speech, rendered navigation or usability.
- Apple documentation supports platform guidance without requiring these tests as
  a condition of trust. Unit observations have exact version/environment scope.
- Runtime skill files, frozen baselines and historical research remain untouched.
- Independent publication/anchor review and future annual OS anchors are separate
  from finishing this implementation's UIKit unit-test coverage.
