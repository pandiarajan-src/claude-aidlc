from outbox import FakeOutbox


class NotificationService:
    def __init__(self, outbox: FakeOutbox) -> None:
        self.outbox = outbox
        self._queued: set[str] = set()

    def submit(self, request_id: str, message: str) -> str:
        if not request_id.strip() or not message.strip():
            raise ValueError("request ID and message must not be blank")
        if request_id in self._queued:
            return "duplicate"
        self.outbox.send(request_id, message)
        self._queued.add(request_id)
        return "queued"
