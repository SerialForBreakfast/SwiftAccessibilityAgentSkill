# Actual Media Selection

When a user asks for real caption/audio choices, connect the visible selection to
the current item's actual media-selection group. Changing a local selected string
does not apply a native media choice. Preserve the player, unrelated audio/subtitle
choices and valid native defaults.

For a full-caption selector, distinguish full subtitle tracks from forced-only
tracks. That is product policy, not a rule to hide forced tracks everywhere. If a
currently selected native option is outside the displayed list, represent it as a
current/unlisted choice rather than silently calling it Off or clearing it. Off
must respect the group's empty-selection permission.

SDK declarations support availability; local synthetic media tests support their
named selection observations, not narration quality or production stream coverage.
Load companion source or units only when a code example or reproducible check is
requested. Use the user's architecture when it satisfies the same contract.
