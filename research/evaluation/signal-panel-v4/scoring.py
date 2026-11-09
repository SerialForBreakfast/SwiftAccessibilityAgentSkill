"""Project a proof verdict from reviewed observations; never infer answer quality from prose."""
def proof_verdict(scope, *, needs_fix=None, path=None, observation=None, native=None):
    if scope not in {'no-added-proof-requirement','only-if-fix-needed','describe-check','focused-check','supply-tests'}:
        raise ValueError(scope)
    if scope=='no-added-proof-requirement' or (scope=='only-if-fix-needed' and needs_fix is False):
        return 'not-required'
    if scope=='only-if-fix-needed' and needs_fix is None:
        return 'undetermined'
    if native not in {None,'missed-qualified-mutant','interface-gap','no-executable-proof'}:
        raise ValueError(native)
    if native=='missed-qualified-mutant':
        return 'does-not-distinguish-defect'
    if native=='no-executable-proof' and scope in {'supply-tests','only-if-fix-needed'}:
        return 'requested-unit-check-missing'
    if path is False or observation is False:
        return 'does-not-establish-requested-effect'
    if path is None or observation is None:
        return 'undetermined'
    # Source appraisal can stand even if a native oracle could not bind it.
    return 'source-supported-check'
