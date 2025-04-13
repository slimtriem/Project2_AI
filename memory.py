 # Optional: store conversation history


class ConversationMemory:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    def add_user_input(self, input_text):
        self.messages.append({"role": "user", "content": input_text})

    def add_assistant_reply(self, reply_text):
        self.messages.append({"role": "assistant", "content": reply_text})

    def get(self):
        return self.messages