from lib.core.history import History
from lib.core.message import Message


class Session:
    def __init__(self):
        self.history = History()

    def add_user_message(self, content: str):
        message = Message.create(sender="Human", content=content)
        self.history.add(message)

    def get_history(self):
        return self.history.all()