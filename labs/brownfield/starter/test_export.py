import unittest

from invoice_export import export_invoice


class ExistingExportTests(unittest.TestCase):
    def test_preserves_header_and_row(self):
        self.assertEqual(export_invoice("INV-001"), "invoice_id,amount_cents\nINV-001,1250\n")

    def test_unknown_single_invoice_raises_key_error(self):
        with self.assertRaises(KeyError):
            export_invoice("INV-000")
