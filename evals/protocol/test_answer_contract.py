"""Offline tests for the answer extractor. The real-answer test needs the private rc.1 return copy."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import unittest
from zipfile import ZipFile

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from answer_contract import extract

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "evals/results/rc1-return-20261107/bundles/rc1-release-native-chat-36-v2-return.zip"
SWIFT = "import UIKit\n\nfunc f() {}\n"


class Synthetic(unittest.TestCase):
    def test_single_block_with_prose_is_accepted_unchanged(self):
        r = extract("Here it is:\n\n```swift\n" + SWIFT + "```\n\nNot compiled.")
        self.assertEqual((r["status"], r["code"], r["format"]), ("accepted", SWIFT.encode(), "single block with prose"))

    def test_block_only(self):
        self.assertEqual(extract("```swift\n" + SWIFT + "```\n")["format"], "single block only")

    def test_two_candidates_are_ambiguous_not_first_taken(self):
        r = extract("```swift\n" + SWIFT + "```\nOr:\n```swift\n" + SWIFT + "```\n")
        self.assertEqual((r["status"], r["code"]), ("ambiguous", None))

    def test_swift_plus_other_block_is_ambiguous(self):
        self.assertEqual(extract("```swift\n" + SWIFT + "```\n```sh\nswiftc a.swift\n```\n")["status"], "ambiguous")

    def test_no_code(self):
        self.assertEqual(extract("I changed Submission.swift on disk.")["status"], "no-code")

    def test_unterminated(self):
        self.assertEqual(extract("```swift\n" + SWIFT)["status"], "unterminated")

    def test_wrong_language(self):
        self.assertEqual(extract("```text\n" + SWIFT + "```\n")["status"], "wrong-language")

    def test_inner_backticks_in_longer_fence(self):
        body = "let s = \"```\"\n"
        self.assertEqual(extract("````swift\n" + body + "````\n")["code"], body.encode())


@unittest.skipUnless(V2.exists(), "private rc.1 return copy not present")
class RecordedAnswers(unittest.TestCase):
    def test_all_36_rc1_answers(self):
        z = ZipFile(V2)
        pending = ROOT / "evals/results/rc1-return-20261107/native-pending"
        statuses, distinct = [], set()
        for row in json.loads(z.read("index.json")):
            r = extract(z.read(f"cells/{row['cell']}/answer.txt").decode("utf-8"))
            statuses.append((r["status"], r["format"]))
            distinct.add(hashlib.sha256(r["code"]).hexdigest())
            # Same bytes as the files that were reviewed and graded natively.
            self.assertEqual(r["code"], (pending / f"{row['cell']}-{row['task']}.swift").read_bytes())
        # BigDog's "0/36 raw format" means none was unfenced; all meet the new single-block contract.
        self.assertEqual(Counter(statuses), {("accepted", "single block only"): 21,
                                             ("accepted", "single block with prose"): 15})
        self.assertEqual((len(statuses), len(distinct)), (36, 22))


if __name__ == "__main__":
    unittest.main()
