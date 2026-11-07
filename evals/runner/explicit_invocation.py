"""Explicit native Skill requests and load-proof verification; no inference here.

Registration, a claimed introduction, and a successful 'Launching skill' receipt
are weaker than an observed native message carrying the expected frozen body.
"""
from hashlib import sha256
import re

SKILL = 'native-eval:swift-accessibility-agent'

def skill_body(source):
    """Remove the metadata envelope; retain the body actually loaded by Skill."""
    if source.startswith('---\n'):
        parts = source.split('\n---\n', 1)
        if len(parts) != 2:
            raise ValueError('Unclosed skill frontmatter')
        source = parts[1]
    body = source.strip()
    if not body:
        raise ValueError('Empty skill body')
    return body


def build_request(question, *, skill=None):
    if not isinstance(question, str) or not question.strip():
        raise ValueError('A developer question is required')
    if skill is None:
        return question
    if skill != SKILL:
        raise ValueError('Only the pinned evaluation skill is supported')
    return (
        f'Before answering the developer question below, invoke the native Skill '
        f'tool with skill="{skill}". Follow the loaded skill and retrieve its '
        'applicable references. Do not substitute a claimed invocation or copy '
        'guidance from memory. Then answer the developer question.\n\n'
        'Developer question:\n' + question
    )


class LoadProof:
    """Require successful native dispatch AND its exact body in a user message.

    The controller reads the body for verification only; it is never appended to
    the subject request. Self-reported skill usage and assistant quotations fail.
    """
    def __init__(self, source, *, skill=SKILL):
        self.skill = skill
        self.body = skill_body(source)
        self.source_sha256 = sha256(source.encode()).hexdigest()
        self.body_sha256 = sha256(self.body.encode()).hexdigest()
        self.event = 0
        self.success_event = None
        self.body_event = None
        self.body_payload_sha256 = None

    def observe(self, event, successful_results):
        self.event += 1
        success = any(x.get('canonical_name') == self.skill and not x.get('is_error')
                      for x in successful_results)
        if success and self.success_event is None:
            self.success_event = self.event
        if event.get('type') != 'user' or self.success_event is None:
            return
        msg = event.get('message', {})
        if not isinstance(msg, dict):
            return
        for block in msg.get('content', []):
            if block.get('type') != 'text':
                continue
            text = block.get('text', '')
            if self.body in text:
                self.body_event = self.event
                self.body_payload_sha256 = sha256(text.encode()).hexdigest()

    def finish(self):
        if self.success_event is None or self.body_event is None:
            raise AssertionError('Explicit native skill body load not proven; stop before further sessions')
        return {'passed': True, 'successful_skill_event': self.success_event,
                'body_message_event': self.body_event,
                'source_sha256': self.source_sha256,
                'body_sha256': self.body_sha256,
                'native_payload_sha256': self.body_payload_sha256}
