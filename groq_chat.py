import os
from groq import Groq
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class GroqChat:
    def __init__(self):
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise ValueError("GROQ_API_KEY missing")

        self.client = Groq(api_key=key)
        self.model = "llama-3.1-8b-instant"

    def chat(self, user_message: str, history: List[Dict] = None) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful AI assistant"}
        ]

        if history:
            messages.extend(history[-5:])

        messages.append({"role": "user", "content": user_message})

        res = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )

        return res.choices[0].message.content
