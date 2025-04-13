# Core logic (command-line chatbot)

from chat_engine import ask_gpt
from memory import ConversationMemory

def main():
    memory = ConversationMemory()
    print("🤖 Welcome to your ChatGPT clone! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        memory.add_user_input(user_input)
        response = ask_gpt(memory.get())
        print(f"Bot: {response}")
        memory.add_assistant_reply(response)

if __name__ == "__main__":
    main()