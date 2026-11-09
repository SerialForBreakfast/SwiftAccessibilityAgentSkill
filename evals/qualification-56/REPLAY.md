# Grading packet at a glance

| Platform | Questions | Runnable starters | Native decision qualified | Source contrast | Open oracle | First answers |
|---|---:|---:|---:|---:|---:|---:|
| iOS | 26 | 23 | 21 | 5 | 0 | 52 |
| macOS | 14 | 12 | 12 | 2 | 0 | 28 |
| tvOS | 16 | 14 | 14 | 2 | 0 | 32 |
| Total | 56 | 49 | 47 | 9 | 0 | 112 |

Native decision = two implementations accepted and one intended defect caught on the recorded platform. One probe can serve two questions. Source contrast = two acceptable answers and a rejected counterexample, assessed against the written criterion, not by XCTest. Neither column certifies every secondary criterion.

| First host result | Original contract | Submitted proof |
|---|---:|---:|
| ambiguous-partial-patch | 3 | 3 |
| blocked-by-identical-subject | 0 | 6 |
| compile-only | 37 | 0 |
| no-executable-proof | 0 | 22 |
| no-tests-discovered | 0 | 1 |
| offline-build-only | 5 | 7 |
| source-only | 7 | 7 |
| subject-compile-failure | 11 | 0 |
| test-compile-failure | 4 | 10 |
| unit-failure | 9 | 6 |
| unit-pass | 36 | 50 |

| Question | Platform | Grading control | v2 contract / proof | v4 contract / proof |
|---|---|---|---|---|
| P-7d8c12fe30bd49a4 | iOS | native decision | test-compile-failure / unit-pass | unit-pass / unit-pass |
| P-d76c1ea3d7c9a580 | tvOS | native decision | offline-build-only / unit-failure | offline-build-only / test-compile-failure |
| P-0a2cd6519778f4c7 | tvOS | native decision | test-compile-failure / unit-pass | test-compile-failure / unit-pass |
| P-f28c1ae4058d31a8 | macOS | native decision | offline-build-only / test-compile-failure | offline-build-only / test-compile-failure |
| P-1079cff7faaab5b2 | iOS | native decision | compile-only / unit-pass | compile-only / unit-pass |
| P-7622f1aa06d7a35b | iOS | native decision | unit-failure / unit-pass | unit-pass / test-compile-failure |
| P-48400f490808a2cf | macOS | native decision | unit-pass / test-compile-failure | unit-pass / unit-pass |
| P-f93bec690ad5409c | iOS | source contrast | compile-only / no-executable-proof | compile-only / no-executable-proof |
| P-2865458d46b0d1a4 | iOS | native decision | subject-compile-failure / no-executable-proof | subject-compile-failure / no-executable-proof |
| P-7d27aad438a1d70b | macOS | native decision | unit-pass / unit-pass | unit-failure / unit-pass |
| P-db6ab4c551e67aca | iOS | native decision | unit-failure / unit-pass | unit-failure / unit-pass |
| P-f6c77faf11d5ad05 | macOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-34541ce79ee3d519 | iOS | native decision | compile-only / unit-failure | compile-only / unit-pass |
| P-35ee522327907bd8 | iOS | source contrast | compile-only / no-executable-proof | compile-only / no-executable-proof |
| P-db32e60bc16c19a8 | iOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-51e9f52794c2efdf | iOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-10464d860f6802b2 | tvOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-3f811eea610d0c32 | macOS | native decision | compile-only / no-executable-proof | subject-compile-failure / no-executable-proof |
| P-a5c8091cdffa651a | iOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-852a6aafb1bd0b6f | tvOS | native decision | unit-pass / unit-pass | unit-pass / no-tests-discovered |
| P-777d08cb675db900 | macOS | native decision | unit-pass / test-compile-failure | unit-pass / unit-failure |
| P-4ec92962591872fa | iOS | native decision | compile-only / unit-pass | compile-only / unit-pass |
| P-4328fa34debd8d92 | tvOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-7766a23217bfa0c3 | tvOS | native decision | unit-pass / unit-pass | ambiguous-partial-patch / ambiguous-partial-patch |
| P-4099aaf89ec377cf | tvOS | native decision | unit-failure / unit-pass | ambiguous-partial-patch / ambiguous-partial-patch |
| P-5d121776613655db | tvOS | native decision | compile-only / unit-pass | compile-only / test-compile-failure |
| P-9c455b0bd4be71db | iOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-a12bcd8ed20f1256 | tvOS | native decision | unit-pass / unit-pass | unit-pass / test-compile-failure |
| P-6bfef2bcad970d58 | macOS | source contrast | source-only / source-only | compile-only / no-executable-proof |
| P-6d2dd61c5ac4abfc | iOS | native decision | compile-only / unit-pass | compile-only / test-compile-failure |
| P-da7833399aac7f87 | macOS | native decision | unit-pass / unit-pass | test-compile-failure / unit-pass |
| P-7cc5d89371a12a35 | tvOS | native decision | subject-compile-failure / blocked-by-identical-subject | offline-build-only / test-compile-failure |
| P-a00ec36c978640fc | tvOS | native decision | subject-compile-failure / blocked-by-identical-subject | unit-pass / unit-pass |
| P-90629dd9d60ff906 | iOS | native decision | subject-compile-failure / blocked-by-identical-subject | compile-only / unit-pass |
| P-76d9fe6a4d351668 | macOS | native decision | unit-pass / no-executable-proof | unit-pass / unit-failure |
| P-89b1442c72a8db4b | iOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-a32f106f0aa1cc85 | iOS | source contrast | compile-only / no-executable-proof | compile-only / no-executable-proof |
| P-b12c69f62639d32d | iOS | source contrast | subject-compile-failure / no-executable-proof | compile-only / no-executable-proof |
| P-be25d510c5ffe50f | macOS | native decision | unit-failure / unit-pass | unit-failure / unit-pass |
| P-c04cc5d4aa6f82d2 | iOS | native decision | compile-only / offline-build-only | compile-only / offline-build-only |
| P-c55650380597efd4 | tvOS | source contrast | source-only / source-only | source-only / source-only |
| P-c6b25ad753e6a2d2 | tvOS | native decision | compile-only / offline-build-only | compile-only / offline-build-only |
| P-d4bd274c3a345669 | iOS | native decision | subject-compile-failure / blocked-by-identical-subject | subject-compile-failure / blocked-by-identical-subject |
| P-d82c5ccce8e33f3e | macOS | source contrast | source-only / source-only | source-only / source-only |
| P-9ae50d3a7e4bb9e8 | iOS | native decision | unit-failure / unit-pass | subject-compile-failure / blocked-by-identical-subject |
| P-d2dd979143402b3b | iOS | native decision | unit-failure / unit-failure | ambiguous-partial-patch / ambiguous-partial-patch |
| P-dc1e54ce99c97729 | tvOS | native decision | compile-only / offline-build-only | compile-only / unit-pass |
| P-dd7ee77a4e81a08e | macOS | native decision | compile-only / unit-pass | compile-only / unit-pass |
| P-ddf8bad3cbd8d087 | iOS | source contrast | compile-only / no-executable-proof | compile-only / no-executable-proof |
| P-debf8047cd9f4e4a | iOS | native decision | compile-only / no-executable-proof | compile-only / no-executable-proof |
| P-b43542c4e476c154 | macOS | native decision | unit-pass / unit-failure | unit-pass / unit-pass |
| P-e505d95d8bc6f761 | iOS | native decision | subject-compile-failure / no-executable-proof | compile-only / no-executable-proof |
| P-e56a902ef372a290 | tvOS | source contrast | source-only / source-only | source-only / source-only |
| P-7b8cff8f7531bd8f | tvOS | native decision | unit-pass / unit-pass | unit-pass / unit-pass |
| P-f48375292f98ee5c | macOS | native decision | compile-only / offline-build-only | compile-only / offline-build-only |
| P-f776360cf78dd3e2 | iOS | native decision | compile-only / no-executable-proof | compile-only / no-executable-proof |
