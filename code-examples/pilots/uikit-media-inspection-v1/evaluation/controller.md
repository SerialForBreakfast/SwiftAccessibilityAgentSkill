# UPAIR-06A Controller Rubric

Development draft; independent reviewer and model execution pending. Send only
prompt.json to the subject. This rubric, implementation, tests, incidents and
expected routes stay outside model-visible context.

Score each criterion independently 0 (missing/wrong), 1 (partial), 2 (satisfied).
Do not require these exact types, wording, helper functions or matching source.

| Criterion | Evidence expected | Critical error |
| --- | --- | --- |
| Duration | Distinguishes absent/unavailable, invalid, indefinite and usable finite time; avoids unsafe numeric conversion | Converts nonfinite duration into an integer or invents a duration |
| Stream knowledge | Keeps live/on-demand classification unknown without sufficient evidence | Treats indefinite alone as proof of live or finite alone as proof of on-demand |
| Ranges | Keeps seekable and loaded evidence separate, including gaps and no-item state | Authorizes seeks from loaded ranges or bridges gaps |
| Buffering | Preserves independent full/empty/likely flags and limits prediction claims | Full buffer guarantees uninterrupted playback |
| Rate/status | Distinguishes requested rate from waiting/playing status; retains available waiting reason | Nonzero requested rate proves playback is progressing |
| Noninterference | Inspection does not start playback, alter media selection, or overwrite control semantics | Adds diagnostic payload to spoken labels or starts playback |
| Tests and scope | Focused unit tests with finite/nonfinite, gaps, unknown and contradictory-looking states; labels injected values honestly | Claims unit fixtures establish real playback or VoiceOver behavior |

Accept a different safe duration representation, typed waiting reasons, async loading,
an observation-driven inspector, richer explicit error states, or range membership
delegated directly to CoreMedia. Tests need not match this fixture's architecture.
An empty range list observed now is not permanent inability to seek. Sampling getters
sequentially is not an atomic snapshot. A seek may fail after a valid range check.

Native evidence here validates the value layer and an empty native AVPlayer capture.
Nonempty item extraction, dynamic updates, actual media description tags and option
selection are separate open requirements. Do not credit their completion from this
packet. No audio-description fixture is supplied to the subject in this subcase.

Pair the frozen conditions on identical subject inputs only after independent review.
No-change/control-preservation is a valid outcome; do not reward gratuitous edits.
No UI test or mandatory manual verification is part of this case's acceptance.
