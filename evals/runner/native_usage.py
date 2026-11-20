"""Validate a subscription observation emitted by a native Claude session."""
import math


def subscription_windows(events, *, now):
    records = [e['rate_limit_info'] for e in events if e.get('type') == 'rate_limit_event']
    if not records:
        raise ValueError('Missing subscription event')
    rows = []
    for record in records:
        if (record.get('status') != 'allowed' or record.get('isUsingOverage') is not False
                or record.get('overageStatus') != 'rejected'):
            raise ValueError('Subscription or extra-usage status prevents continuation')
        rows = []
        for bucket in ('five_hour', 'seven_day'):
            window = record.get('unifiedWindows', {}).get(bucket, {})
            value, reset = window.get('utilization'), window.get('resetsAt')
            if (type(value) not in (float, int) or not 0 <= value < 1
                    or type(reset) not in (float, int) or not math.isfinite(reset)
                    or reset <= now or window.get('status') != 'allowed'):
                raise ValueError('Missing, exhausted or expired ' + bucket + ' subscription window')
            rows.append(dict(bucket=bucket, used_percent=round(100 * value, 6), reset_at=reset))
    return rows
