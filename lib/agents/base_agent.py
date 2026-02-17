class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def respond(self, history):
        raise NotImplementedError