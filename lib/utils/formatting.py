from lib.core.message import Message

def format_message(m: Message):
    time_str = m.timestamp.strftime("%H:%M:%S")
    return f"[{time_str}] {m.sender}: {m.content}"