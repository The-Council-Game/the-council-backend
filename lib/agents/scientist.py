from lib.core.message import Message
from lib.core.history import History

from lib.agents.base_agent import BaseAgent


class ScientistAgent(BaseAgent):
    def __init__(self, name: str, llm):
        persona = (
            f"You are {name}, a rational scientist.\n\n"

            "You prioritize evidence, mechanisms, and logical consistency.\n"
            "You challenge claims politely but firmly.\n"
            "You avoid emotional language and focus on facts.\n"
        )

        super().__init__(name, persona, llm)