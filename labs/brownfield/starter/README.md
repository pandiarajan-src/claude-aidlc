# Brownfield starter: Invoice exports

This existing service exports a single synthetic invoice to CSV. From this
directory, run `python -B -m unittest -v` (use `python3` or `py -3` if that is
your Python command). Start with Python 3.10+.

Before making changes, locate the public `export_invoice()` function and record
the exact CSV contract and error behavior. Add a separate `export_bulk()` entry
point in `bulk_export.py`; do not change the existing single export contract.
The exercise uses an explicit keyword flag (`enabled=False` by default).
When off, return no CSV and raise `PermissionError`; when on, accept 1–10
known, unique IDs, preserve request order, and return one header. Reject an
empty, oversized, duplicate, or unknown batch with `ValueError`.

Use the existing synthetic fixture and in-memory CSV only. There are no
customer records or production flags. Keep the existing tests intact and add
acceptance tests for the bulk path.
