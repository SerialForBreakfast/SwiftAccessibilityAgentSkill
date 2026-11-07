# Swift Accessibility Agent 0.3.0-rc.1

One independently installable research candidate and one offline grader. The default GitHub install still installs 0.2.2. The RC is a standalone archive, **not** another discoverable SKILL.md in the repository tree. It has no installed Python router, controller material or research-checkout dependency. Its supported development scope is iOS, macOS and tvOS.

## Try the candidate in an empty project

Extract [the RC archive](swift-accessibility-agent-0.3.0-rc.1.zip) outside the project you want to install into. From that project's root, use the normal skills installer with the **local extracted folder** as its source:

```sh
npx skills add /absolute/path/to/swift-accessibility-agent --skill swift-accessibility-agent
```

Select your agent as usual. Use a separate test project without an existing same-name skill: installing over a project's released copy would replace it. The original repository and global installation do not need to be modified. For a manual project-local Codex install, place the extracted folder at `.agents/skills/swift-accessibility-agent/`. Inspect the installed SKILL.md for version 0.3.0-rc.1. Installation/discovery on disk is not proof that a new chat will invoke the skill.

Rebuild the archive reproducibly with `python3 -B evals/rc1/package/build.py <output.zip>`. The packager flattens selected dev.5-8 notes and target-specific SDK excerpts, verifies the source hashes of six companion examples and rejects broken internal Markdown links. Examples are opt-in and separate from hidden grading assertions.

## Qualify the grader

From the repository root on Apple silicon with Python 3.10+, Xcode, the iOS/tvOS 26.5 simulator runtimes/devices and the macOS SDK:

```sh
python3 -B evals/rc1/grader/qualify.py
```

The launcher boots an installed unit simulator if necessary, runs sequentially and shuts down only devices it started. It never creates devices, downloads runtimes, starts models or performs UI automation. The direct `grade.py` entry point uses already-booted devices. The host macOS lane runs on the actual host version. All lanes target OS 26.0. Fresh scorecards, submitted bytes, hidden harnesses and diagnostics are stored under ignored `evals/results/rc1-grader/`; the SDK module cache can be reused.

The grader passes a case only when the Swift file compiles and the hidden unit executable signals success. A deliberate mutant must compile and hit the expected contract failure (exit 42 and task-specific marker); a build error, timeout, missing SDK/device, or process crash does not count. Inspect the first attempt rather than repairing a submitted file. Infrastructure errors stop dependent execution; completed observations remain intact.

### Subject and controller boundary

`python3 -B evals/rc1/grader/grade.py --export checkout-font` emits just a natural request and its starter file. Export before handing a task to a subject; do **not** expose this repo, grader, fixtures, oracle, results or source package to the subject. Each task takes a single Swift implementation with a stable signature, not a generated project. No subject-controlled build phases, dependencies or shell commands. Submit unchanged Swift bytes; an answer that needs prose or partitioning must be handled separately, not silently repaired.

The ordinary developer-host command runs **only maintained fixtures**. For a future authorized external submission, provision a disposable macOS VM, no credentials, no mounted host repo or shared directories, no network adapter, throwaway checkout and user, with trusted toolchain/runtimes pre-installed. Transfer a single sanitized file and runner before isolation, and retrieve results after shutdown. Only there use `RC1_ISOLATED_WORKER=1 python3 -B evals/rc1/grader/grade.py --task TASK --submission Submission.swift`. VM detection and an operator flag are interlocks, not proof the VM was provisioned safely. If the platform lane cannot run securely in that environment, leave it ungraded. No external-submission worker or model transport is qualified by this fixture run.

See [the controller rubric](RUBRIC.md) for the 12 development cases and evidence boundaries. These cases grade specific contracts, not complete apps, platform usability or universal accessibility. Do not use their 36 executions as independent model answers or as a noise-floor estimate.

## Audit and provenance

Owner's implementation request: "Lets adopt this. Lift the SwiftUI deferral for iOS, macOS and tvOS. Build one installable 0.3.0-rc.1 and the 12-task offline grader in one tranche. Accept valid alternatives and reject the mutants. No model runs, spend or changes to 0.2.2."

The packaged body is newly consolidated; the file selection and checked source hashes are reproducible from package/build.py. The subject prompt text and starter export, original reference/alternative/mutant bodies and independent controller assertions are retained in grader/tasks.py and grade.py. These are authored test fixtures, not historical model answers. The complete authoring/tool conversation is not exported. First and final native build inputs, outputs and diagnostics remain in distinct local attempts. The first fully passing run exposed a simulator linker-driver sysroot warning; the final driver explicitly selects the SDK and SDKROOT. No grading assertion was weakened.

Verify the distributed bytes and the fixture results without rerunning Xcode: `python3 -B evals/rc1/verify.py`. The checked-in [scorecard](scorecard.json) records the measured environment, input hashes and individual outcomes. Verify a local installation by also passing `--installed /path/to/installed/swift-accessibility-agent`.
