# Proof repair: 20 previously non-discriminating XCTest cases

These are development questions about writing a useful accessibility regression test, not modifying production code. The original private packet (coordinator request 1544) supplied a weak test, working sources and one deliberate defect per case. Earlier execution: all 20 tests passed on *both* source variants. These questions reuse those fixtures and existing repository assertion patterns; they are neither hidden transfer cases nor recorded model failures.

## Use the questions

Each row in [cases.tsv](cases.tsv) has a developer question. Give the subject only its materialized `subject/` directory (QUESTION.md, working production files and the original weak XCTest). Withhold variants, assertion names, qualifying tests, rubrics, scores and run artifacts. No production edits or UI testing. Grade an answer by running the **same submitted test** in all three compatible projects. Preserve submissions unchanged; a compile or setup error is not a caught defect. Do not require our test name, setup sequence or assertion wording when adapting the runner to a submitted answer.

Controller: [witnesses.tsv](witnesses.tsv) lists the observable for each prompt; [alternatives.py](alternatives.py) provides the second production implementation. Evaluate the accessibility decision, working and alternative compatibility, and detection of this specific defect separately. A test may compile but exercise the wrong path. A test that rejects a valid alternative overspecifies the implementation. A skip, missing fixture, setup crash, private API inspection or assertion about source spelling is not an accepted behavioral proof. No claim about delivered speech, focus or user interaction follows from configured properties or callback requests.

## Reproduce locally

Use a new directory under the ignored `evals/results/`; preparation and execution refuse to overwrite attempts. From the project root:

```sh
python3 -B evals/proof-repair-20/prepare.py "$PRIVATE_PACKET" evals/results/proof-repair-new
python3 -B evals/proof-repair-20/run.py evals/results/proof-repair-new
python3 -B evals/proof-repair-20/report.py evals/results/proof-repair-new
```

Preparation verifies the original archive checksum; only the target production file varies. The revised proof keeps the weak assertions and adds a focused test body from the matching example, reusing the starter's existing helpers. See the per-case assertion source and method in the evidence. Matching a familiar test is not enough: the qualifying run must execute the assertion against all three builds and locate the expected failure in the submitted test itself. Where the observable is a single Boolean, different implementations may be simple equivalents; this demonstrates compatibility with **one** alternative, not every possible one.

## Provenance and boundaries

Author request: “Lets turn all 20 weak tests into proof-repair questions in one offline batch. Verify each revised test passes the working code and a valid alternative, then fails the supplied defect for the right reason. No model runs or skill changes.” Generated subject files contain the complete prompts and starter inputs. No evaluation prompts were dispatched, no candidate answers exist, and no independent gold review is claimed. The first preparation stopped on Q027 because a source expression matched both header and ordinary-cell lookup. Restricting the substitution to the ordinary lookup corrected the *fixture generator*, not the test or the platform code. Original attempted preparations and all first native logs remain private in evals/results/.

### Callback fixture repair

Q024 initially rejected both valid implementations. The old check and the new check shared the XCTest instance's reply array: firing index zero completed the preceding owner's request and left the intended owner busy. All three first results, logs and source snapshots are preserved under the original attempt. Clearing the capture array **between setups**, not bypassing the triggering edit, produced the final three-way result: both valid owners clear busy without accepting stale input; the supplied defect calls accept once rather than zero. This was an oracle defect, not an accessibility failure.

For this batch, the original private directory is `evals/results/proof-repair-1544-v2`, and the Q024-only repair is `evals/results/proof-repair-1544-repair1`. Pass the repair directory as the second argument to report.py to verify the final outcomes. Use subject_packet.py on a prepared directory to build the private subject-only ZIP without controller material. The Q024 correction did not change any subject bytes.
