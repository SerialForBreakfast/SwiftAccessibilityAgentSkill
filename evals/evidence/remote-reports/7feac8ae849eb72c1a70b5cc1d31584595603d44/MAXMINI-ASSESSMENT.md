# Max Mini suitability for Swift accessibility evaluations

Assessment date: 2026-11-04. Status: peer capability reports received; comparative performance remains unqualified.
Scope: evaluation infrastructure and workload placement, not deployment qualification.

## Recommendation

Keep BigDog as the reproducible evaluation controller for now. Use Max Mini as a
candidate Apple-platform validation worker and, if its measured memory/runtime
capacity permits, a second local inference host. Do not move all jobs or expect the
same Qwen3.5-2B weights to become a better retrieval agent merely by changing hosts.
Max Mini reports an Apple M4 Mac mini with 24 GB unified RAM and an installed
Apple development toolchain. This strengthens the native-validation recommendation,
but does not establish available inference capacity or superior model quality.
The inventory below is peer-reported, not independently inspected by BigDog. No
peer LLM benchmark was run for this analysis. [E5,E6]

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
describes Apple Metal support. Together with the reported M4 hardware, this
establishes a possible runtime path, not an installed compatible llama.cpp build
or sufficient memory for a particular model/context. [E5]

[E4] Official [llama.cpp function-calling documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md)
describes template-dependent tool support. A structured tool-call transport is
not evidence that a particular model chooses the correct tool/path. Runtime and
model behavior must be tested separately. These upstream pages are mutable;
comparisons must pin the actual binary, template and weights used.

## Peer-reported inventory and readiness

[E5] Capability report `nuiak-maxmini-accessibility-capabilities-20261104-v1` and
[E6] inventory supplement `nuiak-maxmini-accessibility-model-inventory-20261104-v1`
arrived through Max Mini's NUIAK coordinator identity. BigDog reviewed both reports
and acknowledged receipt. These identifiers provide provenance; private message
bodies and host reports are not included here. The owner requested publication of
this update; the peer also reported permission to publish sanitized host metadata.

| Item | Peer observation | Qualification limit |
| --- | --- | --- |
| Hardware | Mac mini Mac16,10; Apple M4; 10 CPU cores (4P/6E), 10 GPU cores; 24 GB unified RAM | No comparable inference timing or capacity reservation |
| OS/toolchain | macOS 27.0.1 (26A434); Xcode 27.0 (27A266a); Swift 6.4; macOS SDK 27.0 | Reported versions; simulator/device coverage and actual task checks remain unverified |
| Memory | `memory_pressure` reported 63% free at observation | Transient observation, not guaranteed allocatable model memory or VRAM |
| Harness tools | Node 23.9.0, npx 10.9.2, Git 2.47.0 | Existing evaluation lane has not run on this host |
| Python/Metal | Python 3.13.2, PyTorch 2.13.0; MPS 2x2 matrix smoke returned sum 8 outside sandbox; Coremltools 9.0 | Sandbox reported MPS unavailable; tiny tensor operation is not LLM/runtime qualification |
| Serving | Ollama client 0.40.11 installed; server stopped; no llama.cpp CLI on PATH; no MLX/Transformers in NUIAK environment | No ready inference endpoint; absence from PATH/environment is not a whole-host installation audit |
| Workload | Peer reports readiness for offline harness and Apple SDK checks | No resources reserved and no benchmark execution authorized by this assessment |

The following are **manifest-declared model layers**, not independently rehashed
blobs, loaded models or validated tool-calling configurations. Tags alone do not
establish architecture, parameter count or equivalence with BigDog's pinned 2B
weights. Layer sizes exclude possible companion assets and runtime/KV memory. [E6]

| Manifest tag | Quantization | Declared layer bytes | Declared SHA-256 |
| --- | --- | ---: | --- |
| gemma4/12b | Q4_K_M | 7381382048 | `1278394b693672ac2799eadc9a83fd98259a6a88a40acfb1dcaa6c6fc895a606` |
| gemma4/e4b (latest alias) | Q4_K_M | 9608338848 | `4c27e0f5b5adf02ac956c7322bd2ee7636fe3f45a8512c9aba5385242cb6e09a` |
| llama3.1/8b | Q4_K_M | 4920738944 | `667b0c1932bc6ffc593ed1d03f895bf2dc8dc6df21db3042284a6f4416b06a29` |
| nomic-embed-text/latest | F16 | 274290656 | `970aa74c0a90ef7482477cf803618e776e173c007bf957f635f1015bfcfef0e6` |
| qwen2.5-coder/1.5b-base | Q4_K_M | 986048512 | `6a77366395772462c84f0c4d226ac404674327cbe78c01e4391cc7e0c698851e` |
| qwen2.5-coder/14b | Q4_K_M | 8988110784 | `ac9bc7a69dab38da1c790838955f1293420b55ab555ef6b4615efa1c1507b1ed` |
| qwen3.5/latest | Q4_K_M | 6594462816 | `dec52a44569a2a25341c4e4d3fee25846eed4f6f0b936278e3a3c900bb99d37c` |

Prioritize native SDK validation first. For inference, inspect the existing
qwen3.5/latest artifact's exact architecture/template and validate its blob before
selecting it; do not describe it as the same 2B model. The coder/14b tag is another
candidate for a separate coding-answer arm after equivalent checks, not an assumed
tool-use winner. Embedding and base-model tags are not interchangeable with a chat
agent. Choose the first trial only after backend compatibility and measured memory
headroom are established. Retain llama.cpp for the closest host comparison if a
compatible build is available; an Ollama trial would change the serving stack and
must be labeled separately. No installation or server start is included here.

## Workload placement

| Job | Recommendation | Reason / evidence still needed |
| --- | --- | --- |
| Harness, manifests, hashes, offline tests and scoring aggregation | Keep on BigDog; portable to Max Mini | Existing lane works. Moving orchestration offers no demonstrated quality benefit. [E1] |
| Same 2B model, same prompts and tool protocol | Comparative host trial only | Hardware can change latency/capacity and numerical output; it does not establish better reasoning or repair the observed lookup failure. [E1,E4] |
| Larger local model with stronger retrieval behavior | Candidate Max Mini role, conditional | Manifest inventory received; blob verification, serving compatibility, memory headroom and independent quality results remain required. [E5,E6] |
| Swift compilation, SDK availability checks, simulator/accessibility checks | Prefer an appropriately equipped Apple worker | Linux inference cannot substitute for Apple SDK/runtime evidence. Xcode/macOS SDK are peer-reported; simulator/device access and task-specific checks remain pending. [E5] Physical-device behavior remains a separate gate. |
| Independent answer grading | Peer review useful; retain source-backed rubric | Ask for citations to returned reference contents, factual errors and unsupported claims. Another model's agreement or confidence is not ground truth. |
| Sustained/background batches | Choose after measuring load and memory | No verified Max Mini capacity or concurrency baseline. Start serial; avoid swapping or competing with native test work. |

The most plausible quality improvement is a better model or better evidence
supply, not relocation alone. Deterministic reference selection followed by local
summarization is worth grading because C2 already supplies evidence reliably; it
still has no demonstrated answer-quality advantage. Do not label it successful
retrieval or use it to conceal C3 failures. [E1,E2]

## Proposed verification sequence (not execution authorization)

1. Inventory reports are received [E5,E6]. Next verify selected model blob bytes,
   exact architecture/template, backend availability and current memory/workload
   headroom. Pin the chosen runtime and confirm native SDK/simulator scope. Do not
   request credentials, full profiles or raw system dumps. No resources are reserved.
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

Both peer reports corroborate the conditional recommendation and explicitly state
that no LLM was loaded, server started or throughput/quality benchmark performed.
The original direct Max Mini notification remains unread, while the replies arrived
through NUIAK; direct-message status must not be used to infer absence of a reply.
The existing NUIAK route was used to acknowledge both reports. This is an observed
reply route, not authority to merge identities or change enrollment.

The next decision is a finite, explicitly scoped native-validation or local-model
trial with a named runtime/model and budget. No installation, paid provider call,
generated Swift execution or benchmark is authorized by this document. Max Mini is
a better-supported candidate for complementary Apple validation and larger-model
experiments, but remains unproven as a faster or more accurate inference replacement.
