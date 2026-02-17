from lib.core.history import History

from lib.agents.base_agent import BaseAgent


class FreeloaderAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=f"{name} the Freeloader")

    def respond(self, history: History) -> str:
        return "Wrong, I think you should do your research buddy :)"