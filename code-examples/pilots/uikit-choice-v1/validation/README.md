# Revision1 Native Evidence

[Sanitized results](revision-1.json) bind the manifest, input hashes, exact test
identities, environment and original private log/record hashes. All six checks met
their expectations on the first native attempt. Nine positive methods passed and
each of four manufactured defects failed its selected assertion. There were no
unexpected compiler or native assertion failures and no repair revision to conceal.

| Check | Observed result | Contract outcome |
| --- | --- | --- |
| compile-choice | Compile success | Passed |
| choice-unit | Nine positive methods passed | Passed |
| singleline-negative | Unlimited-line assertion failed for both configured labels | Expected negative passed |
| fixedfont-negative | Preferred body-font size/descriptor assertions failed | Expected negative passed |
| staleselection-negative | Selected trait remained after deselection | Expected negative passed |
| clobberedtraits-negative | Unrelated updatesFrequently trait was removed | Expected negative passed |

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430, arm64,
deployment26.0 and actual iOS26.5 build23F77 for unit checks. Compile-only evidence
has no runtime. Local work date is November5,2026; raw UTC timestamps are November6.

This establishes explicit configuration and direct metadata assertions, not rendered
fit, actual controller input, speech, navigation or usability. Source tiers and
annual anchors are unchanged. Independent source/oracle/prompt review remains pending.
No gold promotion, model run or measured skill improvement follows from these passes.

Run `node --test code-examples/tools/choice-contract.test.mjs` for offline checks
of source hashes, coverage, paired-case separation and native-result bindings.
Raw process logs and xcresult bundles remain private; exact deliberately broken
Swift is retained under `NegativeFixtures/` and shown in `MUTATIONS.md`.

Final offline check: all175 combined library/evaluation tests passed; all210 frozen
baseline files and87 historical evidence pins verified. The runtime candidate hash
remains `3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
The dedicated pilot simulator was confirmed shut down after execution.
