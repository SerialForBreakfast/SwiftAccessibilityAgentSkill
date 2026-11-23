# signal-v7-2-qualify1 return 1

Status: **complete**.

The owner approved this job in chat on 2026-11-22 ("You can do that here"). The Mac ran it once, with 1 batch.

## Revision and seal

- Checkout: `420a5d4a73f47532dfa1b78beee2cbf484d71e89` (detached).
- `build.py --check` printed `f2b89677ba1039f535cc6ad3e1015a5645f9b82963fc8d2a8162384f787408c3 2858 31111`. This matches the expected seal.

## Step 1: static check

`qualify.py --static` exited with 0. All 9 compared items print "identical to v7.1". The output also prints the `ApiProbe` source first, as the script does. See [static.txt](static.txt).

## Step 2: native qualification

Result: **PASS**. All 15 runs are OK:
- macOS: 4 (fixed, media, dismissal, observer).
- iOS: 6 (fixed, callbacks, media, dismissal, late, observer).
- tvOS: 5 (fixed, callbacks, dismissal, late, observer).

On macOS, `testAppKitRowGetters` passed.

| Batch | Counts | Notes |
|---|---|---|
| `qualify-93hl0_in` | yes | The only batch. No harness error. No retry. |

Files:
- [qualify-93hl0_in/receipt.json](qualify-93hl0_in/receipt.json) is a byte copy of the receipt, with no changes.
- [logs.tar.gz](logs.tar.gz) holds all 15 `native.log` files at their original relative paths. It is 123 KB, so no log was cut.

**Log change:** the logs contained the Mac's home path. In the archived copies, the home folder is replaced with `$HOME` and the account name with `USER`. Nothing else changed. The original logs on the Mac are unchanged. The tar entries have owner `root:wheel`.

## Step 3: sheet(item:) source check

Claim: "With `sheet(item:)`, the item is already `nil` when `onDismiss` runs."

| Source | Result |
|---|---|
| macOS SDK 27.0, SwiftUI | **SILENT** |
| iOS SDK 27.0, SwiftUI | **SILENT** |
| tvOS SDK 27.0, SwiftUI | **SILENT** |
| Xcode offline documentation | not found |

- The SwiftUI `.swiftinterface` files of all 3 SDKs contain no `///` doc comments.
- The comments are in the `.swiftdoc` files. `xcrun swift-symbolgraph-extract` (part of Xcode) read them. The 3 SDKs have the same comment (sha256 `76be8b25…`).
- The comment says only that `onDismiss` is "The closure to execute when dismissing the sheet." It does not give the value of `item` when `onDismiss` runs.
- No hosted test or UI test was written.

See [sdk-sheet-item.txt](sdk-sheet-item.txt) for the verbatim comment and the file paths.

## Environment

- Xcode 27.0, build 27A266a. The SDKs are macOS 27.0, iOS 27.0 and tvOS 27.0.
- macOS 27.0.1, build 26A434, Apple silicon.
- Simulators:

| Name | Device ID | Device type | Runtime |
|---|---|---|---|
| SwiftAccessibility-OS26-Unit-iOS | `D4587FA1-721C-4F60-8BAF-D7926600AFCD` | iPhone 17 | iOS 26.5 (23F77) |
| SwiftAccessibility-OS26-Unit-tvOS | `8867CB2B-1669-416E-B22F-57A6C98FF060` | Apple TV 4K (3rd generation) | tvOS 26.5 (23L470) |

## Differences from the v7.1 environment

- This Mac had no simulators with the 2 required names. The agent made them with `simctl create` from runtimes that were already installed, then booted them. Nothing was installed or downloaded.
- The SDKs are version 27.0. If v7.1 used the 26 SDKs, this batch is not the same toolchain as `qualify-zpbur0f2`.

## Not done

- Nothing from the brief is left.
- The return does not include `evals/results/`.
