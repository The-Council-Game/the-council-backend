import sys

from lib.core.session import Session as GameSession
from lib.utils.formatting import format_message

def clear_last_line():
    # Move cursor up one line
    sys.stdout.write("\033[F")

    # Clear the entire line
    sys.stdout.write("\033[2K")
    sys.stdout.flush()

def run_console():
    session = GameSession()

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
        
        # Add to session
        session.add_user_message(user_input)

        # Get last message only
        last_message = session.history.get_last()

        # Print like chat
        print(format_message(last_message))


if __name__ == "__main__":
    run_console()
