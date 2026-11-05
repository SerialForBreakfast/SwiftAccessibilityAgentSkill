# Second-pass source ledger

Retrieved and reviewed 2026-11-05. Tier-1 sources. Public HTTPS responses fetched with curl; Support HTML text and API JSON metadata reviewed. Hashes cover raw response bytes including navigation, not permanent source revisions. Originals remain in temporary research storage.

## P2-linked

- [Source](https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitylinkedgroup(id:in:).json)
- Reviewed scope: API-01; metadata.platforms
- Bytes: 14610
- SHA-256: `4f557d24424150d8af909db4c724ca63c9fbb6b8d329c11315396fc5f5be9b8d`

## P2-tabs

- [Source](https://developer.apple.com/tutorials/data/documentation/swiftui/tabspickerstyle.json)
- Reviewed scope: API-02; metadata.platforms
- Bytes: 14763
- SHA-256: `92399423903a4bbe26198b50475b50a75d804f71b3f8f774dc0ecc4482cad0a6`

## P2-edit

- [Source](https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/editcategory.json)
- Reviewed scope: API-03; metadata.platforms
- Bytes: 8753
- SHA-256: `dd36fca5f6128d797a83feff4e6515d1b6ee3397262c2e017c47171ad2c2d642`

## P2-textManager

- [Source](https://developer.apple.com/tutorials/data/documentation/appkit/nstextselectionmanager.json)
- Reviewed scope: API-04; metadata.platforms
- Bytes: 32502
- SHA-256: `85ce1cbe6f9df21d9b8a789d97812b33bcb25d0bc604f9f3ce636dcd71bfcccb`

## P2-toolbar

- [Source](https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbaritemgroup/role-swift.property.json)
- Reviewed scope: API-05; metadata.platforms; mobile entries require interpretation
- Bytes: 14894
- SHA-256: `f940cac6da88cd216acd83c6da6113866f6d5ab2d300db111df8c892c0bcd50f`

## P2-watch

- [Source](https://support.apple.com/en-us/guide/watch/apdb93ea3872/27/watchos/27)
- Reviewed scope: watchOS 27; Convenience and productivity; Sound Recognition
- Bytes: 759903
- SHA-256: `1352ec10f3901a9b6c5d884e15f8a38ecfb7ee8c5e7e7def3c4bb2fec6714caf`

## P2-watchSound

- [Source](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/27/watchos/27)
- Reviewed scope: SHIP-05; introduction, warning, setup
- Bytes: 743880
- SHA-256: `57215b0ee72082b2f05c5ded54cc6a5549e26b9afcc35ec057fe3ee7313433eb`

## P2-vision

- [Source](https://support.apple.com/en-us/149067)
- Reviewed scope: SHIP-03/04; visionOS 27 Accessibility and 27.2 Other
- Bytes: 165908
- SHA-256: `2b0b25605c7e9a3e6ebb751d6ca4b879b6bec5f274b11013ad06cb2b3f8c59de`

## P2-iphoneCaptions

- [Source](https://support.apple.com/en-us/guide/iphone/iph3e2e23d1/27/ios/27)
- Reviewed scope: SHIP-01; introductory availability note
- Bytes: 1458927
- SHA-256: `1ecbe21b78d90fc03202566aab97fd8abf6fa4fcaa12e662212df96481a174fc`

## P2-macCaptions

- [Source](https://support.apple.com/en-us/guide/mac-help/mchlc1cb8d54/27/mac/27)
- Reviewed scope: SHIP-02; introductory availability note
- Bytes: 715073
- SHA-256: `3ef07a48dec201620c2561f2071fe7adbe6074c839e793a31304dbfc25f3289f`

## P2-managed

- [Source](https://support.apple.com/en-us/guide/deployment/depdc9488053/web)
- Reviewed scope: SHIP-06; minimum versions, supervision, enrollment, Vision settings
- Bytes: 823626
- SHA-256: `4aafb08ebe7258c335cdcc08b2d897ef812015a4ecac2bf0743281ab953504db`

## Retrieval reconciliation

The web reader returned 429/cache errors for several Support pages; direct public HTML retrieval succeeded and the relevant passages were reviewed. Initial inferred edit-category and toolbar-role URLs returned 404. These were resolved using Apple search results and parent-symbol references to the exact URLs recorded above. No unavailable response was treated as reviewed evidence.
