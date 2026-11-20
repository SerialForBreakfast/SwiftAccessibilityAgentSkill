# Swift Accessibility Agent 0.3.0-rc.4

[Candidate archive](swift-accessibility-agent-0.3.0-rc.4.zip) · [Reproducible builder](build.py)

Based on rc.3, this candidate replaces two lines of its proof checklist. It asks for the first assertion that distinguishes working and broken behavior, the observed values on the actual owner, and both stale and current dispatch or pre- and post-completion checks when relevant.

| Evidence on Gemini Flash Low | Unaided | With isolated assertion instruction |
|---|---:|---:|
| Selected repair cases with previously failing tests | 0/23 | 5/23 |
| Sample of passing test controls | 12/12 | 12/12 |

One production-code component regressed in that earlier experiment. The installed rc.3 and rc.4 each passed 8/20 tests on the targeted Flash Low panel (3/14 prior failures and 5/6 passing controls). One control improved and one regressed. One test per candidate remained unresolved. The discovery audit independently identified 14 defective checks in 75 test-design answers. The local Swift callback test caught both an obsolete delivery and a silently disabled current action.

Build with `python3 evals/rc4/build.py`. Verified SHA-256: `825518da86c7463b176758b6fe1d8045de5ce924383f3d9ae149307f41728e20`.
