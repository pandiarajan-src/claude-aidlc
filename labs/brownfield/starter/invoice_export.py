import csv
import io
from collections.abc import Iterable


INVOICES = {"INV-001": 1250, "INV-002": 2180}


def render_csv(rows: Iterable[tuple[str, int]]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(("invoice_id", "amount_cents"))
    writer.writerows(rows)
    return stream.getvalue()


def export_invoice(invoice_id: str) -> str:
    return render_csv([(invoice_id, INVOICES[invoice_id])])
