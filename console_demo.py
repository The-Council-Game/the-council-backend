import sys

from langchain_ollama import ChatOllama

from lib.core.session import Session as GameSession
from lib.utils.formatting import format_message

def clear_last_line():
    # Move cursor up one line
    sys.stdout.write("\033[F")

    # Clear the entire line
    sys.stdout.write("\033[2K")
    sys.stdout.flush()

def run_console():
    llm = ChatOllama(model="llama3:8b")
    session = GameSession(llm=llm)

    print("=== PolyAgent Console ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        clear_last_line()
        if user_input.lower() in {"exit", "quit"}:
            print("\nSession ended.")
            break

        if not user_input:
            continue
        
        session.add_user_message(user_input)
        human_msg = session.history.get_last()
        print(format_message(human_msg))

        # Generate all agent replies
        bot_messages = session.generate_agent_replies()

        for bot_msg in bot_messages:
            print(format_message(bot_msg))

if __name__ == "__main__":
    run_console()
