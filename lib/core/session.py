from typing import List

from lib.core.history import History
from lib.core.message import Message

from lib.agents.historian import HistorianAgent
from lib.agents.freeloader import FreeloaderAgent
from lib.agents.scientist import ScientistAgent


class Session:
    def __init__(self):
        self.history = History()
        self.agents = [
            HistorianAgent("Dennis"),
            ScientistAgent("Alex"),
            FreeloaderAgent("Bob"),
        ]

    def add_user_message(self, content: str) -> None:
        message = Message.create(sender="Human", content=content)
        self.history.add(message)

    def generate_agent_replies(self) -> List[Message]:
        replies = []

        for agent in self.agents:
            response = agent.respond(self.history)
            message = Message.create(sender=agent.name, content=response)
            self.history.add(message)
            replies.append(message)

        return replies

    def get_history(self):
        return self.history.all()