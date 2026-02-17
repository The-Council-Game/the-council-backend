from lib.core.history import History
from lib.core.message import Message

from lib.agents.historian import HistorianAgent


class Session:
    def __init__(self):
        self.history = History()
        self.agent = HistorianAgent("Dennis")

    def add_user_message(self, content: str) -> None:
        message = Message.create(sender="Human", content=content)
        self.history.add(message)

    def generate_agent_reply(self) -> Message:
        response = self.agent.respond(self.history)
        message = Message.create(sender=self.agent.name, content=response)
        self.history.add(message)
        
        return message

    def get_history(self):
        return self.history.all()