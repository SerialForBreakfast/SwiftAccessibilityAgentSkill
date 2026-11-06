# First Attempt

Revision1 source, tests, negative fixtures, manifest and source/coverage records
are preserved before the locale accessor repair. Compilation and seven positive
methods passed; the compiler emitted the languageCode deprecation warning.
No revision1 mutant execution is claimed. Current revision2 changes only that
accessor in source and matching mutant files, with refreshed hashes.

Reports in ../validation bind each revision independently. Do not replace old
records when a later toolchain changes its diagnostic wording.
