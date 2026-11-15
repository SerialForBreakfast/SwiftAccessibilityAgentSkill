"""Offline component graders for observed transitions. None means not established."""

def wording(value):
    return " ".join(value.casefold().split()) if isinstance(value, str) else ""


def selection(observations, reviewed_terms=None):
    """Supply (visible, accessibility value) after select then deselect on the same row.
    Supply controller-reviewed localized or equivalent meanings as text -> bool.
    """
    meanings = {"selected": True, "not selected": False, "unselected": False}
    for term, meaning in (reviewed_terms or {}).items():
        key = wording(term)
        if not key or type(meaning) is not bool or meanings.get(key, meaning) != meaning:
            raise ValueError("invalid or conflicting wording calibration")
        meanings[key] = meaning
    if observations is None or len(observations) != 2:
        return "inconclusive"
    unknown = False
    prior = None
    for pair, expected in zip(observations, (True, False)):
        if pair is None:
            unknown = True
            continue
        visible, spoken_value = map(wording, pair)
        if not visible or not spoken_value or prior == visible:
            return "fail"
        prior = visible
        for term in (visible, spoken_value):
            if term not in meanings:
                unknown = True
            elif meanings[term] != expected:
                return "fail"
    return "review wording or missing observation" if unknown else "pass"


def focus(case, *, ordinary, challenge):
    """Each observation is (ordered target IDs from injected request, finish result)."""
    expected = {"Q082-A": (["fallback"], True), "Q082-B": (["primary"], False)}[case]
    def compare(actual, wanted):
        if actual is None:
            return "inconclusive"
        targets, result = actual
        if targets is not None and targets != wanted[0]:
            return "fail"
        if result is not None and result is not wanted[1]:
            return "fail"
        return "inconclusive" if targets is None or result is None else "pass"
    return {"ordinary": compare(ordinary, (["primary"], True)),
            "challenge": compare(challenge, expected)}
