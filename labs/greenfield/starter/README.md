# Greenfield starter: Notification outbox

This practice repository contains a fake outbox and one passing test, but no
notification service yet. No real address, queue, provider, or network is needed.
From this directory, run `python -B -m unittest -v` (use `python3` or `py -3`
if that is your Python command). Start with Python 3.10+.

Add a `NotificationService` in `notifications.py`. Use only the standard
library and `FakeOutbox`. In the exercise design, `submit(request_id,
message)` returns `queued` for a new ID, `duplicate` for a valid repeat,
and raises `ValueError` for blank or whitespace-only input. The first
message wins; a repeat does not change the existing outbox entry.
Deduplication lasts only for the lifetime of the service instance.

Review the spec and agree on the rules before editing. Add acceptance tests,
run them, and compare your result with the worked solution only after trying.
