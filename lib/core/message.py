from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class Message:
    sender: str
    content: str
    timestamp: datetime

    @staticmethod
    def create(sender: str, content: str) -> "Message":
        return Message(
            sender=sender,
            content=content,
            timestamp=datetime.now(timezone.utc),
        )