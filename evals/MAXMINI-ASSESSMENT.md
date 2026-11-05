# Max Mini suitability for Swift accessibility evaluations

Assessment date: 2026-11-04. Status: provisional; peer verification requested separately.
Scope: evaluation infrastructure and workload placement, not deployment qualification.

## Recommendation

Keep BigDog as the reproducible evaluation controller for now. Use Max Mini as a
candidate Apple-platform validation worker and, if its measured memory/runtime
capacity permits, a second local inference host. Do not move all jobs or expect the
same Qwen3.5-2B weights to become a better retrieval agent merely by changing hosts.
No Max Mini chip, RAM, installed model, available capacity, Xcode version or measured
throughput has been verified for this assessment. The machine nickname is not a
hardware specification. No peer benchmark or inference was run for this analysis.

## Evidence and limits

[E1] [Development results](evidence/llamacpp-development-v1.json), produced with
runner/source commit f8d0a258362bf58aec41c37bcbdd06a883137d5b: 32 candidate jobs
completed without transport failures using Qwen3.5-2B Q4_K_M, llama.cpp b11457,
16,384 context, temperature 0, seed 42 and reasoning disabled. Output truncation was
3/16 at 1,024 output tokens and 1/16 at 2,048. Both C3 prompt variants together
produced zero reference reads in 12 accessibility cases. Arm medians were about
3.45–5.41 seconds. These are correlated development cases, not independent quality
scores, cross-host benchmarks or throughput measurements under concurrent load.

[E2] [Initial smoke](evidence/bigdog-smoke-v1.json): 32 baseline/candidate jobs
completed; 12 outputs truncated and 0/4 accessibility C3 cases read references.
Source-backed answer correctness remains ungraded. C2 reference contents are
injected by the harness and must not be counted as successful model tool use.

[E3] Official [llama.cpp build documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
describes Apple Metal support. This establishes a possible runtime path, not that
Max Mini has Apple silicon, a compatible installed build or sufficient memory.

[E4] Official [llama.cpp function-calling documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md)
describes template-dependent tool support. A structured tool-call transport is
not evidence that a particular model chooses the correct tool/path. Runtime and
model behavior must be tested separately. These upstream pages are mutable;
comparisons must pin the actual binary, template and weights used.

## Workload placement

| Job | Recommendation | Reason / evidence still needed |
| --- | --- | --- |
| Harness, manifests, hashes, offline tests and scoring aggregation | Keep on BigDog; portable to Max Mini | Existing lane works. Moving orchestration offers no demonstrated quality benefit. [E1] |
| Same 2B model, same prompts and tool protocol | Comparative host trial only | Hardware can change latency/capacity and numerical output; it does not establish better reasoning or repair the observed lookup failure. [E1,E4] |
| Larger local model with stronger retrieval behavior | Candidate Max Mini role, conditional | Requires actual installed-model inventory, memory headroom and independent quality results. Parameter count alone does not qualify it. |
| Swift compilation, SDK availability checks, simulator/accessibility checks | Prefer an appropriately equipped Apple worker | Linux inference cannot substitute for Apple SDK/runtime evidence. Max Mini suitability depends on its installed Xcode/SDKs, simulator/device access and workload authority. Physical-device behavior remains a separate gate. |
| Independent answer grading | Peer review useful; retain source-backed rubric | Ask for citations to returned reference contents, factual errors and unsupported claims. Another model's agreement or confidence is not ground truth. |
| Sustained/background batches | Choose after measuring load and memory | No verified Max Mini capacity or concurrency baseline. Start serial; avoid swapping or competing with native test work. |

The most plausible quality improvement is a better model or better evidence
supply, not relocation alone. Deterministic reference selection followed by local
summarization is worth grading because C2 already supplies evidence reliably; it
still has no demonstrated answer-quality advantage. Do not label it successful
retrieval or use it to conceal C3 failures. [E1,E2]

## Proposed verification sequence (not execution authorization)

1. Max Mini confirms chip/model, total and currently available RAM, OS, installed
   llama.cpp version/backend, locally available model hashes/quantization, Xcode/SDK
   versions and competing workloads. Return public metadata only, no credentials,
   private profiles or raw system dump. Confirm whether these facts may be recorded
   in this repository before publishing host-specific inventory.
2. For host performance, use the same GGUF and frozen b11457/template where
   available. Metal and CUDA binaries necessarily differ: record each binary/build
   identity. If that revision is unavailable, record the mismatch rather than
   silently upgrading. Run the existing 32-job development lane locally through
   loopback, concurrency one, same context/output budgets, prompts and tool rules.
   No remote model listener is required. Preflight Node/runtime/API compatibility.
3. Record cold startup separately from warm case latency, input/output counts,
   finish reasons, exact successful reference paths, peak process memory and system
   memory pressure/swap. Compare like-for-like cases, not tokens/sec from unrelated
   prompts. Do not equate CUDA device allocation and Apple unified-memory RSS, or
   infer energy efficiency from speed. Stable power measurement is a separate test.
4. Evaluate a different model only in a separately identified development arm.
   Freeze prompts before heldout evaluation; do not tune on heldout material.
   First verify tool-call parsing and exact allowed reference paths. A forced tool
   smoke does not count as automatic retrieval. Use existing local weights first;
   model installation, provider calls and larger campaigns need separate scope.
5. Grade answers blind to host/model using the same source-backed rubric: factual
   correctness, omissions, unsupported claims, appropriate abstention, valid
   reference reads and truncation. Keep latency/cost and quality scores separate.
   Prefer a new host/model only after it improves the target metric without new
   correctness, safety, memory or operational regressions. Expand samples before
   production adoption; these development cases cannot establish statistical superiority.

## Verification request and next decision

Ask Max Mini to confirm or correct the assessment, report the inventory above,
identify which workload it can support now, and propose a finite comparison budget
and schedule. This is a request for assessment verification, not permission to
install models, start paid providers, execute generated Swift or run the benchmark.
Keep notification storage, peer read receipt, acceptance and actual benchmark
results separate. Until a verified response arrives, Max Mini is a potential
complement to BigDog, not a proven faster or more accurate replacement.
