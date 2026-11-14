import hashlib
import json
import unittest
from zipfile import ZipFile
from build import DISC, HERE, build


class FocusedPanel(unittest.TestCase):
    def test_archived_prompts_match_originals_or_reviewed_controls(self):
        panel = json.loads((HERE/"panel.json").read_bytes())
        specs = json.loads((HERE/"controls/rubrics.json").read_bytes())
        authored = {panel["controlsByDecision"][f]: spec for f,spec in specs.items()}
        with ZipFile(HERE/"questions.zip") as subjects, ZipFile(DISC/"subjects.zip") as originals:
            self.assertEqual(len(subjects.namelist()),62)
            self.assertEqual(len(panel["questions"]),62)
            self.assertEqual(set(subjects.namelist()),{f"questions/{r['id']}.md" for r in panel["questions"]})
            for row in panel["questions"]:
                k = row["id"]
                name = f"questions/{k}.md"
                data = subjects.read(name)
                self.assertEqual(hashlib.sha256(data).hexdigest(),row["promptSHA256"])
                expected = (HERE/"controls"/authored[k]["file"]).read_bytes() if k in authored else originals.read(name)
                self.assertEqual(expected,data)
        self.assertEqual(len(panel["controlsByDecision"]),17)
        self.assertNotIn(None,panel["controlsByDecision"].values())

    def test_outputs_rebuild_without_modifying_candidate(self):
        for name,data in build().items():
            self.assertEqual(data,(HERE/name).read_bytes())
        self.assertEqual(hashlib.sha256((HERE/"candidate.zip").read_bytes()).hexdigest(),
                         "aa23b85f2235f1eb74f7738c8541529950b44b9a048fdf38f2660024ceed7b5c")
