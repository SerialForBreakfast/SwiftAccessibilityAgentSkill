"""Offline protocol and quota accounting regressions; no provider calls."""
import pathlib
import tempfile
import unittest
from native_trace import Trace, QuotaBudget, MODEL, UnavailableToolRequest

class NativeTraceTests(unittest.TestCase):
    def trace(self):
        return Trace({'workspace': '/tmp/native-test', 'expected_skill': None,
                      'condition': 'generic'}, {'client_background_skills': []})

    def result(self, turns=5, subtype='success'):
        return {'type': 'result', 'subtype': subtype, 'is_error': subtype != 'success',
                'num_turns': turns, 'modelUsage': {MODEL: {}}, 'result': 'done',
                'usage': {'input_tokens': 6, 'cache_creation_input_tokens': 712,
                          'cache_read_input_tokens': 15447, 'output_tokens': 469}}

    def assistant(self, trace, response_id, content):
        trace.feed({'type': 'assistant', 'message': {'id': response_id, 'content': content}})

    def test_five_blocks_three_responses_is_success(self):
        trace = self.trace()
        for response_id in ['a', 'a', 'b', 'b', 'c']:
            self.assistant(trace, response_id, [{'type': 'text', 'text': 'part'}])
        trace.feed(self.result())
        out = trace.finish()
        self.assertEqual(out['num_turns'], 5)
        self.assertEqual(out['observed_model_responses'], 3)
        self.assertEqual(out['assistant_message_events'], 5)
        self.assertEqual(out['total_tokens'], 16634)

    def test_more_than_four_real_responses_are_telemetry(self):
        trace = self.trace()
        for index in range(6):
            self.assistant(trace, str(index), [{'type': 'text', 'text': 'part'}])
        trace.feed(self.result(turns=6))
        self.assertEqual(trace.finish()['observed_model_responses'], 6)

    def test_missing_ids_are_unknown_not_fabricated(self):
        trace = self.trace()
        self.assistant(trace, None, [{'type': 'text', 'text': 'answer'}])
        trace.feed(self.result())
        self.assertIsNone(trace.finish()['observed_model_responses'])

    def test_status_text_not_answer_or_tool_result(self):
        trace = self.trace()
        trace.feed({'type': 'system', 'subtype': 'permission_denied', 'message': 'denied'})
        self.assertEqual(trace.answer, [])
        self.assertEqual(trace.reads, [])

    def test_malformed_assistant_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'Malformed'):
            self.trace().feed({'type': 'assistant', 'message': 'bad'})

    def test_missing_finish_and_usage_remain_invalid(self):
        trace = self.trace()
        with self.assertRaisesRegex(AssertionError, 'Missing finish'):
            trace.finish()
        result = self.result()
        del result['usage']['cache_read_input_tokens']
        trace.feed(result)
        with self.assertRaisesRegex(AssertionError, 'Incomplete'):
            trace.finish()

    def test_known_limit_is_incomplete_not_semantic_failure(self):
        trace = self.trace()
        trace.feed(self.result(subtype='error_max_turns'))
        self.assertEqual(trace.finish()['status'], 'turn-limit')

    def test_model_substitution_still_rejected(self):
        trace = self.trace()
        result = self.result()
        result['modelUsage'] = {'other-model': {}}
        trace.feed(result)
        with self.assertRaisesRegex(AssertionError, 'Model substitution'):
            trace.finish()

    def test_permissions_and_hooks_still_enforced(self):
        for obj in [
            {'type': 'system', 'subtype': 'hook_started'},
            {'type': 'assistant', 'message': {'content': [
                {'type': 'tool_use', 'id': 'x', 'name': 'Bash', 'input': {}}]}},
        ]:
            with self.assertRaises(AssertionError):
                self.trace().feed(obj)

    def test_unavailable_write_is_a_subject_request_after_verified_catalog(self):
        trace = self.trace()
        trace.feed({'type': 'system', 'subtype': 'init', 'tools': ['Read', 'Skill']})
        with self.assertRaises(UnavailableToolRequest):
            self.assistant(trace, 'a', [{'type': 'tool_use', 'id': 'write', 'name': 'Write'}])

    def test_advertised_write_is_still_an_isolation_failure(self):
        with self.assertRaisesRegex(AssertionError, 'Unexpected tool catalog'):
            self.trace().feed({'type': 'system', 'subtype': 'init', 'tools': ['Write']})

    def test_denied_write_can_finish_with_chat_answer(self):
        for response, valid in [(None, False), ('disk error', False),
                                ('No such tool available: Write', True)]:
            trace = self.trace()
            trace.job['observe_denied_write'] = True
            trace.feed({'type': 'system', 'subtype': 'init', 'tools': ['Read', 'Skill']})
            self.assistant(trace, 'a', [{'type': 'tool_use', 'id': 'w', 'name': 'Write'}])
            if response is None:
                with self.assertRaises(UnavailableToolRequest):
                    trace.finish()
                continue
            event = {'type': 'user', 'message': {'content': [
                {'type': 'tool_result', 'tool_use_id': 'w', 'is_error': True, 'content': response}]}}
            if not valid:
                with self.assertRaises(UnavailableToolRequest):
                    trace.feed(event)
                continue
            trace.feed(event)
            trace.feed(self.result())
            self.assertEqual(trace.finish()['answer'], 'done')
            self.assertEqual(trace.calls['w']['denial'], response)

    def test_successful_write_still_rejects_the_read_only_transport(self):
        trace = self.trace()
        trace.job['observe_denied_write'] = True
        trace.feed({'type': 'system', 'subtype': 'init', 'tools': ['Read', 'Skill']})
        self.assistant(trace, 'a', [{'type': 'tool_use', 'id': 'w', 'name': 'Write'}])
        with self.assertRaisesRegex(AssertionError, 'Write succeeded'):
            trace.feed({'type': 'user', 'message': {'content': [
                {'type': 'tool_result', 'tool_use_id': 'w', 'content': 'File created'}]}})

    def test_outside_read_needs_real_error_result(self):
        trace = self.trace()
        self.assistant(trace, 'a', [{'type': 'tool_use', 'id': 'read', 'name': 'Read',
                                   'input': {'file_path': '/tmp/outside'}}])
        trace.feed({'type': 'system', 'subtype': 'permission_denied', 'message': 'denied'})
        self.assertEqual(trace.reads, [])
        with self.assertRaisesRegex(AssertionError, 'Outside-root'):
            trace.feed({'type': 'user', 'message': {'content': [
                {'type': 'tool_result', 'tool_use_id': 'read', 'content': 'leaked'}]}})

class QuotaTests(unittest.TestCase):
    def snapshot(self, five=24, weekly=18, reset=100):
        return {'windows': [{'bucket': 'five_hour', 'used_percent': five, 'reset_at': reset},
                            {'bucket': 'seven_day', 'used_percent': weekly, 'reset_at': 200}]}

    def test_percentage_points_not_relative_percent(self):
        budget = QuotaBudget(self.snapshot())
        self.assertEqual(budget.observe(self.snapshot(five=27))['five_hour'], 3)
        self.assertFalse(budget.exhausted())
        budget.observe(self.snapshot(five=29))
        self.assertTrue(budget.exhausted())

    def test_reset_does_not_refund_consumption(self):
        budget = QuotaBudget(self.snapshot())
        budget.observe(self.snapshot(five=26))
        budget.observe(self.snapshot(five=1, reset=300))
        self.assertEqual(budget.consumed['five_hour'], 3)

    def test_weekly_stop_and_missing_reading(self):
        budget = QuotaBudget(self.snapshot())
        budget.observe(self.snapshot(weekly=19))
        self.assertTrue(budget.exhausted())
        with self.assertRaises(ValueError):
            budget.observe({'windows': []})

if __name__ == '__main__':
    unittest.main()
