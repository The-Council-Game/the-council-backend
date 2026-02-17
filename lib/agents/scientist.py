from lib.core.message import Message
from lib.core.history import History

from lib.agents.base_agent import BaseAgent


class ScientistAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=f"{name} the Scientist")

    def respond(self, history: History) -> str:
        last_message: Message = history.get_last()
        content = last_message.content.lower()

        if "ai" in content:
            return "There is currently no conclusive empirical evidence supporting that claim."
        elif "climate" in content:
            return "Scientific consensus indicates measurable long-term trends."
        else:
            return "A proper conclusion requires controlled evidence and reproducibility."