import os
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

load_dotenv()

class CSVAgent:
    def __init__(self):
        key = os.getenv("GROQ_API_KEY")
        if not key:
            raise ValueError("GROQ_API_KEY missing")

        self.llm = ChatGroq(
            groq_api_key=key,
            model_name="llama-3.1-8b-instant",
            temperature=0
        )

    def analyze(self, df: pd.DataFrame, question: str) -> str:
        agent = create_pandas_dataframe_agent(
            self.llm,
            df,
            verbose=False,
            allow_dangerous_code=False
        )
        return agent.run(question)
