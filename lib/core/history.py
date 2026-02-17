from typing import List
from lib.core.message import Message

from copy import deepcopy as clone

class History:
    def __init__(self):
        self.__messages: List[Message] = []

    def add(self, message: Message) -> None:
        self.__messages.append(message)

    def get_last_n(self, n: int) -> List[Message]:
        return list(self.__messages[-n:])
    
    def get_last(self) -> Message:
        return clone(self.__messages[-1])

    def all(self) -> List[Message]:
        return list(self.__messages)

    @property
    def is_empty(self) -> bool:
        return len(self.__messages) == 0
    
    @property
    def length(self) -> int:
        return len(self.__messages)