# UPAIR-06B Controller Rubric

Draft development case; independent review pending. Send only prompt.json to the
subject, never fixture implementation, mutation code, incident history or this rubric.

Score each row 0 (wrong/missing), 1 (partial), 2 (satisfied). Accept valid alternative
types, loading structure and error representations; do not require our exact API wrapper.

| Criterion | Required outcome | Critical error |
| --- | --- | --- |
| Description metadata | Uses actual media characteristics, separately reports language/name | Treats all alternate audio or a track name as proof of description |
| Native extraction | Loads actual local asset groups/duration with error handling | Injected Boolean is presented as proof of native extraction |
| Selection | Reports current options without changing them; subtitle-off stays off | Inspector changes selected audio or silently enables captions |
| Missing information | No item, absent group and load error remain distinguishable | Error silently reported as no available descriptions |
| Content claim | Explicit tag is evidence of declared metadata | Tag proves audible narration quality or full accessibility |
| Lifecycle | Asynchronous result is scoped to the inspected item | Claims a result must still describe the player's current item after replacement |
| Tests | Tagged/untagged fixtures, selection preservation, missing/error cases and scoped assertions | Unit result presented as actual playback or assistive-technology delivery |

Fixtures may be generated with AVAssetWriter or another documented local method;
do not require the byte-patching utility. Accept explicit unavailable/failure objects
or thrown errors, provided failure is not collapsed into absence. Language matching
must not be used as the sole discriminator for audio description.

Do not require UI tests, speech checks or mandatory manual verification. Preserving
controls means no speculative accessibility edits merely to make the inspector look
more comprehensive. Existing correct behavior may remain unchanged.

Model evaluations must use identical subject payloads per condition. This exposed
case is development material, not a new holdout. First answers and authorized repairs
must be recorded separately. No model run has been performed for this packet.
