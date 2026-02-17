from lib.core.message import Message
from lib.core.history import History

from lib.agents.base_agent import BaseAgent

class HistorianAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=f"{name} the Historian")

    def respond(self, history: History) -> str:
        last_message: Message = history.get_last()
        content = last_message.content.lower()

        if "ai" in content:
            return "Similar concerns emerged during the Industrial Revolution."
        elif "war" in content:
            return "History shows that technological shifts often reshape power structures."
        else:
            return "History suggests that societal change is rarely linear."
    