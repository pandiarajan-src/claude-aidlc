import unittest
from unittest.mock import patch

from bulk_export import export_bulk
from invoice_export import export_invoice


class BulkExportTests(unittest.TestCase):
    def test_bulk_writes_one_header_and_keeps_request_order(self):
        self.assertEqual(
            export_bulk(["INV-002", "INV-001"], enabled=True),
            "invoice_id,amount_cents\nINV-002,2180\nINV-001,1250\n",
        )

    def test_exact_batch_limit_is_allowed(self):
        fixtures = {f"INV-{number:03}": number for number in range(10)}
        with patch("bulk_export.INVOICES", fixtures):
            self.assertEqual(len(export_bulk(list(fixtures), enabled=True).splitlines()), 11)

    def test_rejects_bad_batches_before_rendering(self):
        for ids in [[], ["INV-001"] * 11, ["INV-001", "INV-001"], ["INV-001", "INV-999"]]:
            with self.subTest(ids=ids), patch("bulk_export.render_csv") as render:
                with self.assertRaises(ValueError):
                    export_bulk(ids, enabled=True)
                render.assert_not_called()

    def test_rollout_can_be_disabled_without_changing_legacy_export(self):
        self.assertEqual(export_bulk(["INV-001"], enabled=True), export_invoice("INV-001"))
        with self.assertRaises(PermissionError):
            export_bulk(["INV-001"])
        self.assertEqual(export_invoice("INV-001"), "invoice_id,amount_cents\nINV-001,1250\n")
