"""Chat answer contract for future packets, plus the strict extractor that grades against it.

Format, code behavior and skill invocation are separate grades. The extractor never repairs code:
it accepts exactly one unambiguous Swift block unchanged, or records why it could not.
"""
import re

# Appended to every subject prompt in future packets (replaces "Return only Submission.swift").
CONTRACT = ("Put the complete Swift file in exactly one fenced ```swift code block in your final reply. "
            "Do not create, edit or save any files. Text outside the block is allowed and is not graded.")

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})\s*([\w+-]*)\s*$")


def blocks(answer):
    """Return (blocks, unterminated, outside). Each block is (language, text); outside is the prose."""
    found, open_fence, lang, lines, outside = [], None, "", [], []
    for line in answer.splitlines(keepends=True):
        m = FENCE.match(line.rstrip("\n"))
        if open_fence is None:
            if m:
                open_fence, lang, lines = m.group(1), m.group(2).lower(), []
            else:
                outside.append(line)
        elif m and m.group(1)[0] == open_fence[0] and len(m.group(1)) >= len(open_fence) and not m.group(2):
            found.append((lang, "".join(lines)))
            open_fence = None
        else:
            lines.append(line)
    return found, open_fence is not None, "".join(outside)


def extract(answer):
    """Classify one original response. Returns a dict; 'code' is set only when status == 'accepted'."""
    found, unterminated, outside = blocks(answer)
    if unterminated:
        return dict(status="unterminated", blocks=len(found), code=None)
    if not found:
        return dict(status="no-code", blocks=0, code=None)
    if len(found) > 1:
        return dict(status="ambiguous", blocks=len(found), languages=[l for l, _ in found], code=None)
    lang, text = found[0]
    if lang not in ("swift", ""):
        return dict(status="wrong-language", blocks=1, languages=[lang], code=None)
    return dict(status="accepted", blocks=1, language=lang or "unlabeled", code=text.encode("utf-8"),
                format="single block only" if not outside.strip() else "single block with prose")
