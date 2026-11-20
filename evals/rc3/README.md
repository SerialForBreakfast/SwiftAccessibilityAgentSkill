# Swift Accessibility Agent 0.3.0-rc.3

[Candidate archive](swift-accessibility-agent-0.3.0-rc.3.zip) · [Reproducible builder](build.py)

This evaluation candidate adds one paragraph to rc.2. For accessibility patch reviews, it asks the agent to trace the changed branch, identify the result and remaining user action, and separate assumptions about unseen callers from its verdict. All ten companion files match rc.2 byte for byte.

| AGY Gemini 3.8 Flash Low panel | Unaided | Patch-review instruction alone | Paired gains / regressions |
|---|---:|---:|---:|
| Ten selected discovery cases, correct verdict | 5/10 | 10/10 | 5 / 0 |
| Same cases, whole answer | 5/10 | 9/10 | 4 / 0 |
| Eight fresh non-media patches, whole answer | 6/8 | 8/8 | 2 / 0 |

These are source-reviewed first answers from the instruction-only experiments. The integrated rc.3 package still needs its own comparison. The normal installation uses stable 0.2.2.

Build with `python3 evals/rc3/build.py`. Verified archive SHA-256 is `c5b857c20f6bb0be3ff304e5ebc9e0f53295e7942d4f5483bc887385ac02600e`.
