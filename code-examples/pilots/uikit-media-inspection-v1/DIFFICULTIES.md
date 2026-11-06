# UPAIR-06A Difficulty Ledger

Work date2026-11-05. These observations come from assisted development, not a
controlled model comparison. Exact serving revision/context are not recorded.

| ID | Classification | Observation and treatment |
| --- | --- | --- |
| MI01 | Source access limitation | Apple pages exposed markdown links; web tool rejected text/markdown. Reviewed installed SDK headers instead and pinned them. Web bodies are not claimed reviewed. |
| MI02 | Anticipated design risk | Indefinite duration is not a stream-type oracle. Keep classification explicitly supplied, with unknown default. |
| MI03 | Anticipated design risk | Loaded data and seekable ranges can differ and have gaps. Test separate values and half-open membership, not a single min/max envelope. |
| MI04 | Anticipated design risk | Full buffer can coexist with a false likely-to-keep-up prediction. Preserve both fields rather than derive one from the other. |
| MI05 | Evidence boundary | Injected snapshots cannot validate extraction from actual audio-description tracks. Keep that work open rather than treating DTO assertions as framework behavior. |
| MI06 | Authoring defect | Initial coverage JSON used U-014 (table/form) rather than U-015 (media). File-name audit caught this before case pinning; corrected mapping. No native code or baseline affected. |
| MI07 | Oracle limitation | Checking an unrelated button is a narrow noninterference assertion, not proof of all UI semantics. Capture takes no control argument and tests no speech. |
| MI08 | Documentation tooling error | A multi-file apply_patch used an unmatched heading context in evals/README.md and was rejected before applying. Retried with exact inspected context; not a Swift or evaluation failure. |

Exact intentional defects are separate in MUTATIONS.md. Preserve any unexpected
native failure with its original code, diagnostic and environment before repairs.
Do not attribute these design risks to other models without independent runs.

## Native outcome

First-attempt compile and all nine positive methods passed. Three manufactured
defects were rejected by their selected assertions. No unexpected Swift failure
was observed. Exact code is retained in NegativeFixtures and MUTATIONS.md;
[diagnostics and environment](validation/revision-1.json) remain separate from
independent prompt review and model evaluation, neither of which has run.
