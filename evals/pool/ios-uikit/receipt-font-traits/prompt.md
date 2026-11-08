iOS 26.0, UIKit.

In our "Preview text size" sheet the receipt descriptions never get bigger when a customer picks a larger size, and long descriptions are cut off with "…". The descriptions should keep our brand font, sized like body text, and the wording must stay as it is. Can you fix `makeDescriptionLabel(text:traits:)`?

Keep `ReceiptRowStyler`, `brandFont`, `detailColor` and `makeDescriptionLabel(text:traits:)` with their current names and signatures. The preview controller already works.
