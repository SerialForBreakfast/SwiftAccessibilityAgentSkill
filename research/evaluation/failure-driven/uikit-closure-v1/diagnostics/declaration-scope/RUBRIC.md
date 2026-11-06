# Declaration Scope Diagnostic Rubric

Author draft; independent review pending. Keep separate from the subject prompt.
This diagnoses source tooling, not an accessibility recommendation or model ranking.

Accept a bounded scan or a real parser. Require handling a completed `@end` before a
global declaration, distinguishing forward declarations from open protocol scopes,
and preserving class/category ownership for members inside a scope. Tests should
include a global after a closed category, an actual member, and a forward declaration.
Do not require the exact implementation in this repository. More complete parsers
may support comments, macros and multiline syntax; a minimal helper should state its
limits rather than claim to parse all Objective-C. Nearby availability annotations
must not be assigned to unrelated symbols.

Score correctness, representative tests, limitations and preservation of raw evidence
separately, 0 absent/wrong, 1 partial, 2 complete. No Apple API introduction dates or
runtime conclusions can be inferred solely from the helper returning a scope.
