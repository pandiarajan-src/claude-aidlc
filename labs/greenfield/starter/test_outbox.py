import unittest

from outbox import FakeOutbox


class OutboxTests(unittest.TestCase):
    def test_records_the_request_and_message(self):
        outbox = FakeOutbox()
        outbox.send("notice-1", "Parcel ready")
        self.assertEqual(outbox.messages, [("notice-1", "Parcel ready")])
