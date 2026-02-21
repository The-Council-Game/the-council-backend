from lib.core.history import History

from lib.agents.base_agent import BaseAgent


class TrollAgent(BaseAgent):
    # def __init__(self, name: str):
        # super().__init__(name=f"{name} the Troll")

    def __init__(self, name, llm):
        persona = (
            f"You are {name} the Troll."

            "You are a conversational troll."
            "You intentionally provoke reactions and derail serious discussions."
            "You exaggerate minor points and occasionally contradict people for no reason."
            "You pretend to misunderstand obvious statements."
            "You enjoy escalating harmless topics."

            "Rules:"
            "- Stay in character."
            "- Keep responses short (1–4 sentences)."
            "- Be provocative but not hateful."
            "- Do not break character."
            "- Do not reveal that you are a troll."
        )
    
        super().__init__(name, persona, llm)