# Research basis and adaptation

Sources reviewed online earlier in this chat, November 6, 2026. This tranche applies
those findings to measurement design, not runtime guidance. These studies are not
Swift/accessibility validations; recent preprints are provisional empirical evidence.
No reported benchmark improvement is imported as a claim about this skill.

| Primary source | Finding used | Adaptation and limit |
| --- | --- | --- |
| [SkillsBench](https://arxiv.org/abs/2602.12670) | Matched skill/no-skill evaluation and deterministic task verifiers; focused skill bundles can outperform exhaustive ones | Keep task outcomes and package size separate; retain held-out scenarios. This is not proof that our notes improve Swift answers. |
| [The Regression Tax](https://arxiv.org/abs/2607.22520) | Skills can introduce regressions; aggregate gains hide lost capabilities | Report gain, regression, preservation and persistent failure per pair. Preprint findings motivate tests, not universal causal claims. |
| [Demystifying Agent Skills](https://arxiv.org/abs/2608.14036) | Retrieval and downstream usefulness differ; brittle assumptions and incompatible contexts matter | Separate activation/read provenance from task correctness. Exact expected-reference matching is not a substitute for acceptable alternatives. |
| [Anthropic evaluation guidance](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) | Prefer deterministic grading where appropriate, inspect grading defects, allow partial success and valid solutions | Preserve code/unit evidence and unknown outcomes; compare same frozen rubric. Transcript review is not mandatory manual accessibility verification. |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Realistic trigger/non-trigger queries and independent blind comparisons | Add near misses and ambiguity. Vendor-specific model-call loops are not enabled. |
| [Context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Small high-signal context, not arbitrary brevity | Measure full relevant context and actual reads; do not delete needed constraints based on byte count alone. |
| [GEPA](https://arxiv.org/abs/2507.19457) | Generalize improvements from execution feedback and test candidate instructions | Use evidence-driven hypotheses. Automated optimization still needs model calls; no optimizer was installed or run. |
