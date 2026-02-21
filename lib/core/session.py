from typing import List, TypedDict

from lib.core.history import History
from lib.core.message import Message

from lib.agents.base_agent import BaseAgent, Activation
# from lib.agents.historian import HistorianAgent
# from lib.agents.scientist import ScientistAgent
from lib.agents.troll import TrollAgent

class GameState(TypedDict):
    history: History
    activation_threshold: float

class Session:
    def __init__(self, llm):
        self.state: GameState = {
            "history": History(),
            "activation_threshold": 0.5
        }

        self.agents: List[BaseAgent] = [
            TrollAgent(name="Bob", llm=llm),
        ]
    
    @property
    def history(self):
        return self.state["history"]
    
    @property
    def activation_threshold(self):
        return self.state["activation_threshold"]

    def add_user_message(self, content: str) -> None:
        message = Message.create(sender="Human", content=content)
        self.history.add(message)

    def show_decision_debug_message(self, decisions: List[Activation]):
        for i, act in enumerate(decisions):
            msg = (
                f" -- (DEBUG) -- {self.agents[i].name} decided {"not " if not act.priority >= self.activation_threshold else ""}to speak.\n"
                f" -- (DEBUG) -- Priority: {act.priority}\n"
                f" -- (DEBUG) -- Reason: {act.reason}"
            )

            print(msg)

    def generate_agent_replies(self) -> List[Message]:
        replies = []
        decisions = [
            agent.score_activation(self.state, n=20) for agent in self.agents
        ]
        
        self.show_decision_debug_message(decisions)

        for i, agent in enumerate(self.agents):
            if not decisions[i].priority >= self.activation_threshold:
                continue

            response = agent.respond(self.history, decisions[i], n=20)
            message = Message.create(sender=agent.name, content=response.message)
            
            self.history.add(message)
            replies.append(message)

        return replies

    def get_history(self):
        return self.history.all()