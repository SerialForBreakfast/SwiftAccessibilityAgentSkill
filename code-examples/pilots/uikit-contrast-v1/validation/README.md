# Revision1 Native Evidence

The [sanitized records](revision-1.json) bind exact manifest inputs, selected tests,
environment, original record/log hashes and configured semantic-color observations.
Raw process logs and xcresult bundles remain private and immutable.

All six native checks met expectations on the first attempt: compile success, nine
passing positive methods, and four expected-negative checks with exactly the
selected failed test identities. No unexpected Swift compiler or native assertion
failure occurred. The separate offline invocation mistake is preserved in the
difficulty ledger rather than hidden as a successful test.

## Interpretation

The positive suite has nine distinct methods. Four separate intentional mutations
remove linearization, use the wrong destination color space, ignore supplied traits,
or discard alpha. Their expected assertion failures are test-sensitivity evidence,
not spontaneous model failures. Do not count their executions as additional positive
methods or independent scenario families.

The configured `.label`/`.systemBackground` pair measured21:1 in light/normal,
light/high, dark/normal and dark/high trait contexts in the positive run. This is
an observation at the recorded anchor, not a promise for future palettes, other
semantic colors, visual materials or rendered pixels.

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430, arm64,
deployment26.0 and actual iOS26.5 build23F77 for unit checks. Compile-only evidence
has no runtime. Local work date is November5,2026; raw UTC dates are November6.

Run `node --test code-examples/tools/contrast-contract.test.mjs` to check source
hashes, distinct source authorities, paired-case separation, native outcome bindings
and the four recorded measurements. Independent case review and model evaluation
remain pending; native evidence does not promote the skill or change source tiers.
