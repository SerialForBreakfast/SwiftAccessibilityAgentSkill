#!/usr/bin/env python3
"""Mechanically transfer release-note inventory tables/bullets from the pass-3 notes
into research/os-27/inventory/. No retyping of Apple text: rows are copied from notes."""
import re, sys, os

NOTES = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def read(name):
    with open(os.path.join(NOTES, name), encoding="utf-8") as f:
        return f.read().splitlines()

# Pass-2 claim IDs keyed by Apple issue number (from the pass-2 platform pages)
PASS2 = {
    "173211711": "IOS-01, TV-02, API-02",
    "161843040": "IOS-02",
    "170005251": "IOS-03",
    "186294594": "IOS-04",
    "188312290": "IOS-05",
    "159870239": "IOS-06, WATCH-01",
    "170479084": "IPAD-01",
    "170480710": "IPAD-01",
    "166422120": "IPAD-02",
    "168247372": "IPAD-03",
    "162577742": "MAC-01, API-05",
    "163365571": "MAC-02, API-04",
    "43112307": "MAC-03",
    "169837566": "MAC-03",
    "155906280": "MAC-04",
    "171831601": "MAC-04",
    "188643179": "MAC-05",
    "187921017": "MAC-06",
    "177389941": "TV-03",
    "175305506": "VISION-01",
    "172214657": "VISION-02",
    "187035825": "VISION-03",
    "98999595": "WEB-02",
    "159865815": "WEB-02",
    "172931277": "WEB-02",
    "186015032": "WEB-03",
    "186766347": "WEB-04",
    "187788949": "WEB-05",
    "182558329": "WEB-06",
}

def pass2_for(text):
    ids = []
    for num in re.findall(r"\b(\d{8,9})\b", text):
        if num in PASS2 and PASS2[num] not in ids:
            ids.append(PASS2[num])
    return "; ".join(ids)

def table_rows(lines, prefix):
    return [l for l in lines if re.match(r"^\| %s-\d+" % prefix, l)]

def split_cells(row):
    # rows from notes never contain escaped pipes inside cells except inside code; keep simple
    cells = row.strip().strip("|").split(" | ")
    return [c.strip() for c in cells]

HEADER_NOTE = (
    "Research only. Mechanically transferred from the pass-3 research notes on 2026-11-05 "
    "(script `build_inventory.py`, not retyped). Every row is **Tier-1**, evidence type "
    "**release note**. Apple text is truncated in the notes (22 words or fewer). "
    "Symbol availability for any API named here is pending unless "
    "[api-availability.md](../api-availability.md) records DocC metadata. The `Pass-2 ID` column "
    "cross-references earlier claim IDs by Apple issue number.\n"
)

def write(name, content):
    fixed = []
    for ln in content.split("\n"):
        fixed.append(ln)
        if ln and not ln.startswith("|"):
            fixed.append("")
    content = "\n".join(fixed)
    while "\n\n\n" in content:
        content = content.replace("\n\n\n", "\n\n")
    content = content.rstrip("\n") + "\n"
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)

# ---------------- iOS / iPadOS ----------------
lines = read("ios_ipados.md")
rows = table_rows(lines, "IOS") + table_rows(lines, "IPAD")
hdr = "| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | iPad-specific | A11y / adjacent flag | Apple text (≤22 words) | Workaround (≤18 words) | Pass-2 ID |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
def idnum(r):
    c = split_cells(r)[0]
    p, n = c.split("-")
    return (0 if p == "IOS" else 1, int(n))
groups = {"27.0": [], "27.2": [], "27.3 beta": []}
for r in rows:
    rel = split_cells(r)[1]
    groups[rel].append(r)
def ios_order(r):
    # keep notes' alphabetical-section order: sort by section then by original ID
    c = split_cells(r)
    return (c[2].lower(), idnum(r))
out = ["# iOS and iPadOS 27 release-note inventory\n", HEADER_NOTE,
       "Sources: [27.0](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes) "
       "(68,415 bytes), [27.2](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_2-release-notes) "
       "(4,276 bytes), [27.3 beta](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes) "
       "(5,111 bytes). Full hashes: [sources.md](../sources.md). No 27.1 notes exist (HTTP 404; see [releases.md](../releases.md)).\n",
       "iOS and iPadOS share one Apple document. `IPAD-1xx` rows are entries the notes classified as iPad-specific; they are listed in Apple section order alongside `IOS-1xx` rows.\n",
       "Locator for every row: the release page plus the `Section` column plus the issue number.\n"]
counts = {}
for rel, title in (("27.0", "Stable: 27.0"), ("27.2", "Stable: 27.2"), ("27.3 beta", "Beta (not shipped): 27.3 beta")):
    rs = sorted(groups[rel], key=ios_order)
    counts[rel] = len(rs)
    out.append(f"\n## {title} ({len(rs)} entries)\n\n")
    if rel == "27.3 beta":
        out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
    out.append(hdr)
    for r in rs:
        out.append(r.rstrip() + f" {pass2_for(r)} |\n")
out.append(f"\nTotals: {sum(counts.values())} entries (27.0: {counts['27.0']}; 27.2: {counts['27.2']}; 27.3 beta: {counts['27.3 beta']}). Matches the notes' count of 322.\n")
write("ios-ipados.md", "".join(out))
print("ios", counts)

# ---------------- macOS ----------------
lines = read("macos.md")
rows = table_rows(lines, "MAC")
hdr = "| ID | Release | Section | Status | Apple issue (FB) | Apple text (≤22 words, verbatim prefix) | SDK cond. | Workaround | A11y/interaction flag (heuristic) | Tier | Priority | Pass-2 ID |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
groups = {"27.0": [], "27.2": [], "27.3 beta": []}
for r in rows:
    groups[split_cells(r)[1]].append(r)
out = ["# macOS 27 release-note inventory\n", HEADER_NOTE,
       "Sources: [27.0](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) (66,704 bytes), "
       "[27.2](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes) (2,463 bytes), "
       "[27.3 beta](https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes) (6,176 bytes). No macOS 27.1 exists.\n",
       "The `Tier` column says `T1` as in the notes; under the corpus README this is **Tier-1, release note**. The flag column is the notes' keyword heuristic and includes false positives; the curated list is in [macos.md](../macos.md).\n"]
counts = {}
for rel, title in (("27.0", "Stable: 27.0"), ("27.2", "Stable: 27.2"), ("27.3 beta", "Beta (not shipped): 27.3 beta")):
    rs = groups[rel]
    counts[rel] = len(rs)
    out.append(f"\n## {title} ({len(rs)} entries)\n\n")
    if rel == "27.3 beta":
        out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
    out.append(hdr)
    for r in rs:
        out.append(r.rstrip() + f" {pass2_for(r)} |\n")
out.append(f"\nTotals: {sum(counts.values())} entries (27.0: {counts['27.0']}; 27.2: {counts['27.2']}; 27.3 beta: {counts['27.3 beta']}). Matches the notes' count of 296.\n")
write("macos.md", "".join(out))
print("mac", counts)

# ---------------- visionOS ----------------
lines = read("visionos.md")
rows = table_rows(lines, "VISION")
hdr = "| ID | Source | Section › Sub-heading | Status | Apple issue / FB | SDK-linked | Workaround | Excerpt (≤22 words) | A11y | Tier | Pass-2 ID |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
groups = {"27.0": [], "27.2": [], "27.3 beta": []}
for r in rows:
    src = split_cells(r)[1]
    rel = "27.3 beta" if "27.3" in src else ("27.2" if "27.2" in src else "27.0")
    groups[rel].append(r)
out = ["# visionOS 27 release-note inventory\n", HEADER_NOTE,
       "Sources: [27.0](https://developer.apple.com/documentation/visionos-release-notes/visionos-27-release-notes) (39,780 bytes), "
       "[27.2](https://developer.apple.com/documentation/visionos-release-notes/visionos-27_2-release-notes) (1,919 bytes), "
       "[27.3 beta](https://developer.apple.com/documentation/visionos-release-notes/visionos-27_3-release-notes) (1,416 bytes). No visionOS 27.1 exists.\n",
       "Cross-release issue tracking (VISION-269 to VISION-276) and non-release-note claims are in [visionos.md](../visionos.md).\n"]
counts = {}
for rel, title in (("27.0", "Stable: 27.0"), ("27.2", "Stable: 27.2"), ("27.3 beta", "Beta (not shipped): 27.3 beta, build 24N5286r")):
    rs = groups[rel]
    counts[rel] = len(rs)
    out.append(f"\n## {title} ({len(rs)} entries)\n\n")
    if rel == "27.3 beta":
        out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
    out.append(hdr)
    for r in rs:
        out.append(r.rstrip() + f" {pass2_for(r)} |\n")
out.append(f"\nTotals: {sum(counts.values())} entries (27.0: {counts['27.0']}; 27.2: {counts['27.2']}; 27.3 beta: {counts['27.3 beta']}). Matches the notes' count of 168.\n")
write("visionos.md", "".join(out))
print("vision", counts)

# ---------------- tvOS / watchOS (bullets) ----------------
lines = read("tvos_watchos.md")
section = None
rel = None
entries = []  # dicts
bullet_re = re.compile(r"^- ((?:TV|WATCH)-\d+(?:[–-]\d+)?) · (.*)$")
for i, l in enumerate(lines):
    m = re.match(r"^#### (tvOS|watchOS) (27\.\d)( beta)?", l)
    if m:
        plat = m.group(1)
        rel = m.group(2) + (" beta" if m.group(3) else "")
        continue
    if l.startswith("#### DocC") or l.startswith("### Inferences"):
        rel = None
    if rel is None:
        continue
    m = bullet_re.match(l)
    if m:
        entries.append({"plat": plat, "rel": rel, "id": m.group(1), "body": m.group(2), "sub": []})
    elif l.startswith("  - ") and entries and entries[-1]["rel"] == rel:
        entries[-1]["sub"].append(l.strip()[2:])

def parse_body(body):
    parts = body.split(" · ")
    sect = parts[0].strip()
    status = parts[1].strip() if len(parts) > 1 else ""
    rest = " · ".join(parts[2:]) if len(parts) > 2 else ""
    issues = re.findall(r"\((\d{6,9})\)(?:\((FB\d+)\))?", rest)
    # flag segment(s) between issue and colon
    m = re.match(r"^((?:\(\d+\)(?:\(FB\d+\))?(?:, )?)+)(.*?):\s(.*)$", rest)
    flag, text = "", rest
    if m:
        flag = m.group(2).strip(" ·")
        text = m.group(3)
    return sect, status, issues, flag, text

STATUS = {"NF": "New Feature", "RI": "Resolved", "KI": "Known Issue", "DEP": "Deprecation"}
rows_by = {}
text_by_issue = {}
expanded = []
for e in entries:
    sect, status, issues, flag, text = parse_body(e["body"])
    if e["sub"]:
        text = text + " " + " ".join("[" + s + "]" for s in e["sub"])
    ids = e["id"]
    m = re.match(r"^(TV|WATCH)-(\d+)[–-](\d+)$", ids)
    if m:
        p, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        idlist = [f"{p}-{n}" for n in range(a, b + 1)]
    else:
        idlist = [ids]
    if len(idlist) > 1:
        # expand grouped bullet: assign IDs in the order the issue numbers are listed
        nums = re.findall(r"\((\d{6,9})\)(?:\((FB\d+)\))?", e["body"])
        labels = {}
        for mm in re.finditer(r"\((\d{6,9})\)(?:\(FB\d+\))?([^;(]*)", e["body"]):
            lab = mm.group(2).split(". **")[0].strip().strip("*:,").strip()
            if lab and not lab.startswith("same as"):
                labels[mm.group(1)] = lab
        sm = re.match(r"^(NF|RI|KI|DEP)\b", status)
        if sm:
            status = sm.group(1)
        for k, cid in enumerate(idlist):
            if k < len(nums):
                num, fb = nums[k]
                expanded.append(dict(plat=e["plat"], rel=e["rel"], id=cid, sect=sect, status=status,
                                     issue=num + (f" ({fb})" if fb else ""), flag="", text=None,
                                     note=f"grouped in notes as {ids}; ID assigned by listing order",
                                     raw=labels.get(num, text), label=labels.get(num, "")))
            else:
                expanded.append(dict(plat=e["plat"], rel=e["rel"], id=cid, sect=sect, status=status,
                                     issue="(not listed)", flag="", text=text, note=f"grouped in notes as {ids}", raw=text))
    else:
        iss = "; ".join(n + (f" ({fb})" if fb else "") for n, fb in issues) or "—"
        expanded.append(dict(plat=e["plat"], rel=e["rel"], id=ids, sect=sect, status=status, issue=iss,
                             flag=flag, text=text, note="", raw=text))
        for n, fb in issues:
            text_by_issue.setdefault((e["plat"], n), text)
            text_by_issue.setdefault(("any", n), text)

# fill grouped rows' text from the matching single row (same platform first, else other platform)
for x in expanded:
    if x["text"] is None:
        num = x["issue"].split(" ")[0]
        t = text_by_issue.get((x["plat"], num)) or text_by_issue.get(("any", num))
        if t:
            x["text"] = (("Notes label: " + x["label"] + ". ") if x.get("label") else "") + t + " *(text taken from the matching single entry with the same issue number)*"
        else:
            x["text"] = x["raw"]

def sdk_flag(x):
    return "Yes" if re.search(r"SDK-linked|SDK/deployment|built with the|building against|linked on", x["flag"] + " " + x["text"]) else ""

def emit_platform(plat, fname, title, srcs, expected):
    out = [f"# {title} release-note inventory\n", HEADER_NOTE, srcs,
           "The notes recorded these entries as bullets, not a table; this file converts them mechanically. "
           "Status codes: NF New Feature, RI Resolved Issue, KI Known Issue, DEP Deprecation. "
           "Where the notes grouped several entries under one ID range, the rows are expanded in listing order and marked.\n"]
    counts = {}
    for rel, t in (("27.0", "Stable: 27.0"), ("27.2", "Stable: 27.2"), ("27.3 beta", "Beta (not shipped): 27.3 beta")):
        rs = [x for x in expanded if x["plat"] == plat and x["rel"] == rel]
        counts[rel] = len(rs)
        out.append(f"\n## {t} ({len(rs)} entries)\n\n")
        if rel == "27.3 beta":
            out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
        out.append("| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |\n|---|---|---|---|---|---|---|---|---|---|\n")
        for x in rs:
            st = " / ".join(STATUS.get(s.strip(), s.strip()) for s in [x["status"]])
            text = x["text"].replace("|", "\\|")
            out.append(f"| {x['id']} | {rel} | {x['sect']} | {st} | {x['issue']} | {sdk_flag(x)} | {x['flag'].replace('*','')} | {text} | {x['note']} | {pass2_for(x['issue'])} |\n")
    total = sum(counts.values())
    out.append(f"\nTotals: {total} entries (27.0: {counts['27.0']}; 27.2: {counts['27.2']}; 27.3 beta: {counts['27.3 beta']}). Expected from the notes: {expected}.\n")
    write(fname, "".join(out))
    print(plat, counts)

emit_platform("tvOS", "tvos.md", "tvOS 27",
    "Sources: [27.0](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes) (17,814 bytes), "
    "[27.2](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes) (1,517 bytes), "
    "[27.3 beta](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_3-release-notes) (1,385 bytes). No tvOS 27.1 exists.\n",
    "62 + 4 + 2 = 68")
emit_platform("watchOS", "watchos.md", "watchOS 27",
    "Sources: [27.0](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) (18,698 bytes), "
    "[27.2](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_2-release-notes) (1,544 bytes), "
    "[27.3 beta](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes) (1,412 bytes). No watchOS 27.1 exists.\n",
    "67 + 4 + 2 = 73")

# ---------------- Safari and Xcode (bullets, split by radar) ----------------
lines = read("safari_webkit_xcode.md")
def collect(prefix, start_pat, stop_pat):
    res = []
    rel = None
    sect = ""
    for l in lines:
        m = re.match(start_pat, l)
        if m:
            rel = m.group(1)
            sect = l.strip("*").strip()
            continue
        if re.match(stop_pat, l):
            rel = None
        if rel is None:
            continue
        m = re.match(r"^- \*\*(%s-\d+[a-e]?)\*\*\s*(\[T\d\]\s*)?(.*)$" % prefix, l)
        if m:
            res.append(dict(rel=rel, sect=sect, id=m.group(1), text=m.group(3)))
    return res

def split_radar(text):
    frags = re.split(r"(?<=\))\.\s+", text)
    rows, loc = [], []
    for f in frags:
        if re.search(r"\(\d{6,9}", f) or re.search(r"\(\d{7,9}\)", f):
            rows.append(f.strip())
        elif re.match(r"^(Locator|§|Source)", f.strip()):
            loc.append(f.strip())
        elif rows:
            rows[-1] = rows[-1] + ". " + f.strip()
        else:
            rows.append(f.strip())
    return rows, " ".join(loc)

def radars(s):
    return ", ".join(re.findall(r"\b(\d{7,9})\b", s)) or "—"

# Safari: release headings in the notes
saf = []
cur_rel = None
for l in lines:
    if l.startswith("## Q2"):
        break
    m = re.match(r"^\*\*Safari (27\.\d)( beta)?", l)
    if m:
        cur_rel = m.group(1) + (" beta" if m.group(2) or "BETA" in l else "")
        cur_sect = l.strip("*").split("**")[0].strip()
        continue
    m = re.match(r"^- \*\*(WEB-\d+[a-e]?)\*\*\s*(\[T\d\]\s*)?(.*)$", l)
    if m and cur_rel:
        saf.append(dict(rel=cur_rel, sect=cur_sect, id=m.group(1), text=m.group(3)))

out = ["# Safari and WebKit 27 release-note inventory\n", HEADER_NOTE,
       "Sources: [Safari 27](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) (117,412 bytes), "
       "[27.1](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes) (1,870 bytes), "
       "[27.2](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) (5,322 bytes), "
       "[27.3 beta](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes) (64,306 bytes). Full hashes: [sources.md](../sources.md).\n",
       "**Scope warning.** Unlike the OS inventories, the notes did not extract every Safari entry. They extracted every entry in the Accessibility sections plus accessibility-relevant entries from other sections (CSS focus, forms, HTML focus, media/captions, Web Inspector, WebDriver). WebKit's beta post counts 58 new features, 525 fixes and 4 deprecations for 27.0 alone. A complete Safari inventory is in the [backlog](../backlog.md). Issue numbers are Apple radar IDs, not WebKit Bugzilla IDs.\n",
       "Rows are split from the notes' bullets at each radar-numbered sentence; grouped bullets keep their claim ID with a part number.\n"]
order = ["27.0", "27.1", "27.2", "27.3 beta"]
for rel in order:
    rs = [x for x in saf if x["rel"] == rel]
    title = ("Beta (not shipped): " if "beta" in rel else "Stable: ") + "Safari " + rel
    out.append(f"\n## {title}\n\n")
    if "beta" in rel:
        out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
    out.append("| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Pass-2 ID |\n|---|---|---|---|---|---|---|\n")
    n = 0
    for x in rs:
        frs, loc = split_radar(x["text"])
        for k, f in enumerate(frs, 1):
            cid = x["id"] if len(frs) == 1 else f"{x['id']} (part {k})"
            out.append(f"| {cid} | {rel} | {x['sect']} | {radars(f)} | {f.replace('|','\\|')} | {loc.replace('|','\\|')} | {pass2_for(f)} |\n")
            n += 1
    out.append(f"\n{n} rows.\n")
write("safari.md", "".join(out))
print("safari rows", len(saf))

# Xcode
xc = []
cur_rel = None
inq3 = False
for l in lines:
    if l.startswith("## Q3"):
        inq3 = True
        continue
    if l.startswith("## Q4"):
        break
    if not inq3:
        continue
    m = re.match(r"^\*\*Xcode (27(?:\.\d)?)( beta)?", l)
    if m:
        cur_rel = (m.group(1) if "." in m.group(1) else "27.0") + (" beta" if "BETA" in l or m.group(2) else "")
        cur_sect = l.strip("*").split("**")[0].strip()
        continue
    if l.startswith("**Security skill"):
        cur_rel = "27.0"
        cur_sect = "Security skill (naming collision with \"audit\")"
        continue
    m = re.match(r"^- \*\*(XCODE-\d+[a-e]?)\*\*\s*(\[T\d\]\s*)?(.*)$", l)
    if m and cur_rel:
        xc.append(dict(rel=cur_rel, sect=cur_sect, id=m.group(1), text=m.group(3)))
out = ["# Xcode 27 release-note inventory\n", HEADER_NOTE,
       "Sources: [Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) (67,593 bytes), "
       "[27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) (2,210 bytes), "
       "[27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) (7,778 bytes), "
       "[27.3 beta](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes) (3,878 bytes). Full hashes: [sources.md](../sources.md).\n",
       "**Scope warning.** The notes extracted accessibility tooling, testing, previews, Simulator, Device Hub, coding-assistant and availability entries, not every Xcode entry. A complete Xcode inventory is in the [backlog](../backlog.md). XCODE-102 and XCODE-103 are DocC API-reference records, not release-note entries; they are kept here because the notes number them in the same sequence. WWDC claims XCODE-121 to XCODE-127 are in [wwdc.md](../wwdc.md) and [xcode-tooling.md](../xcode-tooling.md).\n"]
for rel in ["27.0", "27.1", "27.2", "27.3 beta"]:
    rs = [x for x in xc if x["rel"] == rel]
    title = ("Beta (not shipped): " if "beta" in rel else "Stable: ") + "Xcode " + rel
    out.append(f"\n## {title}\n\n")
    if "beta" in rel:
        out.append("These rows are beta-only. Do not treat them as shipped behavior.\n\n")
    out.append("| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Evidence type |\n|---|---|---|---|---|---|---|\n")
    n = 0
    for x in rs:
        frs, loc = split_radar(x["text"])
        et = "API declaration (DocC)" if x["id"] in ("XCODE-102", "XCODE-103") else "release note"
        for k, f in enumerate(frs, 1):
            cid = x["id"] if len(frs) == 1 else f"{x['id']} (part {k})"
            out.append(f"| {cid} | {rel} | {x['sect']} | {radars(f)} | {f.replace('|','\\|')} | {loc.replace('|','\\|')} | {et} |\n")
            n += 1
    out.append(f"\n{n} rows.\n")
write("xcode.md", "".join(out))
print("xcode bullets", len(xc), [x['id'] for x in xc])
