# Shipping and deployment constraints

Second pass, 2026-11-05. Tier-1 Support pages were retrieved directly and their
relevant sections reviewed. See [retrieval fingerprints](pass-2-sources.md).
These records refine announcement-level claims; they do not replace the entire
release/build reconciliation still in the research backlog.

| ID | Feature and supported constraint | Source section | Research effect |
| --- | --- | --- | --- |
| SHIP-01 | Generated subtitles/multiple subtitle languages require iOS 27 and iPhone 15 Pro/Pro Max or iPhone 16 models and later. Generated subtitles are listed for English US/Canada when absent from content. | [iPhone subtitles guide](https://support.apple.com/en-us/guide/iphone/iph3e2e23d1/27/ios/27), introductory note | OS version alone is insufficient. Keep generated subtitles distinct from authored captions/SDH. |
| SHIP-02 | Mac generated subtitles/multiple subtitle languages require macOS 27 and M1 or later; the guide specifies English US/Canada for generated subtitles. | [Mac captions guide](https://support.apple.com/en-us/guide/mac-help/mchlc1cb8d54/27/mac/27), introductory note | Do not extend this feature to every Mac that runs the OS. |
| SHIP-03 | visionOS 27 includes Look to Drive with compatible wheelchair accessories and Dwell Control confirmation using an eye-directed selection marker. | [visionOS updates](https://support.apple.com/en-us/149067), visionOS 27 / Accessibility | Promotes these two aspects of ANN-04 from announcement to shipping-documentation evidence; exact accessory compatibility remains separate. |
| SHIP-04 | visionOS 27.2 supports adding a third-party sign-language interpreter or live captioner to FaceTime. | [visionOS updates](https://support.apple.com/en-us/149067), visionOS 27.2 / Other | Shipping system feature; developer API name and entitlements still need documentation. |
| SHIP-05 | Watch Sound Recognition is documented for Series 12 and Ultra 4. Setup uses the paired iPhone and may require a sound download. | [Watch Sound Recognition](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/27/watchos/27), introduction and setup | Hardware-dependent feature. Apple cautions against relying on it for emergencies, high-risk situations or navigation. |
| SHIP-06 | A managed Accessibility configuration controls Live Recognition on supervised iOS/iPadOS/macOS/visionOS 27 devices using Automated Device Enrollment. | [Deployment guide](https://support.apple.com/en-us/guide/deployment/depdc9488053/web), configuration requirements and Vision settings | Managed-device policy can limit feature access independently of app semantics and OS version. |

## User-task implications (research inference)

Ask which device, OS, language, account/management policy and media content the person
uses before promising an AI-assisted accessibility feature. Preserve a usable ordinary
interaction when an optional generated or hardware-dependent feature is unavailable.
System interpretation of content does not remove the app's responsibility for labels,
independent actions, text structure and authored media alternatives.

## Remaining checks

Retrieve iPad, Apple TV and Vision Pro media hardware/language tables before applying
SHIP-01/02 constraints to those devices. Apple's Music-app “Larger Text” lyrics setting
is a different feature from tvOS-wide Larger Text: a search match is not corroboration.
ANN-04 motion cues and face gestures still need their specific shipping-guide review.
