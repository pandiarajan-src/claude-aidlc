import unittest

from notifications import NotificationService
from outbox import FakeOutbox


class NotificationTests(unittest.TestCase):
    def setUp(self):
        self.outbox = FakeOutbox()
        self.service = NotificationService(self.outbox)

    def test_new_request_is_queued(self):
        self.assertEqual(self.service.submit("notice-1", "Parcel ready"), "queued")
        self.assertEqual(self.outbox.messages, [("notice-1", "Parcel ready")])

    def test_duplicate_does_not_replace_first_message(self):
        self.service.submit("notice-1", "Parcel ready")
        self.assertEqual(self.service.submit("notice-1", "Changed text"), "duplicate")
        self.assertEqual(self.outbox.messages, [("notice-1", "Parcel ready")])

    def test_blank_id_or_message_is_rejected_without_writing(self):
        for request_id, message in [(" ", "Parcel ready"), ("notice-1", "\t")]:
            with self.subTest(request_id=request_id, message=message):
                with self.assertRaises(ValueError):
                    self.service.submit(request_id, message)
        self.assertEqual(self.outbox.messages, [])
