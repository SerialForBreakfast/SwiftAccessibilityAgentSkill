"""Verify observed AGY generation metadata for the pinned Flash Low transport.

In the recorded AGY format, a session may include compact response metadata
without a request block. Never use text from a subject prompt as model evidence.
"""


def _varint(data, offset):
    for shift in range(0, 70, 7):
        if offset >= len(data):
            raise ValueError('Truncated AGY metadata')
        byte = data[offset]
        offset += 1
        if shift == 0:
            value = 0
        value |= (byte & 127) << shift
        if byte < 128:
            return value, offset
    raise ValueError('Invalid AGY varint')


def _bytes_fields(data):
    offset = 0
    while offset < len(data):
        tag, offset = _varint(data, offset)
        field, kind = divmod(tag, 8)
        if not field:
            raise ValueError('Invalid AGY field')
        if kind == 0:
            _, offset = _varint(data, offset)
        elif kind in (1, 5):
            offset += 8 if kind == 1 else 4
        elif kind == 2:
            length, offset = _varint(data, offset)
            end = offset + length
            if end > len(data):
                raise ValueError('Truncated AGY field')
            yield field, data[offset:end]
            offset = end
        else:
            raise ValueError('Unsupported AGY wire type')
        if offset > len(data):
            raise ValueError('Truncated AGY field')


def flash_low_evidence(records):
    evidence = []
    for record in records:
        labels, models, requests = [], [], []
        for field, value in _bytes_fields(record):
            if field == 1:
                for key, item in _bytes_fields(value):
                    if key == 19:
                        models.append(item.decode())
                    if key == 21:
                        labels.append(item.decode())
            if field == 3:
                requests.extend(item.decode() for key, item in _bytes_fields(value) if key == 28)
        if labels != ['Gemini 3.8 Flash (Low)'] or models != ['gemini-3.8-flash-n']:
            raise ValueError('Unexpected AGY response model')
        if any(req != 'gemini-3.8-flash-low' for req in requests):
            raise ValueError('Unexpected AGY requested model')
        evidence.append(dict(response_model=models[0], label=labels[0], requested_ids=requests))
    if not any(row['requested_ids'] for row in evidence):
        raise ValueError('Missing AGY session request metadata')
    return evidence
