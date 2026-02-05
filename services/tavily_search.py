import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

class TavilySearch:
    def __init__(self):
        key = os.getenv("TAVILY_API_KEY")
        if not key:
            raise ValueError("TAVILY_API_KEY missing")

        self.client = TavilyClient(api_key=key)

    def search(self, query: str, k: int = 5):
        res = self.client.search(query=query, max_results=k)

        return [
            {
                "title": r["title"],
                "content": r["content"],
                "url": r["url"],
            }
            for r in res["results"]
        ]
