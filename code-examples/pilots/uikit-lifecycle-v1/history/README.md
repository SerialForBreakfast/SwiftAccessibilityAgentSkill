# Lifecycle pilot history

Revision1's library compiled, but the unit target did not: the category test used
object identity (`===`) for the String-valued edit category. No tests executed.
The adapter rejected the zero-test record as an error; none of the negative checks
were attempted. Original source/test/manifest inputs remain in [revision-1](revision-1/).

Revision2 changes only that assertion to String value equality. Source, mutations,
selected test IDs and adapter safeguards are unchanged. This was an authored-test
type error, not an Apple API behavior observation. The original failed build and
diagnostics remain in the private immutable evidence ledger.
