import random
from typing import List, TypedDict, Dict

from lib.core.history import History
from lib.core.message import Message

from lib.agents import (
    BaseAgent, Activation,
    HistorianAgent, ScientistAgent, TrollAgent
)

# class GameState(TypedDict):
#     history: History
#     activation_threshold: float
#     strong_activation_threshold: float,
#     agent_names: list[str]

class Session:
    def __init__(self, llm):
        self.agents: Dict[int, BaseAgent] = {
            0: TrollAgent(name="Bob", llm=llm),
            1: HistorianAgent(name="Aurelius", llm=llm),
            2: ScientistAgent(name="Vega", llm=llm)
        }

        agent_names = [x.name for x in self.agents.values()]

        self.state = {
            "history": History(),
            "activation_threshold": 0.5,
            "strong_activation_threshold": 0.8,
            "agent_names": agent_names
        }
    
    @property
    def history(self):
        return self.state["history"]
    
    @property
    def activation_threshold(self):
        return self.state["activation_threshold"]
    
    @property
    def strong_activation_threshold(self):
        return self.state["strong_activation_threshold"]

    def add_user_message(self, content: str) -> None:
        message = Message.create(sender="Human", content=content)
        self.history.add(message)

    def show_decision_debug_message(self, decisions):
        for aid, act in decisions.items():
            msg = (
                f" -- (DEBUG) -- {self.agents[aid].name} decided {"not " if act.priority < self.activation_threshold else ""}to speak.\n"
                f" -- (DEBUG) -- Priority: {act.priority}\n"
                f" -- (DEBUG) -- Reason: {act.reason}"
            )

            print(msg)

    def generate_agent_replies(self) -> List[Message]:
        replies = []
        decisions = {
            agent_id: self.agents[agent_id].score_activation(self.state, n=20) for agent_id in self.agents
        }
        
        self.show_decision_debug_message(decisions)

        strong = {
            aid: dec for aid, dec in decisions.items() 
            if dec.priority >= self.strong_activation_threshold
        }
        
        reluctant = {
            aid: dec for aid, dec in decisions.items() 
            if aid not in strong and dec.priority >= self.activation_threshold
        }

        for aid in strong:
            agent = self.agents[aid]

            response = agent.respond(self.state, decisions[aid], n=20)
            message = Message.create(sender=agent.name, content=response.message)

            self.history.add(message)
            replies.append(message)

        selected_aid = max(reluctant, key=lambda k: reluctant[k].priority) if reluctant else None
        if selected_aid is not None:
            selected_agent = self.agents[selected_aid]
            print(f" -- (DEBUG) -- Selected Reluctant Agent: {selected_agent.name}")
            
            response = selected_agent.respond(self.state, decisions[selected_aid], n=20)
            message = Message.create(sender=selected_agent.name, content=response.message)

            self.history.add(message)
            replies.append(message)

        return replies

    def get_history(self):
        return self.history.all()