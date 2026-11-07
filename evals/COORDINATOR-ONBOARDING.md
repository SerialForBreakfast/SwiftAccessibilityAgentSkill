# Coordinator enrollment checkpoint

Updated 2026-11-05 against owner-supplied TVTestRig handoff revision 2.
Status: activated; direct mutual-TLS messaging verified and accepted by BigDog.
No native fixture, model or device execution occurred.

## Activation and live verification

Authenticated activation notice: `bigdog-swift-enrollment-activated-20261105-r1`,
TTR cursor1934. Public packet SHA-256:
`4106e7b67880d0b7f4b9c7d98f7e8cb0ef66d9fd1dc75fefa55c98151600eb78`.
All seven member hashes checked; certificate chain/client purpose, fingerprint
and match to the existing private key passed. Private configuration stays in the
approved non-synced application-support directory, not this repository.

- Principal: `sillycon-swift-accessibility-agent-skill`.
- Protocol/project: `project-dev-1` / `swift-accessibility-agent-skill`.
- Certificate expires December 5, 2026 at 14:09:53 America/Los_Angeles.
- Revocation/renewal contact: BigDog-Coordinator; no automatic renewal.
- Capabilities confirm exactly five project messaging methods; `execution:false`.
- Hello `swift-accessibility-enrollment-hello-20261105-r1`: stored cursor1385,
  message `622e8d99-b55b-4c5d-a182-07907ad51c9f`; fresh-process status reconciled.
- Welcome message `b71e8ebe-5150-48b9-9fb6-a9cb903db38a`: inspected then exact
  `project.read` returned `state:read`, `work_accepted:false`.
- BigDog acceptance `bigdog-swift-enrollment-confirmed-20261105-r1`, cursor1387,
  message `bcfe19c5-22a9-43de-af35-32802aaa2c79`: inspected and exact read verified.
  Its text explicitly accepts enrollment and acknowledges the original hello.
- Private `receipts/` retains immutable request/response bytes. Read acknowledgments
  are recorded separately; storage is not inferred to mean task acceptance.
- Private `qualification.json` records direct messaging verification, exact read
  acknowledgments and receipt hashes. TTR reports replying to the routed hello;
  its forwarded reply did not arrive during the additional ten-minute bounded
  read-only check. Peer roundtrip remains pending, separately from completed
  activation/direct messaging. No polling or background service remains running.

The following sections preserve setup history; earlier pending states are historical.

## Provisioning progress

BigDog's authenticated reply `bigdog-swift-two-step-setup-20261105-r1` (cursor
1922, relayed by TTR) selects the dedicated BigDogCoordinator application-support
location and supersedes the earlier proposed path. The owner-authorized setup
script SHA-256 is `038392b6997b51968c77f3588c82d77b1f701870778bfdea602319460d87a60a`.
Reviewed script executed successfully: RSA3072 key retained locally, SHA256 CSR
self-signature and key match verified, directory0700/key0600. No private key sent.
Public return files were submitted to TTR for approved share publication/issuance:

- CSR: 1281 bytes, SHA-256 `896ce902434b451976cd6d177d6881acb9daa9fe6fe092f53ac679dab871b363`.
- Enrollment metadata: 866 bytes, SHA-256 `487a42f2a5eabb2657ffd6fa044fa45a3fbdbda2abae0bb3823fcc6581b10975`.

TTR independently verified and published only those public files, then notified
BigDog with `ttr-swift-csr-ready-20261105-r1`, stored at cursor **1926** and queued
as `review-2e7689aea21f5af82db06bd0`. A single five-minute deterministic issuance
wait completed with 12 list checks, no errors and cursor unchanged at1928. Result:
`issuance_pending`. No certificate/activation packet arrived; direct messaging
verification cannot run yet. BigDog owns the remaining issuance step. Existing key
and CSR are retained; no resend, regeneration or background monitoring is active.
TTR evidence: `.local-work/swift-accessibility-enrollment-20261105/issuance-wait/result.json`.

The following worksheet history records earlier states; the latest status above
takes precedence. No provider/device authorization accompanies this enrollment.

## Verified locally

- Public packet located in TVTestRig's `Docs/Coordination/SwiftAccessibilityAgentSkill/setup-r1/`.
- All seven file hashes match `SHA256SUMS.json`.
- Reviewed standard-library Python client as text; not executed.
- Client SHA-256: `c82d839418cda0d80ffea65ac8fbb07504d42928ec2ccf215a918b526342e1c1`.
- Python 3 is available. Repository is cloud-synchronized; credentials must live elsewhere.
- HOME and Application Support resolve outside Dropbox, but complete backup/sync
  policy is not established. No credential directory has been created or approved.

The supplied contract is `project-dev-1`, NOT the older TTR `message.*` relay.
Proposed project: `swift-accessibility-agent-skill`; operation prefix:
`swift-accessibility-`; recipient: `bigdog-coordinator`. Proposed methods:
`project.capabilities`, `project.send`, `project.status`, `project.list`, `project.read`.
These are proposals until the dedicated principal is activated. Private endpoint
and host-binding details remain in the owner handoff, not this public guide.

## Current blocker and next action

The initial worksheet transmission was rejected for host/account/path metadata.
The owner subsequently explicitly approved sharing those fields with the TTR thread
"Brainstorm TTR developer features" for relay to BigDog. The approved worksheet
was delivered to that thread; this is not yet a coordinator storage or activation
receipt. No keys, tokens or active profiles were sent. The server certificate passes
the offline CA-chain check and its IP SAN matches the supplied endpoint.

TTR subsequently reported coordinator storage for
`ttr-swift-accessibility-host-binding-20261105-r1` at cursor **1919**. The request is
queued for coordinator-agent review. This is a relay-reported storage receipt, not
activation; the consolidated provisioning response has not arrived. No further
owner confirmation was requested and fixture work remains excluded.

TTR was asked to relay the worksheet using existing enrollment lineage
`ttr-swift-accessibility-enrollment-20261105-r1`. BigDog returns the concrete
host-bound CSR plan and location approval. The owner requested two consolidated
phases: binding/plan, then provisioning/activation/verification, without repetitive
approval loops. Execute the approved plan within filesystem permissions; report
concrete blockers rather than inventing activation. Keep private material outside Git and sync folders.
Do not borrow TTR credentials or install a service.

## Qualification after activation

1. Verify trust-file hashes, certificate validity, chain and server IP SAN against
   the authenticated packet. The client validates CA/hostname but does not implement
   an independent server-fingerprint pin or persist intents itself.
2. Confirm activation, exact identity/recipient/methods and response schemas.
3. Bound the check to 15 minutes, 12 RPC calls and 5 MiB sanitized evidence.
4. Persist exact hello bytes/hash and operation ID before sending once. Retain
   output/error separately; reconcile uncertain delivery by original operation ID.
5. Use capabilities epoch for bounded listing; read only actual inspected message
   IDs. Do not apply legacy `message.ack` expectations to `project.read`.
6. Verify coordinator reply and a coordinator-forwarded TTR round-trip. Reopen the
   client and reconcile original state without resending or automatic retries.
7. Report storage, read, forwarding and explicit acceptance separately. Missing
   responses remain pending. Messaging never grants provider/device execution.

## Existing fixture request

Preserve `bigdog-sillycon-swift-os26-fixtures-20261105-v1` without duplicate dispatch.
The local project has inspected the referenced fixtures. Owner now confirms unit
and compile tests only, no mandatory manual verification or UI tests. Promotion
revision `os26-code-contract-3` reflects that scope. Actual Apple execution remains
unrun and gold promotion remains blocked on evidence. Do not relabel OS27 runs OS26.
