"""Native Claude stream accounting: response IDs are distinct from content blocks.

No provider calls. Preserve the client's num_turns as opaque telemetry, not a
hard count of model round trips. Permissions and actual retrieval stay separate.
"""
import pathlib, hashlib
MODEL = 'claude-haiku-5-5'
sha = lambda data: hashlib.sha256(data).hexdigest()

def text_of(x):
    if isinstance(x, str):
        return x
    if isinstance(x, list):
        return '\n'.join((text_of(y) for y in x))
    if isinstance(x, dict):
        return text_of(x.get('content', '')) if x.get('type') == 'tool_result' else str(x.get('text', ''))
    return ''

class Trace:

    def __init__(self, job, catalog_pins):
        self.job = job
        self.catalog_pins = catalog_pins
        self.response_ids = []
        self.assistant_blocks = 0
        self.missing_response_ids = 0
        self.calls = {}
        self.reads = []
        self.skill_results = []
        self.contents = []
        self.answer = []
        self.result = None
        self.init = None
        self.error = None
        self.read_bytes = 0

    def feed(self, obj):
        typ = obj.get('type')
        assert obj.get('subtype') not in ('hook_started', 'hook_progress', 'hook_response'), 'Unexpected hook event'
        if typ == 'system' and obj.get('subtype') == 'init':
            self.init = obj
            tools = set(obj.get('tools', []))
            assert tools <= {'Read', 'Skill', 'EndConversation'}, 'Unexpected tool catalog'
            assert not obj.get('mcp_servers'), 'Unexpected MCP'
            allowed = {'cc-plugin-agents-md', 'cc-plugin-telemetry', 'cc-plugin-privacy', 'cc-plugin-plugin-authoring'}
            assert all((x.get('name') in allowed and x.get('path') == 'builtin' and (x.get('source') == x.get('name') + '@builtin') or (x.get('name') == 'native-eval' and pathlib.Path(x.get('path', '')).resolve() == pathlib.Path(self.job.get('plugin_root', '/nonexistent')).resolve()) for x in obj.get('plugins', []))), 'Unexpected external/unpinned plugin'
            catalog = self.catalog_pins
            skills = set(obj.get('skills', []))
            expected = self.job['expected_skill']
            assert skills <= set(catalog['client_background_skills']) | ({expected} if expected else set()), 'Unexpected skill catalog'
            if expected:
                assert expected in skills, 'Expected native skill absent from catalog'
            else:
                assert not any((x.endswith('swift-accessibility-agent') for x in skills)), 'Generic control contaminated by target skill'
        msg = obj.get('message', {}) if typ in ('assistant', 'user') else {}
        assert isinstance(msg, dict), 'Malformed assistant/user message'
        content = msg.get('content', [])
        self.contents.append(text_of(content))
        if typ == 'assistant' and isinstance(content, list):
            self.assistant_blocks += 1
            response_id = msg.get('id')
            if isinstance(response_id, str) and response_id:
                if response_id not in self.response_ids:
                    self.response_ids.append(response_id)
            else:
                self.missing_response_ids += 1
            for block in content:
                if block.get('type') == 'tool_use':
                    name = block.get('name')
                    assert name in ('Read', 'Skill', 'EndConversation'), 'Unsupported tool call'
                    assert block['id'] not in self.calls, 'Duplicate tool call ID'
                    self.calls[block['id']] = {'name': name, 'input': block.get('input', {}), 'returned': False}
                    if name == 'Skill':
                        assert block.get('input', {}).get('skill') in self.job.get('skill_aliases', [self.job['expected_skill']]), 'Unexpected skill'
                elif block.get('type') == 'text':
                    self.answer.append(block.get('text', ''))
        if typ == 'user' and isinstance(content, list):
            for block in content:
                if block.get('type') != 'tool_result':
                    continue
                call = self.calls.get(block.get('tool_use_id'))
                assert call is not None, 'Unmatched tool result'
                call['returned'] = True
                failed = bool(block.get('is_error'))
                txt = text_of(block.get('content', ''))
                if call['name'] == 'Read':
                    args = call['input']
                    path = pathlib.Path(args.get('file_path', args.get('path', '')))
                    if not path.is_absolute():
                        path = pathlib.Path(self.job['workspace']) / path
                    resolved = path.resolve()
                    inside = resolved.is_relative_to(pathlib.Path(self.job['workspace']).resolve())
                    if not inside:
                        assert failed, 'Outside-root read succeeded'
                    self.read_bytes += len(txt.encode())
                    self.reads.append({'path': str(resolved), 'inside_workspace': inside, 'is_error': failed, 'arguments': args, 'returned_bytes': len(txt.encode()), 'returned_sha256': sha(txt.encode()), 'source_sha256': sha(resolved.read_bytes()) if inside and resolved.is_file() else None, 'result_excerpt': txt if self.job['condition'] == 'qualification' else None})
                elif call['name'] == 'Skill':
                    self.skill_results.append({'name': call['input'].get('skill'), 'canonical_name': self.job['expected_skill'], 'is_error': failed, 'returned_sha256': sha(txt.encode())})
        if typ == 'result':
            self.result = obj

    def finish(self):
        assert self.result is not None, 'Missing finish receipt'
        o = self.result
        u = o.get('usage')
        assert isinstance(u, dict), 'Missing usage'
        keys = ['input_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens', 'output_tokens']
        assert all((type(u.get(k)) is int and u[k] >= 0 for k in keys)), 'Incomplete token telemetry'
        assert type(o.get('num_turns')) is int and o['num_turns'] >= 0, 'Missing/invalid client turn counter'
        assert set(o.get('modelUsage', {})) == {MODEL}, 'Model substitution/unexposed model'
        success = o.get('subtype') == 'success' and (not o.get('is_error'))
        turn_limit = o.get('subtype') == 'error_max_turns'
        assert success or turn_limit, 'Unexpected provider termination'
        return {'status': 'completed' if success else 'turn-limit', 'total_tokens': sum((u[k] for k in keys)), 'usage': u, 'num_turns': o['num_turns'], 'observed_model_responses': len(self.response_ids) if not self.missing_response_ids else None, 'assistant_message_events': self.assistant_blocks, 'response_ids': self.response_ids, 'returned_read_bytes': self.read_bytes, 'tool_calls': self.calls, 'reads': self.reads, 'skill_results': self.skill_results, 'answer': o.get('result', '') or '\n'.join(self.answer), 'result': o, 'catalog': self.init, 'native_context_text': '\n'.join(self.contents)}

class QuotaBudget:
    """Conservative observed percentage-point usage, including other account use.

    Readings are rounded. Check between sessions, so thresholds can overshoot by
    one session plus display rounding. Reset segments never refund prior usage.
    """

    def __init__(self, baseline, limits=None):
        self.limits = limits or {'five_hour': 5.0, 'seven_day': 1.0}
        self.previous = self._windows(baseline)
        self.consumed = {key: 0.0 for key in self.limits}

    def _windows(self, snapshot):
        windows = {row['bucket']: row for row in snapshot.get('windows', [])}
        for key in self.limits:
            row = windows.get(key, {})
            value = row.get('used_percent')
            if type(value) not in (int, float) or not 0 <= value <= 100 or type(row.get('reset_at')) not in (int, float):
                raise ValueError('Missing/invalid subscription quota reading: ' + key)
        return windows

    def observe(self, snapshot):
        current = self._windows(snapshot)
        for key in self.limits:
            old, new = (self.previous[key], current[key])
            delta = new['used_percent'] - old['used_percent'] if new['reset_at'] == old['reset_at'] else new['used_percent']
            self.consumed[key] += max(0.0, delta)
        self.previous = current
        return dict(self.consumed)

    def exhausted(self):
        return any((self.consumed[key] >= limit for key, limit in self.limits.items()))
