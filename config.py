 # API key & settings

import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Store securely in .env if using in prod
MODEL = "gpt-3.5-turbo"  # Or "gpt-4" "gpt-3.5-turbo"