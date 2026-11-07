"""Offline protocol and quota accounting regressions; no provider calls."""
import pathlib
import tempfile
import unittest
from native_trace import Trace, QuotaBudget, MODEL

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
