I am using UIKit on tvOS 26 deployment target; available validation anchor tvOS 26.5.

A video card can show whether audio description is available. Loading track information may succeed with no match, fail, or still be in progress. The player item can change before loading finishes. We must preserve the user’s selected audio and captions. How should the metadata state and callback logic work, and what would unit tests prove?

This is a design/debugging question; no existing project or omitted source files are available. If code is useful, supply a self-contained minimal example and state material assumptions. Do not execute anything.
