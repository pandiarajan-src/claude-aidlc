class FakeOutbox:
    def __init__(self) -> None:
        self.messages: list[tuple[str, str]] = []

    def send(self, request_id: str, message: str) -> None:
        self.messages.append((request_id, message))
