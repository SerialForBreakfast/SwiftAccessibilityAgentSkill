import unittest
from explicit_invocation import SKILL, LoadProof, build_request, skill_body

class ExplicitInvocationTests(unittest.TestCase):
    source = '---\nname: swift-accessibility-agent\n---\n\n# Frozen body\nRead the applicable evidence.\n'
    success = [{'canonical_name': SKILL, 'is_error': False}]
    def event(self, kind='user', text=None):
        return {'type': kind, 'message': {'content': [{'type': 'text', 'text': text or '# Frozen body\nRead the applicable evidence.'}]}}
    def test_generic_question_unchanged(self):
        self.assertEqual(build_request('Question'), 'Question')
    def test_guided_request_is_native_call_not_body_injection(self):
        request = build_request('Question', skill=SKILL)
        self.assertIn('Skill tool', request);self.assertTrue(request.endswith('Question'))
        self.assertNotIn('Frozen body', request)
    def test_native_message_after_success_proves_body(self):
        proof = LoadProof(self.source);proof.observe(self.event(), self.success)
        self.assertTrue(proof.finish()['passed'])
    def test_announcement_and_assistant_quotation_do_not_prove_load(self):
        for event in [self.event('assistant'), self.event(text='Swift Accessibility Agent v0.2.2')]:
            proof = LoadProof(self.source);proof.observe(event, self.success)
            with self.assertRaises(AssertionError):proof.finish()
    def test_launch_receipt_alone_does_not_prove_body(self):
        proof = LoadProof(self.source);proof.observe(self.event(text='Launching skill'), self.success)
        with self.assertRaises(AssertionError):proof.finish()
    def test_wrong_or_partial_body_rejected(self):
        for text in ['# Frozen body', '# Another version\nRead the applicable evidence.']:
            proof=LoadProof(self.source);proof.observe(self.event(text=text),self.success)
            with self.assertRaises(AssertionError):proof.finish()
    def test_body_without_successful_dispatch_rejected(self):
        proof=LoadProof(self.source);proof.observe(self.event(),[])
        with self.assertRaises(AssertionError):proof.finish()
    def test_body_before_failed_dispatch_does_not_count(self):
        proof=LoadProof(self.source);proof.observe(self.event(),[]);proof.observe(self.event(text='Launching skill'),self.success)
        with self.assertRaises(AssertionError):proof.finish()
    def test_invalid_request_and_frontmatter(self):
        for kwargs in [{'question':''},{'question':'q','skill':'unreviewed'}]:
            with self.assertRaises(ValueError):build_request(**kwargs)
        with self.assertRaises(ValueError):skill_body('---\nmissing end')
if __name__=='__main__':unittest.main()
