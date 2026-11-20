import unittest

from native_usage import subscription_windows


class SubscriptionWindowsTests(unittest.TestCase):
    def record(self):
        return dict(status='allowed', isUsingOverage=False, overageStatus='rejected',
                    unifiedWindows={key: dict(status='allowed', utilization=0.21, resetsAt=200)
                                    for key in ('five_hour', 'seven_day')})

    def windows(self, record):
        return subscription_windows([dict(type='rate_limit_event', rate_limit_info=record)], now=100)

    def test_observed_percent(self):
        self.assertEqual([r['used_percent'] for r in self.windows(self.record())], [21, 21])

    def test_missing_event(self):
        with self.assertRaises(ValueError):
            subscription_windows([], now=100)

    def test_overage(self):
        with self.assertRaises(ValueError):
            self.windows(dict(self.record(), isUsingOverage=True))

    def test_incomplete_or_stale_windows(self):
        for update in ({'resetsAt': 100}, {'resetsAt': None}, {'utilization': 1},
                       {'utilization': float('nan')}, {'status': 'rejected'}):
            with self.subTest(update=update), self.assertRaises(ValueError):
                record = self.record()
                record['unifiedWindows']['five_hour'].update(update)
                self.windows(record)
        record = self.record()
        del record['unifiedWindows']['seven_day']
        with self.assertRaises(ValueError):
            self.windows(record)
