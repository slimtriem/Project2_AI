# Chat logic wrapper

import openai
from config import OPENAI_API_KEY, MODEL

openai.api_key = OPENAI_API_KEY

def ask_gpt(messages):
    """
    messages: List of dicts like {"role": "user", "content": "Hello"}
    """
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message["content"]