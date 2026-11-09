"""Offline retention checks, not a simulated model grader."""
from pathlib import Path
import unittest
from zipfile import ZipFile

D=Path(__file__).resolve().parent
def load(p):
    with ZipFile(p) as z:
        return {k.removeprefix('swift-accessibility-agent/'):z.read(k) for k in z.namelist()}

class Retention(unittest.TestCase):
    def setUp(self):
        self.parent=load(D.parent/'feedback-review/candidate.zip')
        self.child=load(D/'candidate.zip')
    def test_protected_material(self):
        self.assertEqual(self.parent.keys(), self.child.keys())
        for n in self.parent:
            if '/examples/' in n or n in ('references/facts.md','references/font.md'):
                self.assertEqual(self.parent[n],self.child[n],n)
    def test_entry_contract(self):
        text=self.child['SKILL.md'].decode()
        for anchor in ['on first use','only consulted files','leave it alone','ordinary activation','installed callback']:
            self.assertIn(anchor,text)
        self.assertLess(len(text.encode()),len(self.parent['SKILL.md']))
    def test_scope_and_contrasts(self):
        for name,anchors in {
            'actions':['independently actionable children','current and retired','permitted now','without hiding','is not retirement'],
            'return':['not the close request','initially hidden','before calling reentrant','no-argument callback','on refusal','origin independently'],
            'media':['automatic is different','same item','actual caption','independently','read-only'],
            'validation':['native field','without a newer submission','neither feedback nor eligibility']
        }.items():
            data=self.child['references/'+name+'.md'].decode()
            for a in anchors:
                with self.subTest(card=name,anchor=a): self.assertIn(a,data)
    def test_no_controller_content(self):
        for data in self.child.values():
            self.assertNotRegex(data,rb'P-[0-9a-f]{16}|G-[0-9a-f]{14}|Q[0-9]{2}[XY]')
if __name__=='__main__':unittest.main()
