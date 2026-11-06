# Independent Controller Rubric

Development draft; do not include in subject context. Known checkout incidents
informed this family, so it is not a fresh holdout. UIKit only.

- Complete compilable ownership/integration, not methods referring to setup locals.
- Preserve the supplied button identity, title, styling, configuration, enabled
  state and existing callback wiring. Do not install a replacement payment action.
- Repeated total updates change the displayed total without activating payment,
  duplicating actions or accumulating controls. A direct activation dispatch reaches
  the preexisting fixture action once per dispatch.
- Configure scalable multiline text without a fixed enclosing height or using
  autoshrink as the response to a request for larger text.
- Accept equivalent implementations: no required class name, exact text style,
  stack type, trait observation API or adaptive-axis pattern. Static vertical is
  explicitly acceptable. Do not score semantic quality by similarity to our example.
- Unit assertions establish configuration, direct callback dispatch and ownership,
  not rendered clipping, actual input, VoiceOver delivery or universal usability.

Critical defects: lost/duplicated payment action; mutations to supplied button
styling; missing ownership that prevents compilation. Report each separately.
Grade 0-4 using the existing project quality scale, with criterion-level rationale;
do not turn one green example into proof of a gold oracle. Independent review of
prompt neutrality and accepted alternatives is pending.

The known-good fixture provides its own payment callback explicitly. This is a new
contract, not an invented callback added to any of the eight reviewed answers.
Controlled mutants (font overwrite and fixed stack height) are not model failures.

## Companion Oracle Question

`UIKIT-BUTTON-CONFIGURATION-ORACLE-D1` is a separate controller-diagnostic case.
Accept answers that investigate source writes and state/configuration resolution,
separate input configuration from effective state, and propose assertions for the
explicitly preserved fields. Do not require the exact internal description from
our observed failure. Reject declaring the component broken from whole-value
inequality alone, suppressing assertions without a replacement contract, or
claiming a specific OS behavior was executed when no tools were used. An answer
may request a minimal reproducer rather than assume the cause. No API workaround
or runtime skill rule follows automatically from this test-oracle defect.
