# Preserved Modal Revisions

- Revision1: eleven positive methods passed; four intentional defects were caught.
  That green suite omitted a retained-but-removed target boundary.
- Revision2: unchanged implementation, expanded twelve-method test suite. Exactly
  the new retained-removal assertion failed. This reproduces the gap before repair.
- Revision3: current implementation checks background-subtree membership and prior
  hidden state, with thirteen positive methods and five deliberate negative controls.

Sources, tests, negative fixtures, manifests and coverage for revisions1/2 are
preserved here. Sanitized run records live under the root validation directory.
Old hashes are not refreshed to make old results look current. The historical
prompt/controller copy in revision1 is a draft, not a released gold artifact.
