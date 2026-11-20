from invoice_export import INVOICES, render_csv


def export_bulk(invoice_ids: list[str], *, enabled: bool = False) -> str:
    if not enabled:
        raise PermissionError("bulk export is disabled")
    if not 1 <= len(invoice_ids) <= 10:
        raise ValueError("choose between 1 and 10 invoices")
    if len(set(invoice_ids)) != len(invoice_ids):
        raise ValueError("invoice IDs must be unique")
    try:
        rows = [(invoice_id, INVOICES[invoice_id]) for invoice_id in invoice_ids]
    except KeyError as error:
        raise ValueError(f"unknown invoice: {error.args[0]}") from error
    return render_csv(rows)
