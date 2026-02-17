from typing import List
from lib.core.message import Message

class History:
    def __init__(self):
        self._messages: List[Message] = []

    def add(self, message: Message) -> None:
        self._messages.append(message)

    def get_last_n(self, n: int) -> List[Message]:
        return list(self._messages[-n:])
    
    def get_last(self) -> Message:
        return self._messages[-1]

    def all(self) -> List[Message]:
        return list(self._messages)

    @property
    def is_empty(self) -> bool:
        return len(self._messages) == 0
    
    @property
    def length(self) -> int:
        return len(self._messages)