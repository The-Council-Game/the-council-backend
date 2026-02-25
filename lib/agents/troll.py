from lib.core.history import History

from lib.agents.base_agent import BaseAgent


class TrollAgent(BaseAgent):
    # def __init__(self, name: str):
        # super().__init__(name=f"{name} the Troll")

    def __init__(self, name: str, llm):
        persona = (
            f"You are {name}, a troll.\n\n"

            "You are a calm conversational provocateur.\n"
            "You rarely raise your voice.\n"
            "You subtly challenge opinions in a slightly condescending way.\n"
            "You enjoy planting doubt rather than yelling.\n"
            "You speak as if you're amused, not angry.\n"
        )
    
        super().__init__(name, persona, llm)