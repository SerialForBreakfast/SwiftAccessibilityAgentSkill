I am using UIKit on tvOS 26 deployment target; available validation anchor tvOS 26.5.

I reuse one download card for different files. It has a title, optional status, optional help text, selected state and an Open button. Updates can arrive without reconstructing the card: A has status “Ready” and help “Opens offline”; B has neither. A late metadata result for A may arrive after B is shown. Describe a complete update strategy and focused unit checks. Keep Open working.

This is a design/debugging question; no existing project or omitted source files are available. If code is useful, supply a self-contained minimal example and state material assumptions. Do not execute anything.
