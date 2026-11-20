"""Derive the read-only chat revision without changing the original packet."""
import hashlib
import json
from pathlib import Path

ORIGINAL = 'Return only Submission.swift, preserving this interface.'
REPLACEMENT = ('Paste only the complete Swift source in your final chat response. '
               'Leave all files unchanged and preserve this interface.')


def revised_packet():
    source = Path(__file__).with_name('packet.json').read_bytes()
    digest = hashlib.sha256(source).hexdigest()
    assert digest == '496c51e084498d3eb164cc5a74b0c6398ec654d9acc686212b526f6e492f69c2'
    packet = json.loads(source)
    packet['parentPacketSHA256'] = digest
    packet['job'] = 'rc1-release-native-chat-36-v2'
    for name, question in packet['subjectExports'].items():
        assert question.count(ORIGINAL) == 1
        packet['subjectExports'][name] = question.replace(ORIGINAL, REPLACEMENT)
    for cell in packet['cells']:
        prompt = packet['subjectExports'][cell['task']]
        if cell['lane'] == 'explicit':
            prompt = packet['explicitPrefix'] + prompt
        cell['promptSHA256'] = hashlib.sha256(prompt.encode()).hexdigest()
    return packet


if __name__ == '__main__':
    print(json.dumps(revised_packet(), indent=2))
